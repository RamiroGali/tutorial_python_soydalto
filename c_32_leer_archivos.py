archivo = open("src\\texto.txt", encoding="UTF-8")

# Leer archivo completo
texto_archivo = archivo.read()
print(texto_archivo)

# Se debe cerrar el archivo antes de desarrollar una nueva lectura del mismo
archivo.close()
# Se vuelve a abrir el acceso al archivo
archivo = open("src\\texto.txt", encoding="UTF-8")
print("--" * 30)

# Leer linea 1
linea1 = archivo.readline()
print(linea1)

# Leer linea 2
linea2 = archivo.readline()
print(linea2)

# Se debe cerrar el archivo antes de desarrollar una nueva lectura del mismo
archivo.close()
# Se vuelve a abrir el acceso al archivo
archivo = open("src\\texto.txt", encoding="UTF-8")
print("--" * 30)

# Leer lineas separadas en una lista
lineas = archivo.readlines()
print(lineas)

# Se debe cerrar el archivo antes de desarrollar una nueva lectura del mismo
archivo.close()
# Se vuelve a abrir el acceso al archivo
archivo = open("src\\texto.txt", encoding="UTF-8")
print("--" * 30)

# Leer lineas separadas en una lista
lineas = archivo.readline(10)
print(lineas)

# Se debe cerrar el archivo antes de desarrollar una nueva lectura del mismo
archivo.close()
# Leer linea con un límite de caracteres
