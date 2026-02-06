# Curso Python 6 - soydalto
# Operadores Lógicos

# Operadores lógicos: and, or, not

# AND
resultado_and_1 = True and True
resultado_and_2 = False and True
resultado_and_3 = True and False
resultado_and_4 = False and False
print("AND:")
print("True and True =", resultado_and_1)
print("False and True =", resultado_and_2)
print("True and False =", resultado_and_3)
print("False and False =", resultado_and_4)

# OR
resultado_or_1 = True or True
resultado_or_2 = False or True
resultado_or_3 = True or False
resultado_or_4 = False or False
print("OR:")
print("True or True =", resultado_or_1)
print("False or True =", resultado_or_2)
print("True or False =", resultado_or_3)
print("False or False =", resultado_or_4)

# NOT
resultado_not_1 = not True
resultado_not_2 = not False
print("NOT:")
print("not True =", resultado_not_1)
print("not False =", resultado_not_2)

# Ejemplos combinados de operadores lógicos
edad = 25
ingreso = 2000
tiene_trabajo = True
acceso_credito = (edad >= 18) and (ingreso >= 1500) and tiene_trabajo
print("Acceso a crédito:", acceso_credito)
