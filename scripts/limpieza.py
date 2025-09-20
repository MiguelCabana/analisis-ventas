import pandas as pd

def limpiar(df):
    # Quitar valores nulos
    df = df.dropna()
    # Quitar duplicados
    df = df.drop_duplicates()
    return df
