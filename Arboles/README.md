📊 Comparación de Métodos de Búsqueda

Este ejercicio consiste en comparar el tiempo de búsqueda de estudiantes utilizando tres estructuras de datos diferentes:

Lista secuencial

Árbol Binario de Búsqueda (ABB)

Índice tipo B+ Tree (simulado con búsqueda binaria)

El objetivo es analizar el rendimiento de cada estructura cuando se realizan muchas búsquedas sobre una colección de datos.

🎯 Objetivo del ejercicio

Simular un sistema que almacena información de estudiantes y comparar qué tan rápido se puede encontrar un estudiante usando distintas estructuras de datos.

Cada estudiante tiene:

id → identificador único

nombre → nombre del estudiante

promedio → promedio académico

Se generan 10,000 estudiantes y luego se realizan múltiples búsquedas para medir el tiempo de ejecución.

🧠 Estructuras de datos comparadas
1️⃣ Lista

Es la estructura más simple.

Para encontrar un estudiante se revisa uno por uno hasta encontrar el ID buscado.

Complejidad aproximada:

O(n)

Esto significa que mientras más datos haya, más lenta será la búsqueda.

2️⃣ Árbol Binario de Búsqueda (ABB)

Los estudiantes se organizan en forma de árbol.

Reglas del árbol:

IDs menores van a la izquierda

IDs mayores van a la derecha

Esto permite reducir la cantidad de comparaciones necesarias.

Complejidad aproximada:

O(log n)

Sin embargo, si los datos se insertan ordenados, el árbol puede degenerarse y comportarse como una lista.

3️⃣ Índice B+ (simulado)

Los B+ Trees son estructuras utilizadas en bases de datos reales para acelerar búsquedas.

En este ejercicio se simulan usando:

una lista ordenada

búsqueda binaria (bisect)

Complejidad aproximada:

O(log n)

En sistemas reales, los B+ Trees son muy eficientes porque:

mantienen el árbol balanceado

optimizan accesos a disco

permiten búsquedas rápidas incluso con millones de registros

⚙️ Funcionamiento del programa

El programa realiza los siguientes pasos:

1️⃣ Genera 10,000 estudiantes.

2️⃣ Se crean dos escenarios:

IDs ordenados

IDs aleatorios

3️⃣ Se construyen las estructuras de datos:

lista

ABB

índice B+

4️⃣ Se realizan búsquedas de diferentes tamaños:

100

1,000

2,000

5,000

7,000

10,000

5️⃣ Se mide el tiempo real de ejecución utilizando:

time.perf_counter()
⏱️ Qué mide el experimento

El programa mide cuánto tiempo tardan las estructuras en encontrar estudiantes cuando se realizan muchas consultas.

Se comparan:

tiempo de búsqueda en lista

tiempo de búsqueda en ABB

tiempo de búsqueda en índice B+

Esto permite analizar qué estructura escala mejor cuando aumenta el número de búsquedas.

▶️ Cómo ejecutar el programa

1️⃣ Asegúrate de tener Python 3 instalado

2️⃣ Ejecuta el archivo:

python busqueda_estudiantes.py

3️⃣ El programa mostrará en consola algo como:

PRUEBA CON IDS EN ORDEN

100 búsquedas
Lista: 0.00123 segundos
ABB: 0.00054 segundos
B+: 0.00032 segundos
📚 Conceptos aprendidos

Este ejercicio permite practicar conceptos importantes de:

estructuras de datos

análisis de algoritmos

complejidad computacional

medición de rendimiento

árboles binarios

índices utilizados en bases de datos

📁 Archivo incluido
ARBOLES3.py

Script que implementa:

generación de estudiantes

estructuras de búsqueda

medición de tiempos de búsqueda 

👨‍💻 Autor: Santiago Rendón Rivera

Estudiante de Ingeniería de Sistemas.

Repositorio utilizado para subir trabajos académicos y ejercicios de programación, desarrollados usando vibe coding como metodología de aprendizaje.
