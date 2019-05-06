#@author Xavier Collantes
#@date May 5 2019

from Match import *
import os



def main():
  username = 'Me'
  passwd = 'Hello'
  os.getcwd()
  match = Match(username, passwd)
  match.logIn()




if __name__=='__main__':
  main()
