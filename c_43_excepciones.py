def sumar_dos():
    while True:
        a = input("Numero 1:")
        b = input("Numero 2:")
        try:
            resultado = int(a) + int(b)
        # except Exception as e:
        #     # Identificar el tipo de la excepción frente al caso presente
        #     print(f"Error:{type(e).__name__}")
        except ValueError as e:
            print(f"Error:{e}")
            print("continua, ingresa dos numeros")
        else:
            break
        finally:
            print("Esto se ejecuta siempre")

    # Mostrar la suma de dos numeros
    return resultado


print(sumar_dos())
