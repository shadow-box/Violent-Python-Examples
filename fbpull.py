#!/usr/bin/env python3

import json
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
    driver.get("https://www.facebook.com")
    #assert "Python" in driver.title
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    email.clear
    password.clear
    email.send_keys("user@email.com")
    password.send_keys("p@ssw0rd", Keys.RETURN)
    sleep(5)
    assert "No results found." not in driver.page_source
    return driver
   
driver = login()

load_count = 0
while load_count < 0:
    print("Do stuff")

friends = soup.findAll("div", {"class" : "fsl fwb fcb }) ## Builds list of friends
                               
                            

#soup = BeautifulSoup(str(driver.page_source), "lxml")#set up bs4 object from robo browser page content
#load_tweets(soup)



#    email = wait.until(EC.visibility_of_element_located((By.NAME, "session[username_or_email]")))
#    password = wait.until(EC.visibility_of_element_located((By.NAME, "session[password]")))
