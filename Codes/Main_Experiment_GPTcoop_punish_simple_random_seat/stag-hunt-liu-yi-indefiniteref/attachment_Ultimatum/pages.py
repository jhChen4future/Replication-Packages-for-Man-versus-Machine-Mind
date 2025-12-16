from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class Introduction2(Page):
    pass

class Offer(Page):
    form_model = 'player'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1,2

class Accept1234(Page):
    form_model = 'player'
    form_fields = ['amount_accept']

    def is_displayed(self):
        return self.player.id_in_group == 1,2


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class ResultsWaitPageTime(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffwait()

class Results(Page):
    timeout_seconds = 120

page_sequence = [Introduction,
                 Introduction2,
                 Offer,
                 Accept1234,
                 ResultsWaitPage,
                 Results
                 ]

