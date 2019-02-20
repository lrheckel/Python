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


# In[39]:


# Common external libraries

import scipy
import pandas as pd
import numpy as np
import sklearn # scikit-learn
import skimage  #scikit-image
import statsmodels as sm

import requests  #HTTP information
from bs4 import BeautifulSoup
import mlxtend as mlextend

import pdir  #pdir2

import graphviz
import bokeh
import sympy

import h5py  #HDF5 module
import tables  #pytables
import cython  #interaction with C modules

# import pytest  #comment out until required.


# In[21]:


# Visualization libraries

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[38]:


# Load external external iPython modules

get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('load_ext', 'version_information')

# %lsmagic  #list the available magic commands, leave commented
# %version_information  #version info for python, ipython, and OS
# %version_information scipy,pandas, numpy, sklearn, skimage, requests


# In[23]:


# Setting plot appearance
# See here for more options: https://matplotlib.org/users/customizing.html

get_ipython().run_line_magic('config', "InlineBackend.figure_format='retina'")
sns.set() # Revert to matplotlib defaults
plt.rcParams['figure.figsize'] = (9, 6)
plt.rcParams['axes.labelpad'] = 10
sns.set_style("darkgrid")
# sns.set_context("poster", font_scale=1.0)


# In[24]:


# Ignore warnings (don't display stderr)

import warnings
warnings.filterwarnings('ignore')

