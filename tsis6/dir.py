# 1 
import os
path = 'C:\\Users\LENOVO\Desktop\pp2-22B050871\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("Only files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
print("All directories ,  files :")
print([ name for name in os.listdir(path)])

2 

print('Exist:', os.access('C:\\Users\LENOVO\Desktop\pp2-22B050871\\', os.F_OK))
print('Readable:', os.access('C:\\Users\LENOVO\Desktop\pp2-22B050871\\', os.R_OK))
print('Writable:', os.access('C:\\Users\LENOVO\Desktop\pp2-22B050871\\', os.W_OK))
print('Executable:', os.access('C:\\Users\LENOVO\Desktop\pp2-22B050871\\', os.X_OK))


3 
path = 'C:\\Users\\LENOVO\\Desktop\\pp2-22B050871\\'
check = os.path.exists(path)
if check == True:
    direct, files = os.path.split(path)
    print('Directory:' ,direct)
    print( 'File:',files)

4 
with open("test.txt" , "r") as f:
    print (sum(1 for _ in f))

5
my_list = ['PP1','PP2','PP3','PP4']
with open('test.txt', 'w') as my_file:
    for i in my_list:
        my_file.write("%s\n" % i)
content = open('test.txt')
print(content.read())

6
list1 = ['A' , 'B' , 'C' , 'D', 'E' , 'F' ,'G' , 'H' ,'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
for i in list1:
    files = f'{i}.txt'
    with open(files, "w") as file:
        file.write('a')

7 
from shutil import copyfile
copyfile('test.txt', 'file_Z.txt')

8 
path = 'C:\\Users\\LENOVO\\Desktop\\pp2-22B050871\\'
if os.access(path, os.F_OK) and (os.path.isfile('delete.txt')):
   os.remove('delete.txt')
   print('ok')
else:
    print(f'{path} does not exist')