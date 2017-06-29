import requests
import os
import re
from pymongo import MongoClient
import config

##巨潮资讯网  深市公告部分

connection = MongoClient(host=config.db_host, port=config.db_port)
db = connection[config.db_name]
cninfo_col_sz = db[config.db_col_sz]
datalist=[]
category = '深市公告—最新'
source = '巨潮资讯网'
db.cninfo_sz.drop()

for i in range(1, 30):#1394-30
    dir = '/Users/S1Lence/Desktop/new_html/cninfo'

    payload = {'column': 'szse', 'columnTitle': '深市公告', 'pageNum': str(i), 'pageSize': '50', 'tabName': 'latest'}
    res = requests.post('http://www.cninfo.com.cn/cninfo-new/disclosure/szse_latest', data=payload)
    content = res.json()
    c = content['classifiedAnnouncements']
    for bb in c:
        for b in bb:
            b['download_url'] ='http://www.cninfo.com.cn/'+b.get('adjunctUrl')

    if c not in datalist:
        datalist.append(c)

for a in datalist:
    # print(a)#[[
    for b in a:

         cninfo_col_sz.insert_many(b)

