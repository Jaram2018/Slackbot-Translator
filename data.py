from enum import Enum
import os
import json

credentials = None
with open('credentials.json', 'r') as fr:
    credentials = json.loads(fr.read())

# For using Heroku
class SlackUrls(Enum):
    base_url = 'https://slack.com/api/rtm.connect?token='
    token = credentials['SLACKBOT_TOKEN']

class NaverUrls(Enum):
    client_id = credentials['PAPAGO_CLIENT_ID']
    client_secret = credentials['PAPAGO_CLIENT_SECRET']
    """
    < 네이버 파파고 API >
    1. 네이버 개발자 센터 파파고 API 신청 (https://developers.naver.com/apps/#/register?api=ppg_n2mt).
    2. 사용 API - 'Papago NMT 번역' 으로 설정하고, 비로그인 오픈 API 서비스 환경을 'WEB 설정' 으로 등록.
    3. client_id 와 client_secret 키를 발급.
    """