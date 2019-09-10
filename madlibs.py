'''
Mad Libs
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:


The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them.


Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:


The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.
'''

#mad libs

import re

mad = open('madlibs.txt', 'w')
mad.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.\n')
mad.close()

myfile = open('madlibs.txt', 'r')
mystring = myfile.read()
split_string = re.split(r'(\W+)', mystring)
#print(mystring) #printing contents of my file saved to 'mystring' variable
#print(split_string)

myregex = re.compile(r'[A-Z+]{4,}')
mo1 = myregex.findall(mystring) #finds all capitalized words to replace


for i in mo1:
	if i == "ADJECTIVE":
		adjective = input("Enter an adjective: ")
		mo1[mo1.index(i)] = adjective
		split_string[split_string.index(i)] = adjective  
		#print(split_string)
		#print(mo1)
	elif i == "NOUN":
		noun = input("Enter a noun: ")
		mo1[mo1.index(i)] = noun
		split_string[split_string.index(i)] = noun  
		#print(split_string)
		#print(mo1)
	elif i == "VERB":
		verb = input("Enter a verb: ")
		mo1[mo1.index(i)] = verb
		split_string[split_string.index(i)] = verb  
		#print(split_string)
		#print(mo1)
	elif i == "ADVERB":
		adverb = input("Enter an adverb: ")
		mo1[mo1.index(i)] = adverb
		split_string[split_string.index(i)] = adverb  
		#print(split_string)
		#print(mo1)

new_string = ''.join(split_string)
print(new_string)

new_mad = open('new_madlibs.txt', 'w')
new_mad.write(new_string + '\n')
new_mad.close()
