# No es necesario cerrarlo cuando se usa with open
with open("src\\texto.txt", encoding="UTF-8") as archivo:
    print("acceso al archivo con with open")
    contenido_archivo = archivo.readlines()

    print(contenido_archivo)
