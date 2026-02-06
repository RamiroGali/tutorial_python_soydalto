# Curso Python 20 - soydalto
# Funciones en Python

# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Se definen con la palabra clave 'def' seguida del nombre de la función y paréntesis.
# Los parámetros son valores que se pasan a la función cuando se llama.
# El valor de retorno es lo que devuelve la función al finalizar su ejecución.

# Funciones de Python incorporadas (built-in)
# Algunas funciones comunes incluyen:
numeros = [1, 2, 3, 4, 5]

numero_mas_bajo = min(numeros)
print(f"El número más bajo es: {numero_mas_bajo}")

numero_mas_alto = max(numeros)

print(f"El número más alto es: {numero_mas_alto}")

# redondeando a 6 decimales
pi = 3.141592653589793
print(f"El valor de pi redondeado a 6 decimales es: {round(pi, 6)}")

# Convertir a booleano
resultado_bool = bool(-1)
print(f"El resultado booleano es: {resultado_bool}")

# Verificar si todos los elementos son verdaderos
resultado_all = all([True, "true", "casa", True, 1, None])
print(f"El resultado de all() es: {resultado_all}")


# Definición de una función simple
def saludar(nombre):
    return f"Hola, {nombre}!"


# Llamada a la función
print(saludar("Ramiro"))


def crear_contrase_random(num):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena


password = crear_contrase_random(5)
print(f"tu contraseña nueva es {password}")
