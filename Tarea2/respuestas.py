import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def punto2(df):
    # Esto va a responder el punto 2
    print(f"La cantidad de valores faltantes por columnas es de:\n{df.isnull().sum()}")
    print(f"La cantidad de valores faltantes es totales es de:\n{df.isnull().sum().sum()}")


# Seleccionar Columnas numericas en el dataframe
def cantidad_cnumericas(df):
    return df.select_dtypes(include="number").columns



