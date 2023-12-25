#encoding: utf-8

def getResponseText(path, startAt, maxResults, count):
    import requests
    from requests import RequestException
    import json
    import base64

    # print("called:" + str(count))
    # symbols
    auth = ""
    header = {}
    method = ""
    url = ""
#    pem = ""

    with open(path,encoding="utf-8",mode='r') as f:
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
          "&startAt=" + \
          str(startAt) + \
          "&maxResults=" + \
          str(maxResults)
# print (auth)

# additional settings
        cred = "Basic " + base64.b64encode(bytes(auth.replace('\'',''),"utf-8")).decode("utf-8")
        header['Authorization'] = cred


        # request
        response = requests.request(
            method,
            url=url,
            headers=header
            )
#        print(response.text)
        return json.loads(response.text)




# Is it better to use argument?
PATH = "./myconf/setting.json"

maxResults = 100
startAt = 0
call_count = 0
# 設定ファイルから読み出し


# maxResult => 100
# total = 270
# startAt = 0
while True:
    data = getResponseText(PATH, startAt, maxResults, call_count)
    print("startAt:", startAt, \
          "maxResults:", maxResults, \
          "call_count:", call_count)
    total = int(data["total"])
    print ("total:", total)

#    print (data)
    for issuekey in data["issues"]:
        print(issuekey["key"])

    call_count += 1 # it can use filename...?
#    print(call_count,"\n")
    startAt = startAt + maxResults
    if total < startAt:
        break
# やること
# APIコールの回数に制限をかける。最大でも1000件までの取得となるようにする
# maxresultsが100の場合10回までのコールに制限)

# print("APIcall count: " + str(call_count))

#parse json
