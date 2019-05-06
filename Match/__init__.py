#@author Xavier Collantes
#@date May 5 2019
#@file Match.py

import logging
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.DEBUG)

class Match:

  def __init__(self, user, pw, driverPath='/home/ec2-user/match/chromedriver'):
    self.user = user
    self.pw = pw
    self.driverPath = driverPath

    options = Options()
    options.headless = True
    options.binary_location = '/usr/bin/google-chrome'
    self.browser = webdriver.Chrome(executable_path=self.driverPath, chrome_options=options)




  def logIn(self):
    logging.info("Logging in")

    self.browser.get('https://www.match.com/login/')    
    self.browser.get_element_by_id('email').send_keys(self.user)
    self.browser.get_element_by_id('password').send_keys(self.pw)
    self.browser.get_element_by_xpath('//*[@id="mainContent"]/section/form/div/div/div[1]/div[5]/button').click()


  def quit():
    self.browser.quit()
