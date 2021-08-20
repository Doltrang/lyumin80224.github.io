# 抓取PTT 八卦版的網頁原始碼(HTML)
import urllib.request as req
def getdata(url):
    # 建立一個 Request 物件，附加Request Header的資訊
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "cookie":"over18=1"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)
    #解析原始碼, 取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") # 讓BeautifulSoup 協助我們解析 HTML 格式文件
    titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的div 標籤
    for title in titles:
            if title.a != None: # 如果標題包含 a標籤(貼文未被刪除),印出來
                print(title.a.string)
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]

# 主程序: 抓取多個頁面的標題
link="https://www.ptt.cc/bbs/Gossiping/index.html"
page=0
while page<4: # 抓取幾頁
    link="https://www.ptt.cc"+getdata(link)
    page+=1