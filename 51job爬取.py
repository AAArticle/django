# __author : "ArticleYeung"
# date : 2019/8/20

import re
import requests
import matplotlib
from lxml import etree
import matplotlib.pyplot as plt


def getHTML(url):
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    r = requests.get(url, headers=hd, timeout=10)
    r.encoding = r.apparent_encoding
    return r.text


def getInfo():
    info_list = []
    keywords = ['python', 'python 数据', 'python 运维', 'python 爬虫', 'python 前端', 'python 后端']
    for keyword in keywords:
        url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,' + keyword + ',2,1.html?lang=c'
        html = getHTML(url)
        content = etree.HTML(html)
        nums = content.xpath('//div[@class="rt"]/text()')
        num = re.findall(r'共(.*?)条职位', nums[0])
        dict = {'职位':keyword, '数量':num}
        info_list.append(dict)
    return info_list


def draw_pic(info_list):
    matplotlib.rcParams['font.family'] = 'SimHei'
    for i in range(len(info_list)):
        plt.title('2019年python职位数据调查', fontsize=16)
        x = [i]
        y = float(info_list[i]['数量'][0])
        plt.bar(x, y, label=info_list[i]['职位'], width=0.45)
        plt.legend()
    plt.savefig('F:/pics/Matplotlib/Python岗位', dpi=600)


def main():
    try:
        contents = getInfo()
        draw_pic(contents)
    except:
        main()


if __name__ == '__main__':
    main()