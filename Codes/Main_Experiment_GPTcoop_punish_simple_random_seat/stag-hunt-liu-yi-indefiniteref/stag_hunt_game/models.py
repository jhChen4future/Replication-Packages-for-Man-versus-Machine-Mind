from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Zoe Zhao'

doc = """
Stag-hunt game
"""


class Constants(BaseConstants):
    name_in_url = 'stag_hunt_game'
    players_per_group = 2
    for i in range(0,5):
        x = random.uniform(0, 1)
        if x <= 0.45:
            i = i+1
        else:
            break
    num_rounds = 5 + i
    instructions_template = 'stag_hunt_game/instructions.html'
    result_wait_template = 'stage_hunt_game/MyWaitPage.html'

    stag_match_payoff = c(4)
    stag_mismatch_payoff = c(0)
    h_1_hare_payoff = c(1)
    players_per_group = 2



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round


class Group(BaseGroup):

    def h_2_hare_payoff(self):
        if self.round_number <= 3:
            h_2_hare_payoff = c(2)
        else:
            h_2_hare_payoff = c(3)
        return h_2_hare_payoff

    def set_payoffs(self):
        h_1 = self.get_player_by_role('Hunter_1')
        h_2 = self.get_player_by_role('Hunter_2')
        if h_1.decision == 'hare' and h_2.decision == 'hare':
            h_1.payoff = Constants.h_1_hare_payoff
            h_2.payoff = self. h_2_hare_payoff()
        else:
            if h_1.decision == 'hare' and h_2.decision == 'stag':
                h_1.payoff = Constants.h_1_hare_payoff
                h_2.payoff = Constants.stag_mismatch_payoff
            else:
                if h_1.decision == 'stag' and h_2.decision == 'hare':
                    h_1.payoff = Constants.stag_mismatch_payoff
                    h_2.payoff = self. h_2_hare_payoff()
                else:
                    h_1.payoff = Constants.stag_match_payoff
                    h_2.payoff = Constants.stag_match_payoff

class Player(BasePlayer):
    decision = models.StringField(
        choices=['stag', 'hare'],
        doc="""This player's decision is either stag or hare""",
        widget=widgets.RadioSelect,
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def role(self):
       if self.id_in_group == 1:
           return 'Hunter_1'
       if self.id_in_group == 2:
           return 'Hunter_2'

    name = models.StringField()
    age = models.IntegerField()
    gender = models.StringField()
    major = models.IntegerField()
    race = models.IntegerField()
    feelings = models.IntegerField()