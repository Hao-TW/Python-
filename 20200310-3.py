# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:33:18 2020

@author: ASUS
"""

print('開啟搜尋網頁')
param ={'wd':'yahoo購物'} #搜尋訊息"網址?wd="
r = requests.get('https://www.baidu.com/s',params=param)
webbrowser.open(r.url)