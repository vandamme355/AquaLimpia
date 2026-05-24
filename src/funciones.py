import pandas as pd

def cargar_datos(ruta):
    return pd.read_excel(ruta)

def calcular_eficiencia(df):
    df["eficiencia"] = (
        (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"]) / df["DBO_entrada_mg_L"]
    ) * 100
    return df

def agrupar_por_planta(df):
    return df.groupby("planta")[["eficiencia", "DBO_salida_mg_L"]].mean()
