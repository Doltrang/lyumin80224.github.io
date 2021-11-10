# 爬steam appid及擁有區間
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
    print(id,end=',')
    try:
        owners=root1.select('p')[0].text.split('Owners: ')[1].split('Followers')[0].replace(',','').replace('..','-')
        print(owners)
    except IndexError:
        owners='None'
    with open("data.csv", mode= "a+", encoding= "utf-8") as file:
        file.write(id+','+owners+'\n')
        file.close()
# delay_choices = [5, 6, 7, 10 ,15]  #延遲的秒數
# delay = random.choice(delay_choices)  #隨機選取秒數
# time.sleep(delay)  #延遲