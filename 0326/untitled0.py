# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:07:22 2020

@author: ASUS
"""

import requests
import re
from bs4 import BeautifulSoup
Y_MOVIE_URL = 'https://movies.yahoo.com.tw/movie_thisweek.html'
def get_web_page(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Invaid url',resp.url)
        return None
    else:
        return resp.text


def get_data(data_str):
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern,data_str)
    if match != None:
        return data_str
    else:
        return match.group(0)
    
def get_movie_id(url):
    try:
        movie_id = url.split('.html')[0].split('-')[-1]
    except:
        movie_id = url
    return movie_id
    
if __name__ == '__main__':
    page = get_web_page(Y_MOVIE_URL)
    print(get_movie_id('https://movies.yahoo.com.tw/movieinfo_main/%E8%A8%98%E6%86%B6%E5%B1%8B-kiokuya-10470'))
    
    
    
    
    
def get_movies(dom):
    soup = BeautifulSoup(dom,'html.parser')
    movies=[]
    rows = soup.find_all('div','release_info_text')
    for row in rows:
        movie = dict()
        movie['expection']=row.find('div','leveltext').span.text.strip()
        movie['ch_name']=row.find('div','release_movie_name').a.text.strip()
        movie['eng_name']=row.find('div','release_movie_name').find('div','en').a.text.strip()
        movie['movie_id']=get_movie_id(row.find('div','release_movie_name').a['href'])
        movie['poster_url']=row.parent.find_previous_sibling('div','release_foto').a.img['src']
        movie['release_data'] = get_data(row.find('div','release_movie_time').text)
        movies.append(movie)
    return movies

if __name__ == '__main__':
    page = get_web_page(Y_MOVIE_URL)
    movies = get_movies(page)
    for movie in movies:
        print(movie)