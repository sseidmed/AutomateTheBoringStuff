'''
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
Copy these files from whatever location they are in to a new folder.

1. os.walk()
2. finds .pdf or .jpg files
3. copy those files to a new folder 

'''

import os, shutil
os.chdir('C:\\Users\\Shahlo\\Desktop\\AOS')
mypath = 'C:\\Users\\Shahlo\\Desktop\\AOS'
backup = 'C:\\Users\\Shahlo\\Desktop\\AOS_backup'


for folderName, subfolders, filenames in os.walk(mypath):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if filename.lower().endswith('.docx'):
            print('FILE INSIDE ' + folderName + ': '+ filename)
            print(os.path.join(folderName, filename))
            shutil.copy(os.path.join(folderName, filename), backup)

    print('')
print("Backup finished")
