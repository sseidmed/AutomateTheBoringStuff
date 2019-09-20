#!python
#This will log in your email and send out an email 
#to the specified recipient with the body of text from command line

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys


if len(sys.argv) < 2:
	print('Enter the body of email that you want to send')
	sys.exit()

#assign email and message values to variables	
recipient_email = sys.argv[1]
email_text = ' '.join(sys.argv[2:])

#open the browser and Gmail
browser = webdriver.Chrome()
browser.get('https://gmail.com')

#find user login field and enter email
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('your_email@gmail.com')

#find and click the Next button
nextElem = browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
time.sleep(3)

#find the password field and enter your password
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('your_password')

#click on the Next button
finishElem = browser.find_element_by_id('passwordNext').click()

time.sleep(3)
#get the new page, displaying all your Inbox
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(3)

#get the recipient email line
email_line = browser.find_element_by_id(':169')
email_line.send_keys(recipient_email)
time.sleep(5)

#get and click on the subject box
message = browser.find_element_by_css_selector("div[aria-label='Message Body']")
message.click()
message.send_keys(email_text)
time.sleep(5)

#get the Send button and click on it
send_button = message.send_keys(Keys.TAB + Keys.ENTER)
time.sleep(5)

#safely close your browser. Now you are done!
browser.quit()

