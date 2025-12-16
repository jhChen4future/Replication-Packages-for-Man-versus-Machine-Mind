from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribute']


class ContributeWait(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()




class Results(Page):
    pass
class History(Page):
    def vars_for_template(self):
        return dict(
            player_in_all_rounds = (self.player.in_all_rounds)
        )


page_sequence = [Contribute, ContributeWait, Results, History]
