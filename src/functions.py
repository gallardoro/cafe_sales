'''
FUNCTIONS
    This is a Python module created for the optimization of the Dirty Cafe Sales data analysis code
'''
import pandas as pd
import numpy as np

# Mode would be used for string elements
# calculate mode per column
def mode_calculator(df, column):
    column_mode = df[column].mode()
    return column_mode[0]

# Mean would be used for numeric elements
# calculate mean per column
def mean_calculator(df, column):
    df[column] = df[column].replace(['UNKNOWN', 'ERROR'], np.nan)
    df[column] = pd.to_numeric(df[column], errors='coerce') # convert to numeric before making math processes
    column_mean = df[column].mean()
    return column_mean

# replace UNKNOWN, ERROR and NaN values with the Mean or Mode as required
def data_replacement(df, column, mean_or_mode):
    df[column] = df[column].fillna(mean_or_mode)
    df[column] = df[column].replace('UNKNOWN', mean_or_mode)
    df[column] = df[column].replace('ERROR', mean_or_mode)
    return 'Column Affected'

# Calculate total spent
def total_spent_calculator(df, column_0, column_1, column_2):
    df.loc[df[column_0].isna(), column_0] = df[column_1] * df[column_2]
    
