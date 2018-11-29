# -*- coding:utf-8 -*-

from config import urls
import requests
import json

# 2017年12月4日修改增加了For
for i in range(1, 10):

    try:

        print('共三步,第一步:取服务器人员已处理好的微信数据')
        r = requests.get(urls.jobsUrl)
        print(r.status_code)
        jobs = r.text
        print('任务服务器:'+jobs)
        jobs_json = json.loads(jobs)

        jobs_id = jobs_json[0]['id']
        jobs_data = jobs_json[0]
        print(jobs_data)
        #jobs_data['createUserId'] = 5

        test_url = jobs_data['contentUrl']
        print(test_url)
        r = requests.get(test_url)
        testcontext = r.text
        print(r.status_code)
        # if testcontext.find('系统出错') > 1:
        #    exit()

        print('共三步,第二步:向总服务器进行提交数据')
        r = requests.post(urls.postUrl, json=jobs_data)
        print(r.status_code)
        status_message = r.text

        print('共三步,第三步:上传完成后把结果给运维服务器')
        ok_data = {
            'id': jobs_id,
            'status_message': status_message
        }
        r = requests.post(urls.jobsOKUrl, data=ok_data)
        print(r.status_code)
        print(r.text)
    except:
        print('系统出问题了_并退出')
        exit()
