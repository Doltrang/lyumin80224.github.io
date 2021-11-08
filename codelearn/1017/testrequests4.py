import requests
from requests.models import Response
url='https://pchome.megatime.com.tw/m/stock/sid1234.html'
response = requests.post(url,data={'is_check':'1'})
html = response.text
btext = '<i id="col1"><span class="red">'
ctext = '<i id="col6"><span class="red">'
etext = '</span></i>'
bi=html.index(btext) + len(btext)
ci=html.index(ctext)
ei=html.index(etext)
print(html[bi:ei],'上漲',html[ci:ei])