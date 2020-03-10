# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:24:06 2020

@author: ASUS
"""

'''

#選取完 Ctrl+/ 一次註解(#) 二次解除


#下載網頁使用requests.get()方法
url='http://www.grandtech.info'
htmlfile = requests.get(url)
print(type(htmlfile))
#可以知道回傳的資料型態是Response物件

'''

#延伸
'''
認識Responese物件
status_code如果直是requests.codes.ok表示獲得網頁內容成功
test : 網頁內容
'''
url = 'http://www.grandtech.info'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print('取得網頁內容成功')
else:
    print('取得網頁內容失敗')
print(htmlfile.text)    #列印網頁內容