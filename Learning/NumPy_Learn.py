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


#Create a 8x8 matrix and fill it with a checkerboard pattern
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)





