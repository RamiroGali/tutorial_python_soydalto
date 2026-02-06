# Curso Python 2 - soydalto
# Tipos de datos compuestos en Python
# Definición de variables con tipos de datos compuestos
# - Listas: Colecciones ordenadas y mutables de elementos, definidas con corchetes []
# - Tuplas: Colecciones ordenadas e inmutables de elementos, definidas con paréntesis ()
# - Diccionarios: Colecciones de pares clave-valor, definidas con llaves {}
# - Conjuntos: Colecciones no ordenadas de elementos únicos, definidas con llaves {}


my_list = [1, 2, 3, "cuatro", True]; # Lista con diferentes tipos de datos
print("Lista:", my_list);

# Las listas se encuentran indexadas, lo que significa que cada elemento tiene una posición numérica que funciona a modo de key para acceder a dicho elemento.
print("Primer elemento de la lista:", my_list[0]); # Acceder al primer elemento
print("Último elemento de la lista:", my_list[-1]); # Acceder al último elemento
# Las listas son mutables, lo que significa que se pueden modificar después de su creación.
my_list[0] = 10; # Modificar el primer elemento
print("Lista modificada:", my_list);

# Las listas se pueden recorrer, haciendo uso de las keys/indexes de cada elemento.
for index in range(len(my_list)):
	print(f"Elemento en el índice {index}:", my_list[index]); 

# Operaciones con tipos de datos compuestos de tipo lista
my_list.append("nuevo elemento"); # Agregar un nuevo elemento al final de la lista
print("Lista después de append:", my_list);
my_list.remove(2); # Eliminar el elemento con valor 2 de la lista
print("Lista después de remove:", my_list);
my_list.pop(1); # Eliminar el elemento en el índice 1 de la lista
print("Lista después de pop:", my_list);
my_list.sort(key=str); # Ordenar la lista (los elementos se convierten a string para evitar errores al comparar diferentes tipos de datos)
print("Lista después de sort:", my_list);
my_list.reverse(); # Invertir el orden de los elementos en la lista
print("Lista después de reverse:", my_list);

# Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. Se definen con paréntesis ().
my_tuple1 = (1, 2, 3, "cuatro", True); # Tupla con diferentes tipos de datos
print("Tupla1:", my_tuple1);

# Las tuplas también se pueden crear sin paréntesis, simplemente separando los elementos con comas. Sin embargo, es recomendable usar paréntesis para mejorar la legibilidad.
my_tuple2 = 1, 2, 3, "cuatro", True; # Tupla creada sin paréntesis, aunque es recomendable usar paréntesis para mejorar la legibilidad

# No se puede hacer con una tupla:
# my_tuple1[0] = 10; # Esto generará un error porque las tuplas son inmutables
print("Tupla2:", my_tuple2);

# Los diccionarios son colecciones de pares clave-valor, donde cada clave es única. Se definen con llaves {}.
# - Se les llama mapas o tablas hash. Las claves pueden ser de cualquier tipo inmutable, como strings, números o tuplas.
# - Se les llama JSON en otros contextos, aunque JSON es un formato de intercambio de datos que se basa en la sintaxis de los diccionarios de Python.
my_dict1 = {"clave1": "valor1", "clave2": 2, "clave3": [1, 2, 3]}; # Diccionario con diferentes tipos de datos
print("Diccionario:", my_dict1);

# También se pueden crear diccionarios usando la función dict() con una lista de tuplas, donde cada tupla representa un par clave-valor.
my_dict2 = dict([("clave1", "valor1"), ("clave2", 2), ("clave3", [1, 2, 3])]); # Diccionario creado con la función dict()
print("Diccionario:", my_dict2);

# Los conjuntos son colecciones no ordenadas de elementos únicos. Se definen con llaves {}, pero a diferencia de los diccionarios, no tienen pares clave-valor.
my_set = {1, 2, 3, "cuatro", True}; # Conjunto con diferentes tipos de datos
print("Conjunto:", my_set);

# No se puede hacer con un conjunto:
# my_set.add(1); # Esto no hará nada porque el elemento 1 ya está en el conjunto, ya que los conjuntos no permiten elementos duplicados
# my_set[1] = "10"; # Esto generará un error porque los conjuntos no son indexados, es decir, no se pueden acceder a sus elementos mediante índices como en las listas o tuplas

# Operaciones con tipos de datos compuestos de tipo conjunto/set
my_set = my_set.union({5, 6}); # Esto agregará los elementos 5 y 6 al conjunto, ya que la operación de unión combina los elementos de ambos conjuntos sin duplicados
print("Conjunto:", my_set);

my_set = my_set.difference({1, 2}); # Esto eliminará los elementos 1 y 2 del conjunto, ya que la operación de diferencia devuelve un nuevo conjunto con los elementos que están en el primer conjunto pero no en el segundo
print("Conjunto:", my_set);

# los conjuntos se pueden sobreescribir con la función set() para crear un nuevo conjunto a partir de una lista, tupla o cualquier iterable, eliminando los elementos duplicados y manteniendo solo los elementos únicos.
my_set = set([1, 2, 2, 3, 4, 4, 5]); # Esto creará un nuevo conjunto con los elementos únicos de la lista, eliminando los duplicados
print("Conjunto:", my_set);