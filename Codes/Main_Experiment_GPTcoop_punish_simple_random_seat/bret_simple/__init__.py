import random

from otree.api import *
from settings import LANGUAGE_CODE

author = 'Felix Holzmeister & Armin Pfurtscheller'
doc = """
Bomb Risk Elicitation Task (BRET) à la Crosetto/Filippin (2013), Journal of Risk and Uncertainty (47): 31-65.
"""


class Constants(BaseConstants):
    name_in_url = 'bret'
    players_per_group = None
    num_rounds = 1
    BOX_VALUE = cu(1)
    NUM_ROWS = 10
    NUM_COLS = 10
    INSTRUCTIONS_TEMPLATE = 'bret_simple/instructions.html'
    NUM_BOXES = NUM_ROWS * NUM_COLS
    bomb = random.randint(1,NUM_BOXES)

class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']],label='',widget=widgets.RadioSelect)
    boxes_collected = models.IntegerField(label='我希望收集多少个盒子', max=Constants.NUM_BOXES, min=0)
    pay_this_round = models.BooleanField()
    Train1 = models.FloatField(
        label='问题1：假设您决定收集50个盒子，您有多大的概率收集到装有定时炸弹的盒子？（请用小数填写答案）')
# FUNCTIONS
def set_payoff(group: Group):
    players = group.get_players()
    for p in players:
        if Constants.bomb <= p.boxes_collected:
            p.pay_this_round = False
        else:
            p.pay_this_round = True
        if p.pay_this_round == True:
            p.payoff = p.boxes_collected * Constants.BOX_VALUE
        else:
            p.payoff = cu(0)
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

class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return  player.round_number == 1
class Train(Page):
    form_model = 'player'
    form_fields = ['Train1'] #neglect train3
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    def error_message(player: Player, values):
        if values['Train1'] != 0.5:
            return "您问题1的答案错误，请您重新输入"

class Game(Page):
    # form fields on player level
    form_model = 'player'
    form_fields = [
        'boxes_collected'
    ]

class WaitforResults(WaitPage):
    after_all_players_arrive = set_payoff

class Results(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if player.round_number == Constants.num_rounds:
            participant.bret_simple = player.payoff


page_sequence = [LabelInitiate, Introduction, Train, LabelResults,Game, WaitforResults, Results]
