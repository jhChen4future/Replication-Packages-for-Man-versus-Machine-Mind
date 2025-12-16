###indefinite parameters
import random
stop_p = 0.25
rounds = 1
i=random.random()

from otree.api import *
c = cu

doc = ''
class Constants(BaseConstants):
    name_in_url = 'RD3'
    players_per_group = 2
    while i>stop_p:
        rounds = rounds+1
        i = random.random()
    if rounds > 10:
        rounds = 10
    num_rounds = rounds
    both_cooperate_payoff = 30
    both_defect_payoff = 20
    sucker_payoff = 10
    defector_payoff = 40
    INSTRUCTIONS_TEMPLATE = 'Repeated_PD3/instructions.html'

class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    for p in group.get_players():
        set_payoff(p)
class Group(BaseGroup):
    Player_1_Round_Payoff = models.CurrencyField(initial=0)
    Player_2_Round_Payoff = models.CurrencyField(initial=0)
    Player_1_decision = models.StringField(choices=[['A', 'A'], ['B', 'B']], label='', widget=widgets.RadioSelect)
    Player_2_decision = models.StringField(choices=[['A', 'A'], ['B', 'B']], label='', widget=widgets.RadioSelect)
def other_player(player):
    group = player.group
    return player.get_others_in_group()[0]
def set_payoff(player):
    group = player.group
    if player.round_number == 1:
        player.Total_payoff = 0
    else:
        prev_player = player.in_round(player.round_number - 1)
        player.Total_payoff = prev_player.Total_payoff
    if player.id_in_group == 1:
        if group.Player_1_decision == "A":
            if group.Player_2_decision == "A":
                player.R1_payoff = Constants.both_cooperate_payoff
                player.Total_payoff = player.Total_payoff + Constants.both_cooperate_payoff
            else:
                player.R1_payoff = Constants.sucker_payoff
                player.Total_payoff = player.Total_payoff + Constants.sucker_payoff
        else:
            if group.Player_2_decision == "A":
                player.R1_payoff = Constants.defector_payoff
                player.Total_payoff = player.Total_payoff + Constants.defector_payoff
            else:
                player.R1_payoff = Constants.both_defect_payoff
                player.Total_payoff = player.Total_payoff + Constants.both_defect_payoff
    if player.id_in_group == 2:
        if group.Player_2_decision == "A":
            if group.Player_1_decision == "A":
                player.R1_payoff = Constants.both_cooperate_payoff
                player.Total_payoff = player.Total_payoff + Constants.both_cooperate_payoff
            else:
                player.R1_payoff = Constants.sucker_payoff
                player.Total_payoff = player.Total_payoff + Constants.sucker_payoff
        else:
            if group.Player_1_decision == "A":
                player.R1_payoff = Constants.defector_payoff
                player.Total_payoff = player.Total_payoff + Constants.defector_payoff
            else:
                player.R1_payoff = Constants.both_defect_payoff
                player.Total_payoff = player.Total_payoff + Constants.both_defect_payoff
    player.payoff = player.R1_payoff
class Player(BasePlayer):
    R1_payoff = models.CurrencyField(initial=0)
    Total_payoff = models.CurrencyField(initial=0)
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    Train1 = models.IntegerField(
        label='问题1：玩家1选择A，玩家B选择B，玩家A本轮的收入是多少？')
    Train2 = models.IntegerField(
        label='问题2：玩家1选择A，玩家B选择A，玩家B本轮的收入是多少？')
    Train3 = models.IntegerField(
        label='问题3：玩家1选择B，玩家B选择A，玩家A本轮的收入是多少？')
    Train4 = models.IntegerField(
        label='问题4：玩家1选择B，玩家B选择B，玩家B本轮的收入是多少？')
    round_to_pay = models.IntegerField()
def creating_session(subsession:Subsession):
    if subsession.round_number == 1:
        subsession.group_randomly()
    else:
        subsession.group_like_round(1)
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
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
class LabelResults(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(),
        )
    def is_displayed(player):
        return player.round_number == 1
class Train(Page):
    form_model = 'player'
    form_fields = ['Train1', 'Train2','Train3', 'Train4']
    @staticmethod
    def error_message(player: Player, values):
        if values['Train1'] != 10:
            return "您问题1的答案错误，请您重新输入"
        if values['Train2'] != 30:
            return "您问题2的答案错误，请您重新输入"
        if values['Train3'] != 40:
            return "您问题3的答案错误，请您重新输入"
        if values['Train4'] != 20:
            return "您问题4的答案错误，请您重新输入"
class WaitforStart(WaitPage):
    wait_for_all_groups = True
class Introduction(Page):
    form_model = 'player'
    #timeout_seconds = 100
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
class Decision_R1_P1(Page):
    form_model = 'group'
    form_fields = ['Player_1_decision']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1
class Decision_R1_P2(Page):
    form_model = 'group'
    form_fields = ['Player_2_decision']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2
class R1_WaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Waitforallgroups(WaitPage):
    wait_for_all_groups = True
class Results_Page_R1(Page):
    form_model = 'group'
    '''这是pd在最后一轮时，随机抽取一轮作为最终收入的代码
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if player.round_number == Constants.num_rounds:
            player.round_to_pay = random.randint(1,Constants.num_rounds)
            prev_player = player.in_round(player.round_to_pay)
            player.payoff = prev_player.payoff
            participant.pd2 = player.payoff
            participant.pd2_round = player.round_to_pay
    '''
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if player.round_number == 1:
            participant.pd3 = 0
            participant.pd3 = participant.pd3 + player.payoff
        else:
            participant.pd3 = player.payoff + participant.pd3
        print(participant.pd3)
        print(player.payoff)
class Results_round(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

page_sequence = [LabelInitiate, WaitforStart, LabelResults,  Decision_R1_P1, Decision_R1_P2, R1_WaitPage, Waitforallgroups, Results_Page_R1, Results_round]