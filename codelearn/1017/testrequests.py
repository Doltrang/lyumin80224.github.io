import requests
# print(dir(requests))
url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&amp;api_key=9be7b239-557b-4c10-9775-78cadfc555e9&amp;sort=ImportDate%20desc&amp;format=json'
response = requests.get(url)
# print(dir(response))
air = response.json()
print(air)
print(air["records"][0]["Site"])
print(air["records"][0]["PM25"])
# print(response.status_code)

