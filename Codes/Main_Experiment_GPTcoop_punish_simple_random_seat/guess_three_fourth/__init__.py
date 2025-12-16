
from otree.api import *
c = cu

doc = '\na.k.a. Keynesian beauty contest.\nPlayers all guess a number; whoever guesses closest to\n2/3 of the average wins.\nSee https://en.wikipedia.org/wiki/Guess_2/3_of_the_average\n'
class C(BaseConstants):
    NAME_IN_URL = 'guess_three_fourth'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    JACKPOT = cu(200)
    GUESS_MAX = 100
    Bot_numbers = 3
    Total = 11 #看html文件，total是不含被试本人的数量
    INSTRUCTIONS_TEMPLATE = 'guess_three_fourth/instructions.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    three_fourth_avg = models.FloatField()
    best_guess = models.IntegerField()
    num_winners = models.IntegerField()
def set_payoffs(group: Group):
    players = group.get_players()
    guesses = [p.guess for p in players]
    three_fourth_avg = (3 / 4) * sum(guesses) / len(players)
    group.three_fourth_avg = round(three_fourth_avg, 2)
    group.best_guess = min(guesses, key=lambda guess: abs(guess - group.three_fourth_avg))
    winners = [p for p in players if p.guess == group.best_guess]
    group.num_winners = len(winners)
    for p in winners:
        p.is_winner = True
        p.payoff = C.JACKPOT / group.num_winners
def three_fourth_avg_history(group: Group):
    return [g.three_fourth_avg for g in group.in_previous_rounds()]
class Player(BasePlayer):
    guess = models.IntegerField(label='请输入一个0-100间的整数', max=C.GUESS_MAX, min=0)
    is_winner = models.BooleanField(initial=False)
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    Train1 = models.IntegerField(
        label='问题1：假设现在有三名玩家参与游戏，玩家1选择20，玩家2选择30，玩家3选择70，请问本轮游戏的赢家是玩家几？（请输入玩家序号）')
 #   Train2 = models.IntegerField(
     #   label='问题2：假设现在有三名玩家参与游戏，玩家1选择10，玩家2选择30，玩家3选择50，请问本轮游戏玩家2的最终收入是多少？')
 #   Train3 = models.IntegerField(
  #      label='问题3：现在有三名玩家参与游戏，玩家1选择10，玩家2选择30，玩家3选择50，请问本轮游戏玩家3的最终收入是多少？')
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
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(),
        )
class Train(Page):
    form_model = 'player'
    form_fields = ['Train1'] #neglect train2.3
    @staticmethod
    def error_message(player: Player, values):
        if values['Train1'] != 2:
            return "您问题1的答案错误，请您重新输入"
        #if values['Train2'] != 200:
        #    return "您问题2的答案错误，请您重新输入"
      #  if values['Train3'] != 0:
          #  return "您问题3的答案错误，请您重新输入"
class WaitforStart(WaitPage):
    wait_for_all_groups = True
class Introduction(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(three_fourth_avg_history=three_fourth_avg_history(group))
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Waitforallgroups(WaitPage):
    wait_for_all_groups = True
class Results(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if player.round_number == C.NUM_ROUNDS:
            participant.guess_three_fourth = player.payoff
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        sorted_guesses = sorted(p.guess for p in group.get_players())
        return dict(sorted_guesses=sorted_guesses)
page_sequence = [LabelInitiate, Introduction, Train, WaitforStart, LabelResults, Guess, ResultsWaitPage, Waitforallgroups, Results]