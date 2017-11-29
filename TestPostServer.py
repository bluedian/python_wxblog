# -*- coding:utf-8 -*-

import requests

datas = {
    'type': '3',
    'contentText': '历害呀!我的大成都',
    'contentUrl': 'https://mp.weixin.qq.com/s?src=11&timestamp=1511946002&ver=543&signature=QDvyYvhnkU4vwpydtm3zcobXfn3cGPu6vsN3MODhLAAYpdV1A6nrTMVJViidVP14HChq4WwaQDde3Iu-eOzlF9TSMFB8KIsZYgvqFfH2m3wmzk9*D2PB-dBdQInVZso*&new=1'
}

postUrl = 'http://118.190.45.100/mm-admin/api/v1/article'

r = requests.post(postUrl, json=datas)

print(r.status_code)
print(r.text)