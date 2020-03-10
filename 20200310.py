# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:49:28 2020

@author: ASUS
"""

import requests

import webbrowser

address = input('請輸入地址:')

webbrowser.open('https://www.google.com.tw/maps/search/' + address)
