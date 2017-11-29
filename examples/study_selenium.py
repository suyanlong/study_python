#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# http://blog.csdn.net/zhaoyabei/article/details/52355021
# sudo pip install selenium
# #requests模块，可选安装
# sudo pip install requests

# wget -N http://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip
# chmod +x chromedriver
# sudo mv -f chromedriver /usr/local/share/chromedriver
# sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
# sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://suyanlong.github.io/")
driver.save_screenshot(driver.title+".png")