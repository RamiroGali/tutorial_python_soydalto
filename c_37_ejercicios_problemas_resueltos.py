# Tenemos 2 listas con nombres y apellidos
# Escribir los datos en un archivo de texto txt de forma óptima con un for


nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Dalto", "Robertix", "Zarado"]

# Registrar información de forma óptima con with open en un archivo txt
with open("src/nombres y apellidos.txt", "w") as archivo:
    archivo.writelines("Datos presentes:\n----------\n")

    # Ejecutar el recorrer los elementos de ambas listas, haciendo uso de "list comprehension"
    [
        archivo.writelines(f"Nombre: {n}\nApellido:{a}\n----------\n")
        for n, a in zip(nombres, apellidos)
    ]
