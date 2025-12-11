
# Importar librerías comunes
import pandas as pd

class Importacion:
    def importacion(self):
        return pd.read_csv("student-mat.csv",
                        sep=";",
                        header=None,
                        engine="python")

    def importacion2(self):
        return pd.read_csv("student-por.csv",
                        sep=";",
                        header=None,
                        engine="python")


