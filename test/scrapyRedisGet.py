#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: Guos
import requests
import time
import json
from bs4 import BeautifulSoup


redisUrl="http://118.190.45.192:8080/qq-server/guosong/spider"
upUrl = 'http://localhost/blog/api'
#upUrl = 'http://192.168.1.197/blog/api'
rootUrl= 'http://wx.sogou.com/'
listAll = []


def urlToHtml(url, datas=None,getType=True):
    r=''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }
    if getType:
        r = requests.get(url, headers=headers, data=datas)
    else:
        r = requests.post(url, headers=headers, data=datas)
    print(r.url)
    r.encoding = 'utf-8'
    print(r.status_code)
    if (r.status_code) != 200:
        return False
    return r.text

def htmlToContext(htmltext):
    soup = BeautifulSoup(htmltext, "html.parser")
    try:
        divall = soup.find(id='js_content')
        return str(divall)
    except:
        return False

def runJobs():

    getJobs=urlToHtml(redisUrl)

    if (getJobs==False) or (len(getJobs)<100):
        print(getJobs)
        print(len(getJobs))
        return False
    else:
        getJobsJson = json.loads(getJobs)
        contextUrl=getJobsJson['url']
        contextUrlText=urlToHtml(contextUrl)
        if contextUrlText==False:
            getJobsJson['context']="False"
        else:
            getJobsJson['context']=contextUrlText

        getJobsJson['type']=2
        print(urlToHtml(upUrl,datas=getJobsJson,getType=False))
        return True

if __name__ == '__main__':

    while(True):
        noDo=runJobs()
        if noDo==False:
            exit()
        time.sleep(5)






