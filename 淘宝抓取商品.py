# __author : "ArticleYeung"
# date : 2019/7/20

import requests
import xlwt
import re

def getHTMLText(url):
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    cookies = {
        'cookie' : '登录后的cookie信息'}
    try:
        r = requests.get (url,headers=hd,cookies=cookies,timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取网址内容失败"

def parsePage(ilt,html):
    try:
        pat = re.compile(r'"raw_title":".*?"')
        tlt = pat.findall(html)
        pat1 = re.compile(r'"view_price":".*?"')
        plt = pat1.findall(html)
        pat2 = re.compile(r'"detail_url":".*?"')
        ult = pat2.findall(html)
        for i in range(len(tlt)):
            # eval函数将最外层的双引号或单引号去掉
            title = eval(tlt[i].split(':')[1])
            price = eval(plt[i].split(':')[1])
            urls  = eval(ult[i].split(":")[1])
            ilt.append([title,price,urls])
    except:
        print("打印失败")

def printGoodList(ilt):
    tplt = "{0:4}\t{1:{4}^32}\t{2:8}\t{3:32}"
    print(tplt.format("序号","商品名称","价格","链接",chr(12288)))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1],g[2],chr(12288)))

def write_data(ilt,num):
    try:
        root = "F://pics//淘宝商品信息.xls"
        wd = xlwt.Workbook()
        ws = wd.add_sheet("goods")
        ws.write(0,0,"序号")
        ws.write(0,1,"商品名称")
        ws.write(0,2,"价格")
        ws.write(0,3, "链接")
        for i in range(len(ilt)):
              ws.write(i + 1, 0, i + 1)
              ws.write(i + 1, 1, ilt[i][0])
              ws.write(i + 1, 2, ilt[i][1])
              ws.write(i + 1, 3, ilt[i][2])
        wd.save(root)
        print("写入成功")
    except:
        print("写入失败")

def main():
    goods = '书包'
    depth = 100
    # url = "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E4%B9%A6%E5%8C%85&suggest=0_1&_input_charset=utf-8&wq=shubao&suggest_query=shubao&source=suggest"
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(i*44)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)
    write_data(infoList,20)

if __name__ == "__main__":
    main()
