¡Claro! Aquí tienes un **README.md bonito, bien estructurado y profesional** para tu colección de ejercicios de Python, con emojis, secciones claras, y un diseño atractivo para GitHub o cualquier repositorio.

---

# 🐍 Guía Completa de Ejercicios de Python

> ✨ Una colección estructurada y didáctica de ejercicios de programación en Python, desde fundamentos hasta estructuras avanzadas como generadores y diccionarios.

---

## 📚 Contenido

- [📌 Introducción](#-introducción)
- [🧩 Ejercicios por Tema](#-ejercicios-por-tema)
  - [1. Funciones y Depuración](#1-funciones-y-depuración)
  - [2. Ciclos Definidos](#2-ciclos-definidos)
  - [3. Decisiones y Geometría](#3-decisiones-y-geometría)
  - [4. Problemas de Decisión](#4-problemas-de-decisión)
  - [5. Ciclos Indefinidos y Algoritmos](#5-ciclos-indefinidos-y-algoritmos)
  - [6. Cadenas de Caracteres](#6-cadenas-de-caracteres)
  - [7. Tuplas y Listas](#7-tuplas-y-listas)
  - [8. Diccionarios](#8-diccionarios)
  - [9. Generadores](#9-generadores)
- [🚀 Ejecución](#-ejecución)
- [💡 Consejos](#-consejos)
- [📜 Licencia](#-licencia)

---

## 📌 Introducción

Este repositorio contiene una **guía completa de ejercicios de Python**, diseñada para reforzar conceptos fundamentales y avanzados de programación. Cada sección aborda un tema específico, con ejercicios progresivos que te ayudarán a dominar Python paso a paso.

Incluye desde funciones básicas hasta algoritmos matemáticos, manipulación de cadenas, estructuras de datos, y generadores.

---

## 🧩 Ejercicios por Tema

---

### 1. Funciones y Depuración

```python
def potencia():
    print("Calcularanse potencia de dous números")
    n1 = input("Ingrese un número enteiro: ")
    n2 = input("Ingrese outro número enteiro: ")
    for x in range(int(n1), int(n2)):
        print(x*x)
    print("É todo por agora")
```

#### ✍️ Ejercicios:
- **1.1** Ejecutar con (3,5), (3,3), (5,3). ¿Qué ocurre?
- **1.2** Insertar depuración para ver el valor de `x`.
- **1.3** Mejorar salida con `num_cadrados(x)`.
- **1.4** Hacer la salida aún más clara.
- **1.5** Función que salude al usuario y calcule el producto de dos números.
- **1.6** Implementar funciones para:
  - Área y perímetro de rectángulo.
  - Área y perímetro de círculo.
  - Volumen de esfera.
  - Área de rectángulo por coordenadas.
  - Hipotenusa de triángulo rectángulo.
- **1.7** Analizar bloques de código en intérprete.
- **1.8** Implementar:
  - Operaciones básicas entre dos números.
  - Tabla de multiplicar de N.
  - Factorial de N.
- **1.9** Imprimir una palabra 1000 veces con espacios.

---

### 2. Ciclos Definidos

#### ✍️ Ejercicios:
- **2.1** Ciclos para imprimir números 10-20, saludar a 5 amigos, preguntar nombres y saludar.
- **2.2** Calcular interés compuesto:  
  `Cn = C * (1 + x/100)^n`
- **2.3** Convertir Fahrenheit a Celsius: `F = 9/5 * C + 32`
- **2.4** Generar tabla de conversión de 0°F a 120°F.
- **2.5** Imprimir números pares entre dos números dados.
- **2.6** Imprimir primeros N números triangulares (con y sin fórmula).
- **2.7** Calcular factorial de M números ingresados.
- **2.8** Imprimir todas las fichas de dominó sin repetir.
- **2.9** Generalizar dominó para números de 0 a N.

---

### 3. Decisiones y Geometría

#### ✍️ Ejercicios:
- **3.1** Convertir entre segundos ↔ horas:minutos:segundos.
- **3.2** Sumar dos tiempos expresados en h:m:s.
- **3.3** Mayor producto entre 4 números.
- **3.4** Geometría vectorial y áreas:
  - Norma de vector.
  - Resta de puntos.
  - Distancia entre puntos.
  - Vector unitario.
  - Proyección sobre recta.
  - Área de triángulo por base y altura.
  - Área de triángulo por 3 puntos.

---

### 4. Problemas de Decisión

#### ✍️ Ejercicio:
- **4.1** Leer un número y mostrar "Número positivo" si > 0.

---

### 5. Ciclos Indefinidos y Algoritmos

#### ✍️ Ejercicios:
- **5.1** Ingresar notas hasta que el usuario decida, luego mostrar promedio.
- **5.2** Descomposición en factores primos.
- **5.3** Manejo de contraseñas:
  - Pedir hasta acertar.
  - Limitar intentos.
  - Añadir pausas crecientes (`time.sleep`).
  - Devolver `True/False` si se acertó.
- **5.4** Juego de adivinar número aleatorio.
- **5.5** Algoritmo de Euclides para MCD.
- **5.6** Potencias de 2:
  - Verificar si un número es potencia de 2.
  - Sumar potencias de 2 en un rango.
- **5.7** Números perfectos y amigos:
  - Suma de divisores.
  - Encontrar primeros M números perfectos.
  - Encontrar primeras M parejas de números amigos.
- **5.8** Leer números hasta -1, mostrar total, suma y promedio.
- **5.9** Contar múltiplos de un número menores que otro (con `for` y `while`).
- **5.10** Imprimir todos los primos hasta N.
- **5.11** Verificar si un dígito está en un número.
- **5.12** Revisión de exámenes: calcular porcentaje y si aprueba.

---

### 6. Cadenas de Caracteres

#### ✍️ Ejercicios:
- **6.1** Manipulación básica: primeros 2, últimos 3, cada 2 caracteres, inverso, espejo.
- **6.2** Insertar/reemplazar caracteres:
  - Entre letras.
  - Espacios → `_`.
  - Dígitos → `X`.
  - Cada 3 dígitos → insertar `.`.
- **6.3** Limitar cantidad de reemplazos/insertados.
- **6.4** Formatear número con separadores de miles: `1234567890` → `1.234.567.890`.
- **6.5** Procesar palabras:
  - Iniciales → "USB".
  - Capitalizar cada palabra.
  - Palabras que empiezan con "A".
- **6.6** Procesar vocales y consonantes:
  - Solo consonantes.
  - Solo vocales.
  - Reemplazar vocales por la siguiente.
  - Detectar palíndromos.
- **6.7** Comparar cadenas:
  - ¿Es subcadena?
  - ¿Cuál es alfabéticamente anterior?
- **6.8** Convertir binario a decimal.

---

### 7. Tuplas y Listas

#### ✍️ Ejercicios:
- **7.1** Verificar si tupla está ordenada.
- **7.2** Dominó: encajan fichas (como tuplas o como strings "3-4").
- **7.3** Campaña electoral: saludar por nombre, con género, desde posición P.
- **7.4** Vectores:
  - Producto escalar.
  - ¿Ortogonales?
  - ¿Paralelos?
  - Norma.
- **7.5** Filtrar lista de enteros:
  - Números primos.
  - Suma y promedio.
  - Factorial de cada uno.
- **7.6** Dada lista y valor K:
  - Listas de menores, mayores, iguales.
  - Múltiplos de K.
- **7.7** Formatear nombres: `[(Apellido, Nombre, Inicial, DNI)]` → `"Nombre I. Apellido"`.
- **7.8** Inversión de listas:
  - Devolver nueva lista invertida.
  - Invertir in-place.
- **7.9** Empaquetar: `[1,1,1,3,5,1,1,3,3]` → `[(1,3), (3,1), (5,1), (1,2), (3,2)]`.
- **7.10** Matrices:
  - Suma.
  - Producto.
  - Eliminación gaussiana → triangular superior.
  - ¿Vectores linealmente independientes?
- **7.11** Plegado de texto: ajustar líneas sin cortar palabras.
- **7.12** Funciones de orden superior:
  - `mapeado(función, lista)`.
  - `filtro(función, lista)`.
  - ¿En qué ejercicios se podrían usar?

---

### 8. Diccionarios

#### ✍️ Ejercicios:
- **8.1** Convertir lista de tuplas → diccionario:  
  `[('Hola','Pepito'), ('Hola','Jose')]` → `{'Hola': ['Pepito','Jose']}`
- **8.2** Contar apariciones:
  - Palabras en texto.
  - Caracteres en texto.
  - Sumas de tiradas de 2 dados (usar `random`).
- **8.3** Agenda telefónica:
  - Buscar nombre → mostrar/modificar teléfono.
  - Si no existe → agregar.
  - Salir con `*`.
- **8.4** Para cada carácter, devolver la palabra más larga donde aparece.

---

### 9. Generadores

#### ✍️ Ejercicios:
- **9.1** `generar_pares(n)` → números pares de 0 a n.
- **9.2** Generador que lee un archivo y devuelve una palabra por vez.
- **9.3** Generador de primeros N números de Fibonacci.
- **9.4** Generador de primos entre n y m.
- **9.5** Generador que omite los primeros N elementos de un iterable.

---

## 🚀 Ejecución

Cada ejercicio puede implementarse en archivos `.py` separados o en un solo archivo modular.

```bash
python ejercicio_X_Y.py
```

