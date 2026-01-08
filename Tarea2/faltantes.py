import numpy as np
import random
import pandas as pd
from sklearn.impute import KNNImputer


class GestorFaltantes:
    """
    Clase para gestionar valores faltantes en DataFrames.
    Incluye métodos para insertar NaNs, imputar valores y mostrar estadísticas.
    """
    
    @staticmethod
    def insertar_nans(data, porcentaje=20, por_columna=None, seed=None):
        """
        Inserta NaNs aleatoriamente en un DataFrame.
        
        Parameters:
        -----------
        data : pandas.DataFrame
            DataFrame original
        porcentaje : float o int, default=20
            Porcentaje de NaNs a insertar (0-100)
        por_columna : dict, default=None
            Diccionario con porcentajes específicos por columna
        seed : int, default=None
            Semilla para reproducibilidad
        
        Returns:
        --------
        pandas.DataFrame
            DataFrame con NaNs insertados
        """
        df_conna = data.copy()  
        length = len(df_conna)
        
        if seed is not None:
            np.random.seed(seed)
        
        for columna in df_conna.columns:
            if por_columna is not None and columna in por_columna:
                porc = por_columna[columna]
            else:
                porc = porcentaje
            
            num_nans = int(length * porc / 100)
            
            if num_nans > 0:
                filas_reemplazar = np.random.choice(length, size=num_nans, replace=False)
                df_conna.loc[filas_reemplazar, columna] = np.nan
        
        return df_conna
    
    
    @staticmethod
    def impute_nan_meanmedian(df, variable, value):
      
        if value == "median":
            val = df[variable].median()
        if value == "mean":
            val = df[variable].mean()
        df[variable+"_"+value]=df[variable].fillna(val)
        return df
    
    
    @staticmethod
    def _rand_float_range(start, end):
        """Método auxiliar para generar número aleatorio en un rango."""
        return random.random() * (end - start) + start
    
    
    @staticmethod
    def impute_nan_random(df, variable, value=-9):
        """
        Imputa NaNs con valor fijo o aleatorio.
        
        Parameters:
        -----------
        df : pandas.DataFrame
            DataFrame a imputar
        variable : str
            Nombre de la columna
        value : float o int, default=-9
            Si != -9: valor fijo, si == -9: valor aleatorio
        
        Returns:
        --------
        pandas.DataFrame
            DataFrame con nueva columna imputada
        """
        if value != -9:
            df[variable + "_random_fixed"] = df[variable].fillna(value)
        else:
            start, end = df[variable].min(), df[variable].max()
            df[variable + "_random"] = df[variable].fillna(
                GestorFaltantes._rand_float_range(start, end)
            )
        return df
    
    
    @staticmethod
    def mostrar_nans(df: pd.DataFrame):
        """
        Muestra información detallada sobre los datos faltantes en un DataFrame,
        con formato tabular más estético.
        
        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame a analizar
        """
        total_valores = df.shape[0] * df.shape[1]
        total_nans = df.isna().sum().sum()
        porcentaje_global = np.round(total_nans / total_valores * 100, 2)

        print("=" * 70)
        print(f"📊 Dataset: {len(df)} filas × {len(df.columns)} columnas")
        print(f"🔎 Valores totales: {total_valores}")
        print(f"❌ NaNs totales: {total_nans} ({porcentaje_global}%)")
        print("=" * 70)
        print("\nNaNs por columna:\n")

        # Encabezado de la tabla
        print(f"{'Columna':<25} | {'NaNs':<10} | {'% NaNs':<10}")
        print("-" * 70)

        # Filas de la tabla
        for columna in df.columns:
            num_nans = df[columna].isna().sum()
            porcentaje = np.round(num_nans / len(df) * 100, 2)
            print(f"{columna:<25} | {num_nans:<10} | {porcentaje:<10}")

        print("=" * 70)




    
    @staticmethod
    def knn_imputer_dataframe(df, n_neighbors=5, weights='uniform', metric='nan_euclidean'):
        """
        Aplica KNNImputer a un DataFrame y devuelve un nuevo DataFrame
        con los valores imputados y los mismos nombres de columnas.
        Solo imputa columnas numéricas, las categóricas se mantienen sin cambios.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame con posibles NaNs
        n_neighbors : int, opcional
            Número de vecinos a considerar (default=5)
        weights : str, opcional
            'uniform' o 'distance' para ponderar vecinos
        metric : str, opcional
            Métrica de distancia (default='nan_euclidean')

        Returns
        -------
        pandas.DataFrame
            DataFrame imputado con los mismos nombres de columnas
        """
        # Separar columnas numéricas y categóricas
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(exclude=[np.number]).columns
        
        if len(numeric_cols) == 0:
            raise ValueError("El DataFrame no contiene columnas numéricas para imputar")
        
        # Aplicar KNNImputer solo a columnas numéricas
        df_numeric = df[numeric_cols].copy()
        imputer = KNNImputer(n_neighbors=n_neighbors, weights=weights, metric=metric)
        Xtrans = imputer.fit_transform(df_numeric)
        
        # Crear DataFrame imputado con columnas numéricas
        df_numeric_imputed = pd.DataFrame(Xtrans, columns=numeric_cols, index=df.index)
        
        # Combinar con columnas categóricas (sin cambios)
        if len(categorical_cols) > 0:
            df_imputed = pd.concat([df_numeric_imputed, df[categorical_cols]], axis=1)
            # Reordenar columnas según el orden original
            df_imputed = df_imputed[df.columns]
        else:
            df_imputed = df_numeric_imputed
        
        return df_imputed