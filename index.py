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
        print('下面是连接数据')
        linkdata['cateid'] = cateid
        print(linkdata)

        upstatus = request.updataBlogServer(urls.jobsUpUrl, updata=linkdata)
        print(upstatus)


if __name__ == '__main__':
    #2017年11月30日更新

    for cid in urls.spiderNum:
        print(cid)
        for page in range(1, 5):

            spiderAllUrl = (urls.spiderUrl % (cid, page))
            print(spiderAllUrl)

            time.sleep(5)
            run(spiderAllUrl, cateid=cid)






