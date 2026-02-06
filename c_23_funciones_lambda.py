# Curso Python 23 - soydalto
# Funciones lambda en Python

# Las funciones lambda son funciones anónimas, es decir, funciones sin nombre:
# - Se definen utilizando la palabra clave lambda.
# - Son útiles para crear funciones pequeñas y de una sola línea de código.
# - No se pueden usar para funciones complejas o que requieran múltiples líneas de código, pero son ideales para operaciones simples como cálculos rápidos o funciones de orden superior (como map, filter, reduce).
# - Solo se pueden usar para funciones que retornan un valor, no para funciones que realizan acciones sin retornar nada (como imprimir en pantalla).
# - Solo se pueden usar una vez, ya que no tienen un nombre asociado para ser reutilizadas.

# La sintaxis básica de una función lambda es:
# lambda argumentos: expresión

# Ejemplo de función lambda para sumar dos números
sumar = lambda x, y: x + y
resultado = sumar(5, 3)
print(f"El resultado de sumar(5, 3) es: {resultado}")

# Ejemplo de función lambda para elevar un número al cuadrado
numeros = list(range(1, 10))
print(f"Números del 1 al 19:\n{numeros}")
# Filtra los números pares de la lista
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares del 1 al 19:\n{numeros_pares}")
# Eleva cada número al cuadrado usando map y lambda
numeros_cuadrados = list(map(lambda x: x**2, numeros))
print(f"Números del 1 al 19 elevados al cuadrado:\n{numeros_cuadrados}")
