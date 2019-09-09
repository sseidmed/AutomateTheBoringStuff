'''
Regex Version of strip()
Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.'''

#use sub() method
import re
def strip_char(mystring, subset=None):
  if subset == None:
    return mystring.strip()
  else:
    mystring = mystring.strip()
    myregex = re.compile(subset)
    mo1 = myregex.sub('', mystring)
    return mo1

print(strip_char(" xoxo love xoxo ", 'xoxo'))
print(strip_char("android is awesome", 'android'))
