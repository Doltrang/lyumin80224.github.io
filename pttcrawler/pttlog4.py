# ptt 網路爬蟲 抓取留言練習 加入標籤時間 修改輸出為text格式可排除問題
import urllib.request as req
url=input("請輸入需抓取留言的ptt完整網址:")
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "cookie":"over18=1"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 解析網頁原始碼
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
tag=root.find_all("span",class_="push-tag") # 推文標籤
id=root.find_all("span",class_="push-userid") # 抓取留言者ID
msg=root.find_all("span",class_="push-content") # 抓取內容
time=root.find_all("span",class_="push-ipdatetime") # 抓取時間
try:
    with open("data.txt",mode="a+",encoding="utf-8") as file:
        x=0
        while x >=0: # 抓整篇留言，若只抓100則 可改為 x<=99
            file.write(tag[x].text+id[x].text+msg[x].text+time[x].text)
            # if msg[x].string != None: # 排除留言內容是網址的情況
            #     file.write(tag[x].string+id[x].string+msg[x].string+time[x].string) # 發現如果推文是內容加圖片只會顯示內容
            # else:
            #     file.write(tag[x].string+id[x].string+": "+msg[x].a.string+time[x].string) # 留言內容為網址、圖片等 包在a標籤內
            x+=1
        file.close
except IndexError: # 排除tag[x]、id[x]、msg[x]、time[x]是空值的狀況
    pass