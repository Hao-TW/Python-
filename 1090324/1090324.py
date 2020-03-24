# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:48:31 2020

@author: ASUS
"""

from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from time import time

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)
print(response.text[:300])

html_soup = BeautifulSoup(response.text, 'html.parser')    #html_soup 為解析
type(html_soup)
movie_containers = html_soup.find_all('div',class_ = 'lister-item mode-advanced')


#print(type(movie_containers))
#print(len(movie_containers))


names=[]
years=[]
imdb_ratings=[]
metascore=[]
votes=[]
for container in movie_containers:
    if container.find('div',class_='ratings-metascore') is not None:
        # The name
        name = container.h3.a.text
        names.append(name)
        # The year
        year = container.h3.find('span',class_ = 'lister-item-year').text
        years.append(year)
        # The IMDB ratings
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
        # The number of votes
        vote = container.find('span', attrs ={'name':'nv'})['data-value']
        votes.append(int(vote))
        
test_df = pd.DataFrame({'movie': names,
                       'year': years,
                       'imdb': imdb_ratings,
                       'votes': votes})
print(test_df.info())

test_df['year'].unique()
test_df.loc[:, 'year'] = test_df['year'].str[-5:-1].astype(int)
test_df.to_csv('movie.csv')