# ptt 網路爬蟲 抓取留言練習 改為while迴圈
import urllib.request as req
url=input("請輸入需抓取留言的ptt完整網址:")
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "cookie":"over18=1"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 解析網頁原始碼
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
id=root.find_all("span",class_="push-userid") # 抓取留言者ID
msg=root.find_all("span",class_="push-content") # 抓取內容
try:
    with open("data.txt",mode="w",encoding="utf-8") as file:
        x=0
        while x >=0: # 抓整篇留言，若只抓100則 可改為 x<=99
            if msg[x].string != None: # 排除留言內容是網址的情況
                file.write(id[x].string+msg[x].string+"\n")
            else:
                file.write(id[x].string+": "+msg[x].a.string+"\n") # 留言內容為網址、圖片等 包在a標籤內
            x+=1
    file.close
except IndexError: # 排除id[x]及msg[x]是空值的狀況
    pass