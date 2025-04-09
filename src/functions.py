'''
FUNCTIONS
'''
import pandas as pd
import numpy as np


#Se usará la moda para columnas con elementos alfabeticos
# funcion para calcular la moda de los elementos de una columna
def mode_calculator(df, column):
    column_mode = df[column].mode()
    return column_mode[0]


#Se usará la media para columnas con elementos numericos
# funcion para calcular la media de los elementos de una columna
def mean_calculator(df, column):
    df[column] = df[column].replace(['UNKNOWN', 'ERROR'], np.nan)
    df[column] = pd.to_numeric(df[column], errors='coerce') # convertir a valores numericos
    column_mean = df[column].mean()
    return column_mean

# funcion para reemplazar valores UNKNOWN, ERROR y NaN con la moda o la media de la columna
def data_replacement(df, column, option):
    df[column] = df[column].fillna(option)
    df[column] = df[column].replace('UNKNOWN', option)
    df[column] = df[column].replace('ERROR', option)
    return True