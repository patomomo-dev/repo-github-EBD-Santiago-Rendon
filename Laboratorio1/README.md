# 🔐 Cryptography Brute Force Exercises

Este repositorio contiene soluciones a dos problemas clásicos relacionados con criptografía:

* Inversión de hash con SHA-256
* Reconstrucción de orden en un árbol de Merkle

Ambos problemas están diseñados para demostrar conceptos fundamentales como funciones hash y estructuras criptográficas.

---

# 📌 Problema 1: Invertir un hash SHA-256

## 🧩 Enunciado

Dado un hash generado con SHA-256, encontrar la secuencia de números que lo produce.

### Reglas:

* La secuencia consiste en 10 dígitos
* Cada dígito está en el rango `[0-9]`
* Se concatenan para formar un número (ej: `1234567890`)

---

## ⚠️ Observación clave (truco)

Aunque el problema parece implicar:

10¹⁰ combinaciones posibles

En realidad, el código usa:

* Permutaciones sin repetición de los dígitos `0–9`

Por lo tanto, el espacio real es:

10! = 3,628,800 combinaciones

👉 Esto hace que el problema sea resoluble en tiempo razonable.

---

## ⚙️ Estrategia

Se utiliza un enfoque de **fuerza bruta probabilística**:

1. Generar una permutación aleatoria
2. Calcular su hash usando SHA-256
3. Comparar con el hash objetivo
4. Repetir hasta encontrar coincidencia

---

## 🧪 Código relevante

* `hash(l)` → genera una secuencia aleatoria y su hash
* `unhash(l)` → intenta encontrar la secuencia original

---

## 🔐 Concepto clave

* SHA-256 es una función hash criptográfica segura
* No es reversible, por lo que se usa fuerza bruta

---

# 🌳 Problema 2: Árbol de Merkle

## 🧩 Enunciado

Dado el hash raíz (root) de un árbol de Merkle, determinar el orden correcto de las transacciones.

### Reglas:

* Las transacciones son conocidas
* El número de transacciones también
* El orden es desconocido

---

## ⚠️ Observación clave

El hash raíz de un árbol de Merkle depende del orden de las transacciones.

Cambiar el orden ⇒ cambia completamente el root

---

## ⚙️ Estrategia

Se utiliza fuerza bruta con permutaciones:

1. Reordenar aleatoriamente las transacciones
2. Calcular el Merkle root
3. Comparar con el objetivo
4. Repetir hasta encontrar coincidencia

---

## 🧪 Código relevante

* `calcular_merkle_root(transacciones)` → calcula el root
* `resolver_merkle_fuerza_bruta(...)` → busca el orden correcto

---

## 🌲 Concepto clave

Un árbol de Merkle es una estructura donde:

* Las hojas son hashes de datos
* Los nodos internos son hashes de combinaciones

Esto permite verificar integridad de datos de forma eficiente.

---

# 🚀 Limitaciones

## Problema 1

* Aunque reducido, sigue siendo costoso
* El método aleatorio puede repetir intentos

## Problema 2

* Complejidad factorial: n!
* Escala muy mal con más transacciones

---

# 💡 Posibles mejoras

* Usar permutaciones en lugar de aleatoriedad
* Paralelizar con multiprocessing
* Usar hashes en formato binario (más rápido)
* Evitar recomputar hashes innecesarios

---

# 📂 Estructura sugerida

```
.
├── sha256_bruteforce.py
├── merkle_bruteforce.py
└── README.md
```

---

# 🎯 Objetivo del proyecto

Este proyecto no busca eficiencia extrema, sino:

* Entender cómo funcionan los hashes
* Comprender la dificultad de invertir funciones criptográficas
* Experimentar con fuerza bruta y complejidad computacional

---

# ⚠️ Nota final

Estos ejercicios reflejan por qué:

* Las funciones hash son seguras
* Las estructuras como Merkle trees son fundamentales en sistemas como blockchain

---

# 👨‍💻 Autor

Proyecto educativo sobre criptografía y algoritmos de búsqueda.
