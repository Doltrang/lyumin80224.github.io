from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
trs=soup.select('table')[0].select('tr')
tds = trs[38].select('td')
for td in tds[1:]:
    winners = td.select('a')
    for w in winners:
        if not w.attrs['href'].startswith('#'):
            print(w.text.strip())