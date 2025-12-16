from otree.api import *
c = cu
import random


#role is changed into position due to reserved letter

class C(BaseConstants):
    NAME_IN_URL = 'pd3'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    R1_1A2C = 65
    R1_1A2D = 20
    R1_1B2E = 80
    R1_1B2F = 25
    R2_1A2C = 65
    R2_1A2D = 80
    R2_1B2E = 20
    R2_1B2F = 25
    Role1Player = random.randint(1, 2)
    QSR = 2
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    player_1_position1 = models.StringField()
    player_1_position2 = models.StringField()
    player_1_position3 = models.StringField()
    player_2_position1 = models.StringField()
    player_2_position2 = models.StringField()
    player_2_position3 = models.StringField()
class Player(BasePlayer):
    YouRole1 = models.StringField(choices=[['A','A'],['B','B']], label='若你是角色1，你会选择哪个决策', widget=widgets.RadioSelect)
    YouRole2 = models.StringField(choices=[['C','C'],['D','D']],label='若你是角色2，对手选择了A的条件下，你会选择哪个决策', widget=widgets.RadioSelect)
    YouRole3 = models.StringField(choices=[['E','E'],['F','F']], label='若你是角色2，对手选择了B的条件下，你会选择哪个决策', widget=widgets.RadioSelect)
    OppoRole1A = models.FloatField(max=1, min=0, label="若你的对手是角色1，你认为其有多大概率选择A（请输入小数）")
    OppoRole1B = models.FloatField(max=1, min=0, label="若你的对手是角色1，你认为其有多大概率选择B（请输入小数）")
    OppoRole2C = models.FloatField(max=1, min=0, label="若你的对手是角色2（假设你已选择了A），你认为其有多大概率选择C（请输入两位小数）")
    OppoRole2D = models.FloatField(max=1, min=0, label="若你的对手是角色2（假设你已选择了A），你认为其有多大概率选择D（请输入两位小数）")
    OppoRole2E = models.FloatField(max=1, min=0, label="若你的对手是角色2（假设你已选择了B），你认为其有多大概率选择E（请输入两位小数）")
    OppoRole2F = models.FloatField(max=1, min=0, label="若你的对手是角色2（假设你已选择了B），你认为其有多大概率选择F（请输入两位小数）")
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    X1X2 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果你选择A，对手选择C，你的收入为{C.R1_1A2C}，对手收入为{C.R2_1A2C}', widget=widgets.RadioSelect)
    X3X4 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果你选择A，对手选择D，你的收入为{C.R1_1A2D}，对手收入为{C.R2_1A2D}', widget=widgets.RadioSelect)
    Y1Y2 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果你选择B，对手选择E，你的收入为{C.R1_1B2E}，对手收入为{C.R2_1B2E}', widget=widgets.RadioSelect)
    Y3Y4 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果你选择B，对手选择F，你的收入为{C.R1_1B2F}，对手收入为{C.R2_1B2F}', widget=widgets.RadioSelect)
    X2X1 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果对手选择A，你选择C，你的收入为{C.R2_1A2C}，对手收入为{C.R1_1A2C}', widget=widgets.RadioSelect)
    X4X3 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果对手选择A，你选择D，你的收入为{C.R2_1A2D}，对手收入为{C.R1_1A2D}', widget=widgets.RadioSelect)
    Y2Y1 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果对手选择B，你选择E，你的收入为{C.R2_1B2E}，对手收入为{C.R1_1B2E}', widget=widgets.RadioSelect)
    Y4Y3 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果对手选择B，你选择F，你的收入为{C.R2_1B2F}，对手收入为{C.R1_1B2F}', widget=widgets.RadioSelect)
    position = models.IntegerField()
def other_player(player):
    group = player.group
    return player.get_others_in_group()[0]

def creating_session(subsession:Subsession):
    subsession.group_randomly()

def set_payoff(player: Player):
    group = player.group
    if player.id_in_group == 1:
        if player.position == 1:
            if player.YouRole1 == "A":
                if group.player_2_position2 == "C":
                    player.payoff = C.R1_1A2C
                else:
                    player.payoff = C.R1_1A2D
            else:
                if group.player_2_position3 == "E":
                    player.payoff = C.R1_1B2E
                else:
                    player.payoff = C.R1_1B2F
        else:
            if group.player_2_position1 == "A":
                if player.YouRole2 == "C":
                    player.payoff = C.R2_1A2C
                else:
                    player.payoff = C.R2_1A2D
            else:
                if player.YouRole3 == "E":
                    player.payoff = C.R2_1B2E
                else:
                    player.payoff = C.R2_1B2F
    else:
        if player.position == 1:
            if player.YouRole1 == "A":
                if group.player_1_position2 == "C":
                    player.payoff = C.R1_1A2C
                else:
                    player.payoff = C.R1_1A2D
            else:
                if group.player_1_position3 == "E":
                    player.payoff = C.R1_1B2E
                else:
                    player.payoff = C.R1_1B2F
        else:
            if group.player_1_position1 == "A":
                if player.YouRole2 == "C":
                    player.payoff = C.R2_1A2C
                else:
                    player.payoff = C.R2_1A2D
            else:
                if player.YouRole3 == "E":
                    player.payoff = C.R2_1B2E
                else:
                    player.payoff = C.R2_1B2F
    participant = player.participant
    participant.pd3payoff = player.payoff

def set_payoffs(group):
    for p in group.get_players():
        set_payoff(p)

def set_guess_payoffs(group:Group):
    for play in group.get_players():
        guess1 = float(0)
        guess2 = float(0)
        guess3 = float(0)
        p_Role1A = play.OppoRole1A
        p_Role1B = play.OppoRole1B
        p_Role2C = play.OppoRole2C
        p_Role2D = play.OppoRole2D
        p_Role2E = play.OppoRole2E
        p_Role2F = play.OppoRole2F
        for p in play.get_others_in_group():
            if p.YouRole1 == "A":
                guess1 = 20 * max(0, 1 - C.QSR * (1 - p_Role1A) ** 2)
            else:
                guess1 = 20 * max(0, 1 - C.QSR * (1 - p_Role1B) ** 2)
            if p.YouRole2 == "C":
                guess2 = 20 * max(0, 1 - C.QSR * (1 - p_Role2C) ** 2)
            else:
                guess2 = 20 * max(0, 1 - C.QSR * (1 - p_Role2D) ** 2)
            if p.YouRole3 == "E":
                guess3 = 20 * max(0, 1 - C.QSR * (1 - p_Role2E) ** 2)
            else:
                guess3 = 20 * max(0, 1 - C.QSR * (1 - p_Role2F) ** 2)
        participant = play.participant
        participant.pd3guess = guess1 + guess2 + guess3
def set_labels(group:Group):
    for p in group.get_players():
        participant = p.participant
        p.label1 = participant.label1

def Store(group:Group):
    for p in group.get_players():
        if p.position == 1:
             group.player_1_position1 = p.YouRole1
             group.player_1_position2 = p.YouRole2
             group.player_1_position3 = p.YouRole3
        else:
             group.player_2_position1 = p.YouRole1
             group.player_2_position2 = p.YouRole2
             group.player_2_position3 = p.YouRole3


def Roleallocate(player):
    group = player.group
    if player.id_in_group == 1:
        player.position = C.Role1Player
    if player.id_in_group == 2:
        player.position = 3 - C.Role1Player
def Roleallocates(group):
    for p in group.get_players():
        Roleallocate(p)


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


class WaitforStart(WaitPage):
    wait_for_all_groups = True

class DecisionYou(Page):
    form_model = 'player'
    form_fields = ['YouRole1','YouRole2','YouRole3']

class DecisionOthers(Page):
    form_model = 'player'
    form_fields = ['OppoRole1A', 'OppoRole1B','OppoRole2C','OppoRole2D','OppoRole2E','OppoRole2F']
    @staticmethod
    def error_message(player: Player, values):
        if values['OppoRole1A'] + values['OppoRole1B'] != 1:
            return "选择A和B的概率相加应等于1，请您重新输入"
        if values['OppoRole2C'] + values['OppoRole2D'] != 1:
            return "选择E和F的概率相加应等于1，请您重新输入"
        if values['OppoRole2E'] + values['OppoRole2F'] != 1:
            return "选择E和F的概率相加应等于1，请您重新输入"
class RoleAllocation(WaitPage):
    after_all_players_arrive = Roleallocates
class Storage(WaitPage):
    after_all_players_arrive = Store
class Set_Guess_Payoffs(WaitPage):
    after_all_players_arrive = set_guess_payoffs
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    form_model = 'player'
    #@staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     participant = player.participant
    #     if player.round_number == C.num_rounds:
    #         participant.ultimatum = player.payoff

class SliderPage(Page):
    form_model = 'player'
    form_fields = ['X1X2', 'X3X4','Y1Y2','Y3Y4','X2X1','X4X3','Y2Y1','Y4Y3']
page_sequence = [LabelInitiate, Introduction,  WaitforStart, LabelResults, DecisionYou, DecisionOthers, SliderPage, RoleAllocation, Storage, Set_Guess_Payoffs, ResultsWaitPage, Results]