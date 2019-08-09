import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def search():
    # EC 模块用来寻找网页中的元素
    # By.XPATH，以XPATH的形式来进行定位
    input = waite.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kw"]')))
    # 向文本框输入内容
    input.send_keys('bilibili')
    submit = waite.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="su"]')))
    submit.click()

    drop_down()

# 模拟进度条滚动
def drop_down():
    for x in range(1,11,2):
        time.sleep(0.5)
        j = x/10  # j为滑动到的位置
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)

def get_contents():
    infolist = []
    num = 1
    page = 1
    while num < 31:     # num为想要获取的标签总数
        try:
            # 每个标签的名称 //*[@id="1"]/h3/a[1]
            name = driver.find_element_by_xpath('//*[@id="content_left"]/div[@id="{}"]/h3/a '.format(num)).text
            # 每个标签的链接 //*[@id="1"]/h3/a[1] 下的href属性
            href = driver.find_element_by_xpath('//*[@id="content_left"]/div[@id="{}"]/h3/a'.format(num)).get_attribute('href')
            infoDict = {'序号': num, '词条链接': href, '词条名称': name, }
            infolist.append(infoDict)


            if num % 10 == 0 or num == 19:
                driver.get('https://www.baidu.com/s?wd=bilibili&pn={}'.format(page * 10))
                drop_down()
                time.sleep(2)
                page += 1

            num += 1
            # 词条id = 20，31缺失
            if num == 20 or num == 31:
                num += 1
        except:
            print('第', page, '页', num, '未录入')
            break
    return infolist

if __name__ == '__main__':
    driver = webdriver.Chrome()
    waite = WebDriverWait(driver, 10)
    driver.get('http://www.baidu.com')
    search()
    contents = get_contents()
    for i in range(len(contents)):
        print(contents[i]['序号'],contents[i]['词条名称'],contents[i]['词条链接'])




