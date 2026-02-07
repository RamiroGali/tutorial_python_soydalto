# Curso Python 24 - soydalto
# Ejercicio Práctico 3

"""
Ejercicio Práctico 3

El profesor no llegó a clases y los alumnos se pusieron a armar su propia clase
Uno tomó el rol del profesor y otro alumno asumió el rol del asistente.
Ambos le pidieron a los estudiantes:
- Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
- El mayor es el profesor y el menor es el asistente.
"""


def get_ages(cant_alumnos):
    edades_alumnos = []
    for i in range(cant_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        edades_alumnos.append((nombre, edad))

    # Ordenar la lista de tuplas por edad (segundo elemento de la tupla)
    edades_alumnos.sort(key=lambda x: x[1])

    # El mayor es el profesor y el menor es el asistente
    profesor = edades_alumnos[-1]  # El último elemento es el mayor
    asistente = edades_alumnos[0]  # El primer elemento es el menor

    return edades_alumnos, profesor, asistente


edades_alumnos, profesor, asistente = get_ages(3)

print(f"El profesor es: {profesor[0]} y el asistente es: {asistente[0]}")

print("Edades de los alumnos ordenadas de menor a mayor:")
for nombre, edad in edades_alumnos:
    print(f"{nombre}: {edad} años")
