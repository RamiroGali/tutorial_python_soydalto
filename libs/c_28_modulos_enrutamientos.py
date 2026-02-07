#
def algo():
    return "has accedido a la función enrutada dentro de libs"


# sys: módulo build-in para el manejo de las rutas de importación de módulos entre otras funciones.
import sys

# # Muestra todos los comandos de las propiedades en sys
# print(sys.builtin_module_names)

# # Muestra la lista de las rutas de los módulos a los que el código presente accede para cargar los diferentes módulos y librerias
# print(sys.path)

# Habilitar el acceso a los archivos de módulos ubicados en la siguiente ruta
sys.path.append(
    "C:\\Users\\ramiro.galindo\\OneDrive - Empresas Repremundo\\Documentos\\GitHub\\tutoriales\\python_soydalto"
)

# Ahora si es posible importar el módulo que se encuentra al nivel de la carpeta contenedora del archivo de código actual.
import c_26_modulos_definir


def saludo2():
    print(c_26_modulos_definir.saludar1(", Saludos desde c_28"))
