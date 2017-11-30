# -*- coding:utf-8 -*-

import requests
import json

datas = {
    'type': '3',
    'contentText': '历害呀!我的大成都',
    'contentUrl': 'https://mp.weixin.qq.com/s?src=11&timestamp=1511946002&ver=543&signature=QDvyYvhnkU4vwpydtm3zcobXfn3cGPu6vsN3MODhLAAYpdV1A6nrTMVJViidVP14HChq4WwaQDde3Iu-eOzlF9TSMFB8KIsZYgvqFfH2m3wmzk9*D2PB-dBdQInVZso*&new=1'
}

postUrl = 'http://118.190.45.100/mm-admin/api/v1/article'
jobsUrl = 'http://localhost/blog/api/upServer'
jobsOKUrl = 'http://localhost/blog/api/upJobsOK'

r = requests.get(jobsUrl)


jobs=r.text
print(jobs)
print(type(jobs))
print('-----------')
jobs_json = json.loads(jobs)
print(jobs_json)
print(type(jobs_json))

jobs_id=jobs_json[0]['id']

print(jobs_id)

datas={
    'type': '3',
    'contentText': jobs_json[0]['contentText'],
    'contentUrl': jobs_json[0]['contentUrl']
}

print(datas)
print(type(datas))

okData={
    'id':jobs_id
}

r_ok = requests.post(jobsOKUrl, data=okData)

r_ok_text=r_ok.text
print(r_ok_text)
print(type(r_ok_text))
exit()





rgo = requests.post(postUrl, json=datas)

print(rgo.status_code)
print(rgo.text)




