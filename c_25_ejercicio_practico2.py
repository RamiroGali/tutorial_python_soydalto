# Curso Python 25 - soydalto
# Ejercicio Práctico 4

"""
Ejercicio Práctico 4

- Crear una función que genere una lista de números primos hasta un número dado por el usuario. Luego, imprimir la lista de números primos generada.
- Crear una función que genere una lista de números de la serie de Fibonacci hasta un número dado por el usuario. Luego, imprimir la lista de números de la serie de Fibonacci generada.
"""


def es_primo(num):
    # Un número es primo si es mayor que 1 y no tiene divisores positivos aparte de 1 y él mismo
    if num < 2:
        return False

    # Verificar si el número es divisible por algún número desde 2 hasta la raíz cuadrada de num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generar_primos(hasta):
    primos = []
    for num in range(2, hasta + 1):
        if es_primo(num):
            primos.append(num)
    return primos


def generar_fibonacci(hasta):
    fibonacci = []
    a, b = 0, 1
    while a <= hasta:
        fibonacci.append(a)
        # Actualizar a y b para la siguiente iteración
        a, b = b, a + b
    return fibonacci


def generar_serie(hasta, tipo):
    if tipo == "primos":
        # Ejemplo usando una lambda: definimos y ejecutamos inmediatamente
        # la lambda que recibe 'n' y devuelve la lista filtrada de primos.
        # No es mas eficiente, pero es una forma diferente de hacerlo
        # all funciona como una función con un while que verificará si el numero es primo, y que si no es primo, retornará un false
        # posteriormente, filter se encargará de filtrar los números primos y devolver una lista con ellos
        # al final se escribe (hasta) que se usará como un argumento para la función lambda, y se generará la lista de números primos hasta el número dado por el usuario
        return (
            lambda n: list(
                filter(
                    lambda x:
                    # verificar numero primo
                    # A diferencia de la función con el ciclo while,
                    # la función all recorrerá todos los valores incluso
                    # cuando se haya topado con alguno que no cumple la condición de ser primo
                    # generando ciclos de operaciones innecesarios
                    all(x % i != 0 for i in range(2, int(x**0.5) + 1)),
                    range(2, n + 1),
                )
            )
        )(hasta)

    elif tipo == "fibonacci":
        return generar_fibonacci(hasta)
    else:
        raise ValueError("Tipo de serie no reconocido. Use 'primos' o 'fibonacci'.")


lim_maximo = int(input("Ingrese el limite máximo de la serie: "))

primos = generar_serie(lim_maximo, "primos")
print(f"Números primos hasta {lim_maximo}: {primos}")

fibonacci = generar_serie(lim_maximo, "fibonacci")
print(f"Números de la serie Fibonacci hasta {lim_maximo}: {fibonacci}")
