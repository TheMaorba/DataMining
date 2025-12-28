def punto2(df):
    # Esto va a responder el punto 2
    print(f"La cantidad de valores faltantes por columnas es de:\n{df.isnull().sum()}")
    print(f"La cantidad de valores faltantes es totales es de:\n{df.isnull().sum().sum()}")



    # Esto me va ayudar a responder el punto 3 de la actividad donde tengo que llenar los datos faltantes
