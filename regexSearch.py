import re, os

work_dir = 'C:\\Users\\Shahlo\\Desktop\\code related\\python_work'
os.chdir(work_dir)

def regsearch(user_input):
	for i in os.listdir():
		if i.endswith('.txt'):
			f = open(i, 'r')			
			read_file = f.read()
			string = ''.join(read_file)
			var1 = re.compile(user_input)
			mo1 = var1.findall(read_file)
			found_mo1 = ' '.join(mo1)
			print(found_mo1)
			f.close()		
		
			
regsearch('[0-9]')
