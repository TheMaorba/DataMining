import numpy as np

class ManejoFaltantes():
    # Esto me va ayudar a responder el punto 3 de la actividad donde tengo que llenar los datos faltantes
    @staticmethod
    def crear_faltantes_columna(df, columna, porcentaje, seed=None):
        # Reproducibilidad
        if seed is not None:
            np.random.seed(seed)
        
        # Copio el original
        df_nuevo = df.copy()
        
        # Número de filas
        n = len(df_nuevo)
        
        # Cantidad de NaN a crear
        cantidad_nan = int(n * porcentaje)
        
        # Seleccionar filas al azar
        filas = np.random.choice(n, cantidad_nan, replace=False)
        
        # Asignar valores faltantes en esa columna
        df_nuevo.loc[filas, columna] = np.nan
        
        return df_nuevo

    @staticmethod
    def eliminar_faltantes(df):
        return df.dropna()
    
    @staticmethod
    def contar_faltantes(df):
        total_faltantes = df.isna().sum().sum()
        return total_faltantes