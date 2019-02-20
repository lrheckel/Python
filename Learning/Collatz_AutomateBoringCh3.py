#!/usr/bin/env python
# coding: utf-8


################
#
#this command creates the template.py file in the same directory
#
#Keep this commented out, except to run it

#!jupyter nbconvert --to python Template.ipynb

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

# Common standard libraries

import datetime
import time
import os

# import pytest  #comment out until required.

# Ignore warnings (don't display stderr)
#import warnings
#warnings.filterwarnings('ignore')

'''
The program accepts an integer input then runs the Collatz Sequence.


'''

#Input for a positive integer
#From the User_Input.py file
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

def collatz(number):
    #check for even/odd
    if number%2 > 0:  #odd, using modulus function
        answer=(3*number) + 1
        print(str(answer))
        #print("Answer odd is " + str(answer))
        collatz(answer)
        #print("odd")
    else:
        answer=number // 2
        #print("Answer even is " + str(answer))
        #print("even")
        if answer == 1:
            print(str(answer))
            print("The end")
        else:
            print(str(answer))
            collatz(answer)
    return number


firstNum = get_positive_int("Please enter a positive integer: ")

number2=collatz(firstNum)


