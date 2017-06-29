import requests
import re
import simplejson
from pymongo import MongoClient
import config
#上海证券交易所

connection = MongoClient(host=config.db_host, port=config.db_port)
db = connection[config.db_name]
sse_col = db[config.db_col_sse]
datalist=[]
db.sse.drop()
headers = {'Host': 'query.sse.com.cn',
           'Referer': 'http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0'
           }
for i in range(1, 43):
    url = 'http://query.sse.com.cn/commonSoaQuery.do?jsonCallBack=jsonpCallback29292&siteId=28&sqlId=BS_GGLL&extGGLX=&stockcode=&channelId=10743%2C10744%2C10012&extGGDL=&order=createTime%7Cdesc%2Cstockcode%7Casc&isPagination=true&pageHelp.pageSize=15&pageHelp.pageNo='+str(i)+'&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1498029405034'
    r = requests.get(url, headers=headers)
    p = re.compile('jsonpCallback29292\((.*)\)')
    content = simplejson.loads(p.findall(r.text)[0])

    data = content['pageHelp']
    d = data['data']


    sse_col.insert_many(d)