# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:36:35 2020

@author: ASUS
"""

import  bs4,requests

url = 'https://www.taiwanlottery.com.tw/'
html = requests.get(url)

html.raise_for_status()

objSoup = bs4.BeautifulSoup(html.text,'html.parser')
#透過 select() 去選出.content_box02
dataTag = objSoup.select('.contents_box02')
print("串列長度",len(dataTag))
for i in range(len(dataTag)):
    print(dataTag[i])