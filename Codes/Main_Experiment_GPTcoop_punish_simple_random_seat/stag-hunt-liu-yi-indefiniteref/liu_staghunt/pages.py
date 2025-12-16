from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Assignment(Page):
    template_name = 'liu_staghunt/role_assignment.html'
    def is_displayed(self):
        return self.round_number == 1


class Reminder(Page):
    template_name = 'liu_staghunt/round3reminder.html'
    def is_displayed(self):
        return self.round_number == 4
    timeout_seconds = 30

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_seconds = 20

    def before_next_page(self):
        if self.timeout_happened:
            self.player.decision = 'Stag'

    def vars_for_template(self):
        return dict(
            player_in_previous_rounds=self.player.in_previous_rounds()
        )


class ResultsWaitPage(WaitPage):
    template_name = 'liu_staghunt/wait.html'
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return dict(
            my_decision=me.decision,
            opponent_decision=opponent.decision,
            same_choice=me.decision == opponent.decision,
            player_in_all_rounds=self.player.in_all_rounds()
        )

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class Summary(Page):
    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return dict(
            player_in_all_rounds=player_in_all_rounds,
            paying_round=self.session.vars['paying_round'],
            total_payoff=sum([p.payoff for p in player_in_all_rounds]),
        )

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

page_sequence = [Introduction, Assignment, Reminder, Decision, ResultsWaitPage, Results, Summary, Questionnaire]
