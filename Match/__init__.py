#@author Xavier Collantes
#@date May 5 2019
#@file Match.py

import logging
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os, sys

logging.basicConfig(level=logging.DEBUG)

class Match:
  def __init__(self, user, pw, driverPath='/home/ec2-user/match/chromedriver'):
    self.user = user
    self.pw = pw
    self.driverPath = driverPath






  def logIn(self):
    logging.info("Logging in")
    logging.debug(os.getcwd())

    options = Options()
    options.headless = True
    options.binary_location = '/usr/bin/google-chrome'
    browser = webdriver.Chrome(executable_path=self.driverPath, chrome_options=options)
    #browser.get('https://www.match.com/login/')    
    browser.get('https://www.google.com')
