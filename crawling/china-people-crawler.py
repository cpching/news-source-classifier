from opencc import OpenCC
import os
import requests
from bs4 import BeautifulSoup as BS
import urllib
from datetime import date, timedelta
import time

def article(url, p, n):
    html = requests.get(url)
    bs = BS(html.text, 'html.parser')
    
    p = '_{:0>2s}'.format(str(p))
    n = '_{:0>2s}'.format(str(n))
    
    f_name = path + start_day.strftime("%Y_%m_%d") + str(p) + str(n) + '.txt'

    if not os.path.isfile(f_name):
        f = open(f_name, 'w')
    
        cc = OpenCC('s2tw')
    
        for new in bs.find('div', {'id': 'articleContent'}).find_all('p'):
            f.writelines(cc.convert(new.text))
#            print(new.text)
        
        f.close()

def same_day(url, p):
    html = requests.get(url)
    bs = BS(html.text, 'html.parser')

    i=0

    
    for link in bs.find_all(class_='fontstyle'):
        # a piece of news
        # `l` example: nw.D110000renmrb_20191207_1-01.htm    
        for l in link.find_all('a'):
            if 'href' in l.attrs:
                h = l.attrs['href']
                if 'nw' in h:
                    i+=1
                    article(head+day+h, p, i)

tStart = time.time()#計時開始
#start_day = date.start_day()
start_day = date(2019, 12, 10) #比較近的日期
day = start_day.strftime("%Y-%m/%d/")

last_day = date(2019, 12, 8)

while (start_day - last_day).days >= 0:
    try:
        # daily news link example: http://paper.people.com.cn/rmrb/html/2019-12/27/nbs.D110000renmrb_01.htm
        day = start_day.strftime("%Y-%m/%d/")
        head = 'http://paper.people.com.cn/rmrb/html/'
        enter_page = 'nbs.D110000renmrb_01.htm'

        path = r'./人民日報/' + start_day.strftime("%Y_%m") + '/'

        if not os.path.isdir(path):
            os.makedirs(path)

        url = head+day+enter_page

        html = requests.get(url)
        bs = BS(html.text, 'lxml')

        i = 0

        # different news blocks
        # `link` example: nbs.D110000renmrb_01.htm
        for link in bs.find_all('a', {'id': 'pageLink'}):
            l = head+day+link.attrs['href']
            print(l)
            i+=1
            same_day(l, i)

        start_day = yesterday(start_day)

    except:
        pass

                    

