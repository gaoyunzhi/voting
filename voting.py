# -*- coding: utf-8 -*-

import time
import random
import os
import sys

if sys.version_info[0] == 3:
    pythonv = '3'
else:
    pythonv = ''

try:
    import requests
except:
    r = os.system('pip%s install -r requirements.txt' % pythonv)
    if r != 0:
        os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
        os.system('python%s get-pip.py' % pythonv)
        os.system('rm get-pip.py')
        os.system('pip%s install -r requirements.txt' % pythonv)
    import requests

VOTING_URL = 'https://sv.ifeng.com/index.php/survey/postsurvey?sur[32486][]=127074&id=15990&act=postsurvey&surid=15990&ref=http%3A%2F%2Ffinance.ifeng.com%2Fsurvey.html&callback=postSurveyData'
SUCCESS = '\\u6295\\u7968\\u6210\\u529f\\uff0c\\u611f\\u8c22\\u60a8\\u53c2\\u4e0e' # 投票成功，感谢您参与'

count = 0
while True:
    try:
        session = requests.Session()
        result = session.get(VOTING_URL, verify=False).text
        if SUCCESS in result:
            count += 1
            print('voted, count:', count)
        else:
            time.sleep(random.random() / 3.0)
    except:
        print("Connect failed, sleep for few seconds then try again..")
        time.sleep(random.randint(1, 10))
