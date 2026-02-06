# Curso Python 10 - soydalto
# Función input() - Entrada de datos del usuario

# La función input() permite al usuario ingresar datos desde el teclado
# Retorna siempre una cadena de texto (string), incluso si el usuario ingresa números

print("=== Usando input() para capturar texto ===")
nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}!")

print("\n=== Usando input() para capturar números (conversión a int) ===")
# Importante: input() devuelve un string, por lo que debemos convertir a int explícitamente
edad = int(input("Ingresa tu edad: "))
print(f"Tienes {edad} años")

print("\n=== Usando input() para capturar números decimales (conversión a float) ===")
# Similar a int, debemos convertir explícitamente a float para números decimales
altura = float(input("Ingresa tu altura en metros: "))
print(f"Tu altura es {altura}m")

print("\n=== ADVERTENCIA: Conversión de float a int ===")
# IMPORTANTE: Si el usuario ingresa un decimal y queremos convertir a int,
# debemos primero convertir a float y luego a int
# NO podemos hacer directamente int() de un string con decimal

print("Intenta ingresar un número decimal y luego lo convertiremos a entero...")
numero_decimal_str = input("Ingresa un número decimal: ")

# Forma CORRECTA: float primero, luego int
numero_decimal = float(numero_decimal_str)  # Primero a float
numero_entero = int(numero_decimal)  # Luego a int
print(f"Número decimal: {numero_decimal}")
print(f"Número entero: {numero_entero}")

# Forma INCORRECTA (generaría error):
# numero_entero = int("3.5")  # ValueError: invalid literal for int() with base 10: '3.5'

print("\n=== Capturando múltiples valores ===")
# Se pueden capturar múltiples valores separándolos
valor1 = input("Primer valor: ")
valor2 = input("Segundo valor: ")
print(f"Valor 1: {valor1}, Valor 2: {valor2}")

print("\n=== Capturando múltiples valores en una sola línea ===")
# También es posible usar split() para separar valores ingresados en una sola línea
print("Ingresa dos números separados por espacio:")
numero1, numero2 = input().split()
numero1 = int(numero1)
numero2 = int(numero2)
print(f"Suma: {numero1 + numero2}")

# === Consideraciones importantes ===
# 1. input() SIEMPRE retorna un string
# 2. Cuando se quiera trabajar con números, se debe convertir explícitamente
# 		de string a float y posteriormente de float a int.
# 4. int() no acepta strings con puntos decimales directamente
# 5. Maneja excepciones si esperas valores específicos con try-except
