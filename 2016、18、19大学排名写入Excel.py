# __author : "ArticleYeung"
# date : 2019/7/18

# __author : "ArticleYeung"
# date : 2019/7/18

import requests
import bs4
import xlwt
from bs4 import BeautifulSoup

def getHTMLText(url):
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    try:
        r = requests.get (url,headers=hd,timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "抓取失败"

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    #在tbody标签下找到每一所大学所对应的tr标签
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            #在tr标签中找到td标签的信息，并加入需要的td标签的信息
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    # {1:{3}^10} 打印第二个字符串时，使用第五个变量来进行填充（索引从0开始）
    print(tplt.format("排名","学校名称","所在省份","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def write_data(ulist,num):
    try:
        root = "F://pics//大学排名2019.xls"
        wd = xlwt.Workbook()
        ws = wd.add_sheet("univs")
        ws.write(0,0,"排名")
        ws.write(0,1,"大学名称")
        ws.write(0,2,"所在省份")
        ws.write(0,3, "总分")
        for i in range(len(ulist)):
              ws.write(i + 1, 0, ulist[i][0])
              ws.write(i + 1, 1, ulist[i][1])
              ws.write(i + 1, 2, ulist[i][2])
              ws.write(i + 1, 3, ulist[i][3])
        wd.save(root)
        print("写入成功")
    except:
        print("写入失败")

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
    write_data(uinfo,20)

if __name__ == "__main__":
    main()