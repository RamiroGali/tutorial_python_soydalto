# Curso Python 15 - soydalto
# Diccionarios (dict) y métodos de diccionarios

# El diccionario (dict) es una colección de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
# Se pueden crear diccionarios utilizando llaves {} o la función dict().

my_diccionario1 = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

my_diccionario2 = dict(clave1="valor1", clave2="valor2", clave3="valor3")

my_diccionario3 = dict(
    [("clave1", "valor1"), ("clave2", "valor2"), ("clave3", "valor3")]
)

# La función zip() permite crear un diccionario a partir de dos listas: una lista de claves y una lista de valores. Cada elemento de la primera lista se empareja con el elemento correspondiente de la segunda lista para formar los pares clave-valor del diccionario.
my_diccionario4 = dict(
    zip(["clave1", "clave2", "clave3"], ["valor1", "valor2", "valor3"])
)

# La función fromkeys() permite crear un diccionario a partir de una lista de claves, asignando a cada clave un valor por defecto especificado.
my_diccionario5 = dict.fromkeys(["clave1", "clave2", "clave3"], "valor_por_defecto")

# Las claves de un diccionario pueden ser de cualquier tipo inmutable (hashable), como números, cadenas, tuplas, etc. Sin embargo, no pueden ser listas, conjuntos u otros diccionarios, ya que estos son mutables y no hashables.
# Las tuplas son inmutables y hashables, por lo que pueden ser utilizadas como claves en un diccionario. Por ejemplo:
my_diccionario6 = {
    ("clave1", "subclave1"): "valor1",
    ("clave2", "subclave2"): "valor2",
    ("clave3", "subclave3"): "valor3",
}

print(my_diccionario6)

# Si se utiliza el frozenset sobre un 'list', se puede usar una representación de esa 'list' como clave en un diccionario
# El frozenset es una versión inmutable de un conjunto (set) en Python. Al convertir una lista a un frozenset
# se obtiene un objeto que es hashable y puede ser utilizado como clave en un diccionario. Por ejemplo:
my_diccionario7 = {
    frozenset(["clave1", "subclave1"]): "valor1",
    frozenset(["clave2", "subclave2"]): "valor2",
    frozenset(["clave3", "subclave3"]): "valor3",
}

print(my_diccionario7)
