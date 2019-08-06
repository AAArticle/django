# __author : "ArticleYeung"
# date : 2019/7/21

import bs4
import re
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
    try:
        r = requests.get(url,headers = hd,timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('抓取网页失败')

def getUrl(infoList,html):
    try:
        soup = BeautifulSoup(html,'html.parser')
        div = soup.find_all('a',attrs={'target':'new'})
        for i in range(len(div)):
            href = div[i].attrs.get('href')
            urls = 'http://www.dili360.com' + href  # urls为需要抓取图片的网址
            infoList.append(urls)
        #print(infoList)
    except:
        print('获取网页内容失败')

def write_data(infoList):
    for i in range(len(infoList)):
        pic_url = infoList[i]
        #print(pic_url)
        h = getHTMLText(pic_url)
        soup1 = BeautifulSoup(h,'html.parser')
        ul = soup1.find('ul',attrs={'id':'slider-one'})
        src = ul('img')
        for j in range(len(src)):
            # range : len(src)
            pic_urls = src[j].attrs.get('src')
            pic_urls = re.findall(r'(.*)@!rw3',pic_urls)
            #print(src[1].attrs.get('src'))

            # 把图片写入文件中
            path = "F://pics//国家地理保存图片//" + str(i)+str(j) +'.jpg'
            print(pic_urls[0])
            pics = requests.get(pic_urls[0])
            with open(path, 'wb') as f:
                f.write(pics.content)
                f.close()
                print("图片保存成功")


def main():
    infoList = []
    try:
        url = 'http://www.dili360.com/Gallery/cate/5/1.htm'
        html = getHTMLText(url)
        getUrl(infoList,html)
        write_data(infoList)
    except:
        print("爬取失败")

if __name__ == "__main__":
    main()