import matplotlib.pyplot as plt
from funciones import cargar_datos, calcular_eficiencia, agrupar_por_planta

# Cargar datos
df = cargar_datos("dataset_set_A_aguas_residuales.xlsx")

# Aplicar funciones
df = calcular_eficiencia(df)
resumen = agrupar_por_planta(df)

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