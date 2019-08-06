# __author : "ArticleYeung"
# date : 2019/8/6

import re
import json
import requests
from bs4 import BeautifulSoup

def getHTML(url):
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    r = requests.get(url, headers=hd, timeout=10)
    r.encoding = r.apparent_encoding
    return r.text

def getSongName(html):
    demo = BeautifulSoup(html, 'html.parser')
    list = demo.find('ul', attrs={'class':'f-hide'})
    song_name = []
    # print(list('li'))                    尝试提取<ul>标签内<li>标签
    # print(list('a'))                     尝试提取<ul>标签内<a>标签
    # print(list('a')[0].attrs             尝试提取<a>标签中的属性
    # print(list('a')[0].attrs['href'])    提取返回的字典形式中的href属性
    for i in range(len(list)):
        song_name.append(list('li')[i].text)
        song_url = 'https://music.163.com/'+list('a')[i].attrs['href']
        song_id = re.findall(r'id=(.*)', song_url)
        # print(song_id) # 获取歌曲的 id
        # print(i+1, '-', song_name, '----------', song_url) # li标签的text 歌曲名
        # print(song_list_id)
    return song_name

def getINFO(html):
    demo = BeautifulSoup(html, 'html.parser')
    list = demo.find('ul', attrs={'class':'f-hide'})
    song_name = ' '
    song_list_id = []
    # print(list('li'))                    尝试提取<ul>标签内<li>标签
    # print(list('a'))                     尝试提取<ul>标签内<a>标签
    # print(list('a')[0].attrs             尝试提取<a>标签中的属性
    # print(list('a')[0].attrs['href'])    提取返回的字典形式中的href属性
    for i in range(len(list)):
        song_name = list('li')[i].text
        song_url = 'https://music.163.com/'+list('a')[i].attrs['href']
        song_id = re.findall(r'id=(.*)', song_url)
        song_list_id.append(song_id[0]) # 把每首歌的id添加到列表中
        # print(song_id) # 获取歌曲的 id
        # print(i+1, '-', song_name, '----------', song_url) # li标签的text 歌曲名
        # print(song_list_id)
    return song_list_id

def getContent(id,name):
    try:
        # 获取网易云音乐歌词的api接口地址http://music.163.com/api/song/lyric?id=song_id&lv=1&kv=1&tv=-1
        '''
        检查每个元素的属性以及元素对应的内容
        print(info[0])   
        print(type(info))
        print(type(info[0]))
        '''
        contents = ' '
        for i in range(len(id)):
            url = 'http://music.163.com/api/song/lyric?id=' + id[i] + '&lv=1&kv=1&tv=-1'
            path = 'F://pics//网易云音乐歌词//' + name[i] + '.txt'
            html = getHTML(url)
            dic = json.loads(html)
            # print(type(dic))  # 查看 dic 的属性
            # print(dic['lrc']['lyric']) # 获取歌词
            contents = name[i] + '\n' + dic['lrc']['lyric']
            # print(contents)
            try:
                with open(path, "a") as f:
                    f.write(contents)
                    f.close()
                    print(name[i] + '歌词保存成功!')
            except:
                print(name[i] + '歌词保存失败!')
    except:
        print('歌词获取失败！！')


def main():
    # url 为歌手热门歌曲主页所在地址
    url = 'https://music.163.com/artist?id=7763'
    html = getHTML(url)
    id = getINFO(html)
    name = getSongName(html)
    content = getContent(id,name)

if __name__ == '__main__':
    main()
