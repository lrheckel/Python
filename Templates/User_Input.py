#!/usr/bin/env python
# coding: utf-8

################
#
#the below functions accept and validate keyboard input
#
#Keep this commented out, except to run it

#!jupyter nbconvert --to python Template.ipynb

# Common standard libraries

import datetime
import time
import os

########################################################
#Input for a positive integer
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

#####################################################################
