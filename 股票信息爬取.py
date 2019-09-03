# __author : "ArticleYeung"
# date : 2019/7/20

import requests
import re
import bs4
import xlwt
import traceback
from bs4 import BeautifulSoup

def getHTMLText(url):
    hd = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    try:
        r = requests.get(url,headers = hd,timeout = 20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取网页列表失败")

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][zh]\d{6}',href)[0])
        except:
            continue

def getStockInfo(lst,stockURL):
    root = "F://pics//股票信息.txt"
    for stock in lst:
        url = stockURL + stock +'.html'
        html = getHTMLText(url)
        try:
            if html == " ":
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value

            with open(root, 'a', encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
            print("写入成功")
        except:
            traceback.print_exc()
            continue

def writeExcel(slist):
    try:
        root = "F://pics//股票信息.xls"
        wd = xlwt.Workbook()
        ws = wd.add_sheet("goods")
        ws.write(0,0,"序号")
        ws.write(0,1,"股票名称")
        ws.write(0,2,"今开")
        ws.write(0,3,"成交量")
        for i in range(len(slist)):
              ws.write(i + 1, 0, i + 1)
              ws.write(i + 1, 1, slist[i][0])
              ws.write(i + 1, 2, slist[i][1])
              ws.write(i + 1, 3, slist[i][2])
        wd.save(root)
        print("写入成功")
    except:
        print("写入失败")

def writeTXT(slist):
    try:
        root = "F://pics//股票信息.txt"
        with open(root ,'a') as f:
            f.write(slist)
            f.close()
            print("写入成功")
    except:
        print("写入失败")

def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url)
    # writeExcel(slist)

if __name__ == '__main__':
    main()


