class MyExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometistes el siguiente error: {err}")


try:
    raise MyExcepcion("Tener cuidado")
except:
    print("Posiblemente se solucione")
