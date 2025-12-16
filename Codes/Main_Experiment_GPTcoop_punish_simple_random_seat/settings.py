from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.25, participation_fee=10)
SESSION_CONFIGS = [dict(name='games', num_demo_participants=4, app_sequence=['general_instruction','trust','Ultimatum','Repeated_PD','Repeated_PD2','Repeated_PD3','Repeated_PD4','Repeated_PD5','Repeated_PD6','Repeated_PD7','Repeated_PD8','dictator','punishment_simple','guess_three_fourth','bret_simple','after_survey'])]
LANGUAGE_CODE = 'zh-hans'
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['label1','credit','lowcredit','trust','ultimatum','pd1','pd2','pd3','pd4','pd5','pd6','pd7','pd8','pd','pd_block','dictator','punishment_simple','simple_punishment','guess_three_fourth','bret_simple','random_game','game_to_pay']
SESSION_FIELDS = []
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


