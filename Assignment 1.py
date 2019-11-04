#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Name : Ahtisham Ansari
Roll No : PY00361
"""


# In[13]:


# Q.1

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[14]:


# Q.2

import sys

print("Python Version")
print(sys.version)


# In[16]:


# Q.3

import datetime

date_time = datetime.datetime.now()

print(date_time)


# In[18]:


# Q.4

from math import pi

r = 2.2

print("The radius of the circle" + str(r))
print("TThe area of the circle with radius" + str(r) + " is " + str(pi * r**2))


# In[19]:


# Q.5

fname = "Ahtisham"
lname = "Ansari"

print(lname + " " + fname)


# In[23]:


# Q.6

roll_no = input("Enter your roll no : ")
name = input("Enter your name : ")

print("\nYour roll number is " + roll_no)
print("Your name is " + name)


