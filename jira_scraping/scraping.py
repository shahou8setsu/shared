import requests
from requests import RequestException
import json
import base64

PATH = "./conf/setting.json"

# symbols
auth = ""
header = {}
method = ""
url = ""
pem = ""

# 設定ファイルから読み出し
with open(PATH,encoding="utf-8",mode='r') as f:
    settings = json.load(f)
    email = repr(str(settings['user']['email']))
    token = repr(str(settings['user']['token']))
    auth = (email+r':'+token).replace('\n','').replace('\'','')
    header = settings['header']
    method = str(settings['header']['Method'])
    url = str(settings['url']['target']) + \
          str(settings['url']['path']) + \
          "fields=" + \
          str(settings['url']['fields']) + \
          "&jql=" + \
          str(settings['url']['jql']) + \
          "&maxResults=" + \
          str(settings['url']['maxResults'])

print (auth)

# additional settings 
cred = "Basic " + base64.b64encode(bytes(auth.replace('\'',''),"utf-8")).decode("utf-8")
header['Authorization'] = cred


# request
response = requests.request(
    method,
    url=url,
    headers=header
    )
print(response.text)
# data = json.loads(response.text)


