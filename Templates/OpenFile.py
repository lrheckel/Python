#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:49:10 2018

@author: larry
"""

import os

#put the file name here
file1 = 'array_ex.txt'   #just the file name itself
file2 = 'pydata-book-2nd-edition/examples/array_ex.txt'  #relative dir location to current directory
file3 = '/media/larry/Samsung_T5/Learning/Python/pydata-book-2nd-edition/examples/array_ex.txt'   #complete path to file

#######################################
#if the scenario is 1 or 2, get the full file path into a string.
#Assumption is that, if a filename or relative path comes in,
#it is in the directory path of the file that is
#currently being executed

#set the directory to current
#set an absolute path
curDir = os.path.abspath('.') #sets the current directory to the one holding the file being executed.
os.chdir(curDir) #sets the new current working directory
cwd = os.getcwd()  #put the current working directory into string variable
    
#check to see if the file exists and assign to filepath variable
if len(file1)>0:
    if os.path.isfile(os.path.join(cwd, file1)):
        filepath = os.path.join(cwd, file1)
        #print(filepath)
    else:
        #error, the file doesn't exist
        print('other1')
elif len(file2)>0:
    if os.path.isfile(os.path.join(cwd, file2)):
        filepath = os.path.join(cwd, file2)
        #print(filepath)
    else:
        #error, the file doesn't exist
        print('other2')
elif len(file3)>0:
    if os.path.isfile(file3):
        filepath = (file3)
        #print(filepath)
    else:
        #error, the file doesn't exist
        print('other3')
else:
    print('error')
       
#now go ahead and open the file, for a directory and filename (relative path or just name)
#open file for full path and filename and strip the EOL from each string
with open(filepath, 'r') as f:
    for line in f:
        line = line.rstrip("\n")
        #print(line)
    f.seek(0)
    content = f.readlines()

for x in range(len(content)):
    content[x] = content[x].rstrip()
    #print(content[x])
    
print(content)
    
f.close()



