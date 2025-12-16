import random
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'after_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    pd_to_pay = random.randint(1,8)
    showup = 10
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
    GPT = models.StringField(choices=[['极少使用（少于每月一次）', '极少使用（少于每月一次）'], ['每月大i于一次', '每月至少一次'], ['每周大于一次', '每周至少一次'], ['每天至少一次', '每天至少一次']], label='您的GPT大模型（ChatGPT、Claude、Kimi、文心一言等）使用频率', widget=widgets.RadioSelect)
    worry = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我总是自己的境况感到焦虑', widget=widgets.RadioSelect)
    welfare = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我关注他人的福祉', widget=widgets.RadioSelect)
    income = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我只关注自己游戏中的收入', widget=widgets.RadioSelect)
    others = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我不关心其他的参与者', widget=widgets.RadioSelect)
    connect = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我觉得我和他人是联系在一起的', widget=widgets.RadioSelect)
    team = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我关注我的决定对集体的影响', widget=widgets.RadioSelect)
    pay = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我关注实验中的金钱回报', widget=widgets.RadioSelect)
    other_influnce = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我不担心他人的行为对我的影响', widget=widgets.RadioSelect)
    altruistic = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我想尽量减少对集体的负面影响', widget=widgets.RadioSelect)
    expect = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我在游戏中试图按照社会期望的方式进行决策', widget=widgets.RadioSelect)
    fair = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我想做到公平', widget=widgets.RadioSelect)
    other_perspective = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我担心别人会怎么看我', widget=widgets.RadioSelect)
    norm = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我考虑到了社会规范', widget=widgets.RadioSelect)
    fair_worry = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我担心公平问题', widget=widgets.RadioSelect)
    ontime = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我关注游戏中的实时反馈', widget=widgets.RadioSelect)
    overall = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我关注“大局”', widget=widgets.RadioSelect)
    level = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我从更高的层面、更抽象的角度来思考当前的情况',widget=widgets.RadioSelect)
    human_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为其他人类玩家关注金钱收入', widget=widgets.RadioSelect)
    ChatGPT_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家关注金钱收入', widget=widgets.RadioSelect)
    human_equal_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为其他人类玩家的行为可以视作他关注金钱收入', widget=widgets.RadioSelect)
    ChatGPT_equal_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家的行为可以视作他关注金钱收入', widget=widgets.RadioSelect)
    ChatGPT_code_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家关注金钱收入的行为完全是由其编程的方式驱使的', widget=widgets.RadioSelect)
    behavior_diff = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家的行为和人类玩家有差别', widget=widgets.RadioSelect)
    treat_diff = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为我对待ChatGPT玩家和对待真人玩家有区别', widget=widgets.RadioSelect)
    ChatGPT_self = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家的游戏行为经过了他自身的思考', widget=widgets.RadioSelect)
    agent = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'不一定'],[4,'同意'],[5,'非常同意']], label='若能选择代理替代我游戏，我会选择ChatGPT来代替我进行游戏', widget=widgets.RadioSelect)
    total_payoff = models.CurrencyField()
    game_to_pay = models.IntegerField()
    final_pay = models.FloatField()#防止html里有个“点”字，不方便展现人民币
    final_paypay = models.FloatField()#加了出场费
    suggestion = models.LongStringField(label='您的建议')
def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]
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
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'major', 'grade', 'GPT']
class Survey1(Page):
    form_model = 'player'
    form_fields = ['worry', 'welfare', 'income','others','connect']
class Survey2(Page):
    form_model = 'player'
    form_fields = ['team', 'pay', 'other_influnce','altruistic']
class Survey3(Page):
    form_model = 'player'
    form_fields = ['expect','fair','other_perspective','norm','fair_worry']
class Survey4(Page):
    form_model = 'player'
    form_fields = ['ontime','overall','level']
class Survey5(Page):
    form_model = 'player'
    form_fields = ['human_driven','ChatGPT_driven','human_equal_driven','ChatGPT_equal_driven','ChatGPT_code_driven']
class Survey6(Page):
    form_model = 'player'
    form_fields = ['behavior_diff','treat_diff','ChatGPT_self','agent']
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        '''
        list=['trust','ultimatum','pd','dictator','punishment_simple','guess_three_fourth','bret_simple']
        participant.random_game = random.randint(1,7) - 1
        player.game_to_pay = participant.random_game + 1 #从列表下标转为正常开始的顺序
        participant.game_to_pay =list[participant.random_game]
        participant.payoff = getattr(participant, participant.game_to_pay)
        player.payoff = participant.payoff
        #participant.payoff = participant.trust + participant.ultimatum + participant.pd + participant.dictator + participant.punishment_simple + participant.guess_three_fourth + participant.bret_simple
        player.total_payoff = participant.payoff
        '''
        divide = participant.lowcredit / participant.credit
        participant.payoff = participant.trust + participant.ultimatum + divide * participant.pd + participant.dictator + divide * participant.punishment_simple + participant.guess_three_fourth + participant.bret_simple
        player.final_pay = float(participant.payoff * participant.credit)
        player.final_paypay = float(player.final_pay + C.showup)
class Suggestion(Page):
    form_model = 'player'
    form_fields = ['suggestion']
class End(Page):
    form_model = 'player'
page_sequence = [Label1, LabelWaitPage, LabelResults, Demographics, Survey1 ,Survey2,Survey3,Survey4,Survey5,Survey6,Suggestion,End]