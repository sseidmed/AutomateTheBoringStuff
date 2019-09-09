'''
Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.'''

import re

def myexpression(mystring):
  x = re.compile(r'[A-Za-z0-9]{8,8}')
  mo = x.search(mystring)
  return not mo == None

print(myexpression('IamTestingaPassword5673')) #True
print(myexpression('Still3'))                  #False
print(myexpression('Hello#####$$$$$$$$$8'))    #False
