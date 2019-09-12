
import os, shutil
os.chdir('C:\\Users\\Shahlo\\Desktop\\English books\\')
mypath = 'C:\\Users\\Shahlo\\Desktop\\English books\\'
#backup = 'C:\\Users\\Shahlo\\Desktop\\AOS_backup'


for folderName, subfolders, filenames in os.walk(mypath):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        size = os.path.getsize(filename)
        if size <= 100:
             print(os.path.abspath(filename))
            

    print('')
print("Large files found")
