#coding UTF-8
import os
import re
import time
import urllib

import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_news(bs):
    date_point = bs.find_all('div', string='日期 ')
    date = date_point[0].parent.next_sibling.next_sibling
    
    date = date.text.split('/')
    path = r'./中央社/' + date[0] + '_' +date[1] + '/'
    
    news_point = bs.find_all('div', string='原始本文')
    news = news_point[0].parent.next_sibling.next_sibling.find('div')
    
    global n, day
    
    if date[2] != day:
        n = 1
        
    day = date[2]
        
    f_n = '_{:0>3s}'.format(str(n))
    
    if not os.path.isdir(path):
        os.makedirs(path)
        
    f_name = path + date[0] + '_' +date[1] + '_' + day + str(f_n) + '.txt'
        
    if not os.path.isfile(f_name):
        with open(f_name, 'w', encoding="utf-8") as f:
            n+=1

            f.write(news.text)
                
            f.close()


#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#Browser = webdriver.Chrome(chrome_options=options)

Browser = webdriver.Chrome()
n = 1

url  = 'http://210.69.89.181/CNA/www/UserLogin.jsp'
Browser.get(url)

UserName= 'nccu'
UserPass= 'ai887'

Browser.find_element_by_name('userId').send_keys(UserName)
Browser.find_element_by_name('password').send_keys(UserPass)
Browser.find_element_by_xpath("//input[@*='submit']").click()

Browser.find_element_by_xpath("//a[text()='進階檢索']").click()

html = Browser.page_source
bs = BS(html, 'html.parser')


day = '01'
StartDate='202003' + day 
LastDate='20200302' #比較近的日期

for _ in range(8):
    Browser.find_element_by_name("startDate").send_keys(Keys.BACK_SPACE)
Browser.find_element_by_name("startDate").send_keys(StartDate)

for _ in range(8):
    Browser.find_element_by_name("endDate").send_keys(Keys.BACK_SPACE)
Browser.find_element_by_name("endDate").send_keys(LastDate)

Browser.find_element_by_xpath('//option[text()="新聞"]').click()

Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="中央社社稿"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="中央社商情"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="世界年鑑"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="新聞大舞台"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="名人錄"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="背景資料"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="工商時報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="中國時報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="中華日報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="台灣時報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="台灣新生報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="民生報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="民眾日報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="自由時報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="青年日報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="國語日報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="經濟日報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="聯合報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="聯合晚報"]').click()
Browser.find_element_by_xpath('//select[@name="newspaper"]/option[text()="蘋果日報"]').click()

Browser.find_element_by_xpath('//input[@value="檢索"]').click()

news = Browser.find_elements_by_xpath('//a[@href="#"]')

#time.sleep(3)

html = Browser.page_source
bs = BS(html, 'html.parser')

page_point = bs.find_all('a', string = '下一頁')
page = page_point[0].parent

nums = re.findall(r'\d+', page.text)

all_page = int(nums[1])

try:
    for i in range(all_page):
        news = Browser.find_elements_by_xpath('//a[@href="#"]')
        
        for j in range(1, 11):
            news[j].click()
            windows=Browser.window_handles  #獲得當前瀏覽器所有視窗
            Browser.switch_to.window(windows[-1])
            
            html = Browser.page_source
            
            bs = BS(html, 'html.parser')
            
            get_news(bs)
            
            Browser.close()
    
            Browser.switch_to.window(windows[0])
        
        if i<all_page-1:
            Browser.find_element_by_xpath('//a[text()="下一頁"]').click()

except Exception as e:
    print(e)

Browser.quit()
