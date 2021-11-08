import requests
from requests.models import Response
url='https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
html = response.text
btext = '<th>'
etext = '</th>'
bi = html.index(btext) + len(btext)
ei = html.index(etext)
print(html[bi:ei])