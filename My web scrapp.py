# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:33:54 2020

@author: jagadeesan
"""

from bs4 import BeautifulSoup as bs #like parser#
import requests
import pyperclip as pc
import re
j=requests.get("https://www.imdb.com/chart/top")
print(j.text)
s = bs(j.text, 'lxml')
print(s)
print(re.match(r'jandu','jandu real warrior is jandu'))