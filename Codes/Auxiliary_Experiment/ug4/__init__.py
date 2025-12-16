from otree.api import *
c = cu
import random


#role is changed into position due to reserved letter

class C(BaseConstants):
    NAME_IN_URL = 'ug4'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    R1_1A = 50
    R1_1B2E = 75
    R1_1B2F = 10
    R2_1A = 50
    R2_1B2E = 25
    R2_1B2F = 10
    QSR = 2
    Role1Player = random.randint(1, 2)

class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    player_1_position1 = models.StringField()
    player_1_position2 = models.StringField()
    player_2_position1 = models.StringField()
    player_2_position2 = models.StringField()
class Player(BasePlayer):
    YouRole1 = models.StringField(choices=[['A','A'],['B','B']], label='若你是角色1，你会选择哪个决策', widget=widgets.RadioSelect)
    YouRole2 = models.StringField(choices=[['E','E'],['F','F']], label='若你是角色2，你会选择哪个决策', widget=widgets.RadioSelect)
    OppoRole1A = models.FloatField(max=1, min=0, label="若你的对手是角色1，你认为其有多大概率选择A（请输入两位小数）")
    OppoRole1B = models.FloatField(max=1, min=0, label="若你的对手是角色1，你认为其有多大概率选择B（请输入两位小数）")
    OppoRole2E = models.FloatField(max=1, min=0, label="若你的对手是角色2（假设你已选择了B），你认为其有多大概率选择E（请输入两位小数）")
    OppoRole2F = models.FloatField(max=1, min=0, label="若你的对手是角色2（假设你已选择了B），你认为其有多大概率选择F（请输入两位小数）")
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    M1M2 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f"如果你选择A，你的收入为 {C.R1_1A}，对手收入为 {C.R2_1A}", widget=widgets.RadioSelect)
    N1N2 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果你选择B，对手选择E，你的收入为{C.R1_1B2E}，对手收入为{C.R2_1B2E}', widget=widgets.RadioSelect)
    N3N4 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果你选择B，对手选择F，你的收入为{C.R1_1B2F}，对手收入为{C.R2_1B2F}', widget=widgets.RadioSelect)
    M2M1 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果对手选择A，你的收入为{C.R2_1A}，对手收入为{C.R1_1A}', widget=widgets.RadioSelect)
    N2N1 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果对手选择B，你选择E，你的收入为{C.R2_1B2E}，对手收入为{C.R1_1B2E}', widget=widgets.RadioSelect)
    N4N3 = models.IntegerField(choices=[[1, '非常不满意'], [2, '不满意'], [3, '比较不满意'], [4, '一般'], [5, '比较满意'], [6, '满意'], [7, '非常满意']],label=f'如果对手选择B，你选择F，你的收入为{C.R2_1B2F}，对手收入为{C.R1_1B2F}', widget=widgets.RadioSelect)
    position = models.IntegerField()

def creating_session(subsession:Subsession):
    subsession.group_randomly()

def other_player(player):
    group = player.group
    return player.get_others_in_group()[0]

def set_payoff(player):
    group = player.group
    if player.id_in_group == 1:
            if player.position == 1:   #position1-player1 position2-player2
                if player.YouRole1 == "A":
                    player.payoff = C.R1_1A   #position1A
                else:
                    if group.player_2_position2 == "E":  #position1B position2C
                        player.payoff = C.R1_1B2E #r1.payoff=p1.payoff
                    else:
                        player.payoff = C.R1_1B2F
            else:
                if player.YouRole2 == "E": #position1-player2 position2-player1
                    if group.player_2_position1 == "A":
                        player.payoff = C.R1_1A #position1A position2C
                    else:
                        player.payoff = C.R1_1B2E #position1B position2C
                else:
                    if group.player_2_position1 == "A":
                        player.payoff = C.R1_1A
                    else:
                        player.payoff = C.R1_1B2F
    if player.id_in_group == 2:
        if player.position == 1:
            if player.YouRole1 == "A":
                player.payoff = C.R1_1A
            else:
                if group.player_1_position1 == "E":
                    player.payoff = C.R1_1B2E
                else:
                    player.payoff = C.R1_1B2F
        else:
            if player.YouRole2 == "E":
                if group.player_1_position1 == "A":
                    player.payoff = C.R1_1A
                else:
                    player.payoff = C.R1_1B2E
            else:
                if group.player_1_position1 == "A":
                    player.payoff = C.R1_1A
                else:
                    player.payoff = C.R1_1B2F
    participant = player.participant
    participant.ug4payoff = player.payoff
def set_payoffs(group):
    for p in group.get_players():
        set_payoff(p)

def set_guess_payoffs(group:Group):
    for play in group.get_players():
        guess1 = float(0)
        guess2 = float(0)
        p_Role1A = play.OppoRole1A
        p_Role1B = play.OppoRole1B
        p_Role2E = play.OppoRole2E
        p_Role2F = play.OppoRole2F
        for p in play.get_others_in_group():
            if p.YouRole1 == "A":
                guess1 = 30 * max(0, 1 - C.QSR * (1 - p_Role1A) ** 2)
            else:
                guess1 = 30 * max(0, 1 - C.QSR * (1 - p_Role1B) ** 2)
            if p.YouRole2 == "E":
                guess2 = 30 * max(0, 1 - C.QSR * (1 - p_Role2E) ** 2)
            else:
                guess2 = 30 * max(0, 1 - C.QSR * (1 - p_Role2F) ** 2)
        participant = play.participant
        participant.ug4guess = guess1 + guess2

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

def Store(group:Group):
    for p in group.get_players():
        if p.position == 1:
             group.player_1_position1 = p.YouRole1
             group.player_1_position2 = p.YouRole2
        else:
             group.player_2_position1 = p.YouRole1
             group.player_2_position2 = p.YouRole2


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
    form_fields = ['YouRole1','YouRole2']

class DecisionOthers(Page):
    form_model = 'player'
    form_fields = ['OppoRole1A', 'OppoRole1B','OppoRole2E','OppoRole2F']
    @staticmethod
    def error_message(player: Player, values):
        if values['OppoRole1A'] + values['OppoRole1B'] != 1:
            return "选择A和B的概率相加应等于1，请您重新输入"
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
    form_fields = ['M1M2', 'N1N2','N3N4','M2M1','N2N1','N4N3']
page_sequence = [LabelInitiate, Introduction,  WaitforStart, LabelResults, DecisionYou, DecisionOthers, SliderPage, RoleAllocation, Storage, Set_Guess_Payoffs, ResultsWaitPage, Results]