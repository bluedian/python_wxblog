# -*- coding:utf-8 -*-
from config import urls
from fun import request
from fun import buss

import time


def run(url, cateid=1):
    listhtml = request.getHtml(url)
    if listhtml is None:
        print('网页内容为空')
        exit()
    lists = buss.htmlToLists(listhtml)
    if lists is None:
        print('返回列表内容为空')
        exit()

    for linkdata in lists:
        linkdata['cateid'] = cateid
        upstatus = request.updataBlogServer(urls.jobsUpUrl, updata=linkdata)
        print(upstatus)


if __name__ == '__main__':
    #2017年11月30日更新
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    for cid in urls.spiderNum:
        for page in range(1, 10):
            spiderAllUrl = (urls.spiderUrl % (cid, page))
            time.sleep(5)
            run(spiderAllUrl, cateid=cid)


