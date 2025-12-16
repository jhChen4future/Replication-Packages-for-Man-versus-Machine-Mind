from otree.api import *
from otree.constants import participant_label

c = cu
doc = '\nThis is a standard 2-player trust game where the amount sent by player 1 gets\ntripled. The trust game was first proposed by\n<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">\n    Berg, Dickhaut, and McCabe (1995)\n</a>.\n'
class C(BaseConstants):
    NAME_IN_URL = 'trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(20)
    MULTIPLIER = 3
    INSTRUCTIONS_TEMPLATE = 'trust/instructions.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    sent_amount = models.CurrencyField(doc='赠送点数', label='请输入一个0-20间的整数', max=C.ENDOWMENT, min=0)
    sent_back_amount = models.CurrencyField(doc='返还点数', label='请输入整数',min=0)
def sent_back_amount_max(group: Group):
    return group.sent_amount * C.MULTIPLIER
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount
class Player(BasePlayer):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    Train1 = models.IntegerField(
        label='问题1：假设角色A将10个点数赠送给B。请问B最多返还多少点数给A？')
    Train2 = models.IntegerField(
        label='问题2：假设角色A将10个点数赠送给B。请问B最少返还多少点数给A？')
    Train3 = models.IntegerField(
        label='问题3：假设角色A将10个点数赠送给B。B返还15个点数给A。请问A本轮游戏最终收入是多少点数？')
    Train4 = models.IntegerField(
        label='问题4：假设角色A将10个点数赠送给B。B返还15个点数给A。请问B本轮游戏最终收入是多少点数？')
    ''''
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
    form_fields = ['Train1', 'Train2','Train3', 'Train4']
    @staticmethod
    def error_message(player: Player, values):
        if values['Train1'] != 30:
            return "您问题1的答案错误，请您重新输入"
        if values['Train2'] != 0:
            return "您问题2的答案错误，请您重新输入"
        if values['Train3'] != 25:
            return "您问题3的答案错误，请您重新输入"
        if values['Train4'] != 15:
            return "您问题4的答案错误，请您重新输入"
class WaitforStart(WaitPage):
    wait_for_all_groups = True
class Introduction(Page):
    form_model = 'player'
class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group == 1
class SendBackWaitPage(WaitPage):
    pass
class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group == 2
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        tripled_amount = group.sent_amount * C.MULTIPLIER
        return dict(tripled_amount=tripled_amount)
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Waitforallgroups(WaitPage):
    wait_for_all_groups = True
class Results(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.payoff = player.payoff + participant.payoff
        if player.round_number == C.NUM_ROUNDS:
            participant.trust = player.payoff
    def vars_for_template(player: Player):
        group = player.group
        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)
page_sequence = [LabelInitiate,Introduction, Train, WaitforStart,  LabelResults, Send, SendBackWaitPage, SendBack, ResultsWaitPage, Waitforallgroups, Results]