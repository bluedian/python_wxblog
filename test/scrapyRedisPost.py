#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Guos
import requests
import time
import json
from bs4 import BeautifulSoup

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


def urlToUrl(urlstr):
    return urlstr.replace('3×tamp', '3&timestamp')


def htmlToListWx(htmltext):
    soup = BeautifulSoup(htmltext, "html.parser")
    num = 0
    try:
        for p1 in soup.find_all('li'):
            name = p1.find('h3').string
            tag = p1.p.string
            url = p1.find('a').get('href')
            img = p1.find('img').get('src')
            wxtitle = p1.find(class_="account").string
            wxurl = p1.find(class_="account").get('href')
            upData = {
                'name': name,
                'tag': tag,
                'img': img,
                'url': urlToUrl(url),
                'wxtitle': wxtitle,
                'wxurl': urlToUrl(wxurl),
                'cateid':cateid
            }
            print(upData)
            upjson= json.dumps(upData, ensure_ascii=False).encode("UTF-8")
            num=num+1
            print(num)
            print(urlToHtml(redisUrl, getType=False, datas=upjson))

    except:
        return num
    return num


if __name__ == '__main__':
    beseUrl = 'http://wx.sogou.com/pcindex/pc/pc_%d/%d.html'
    redisUrl="http://118.190.45.192:8080/qq-server/guosong/spider"
    nnn=0

    #cateid = input("cateid: ")

    for cid in range(0,20):

        cateid=str(cid)

        for i in range(1, 15):
            getUrl = ('http://wx.sogou.com/pcindex/pc/pc_%s/%d.html' % (cateid, i))
            print(getUrl)
            getWxHtml = urlToHtml(getUrl)

            if getWxHtml!=False:
                getWxList = htmlToListWx(getWxHtml)
                nnn = nnn + getWxList
        print(nnn)