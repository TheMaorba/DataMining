import numpy as np
import matplotlib as plt
import seaborn as sns


class Graficos:
#Elaboro el constructor de la clase que se encarga de almacenar la informacion

    def __init__(self, df1=None, df2=None):  
        self.df1 = df1
        self.df2 = df2



    def crear_histograma_columna(df, df_conna, columna): 
        plt.figure(figsize=(8,5)) 
        sns.histplot(df[columna], bins=30, kde=True, stat="density", label="Original") 
        sns.histplot(df_conna[columna], bins=30, kde=True, stat="density", label="Con NA") 
        plt.title(f"Distribución de {columna}") 
        plt.legend() 
        plt.show()