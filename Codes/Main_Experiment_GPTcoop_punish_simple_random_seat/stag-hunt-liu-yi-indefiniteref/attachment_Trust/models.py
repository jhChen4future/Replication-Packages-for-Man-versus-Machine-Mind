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

author = 'Yi Liu'
doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
multiplied by the multiplier. The trust game was first proposed by
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'attachment_Trust/instructions.html'

    # Initial amount allocated to each player
    endowment = c(2)
    multiplier = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        import random
        matrix = self.session.vars['id_matrix']
        for row in matrix:
            random.shuffle(row)
        self.set_group_matrix(matrix)


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment, doc="""Amount sent by P1"""
    )

    sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""", min=c(0))

    def sent_back_amount_max(self):
        return self.sent_amount * Constants.multiplier

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount


class Player(BasePlayer):
    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
