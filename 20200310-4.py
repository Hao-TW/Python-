# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:58:40 2020

@author: ASUS
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bsObj=BeautifulSoup(html)
print(type(bsObj))
print(bsObj.h1)
