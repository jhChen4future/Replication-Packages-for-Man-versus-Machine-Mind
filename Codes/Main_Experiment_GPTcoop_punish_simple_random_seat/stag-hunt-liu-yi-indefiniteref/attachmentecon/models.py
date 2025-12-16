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
This is an experiment contains one survey and 4 simple games including prisoner's dilemma, simple trust game, ultimatum game, and  dictator game.
"""


class Constants(BaseConstants):
    name_in_url = 'attachmentecon'
    players_per_group = 2
    num_rounds = 1
    betray_payoff = c(10)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(5)
    both_defect_payoff = c(2)

class Subsession(BaseSubsession):
    def creating_session(self):
        id_matrix = []
        for row in self.get_group_matrix():
            ids = [p.id_in_subsession for p in row]
            id_matrix.append(ids)
        self.session.vars['id_matrix'] = id_matrix


class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            p.set_payoff()


class Player(BasePlayer):
    decision = models.StringField(
        choices=[['Strategy_1', 'Strategy_1'], ['Strategy_2', 'Strategy_2']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    def other_player(self):
        return self.get_others_in_group()[0]


    def set_payoff(self):
        payoff_matrix = dict(
            Strategy_1=dict(
                Strategy_1=Constants.both_cooperate_payoff,
                Strategy_2=Constants.betrayed_payoff,
            ),
            Strategy_2=dict(
                Strategy_1=Constants.betray_payoff, Strategy_2=Constants.both_defect_payoff
            ),
        )
        self.payoff = payoff_matrix[self.decision][self.other_player().decision]


    q1 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I am afraid that I will lose the love from my closed ones'
    )

    q2 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I prefer not to show people how I feel deep down'
    )
    q3 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I often worry that people will not want to stay with me'
    )
    q4 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I feel comfortable sharing my private thoughts and feelings with my closed ones'
    )
    q5 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label="I often worry that people don't really like me"
    )
    q6 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I find it difficult to allow myself to depend on other people'
    )
    q7 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label="I worry my closed ones won't care about me as much as I care about them"
    )
    q8 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I am very comfortable being close to other people'
    )
    q9 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label="I often wish that my closed one's feelings for me were as strong as my feelings for them"
    )
    q10 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6', '7(Strongly Agree)'],
        label='I do not feel comfortable opening up to my closed ones'
    )
    q11 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I worry a lot about my closed relationship such as friendship'
    )
    q12 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I prefer not to be too close to other people'
    )
    q13 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='When others are out of sight, I worry that they might become interested in someone else'
    )
    q14 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I get uncomfortable when others want to be very close"'
    )
    q15 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='When I show y feelings for others, I am afraid they will not feel the same about me"'
    )
    q16 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I find it relatively easy t oget close to others'
    )
    q17 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I rarely worry about others leaving me'
    )
    q18 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='It is not difficult for me to get close to others'
    )
    q19 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='Others make me doubt myself'
    )
    q20 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I usually discuss my problems and concerns with others'
    )
    q21 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6', '7(Strongly Agree)'],
        label='I do not often worry about being abandoned'
    )
    q22 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='It helps to turn to others in times of need'
    )
    q23 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label="I find that others don't want to get as close as I would like"
    )
    q24 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I tell others just about everything'
    )
    q25 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='Sometimes others change their feelings about me for no apparent reason'
    )
    q26 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I talk things over with others'
    )
    q27 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='My desire to be very close sometimes scares other people away'
    )
    q28 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I am nervous when others get too close to me'
    )
    q29 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I am afraid that once others get to know me, they will not like who I really am'
    )
    q30 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I feel comfortable depending on others'
    )
    q31 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label="It makes me mad that I don't get the affection and support I need from others (such as parents)"
    )
    q32 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='I find it easy to depend on others'
    )
    q33 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label="I worry that I won't measure up to other people"
    )
    q34 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='It is easy for me to be affectionate with others'
    )
    q35 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='Others only seem to notice me when I am angry'
    )
    q36 = models.StringField(
        choices=['1(Strongly Disagree)', '2', '3', '4', '5', '6','7(Strongly Agree)'],
        label='My closed ones really understand me and my needs'
    )

