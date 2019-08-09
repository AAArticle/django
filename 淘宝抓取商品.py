# __author : "ArticleYeung"
# date : 2019/7/20

import requests
import xlwt
import re

def getHTMLText(url):
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    cookies = {
        'cookie' : 'thw=cn; cna=pXC5FetwgH0CAXch6c/roNIS; t=8bbc7a0cb368ac33398437899128df75; cookie2=1be8d41aeae8a6f59ef4d2f91d9fbe7b; _tb_token_=b5b55677e739; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; enc=CeH7RLay98NfQnSmyEVtc3e7gUMHsZ7vYxu3GuEGKUeMp9wOhSoBbmPL7fACBO2IHtoS8u2D4v53wc520oKC5Q%3D%3D; alitrackid=www.taobao.com; swfstore=254499; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _cc_=VFC%2FuZ9ajQ%3D%3D; JSESSIONID=D4D515FAD4A91D5F4256A0B7BE403BA0; lastalitrackid=login.taobao.com; whl=-1%260%260%261563599899542; v=0; unb=791623994; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=U%2BGCWk%2F7pY%2FF&cookie15=URm48syIIVrSKA%3D%3D&existShop=false&pas=0&cookie14=UoTaG7r6AP9icw%3D%3D&tag=8&lng=zh_CN; sg=04f; _l_g_=Ug%3D%3D; skt=5b97202b462f0ab7; cookie1=BvXkUpL1kafr8I4NZvUMeIYqcmhZPjcw6OIFnwiUaq0%3D; csg=a29b7b03; uc3=vt3=F8dBy3zcqY8cS%2BZXlw4%3D&id2=VAiW4T2jpvnC&nk2=F5RBxEAtA4HERdg%3D&lg2=URm48syIIVrSKA%3D%3D; existShop=MTU2MzU5OTkyMw%3D%3D; tracknick=tb412027_00; lgc=tb412027_00; dnk=tb412027_00; _nk_=tb412027_00; cookie17=VAiW4T2jpvnC; mt=ci=0_0&np=; isg=BGtrPkBGsoBN8e5UT754KP3H-o-VKH5l6WcELd3oR6oBfIveZVAPUgne1vy3x9f6; l=cBx0XRerq_BCSHu2BOCanurza77OSIRYYuPzaNbMi_5BK6T6fu_OkqWPWF96VjWdO28B4k6UXwp9-etkZ9MWI2IpXUJ1.'}
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