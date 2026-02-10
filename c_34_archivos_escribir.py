# Ruta del archivo
ruta_archivo = "src\\texto.txt"
objeto = {"nombre": "Ram", "apellido": "GO"}
lineas = ["Primera línea\n", "Segunda línea\n", "Tercera línea\n"]


# Escribir sobre un archivo
# No es necesario cerrarlo cuando se usa with open
# - Sobreescribir el archivo con el modo de escritura "w"
with open(ruta_archivo, "w", encoding="UTF-8") as archivo:
    # archivo.write("sobre-escritura del archivo");
    # print("acceso de sobreescritura  al archivo con with open")

    # Inserción de línea:
    archivo.write("Esta será la primera línea\n")
    # Inserción de líneas
    archivo.writelines(
        ["Acceso al archivo para añadir líneas\n", "Nueva línea añadida\n"]
    )

    # Inserción de objetos
    archivo.write("{\n")
    archivo.writelines(f"  {k}: {v}\n" for k, v in objeto.items())
    archivo.write("}\n")

# Escritura segura con writelines

try:
    # Agregar nuevas líneas al archivo con el modo de escritura "a"
    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.writelines(lineas)
    print("Archivo escrito correctamente.")
except OSError as e:
    print(f"Error al escribir el archivo: {e}")


# Lectura de un archivo
# No es necesario cerrar el acceso al archivo que se está leyendo cuando se usa with open
with open(ruta_archivo, encoding="UTF-8") as archivo:
    print("acceso al archivo con with open")
    contenido_archivo = archivo.readlines()

    print(contenido_archivo)


# Consideraciones:
# - No agrega saltos de línea, solo las separa, toca añadir \n al final de cada línea.
# - Requiere de un iterable para añadir objetos
# - Depende del modo de apertura en el with open que se aplica al archivo
# 	- "w": sobrescribe el archivo.
# 	- "a": agrega al final.
# 	- "x": crea un archivo nuevo y falla si ya existe.
# 	- "wb" o "ab": para binarios (requiere bytes en lugar de str).
# - No es ideal para archivos muy grandes:
# 	- Si la lista de cadenas es enorme, puede consumir mucha memoria
# 	- En esos casos, es mejor escribir línea por línea con write en un bucle.
