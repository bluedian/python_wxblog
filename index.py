# -*- coding:utf-8 -*-
from config import urls
from fun import request
from fun import buss

import time


#spiderUrl = ('http://wx.sogou.com/pcindex/pc/pc_8/1.html')




upblog = {'title': '景甜自曝在高定礼服下穿秋裤,网友赞这个仙女很真实', 'tag': '11月29日某著名杂志举办的“时尚之夜”活动，邀请了景甜、唐嫣、刘亦菲、吴秀波、李宇春等明星，现场星光熠熠，女明星纷纷穿上了惊艳的礼服，争相比美。其中景甜穿了粉色的蓬蓬裙礼服，上面还绣着飞翔的小鸟，特...', 'wxaccount': '微利宝咨询中心', 'url': 'http://mp.weixin.qq.com/s?src=11&timestamp=1512021603&ver=545&signature=8hBLrj22ArhLbHrm-ScJHn8qVppShp7Vt7YVAE7P1Z2RcdWfBxeYLCcUkrv*6MVDqJxCheYSulvQdpwo3sTN48*sYtaWJ*0D*rIG1-g5A*2kpyLQTR95qYYsyNGxHZRK&new=1', 'wxaccounturl': 'http://mp.weixin.qq.com/profile?src=3&timestamp=1512021603&ver=1&signature=S3VLeoQtM5*gDM0Z*ejKVANZ09Kn2QViF7QKUXZ*RWOLDQJcIlri1ABG2CKGHQN8c9fvJNVV22fNB4lBLalZZg=='}

blogUrl = 'http://localhost/blog/api/upblog'




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

        for page in range(1, 2):

            spiderAllUrl = (urls.spiderUrl % (cid, page))
            print(spiderAllUrl)

            time.sleep(5)

            run(spiderAllUrl, cateid=cid)






