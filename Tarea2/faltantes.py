import numpy as np


def insertar_nans(data, seed=None):
    df_conna = data.copy()  
    length = len(df_conna)
    
    # Establecer la semilla si se proporciona
    if seed is not None:
        np.random.seed(seed)
    
    for i in df_conna.columns:
        num = int(np.random.randint(0, 90) / 100 * length)
        filas_reemplazar = np.random.choice(length, size=num, replace=False)
        df_conna.loc[filas_reemplazar, i] = np.nan
    
    return df_conna
    


def impute_nan_meanmedian(df, variable, value):
    if value=="median":
        val=df[variable].median()
    if value=="mean":
        val=df[variable].mean()
    df[variable+"_"+value]=df[variable].fillna(val)
    return df
import random
def rand_float_range(start, end):
    return random.random() * (end - start) + start

def impute_nan_random(df, variable, value=-9):
    if value!=-9:
        df[variable+"_random_fixed"]=df[variable].fillna(value)
    else:
        start,end=df[variable].min(),df[variable].max()
        df[variable+"_random"]=df[variable].fillna(rand_float_range(start,end))
    return df
    






