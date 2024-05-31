# -*- coding: utf-8 -*-
"""
Created on Mon May 20 07:55:23 2024

@author: ADMIN
"""

#DATA CLEANING 

#Importing neccessary modules

import numpy as np
import pandas as pd

#Load the dataset

df=pd.read_csv("C:/Users/ADMIN/Desktop/PROJECT$$/andhra_surfacewq.csv")

head=df.head()
print(head)

tail=df.tail()
print(tail)

#Handling missing values: NAN 

print(df.isnull().sum()) #Count all missing values
df.dropna()       #Drop rows with missing values
df.fillna(avg)    #Replace/fill missing values #NONE

#Remove Duplicates
print(df.isduplicate().sum()) 
df.dropduplicates() #Remove duplicate rows #NONE

df[(df['date'] >= '2024-01-01') & (df['date'] <= '2024-05-30')]





