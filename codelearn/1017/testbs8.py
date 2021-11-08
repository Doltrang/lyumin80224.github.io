from bs4 import BeautifulSoup
import requests
BASE_URL = 'https://en.wikipedia.org'
HEADERS = {'User-Agent':'Mozilla/5.0'}

def get_Nobel_soup():
    response = requests.get(BASE_URL + '/wiki/List_of_Nobel_laureates')
    return BeautifulSoup(response.content,'lxml')

def get_column_titles(table):
    cols = []
    #撈取獲獎類別
    for th in table.select('tr')[0].select('th')[1:]:
        a = th.select('a')
        if len(a) > 0:
            category = a[0].text.replace('or ',' or ').strip()
            link = a[0].attrs['href']
            cols.append({'name':category,'href':link})
    return cols

def get_Nobel_winners(table):
    cols = get_column_titles(table)
    winners = []
    for tr in table.select('tr')[1:-1]:
        tds = tr.select('td')
        year = tds[0].text.strip()
        for i,td in enumerate(tds[1:]):
            for a in td.select('a'):
                if not a.attrs['href'].startswith('#'):
                    winners.append({
                        'year':year,
                        'category':cols[i]['name'],
                        'name':a.text.strip(),
                        'link':a.attrs['href']
                    })
    return winners
soup = get_Nobel_soup()
print(get_column_titles(soup.select('table')[0]))
print(get_Nobel_winners(soup.select('table')[0]))