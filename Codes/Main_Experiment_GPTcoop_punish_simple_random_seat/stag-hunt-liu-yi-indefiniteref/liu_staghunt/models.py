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

doc = """
This is a min 5 max 10 rounds indefinitely repeated "Stag Hunt Game". Two players are asked separately and simultaneously
whether they want to hunt stags or hares. Their choices directly determine their
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'YI_LIU_staghunt'
    players_per_group = 2
    for i in range(0,5):
        y = random.uniform(0,1)
        if y <= 0.45:
            i = i + 1
        else:
            break
    num_rounds = 5+i

    instructions_template = 'liu_staghunt/instructions.html'


    both_stag_payoff = c(4)
    hare_p1_payoff = c(1)
    stag_hare_p1_payoff = c(0)



class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round

        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)



class Group(BaseGroup):

    def hare_p2_payoff(self):
        if self.round_number <= 3:
            hare_p2_payoff = c(2)
        else:
            hare_p2_payoff = c(3)
        return hare_p2_payoff

    def set_payoffs(self):
        h1 = self.get_player_by_role('Hunter 1')
        h2 = self.get_player_by_role('Hunter 2')
        if h1.decision == 'Hare' and h2.decision == 'Hare':
            h1.payoff = Constants.hare_p1_payoff
            h2.payoff = self. hare_p2_payoff()
        else:
            if h1.decision == 'Hare' and h2.decision == 'Stag':
                h1.payoff = Constants.hare_p1_payoff
                h2.payoff = Constants.stag_hare_p1_payoff
            else:
                if h1.decision == 'Stag' and h2.decision == 'Hare':
                    h1.payoff = Constants.stag_hare_p1_payoff
                    h2.payoff = self. hare_p2_payoff()
                else:
                    h1.payoff = Constants.both_stag_payoff
                    h2.payoff = Constants.both_stag_payoff


class Player(BasePlayer):
    decision = models.StringField(
        choices=[['Stag', 'Stag'], ['Hare', 'Hare']],
        doc="""Each players' decision is either Stag or Hare""",
        widget=widgets.RadioSelect,
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def role(self):
       if self.id_in_group == 1:
           return 'Hunter 1'
       if self.id_in_group == 2:
           return 'Hunter 2'




    gpa = models.StringField(
        choices=['0-1.00', '1.01-2.00', '2.01-2.59', '2.60-3.00', '3.01-3.49', '3.50-4.00'],
        label='What is your GPA? Please choose a range below?'
    )
    age = models.IntegerField(label='What is your age?', min=18, max=125)
    gender = models.StringField(
        choices = ['Male', 'Female', 'Non-binary', 'Non-conforming', 'Do not want to disclose'],
        label='What is your gender?'
    )
    major = models.StringField(label='What is your major?')
    ifmajor = models.StringField(
        choices = ['Yes', 'No'],
        label='Please indicate if you have taken any game theory classes. Yes or No.'
    )