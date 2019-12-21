import requests
import time
import random

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
            print('something wrong, contact wechat yunzhi_gao, owner of the script')
    except:
        print("Connect failed, sleep for few seconds then try again..")
        time.sleep(random.randint(1, 10))
