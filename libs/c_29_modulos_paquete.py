import paquete.c_30_modulos_paquete_definir
import paquete.subpaquete.c_31_modulos_subpaquetes


print(type(paquete.__path__))
print(paquete.__path__)
print(paquete.subpaquete.__path__)

print(paquete.c_30_modulos_paquete_definir.saludar3())
print(paquete.subpaquete.c_31_modulos_subpaquetes.saludar4())
