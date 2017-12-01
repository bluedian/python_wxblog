# -*- coding:utf-8 -*-
import requests


def getVer():
    return 1

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

def getHtml(url):

    if url is None:
        return None
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }

    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    if (r.status_code) != 200:
        return r.status_code
    return r.text

def updataBlogServer(url, updata):

    if url is None:
        url = 'http://localhost/blog/api/upblog'

    print(url)
    r = requests.post(url, data=updata)
    r.encoding = r.apparent_encoding
    if (r.status_code) != 200:
        return r.status_code
    return r.text
