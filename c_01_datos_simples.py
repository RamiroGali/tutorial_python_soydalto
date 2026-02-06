# # The `Curso` in the code is a comment that indicates the course name or topic related to the Python
# code. It is used to provide a brief description or title for the code section that follows. In
# this case, it seems to be indicating that the following code section is related to a Python course
# or tutorial.
# Curso Python 1 - soydalto
# Tipos de datos y asignación de variables en Python
# Definición de variables con diferentes tipos de datos
# - Formatos de definición de nombres de variables:
#  - snake_case: my_variable
#  - camelCase: myVariable
#  - PascalCase: MyVariable
#  - Reglas para nombres de variables:
#    - No pueden comenzar con un número
my_string = "string"; # String
my_int = 1; # Integer
my_float = 1.0; # Float
my_bool = True; # Boolean
my_list = [1, 2, 3]; # List

# Imprimir los valores y resultados de operaciones con los tipos de datos
print("String:", my_string);
print("Integer:", my_int);
print("Float:", my_float);
print("Boolean:", my_bool);
print("List:", my_list);

# Operaciones con tipos de datos
# Concatenación de strings con el operador +
print("Concatenación de string:", my_string + " concatenado");

# Concatenación de strings con el operador f-string
nombre = 'Mario';
apellido = 'Galindo';
fullname = f"{nombre} {apellido}";
print("Nombre completo usando f-string:", fullname);

# Verificar si una cadena "Mario" se encuentra dentro de otra cadena, usando operadores de pertenencia
print("Mario está en el fullname:", "Mario" in fullname); # Verificar si "Mario" está en fullname
print("Ramiro está en el fullname:", "Ramiro" not in fullname); # Verificar si "Ramiro" está en fullname

del fullname; # Eliminar variable fullname

print("Suma de integer y float:", my_int + my_float);
print("Multiplicación de integer:", my_int * 2);

# Acceso a elementos de una lista
for item in my_list:
	print("Elemento de lista:", item);