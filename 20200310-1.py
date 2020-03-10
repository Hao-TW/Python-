# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:54:51 2020

@author: ASUS
"""

import requests

#使用GET下載

r=requests.get('http://www.grandtech.info')
print("OK")
#http://www.grandtech.info

#伺服器回應狀態
'''
print(r.status_code)

#檢查伺服器狀態狀態是否OK

if r.status_code == requests.codes.ok:
    print("OK")
'''
    