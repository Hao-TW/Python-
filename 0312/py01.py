# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:40:57 2020

@author: ASUS
"""

from bs4 import BeautifulSoup

from urllib.request import urlopen

#html = urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')

#soup = BeautifulSoup(html,'html.parser')
'''
print(type(soup))
#print(soup.h1)
#print(soup.p)

print(soup.h1.text)
print(soup.p.text)

#透過find_all抓取連結
all_href = soup.find_all('a')

findAll   是2.x版本
find_all  是3.x版本
兩者在3.x 均可使用



print(all_href)
for i in all_href:
    print(i['href'])
'''  
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.find_all("span",{"calss':'red"})
for name in nameList:
    print(name.get_text())
    