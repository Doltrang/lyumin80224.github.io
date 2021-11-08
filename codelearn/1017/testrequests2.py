import requests
url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&amp;api_key=9be7b239-557b-4c10-9775-78cadfc555e9&amp;sort=ImportDate%20desc&amp;format=json'
response = requests.get(url)
air = response.json()
for x in air["records"]:
    print(x["Site"],x["PM25"],sep='\t')
###############################################
import requests
url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&amp;api_key=9be7b239-557b-4c10-9775-78cadfc555e9&amp;sort=ImportDate%20desc&amp;format=json'
response = requests.get(url)
air = response.json()
county=input('請輸入縣市: ')
for x in air["records"]:
    if county in x['county']:
    # if x['county'].find(county) != -1:
        print(x['Site'],x['PM25'],x['county'],sep='\t')