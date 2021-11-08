from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
print(soup.select('table')[0].select('th')[0].text.strip()) # suop.select出來一定是list
print(soup.select('table')[0].select('th')[1].text.strip())
print(soup.select('table')[0].select('th')[2].text.strip())
print(soup.select('table')[0].select('th')[3].text.strip())
print(soup.select('table')[0].select('th')[4].text.strip())
print(soup.select('table')[0].select('th')[5].text.strip())
print(soup.select('table')[0].select('th')[6].select('a')[0].text)