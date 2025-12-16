from otree.api import *
c = cu
import random
RandomOption = random.randint(1, 2)


class C(BaseConstants):
    NAME_IN_URL = 'lottery'
    PLAYERS_PER_GROUP = 1
    NUM_ROUNDS = 1
    option = RandomOption
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    lottery = models.StringField(choices=[['L1','A=18,         B=18'],['L2','A=22,         B=15'],['L3','A=26,         B=12'],['L4','A=30,         B=9'],['L5','A=34,        B=6'],['L6','A=37,         B=2']],
                                  label='请选择一个选项，你有50%概率获得A的值，50%概率获得B的值', widget=widgets.RadioSelect)
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    Train1 = models.FloatField(
        label='问题1：假设角色1选择了选项2，有多大的概率能获得18点数？（请输入小数）')
    Train2 = models.IntegerField(
        label='问题2：假设角色1选择了选项3，且计算机抽取的是结果A，角色1本游戏的收入是多少？')
def other_player(player):
    group = player.group
    return player.get_others_in_group()[0]
def creating_session(subsession:Subsession):
    subsession.group_randomly()
def set_payoff(player: Player):
    lottery_values = {
            "L1": (18, 18),
            "L2": (22, 15),
            "L3": (26, 12),
            "L4": (30, 9),
            "L5": (34, 6),
            "L6": (37, 2),
        }
    a_value, b_value = lottery_values.get(player.lottery, (0, 0))
    participant = player.participant
    if C.option == 1:
        player.payoff = a_value
        participant.lottery = a_value
    elif C.option == 2:
        player.payoff = b_value
        participant.lottery = b_value
    else:
        player.payoff = -10000  # 若 option 异常，则设置为 0 或其他默认值
    print(a_value)

def set_payoffs(group):
    for p in group.get_players():
        set_payoff(p)

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

class LabelResults(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(),
        )
class Train(Page):
    form_model = 'player'
    form_fields = ['Train1', 'Train2']
    @staticmethod
    def error_message(player: Player, values):
        if values['Train1'] != 0.5  :
            return "您问题1的答案错误，请您重新输入"
        if values['Train2'] != 26:
            return "您问题2的答案错误，请您重新输入"
class WaitforStart(WaitPage):
    wait_for_all_groups = True

class DecisionYou(Page):
    form_model = 'player'
    form_fields = ['lottery']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
    #@staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     participant = player.participant
    #     if player.round_number == C.num_rounds:
    #         participant.ultimatum = player.payoff
page_sequence = [LabelInitiate, Introduction,  Train, WaitforStart, LabelResults, DecisionYou, ResultsWaitPage, Results]