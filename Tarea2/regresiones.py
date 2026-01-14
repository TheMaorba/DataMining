import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Inferencia:

    @staticmethod
    def correlation_heatmap(data, figsize=(20,10), vmin=-1, vmax=1, cmap='BrBG', title='Mapa de calor de correlación triangular', fontsize=18):
        plt.figure(figsize=figsize)
        numeric_data = data.select_dtypes(include=[np.number])
        mask = np.triu(np.ones_like(numeric_data.corr(), dtype=bool))  # ← Cambio aquí
        heatmap = sns.heatmap(numeric_data.corr(), mask=mask, vmin=vmin, vmax=vmax, annot=True, cmap=cmap)
        heatmap.set_title(title, fontdict={'fontsize':fontsize}, pad=16)
        plt.show()