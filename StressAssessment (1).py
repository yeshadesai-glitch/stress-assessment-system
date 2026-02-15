weights={'sleep':3,'emotion':3,'energy':2,'nutrition':2,'concentration':2,'mental':2,'procrastination':2,'emotional_reactivity':2,'motivation':2,'restlessness':2,'physical':1,'social':1,'screen_time':1}
severity={1:2,2:1,3:0}
stress_scores={}
questions={
    'sleep':{
        'question': 'Over the past 7 days, how would you describe your sleep?', 
        'options': ('1. Poor (difficulty falling asleep/waking up tired)',
                    '2.Average (some disturbance)',
                    '3. Good (restful and consistent)' )
},
'emotion':{
    'question':'Over the past 7 days, how often have you felt internally irritable, anxious, or emotionally overwhelmed?',
    'options':('1. Often',
              '2. Sometimes',
              '3. Rarely')
},
'energy':{
    'question':'Over the past 7 days, how would you rate your daily energy levels?',
    'options':('1. Low (tired most of the day)',
                '2. Moderate',
                '3. High')
},
'nutrition':{
    'question':'Over the past 7 days, how regular and balanced were your meals?',
    'options':('1. Irregular/frequently skipped (noticed a loss of appetite)',
               '2. Mostly regular',
               '3. Regular and balanced')
},
'concentration':{
    'question':'Over the past 7 days, how well were you able to concentrate on tasks and studies? (Did you do it willingly?)',
    'options':('1. Poor focus',
               '2. Average focus',
               '3. Good focus')
},
'physical':{'question':'Over the past 7 days, have you experienced physical discomfort often linked to stress (e.g. headaches,muscle tension, etc.)',
            'options': ('1. Frequently', 
                        '2. Occasionally',
                        '3. Rarely / not at all')
},
'social': {'question': 'Over the past 7 days, how often did you feel like avoiding social interaction?',
           'options': ('1. Often',
                       '2. Sometimes',
                       '3. Rarely')
},
'mental': {'question':'Over the past 7 days, how often did you feel mentally "cluttered" or unable to think clearly?',
           'options': ('1. Frequently',
                       '2. Occasionally',
                       '3. Rarely')
},
'procrastination': {'question':'Over the past 7 days, did you delay important tasks even when you knew they needed attention?',
                    'options': ('1. Yes, often',
                                '2. Sometimes',
                                '3. Rarely')
},
'emotional_reactivity':{'question':'Over the past 7 days, did you react more strongly towards others than usual due to minor issues?',
                        'options':('1. Yes, often',
                                   '2. Sometimes',
                                   '3. No')
},
'restlessness':{'question':'Over the past 7 days, did you feel physically restless or unable to relax?',
                'options':('1. Often',
                           '2. Sometimes',
                           '3. Rarely')
},
'screen_time':{'question':'Over the past 7 days, did you resort to social media rather than prioritizing important work?',
               'options':('1. Frequently',
                          '2. Occasionaly',
                          '3. Rarely')
},
'motivation':{'question':'Over the past 7 days, how motivated did you feel to complete responsibilities/tasks?',
              'options':('1. Low',
                         '2. Moderate',
                         '3. High')
}}

for factor,value in questions.items():
    print(value['question'])
    for option in value['options']:
        print(option)
    answer=int(input('Answer (1-3): '))
    print('---------------------------------------------------')
    factor_score=severity[answer]*weights[factor]
    stress_scores[factor]=factor_score
stress_score=sum(stress_scores.values())
print('Stress Score: ',stress_score,'/50')
print('Factor Breakdown:')
for key, value in stress_scores.items():
    max_score=severity[1]*weights[key]
    print(key,':',value,'/',max_score)

if stress_score in range(0,15):
    print('You are Managing Stress Well\n Your responses show healthy balance in sleep, energy, and emotions.\n Keep maintaining your routine.\n What to Do:\n    Maintain regular sleep.\n   Stay active.\n  Take breaks when needed. \n Keep a balanced daily schedule.' )
elif stress_score in range (15,25):
    print ('Early Signs of Stress \nSome stress patterns are starting to show. \nThis is the best time to take action.\n What to Do: \n Improve sleep timing. \n    Reduce night screen use \n Plan tasks in small steps. \n   Add short daily movement.')
    print('Retest recommended in 7 days.')
elif stress_score in range (25,35):
    print('Moderate Stress Detected \nStress may be affecting concentration, mood, or energy levels. \n What to Do: \n  Fix sleep schedule. \n Break big tasks into small goals. \n Practice slow breathing (4-4-6 pattern). \n Talk to a trusted adult if needed.')
    print('Retest recommended in 7 days.')
elif stress_score >= 35:
    print('High Stress Level Detected \nYour responses suggest strong and ongoing stress activation. \n What to Do: \n  Prioritize sleep immediately. \n   Reduce unnecessary workload. \n  Limit excessive screen time. \n  Use breathing or grounding exercises. \n  Speak to a parent, teacher, or counselor.')
    print('Retest recommended in 7 days. If stress remains high, seek adult or professional guidance.')