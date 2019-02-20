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

my_list=['aaa','bbb','ccc','ddd']

#parse a list and put the values into a string
my_list=['aaa','bbb','ccc','ddd']
print(my_list)

#parse a list and put the values into a string
def parse_list(myvalue=[]):
    str_list = ''
    list_len = len(myvalue)
    for i in range(list_len - 1):
        str_list = (str_list + myvalue[i] + ', ')
    
    str_list = (str_list + 'and ' + myvalue[list_len-1]) #last item in the list
    print(str_list)
    
parse_list(my_list)