
# Importar librerías comunes
import pandas as pd

class Importacion:
    def importacion(self):
        return pd.read_csv(r"student-mat.csv")

    def importacion2(self):
        return pd.read_csv(r"student-por.csv")


