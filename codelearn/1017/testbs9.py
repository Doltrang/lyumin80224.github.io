from bs4 import BeautifulSoup
import requests
url = 'https://stock.pchome.com.tw/m/stock/sid1234.html'
headers = {'User-Agent':'Mozilla/5.0','is_check':'1'}
response = requests.post(url,headers)
soup = BeautifulSoup(response.content,'lxml')
uls = soup.find("ul", class_= "infolist flexbox infosid")
li=uls.select('b')
ul=uls.select('span')
print(li[0].text,ul[0].text,sep=" : ")
print(li[1].text,uls.select('ul')[1].select('li')[1].text,sep=" : ")
print(li[5].text,ul[4].text,sep=" : ")


def get_Stock_price(stock_id):
    url = 'https://pchome.megatime.com.tw/m/stock/sid'+stock_id+'.html'
    response = requests.post(url,data={'is_check':'1'})
    soup = BeautifulSoup(response.content,'lxml')
    title = soup.select('title')[0].text
    ti = title.index(' 個股資訊')
    print(title[:ti])
    print('成交價 ：',soup.select('ul')[5].select('ul')[0].select('li')[1].text)
    print('成交張 ：',soup.select('ul')[5].select('ul')[1].select('li')[1].text)
    print('漲跌 ：',soup.select('ul')[5].select('ul')[5].select('li')[1].text)

# get_Stock_price('1234')
# get_Stock_price('1235')
# get_Stock_price('1236')
# get_Stock_price('2330')