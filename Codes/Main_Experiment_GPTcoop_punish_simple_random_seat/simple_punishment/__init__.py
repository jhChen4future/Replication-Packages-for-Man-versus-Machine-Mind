from otree.api import *
import random

doc = """
Public goods with punishment, roughly based on Fehr & Gaechter 2000. 
"""


class Constants(BaseConstants):
    name_in_url = 'simp_show'
    players_per_group = 4
    num_rounds = 20
    endowment = cu(20)
    multiplier = 1.6
    max_punishment = 10
    max_payoff = endowment * multiplier
    INSTRUCTIONS_TEMPLATE = 'simple_punishment/instructions.html'
    punishment_schedule = {
        0: 0,
        1: 1,
        2: 2,
        3: 4,
        4: 6,
        5: 9,
        6: 12,
        7: 16,
        8: 20,
        9: 25,
        10: 30,
    }



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


def make_punishment_field(id_in_group):
    return models.IntegerField(
        min=0, max=Constants.max_punishment, label="Punishment to player {}".format(id_in_group)
    )


class Player(BasePlayer):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']],label='',widget=widgets.RadioSelect)
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, label="本轮您想投入多少?"
    )
    Train1 = models.IntegerField(
        label='问题1：玩家1投入0点数至小组公共账户，玩家2投入5点数，玩家3投入10点数，玩家4投入15点数，请问本轮玩家1的最终收入是？')
    Train2 = models.IntegerField(
        label='问题2：玩家1投入0点数至小组公共账户，玩家2投入5点数，玩家3投入10点数，玩家4投入15点数，请问本轮玩家2的最终收入是？')
    Train3 = models.IntegerField(
        label='问题3：玩家1投入0点数至小组公共账户，玩家2投入5点数，玩家3投入10点数，玩家4投入15点数，请问本轮玩家3的最终收入是？')
    Train4 = models.IntegerField(
        label='问题4：玩家1投入0点数至小组公共账户，玩家2投入5点数，玩家3投入10点数，玩家4投入15点数，请问本轮玩家4的最终收入是？')
    round_to_pay = models.IntegerField()
    '''
    punish_p1 = make_punishment_field(1)
    punish_p2 = make_punishment_field(2)
    punish_p3 = make_punishment_field(3)
    punish_p4 = make_punishment_field(4)
    self_cost_of_punishment = models.CurrencyField()
    punishment_received = models.CurrencyField()

def get_self_field(player: Player):
    return 'punish_p{}'.format(player.id_in_group)


def punishment_fields(player: Player):
    fields = ['punish_p1', 'punish_p2', 'punish_p3', 'punish_p4']
    # can't punish yourself
    fields.remove(get_self_field(player))
    return fields

'''
'''
def creating_session(subsession:Subsession):
    if subsession.round_number == 1:
        subsession.group_randomly()
    else:
        subsession.group_like_round(1)
'''
def set_identification(group:Group):
    players = group.get_players()
    for p in players:
        p.label1 = p.in_round(1).label1
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * Constants.multiplier / Constants.players_per_group
    )

    for p in players:
        payoff_before_punishment = Constants.endowment - p.contribution + group.individual_share
        '''
        self_field = get_self_field(p)
        punishments_received = [getattr(other, self_field) for other in p.get_others_in_group()]
        p.punishment_received = min(10, sum(punishments_received))
        punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
        p.self_cost_of_punishment = sum(
            Constants.punishment_schedule[points] for points in punishments_sent
        )
        p.payoff = (
            payoff_before_punishment * (1 - p.punishment_received / 10) - p.self_cost_of_punishment
        )
        '''
        p.payoff = payoff_before_punishment


# PAGES
def set_labels(group:Group):
    for p in group.get_players():
        participant = p.participant
        p.label1 = participant.label1
class LabelInitiate(WaitPage):
    after_all_players_arrive = set_labels
class Label1(Page):
    form_model = 'player'
    form_fields = ['label1']
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
class LabelWaitPage(WaitPage):
    pass
class LabelResults(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(),
            schedule=Constants.punishment_schedule.items(),
        )
class Train(Page):
    form_model = 'player'
    form_fields = ['Train1', 'Train2','Train3', 'Train4']
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    def error_message(player: Player, values):
        if values['Train1'] != 32:
            return "您问题1的答案错误，请您重新输入"
        if values['Train2'] != 27:
            return "您问题2的答案错误，请您重新输入"
        if values['Train3'] != 22:
            return "您问题3的答案错误，请您重新输入"
        if values['Train4'] != 17:
            return "您问题4的答案错误，请您重新输入"
class WaitforStart(WaitPage):
    wait_for_all_groups = True
class Introduction(Page):
    form_model = 'player'
    #timeout_seconds = 100
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
class Introduction2(Page):
    form_model = 'player'
    #timeout_seconds = 100
    @staticmethod
    def is_displayed(player):
        return player.round_number == 11
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

class WaitPage1(WaitPage):
    pass
    @staticmethod
    def is_displayed(player):
        return player.round_number <11

class WaitPage2(WaitPage):
    after_all_players_arrive = set_identification
    @staticmethod
    def is_displayed(player):
        return player.round_number >10

class IndividualResults(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):

        return dict(
            other_players=player.get_others_in_group(),
            #schedule=Constants.punishment_schedule.items(),
        )
    def is_displayed(player):
        return player.round_number >10

class IndividualResults2(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        other_players1 = player.get_others_in_group()
        other_players1 = sorted(other_players1, key=lambda player: player.contribution, reverse=True)
        return dict(other_players=other_players1)
    def is_displayed(player):
        return player.round_number <11

class WaitPage3(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    pass
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if player.round_number == 1:
            participant.simple_punishment = 0
            participant.simple_punishment = participant.simple_punishment + player.payoff
        else:
            participant.simple_punishment = player.payoff + participant.simple_punishment
        if player.round_number == Constants.num_rounds:
            player.payoff = participant.simple_punishment
        print(participant.simple_punishment)
        print(player.payoff)


'''     
            player.round_to_pay = random.randint(1, Constants.num_rounds)
            prev_player = player.in_round(player.round_to_pay)
            player.payoff = prev_player.payoff
            participant.simple_punishment = player.payoff
            participant.payoff = participant.trust + participant.ultimatum + participant.pd + participant.dictator + participant.simple_punishment

class WaitforPay(WaitPage):
    #after_all_players_arrive = set_final_payoff
    def is_displayed(player):
        return player.round_number == 20
'''
class FinalPayoff(Page):
    pass
    @staticmethod
    def is_displayed(player):
        return player.round_number == 20

page_sequence = [LabelInitiate,
                 Introduction,
                 Introduction2,
                 Train,
                 WaitforStart,
LabelResults,
    Contribute,
    WaitPage1,
                WaitPage2,
    IndividualResults,
                IndividualResults2,
    WaitPage3,
    Results,
    #WaitforPay,
    FinalPayoff
]