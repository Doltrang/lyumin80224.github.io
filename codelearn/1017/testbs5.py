from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
trs=soup.select('table')[0].select('tr')
for tr in trs[1:-1]:
    tds = tr.select('td')
    year = tds[0].text.strip()
    for i,td in enumerate(tds[1:]):
        winners = td.select('a')
        for w in winners:
            if not w.attrs['href'].startswith('#'):
                print(year,i,w.text.strip(),sep=',')