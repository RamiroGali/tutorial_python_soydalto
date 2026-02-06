# Curso Python 22 - soydalto
# Funciones en Python


# En esta clase se profundiza en el uso de funciones, incluyendo parámetros con valores por defecto, argumentos nombrados, y consideraciones importantes para su uso efectivo.
def frase(nombre, apellido, adjetivo="capo"):
    return f"{nombre} {apellido} es {adjetivo}"


# Llamada a la función con argumentos nombrados y valor por defecto
print(frase(nombre="Ramiro", apellido="Galindo"))
print(frase(adjetivo="genial", nombre="Ramiro", apellido="Galindo"))
