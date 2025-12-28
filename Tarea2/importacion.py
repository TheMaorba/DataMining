import pandas as pd

class ImportarDatos:  
    # Defino el constructor de la clase que se encargara de almacenar los dataframe introducidos en el link
    def __init__(self, df1=None, df2=None):  
        self.df1 = df1
        self.df2 = df2

    # Defino el metodo de la clase que se encargara de importar las bases de datos mediante diccionario dinamico
    def importar_csv(self, df_rutas):
        for nombre, ruta in df_rutas.items():
            df = pd.read_csv(ruta, sep=';', encoding='latin1')
            setattr(self, f"df_{nombre}", df) 
    
    




   