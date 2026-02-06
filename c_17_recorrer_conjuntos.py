# Curso Python 17 - soydalto
# Recorrer conjuntos (sets) en Python

# Características breves de los conjuntos (set):
# - Colecciones no ordenadas de elementos únicos
# - No mantienen un orden fijo, por lo que no se puede acceder por índice
# - Son iterables, por lo que se pueden recorrer con un bucle for

print("=== Ejemplos de recorrido de conjuntos ===")

conjunto = {
    "manzana",
    "banana",
    "cereza",
    "manzana",
}  # El duplicado "manzana" se ignora
print("Conjunto inicial:", conjunto)

# 1) Recorrer con for
print("\nRecorrer con for:")
for elemento in conjunto:
    print("Elemento:", elemento)

# 2) Usar enumerate (convertir a lista para tener índices)
print("\nRecorrer con índices (convertido a lista):")
conjunto_lista = list(conjunto)
for indice, elemento in enumerate(conjunto_lista):
    print(f"Índice: {indice}, Elemento: {elemento}")

# 3) Iterar y aplicar una transformación (p. ej. mayúsculas)
print("\nTransformar cada elemento a mayúsculas mientras se recorre:")
for e in conjunto:
    print(e.upper())

# 4) Comprobar y recorrer elementos que cumplen una condición
print("\nElementos que contienen la letra 'a':")
for e in conjunto:
    if "a" in e:
        print(e)

# 5) Recorrer frozenset (inmutable)
print("\nRecorrer un frozenset:")
fs = frozenset([1, 2, 3, 4])
for n in fs:
    print(n)

# 6) Convertir a lista si se necesita un orden o posiciones específicas
print("\nOrdenar y recorrer (si necesitas orden):")
for e in sorted(conjunto):
    print(e)

print("\nConsideraciones finales:")
print(
    "- Los sets no garantizan orden; si necesitas índices o orden, convierte a lista o usa sorted()"
)
print(
    "- Recorrer conjuntos es eficiente para operaciones de pertenencia y eliminación de duplicados"
)
