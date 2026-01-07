import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




class Graficos:
#Elaboro el constructor de la clase que se encarga de almacenar la informacion

    def __init__(self, df1=None, df2=None):  
        self.df1 = df1
        self.df2 = df2
    
    @staticmethod
    def comparar_histogramas(df_original, df_procesado, columna_original, columna_procesada=None, bins=7):
        """
        Crea histogramas comparativos de una columna antes y después del manejo de faltantes.
        
        Parameters
        ----------
        df_original : pandas.DataFrame
            DataFrame original (con faltantes)
        df_procesado : pandas.DataFrame
            DataFrame procesado (con faltantes manejados)
        columna_original : str
            Nombre de la columna en el DataFrame original
        columna_procesada : str, opcional
            Nombre de la columna en el DataFrame procesado. 
            Si es None, usa el mismo nombre que columna_original
        bins : int, opcional
            Número de bins para el histograma (default=7)
            
        Returns
        -------
        None
            Muestra los histogramas comparativos
        """
        # Si no se especifica columna_procesada, usar la misma que la original
        if columna_procesada is None:
            columna_procesada = columna_original
        
        # Validar que las columnas existan
        if columna_original not in df_original.columns:
            raise ValueError(f"La columna '{columna_original}' no existe en el DataFrame original")
        if columna_procesada not in df_procesado.columns:
            raise ValueError(f"La columna '{columna_procesada}' no existe en el DataFrame procesado")
        
        # Crear figura con dos subplots
        fig, (ax1, ax2) = plt.subplots(figsize=(20, 5), nrows=1, ncols=2)
        
        # Título general
        fig.suptitle("Histogramas comparando las variables antes y después del manejo de faltantes", 
                     fontsize=16, fontweight='bold')
        
        # Histograma ANTES (con faltantes)
        ax1.set_title(f"Histograma de '{columna_original}' (Sin manejo de faltantes)", fontsize=12)
        ax1.set_xlabel(columna_original, fontsize=11)
        ax1.set_ylabel("Densidad", fontsize=11)
        sns.histplot(df_original[columna_original], bins=bins, kde=True, ax=ax1, 
                     edgecolor='black', color='red', stat='density')
        
        # Agregar información de faltantes
        n_faltantes_original = df_original[columna_original].isna().sum()
        total_original = len(df_original)
        pct_faltantes = (n_faltantes_original / total_original) * 100
        ax1.text(0.02, 0.98, f'Faltantes: {n_faltantes_original} ({pct_faltantes:.1f}%)', 
                 transform=ax1.transAxes, fontsize=10, verticalalignment='top',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Histograma DESPUÉS (sin faltantes)
        ax2.set_title(f"Histograma de '{columna_procesada}' (Con manejo de faltantes)", fontsize=12)
        ax2.set_xlabel(columna_procesada, fontsize=11)
        ax2.set_ylabel("Densidad", fontsize=11)
        sns.histplot(df_procesado[columna_procesada], bins=bins, kde=True, ax=ax2, 
                     edgecolor='black', color='green', stat='density')
        
        # Agregar información de faltantes
        n_faltantes_procesado = df_procesado[columna_procesada].isna().sum()
        total_procesado = len(df_procesado)
        pct_faltantes_proc = (n_faltantes_procesado / total_procesado) * 100
        ax2.text(0.02, 0.98, f'Faltantes: {n_faltantes_procesado} ({pct_faltantes_proc:.1f}%)', 
                 transform=ax2.transAxes, fontsize=10, verticalalignment='top',
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
        
        plt.tight_layout()
        plt.show()

    @staticmethod
    def ver_outliers (df_KNN):
        plt.figure(figsize=(22,6))
        df_KNN.boxplot(grid=True,fontsize=15)
        plt.legend(fontsize=16)
        plt.yticks(fontsize=16)
        plt.show()

    @staticmethod
    def ver_outliers_columna(df_KNN, columna):
        plt.figure(figsize=(6,6))
        df_KNN[[columna]].boxplot(fontsize=14)
        plt.show()