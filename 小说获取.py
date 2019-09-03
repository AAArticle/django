# __author : "ArticleYeung"
# date : 2019/7/17
import re
import os
import requests
from bs4 import BeautifulSoup

url = "https://www.qu.la/book/168/"
hd = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}

# 抓取小说章节所在url地址
r = requests.get(url,headers=hd)
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
urls = re.findall(r'href="(.*?.html)"',demo)
#print(urls)

# 抓取小说章节的内容
# ulist 为需要爬取的网页的url地址
ulist = []
for i in range(len(urls)):
    url1 = 'https://www.qu.la/book/168/' + urls[i]
    ulist.append(url1)
#print(ulist)

# 小说写入txt中
root = "F://pics//择天记//"
# r2 = requests.get('https://www.qu.la/book/75722/4080755.html',headers=hd)
# demo2 = r2.text
# soup2 = BeautifulSoup(demo2,'html.parser')
# title = soup2.find('h1').text
# conts = soup2.find('div', attrs={'id': 'content'}).text
# title = re.sub(r'\?','',title)
# print(title)
for i in range(len(ulist)):
    r1 = requests.get(ulist[i],headers=hd)
    demo1 = r1.text
    soup1 = BeautifulSoup(demo1,'html.parser')
    title = soup1.find('h1').text
    #print(title)
    title = re.sub(r'\?', '', title)
    title = re.sub(r'\.', '', title)
    title = re.sub(r',', '', title)
    conts = soup1.find('div',attrs={'id':'content'}).text
    #print(conts)
    count = round(i/len(ulist)*100, 1)
    print('\r', '----------------'+str(count)+'%----------------', end='', flush=True)

    path = root + title + '.txt'
    if not os.path.exists(path):
        with open(path,"wb") as f:
            f.write(bytes(title,encoding='utf-8'))
            f.write(bytes(conts,encoding='utf-8'))
            f.close()
    else:
        continue


