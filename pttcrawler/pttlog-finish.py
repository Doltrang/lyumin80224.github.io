# ptt 網路爬蟲 抓取留言 加入標籤時間 加入內容及資訊 完成版
import urllib.request as req
import bs4
url=input("請輸入需抓取留言的ptt完整網址:")
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "cookie":"over18=1"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 解析網頁原始碼
root=bs4.BeautifulSoup(data, "html.parser")
header=root.find_all("span","article-meta-value") # 抓文章標籤
all_content=root.find("div",class_="bbs-screen bbs-content") # 抓內文
tag=root.find_all("span",class_="push-tag") # 推文標籤
id=root.find_all("span",class_="push-userid") # 抓取留言者ID
msg=root.find_all("span",class_="push-content") # 抓取內容
time=root.find_all("span",class_="push-ipdatetime") # 抓取時間
# 標籤內容處理
author=header[0].text # 作者
kanban=header[1].text # 看板
title=header[2].text # 標題
date=header[3].text # 時間
# 文章內容
all_text=all_content.text
no1_text=all_text.split("--")[0] # 用"--"做分割 取第1段資料  *若發文者有使用----符號做分段會無法取得完整內容
no2_text=no1_text.split("\n") # 使用換行"\n"做分割
no3_text=no2_text[1:] # 觀察上一段輸出後 第1筆資料為標題 取第2筆資料到最後
content="\n".join(no3_text) # 將換行加回去輸出就是正常內文
with open("data.txt",mode="w",encoding="utf-8") as file:
    # file.write("作者: "+header[0].text+"\n"+"看板: "+header[1].text+"\n"+"標題: "+header[2].text+"\n"+"時間: "+header[3].text+"\n"+"\n"+content+"推文內容"+"\n")
    file.write("作者: "+author+"\n"+"看板: "+kanban+"\n"+"標題: "+title+"\n"+"時間: "+date+"\n"+"\n"+content+"推文內容"+"\n")
    file.close()
try:
    with open("data.txt",mode="a+",encoding="utf-8") as file:
        x=0
        while x >=0: # 抓整篇留言，若只抓100則 可改為 x<=99
            file.write(tag[x].text+id[x].text+msg[x].text+time[x].text)
            # if msg[x].string != None: # 排除留言內容是網址的情況
            #     file.write(tag[x].string+id[x].string+msg[x].string+time[x].string) # 測試後如果內容含網址只會顯示內容
            # else:
            #     file.write(tag[x].string+id[x].string+": "+msg[x].a.string+time[x].string) # 留言內容為網址、圖片等 包在a標籤內
            x+=1
        file.close()
except IndexError: # 排除tag[x]、id[x]、msg[x]、time[x]是空值的狀況
    pass