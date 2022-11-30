import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'df8364e5b34ace61b76dd31f179b3238'
redirect_uri = 'https://naver.com'
authorize_code = 'iW3toHHRzA8S_9qZdeIqTU3Sgq836UcbdQmxiRsEzHGD2dT9y1I0202TOZtzt542ezppBAopcNEAAAGEx4QJcQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)