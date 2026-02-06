# Curso Python 7 - soydalto
# Métodos de Cadenas

# Definición de una cadena de texto
texto = "  Hola, Bienvenido al Curso de Python de soydalto!  "
print("Texto original:", repr(texto))

# Listado de métodos disponibles para cadenas, haciendo uso de la función dir()
print("\nMétodos de cadenas:")
lista_metodos_string = dir(texto)
print(lista_metodos_string)

# Método strip() - Elimina espacios en blanco al inicio y al final
texto_strip = texto.strip()
print("Después de strip():", repr(texto_strip))
# Método lower() - Convierte la cadena a minúsculas
texto_lower = texto_strip.lower()
print("Después de lower():", repr(texto_lower))
# Método upper() - Convierte la cadena a mayúsculas
texto_upper = texto_strip.upper()
print("Después de upper():", repr(texto_upper))

# Método replace() - Reemplaza una subcadena por otra
texto_replace = texto_strip.replace("Python", "Java")
print("Después de replace():", repr(texto_replace))

# Método split() - Divide la cadena en una lista de palabras
texto_split = texto_strip.split()
print("Después de split():", texto_split)

# Método join() - Une una lista de palabras en una cadena
texto_join = " ".join(texto_split)
print("Después de join():", repr(texto_join))

# Método find() - Busca una subcadena y devuelve su posición
posicion_python = texto_strip.find("Python")
print("Posición de 'Python':", posicion_python)

# Método count() - Cuenta cuántas veces aparece una subcadena
conteo_o = texto_strip.count("o")
print("Número de veces que aparece la letra/vocal 'o':", conteo_o)

# Método startswith() - Verifica si la cadena comienza con una subcadena
comienza_con_hola = texto_strip.startswith("Hola")
print("¿El texto comienza con 'Hola'?", comienza_con_hola)
# Método endswith() - Verifica si la cadena termina con una subcadena
termina_con_exclamacion = texto_strip.endswith("!")
print("¿El texto termina con '!'?", termina_con_exclamacion)

# Método isalpha() - Verifica si la cadena contiene solo letras
solo_letras = texto_strip.isalpha()
print("¿El texto contiene solo letras?", solo_letras)

# Uso de la funcion len() para obtener la longitud de la cadena
longitud_texto = len(texto_strip)
print("Longitud del texto después de strip():", longitud_texto)

# Método translate() - Elimina caracteres específicos usando str.maketrans()
tabla_traduccion = str.maketrans("", "", "aeiouAEIOU")
texto_sin_vocales = texto_strip.translate(tabla_traduccion)
print("Texto sin vocales:", repr(texto_sin_vocales))
