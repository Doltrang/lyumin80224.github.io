from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
tr=soup.select('table')[0].select('tr')[0]
for th in tr.select('th'):
    a = th.select('a')
    if len(a) == 0:
        print(th.text.strip())
    else:
        print(a[0].text.strip())