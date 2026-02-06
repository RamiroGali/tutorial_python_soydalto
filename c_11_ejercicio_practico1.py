# Curso Python 11 - soydalto
# Ejercicio Práctico 1: Comparación de Duración de Cursos

"""
Ejercicio: comparar la duración del contenido visto hasta ahora en este curso con otros cursos equivalentes.
Total de contenido visto: 90 minutos (1 horas 30 minutos)
"""

print("=" * 50)
print("COMPARADOR DE DURACIÓN DE CURSOS")
print("=" * 50)

# Duración del contenido visto en este curso
t_curso_soydalto = 1.5
# Duración del contenido visto en otros cursos
t_min_cursos_otros = 2.5
t_max_cursos_otros = 7
t_prom_cursos_otros = 4

# Duracion de cursos
crudo_promedio = 5
crudo_soydalto = 3.5

# Diferencia de duración
diferencia_con_min = 100 - ((t_curso_soydalto / t_min_cursos_otros) * 100)
print("El curso de Dalto dura:")
print(f"- un {diferencia_con_min:.2f}% menos que el curso más rápido")
diferencia_con_max = 100 - ((t_curso_soydalto * 100 / t_max_cursos_otros * 100) / 100)
print(f"- un {diferencia_con_max:.2f}% menos que el curso más lento")
diferencia_con_prom = 100 - ((t_curso_soydalto / t_prom_cursos_otros) * 100)
print(f"- un {diferencia_con_prom:.2f}% menos que el curso promedio")
print("-" * 50)

tiempo_vacio_prom = 100 - t_prom_cursos_otros * 1000 // crudo_promedio / 10
print(
    f"Un curso promedio elimina el {tiempo_vacio_prom:.2f}% del tiempo vacío de un curso promedio"
)

tiempo_vacio_soydalto = 100 - t_curso_soydalto * 1000 // crudo_soydalto / 10
print(
    f"El curso de soydalto elimina el {tiempo_vacio_soydalto:.2f}% del tiempo vacío de un curso promedio"
)
print("-" * 50)
print(
    f"Ver 10 horas de este curso equivale a ver {t_prom_cursos_otros*100//t_curso_soydalto / 10:.2f} horas de un curso promedio"
)

print(
    f"Ver 10 horas de otros cursos equivale a ver {t_curso_soydalto*100//t_prom_cursos_otros / 10:.2f} horas de este curso"
)
