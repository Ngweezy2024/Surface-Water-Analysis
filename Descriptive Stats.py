# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:01:09 2024

@author: ADMIN
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
# Specify the path to your Excel file
df = pd.read_csv('C:/Users/ADMIN/Desktop/PROJECT$$/india2012.csv')

# Specify the column name you want to plot
column_name = 'Amount of Calcium (Ca)'

# Extract the values of the specified column
column_values = df[column_name]

# Generate the histogram
plt.hist(column_values)
plt.xlabel(column_name)
plt.ylabel('Frequency')
plt.title('Histogram of ' + column_name)
plt.show()

# Generate the density curve (bell curve)
sns.kdeplot(column_values, shade=True)
plt.xlabel(column_name)
plt.ylabel('Density')
plt.title('Bell Curve of ' + column_name)
plt.show()

# Generate the violin plot
sns.violinplot(data=df, y=column_name)
plt.ylabel(column_name)
plt.title('Violin Plot of ' + column_name)
plt.show()