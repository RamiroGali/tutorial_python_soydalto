# Curso Python 12 - soydalto
# Ejercicio Práctico 2: Comparación de palabras por segundos

"""
Ejercicio: Realizar un anàlisis sobre la cantidad de palabras por segundos que se demorarìa en decir una frase
"""

frase = input("Ingresa una frase para analizar su duración: ")
palabras_separadas = frase.split(" ")

cantidad_palabras = len(palabras_separadas)
tiempo_por_palabra_prome = (
    0.5  # Asumiendo que se tarda 0.5 segundos en decir cada palabra
)
tiempo_total_prome = cantidad_palabras * tiempo_por_palabra_prome
print(
    f"La frase tiene {cantidad_palabras} palabras y se demoraría aproximadamente {tiempo_total_prome:.2f} segundos en decirla."
)

# Asumiendo que se tarda 0.65 segundos en decir cada palabra
tiempo_total_dalto = cantidad_palabras * tiempo_por_palabra_prome * 100 // 2 * 1.3 / 100
print(
    f"En el estilo de Dalto, se demoraría aproximadamente {tiempo_total_dalto:.2f} segundos en decirla."
)
