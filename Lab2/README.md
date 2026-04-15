# 📊 Análisis de Búsqueda Espacial: Fuerza Bruta vs KD-Tree

## 📌 Descripción del Proyecto

Este proyecto tiene como objetivo comparar dos métodos para realizar búsquedas espaciales en un conjunto de puntos en 2 dimensiones:

- 🔍 **Fuerza Bruta**
- 🌳 **KD-Tree (implementación manual)**

Se analiza su comportamiento en términos de:
- Tiempo de ejecución
- Escalabilidad
- Eficiencia según el tamaño del conjunto de datos

---

## 🎯 Problema

Dado un conjunto de puntos en un espacio 2D, se busca:

1. Encontrar todos los puntos dentro de un radio determinado desde un punto de consulta.
2. Identificar el punto más cercano al punto de consulta.
3. Comparar el rendimiento entre dos enfoques:
   - Fuerza bruta (revisión de todos los puntos)
   - KD-Tree (estructura espacial)

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Librerías estándar:
  - `random`
  - `math`
  - `time`
  - `statistics`
- Visualización:
  - `matplotlib`

❌ No se utilizó `scipy` ni implementaciones externas de árboles.

---

## 🧠 Métodos implementados

### 🔹 Fuerza Bruta

- Recorre todos los puntos
- Calcula distancia a cada uno
- Complejidad: **O(n)**

✔ Ventajas:
- Simple de implementar
- Eficiente en conjuntos pequeños

❌ Desventajas:
- No escala bien

---

### 🌳 KD-Tree

- Divide el espacio recursivamente
- Usa la **mediana estadística** para balancear el árbol
- Reduce el número de comparaciones

✔ Ventajas:
- Mucho más eficiente en grandes volúmenes de datos
- Permite poda del espacio de búsqueda

❌ Desventajas:
- Mayor complejidad de implementación
- Overhead en conjuntos pequeños

---

## 📊 Análisis de rendimiento

Se evaluaron los siguientes tamaños de datos:


5, 50, 100, 300, 600, 1000, 2000, 5000, 10000


Para cada tamaño:
- Se ejecutaron múltiples pruebas
- Se calculó el tiempo promedio
- Se compararon ambos métodos

---

## 📈 Resultados

### 🔍 Observaciones

- Para conjuntos pequeños:
  - La **fuerza bruta es más rápida**
  - Debido a menor sobrecarga

- Para conjuntos grandes:
  - El **KD-Tree es más eficiente**
  - Reduce comparaciones innecesarias

- Punto de cambio:
  - Aproximadamente entre **500 y 2000 puntos**
  - Depende de la distribución de datos

---

## 📉 Visualizaciones

El proyecto incluye:

- 📍 Visualización general de los puntos
- 🔎 Visualización acotada (zoom)
- 📊 Gráfica de comparación de tiempos

Estas ayudan a entender:
- Distribución de datos
- Funcionamiento de los algoritmos
- Diferencias de rendimiento

---

## 🧾 Estructura del código

El código está organizado en secciones:

Configuración del problema
Cálculo de distancia
Búsqueda por fuerza bruta
Visualizaciones
Implementación de KD-Tree
Búsqueda en KD-Tree
Análisis de rendimiento
Discusión de resultados
Gráfica final

---

## 🧪 Cómo ejecutar

1. Abrir el notebook en:
   - Google Colab o Jupyter Notebook

2. Ejecutar todas las celdas en orden:

Runtime → Run all


3. Observar:
- Resultados en consola
- Gráficas generadas

---

## 📌 Conclusiones

- La **fuerza bruta** es adecuada para problemas pequeños.
- El **KD-Tree** es más eficiente para grandes volúmenes de datos.
- La elección del método depende del tamaño del dataset.

---

## 🎓 Aplicaciones

Este tipo de algoritmos se usa en:

- Sistemas de geolocalización 📍
- Motores de búsqueda espacial 🔍
- Videojuegos 🎮
- Machine Learning 🤖
- Sistemas GIS 🌍

---

## 👨‍💻 Autor

Proyecto académico – Análisis de estructuras de datos espaciales.

---

## 🚀 Posibles mejoras

- Implementar búsqueda del vecino más cercano optimizada
- Extender a más dimensiones (k > 2)
- Optimizar distancia (evitar raíz cuadrada)
- Comparar con estructuras avanzadas (Ball Tree, R-Tree)

---
