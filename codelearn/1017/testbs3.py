from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
trs=soup.select('table')[0].select('tr')
for tr in trs[1:-1]:
    print(tr.select('td')[0].text.strip())