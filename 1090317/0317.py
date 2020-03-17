# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:40:36 2020

@author: ASUS
"""

import bs4, requests

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)                                         
objSoup = bs4.BeautifulSoup(html.text, 'html.parser')      

dataTag = objSoup.select('.contents_box04')  
balls = dataTag[0].find_all('div', {'class':'ball_tx ball_purple'})
print("星彩中獎號碼 : ", end='')
for i in range(3):                                  
    print(balls[i].text, end='   ')
    