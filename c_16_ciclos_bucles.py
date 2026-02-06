# Curso Python 16 - soydalto
# Ciclos y bucles (loops)

# Los ciclos o bucles son estructuras de control que permiten repetir una o varias instrucciones mientras se cumpla una condición específica.

# El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena, etc.) y ejecutar un bloque de código para cada elemento de la secuencia.
# Por ejemplo:
mi_lista = ["manzana", "banana", "cereza"]
for fruta in mi_lista:
    # Aquí puedes realizar cualquier operación con la variable 'fruta', que representa cada elemento de la lista en cada iteración del bucle.
    print(fruta)

# El bucle while se utiliza para repetir un bloque de código mientras se cumpla una condición específica.
# Por ejemplo:
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# El bucle for también puede utilizarse con la función range() para generar una secuencia de números.
# Por ejemplo:
for i in range(5):
    print(i)

# La función range() también puede aceptar parámetros adicionales para especificar el inicio, fin y paso de la secuencia.
# los parametros de range() son:
# 1. start (opcional): El número desde el cual se inicia la secuencia
# 2. stop: El número en el cual se detiene la secuencia (no incluido)
# 3. step (opcional): El incremento entre cada número en la secuencia (por defecto es 1)
# Por ejemplo:
for i in range(2, 10, 2):
    print(i)

# Si se cumple con las siguientes condiciones:
# 1. Tienes dos o más listas de la misma longitud
# 2. Quieres iterar sobre ambas listas al mismo tiempo
# Entonces puedes usar la función zip() para combinar las listas y luego iterar sobre ellas con un bucle for.
# Por ejemplo:
numeros = ["uno", "dos", "tres", "cuatro", "cinco"]
animales = ["perro", "gato", "conejo", "hamster", "pez"]
for numero, animal in zip(numeros, animales):
    print(f"numero: {numero}\nanimales: {animal}")

# La función enumerate() se utiliza para obtener tanto el índice como el valor de cada elemento en una secuencia durante la iteración.
# Esto es útil cuando necesitas acceder a la posición de los elementos además de su valor.
for num in enumerate(numeros):
    print(f"Índice: {num[0]}, Valor: {num[1]}")


# For/Else
# El bucle for también puede tener una cláusula else que se ejecuta después de que el bucle haya terminado de iterar sobre la secuencia
# siempre y cuando no se haya interrumpido con una declaración break.
for numero in numeros:
    print(f"Índice: {numeros.index(numero)}, Valor: {numero}")
    # Si el número actual es el penúltimo elemento de la lista, se rompe el bucle para evitar ejecutar la cláusula else
    if numeros.index(numero) == len(numeros) - 2:
        break
else:
    print("Se iteró sobre toda la lista completa!")
