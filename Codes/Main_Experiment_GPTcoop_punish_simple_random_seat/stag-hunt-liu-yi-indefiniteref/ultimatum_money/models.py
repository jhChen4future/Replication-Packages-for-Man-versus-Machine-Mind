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
from datetime import timedelta, datetime

doc = """
Ultimatums Bargaining with Money
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_money'
    players_per_group = 2
    num_rounds = 1
    roles = ['proposer','responder']
    instructionsmoney_template = 'ultimatum_money/instructionsmoney.html'
    instructionsstart_template = 'ultimatum_money/instructionsstart.html'


#####Variablen für das Geld Treatment
    endowment = c(10)
    payoff_if_rejected = c(0)
    ##### Unbenutzt aber wichtig, da Adminrechte drin######
    offer_increment =c(1)
    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)

    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))

#####Variablen für das Treatment Zeit
    endowmenttime = 30
    payoff_if_rejected_time = endowmenttime



class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools
        treatmentgroup = itertools.cycle(['Zeit','Geld'])
        for g in self.get_groups():
            g.treatmentgroup = next(treatmentgroup)
            print(g.treatmentgroup)
            g.use_strategy_method = False
            # g.treatment = g.randomtreatment()
            g.zuteilungrollen()


class Group(BaseGroup):
    # def randomtreatment(self):
    #     rng = random.Random()
    #     rndTreatment = rng.randint(0, 1)
    #
    #     if rndTreatment == 1:
    #         treatment='Zeit'
    #     else:
    #         treatment='Geld'
    #     return treatment

    treatmentgroup = models.StringField()
    treatment = models.StringField()
    use_strategy_method = models.BooleanField(
        doc="""Whether this group uses strategy method""",
    )

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )
    offer_acceptedtime = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )
    grprandom = models.IntegerField()
    amount_offered = models.CurrencyField()
    amount_offeredtime = models.FloatField()

############Berechnung Auszahlung des Geldtreatments#############################
    def set_payoffs(self):
        p1, p2 = self.get_players()

        if p1.randomrole == 'Proposer':
            self.amount_offered = p1.amount_offered
            if p1.amount_offered >= p2.amount_accept:
                p1.accept_offer = True
                self.offer_accepted = True
                p1.payoff = Constants.endowment - p1.amount_offered
                p2.payoff = p1.amount_offered
            else:
                p1.accept_offer = False
                self.offer_accepted = False
                p1.payoff = Constants.payoff_if_rejected
                p2.payoff = Constants.payoff_if_rejected
        elif p1.randomrole == 'Responder':
            self.amount_offered = p2.amount_offered
            if p2.amount_offered >= p1.amount_accept:
                p2.accept_offer = True
                self.offer_accepted = True
                p2.payoff = Constants.endowment - p2.amount_offered
                p1.payoff = p2.amount_offered
            else:
                p2.accept_offer = False
                self.offer_accepted = False
                p1.payoff = Constants.payoff_if_rejected
                p2.payoff = Constants.payoff_if_rejected


        # if self.offer_accepted:
        #     p1.payoff = Constants.endowment - self.amount_offered
        #     p2.payoff = self.amount_offered
        # else:
        #     p1.payoff = Constants.payoff_if_rejected
        #     p2.payoff = Constants.payoff_if_rejected
############Berechnung Auszahlung des Zeittreatments#############################
    def set_payoffwait(self):
        p1,p2 = self.get_players()
        if p1.randomrole == 'Proposer':
            self.amount_offeredtime =  p1.amount_offeredtime
            if p1.amount_offeredtime <= p2.amount_accepttime:
                p1.accept_offertime = True
                self.offer_acceptedtime = True
                p1.payofftime = Constants.endowmenttime - p1.amount_offeredtime
                p1.my_page_timeout_seconds = p1.payofftime*60
                p2.payofftime = p1.amount_offeredtime
                p2.my_page_timeout_seconds = p2.payofftime*60
            else:
                p1.accept_offertime = False
                self.offer_acceptedtime = False
                p1.payofftime = Constants.payoff_if_rejected_time
                p1.my_page_timeout_seconds = p1.payofftime*60
                p2.payofftime = Constants.payoff_if_rejected_time
                p2.my_page_timeout_seconds = p2.payofftime*60
        elif p1.randomrole == 'Responder':
            self.amount_offeredtime = p2.amount_offeredtime
            if p2.amount_offeredtime <= p1.amount_accepttime:
                p2.accept_offertime = True
                self.offer_acceptedtime = True
                p2.payofftime = Constants.endowmenttime - p2.amount_offeredtime
                p2.my_page_timeout_seconds = p2.payofftime*60
                p1.payofftime = p2.amount_offeredtime
                p1.my_page_timeout_seconds = p1.payofftime*60
            else:
                p2.accept_offertime = False
                self.offer_acceptedtime = False
                p1.payofftime = Constants.payoff_if_rejected_time
                p1.my_page_timeout_seconds = p1.payofftime*60
                p2.payofftime = Constants.payoff_if_rejected_time
                p2.my_page_timeout_seconds = p2.payofftime*60

    def rndrollen(self):
        rng = random.Random()
        self.grprandom = rng.randint(1,2)
        return self.grprandom

    def zuteilungrollen(self):
        p1, p2 = self.get_players()
        p1.Rolle = self.rndrollen()
        p2.Rolle = p1.Rolle
        print(p1.Rolle)
        if p1.id_in_group == p1.Rolle:
            p1.randomrole = 'Proposer'
            p2.randomrole = 'Responder'
        else:
            p1.randomrole = 'Responder'
            p2.randomrole = 'Proposer'

        print('p1',p1.randomrole)
        print('p2',p2.randomrole)
        return p1.randomrole, p2.randomrole


class Player(BasePlayer):

    # def zuteilungrollen(self):
    #     self.Rolle = self.group.rndrollen()
    #     print(self.Rolle)
    #     if self.id_in_group==self.Rolle:
    #             self.randomrole = 'Proposer'
    #     else:
    #             self.randomrole = 'Responder'
    #
    #     print(self.randomrole)
    #     return self.randomrole

    amount_offered = models.CurrencyField(
        max=Constants.endowment,
        min=0,
    )
    amount_accept = models.CurrencyField(
        max=Constants.endowment,
        min=0,
    )
    amount_offeredtime = models.IntegerField(
        max=Constants.endowmenttime,
        min=0,
    )
    amount_accepttime = models.IntegerField(
        max=Constants.endowmenttime,
        min=0,
    )
    randomrole = models.StringField()
    Rolle = models.IntegerField()
    accept_offer = models.BooleanField()
    accept_offertime = models.BooleanField()
    payofftime = models.IntegerField()
    my_page_timeout_seconds = models.FloatField()