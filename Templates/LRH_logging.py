#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:49:10 2018

@author: larry
"""
#function to write to the screen or to the log file
import logging 
import os

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

#logging to file
logging.basicConfig(filename='LogFile.txt', level='DEBUG', format=' %(asctime)s - %(levelname)s - %(message)s', filemode='a')

#logging to screen
logging.basicConfig(level='DEBUG', format=' %(asctime)s - %(levelname)s - %(message)s')

#logging.debug('Start of Program')

#set the logging level
logging.disable(logging.ERROR) #only log CRITICAL
logging.disable(logging.WARNING)  #only log ERROR/CRITICAL
   
#logging.debug('after dir path')


