#@author Xavier Collantes
#@date May 5 2019

import yaml
from Match import *
import os



def main():
  with open('temp.yaml') as f:
    config = yaml.safe_load(f)

  username = config['test_credentials']['user']
  passwd = config['test_credentials']['passwd']
  
  match = Match(username, passwd)
  match.logIn()




if __name__=='__main__':
  main()
