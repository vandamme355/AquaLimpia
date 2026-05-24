import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_excel("dataset_set_A_aguas_residuales.xlsx")

# Exploración
print(df.head())
print(df.info())

# Limpieza (aunque no tienes nulos, lo dejamos correcto)
df["DBO_entrada_mg_L"] = df["DBO_entrada_mg_L"].fillna(df["DBO_entrada_mg_L"].mean())
df["DBO_salida_mg_L"] = df["DBO_salida_mg_L"].fillna(df["DBO_salida_mg_L"].mean())

# Cálculo de eficiencia (IMPORTANTE)
df["eficiencia"] = (
    (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"]) / df["DBO_entrada_mg_L"]
) * 100

# Agrupar por planta
resumen = df.groupby("planta")[["eficiencia", "DBO_salida_mg_L"]].mean()

# Gráficos
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.bar(resumen.index, resumen["eficiencia"])
plt.title("Eficiencia promedio por planta")

plt.subplot(1,2,2)
plt.bar(resumen.index, resumen["DBO_salida_mg_L"])
plt.title("DBO salida promedio por planta")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()