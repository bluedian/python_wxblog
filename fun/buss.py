# -*- coding:utf-8 -*-
#解析网络连接及内容

from bs4 import BeautifulSoup


def getVer():
    return 1

def urlToUrl(urlstr):
    return urlstr.replace('×tamp', '&timestamp')


def htmlToLists(htmltext):
    links = []
    if htmltext is None:
        print('html')
        return
    try:
        soup = BeautifulSoup(htmltext, "html.parser")
        for p1 in soup.find_all('li'):
            title = p1.find('h3').string
            tag = p1.p.string
            url = p1.find('a').get('href')
            wxaccount = p1.find(class_="account").string
            wxaccounturl = p1.find(class_="account").get('href')
            upData = {
                'cateid': 0,
                'title': title,
                'tag': tag,
                'wxaccount': wxaccount,
                'url': urlToUrl(url),
                'wxaccounturl': urlToUrl(wxaccounturl),
            }
            #print(upData)
            links.append(upData)
        return links
    except:
        return
