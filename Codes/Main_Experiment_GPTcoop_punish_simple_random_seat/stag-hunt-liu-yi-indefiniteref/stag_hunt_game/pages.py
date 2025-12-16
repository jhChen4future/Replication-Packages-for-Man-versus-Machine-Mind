from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    timeout_seconds = 100


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_seconds = 20

    def before_next_page(self):
        if self.timeout_happened:
            self.player.decision = 'stag'

class MyWaitPage(WaitPage):
    template_name = 'stag_hunt_game/MyWaitPage.html'
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return dict(
            my_decision=me.decision,
            opponent_decision=opponent.decision,
        )


class History(Page):
    def vars_for_template(self):
        return dict(
            player_in_all_rounds_rev=reversed(self.player.in_all_rounds())
        )

class Question(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'gender', 'race', 'feelings']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class Summary(Page):
    def vars_for_template(self):
        return dict(
            player_in_all_rounds_rev=reversed(self.player.in_all_rounds()),
            paying_round=self.session.vars['paying_round'],
        )

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [Introduction, Decision, MyWaitPage, Results, History, Question, Summary]
