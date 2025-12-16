from otree.api import *
c = cu

doc = '\n这是游戏3.一个玩家将做出一个提议，另一名玩家选择接受或拒绝该提议。'
class Constants(BaseConstants):
    name_in_url = 'Ultimatum'
    players_per_group = 2
    num_rounds = 1
    endowment = 20
    INSTRUCTIONS_TEMPLATE = 'Ultimatum/instructions.html'
class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    for p in group.get_players():
        set_payoff(p)
class Group(BaseGroup):
    proposal = models.IntegerField(max=Constants.endowment, label='提议',min=0)
    response = models.StringField(choices=[['接受', '接受'], ['拒绝', '拒绝']],label='选择',widget=widgets.RadioSelect)
def other_player(player):
    group = player.group
    return player.get_others_in_group()[0]
def set_payoff(player):
    group = player.group
    if player.id_in_group == 1:
        if group.response == "接受":
            player.payoff = Constants.endowment - group.proposal
        else:
            player.payoff = 0
    else:
        if group.response == "接受":
            player.payoff = group.proposal
        else:
            player.payoff = 0
class Player(BasePlayer):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    Train1_Proposer = models.IntegerField(
        label='问题1：假设提议者A提议将1点数赠送给响应者B，响应者B接受了这一提议。请问提议者A获得多少实验点数报酬？')
    Train2_Proposer = models.IntegerField(
        label='问题2：假设提议者A提议将1点数赠送给响应者B，响应者B拒绝了这一提议。请问提议者A获得多少实验点数报酬？')
    Train1_Responder = models.IntegerField(
        label='问题3：假设提议者A提议将1点数赠送给响应者B，响应者B接受了这一提议。请问响应者B获得多少实验点数报酬？')
    Train2_Responder = models.IntegerField(
        label='问题4：假设提议者A提议将1点数赠送给响应者B，响应者B拒绝了这一提议。请问响应者B获得多少实验点数报酬？')
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
class Introduction(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

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
class Train_Proposer(Page):
    form_model = 'player'
    form_fields = ['Train1_Proposer', 'Train2_Proposer','Train1_Responder', 'Train2_Responder']
    @staticmethod
    def error_message(player: Player, values):
        if values['Train1_Proposer'] != 19:
            return "您问题1的答案错误，请您重新输入"
        if values['Train2_Proposer'] != 0:
            return "您问题2的答案错误，请您重新输入"
        if values['Train1_Responder'] != 1:
            return "您问题3的答案错误，请您重新输入"
        if values['Train2_Responder'] != 0:
            return "您问题4的答案错误，请您重新输入"
class WaitforStart(WaitPage):
    wait_for_all_groups = True
class Proposer(Page):
    form_model = 'group'
    form_fields = ['proposal']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1
class WaitForP1C1(WaitPage):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2
class Reciever(Page):
    form_model = 'group'
    form_fields = ['response']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2
class WaitForP2C2(WaitPage):
    @staticmethod
    def is_displayed(player):
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
        if player.round_number == Constants.num_rounds:
            participant.ultimatum = player.payoff
page_sequence = [LabelInitiate, Introduction, Train_Proposer, WaitforStart, LabelResults, Proposer, WaitForP1C1, Reciever, WaitForP2C2, ResultsWaitPage, Results]