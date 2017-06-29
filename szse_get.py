import requests
from bs4 import BeautifulSoup
import re
from multiprocessing.dummy import Pool
from pymongo import MongoClient
import config

##巨潮资讯网  深市公告部分

connection = MongoClient(host=config.db_host, port=config.db_port)
db = connection[config.db_name]
szse_col_tab1 = db[config.db_col_szse_tab1]
szse_col_tab2 = db[config.db_col_szse_tab2]
szse_col_tab3 = db[config.db_col_szse_tab3]

category = '非许可和许可类重组问询函'
source = '深交所'

db.szse.drop()
headers = {'Host': 'www.szse.cn',
           'Origin': "http://www.szse.cn",
           'Referer': 'http://www.szse.cn/main/disclosure/jgxxgk/wxhj/',
           'Cookie': 'wP_h=16b53bfdb072ab94aedc732b5f479ef263f598ce',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'
           }

datalist1 = []
datalist2 = []
datalist3 = []


def get_html1(index):
    try:
        beginurl = 'http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=7&AJAX=AJAX-TRUE&CATALOGID=main_wxhj&TABKEY=tab1&tab1PAGENO=1'
        pageurl = beginurl[:-1] + str(index)
        print('第' + str(index) + '页开始++++++++++++++++++++++++++')
        res = requests.get(pageurl, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        table = soup.find('table', id='REPORTID_tab1')
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == 6:
                code = tds[0].text

                name = tds[1].text

                date = tds[2].text

                classify = tds[3].text

                a = tds[4].find_all('a')[0].get('onclick')
                p = re.compile("encodeURIComponent\(('.*')\)")
                link = p.findall(a)[0][1:-1]

                reply_title = tds[5].text
                result = {}
                if reply_title != '':

                    if classify == '非许可类重组问询函' or classify == '许可类重组问询函':
                        # print(reply_title)
                        b = tds[5].find_all('a')[0].get('onclick')

                        link2 = p.findall(b)[0][1:-1]
                        result = {'code': code, 'name': name, 'date': date, 'category': classify, 'content': link,
                                  'reply_title': reply_title, 'reply_content': link2}
                else:
                    if classify == '非许可类重组问询函' or classify == '许可类重组问询函':
                        result = {'code': code, 'name': name, 'date': date, 'category': classify, 'content': link}
                if result not in datalist1:
                    datalist1.append(result)
        print('第' + str(index) + '页结束=====================================')
    except:
        print('第' + str(index) + '页出错！！！！！！！！！！！！！！！！！！！！！！！')
        get_html1(index)


def get_html2(index):
    try:
        beginurl = 'http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=7&AJAX=AJAX-TRUE&CATALOGID=main_wxhj&TABKEY=tab2&tab2PAGENO=1'
        pageurl = beginurl[:-1] + str(index)
        print('第' + str(index) + '页开始++++++++++++++++++++++++++')
        res = requests.get(pageurl, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        table = soup.find('table', id='REPORTID_tab2')
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == 6:
                code = tds[0].text

                name = tds[1].text

                date = tds[2].text

                classify = tds[3].text

                a = tds[4].find_all('a')[0].get('onclick')
                p = re.compile("encodeURIComponent\(('.*')\)")
                link = p.findall(a)[0][1:-1]

                reply_title = tds[5].text
                result = {}
                if reply_title != '':

                    if classify == '非许可类重组问询函' or classify == '许可类重组问询函':
                        # print(reply_title)
                        b = tds[5].find_all('a')[0].get('onclick')

                        link2 = p.findall(b)[0][1:-1]
                        result = {'code': code, 'name': name, 'date': date, 'category': classify, 'content': link,
                                  'reply_title': reply_title, 'reply_content': link2}
                else:
                    if classify == '非许可类重组问询函' or classify == '许可类重组问询函':
                        result = {'code': code, 'name': name, 'date': date, 'category': classify, 'content': link}
                if result not in datalist2:
                    datalist2.append(result)
        print('第' + str(index) + '页结束=====================================')
    except:
        print('第' + str(index) + '页出错！！！！！！！！！！！！！！！！！！！！！！！')
        get_html2(index)


def get_html3(index):
    try:
        beginurl = 'http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=7&AJAX=AJAX-TRUE&CATALOGID=main_wxhj&TABKEY=tab3&tab3PAGENO=1'
        pageurl = beginurl[:-1] + str(index)
        print('第' + str(index) + '页开始++++++++++++++++++++++++++')
        res = requests.get(pageurl, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        table = soup.find('table', id='REPORTID_tab3')
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == 6:
                code = tds[0].text

                name = tds[1].text

                date = tds[2].text

                classify = tds[3].text

                a = tds[4].find_all('a')[0].get('onclick')
                p = re.compile("encodeURIComponent\(('.*')\)")
                link = p.findall(a)[0][1:-1]

                reply_title = tds[5].text
                result = {}
                if reply_title != '':

                    if classify == '非许可类重组问询函' or classify == '许可类重组问询函':
                        # print(reply_title)
                        b = tds[5].find_all('a')[0].get('onclick')

                        link2 = p.findall(b)[0][1:-1]
                        result = {'code': code, 'name': name, 'date': date, 'category': classify, 'content': link,
                                  'reply_title': reply_title, 'reply_content': link2,
                                  'download_content':'http://www.szse.cn/UpFiles/fxklwxhj/'+link,
                                  'download_reply':'http://www.szse.cn/UpFiles/fxklwxhj/'+link2}
                else:
                    if classify == '非许可类重组问询函' or classify == '许可类重组问询函':
                        result = {'code': code, 'name': name, 'date': date, 'category': classify, 'content': link,
                                  'download_content': 'http://www.szse.cn/UpFiles/fxklwxhj/' + link}
                if result not in datalist3:
                    datalist3.append(result)
        print('第' + str(index) + '页结束=====================================')
    except:
        print('第' + str(index) + '页出错！！！！！！！！！！！！！！！！！！！！！！！')
        get_html3(index)


if __name__ == '__main__':
    print('主板开始')
    pool1 = Pool()
    pool1.map(get_html1, [x for x in range(1, 43)])
    szse_col_tab1.insert_many(datalist1)
    print('主板结束')
    print('中小板开始')
    pool2 = Pool()
    pool2.map(get_html2, [x for x in range(1, 41)])
    szse_col_tab2.insert_many(datalist2)
    print('中小板开始')
    print('创业板开始')
    pool3 = Pool()
    pool3.map(get_html3, [x for x in range(1, 28)])
    szse_col_tab3.insert_many(datalist3)
    print('创业板jieshu')
