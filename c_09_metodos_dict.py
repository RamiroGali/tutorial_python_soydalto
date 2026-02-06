# Curso Python 9 - soydalto
# Métodos de Dict


"""
Métodos para diccionarios (dict)
Análisis de métodos clave para manipulación de diccionarios
Útiles para análisis de bases de datos
"""

# ===== MÉTODO: keys() =====
# Retorna una vista de todas las claves del diccionario
print("=" * 50)
print("MÉTODO: keys()")
print("=" * 50)

registro_usuario = {
    "id": 1,
    "nombre": "Juan",
    "email": "juan@example.com",
    "edad": 28,
    "ciudad": "Madrid",
}

print("Diccionario original:")
print(registro_usuario)
print("\nClaves del diccionario:")
print(registro_usuario.keys())
print("Tipo:", type(registro_usuario.keys()))

# Convertir a lista
claves_lista = list(registro_usuario.keys())
print("Claves como lista:", claves_lista)

# Iterar sobre las claves
print("\nIterando sobre las claves:")
for clave in registro_usuario.keys():
    print(f"  - {clave}")

# ===== MÉTODO: get() =====
# Obtiene el valor de una clave, con valor por defecto si no existe
print("\n" + "=" * 50)
print("MÉTODO: get()")
print("=" * 50)

print("Obtener valor existente:")
print(f"  registro_usuario.get('nombre') = {registro_usuario.get('nombre')}")

print("\nObtener valor inexistente (sin defecto):")
resultado = registro_usuario.get("telefono")
print(f"  registro_usuario.get('telefono') = {resultado}")

print("\nObtener valor inexistente (con defecto):")
resultado = registro_usuario.get("telefono", "No disponible")
print(f"  registro_usuario.get('telefono', 'No disponible') = {resultado}")

# Útil para base de datos
print("\nÚtil para análisis de BD:")
datos_bd = {"username": "admin", "last_login": "2024-01-15"}
rol = datos_bd.get("role", "usuario")  # Si no existe, asigna valor por defecto
print(f"  Rol de usuario: {rol}")

# ===== MÉTODO: items() =====
# Retorna pares (clave, valor) del diccionario
print("\n" + "=" * 50)
print("MÉTODO: items()")
print("=" * 50)

print("Items del diccionario:")
print(registro_usuario.items())

print("\nIterando sobre items (clave-valor):")
for clave, valor in registro_usuario.items():
    print(f"  {clave}: {valor}")

# Útil para transformar datos
print("\nConvertir items a lista:")
items_lista = list(registro_usuario.items())
print(items_lista)

# ===== MÉTODO: pop() =====
# Elimina y retorna el valor de una clave
print("\n" + "=" * 50)
print("MÉTODO: pop()")
print("=" * 50)

datos_temp = {
    "id": 1,
    "nombre": "Pedro",
    "token": "abc123xyz",
    "timestamp": "2024-01-15",
}

print("Diccionario antes de pop():")
print(datos_temp)

# Pop con clave existente
token_removido = datos_temp.pop("token")
print(f"\nToken removido: {token_removido}")
print("Diccionario después de pop('token'):")
print(datos_temp)

# Pop con clave inexistente y valor por defecto
estado = datos_temp.pop("estado", "activo")
print(f"\nEstado (no existía): {estado}")

# Pop sin valor por defecto causa error si la clave no existe
# datos_temp.pop('inexistente')  # Esto daría KeyError

print("\nÚtil para BD - Limpiar datos temporales:")
cache = {"user_1": "datos_antiguos", "user_2": "datos_actuales"}
print(f"Cache antes: {cache}")
datos_expirados = cache.pop("user_1", None)
print(f"Cache después: {cache}")

# ===== MÉTODO: clear() =====
# Elimina todos los elementos del diccionario
print("\n" + "=" * 50)
print("MÉTODO: clear()")
print("=" * 50)

sesion_temporal = {
    "user_id": 123,
    "session_token": "token_xyz",
    "inicio": "2024-01-15 10:30",
}

print("Diccionario antes de clear():")
print(sesion_temporal)

sesion_temporal.clear()
print("Diccionario después de clear():")
print(sesion_temporal)
print("¿Está vacío?:", len(sesion_temporal) == 0)

# ===== MÉTODO ADICIONAL: update() =====
# Actualiza el diccionario con pares clave-valor de otro diccionario
print("\n" + "=" * 50)
print("MÉTODO ADICIONAL: update()")
print("=" * 50)

usuario = {"id": 1, "nombre": "Laura"}
print("Usuario original:")
print(usuario)

# Actualizar con nuevo diccionario
usuario.update({"email": "laura@example.com", "edad": 30})
print("\nDespués de update():")
print(usuario)

# Útil para BD: Actualizar registros
print("\nÚtil para BD - Merge de datos:")
datos_basicos = {"id": 1, "nombre": "Carlos"}
datos_adicionales = {"email": "carlos@example.com", "estado": "activo"}
datos_basicos.update(datos_adicionales)
print(f"Datos completos: {datos_basicos}")

# ===== MÉTODO ADICIONAL: values() =====
# Retorna una vista de todos los valores del diccionario
print("\n" + "=" * 50)
print("MÉTODO ADICIONAL: values()")
print("=" * 50)

producto = {"id": 101, "nombre": "Laptop", "precio": 999.99, "stock": 5}
print("Diccionario:")
print(producto)

print("\nValores del diccionario:")
print(producto.values())

print("\nIterando sobre valores:")
for valor in producto.values():
    print(f"  - {valor}")

# Útil para análisis de BD
print("\nÚtil para BD - Verificar valores:")
valores = list(producto.values())
print(f"Cantidad de atributos: {len(valores)}")

# ===== RESUMEN Y CASO DE USO =====
print("\n" + "=" * 50)
print("CASO DE USO: Simulación de operación en BD")
print("=" * 50)

# Simular tabla de usuarios
usuarios_bd = [
    {"id": 1, "username": "admin", "email": "admin@db.com", "activo": True},
    {"id": 2, "username": "user1", "email": "user1@db.com", "activo": True},
    {"id": 3, "username": "user2", "email": "user2@db.com", "activo": False},
]

print("Base de datos de usuarios:")
for usuario in usuarios_bd:
    print(f"  {usuario}")

# Búsqueda con get()
print("\nBúsqueda de usuario específico:")
# Buscando al primer usuario, asumiendo que es ya conocido
usuario_buscado = usuarios_bd[0]
email = usuario_buscado.get("email", "No especificado")
print(f"  Email encontrado: {email}")

# Listar todas las propiedades con items()
print("\nPropiedades del primer usuario:")
for propiedad, valor in usuarios_bd[0].items():
    print(f"  {propiedad} = {valor}")

# Actualizar con update()
print("\nActualizar usuario (simular UPDATE en BD):")
usuarios_bd[0].update({"ultimo_login": "2024-01-15 15:45", "activo": True})
print(f"  {usuarios_bd[0]}")

# Eliminar campo sensible con pop()
print("\nEliminar datos sensibles antes de enviar (simular DELETE de campo):")
usuario_copia = usuarios_bd[0].copy()
usuario_copia.pop("email", None)  # Eliminar email por privacidad
print(f"  Sin email: {usuario_copia}")

print("\n" + "=" * 50)
print("Fin del análisis de métodos de dict")
print("=" * 50)
