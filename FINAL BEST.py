# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:39:35 2024

@author: ADMIN
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to load and concatenate data for a given season
def load_seasonal_data(season, years):
    dfs = []
    for year in years:
        df = pd.read_csv(f'C:/Users/ADMIN/Desktop/PROJECT$$/New/{season}{year}.csv')
        df['Year'] = year
        dfs.append(df)
    combined_df = pd.concat(dfs)
    combined_df.reset_index(drop=True, inplace=True)
    combined_df['Month'] = pd.to_datetime(combined_df['Month'], errors='coerce')
    combined_df['Amount of Sulfate (SO4)'] = combined_df['Amount of Sulfate (SO4)'].fillna(combined_df['Amount of Sulfate (SO4)'].mean())
    combined_df['Amount of Total Dissolved Solids (TDS)'] = combined_df['Amount of Total Dissolved Solids (TDS)'].fillna(combined_df['Amount of Total Dissolved Solids (TDS)'].mean())
    combined_df['Amount of Potential of Hydrogen (H+, pH)'] = combined_df['Amount of Potential of Hydrogen (H+, pH)'].fillna(combined_df['Amount of Potential of Hydrogen (H+, pH)'].mean())
    return combined_df

# Years to be loaded
years = range(2012, 2020)

# Load data for each season
pre_monsoon_df = load_seasonal_data('premoonsoon', years)
monsoon_df = load_seasonal_data('moonsoon', years)
post_monsoon_df = load_seasonal_data('postmoonsoon', years)

# Function to calculate yearly averages
def calculate_yearly_averages(df):
    numeric_df = df.select_dtypes(include=[float, int])
    numeric_df['Year'] = df['Year']
    yearly_averages = numeric_df.groupby('Year').mean()
    return yearly_averages

# Calculate yearly averages for each season
pre_monsoon_averages = calculate_yearly_averages(pre_monsoon_df)
monsoon_averages = calculate_yearly_averages(monsoon_df)
post_monsoon_averages = calculate_yearly_averages(post_monsoon_df)

# Function to plot trend and perform trend analysis
def plot_trend(compound):
    plt.figure(figsize=(12, 8))
    
    # Pre-monsoon plot
    plt.plot(pre_monsoon_averages.index, pre_monsoon_averages[f'Amount of {compound}'], marker='o', label='Pre-monsoon')
    
    # Monsoon plot
    plt.plot(monsoon_averages.index, monsoon_averages[f'Amount of {compound}'], marker='o', label='Monsoon')
    
    # Post-monsoon plot
    plt.plot(post_monsoon_averages.index, post_monsoon_averages[f'Amount of {compound}'], marker='o', label='Post-monsoon')
    
    plt.xlabel('Year')
    plt.ylabel('Concentration(mg/l)')
    plt.title(f'Temporal Variation in Concentration of {compound} in Andhra Pradesh')
    plt.legend()
    plt.show()
    
    # Pre-monsoon trend analysis
    slope, intercept, r_value, p_value, std_err = linregress(pre_monsoon_averages.index, pre_monsoon_averages[f'Amount of {compound}'])
    print(f"Pre-monsoon {compound} - Slope: {slope}, P-value: {p_value}")
    
    # Monsoon trend analysis
    slope, intercept, r_value, p_value, std_err = linregress(monsoon_averages.index, monsoon_averages[f'Amount of {compound}'])
    print(f"Monsoon {compound} - Slope: {slope}, P-value: {p_value}")
    
    # Post-monsoon trend analysis
    slope, intercept, r_value, p_value, std_err = linregress(post_monsoon_averages.index, post_monsoon_averages[f'Amount of {compound}'])
    print(f"Post-monsoon {compound} - Slope: {slope}, P-value: {p_value}")

# List of compounds to plot
compounds = ['Sodium (Na)', 'Potassium (K)', 'Sulfate (SO4)']

# Plot trends for each compound
for compound in compounds:
    plot_trend(compound)
