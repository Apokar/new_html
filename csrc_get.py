import requests
from bs4 import BeautifulSoup
import os
import time
from pymongo import MongoClient
import config

# 证监会

connection = MongoClient(host=config.db_host, port=config.db_port)
db = connection[config.db_name]
csrc_col = db[config.db_col_csrc]

category = '沪市公告—最新'
source = '巨潮资讯网'

db.csrc_list.drop()
dir_name = '/Users/S1Lence/Desktop/new_html/csrc'
artilces_url = []

headers = {
    'Host': 'www.csrc.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0'
}
urls = []
datalist = []
for i in range(25):

    if i == 0:
        urls.append(
            'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index.htm'
        )
    else:
        urls.append(
            'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/index_' + str(i) + '.htm'
        )


def findHtml(url):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        content1 = soup.find('div', class_='er_right')
        if content1:

            ul = content1.find('ul', id='myul')
            lis = ul.find_all('li')
            for ct in lis:
                a = ct.find('a')
                href = a.get('href')
                date = ct.find('span').text
                timeArray = time.strptime(date, "%Y-%m-%d")
                timeStamp = int(time.mktime(timeArray))



                title = a.text.encode('latin1').decode('utf-8')

                result = {'title': title, 'href': href,
                      'download_url': 'http://www.csrc.gov.cn/pub/newsite/ssgsjgb/bgczfkyj/' + href, 'time': date,'timeStamp':timeStamp}
                datalist.append(result)

    except:
        findHtml(url)


for url in urls:
    findHtml(url)

csrc_col.insert_many(datalist)