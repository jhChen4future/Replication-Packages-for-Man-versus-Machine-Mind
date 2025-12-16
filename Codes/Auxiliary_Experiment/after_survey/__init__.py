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
    GPT = models.StringField(choices=[['极少使用（少于每月一次）', '极少使用（少于每月一次）'], ['每月大于一次', '每月至少一次'], ['每周大于三次', '每周大于三次'],['每周大于一次', '每周至少一次'], ['每天至少一次', '每天至少一次']], label='您的GPT大模型（ChatGPT、Claude、Kimi、文心一言等）使用频率', widget=widgets.RadioSelect)
    income = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我只关注自己游戏中的收入', widget=widgets.RadioSelect)
    others = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我不关心其他的参与者', widget=widgets.RadioSelect)
    team = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我不关注我的决定对集体的影响', widget=widgets.RadioSelect)
    pay = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我关注实验中的金钱回报', widget=widgets.RadioSelect)
    altruistic = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我不想尽量减少对集体的负面影响', widget=widgets.RadioSelect)
    fair = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我不想做到公平', widget=widgets.RadioSelect)
    level = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我从更高的层面、更抽象的角度来思考当前的情况',widget=widgets.RadioSelect)
    motivationH = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我做决策时认为其他人类参与者和我的行动动机相似', widget=widgets.RadioSelect)
    behaviorH = models.IntegerField(choices=[[1, '非常不同意'], [2, '不同意'], [3, '态度中立'], [4, '同意'], [5, '非常同意']],label='我做决策时认为其他人类参与者和我的行动相似', widget=widgets.RadioSelect)
    motivationG = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我做决策时认为其他GPT参与者和我的行动动机相似', widget=widgets.RadioSelect)
    behaviorG = models.IntegerField(choices=[[1, '非常不同意'], [2, '不同意'], [3, '态度中立'], [4, '同意'], [5, '非常同意']],label='我做决策时认为其他GPT参与者和我的行动相似', widget=widgets.RadioSelect)
    human_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为其他人类玩家关注金钱收入', widget=widgets.RadioSelect)
    ChatGPT_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家关注金钱收入', widget=widgets.RadioSelect)
    human_equal_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为其他人类玩家的行为可以视作他关注金钱收入', widget=widgets.RadioSelect)
    ChatGPT_equal_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家的行为可以视作他关注金钱收入', widget=widgets.RadioSelect)
    item0 = models.IntegerField(choices=[[1, '非常不同意'], [2, '不同意'], [3, '态度中立'], [4, '同意'], [5, '非常同意']],label='本题请选5，非常同意', widget=widgets.RadioSelect)
    ChatGPT_code_driven = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家关注金钱收入的行为完全是由其编程的方式驱使的', widget=widgets.RadioSelect)
    behavior_diff = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家的行为和人类玩家有差别', widget=widgets.RadioSelect)
    treat_diff = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为我对待ChatGPT玩家和对待真人玩家有区别', widget=widgets.RadioSelect)
    ChatGPT_self = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT玩家的游戏行为经过了他自身的思考', widget=widgets.RadioSelect)
    identity = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为ChatGPT接近于人类', widget=widgets.RadioSelect)
    reliable = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更可靠', widget=widgets.RadioSelect)
    predictable = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更可预测', widget=widgets.RadioSelect)
    dependable = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更值得依赖', widget=widgets.RadioSelect)
    knowledgeable = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更有见识', widget=widgets.RadioSelect)
    competent = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更有能力', widget=widgets.RadioSelect)
    efficient = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更有效率', widget=widgets.RadioSelect)
    rational = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更理性', widget=widgets.RadioSelect)
    understandable = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更容易理解', widget=widgets.RadioSelect)
    honest = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更诚实', widget=widgets.RadioSelect)
    fair_2 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更公平', widget=widgets.RadioSelect)
    empathetic = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更有同理心', widget=widgets.RadioSelect)
    caring = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更关心他人', widget=widgets.RadioSelect)
    selfless = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更无私', widget=widgets.RadioSelect)
    benevolent = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更怀有善意', widget=widgets.RadioSelect)
    polite = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更有礼貌', widget=widgets.RadioSelect)
    responsive = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更积极回应', widget=widgets.RadioSelect)
    patient = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='我认为人类比ChatGPT更有耐心', widget=widgets.RadioSelect)
    item1 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='比较安静', widget=widgets.RadioSelect)
    item2 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='心肠柔软，有同情心', widget=widgets.RadioSelect)
    item3 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='缺乏条理', widget=widgets.RadioSelect)
    item4 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='时常忧心忡忡，担心很多事情', widget=widgets.RadioSelect)
    item5 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='着迷于艺术、音乐或文学', widget=widgets.RadioSelect)
    item6 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='常常处于主导地位，像个领导一样', widget=widgets.RadioSelect)
    item7 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='有时对人比较粗鲁', widget=widgets.RadioSelect)
    item8 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='很难开始行动起来去完成一项任务', widget=widgets.RadioSelect)
    item9 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='时常觉得悲伤', widget=widgets.RadioSelect)
    item10 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='对抽象的概念和想法没什么兴趣', widget=widgets.RadioSelect)
    item11 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='精力充沛', widget=widgets.RadioSelect)
    item12 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='把人往最好的方面想', widget=widgets.RadioSelect)
    item13 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='可信赖的，可靠的', widget=widgets.RadioSelect)
    item14 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='情绪稳定，不易生气', widget=widgets.RadioSelect)
    item15 = models.IntegerField(choices=[[1,'非常不同意'],[2,'不同意'],[3,'态度中立'],[4,'同意'],[5,'非常同意']], label='有创意，能想出新点子', widget=widgets.RadioSelect)
    total_payoff = models.CurrencyField()
    final_pay = models.FloatField()#防止html里有个“点”字，不方便展现人民币
    suggestion = models.LongStringField(label='您的建议')
def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]
def set_guess_payoffs(group:Group):
    for play in group.get_players():
        participant = play.participant
        fields = [
            'ug1guess', 'ug1payoff', 'ug2guess', 'ug2payoff', 'ug3guess', 'ug3payoff', 'ug4guess', 'ug4payoff',
            'ug5guess', 'ug5payoff', 'ug6guess', 'ug6payoff',
            'tg1guess', 'tg1payoff', 'tg2guess', 'tg2payoff', 'tg3guess', 'tg3payoff', 'tg4guess', 'tg4payoff',
            'tg5guess', 'tg5payoff', 'tg6guess', 'tg6payoff',
            'pd1guess', 'pd1payoff', 'pd2guess', 'pd2payoff', 'pd3guess', 'pd3payoff', 'pd4guess', 'pd4payoff',
            'pd5guess', 'pd5payoff', 'pd6guess', 'pd6payoff'
        ]
        guess_fields = [f for f in fields if 'guess' in f]
        payoff_fields = [f for f in fields if 'payoff' in f]
        # 随机抽取字段名
        guess_field = random.choice(guess_fields)
        payoff_field = random.choice(payoff_fields)
        # 存储字段名（可选）
        participant.guesspayoff_name = guess_field
        participant.finalpayoff_name = payoff_field
        # 获取对应字段的值并赋值
        participant.guesspayoff = getattr(participant, guess_field)
        participant.finalpayoff = getattr(participant, payoff_field)
        participant.totalpay = (participant.guesspayoff + participant.finalpayoff) * 0.6 + participant.bret * 0.3
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
class Set_Guess_Payoffs(WaitPage):
    after_all_players_arrive = set_guess_payoffs
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'major', 'grade', 'GPT']
class Survey1(Page):
    form_model = 'player'
    form_fields = ['income','others','team','pay','altruistic','fair','level']
class Survey2(Page):
    form_model = 'player'
    form_fields = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']
class Survey3(Page):
    form_model = 'player'
    form_fields = ['item8', 'item9', 'item10','item11', 'item12', 'item13', 'item14', 'item15']
class Survey4(Page):
    form_model = 'player'
    form_fields = ['motivationH', 'behaviorH', 'motivationG','behaviorG']

class Survey5(Page):
    form_model = 'player'
    form_fields = ['human_driven','ChatGPT_driven','human_equal_driven','ChatGPT_equal_driven','item0','ChatGPT_code_driven','behavior_diff','treat_diff','ChatGPT_self','identity']
class Survey6(Page):
    form_model = 'player'
    form_fields = ['reliable','predictable','dependable',
'knowledgeable','competent','efficient',
'rational','understandable',
'honest']

class Survey7(Page):
    form_model = 'player'
    form_fields = ['fair','empathetic',
'caring','selfless','benevolent',
'polite','responsive','patient']
    @staticmethod
    def before_next_page(player, timeout_happened):
      participant = player.participant
      if player.item0 == 5:
          player.final_pay = float(participant.totalpay + 15)
      else:
          player.final_pay = float(participant.totalpay + 10)

class Suggestion(Page):
    form_model = 'player'
    form_fields = ['suggestion']
class End(Page):
    form_model = 'player'
page_sequence = [Set_Guess_Payoffs, Demographics, Survey1 ,Survey2, Survey3, Survey4, Survey5,Survey6, Survey7, Suggestion,End]