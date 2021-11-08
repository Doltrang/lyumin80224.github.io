from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')

trs=soup.select('table')[0].select('tr')
#撈取獲獎類別
cols=[]
for th in trs[0].select('th')[1:]:
    a = th.select('a')
    if len(a) > 0:
        cols.append(a[0].text.replace('or',' or').strip())
print(cols)
#組合年分、獲獎類別、得主姓名
for tr in trs[1:-1]:
    tds = tr.select('td')
    year = tds[0].text.strip()
    for i,td in enumerate(tds[1:]):
        winners = td.select('a')
        for w in winners:
            if not w.attrs['href'].startswith('#'):
                print(year,cols[i],w.text.strip(),sep=',')