# __author : "ArticleYeung"
# date : 2019/8/11

import requests
from lxml import etree

hd = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
r = requests.get('https://book.douban.com/latest?icn=index-latestbook-all', headers=hd, timeout=10)
r.raise_for_status()
r.encoding = r.apparent_encoding
content = r.text
html = etree.HTML(content)
title1 = html.xpath('//div[@class="article"]/h2/text()')
title2 = html.xpath('//div[@class="aside"]/h2/text()')
lis = html.xpath('//div[@class="article"]/ul')
dict = {}
for li in lis:
    name = html.xpath('//div[@class="article"]/ul/li/div[@class="detail-frame"]/h2/a/text()')
    href = html.xpath('//div[@class="article"]/ul/li/div[@class="detail-frame"]/h2/a/@href')
    author = html.xpath('//div[@class="article"]/ul/li/div[@class="detail-frame"]/p[@class="color-gray"]/text()')
    info = html.xpath('//div[@class="article"]/ul/li/div[@class="detail-frame"]/p[@class="detail"]/text()')
    for i in range(len(name)):
        dict = {'书名: ': name[i], '链接：': href[i], '作者：': author[i], '简介：': info[i]}
        print(dict)

list = html.xpath('//div[@class="aside"]/ul')
for li in list:
    name = html.xpath('//div[@class="aside"]/ul/li/div[@class="detail-frame"]/h2/a/text()')
    href = html.xpath('//div[@class="aside"]/ul/li/div[@class="detail-frame"]/h2/a/@href')
    author = html.xpath('//div[@class="aside"]/ul/li/div[@class="detail-frame"]/p[@class="color-gray"]/text()')
    info = html.xpath('//div[@class="aside"]/ul/li/div[@class="detail-frame"]/p[3]/text()')
    for i in range(len(name)):
        dict = {'书名: ': name[i], '链接：': href[i], '作者：': author[i], '简介：': info[i]}
        print(dict)