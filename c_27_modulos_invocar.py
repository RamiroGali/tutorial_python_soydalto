# Importación del módulo como un objeto con sus funciones como sus métodos.
# Si bien, lo invocamos con el nombre "c_26_modulos_definir"
# Le vamos a dar un nombre diferente para trabajar dentro de este documento
# para llamarle a ese paquete de funciones como "saludos"
import c_26_modulos_definir as saludos

# Importación de una función del módulo como parte del código del documento
from c_26_modulos_definir import saludar1

import libs.c_28_modulos_enrutamientos

# También se puede renombrar a la función que se quiere importar
# from c_26_modulos_definir import saludar1 as saludar

# También se pueden importar todas las funciones contenidas dentro del módulo
# Pero la importación demorará mas tiempo del que le correspondería si el módulo es demasiado extenso en contenido
# from c_26_modulos_definir import *

# Llamar a la función que fue incorporada a este código de manera independiente al resto de sus funciones
print(saludar1("Rodrigo"))

# Llamar al módulo "saludos" como un paquete que contiene en su interior un método que se llama despedir1
print(saludos.despedir1("Rodrigo"))

# Llamar a la función enrutada dentro de la carpeta libs
print(libs.c_28_modulos_enrutamientos.algo())

# Para ver las propiedades y métodos del namespace
print(dir(saludos))

# Accedemos el nombre original del módulo
print(saludos.__name__)

# Accedemos el nombre original del documento actual
print(__name__)

#
