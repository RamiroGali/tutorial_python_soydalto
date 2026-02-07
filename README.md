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

### Clase 11: Ejercicio Práctico 1 (`c_11_ejercicio_practico1.py`)
- Programa interactivo de comparación de duraciones de cursos
- Ingreso múltiple de datos con bucles
- Comparación de valores
- Cálculo de estadísticas (promedio, máximo, mínimo)
- Formateo de salida
- Uso de diccionarios para almacenar datos

---

### Clase 12: Ejercicio Práctico 2 (`c_12_ejercicio_practico2.py`)
- Análisis de frases ingresadas por el usuario
- Cálculo de cantidad de palabras usando `split()`
- Estimación de tiempo de duración al hablar
- Aplicación de conversiones y operaciones aritméticas

### Clase 13: Variables y Desempaquetado (`c_13_variables_desempaquetado.py`)
- Desempaquetado (unpacking) de listas y tuplas
- Asignación múltiple de variables
- Conversión entre tipos con `tuple()` y `list()`

### Clase 14: Conjuntos (`c_14_conjunto.py`)
- Conceptos de `set` y `frozenset` (inmutable)
- Creación de conjuntos a partir de otras colecciones
- Operaciones de teoría de conjuntos:
  - **Subconjuntos:** `issubset()` y operador `<=`
  - **Superconjuntos:** `issuperset()` y operador `>=`
  - **Intersección:** `&` (elementos comunes)
  - **Elementos disjuntos:** `isdisjoint()`

### Clase 15: Diccionarios (avanzado) (`c_15_diccionarios.py`)
- Creación de diccionarios con `{}`, `dict()`, `zip()`, y `fromkeys()`
- Tuplas como claves de diccionarios
- `frozenset` como claves (para representar listas de forma inmutable)
- Ejemplos prácticos de diccionarios complejos

### Clase 16: Ciclos y Bucles (`c_16_ciclos_bucles.py`)
- Bucle `for` para iterar sobre secuencias
- Bucle `while` con condiciones
- Funciones de utilidad: `range()`, `zip()`, `enumerate()`
- Cláusula `for/else` (se ejecuta si no hay `break`)

### Clase 17: Recorrer conjuntos (`c_17_recorrer_conjuntos.py`)
- Características especiales de los `set` (no ordenados, únicos)
- Recorrer sets con `for`
- Conversión a `list` para obtener índices con `enumerate()`
- Usar `sorted()` para ordenar al recorrer
- Transformaciones durante el recorrido

### Clase 18: Recorrer diccionarios (`c_18_recorrer_diccionarios.py`)
- Recorrer solo claves con `for clave in dict`
- Recorrer valores con `.values()`
- Recorrer pares clave-valor con `.items()`
- Diccionarios anidados y detección de tipos con `isinstance()`
- Control de flujo: `continue` dentro de bucles `for`
- Control de flujo: `break` para detener iteraciones

### Clase 19: Métodos de Listas (`c_19_metodos_list.py`)
- Métodos mutables: `append()`, `insert()`, `remove()`
- Manipulación de listas con bucles `for` y `while`
- **List comprehension:** Creación de listas con sintaxis compacta
- Transformaciones: Duplicar, filtrar, y procesar elementos

### Clase 20: Funciones (`c_20_funciones.py`)
- Conceptos básicos de funciones con `def`
- Parámetros y valores de retorno
- Funciones built-in: `min()`, `max()`, `round()`, `bool()`, `all()`
- Definición y uso de funciones personalizadas
- Ejemplo práctico: Generador de contraseñas

### Clase 21: Funciones con *args y **kwargs (`c_21_funciones_parametros_args.py`)
- **`*args`:** Número variable de argumentos posicionales
- **`**kwargs`:** Número variable de argumentos nombrados (clave=valor)
- Diferencia entre pasar listas vs usar `*args`
- Iteración sobre `kwargs` con `.items()`

### Clase 22: Funciones con parámetros por defecto (`c_22_funciones_datos_extra.py`)
- Parámetros con valores por defecto
- Argumentos nombrados (named arguments)
- Orden flexible en llamadas a funciones

### Clase 23: Funciones Lambda (`c_23_funciones_lambda.py`)
- Definición de funciones anónimas con `lambda`
- Uso con `filter()` para filtrar elementos
- Uso con `map()` para transformar elementos
- Limitaciones: Una sola expresión, sin múltiples líneas
- Funciones de orden superior (higher-order functions)

### Clase 24: Ejercicio Práctico 3 (`c_24_ejercicio_practico1.py`)
- Ejercicios integradores de conceptos previos
- Aplicación de funciones y estructuras de datos

### Clase 25: Ejercicio Práctico 4 (`c_25_ejercicio_practico2.py`)
- Ejercicios avanzados de consolidación
- Combinación de múltiples conceptos

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
├── c_11_ejercicio_practico1.py
├── c_12_ejercicio_practico2.py
├── c_13_variables_desempaquetado.py
├── c_14_conjunto.py
├── c_15_diccionarios.py
├── c_16_ciclos_bucles.py
├── c_17_recorrer_conjuntos.py
├── c_18_recorrer_diccionarios.py
├── c_19_metodos_list.py
├── c_20_funciones.py
├── c_21_funciones_parametros_args.py
├── c_22_funciones_datos_extra.py
├── c_23_funciones_lambda.py
├── c_24_ejercicio_practico1.py
├── c_25_ejercicio_practico2.py
└── README.md
```
---

---

## Conceptos Clave Aprendidos

### Tipos de Datos
- ✅ Simples: `str`, `int`, `float`, `bool`
- ✅ Compuestos: `list`, `tuple`, `dict`, `set`, `frozenset`
- ✅ Desempaquetado (unpacking) de colecciones

### Operadores
- ✅ Aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- ✅ Comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
- ✅ Lógicos: `and`, `or`, `not`
- ✅ Pertenencia: `in`, `not in`
- ✅ Teoría de conjuntos: `<=` (subconjunto), `>=` (superconjunto), `&` (intersección)

### Control de Flujo
- ✅ Condicionales: `if`, `elif`, `else`
- ✅ Bucles: `for`, `while`, `for/else`
- ✅ Control: `break`, `continue`

### Manejo de Datos
- ✅ Métodos de strings: `upper()`, `lower()`, `capitalize()`, `split()`, `join()`, etc.
- ✅ Métodos de listas: `append()`, `remove()`, `insert()`, `pop()`, `sort()`, etc.
- ✅ Métodos de diccionarios: `keys()`, `values()`, `items()`, `get()`, `update()`, etc.
- ✅ Recorrido de conjuntos y diccionarios con `for`
- ✅ List comprehension para crear listas de forma compacta

### Funciones
- ✅ Definición de funciones con `def`
- ✅ Parámetros y valores de retorno
- ✅ Funciones built-in: `min()`, `max()`, `round()`, `len()`, `sorted()`, etc.
- ✅ `*args` para múltiples argumentos posicionales
- ✅ `**kwargs` para múltiples argumentos nombrados
- ✅ Parámetros con valores por defecto
- ✅ Funciones lambda (anónimas) con `lambda`
- ✅ Funciones de orden superior: `map()`, `filter()`

### Entrada/Salida
- ✅ Función `print()` para salida
- ✅ Función `input()` para entrada
- ✅ Conversión de tipos: `int()`, `float()`, `str()`, `tuple()`, `list()`, `set()`, `dict()`

### Estructuras de Datos Avanzadas
- ✅ Diccionarios anidados
- ✅ Frozensets como claves de diccionarios
- ✅ Operaciones de teoría de conjuntos

---

## Recomendaciones

1. **Practicar:** Ejecuta cada archivo para ver los ejemplos en acción
2. **Experimentar:** Modifica los ejemplos y observa los resultados
3. **Desafíos:** Intenta resolver los ejercicios prácticos (clases 11, 12, 24, 25) con variaciones propias
4. **Explorar funciones:** Crea tus propias funciones y experimenta con `*args`, `**kwargs`, y lambda
5. **Próximos pasos:** Aprende sobre programación orientada a objetos (clases y objetos), manejo de archivos, librerías (NumPy, Pandas, Matplotlib), y desarrollo web

---

## Autor

**soydalto** - Plataforma de educación en programación

---

## Duración Total

Contenido visto hasta la clase 10: **160 minutos (2 horas 40 minutos)**

Clases adicionales incluidas: **25 clases en total**

El curso completo desde la clase 1 a la 25 incluye:
- Fundamentos de Python (clases 1-10): 160 minutos
- Estructuras de datos avanzadas (clases 11-18): Conjuntos, diccionarios, y técnicas de recorrido
- Funciones y programación funcional (clases 19-25): Métodos de listas, funciones, argumentos variables, y funciones lambda

---
## GitHub

Comandos empleados para subir el repositorio en https://github.com/RamiroGali/tutorial_python_soydalto.git:

```batch
gh auth login;
gh create tutorial_python_soydalto --public --source=. --remote=origin --push;
```

*Última actualización: Febrero 2026*
