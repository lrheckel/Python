#!/usr/bin/env python
# coding: utf-8

# In[2]:


################
#
#this command creates the template.py file in the same directory
#
#Keep this commented out, except to run it

#!jupyter nbconvert --to python Template.ipynb


# In[18]:


#############
#
# Header information here
#
# Template notebook
#
# Larry Heckel
#
# October 21, 2018
#
##############


# In[19]:


# Common standard libraries

import datetime
import time
import os

import numpy as np

'''
np.random.seed(0)
x1=np.random.randint(10, size=6)
x2=np.random.randint(10, size=(3,4))
x3=np.random.randint(10, size=(3,4,5))

#attributes of the array
print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)
print("x3 dtype: ", x3.dtype)
print("x3 itemsize: ", x3.itemsize)
print("x3 nbytes: ", x3.nbytes)
'''

'''
Ask for the first number
    If is a positive integer
        store the number in the first variable
    If not
        ask for the integer again
        
Ask for the second number
    If is a positive integer
        store the number in the first variable
    If not
        ask for the integer again
        
Compute the first fibonacci number and set to varx
    0,1,1,2,3,5,8,13,21,34,55, etc.

Compute the second fibonacci number and set to vary

Compute GCF of varx and vary

Output the five numbers

'''

#input the numbers
  
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("What you entered is not an integer. Please try again.")
            continue

        if value <= 0:
            print("Your integer must be greater than zero. Please try again.")
            continue
        else:
            break
    return value

firstNum = get_positive_int("Please enter a positive integer: ")
secNum = get_positive_int("Please enter a second positive integer: ")

inputNums = [firstNum, secNum]
for i in range(len(inputNums)):
    #print(inputNums[i])
    #seed the summing numbers
    priorNum=0
    currNum=1
    fibNum=0
    if inputNums[i] == 1:
        print("first is " + str(firstNum))
        print("You entered: " + str(firstNum))
        print("The Fibonacci number is " + str(fibNum))
    elif inputNums[i] == 2:
        print("second is " + str(firstNum))
        fibNum=1
        print("You entered: " + str(firstNum))
        print("The Fibonacci number is " + str(fibNum))
    else:
        for A in range(3,inputNums[i]+1):
            #print("number is " + str(A))
            fibNum = priorNum + currNum
            #print("fibNum " + str(fibNum))
            #print("priorNum before " + str(priorNum))
            #print("currNum before " + str(currNum))
            priorNum = currNum
            currNum = fibNum
    print("You entered: " + str(inputNums[i]))
    #print("priorNum " + str(priorNum))
    #print("currNum " + str(currNum))
    print("The Fibonacci number is " + str(fibNum)) 

