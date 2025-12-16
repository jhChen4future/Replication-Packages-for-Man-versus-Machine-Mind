from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass

class Introduction1(Page):
    timeout_seconds = 120

class InstructionsPD(Page):
    pass

class DecisionPrisoner(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_seconds = 60

    def before_next_page(self):
        if self.timeout_happened:
            self.player.decision = 'Strategy_2'


class ResultsWaitPage(WaitPage):
    template_name = 'attachmentecon/wait.html'
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class ResultPD(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return dict(
            my_decision=me.decision,
            opponent_decision=opponent.decision,
            same_choice=me.decision == opponent.decision,
            player_in_all_rounds=self.player.in_all_rounds()
        )
    timeout_seconds = 120

class Survey(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']
    timeout_seconds = 180
class Survey2(Page):
    form_model = 'player'
    form_fields = ['q7', 'q8', 'q9', 'q10', 'q11', 'q12']
    timeout_seconds = 180
class Survey3(Page):
    form_model = 'player'
    form_fields = ['q13', 'q14', 'q15', 'q16', 'q17', 'q18']
    timeout_seconds = 180
class Survey4(Page):
    form_model = 'player'
    form_fields = ['q19', 'q20', 'q21', 'q22', 'q23', 'q24']
    timeout_seconds = 180
class Survey5(Page):
    form_model = 'player'
    form_fields = ['q25', 'q26', 'q27', 'q28', 'q29', 'q30']
    timeout_seconds = 180
class Survey6(Page):
    form_model = 'player'
    form_fields = ['q31', 'q32', 'q33', 'q34', 'q35', 'q36']
    timeout_seconds = 180





page_sequence = [Welcome,
                 Introduction1,
                 InstructionsPD,
                 DecisionPrisoner, ResultsWaitPage, ResultPD]
