# Curso Python 14 - soydalto
# Conjuntos (sets) y teoría de conjuntos

my_list = ["Dato1", "Dato2", "Dato3"]
my_conjunto = set(my_list)

# El conjunto (set) es una colección de elementos únicos y no ordenados. A diferencia de las listas y tuplas, los conjuntos no permiten elementos duplicados y no mantienen un orden específico.
# Se pueden crear conjuntos a partir de listas, tuplas u otras colecciones utilizando la función

# Lo que no se puede hacer:
# Esto generará un error porque las listas no son hashables y no pueden ser elementos de un conjunto. Los conjuntos solo pueden contener elementos inmutables (hashables) como números, cadenas, tuplas, etc.
# my_conjunto = set(["Dato1", ["Subdato1", "Subdato2"], "Dato3"]]);

# Sin embargo, sí se pueden incluir tuplas dentro de un conjunto, ya que las tuplas son inmutables y hashables. Por ejemplo:
my_conjunto = set(["Dato1", tuple(["Subdato1", "Subdato2"]), "Dato3"])

# Esto generará un error porque los conjuntos no pueden contener otros conjuntos como elementos, ya que los conjuntos son mutables y no hashables.
# my_conjunto = set(["Dato1", {"Subdato1", "Subdato2"}, "Dato3"]);

# Esto generará un error porque los conjuntos no pueden contener otros conjuntos como elementos, ya que los conjuntos son mutables y no hashables.
# conjunto1 = {"Elemento1", "Elemento2", "Elemento3"}
# conjunto2 = {conjunto1, "Elemento4", "Elemento5"}
# print(conjunto2);


# Sin embargo, sí se pueden incluir frozensets dentro de un conjunto, ya que los frozensets son inmutables y hashables. Por ejemplo:
conjunto1 = frozenset({"Elemento1", "Elemento2", "Elemento3"})
conjunto2 = frozenset(["Elemento4", "Elemento5", "Elemento6"])
conjunto3 = {conjunto1, conjunto2, "Elemento7", "Elemento8"}
print(conjunto3)


# Teoría de conjuntos, usando métodos y operadores de conjuntos
conjunto_a = {1, 3, 5, 7}
conjunto_b = {1, 3, 7}

# Verifica si conjunto_b es subconjunto de conjunto_a
b_es_subconjunto_de_a = conjunto_b.issubset(conjunto_a)
# b_es_subconjunto_de_a = conjunto_b <= conjunto_a
print(f"¿conjunto_b ⊆ conjunto_a? {b_es_subconjunto_de_a}")

# Verifica si conjunto_a es subconjunto de conjunto_b
a_es_subconjunto_de_b = conjunto_a.issubset(conjunto_b)
# a_es_subconjunto_de_b = conjunto_a <= conjunto_b
print(f"¿conjunto_a ⊆ conjunto_b? {a_es_subconjunto_de_b}")

# Verifica si conjunto_a es un superconjunto de conjunto_b
a_es_superconjunto_de_b = conjunto_a.issuperset(conjunto_b)
# a_es_superconjunto_de_b = conjunto_a >= conjunto_b
print(f"¿conjunto_a ⊇ conjunto_b? {a_es_superconjunto_de_b}")

# Verifica si conjunto_b es un superconjunto de conjunto_a
b_es_superconjunto_de_a = conjunto_b.issuperset(conjunto_a)
# b_es_superconjunto_de_a = conjunto_b >= conjunto_a
print(f"¿conjunto_b ⊇ conjunto_a? {b_es_superconjunto_de_a}")

# Verificar si hay elementos comunes entre conjunto_a y conjunto_b
hay_elementos_comunes = not conjunto_a.isdisjoint(conjunto_b)
# hay_elementos_comunes = bool(conjunto_a & conjunto_b)
print(f"¿conjunto_a y conjunto_b tienen elementos comunes? {hay_elementos_comunes}")
