# Curso Python 18 - soydalto
# Recorrer diccionarios en Python

# Los diccionarios son colecciones de pares clave:valor.
# Para recorrerlos hay varias opciones: claves, valores, o ambos (items).

mi_dict = {
    "nombre": "Ana",
    "edad": 28,
    "curso": "Python",
    "temas": ["listas", "diccionarios", "conjuntos"],
}

print("=== Recorrer claves ===")
for clave in mi_dict:
    print(clave)

print("\n=== Recorrer valores ===")
for valor in mi_dict.values():
    print(valor)

# Recorrer claves y valores juntos
print("\n=== Recorrer claves y valores (items) ===")
for clave, valor in mi_dict.items():
    print(f"{clave}: {valor}")

print("\n=== Acceso seguro con get() ===")
print("País (con get):", mi_dict.get("pais", "No especificado"))

print("\n=== Iterar sobre claves ordenadas ===")
for clave in sorted(mi_dict.keys()):
    print(clave, mi_dict[clave])

print("\n=== Recorrer diccionario anidado ===")
mi_dict_anidado = {
    "curso": "Python",
    "profesor": {"nombre": "Luis", "edad": 35},
    "duracion": 120,
}
for clave, valor in mi_dict_anidado.items():
    print(f"{clave}: {valor}")
    if isinstance(valor, dict):
        print("  -- Detalle del diccionario anidado:")
        for k, v in valor.items():
            print(f"    {k}: {v}")


# For if continue para evitar una clave específica
print("\n=== Recorrer con continue para evitar una clave específica ===")
for clave, valor in mi_dict.items():
    if clave == "edad":
        continue  # Saltar la clave "edad"
    print(f"{clave}: {valor}")

# For if break para detener el recorrido al encontrar una clave específica
print("\n=== Recorrer con break para detener al encontrar una clave específica ===")
for clave, valor in mi_dict.items():
    print(f"{clave}: {valor}")
    if clave == "curso":
        break  # Detener el recorrido al encontrar la clave "curso"
else:
    print("Recorrido completo sin encontrar la clave 'curso'")


print("\nConsideraciones finales:")
print("- Usa .keys(), .values(), .items() según lo que necesites recorrer")
print("- Para acceso seguro usa .get() con valor por defecto")
print("- Si necesitas orden, itera sobre sorted(dict.keys())")
print("- Puedes usar continue o break para controlar el flujo del recorrido")
