#!python
#This will log in your email and send out an email 
#to the specified recipient with the body of text from command line
'''Here is how to run on the command line:
python commandLineEmailer.py some_email@email.com Type anything you want as a body of your message here. 
'''

#import all of the required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

#check to make sure that there is a recipient email and a message
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
emailElem.send_keys('my_email@gmail.com')

#find and click the Next button
nextElem = browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()

#give time to load the next page
time.sleep(3)

#find the password field and enter your password
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('my_password')

#click on the Next button
finishElem = browser.find_element_by_id('passwordNext').click()

#give time to load
time.sleep(3)

#get the new page, displaying all your Inbox
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')

#give time to load. My program would not without extra 3 second here
time.sleep(3)

#get the recipient email line 
email_line = browser.find_element_by_name('to')
email_line.send_keys(recipient_email)

#get and click on the subject box
message = browser.find_element_by_xpath('//*[@id=":16v"]')
message.click()
message.send_keys(email_text)

#get the Send button and click on it
send_button = browser.find_element_by_id(':15g')
send_button.click()

#wait 5 second for your email to be sent
time.sleep(5)

#safely close your browser. Now you are done!
browser.quit()

