import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



class Graficos:
#Elaboro el constructor de la clase que se encarga de almacenar la informacion

    def __init__(self, df1=None, df2=None):  
        self.df1 = df1
        self.df2 = df2


@staticmethod
def crear_histograma_columna(df_sin_na, df2, age):
    fig, (ax1, ax2) = plt.subplots(figsize=(20,5), nrows=1, ncols=2)

    fig.suptitle("Histogramas comparando las variables antes y despues del manejo de faltantes")
    ax1.set_title(f"Histograma de la {age} (Sin manejo de faltantes)")
    ax1.set_xlabel(age)
    ax1.set_ylabel("Densidad de Estudiantes")
    sns.histplot(df2[age], bins=7, kde=True, ax=ax1, edgecolor='black', color='red', stat='density')

    ax2.set_title(f"Histograma de la {age} (Con manejo de faltantes)")
    ax2.set_xlabel(age)
    ax2.set_ylabel("Densidad de Estudiantes")
    sns.histplot(df_sin_na[age], bins=7, kde=True, ax=ax2, edgecolor='black', color='green', stat='density')
    plt.show()   