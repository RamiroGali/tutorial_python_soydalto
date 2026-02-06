# Python desde Cero - Curso soydalto

## Descripción

Curso completo de Python desde cero impartido por **soydalto**. Este curso cubre los fundamentos esenciales del lenguaje Python, desde tipos de datos básicos hasta funciones de entrada/salida.

**Video principal:** https://www.youtube.com/watch?v=nKPbfIU442g

---

## Índice de Contenidos

### Clase 1: Tipos de Datos Simples (`c_01_datos_simples.py`)
- Concepto de variables y tipos de datos
- Tipos de datos primitivos:
  - **String (str):** Cadenas de texto
  - **Integer (int):** Números enteros
  - **Float (float):** Números decimales
  - **Boolean (bool):** Valores verdadero/falso
- Convenciones de nomenclatura:
  - snake_case
  - camelCase
  - PascalCase
- Reglas para nombres de variables
- Operaciones básicas con tipos de datos
- Concatenación de strings con `+` y f-strings
- Operadores de pertenencia: `in`, `not in`
- Iteración sobre listas con `for`

### Clase 2: Tipos de Datos Compuestos (`c_02_datos_compuestos.py`)
- **Listas:**
  - Definición con corchetes `[]`
  - Colecciones ordenadas y mutables
  - Indexación y acceso a elementos
  - Métodos: `append()`, `remove()`, `pop()`, `sort()`, `reverse()`
- **Tuplas:**
  - Definición con paréntesis `()`
  - Colecciones ordenadas e inmutables
  - Diferencias con listas
- **Diccionarios:**
  - Definición con llaves `{}`
  - Pares clave-valor
  - Claves únicas
  - Similitud con JSON
  - Tipos de datos como claves

### Clase 3: Operadores Aritméticos (`c_03_operadores_aritmeticos.py`)
- Operación de suma `+`
- Operación de resta `-`
- Operación de multiplicación `*`
- Operación de división `/`
- Operación de división entera `//`
- Operación de módulo (residuo) `%`
- Operación de potencia `**`
- Precedencia de operadores

### Clase 4: Operadores de Comparación (`c_04_operadores_comparacion.py`)
- Igualdad `==`
- Desigualdad `!=`
- Mayor que `>`
- Menor que `<`
- Mayor o igual que `>=`
- Menor o igual que `<=`
- Retorno de valores booleanos

### Clase 5: Condicionales If-Else (`c_05_if_else.py`)
- Estructura básica de `if`
- Estructura de `if-else`
- Uso de `elif` (else if) para múltiples condiciones
- Anidamiento de condicionales
- Control de flujo del programa
- Ejemplo práctico: Sistema de autenticación y acceso bancario

### Clase 6: Operadores Lógicos (`c_06_operadores_logicos.py`)
- Operador `and` (Y lógico)
- Operador `or` (O lógico)
- Operador `not` (Negación lógica)
- Combinación de operadores lógicos
- Cortocircuito en evaluación de expresiones

### Clase 7: Métodos de Cadenas (`c_07_metodos_cadenas.py`)
- Método `upper()` - Convertir a mayúsculas
- Método `lower()` - Convertir a minúsculas
- Método `capitalize()` - Capitalizar primera letra
- Método `title()` - Capitalizar cada palabra
- Método `strip()` - Eliminar espacios al inicio/final
- Método `replace()` - Reemplazar caracteres
- Método `split()` - Dividir cadenas
- Método `join()` - Unir elementos de una lista
- Método `find()` - Buscar posición de una subcadena
- Método `startswith()` y `endswith()` - Verificar inicio/final
- Método `count()` - Contar ocurrencias

### Clase 8: Métodos de Listas (`c_08_metodos_listas.py`)
- Método `append()` - Agregar elementos
- Método `remove()` - Eliminar por valor
- Método `pop()` - Eliminar por índice
- Método `insert()` - Insertar en posición específica
- Método `sort()` - Ordenar elementos
- Método `reverse()` - Invertir orden
- Método `count()` - Contar ocurrencias
- Método `index()` - Encontrar posición
- Método `extend()` - Extender con otra lista
- Método `copy()` - Copiar lista
- Método `clear()` - Vaciar lista

### Clase 9: Métodos de Diccionarios (`c_09_metodos_dict.py`)
- Método `keys()` - Obtener todas las claves
- Método `values()` - Obtener todos los valores
- Método `items()` - Obtener pares clave-valor
- Método `get()` - Obtener valor de una clave
- Método `pop()` - Eliminar clave-valor
- Método `update()` - Actualizar diccionario
- Método `clear()` - Vaciar diccionario
- Iteración sobre diccionarios
- Acceso a valores por clave

### Clase 10: Función input() (`c_10_inputs.py`) - **2 horas 40 minutos**
- Función `input()` para captura de datos
- `input()` siempre retorna un string
- Conversión a `int()` para números enteros
- Conversión a `float()` para números decimales
- **IMPORTANTE:** Conversión de float a int
  - Forma correcta: `int(float(string))`
  - No hacer: `int("3.5")` (genera error)
- Captura de múltiples valores
- Uso de `split()` para separar valores
- Validación básica de entrada
- Manejo de excepciones con `try-except`

### Clase 11: Ejercicio Práctico 1 (`c_11_ejercicio_practico.py`)
- Programa interactivo de comparación de duraciones de cursos
- Ingreso múltiple de datos con bucles
- Comparación de valores
- Cálculo de estadísticas (promedio, máximo, mínimo)
- Formateo de salida
- Uso de diccionarios para almacenar datos

---

## Estructura del Proyecto

```
python_soydalto/
├── c_01_datos_simples.py
├── c_02_datos_compuestos.py
├── c_03_operadores_aritmeticos.py
├── c_04_operadores_comparacion.py
├── c_05_if_else.py
├── c_06_operadores_logicos.py
├── c_07_metodos_cadenas.py
├── c_08_metodos_listas.py
├── c_09_metodos_dict.py
├── c_10_inputs.py
├── c_11_ejercicio_practico.py
└── README.md
```

---

## Conceptos Clave Aprendidos

### Tipos de Datos
- ✅ Simples (str, int, float, bool)
- ✅ Compuestos (list, tuple, dict)

### Operadores
- ✅ Aritméticos (+, -, *, /, //, %, **)
- ✅ Comparación (==, !=, >, <, >=, <=)
- ✅ Lógicos (and, or, not)
- ✅ Pertenencia (in, not in)

### Control de Flujo
- ✅ Condicionales (if, elif, else)
- ✅ Bucles (for, while) - introducción

### Manejo de Datos
- ✅ Métodos de strings
- ✅ Métodos de listas
- ✅ Métodos de diccionarios

### Entrada/Salida
- ✅ Función `print()` para salida
- ✅ Función `input()` para entrada
- ✅ Conversión de tipos

---

## Recomendaciones

1. **Practicar:** Ejecuta cada archivo para ver los ejemplos en acción
2. **Experimentar:** Modifica los ejemplos y observa los resultados
3. **Desafíos:** Intenta resolver el ejercicio de la clase 11 con variaciones
4. **Próximos pasos:** Aprende sobre bucles (for, while), funciones, y programación orientada a objetos

---

## Autor

**soydalto** - Plataforma de educación en programación

---

## Duración Total

Contenido visto hasta la clase 10: **160 minutos (2 horas 40 minutos)**

---

*Última actualización: Febrero 2026*
