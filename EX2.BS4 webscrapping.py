# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:43:40 2021

@author: jagadeesan
"""

from bs4 import BeautifulSoup
import requests
import re

# getting box office of the movie
url = 'https://en.wikipedia.org/wiki/Avengers:_Infinity_War'
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p.string)
soup.find('title').get_text()

for lk in soup.find_all('a'):#getting all the links of a page
    print(lk.get('href'))
    
print(soup.get_text()) 
