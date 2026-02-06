# Curso Python 11 - soydalto
# Ejercicio Práctico 1: Comparación de Duración de Cursos

"""
Ejercicio: El usuario puede ingresar la duración de varios cursos
y compararla con la duración del contenido visto hasta ahora en este curso.

Hasta el minuto 2:40 (160 minutos) del curso "Python desde Cero - soydalto",
se han cubierto los siguientes temas:

1. Tipos de datos simples (c_01)
2. Tipos de datos compuestos (c_02)
3. Operadores aritméticos (c_03)
4. Operadores de comparación (c_04)
5. Condicionales If-Else (c_05)
6. Operadores lógicos (c_06)
7. Métodos de cadenas (c_07)
8. Métodos de listas (c_08)
9. Métodos de diccionarios (c_09)
10. Función input() (c_10)

Total de contenido visto: 160 minutos (2 horas 40 minutos)
"""

print("=" * 60)
print("COMPARADOR DE DURACIÓN DE CURSOS")
print("=" * 60)

# Duración del contenido visto en este curso
duracion_soydalto = 160  # 2 horas 40 minutos en minutos

print(
    f"\nDuración del contenido visto en 'Python desde Cero - soydalto': {duracion_soydalto} minutos"
)
print(
    f"Esto equivale a: {duracion_soydalto // 60} horas y {duracion_soydalto % 60} minutos"
)

print("\n" + "-" * 60)
print("Ingresa la duración de otros cursos para compararlos")
print("-" * 60)

# Contador para almacenar múltiples cursos
cursos = {}
continuar = True

while continuar:
    nombre_curso = input("\nIngresa el nombre del curso (o 'salir' para terminar): ")

    if nombre_curso.lower() == "salir":
        continuar = False
        break

    try:
        # Capturar duración en minutos
        duracion_str = input(f"Ingresa la duración de '{nombre_curso}' en minutos: ")
        duracion_curso = int(duracion_str)

        # Validar que sea un número positivo
        if duracion_curso < 0:
            print("Por favor, ingresa un número positivo.")
            continue

        cursos[nombre_curso] = duracion_curso

    except ValueError:
        print("Error: Debes ingresar un número válido para la duración.")
        continue

# Mostrar la comparación
if len(cursos) > 0:
    print("\n" + "=" * 60)
    print("RESUMEN COMPARATIVO")
    print("=" * 60)

    print(f"\n{'Curso':<40} {'Duración':<15} {'Diferencia':<15}")
    print("-" * 70)
    print(
        f"{'Python desde Cero - soydalto':<40} {str(duracion_soydalto) + ' min':<15} {'(Referencia)':<15}"
    )
    print("-" * 70)

    for nombre, duracion in cursos.items():
        diferencia = duracion - duracion_soydalto

        if diferencia > 0:
            diferencia_texto = f"+{diferencia} min (más largo)"
        elif diferencia < 0:
            diferencia_texto = f"{diferencia} min (más corto)"
        else:
            diferencia_texto = "Igual duración"

        print(f"{nombre:<40} {str(duracion) + ' min':<15} {diferencia_texto:<15}")

    print("\n" + "=" * 60)
    print("ESTADÍSTICAS")
    print("=" * 60)

    duraciones = list(cursos.values())
    duracion_promedio = sum(duraciones) / len(duraciones)
    duracion_maxima = max(duraciones)
    duracion_minima = min(duraciones)

    print(f"Cantidad de cursos ingresados: {len(cursos)}")
    print(f"Duración promedio: {duracion_promedio:.2f} minutos")
    print(f"Curso más largo: {duracion_maxima} minutos")
    print(f"Curso más corto: {duracion_minima} minutos")

    # Cursos más largos o más cortos que este curso
    cursos_mas_largos = {k: v for k, v in cursos.items() if v > duracion_soydalto}
    cursos_mas_cortos = {k: v for k, v in cursos.items() if v < duracion_soydalto}

    if len(cursos_mas_largos) > 0:
        print(f"\nCursos MÁS LARGOS que '{duracion_soydalto} min':")
        for nombre, duracion in cursos_mas_largos.items():
            print(
                f"  - {nombre}: {duracion} minutos ({duracion - duracion_soydalto} min más)"
            )

    if len(cursos_mas_cortos) > 0:
        print(f"\nCursos MÁS CORTOS que '{duracion_soydalto} min':")
        for nombre, duracion in cursos_mas_cortos.items():
            print(
                f"  - {nombre}: {duracion} minutos ({duracion_soydalto - duracion} min menos)"
            )

    if len(cursos_mas_longos) == 0 and len(cursos_mas_cortos) == 0:
        print("\nTodos los cursos tienen la misma duración que el curso de referencia.")

else:
    print("\nNo se ingresaron cursos para comparar.")

print("\n" + "=" * 60)
print("¡Gracias por usar el comparador de cursos!")
print("=" * 60)
