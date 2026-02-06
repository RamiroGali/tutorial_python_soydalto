# Curso Python 8 - soydalto
# Métodos de Listas

# LEN, APPEND, INSERT, EXTEND, POP, REMOVE, CLEAR, COUNT, INDEX, SORT, REVERSE
# Definición de una lista de números
numeros = [5, 2, 9, 1, 5, 6]
print("Lista original:", numeros)
# Método len() - Devuelve la cantidad de elementos en la lista
longitud_numeros = len(numeros)
print("Longitud de la lista:", longitud_numeros)
# Método append() - Agrega un elemento al final de la lista
numeros.append(3)
print("Después de append(3):", numeros)
# Método insert() - Inserta un elemento en una posición específica
numeros.insert(2, 7)
print("Después de insert(2, 7):", numeros)
# Método extend() - Agrega los elementos de otra lista al final de la lista actual
numeros.extend([8, 4])
print("Después de extend([8, 4]):", numeros)
# Método pop() - Elimina y devuelve el elemento en la posición especificada
elemento_eliminado = numeros.pop(3)
print("Después de pop(3):", numeros)
print("Elemento eliminado con pop(3):", elemento_eliminado)
# Método remove() - Elimina la primera aparición de un valor específico
numeros.remove(5)
print("Después de remove(5):", numeros)
# Método clear() - Elimina todos los elementos de la lista
numeros.clear()
print("Después de clear():", numeros)
# Definición de una lista de frutas
frutas = ["manzana", "banana", "cereza", "manzana", "naranja"]
print("\nLista de frutas:", frutas)
# Método count() - Cuenta cuántas veces aparece un elemento en la lista
conteo_manzana = frutas.count("manzana")
print("Número de veces que aparece 'manzana':", conteo_manzana)
# Método index() - Devuelve la posición de la primera aparición de un elemento
posicion_cereza = frutas.index("cereza")
print("Posición de 'cereza':", posicion_cereza)
# Método sort() - Ordena los elementos de la lista
frutas.sort()
print("Lista de frutas ordenada:", frutas)
# Método sort(reverse=True) - Ordena los elementos de la lista en orden inverso
frutas.sort(reverse=True)
print("Lista de frutas ordenada en orden inverso:", frutas)
# Método reverse() - Invierte el orden de los elementos en la lista
frutas.reverse()
print("Lista de frutas invertida pero sin ordenar:", frutas)
