# -*- coding:utf-8 -*-

import requests

test_url1 = 'http://mp.weixin.qq.com/s?src=11&timestamp=1512358201&ver=553&signature=76XO0AP77PINuRwPA*5bFQI3KPhAM2mpr53h8I4DKZqKhDXx6hCQMIaSXu6s9KVgCSm1axUqZsV27gN5IWa7caUDYUqAW9y*m5m6gPfNCGUz9dY5sXr46d1tFCrxCfNK&new=1'

test_url2 = 'https://mp.weixin.qq.com/s?src=11&timestamp=1506222022&ver=411&signature=da9kWIZVZRO*GCPpotjanTY2vBDidKveCrThPkp7zm4wLOkdNNnHoTkb9Z7wFzL4oI8zzUAVFjYCMSQZjcCuVY0YxRfs5GUmD-IfX3ZQLJmEqJnZe4IR34pfCY*5Yx8G&new=1'

print(test_url1)

r = requests.get(test_url1)
testcontext = r.text
if testcontext.find('系统出错') > -1:
    print(testcontext.find('系统出错'))
    print('test1__找到字付串')

r = requests.get(test_url2)
testcontext = r.text
if testcontext.find('系统出错') > 10000:
    print(testcontext.find('系统出错'))
    print('test2__找到字付串')