# Curso Python 21 - soydalto
# Funciones con parámetros *args y **kwargs en Python


# Forma no optima de sumar valores sin usar *args
def sumar1(lista):
    resultado = 0
    for numero in lista:
        resultado += numero
    return resultado


result = sumar1([1, 2, 3, 4, 5])
print(f"Resultado de sumar1: {result}")


# Forma optima de sumar valores usando *args
def sumar2(nombre, *args):
    resultado = 0
    for numero in args:
        resultado += numero
    return f"{nombre}: {resultado}"


# Llamada a la función sumar2 con múltiples argumentos
result = sumar2("Lucas", 3, 7, 10, 4, 5)
print(result)


# Forma no optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])


result = suma_total([10, 20, 30, 40])
print(f"Resultado de suma_total: {result}")


# Función que usa **kwargs para recibir parámetros nombrados
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


# Llamada a la función mostrar_info con múltiples parámetros nombrados
mostrar_info(nombre="Ana", edad=28, ciudad="Madrid")
mostrar_info(profesion="Ingeniero", empresa="TechCorp", pais="Argentina")
# Consideraciones importantes:
# 1. *args permite pasar un número variable de argumentos posicionales a una función
# 2. **kwargs permite pasar un número variable de argumentos nombrados (clave=valor) a una función
# 3. Ambos son útiles para crear funciones flexibles y reutilizables
# 4. Dentro de la función, *args se trata como una tupla y **kwargs como un diccionario
# 5. Se pueden combinar *args y **kwargs en la misma función, pero *args debe ir antes de **kwargs


# Ejemplo combinando *args y **kwargs
def combinar_todo(*args, **kwargs):
    print("Argumentos posicionales (args):")
    for arg in args:
        print(arg)
    print("\nArgumentos nombrados (kwargs):")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


combinar_todo(1, 2, 3, nombre="Carlos", edad=30)


# Llamada a la función combinar_todo con ambos tipos de argumentos
# Consideraciones adicionales:
# 6. El uso de *args y **kwargs puede mejorar la legibilidad y mantenibilidad del código
# 7. Útil en funciones que requieren flexibilidad en la cantidad de argumentos
# 8. Permite pasar listas o diccionarios directamente usando el operador de desempaquetado (* o **)
def mostrar_lista(*args):
    for item in args:
        print(item)


mi_lista = [10, 20, 30]
mostrar_lista(*mi_lista)  # Desempaquetando la lista al llamar a la función


def mostrar_diccionario(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mi_dict = {"a": 1, "b": 2, "c": 3}
mostrar_diccionario(**mi_dict)  # Desempaquetando el diccionario al llamar a la función


# 9. Ayuda a crear APIs y librerías más flexibles y adaptables a diferentes necesidades
# 10. Es importante documentar el uso de *args y **kwargs para facilitar su comprensión por otros desarrolladores
# Ejemplo avanzado: función que combina *args y **kwargs para crear un perfil de usuario
def crear_perfil_usuario(username, *args, **kwargs):
    profile = {"username": username}
    for i, hobby in enumerate(args, start=1):
        profile[f"hobby_{i}"] = hobby
    for clave, valor in kwargs.items():
        profile[clave] = valor
    return profile


usuario = crear_perfil_usuario(
    "maria123", "lectura", "viajar", edad=25, ciudad="Barcelona", profesion="Diseñadora"
)
print("\nPerfil de usuario creado:")
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
# Llamada a la función crear_perfil_usuario con ambos tipos de argumentos
# Consideraciones finales:
# 11. El uso adecuado de *args y **kwargs puede simplificar la gestión de parámetros en funciones complejas
# 12. Facilita la creación de funciones genéricas que pueden adaptarse a diferentes contextos y requisitos
# 13. Siempre es recomendable validar y documentar los parámetros esperados cuando se usan *args y **kwargs
# 14. Practicar su uso en diferentes escenarios ayuda a entender mejor sus beneficios y limitaciones
# 15. Recuerda que el orden de los parámetros en la definición de la función es importante: primero los parámetros normales, luego *args, y finalmente **kwargs
