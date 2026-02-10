import pandas as pd

df = pd.read_csv("src\\csv_doc.csv")

# Generar una nueva columna con los datos de la edad convertidos en string
df["edad"] = df["Edad"].astype(str)
print(df["edad"][0])

# Deprecado
print(df["Nombre"].replace("Pedro", "maestro Pedro", inplace=True))

# Eliminar datos con columnas faltantes
df_2 = df.dropna()
print(df_2)

# Eliminar filas repetidas
df_3 = df_2.drop_duplicates()
print(df_3)

# Crear un nuevo CSV con el dataframe resultante (limpio)
df_3.to_csv("src/csv_result.csv")
