# Curso Python 5 - soydalto
# Condicionales If-Else

# Definición de informacion almacenada en la base de datos
passw_bd = "admin123"

# Información del usuario
passw_usuario = "admin123"
edad_usuario = 20
economia_ingreso_usuario = 1500
economia_gasto_usuario = 300
economia_balance_usuario = economia_ingreso_usuario - economia_gasto_usuario

if passw_usuario == passw_bd:
    print("INICIANDO SESIÓN...")
    # anidamiento de if-else
    if edad_usuario >= 18:
        print("Eres mayor de edad.")

        # anidamiento de if-else y uso de elif
        if economia_balance_usuario >= 1000:
            print("Tienes acceso a la tarjeta de crédito.")
        elif economia_balance_usuario < 1000 and economia_balance_usuario >= 500:
            print("Tienes acceso a la tarjeta de débito.")
        elif economia_balance_usuario < 500 and economia_balance_usuario >= 0:
            print("Tienes acceso a una cuenta de ahorros básica.")
        elif economia_balance_usuario < 0:
            print("Tu cuenta está en números rojos.")
        else:
            print("No tienes acceso a tarjetas bancarias.")
    else:
        print("Eres menor de edad.")
else:
    print("Acceso denegado. Intente nuevamente.")

# Instrucción fuera del if-else
print("Fin del programa")
