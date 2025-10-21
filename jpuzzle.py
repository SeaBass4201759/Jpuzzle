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

list1 = []
list2 = []


while True:
        user_input = input("Please enter the name of the files. When done press 'd': ")

        if user_input == 'd':
                break 
        list1.append(user_input)

print(f"These are your file you entered {list1}")



def starts_with_soi(filename):
        with open(filename, 'rb') as f:
                start_bytes = f.read(2)
        return start_bytes == b'\xFF\xD8'


def ends_with_eoi(filename):
        with open(filename, 'rb') as f:
                f.seek(-2, os.SEEK_END)
                end_bytes = f.read(2)
        return end_bytes == b'\xFF\xD9'


print("Files that start with SOI (FF D8): ")
for p in list1:
        if starts_with_soi(p):
                print(p)
                pindex1 = list1.index(p)


                list2.append(p)
                list1.pop(pindex1)



print("Files that end with EOI (FF D9): ")
for p in list1:
        if ends_with_eoi(p):
                print(p)
                pindex2 = list1.index(p)


                list2.append(p)
                list1.pop(pindex2)

def makedatshi():
        output_dir = 'reconstructed_images'
        os.makedirs(output_dir, exist_ok=True)


        num = 0

        for i in itertools.permutations(list1):
                num += 1

                i = list(i)
                i.append(list2[1])
                i.insert(0,list2[0])


                inputFiles = i
                outputFile = os.path.join(output_dir, f'img_{num}.jpg')


                with open(outputFile , 'wb') as outfile:
                        for fname in inputFiles:
                                with open(fname, 'rb') as infile:
                                        outfile.write(infile.read())
makedatshi()
