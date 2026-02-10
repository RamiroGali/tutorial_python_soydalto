import pandas as pd

ruta_csv = "src\\csv_doc.csv"

# Los data Frame son estructuras de datos bidimensionales, equivalentes a hojas de cálculo que se acceden a través de filas y columnas.
df = pd.read_csv(ruta_csv)
df2 = pd.read_csv(ruta_csv)
print(df, "\n")

# Si en el csv no se encuentran definidos los encabezados como la primera fila
# se pueden generar nuevos encabezados al momento de su lectura, y la primera fila en el csv se consideraría no como un encabezado
# sino que la primera fila del archivo csv se considerará como el primer registro de datos de la base de datos.
# df = pd.read_csv(ruta_csv, names=["dato1", "dato2", "dato3"])
# print(df, "\n")

# Acceder a la columna "Edad" de datos
print(df["Edad"], "\n")

# Ordenar los datos por la columna edad en orden ascendente
# El ordenamiento ascendente es el configurado por defecto por las funciones sort
df_orden_ascendente = df.sort_values("Edad")
print(df_orden_ascendente, "\n")

df_orden_descendente = df.sort_values("Edad", ascending=False)
print(df_orden_descendente, "\n")

# concatenar 2 data Frame
df_concatenado = pd.concat([df, df2])
print(df_concatenado, "\n")

# Accediendo a las primeras 5 filas de datos con head()
primeras_filas = df.head(5)
print(primeras_filas, "\n")

# Accediendo a las últimas 5 filas de datos con tail()
ultimas_filas = df.tail(5)
print(ultimas_filas, "\n")

# Accediento a la cantidad de filas y columnas con shape
cant_filas_df, cant_columnas_df = df.shape
print(
    f"cantidad de filas: {cant_filas_df}; cantidad de columnas: {cant_columnas_df}",
    "\n",
)

# Obtener información estadística básica de la base de datos
info_df = df.describe()
print(info_df, "\n")

# Accediendo a un elemento de dato con loc
elemento_especifico_loc = df.loc[2, "Edad"]
print(elemento_especifico_loc, "\n")

# Accediendo a un elemento de dato con iloc
# El parámetro Edad corresponde con el parametro 3
elemento_especifico_iloc = df.iloc[2, 3]
print(elemento_especifico_iloc, "\n")

# Accediendo a todos los datos de la columnas que corresponde con el segundo index
departamentos = df.iloc[:, 2]
print(departamentos, "\n")

# Generar una "boolean mask"
# Genera una lista con valores Booleanos que correspondan con las filas de la base de datos que se pretende filtrar
boolean_mask = df["Edad"] > 30
print(boolean_mask, "\n")

# Accediendo a los datos que correspondan con el parametro Edad mayor que 30, haciendo uso de un boolean_mask
mayor_30 = df.loc[boolean_mask, :]
print(mayor_30, "\n")
