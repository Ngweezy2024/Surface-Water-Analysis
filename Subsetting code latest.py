# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:02:25 2024

@author: ADMIN
"""

import pandas as pd

# Function to subset data based on date column
def subset_data_by_date(csv_file, date_column, start_date, end_date, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert the date column to datetime format
    df[date_column] = pd.to_datetime(df[date_column], format='%d-%b-%y')
    
    # Convert start_date and end_date to datetime objects
    start_date = pd.to_datetime(start_date, format='%d-%b-%Y')
    end_date = pd.to_datetime(end_date, format='%d-%b-%Y')
    
    # Filter the DataFrame based on the date range
    subset_df = df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]
    
    # Write the subset DataFrame to a new CSV file
    subset_df.to_csv(output_file, index=False)
    print(f"Subset data saved to {output_file}")

# Example usage
csv_file = 'C:/Users/ADMIN/Desktop/PROJECT$$/india2020.csv'  # Path to your CSV file
date_column = 'Month'  # Column name with dates in dd-Mmm-yy format
start_date = '20-Oct-2022'  # Start date in dd-Mmm-yyyy format
end_date = '20-Dec-2022'  # End date in dd-Mmm-yyyy format
output_file = 'C:/Users/ADMIN/Desktop/PROJECT$$/postmoonnsoon2020.csv'  # Output file path

subset_data_by_date(csv_file, date_column, start_date, end_date, output_file)
