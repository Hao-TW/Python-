# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:11:58 2020

@author: ASUS
"""



from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.find_all("span",{"class":"green"})
for name in nameList:
    print(name.get_text())