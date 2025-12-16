
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'demo_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    label1 = models.StringField(choices=[['ChatGPT', 'ChatGPT'], ['Human', 'Human']], label='',widget=widgets.RadioSelect)
    age = models.IntegerField(label='您的年龄')
    gender = models.StringField(choices=[['男性', '男性'], ['女性', '女性']], label='您的性别', widget=widgets.RadioSelect)
    major = models.StringField(label='您的在读专业')
    grade = models.StringField(choices=[['大一', '大一'], ['大二', '大二'], ['大三', '大三'], ['大四', '大四'], ['大五', '大五'], ['硕士一年级', '硕士一年级'], ['硕士二年级', '硕士二年级'], ['硕士三年级', '硕士三年级'], ['直博一年级', '直博一年级'], ['直博二年级', '直博二年级'], ['直博三年级（含硕转博一年级）', '直博三年级（含硕转博一年级）'],['直博四年级', '直博四年级'],['直博四年级', '直博四年级'],['直博六年级', '直博六年级'], ['其他', '其他']], label='您所在的年级', widget=widgets.RadioSelect)
    GPT = models.StringField(choices=[['极少使用（少于每月一次）', '极少使用（少于每月一次）'], ['每月大于一次', '每月至少一次'], ['每周大于一次', '每周至少一次'], ['每天至少一次', '每天至少一次']], label='您的GPT大模型（ChatGPT、Claude、Kimi、文心一言等）使用频率', widget=widgets.RadioSelect)
    currencytest=models.CurrencyField()
def creating_session(subsession):
    import datetime as dt
    session = subsession.session
    now = dt.datetime.now()
    format_date = now.strftime("%Y-%m-%d %H:%M:%S")
    session.label = format_date
    labels = ['LAB1','LAB2','LAB3','LAB4','LAB5','LAB6','LAB7','LAB8','LAB9','LAB10','LAB11','LAB12','LAB13','LAB14','LAB15','LAB16','LAB17','LAB18','LAB19','LAB20','LAB21','LAB22','LAB23','LAB24']
    for player, label in zip(subsession.get_players(), labels):
        player.participant.label = label
class Label1(Page):
    form_model = 'player'
    form_fields = ['label1']
def set_credits(group:Group):
    for p in group.get_players():
        participant = p.participant
        participant.credit = 0.25
        participant.lowcredit = 0.025
class LabelWaitPage(WaitPage):
    after_all_players_arrive = set_credits
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
class Instruction(Page):
    form_model = 'player'
    timeout_seconds = 180
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'major', 'grade', 'GPT']
page_sequence = [Instruction,Label1,LabelWaitPage,LabelResults]