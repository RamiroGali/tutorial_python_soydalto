# Curso Python 13 - soydalto
# Desempaquetado de variables (unpacking)

# El desempaquetado de variables (unpacking) es una técnica que permite asignar valores de una colección (como una lista, tupla o conjunto) a variables individuales de manera más concisa y legible.
# Ejemplo con una lista
list_variables = [1, 2, 3]
tuplas_variables = (1, 2, 3)

a_list, b_list, c_list = list_variables  # Desempaquetado de la lista
print(f"a: {a_list}, b: {b_list}, c: {c_list}")

a_tuple, b_tuple, c_tuple = tuplas_variables  # Desempaquetado de la tupla
print(f"a: {a_tuple}, b: {b_tuple}, c: {c_tuple}")


# Ejemplo con el comando tuple() para convertir una list en tupla
my_list = ["dato1", "dato2", "dato3"]
my_tupla = tuple(my_list)

print(type(my_tupla))
