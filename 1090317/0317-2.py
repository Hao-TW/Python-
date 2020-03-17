# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:39:03 2020

@author: ASUS
"""

from bs4 import BeautifulSoup

from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon').read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')

text_links = soup.find_all('a')
for link in text_links:
    print(link.get_text())
