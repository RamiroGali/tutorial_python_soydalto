import re

texto = """Hola maestro, esta es la cadena 1, como estas mi capitan
Esta es la segunda linea de texto
Y Esta es la final definitiva mi capitan"""

resultado = re.search("Hola", texto)
print(resultado)

resultado = re.findall("esta", texto)
print(resultado)

texto = """Hola maestro, esta es la cadena 1, como estas mi capitan
Esta es la linea 2. de texto
Y Esta es la final (linea 3) definitiva mi capitan 852"""

# \d : Busca dígitos numéricos del 0-9
resultado = re.findall(r"\d", texto)
print(resultado)

# \D : Busca todo menos los dígitos numéricos del 0-9
resultado = re.findall(r"\D", texto)
print(resultado)

# \w : Busca caracteres alphanuméricos [a-z A-Z _]
resultado = re.findall(r"\w", texto)
print(resultado)

# \W : Busca todo excepto los caracteres alphanuméricos [a-z A-Z _]
resultado = re.findall(r"\W", texto)
print(resultado)

# \s : Busca espacios en blanco -> espacios, tabs, saltos de línea
resultado = re.findall(r"\s", texto)
print(resultado)

# \S : Busca todo excepto los espacios en blanco -> espacios, tabs, saltos de línea
resultado = re.findall(r"\S", texto)
print(resultado)

# \n : Busca saltos de linea \n
resultado = re.findall(r"\n", texto)
print(resultado)

# . : Busca todo menos los saltos de linea \n
resultado = re.findall(r".", texto)
print(resultado)

# \ : Cancela caracteres especiales como un comando de la expresión regular para considerarlo de manera literal
# Previamente el punto servía para buscar todo menos saltos en línea, pero ahora permitirá buscar los puntos en el texto
resultado = re.findall(r"\.", texto)
print(resultado)

# Armando una cadena que busca un numero, seguido de un punto y un espacio
resultado = re.findall(f"\d\.\s", texto)
print(resultado)

# ^ : Busca el comienzo de una línea
resultado = re.findall(f"^", texto, flags=re.M)
print(resultado)

# $ : Busca el final de una línea
resultado = re.findall(f"$", texto, flags=re.M)
print(resultado)

# {n} : busca una n cantidad de veces lo que se estaba buscando con el caracter de la izquierda
resultado = re.findall(r"\d{3}", texto)
print(resultado)

# {nmin, nmax} : busca una nmin cantidad de veces como mínimo, pero sin que se superen las nmax de veces como maximo
#  lo que se estaba buscando con el caracter de la izquierda
resultado = re.findall(r"\d{2,5}", texto)
print(resultado)


texto = "aaaabbbbaaabbabbbbbaaabbbbbb abababab"
# {nmin, nmax} : busca una nmin cantidad de veces como mínimo, pero sin que se superen las nmax de veces como maximo
#  lo que se estaba buscando con el caracter de la izquierda
resultado = re.findall(r"ab{2,5}", texto)
print(resultado)

# {nmin, nmax} : busca una nmin cantidad de veces como mínimo, pero sin que se superen las nmax de veces como maximo
#  lo que se estaba buscando con el caracter de la izquierda
# se usa parentesis para que considere ambos caracteres como una sola referencia
resultado = re.findall(r"(ab){2,5}", texto)
print(resultado)

# | : operador or, busca la referencia de la izquierda o la de la derecha del operador
resultado = re.findall(r"\d|\s", texto)
print(resultado)


# Busca un "The" que se encuentre al principio de la línea, que se encuentre seguido de una cantidad indeterminada de caracteres y encontrar la cadena de texto dog al final de la línea
texto = "The quick brown fox jumps over the lazy dog"
resultado = re.search("^The.*dog$", texto)
print(resultado)

if resultado:
    print("SI")
else:
    print("NO")

# cadena que se pretende buscar la fecha para ocultarla
texto = "La fecha es 23/06/2021 y el telefono es +1-555-555-555"
# patrón a buscar con degex
pattern = r"\d{2}/\d{2}/\d{4}"

# el texto con el que se reemplazará el patrón
replacement = "(Fecha Oculta)"
resultado = re.sub(pattern, replacement, texto)
print(resultado)


texto = "reemplazando todas las vocales con asteriscos"
resultado = re.sub("[aeiou]", "*", texto)
print(resultado)

texto = "example@example.com"
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z]{2,}"
resultado = re.match(pattern, texto)
if resultado:
    print("direccion de correo valido")
else:
    print("direccion de correo no valido")

texto = "Este es un ejemplo de página web: https://www.example.com, https://proyectodalto.com y también podemos visitar http://example.org"
pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
resultado = re.findall(pattern, texto)
print(resultado)


# detectando un numero CABA y ocultandolo:
texto = "Hola Pedro, mi numero son: +54 11 4321-4321, +54 11 4321-4321"
pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"
resultado = re.sub(pattern, "(Numero oculto)", texto)
print(resultado)
