# Curso Python 19 - soydalto
# Métodos de listas en Python

# Los métodos de listas son funciones que se pueden aplicar a objetos de tipo lista para manipular sus elementos.
# Algunos métodos comunes de listas incluyen:
# - append(): Agrega un elemento al final de la lista.
# - insert(): Inserta un elemento en una posición específica.
# - remove(): Elimina la primera ocurrencia de un elemento específico.

numeros = [1, 2, 3, 4, 5]
print("Lista original:", numeros)

# Usando append() para agregar un elemento al final de la lista
numeros.append(6)
print("Después de append(6):", numeros)
# Usando insert() para insertar un elemento en una posición específica
numeros.insert(2, 10)  # Inserta el número 10 en la
# posición 2 (índice 2)
print("Después de insert(2, 10):", numeros)

# Usando remove() para eliminar la primera ocurrencia de un elemento específico
numeros.remove(3)  # Elimina el número 3 de la lista
print("Después de remove(3):", numeros)

# Usando ciclo for para crear una nueva lista con elementos transformados
numeros_duplicados1 = list()
for numero in numeros:
    numeros_duplicados1.append(numero * 2)
print("Lista con duplicados con for:", numeros_duplicados1)

# Usando ciclo while para crear una nueva lista con elementos transformados
numeros_duplicados2 = list()
i = 0
while i < len(numeros):
    numeros_duplicados2.append(numeros[i] * 2)
    i += 1
print("Lista con duplicados con while:", numeros_duplicados2)

# Usando list comprehension para crear una nueva lista con elementos transformados
numeros_duplicados3 = [numero * 2 for numero in numeros]
print("Lista con duplicados con list comprehension:", numeros_duplicados3)

# Consideraciones importantes:
# 1. Los métodos de listas modifican la lista original (mutabilidad).
# 2. Algunos métodos como append() y insert() agregan elementos, mientras que otros como remove() eliminan elementos.
# 3. Es importante entender la diferencia entre métodos que modifican la lista y funciones que retornan una nueva lista (como sorted()).
