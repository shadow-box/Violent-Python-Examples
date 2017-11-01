#!/usr/bin/env python3

import json
from watson_developer_cloud import ToneAnalyzerV3
import os
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/login")
    #assert "Python" in driver.title
    email = driver.find_element_by_class_name("js-username-field")
    password = driver.find_element_by_class_name("js-password-field")
    email.clear
    password.clear
    email.send_keys("username")
    password.send_keys("password", Keys.RETURN)
    sleep(5)
    assert "No results found." not in driver.page_source
    driver.get("https://twitter.com/")
    load_count = 0
    while load_count < 25:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        load_count += 1
    return driver



soup = BeautifulSoup(str(driver.page_source), "lxml")#set up bs4 object from robo browser page content
#load_tweets(soup)



#    email = wait.until(EC.visibility_of_element_located((By.NAME, "session[username_or_email]")))
#    password = wait.until(EC.visibility_of_element_located((By.NAME, "session[password]")))
