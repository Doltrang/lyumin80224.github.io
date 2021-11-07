# 爬steam appid及遊玩時間
import urllib.request as req
import bs4
import random
import time
import pandas as pd
 
data=pd.read_csv('appid.csv',header=0)
x=list(data.appid)
# print(x)
for i in x:
    url = 'https://steamspy.com/app/'+str(i)
    # print(url)
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "cookie":"over18=1",
        "Referer": "https://www.google.com/"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8") # 解析網頁原始碼
    # 爬蟲開始
    root = bs4.BeautifulSoup(data, "html.parser")
    root1=root.find('div',class_='p-r-30')
    root2=root.find('div',class_='page-container')
    id=root2.select('script')[0].text.split('var')[1].split('=')[1].strip("'").strip("';\r\n")
    try:
        playtime=root1.select('p')[0].text.split('Playtime total:')[1].split(' (average) ')[0].strip()
        playtime2=root1.select('p')[0].text.split('Playtime total:')[1].split(' (average) ')[1].split(' ')[0]
    except IndexError:
        playtime='0'
        playtime2='0'
    with open("data.csv", mode= "a+", encoding= "utf-8") as file:
        file.write(id+','+playtime+','+playtime2+'\n')
        file.close()
    delay_choices = [5, 6, 7, 10 ,15]  #延遲的秒數
    delay = random.choice(delay_choices)  #隨機選取秒數
    time.sleep(delay)  #延遲