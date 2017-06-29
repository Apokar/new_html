import requests
from bs4 import BeautifulSoup
url = 'http://www.csrc.gov.cn/wcm/websearch/zjh_adv_list.jsp'
headers = {
    'Host': 'www.csrc.gov.cn',
    'Origin': 'http://www.csrc.gov.cn',
    'Referer': 'http://www.csrc.gov.cn/wcm/websearch/advsearch.htm',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
data = {'searchword3':'旭生汽车',
        'channelid':'1',
        'filetypeid':'doc,xls,pdf,jpg',
        'templet':'demo_result.jsp',
        'prepage':20,
        'getcontent':'on',
        'filetype':'on'}
r = requests.post(url, data=data,headers=headers)
soup=BeautifulSoup(r.text,'lxml')
jieguolists=soup.find_all('div',class_='jieguolist')
for a in jieguolists:
    if a.find('div',class_='h1').text.find('反馈意见')>0:
        print(a)
    else:
        print('没了')