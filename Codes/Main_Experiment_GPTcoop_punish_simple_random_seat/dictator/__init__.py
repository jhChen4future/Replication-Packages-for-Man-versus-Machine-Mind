
from otree.api import *
c = cu

doc = '\nOne player decides how to divide a certain amount between himself and the other\nplayer.\nSee: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness\nand the assumptions of economics." Journal of business (1986):\nS285-S300.\n'
class C(BaseConstants):
    NAME_IN_URL = 'dictator'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(20)
    INSTRUCTIONS_TEMPLATE = 'dictator/instructions.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    kept = models.CurrencyField(doc='Amount dictator decided to keep for himself', label='我选择保留', max=C.ENDOWMENT, min=0)
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = group.kept
    p2.payoff = C.ENDOWMENT - group.kept
class Player(BasePlayer):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',
                                widget=widgets.RadioSelect)
    Train1 = models.IntegerField(
        label='问题1：假设角色A提议将10个点数给B。请问A的最终收入是多少？')
    Train2 = models.IntegerField(
        label='问题2：假设角色A提议将10个点数给B。请问B的最终收入是多少？')
    Train3 = models.IntegerField(
        label='问题3：假设角色A提议将0个点数给B。请问A的最终收入是多少？')
    Train4 = models.IntegerField(
        label='问题4：假设角色A提议将0个点数给B。请问B的最终收入是多少？')
'''
def creating_session(subsession:Subsession):
    if subsession.round_number == 1:
        subsession.group_randomly()
    else:
        subsession.group_like_round(1)
'''
def set_labels(group:Group):
    for p in group.get_players():
        participant = p.participant
        p.label1 = participant.label1
class LabelInitiate(WaitPage):
    after_all_players_arrive = set_labels
class Label1(Page):
    form_model = 'player'
    form_fields = ['label1']
class LabelWaitPage(WaitPage):
    pass
class LabelResults(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(),
        )
class Train(Page):
    form_model = 'player'
    form_fields = ['Train1', 'Train2', 'Train3', 'Train4']
    @staticmethod
    def error_message(player: Player, values):
        if values['Train1'] != 10:
            return "您问题1的答案错误，请您重新输入"
        if values['Train2'] != 10:
            return "您问题2的答案错误，请您重新输入"
        if values['Train3'] != 20:
            return "您问题3的答案错误，请您重新输入"
        if values['Train4'] != 0:
            return "您问题4的答案错误，请您重新输入"
class WaitforStart(WaitPage):
    wait_for_all_groups = True
class Introduction(Page):
    form_model = 'player'
class Offer(Page):
    form_model = 'group'
    form_fields = ['kept']
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group == 1
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Waitforallgroups(WaitPage):
    wait_for_all_groups = True
class Results(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if player.round_number == C.NUM_ROUNDS:
            participant.dictator = player.payoff
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(offer=C.ENDOWMENT - group.kept)
page_sequence = [LabelInitiate, Introduction, Train, LabelResults, WaitforStart, Offer, ResultsWaitPage, Waitforallgroups,Results]