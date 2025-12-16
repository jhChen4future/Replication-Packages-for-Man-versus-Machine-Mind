
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'instruction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    INSTRUCTIONS1_TEMPLATE = 'general_instruction/instructions1.html'
    INSTRUCTIONS2_TEMPLATE = 'general_instruction/instructions2.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    Train1_1 = models.IntegerField(
        label='问题1：假设角色1选择了A，角色2选择了C和E，角色1会获得多少点数？')
    Train1_2 = models.IntegerField(
        label='问题2：假设角色1选择了A，角色2选择了C和E，角色2会获得多少点数')
    Train1_3 = models.IntegerField(
        label='问题3：假设角色1选择了B，角色2选择了D和F，角色1会获得多少点数')
    Train1_4 = models.IntegerField(
        label='问题4：假设角色1选择了B，角色2选择了D和F，角色2会获得多少点数？')
    Train2_1 = models.IntegerField(
        label='问题1：假设角色1选择了A，角色2选择了E，角色1会获得多少点数？')
    Train2_2 = models.IntegerField(
        label='问题2：假设角色1选择了A，角色2选择了E，角色2会获得多少点数？')
    Train2_3 = models.IntegerField(
        label='问题3：假设角色1选择了B，角色2选择了F，角色1会获得多少点数')
    Train2_4 = models.IntegerField(
        label='问题4：假设角色1选择了B，角色2选择了F，角色2会获得多少点数？')
def creating_session(subsession):
    import datetime as dt
    session = subsession.session
    now = dt.datetime.now()
    format_date = now.strftime("%Y-%m-%d %H:%M:%S")
    session.label = format_date
    labels = ['LAB1','LAB2','LAB3','LAB4','LAB5','LAB6','LAB7','LAB8','LAB9','LAB10','LAB11','LAB12','LAB13','LAB14','LAB15','LAB16','LAB17','LAB18','LAB19','LAB20','LAB21','LAB22','LAB23','LAB24']
    for player, label in zip(subsession.get_players(), labels):
        player.participant.label = label

class Instruction(Page):
    form_model = 'player'
    timeout_seconds = 180
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Label1(Page):
    form_model = 'player'
    form_fields = ['label1']

class LabelResults(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(),
        )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.label1 = player.label1

class Introduction1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Introduction2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Introduction3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Train1_introduction(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Train1(Page):
    form_model = 'player'
    form_fields = ['Train1_1', 'Train1_2','Train1_3', 'Train1_4']
    @staticmethod
    def error_message(player: Player, values):
        if values['Train1_1'] != 45  :
            return "您问题1的答案错误，请您重新输入"
        if values['Train1_2'] != 45:
            return "您问题2的答案错误，请您重新输入"
        if values['Train1_3'] != 15:
            return "您问题3的答案错误，请您重新输入"
        if values['Train1_4'] != 15:
            return "您问题4的答案错误，请您重新输入"

class Train2_introduction(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Train2(Page):
    form_model = 'player'
    form_fields = ['Train2_1', 'Train2_2','Train2_3', 'Train2_4']
    @staticmethod
    def error_message(player: Player, values):
        if values['Train2_1'] != 50:
            return "您问题1的答案错误，请您重新输入"
        if values['Train2_2'] != 50:
            return "您问题2的答案错误，请您重新输入"
        if values['Train2_3'] != 10:
            return "您问题3的答案错误，请您重新输入"
        if values['Train2_4'] != 10:
            return "您问题4的答案错误，请您重新输入"
class guess_instruction(Page):
    form_model = 'player'
class End(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

page_sequence = [Instruction, Label1,LabelResults, Introduction1, Introduction2,Introduction3, Train1_introduction, Train1, Train2_introduction, Train2,  End]