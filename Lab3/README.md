🔍 Comparación de Métodos de Búsqueda Espacial
Fuerza Bruta vs Quadtree
📌 Descripción

Este proyecto implementa y compara dos enfoques para resolver problemas de búsqueda espacial en 2D:

Fuerza Bruta
Quadtree

El objetivo es analizar su rendimiento al encontrar puntos dentro de un radio determinado y evaluar cuál es más eficiente dependiendo del tamaño de los datos.

🧠 Conceptos Clave
🔹 Fuerza Bruta

Consiste en recorrer todos los puntos y calcular su distancia respecto a un punto de consulta.

✔ Fácil de implementar
❌ Poco eficiente con grandes volúmenes de datos
🔹 Quadtree

Estructura de datos jerárquica que divide el espacio en cuatro cuadrantes recursivamente.

✔ Reduce el número de comparaciones
✔ Ideal para datos espaciales en 2D
❌ Tiene overhead inicial
⚙️ Funcionalidades del Proyecto
Generación de puntos aleatorios en 2D
Cálculo de:
Puntos dentro de un radio
Punto más cercano
Visualización gráfica:
Vista general
Vista acotada con zoom
Implementación completa de Quadtree:
Inserción de puntos
Búsqueda por rango circular
Análisis de rendimiento comparativo
Gráfica final de tiempos de ejecución
📊 Análisis de Rendimiento

Se evalúan distintos tamaños de datos:

[5, 50, 100, 300, 600, 1000, 2000, 5000, 10000]

Para cada tamaño se mide:

Tiempo promedio usando Fuerza Bruta
Tiempo promedio usando Quadtree
📈 Resultados Esperados
🔸 Tamaños pequeños
La fuerza bruta suele ser más rápida
El Quadtree tiene overhead por subdivisiones
🔸 Tamaños grandes
El Quadtree se vuelve más eficiente
Reduce búsquedas innecesarias en el espacio
🔸 Punto de cambio
Generalmente entre 500 y 2000 puntos
Depende de la distribución de los datos
📌 Conclusión

El Quadtree es más escalable y eficiente en problemas espaciales en 2D, especialmente cuando se realizan múltiples consultas por región.

La fuerza bruta sigue siendo útil en casos pequeños por su simplicidad.

🖼️ Visualizaciones

El programa genera:

Distribución de puntos
Puntos dentro del radio
Punto de consulta
Punto más cercano
Círculo de búsqueda
🛠️ Requisitos
Python 3.x
Librerías:
pip install matplotlib
▶️ Ejecución

Simplemente ejecuta el archivo:

python nombre_del_archivo.py
📂 Estructura del Código
Configuración inicial
Función de distancia
Método de fuerza bruta
Visualización
Implementación de Quadtree:
Clase Rectangulo
Clase Quadtree
Análisis de rendimiento
Gráfica final
🚀 Posibles Mejoras
Implementar búsqueda de vecino más cercano con Quadtree
Optimizar la capacidad de los nodos
Añadir visualización del árbol (subdivisiones)
Comparar con otras estructuras (KD-Tree, R-Tree)
📚 Aplicaciones Reales
Videojuegos (detección de colisiones)
Sistemas GIS (mapas)
Simulaciones físicas
Motores gráficos
👨‍💻 Autor

Proyecto académico orientado al análisis de estructuras de datos espaciales.
