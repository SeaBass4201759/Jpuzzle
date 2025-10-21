
import itertools
import os

def welcome():
	print('''\033[38;5;208m   d8,                                     d8b        
  `8P                                      88P        
                                          d88         
  d88  ?88,.d88b,?88   d8Pd88888P d88888P 888   d8888b
  ?88  `?88'  ?88d88   88    d8P'    d8P' ?88  d8b_,dP
   88b   88b  d8P?8(  d88  d8P'    d8P'    88b 88b    
   `88b  888888P'`?88P'?8bd88888P'd88888P'  88b`?888P'
    )88  88P'                                         
   ,88P d88                                           
`?888P  ?8P   @SeaBass4201759                         
\033[0m''')

welcome()


#start list, this grabs the user input 
list1 = []
#pop list for found SOI and EOI 
list2 = []

#grabbing user input and adding it to variable list
while True:
	user_input = input("Please enter the name of the files. When done press 'd': ")
	
	if user_input == 'd':
		break 
	list1.append(user_input)

print(f"These are your file you entered {list1}")


#searches for FF D8 given files in list
def starts_with_soi(filename):
	with open(filename, 'rb') as f:
		start_bytes = f.read(2)
	return start_bytes == b'\xFF\xD8'

#searches for FF D9 given files in list
def ends_with_eoi(filename):
	with open(filename, 'rb') as f:
		f.seek(-2, os.SEEK_END)
		end_bytes = f.read(2)
	return end_bytes == b'\xFF\xD9'




#return SOI 
print("Files that start with SOI (FF D8): ")
for p in list1:
	if starts_with_soi(p):
		print(p)
		pindex1 = list1.index(p)
		
		#add SOI file to list2 to start the brain fuck of code 
		list2.append(p)
		list1.pop(pindex1)


#returns EOI
print("Files that end with EOI (FF D9): ")
for p in list1:
	if ends_with_eoi(p):
		print(p)
		pindex2 = list1.index(p)
		
		#add EOI to list2 to start the brain fucking code 
		list2.append(p)
		list1.pop(pindex2)


num = 0
#goes through every possible iteration of files given leaving out EOI and SOI 
for i in itertools.permutations(list1):
	num += 1

	i = list(i)
	i.append(list2[1])
	i.insert(0,list2[0])
	#grab index of both items in list2 
	#append them to the start and end of i
	
	posblty = i
	print(posblty)

# Run a function that creates the image every time with the above order.

