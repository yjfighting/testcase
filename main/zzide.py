# -*- coding: utf-8 -*-
'''
@Author: fiyc
@Date : 2018-12-09 13:33
@FileName : jsonTest.py
@Description :
    - python读取json转obj
'''
import os
import json

cwd = os.path.dirname(os.path.realpath(__file__))
targetFile = os.path.join(cwd, "testcase.txt")


f = open(targetFile, 'r', encoding='utf-8')
content = f.read()
if content.startswith(u'\ufeff'):
    content = content.encode('utf8')[3:].decode('utf8')

f.close()
obj = json.loads(content)

a = obj['result']['Result'][0]['RoomList']
b = obj['result']['Result'][0]['RoomList'][0]['HotelId']
c = obj['result']['Result'][0]['SessionId']
d = obj['result']['Code']
if obj['result']['Code']==0:
    print(d)
    print(type(a))
    i = 0
    j = 0
    rateinfoList = []
    ratecodelist = []
    attchmentlist = []
    for i in range(0,len(a)):
        rateinfoList.append(a[i]['RateInfoList'])
        #print(rateinfoList[0])
        for j in range(0,len(rateinfoList[i])):
            ratecodelist.append(a[i]['RateInfoList'][j]['RateCode'])
            attchmentlist.append(a[i]['RateInfoList'][j]['AttachmentKey'])
            #print(rateinfoList,attchmentlist)

    print(type(obj))
    print(ratecodelist,attchmentlist)
else:
    print('1')