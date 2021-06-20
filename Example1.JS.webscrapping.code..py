# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:59:48 2020
@author: jagadeesan
"""

#finding the path of a particular data
from selenium import webdriver
browser = webdriver.PhantomJS(executable_path = r"C:\Users\jagadeesan\AppData\Local\Programs\Python\Python38-32\Lib\phantomjs.exe")
url = "https://finance.yahoo.com/quote/AAPL?=AAPL"
browser.get(url)
elements = browser.find_elements_by_xpath("html")
for element in elements:
    newelements = element.find_elements_by_xpath("./*")
    for newelement in newelements:
          print(newelement.tag_name)
    


#1 finding the general x path of the required data
#2 finding the  exact  x path of the required data
#3 trimming the text data to convert json data
#4 finding the json path
