import numpy as np


def insertar_nans(data, porcentaje=20, por_columna=None, seed=None):
    
    df_conna = data.copy()  
    length = len(df_conna)
    
    # Establecer la semilla si se proporciona
    if seed is not None:
        np.random.seed(seed)
    
    for columna in df_conna.columns:
        # Determinar el porcentaje para esta columna
        if por_columna is not None and columna in por_columna:
            porc = por_columna[columna]
        else:
            porc = porcentaje
        
        # Calcular número de NaNs a insertar
        num_nans = int(length * porc / 100)
        
        # Seleccionar filas aleatorias
        if num_nans > 0:
            filas_reemplazar = np.random.choice(length, size=num_nans, replace=False)
            df_conna.loc[filas_reemplazar, columna] = np.nan
    
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
    

def mostrar_nans(df):
    """
    Muestra información detallada sobre los datos faltantes en un DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame a analizar
    """
    # Información general
    total_valores = df.shape[0] * df.shape[1]
    total_nans = df.isna().sum().sum()
    porcentaje_global = np.round(total_nans / total_valores * 100, 2)
    
    print(f"Dataset: {len(df)} filas × {len(df.columns)} columnas = {total_valores} valores totales")
    print(f"NaNs totales: {total_nans} ({porcentaje_global}%)")
    print("\nNaNs por columna:")
    print("="*60)
    
    # Información por columna
    for columna in df.columns:
        num_nans = df[columna].isna().sum()
        porcentaje = np.round(num_nans / len(df) * 100, 2)
        print(f"{columna}: {num_nans} NaNs ({porcentaje}%)")




