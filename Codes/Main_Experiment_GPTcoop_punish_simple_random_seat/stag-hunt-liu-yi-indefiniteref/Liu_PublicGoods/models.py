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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Liu_PublicGoods'
    players_per_group = 3
    num_rounds = 2
    multiplier = 2
    endowment = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sum = models.CurrencyField()
    individual_share = models.CurrencyField()
    def set_payoffs(self):
        self.sum = sum([p.contribute for p in self.get_players()])
        self.individual_share = (Constants.multiplier*self.sum)/Constants.players_per_group
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribute) + self.individual_share


class Player(BasePlayer):
    contribute = models.CurrencyField()
    def role(self):
        if self.id_in_group == 1:
            return 'A'
        if self.id_in_group == 2:
            return 'B'
        if self.id_in_group == 3:
            return 'C'
