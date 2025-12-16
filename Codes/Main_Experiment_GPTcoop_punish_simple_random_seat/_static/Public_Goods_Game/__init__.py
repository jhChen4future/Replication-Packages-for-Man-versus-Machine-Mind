
from otree.api import *
c = cu

doc = 'A public goods game\n'
class Constants(BaseConstants):
    name_in_url = 'Public_Goods_Game'
    players_per_group = 4
    num_rounds = 1
    multiplier = 1.6
    endowment = 20
    instructions_template = 'Public_Goods_Game/instructions.html'
def creating_session(subsession):
    session = subsession.session
    subsession.group_randomly()
class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    session = group.session
    
    players = group.get_players()
    
    contributions = [p.contribution for p in players]
    
    group.total_contribution = sum(contributions)
    
    group.individual_share = group.total_contribution * Constants.multiplier / session.num_participants
    
    for p in group.get_players():
        set_payoff(p)
class Group(BaseGroup):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    label2 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    label3 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    label4 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    individual_share = models.CurrencyField()
    total_contribution = models.CurrencyField()
def set_payoff(player):
    group = player.group
    player.payoff = Constants.endowment - player.contribution + group.individual_share
class Player(BasePlayer):
    contribution = models.IntegerField(max=Constants.endowment, min=0)
class Label1(Page):
    form_model = 'group'
    form_fields = ['label1']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1
class Label2(Page):
    form_model = 'group'
    form_fields = ['label2']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2
class Label3(Page):
    form_model = 'group'
    form_fields = ['label3']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 3
class Label4(Page):
    form_model = 'group'
    form_fields = ['label4']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 4
class LabelWaitPage(WaitPage):
    pass
class LabelResults(Page):
    form_model = 'group'
class Introduction(Page):
    form_model = 'player'
    timeout_seconds = 100
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player):
        maximum_score = Constants.multiplier * Constants.endowment
        
        return dict(
            maximum_score = maximum_score
        )
class Decision(Page):
    form_model = 'player'
    form_fields = ['contribution']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Waitforallgroups(WaitPage):
    wait_for_all_groups = True
class Results(Page):
    form_model = 'player'
page_sequence = [Label1, Label2, Label3, Label4, LabelWaitPage, LabelResults, Introduction, Decision, ResultsWaitPage, ResultsWaitPage,Results]