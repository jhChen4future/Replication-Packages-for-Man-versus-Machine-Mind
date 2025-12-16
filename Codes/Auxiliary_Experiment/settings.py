from os import environ
import random
app_sequence = [
    'general_instruction',
    'ug1', 'tg1', 'pd1',
    'ug2', 'tg2', 'pd2',
    'ug3', 'tg3', 'pd3',
    'ug4', 'tg4', 'pd4',
    'ug5', 'tg5', 'pd5',
    'ug6', 'tg6', 'pd6',
    'after_survey'
]

start = ['general_instruction']
end = ['bret','after_survey']
middle_blocks = [app_sequence[i:i+3] for i in range(1, len(app_sequence)-1, 3)]
for block in middle_blocks:
    random.shuffle(block)
shuffled_sequence =  start + [item for block in middle_blocks for item in block] + end

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.25, participation_fee=10)
SESSION_CONFIGS = [dict(name='games', num_demo_participants=4, app_sequence=shuffled_sequence)]
LANGUAGE_CODE = 'zh-hans'
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['label1','ug1guess', 'ug1payoff', 'ug2guess', 'ug2payoff', 'ug3guess', 'ug3payoff', 'ug4guess', 'ug4payoff', 'ug5guess', 'ug5payoff', 'ug6guess', 'ug6payoff',
'tg1guess', 'tg1payoff', 'tg2guess', 'tg2payoff', 'tg3guess', 'tg3payoff', 'tg4guess', 'tg4payoff', 'tg5guess', 'tg5payoff', 'tg6guess', 'tg6payoff',
'pd1guess', 'pd1payoff', 'pd2guess', 'pd2payoff', 'pd3guess', 'pd3payoff', 'pd4guess', 'pd4payoff', 'pd5guess', 'pd5payoff', 'pd6guess', 'pd6payoff',
                      'finalpayoff','guesspayoff','totalpay','guesspayoff_name','finalpayoff_name','lottery','bret']
DEBUG = False
ROOMS = [
    dict(
        name='HumanwithGPT',
        display_name='HumanwithGPT',
        #use_secure_url = True
        participant_label_file='_rooms/jointhegame.txt',  #if you don't want to assign a particular number to participants and more security, this can be neglected #if you want everyone to enter a label, just use the url
    ),
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab'
    ),  #another room name, no true meaning
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


#['general_instruction','ug1','tg1','pd1','ug2','tg2','pd2','ug3','tg3','pd3','ug4','tg4','pd4','ug5','tg5','pd5','ug6','tg6','pd6','after_survey']