🌳 Comparación de Búsqueda Espacial: Fuerza Bruta vs Quadtree

Este proyecto implementa y compara dos métodos para realizar búsquedas espaciales en 2D:

🔴 Fuerza Bruta
🌳 Quadtree (estructura jerárquica optimizada)

El objetivo es analizar rendimiento y eficiencia al buscar puntos dentro de un radio y encontrar el punto más cercano.

📌 Descripción del Problema

Dado un conjunto de puntos en 2D:

Encontrar todos los puntos dentro de un radio específico
Encontrar el punto más cercano a una consulta

Se comparan dos enfoques:

Método	Descripción
Fuerza Bruta	Revisa todos los puntos
Quadtree	Divide el espacio recursivamente para optimizar la búsqueda
⚙️ Tecnologías utilizadas
Python 🐍
Librerías:
random
math
matplotlib
time
🧠 ¿Cómo funciona?
🔴 Fuerza Bruta
Recorre todos los puntos
Calcula la distancia uno por uno
Complejidad: O(n)
🌳 Quadtree
Divide el espacio en 4 regiones (cuadrantes)
Solo explora zonas relevantes
Usa poda espacial (intersección con círculo)
Complejidad promedio: O(log n)
📊 Funcionalidades del código

✔️ Generación de puntos aleatorios
✔️ Búsqueda por radio
✔️ Búsqueda del punto más cercano
✔️ Comparación de tiempos
✔️ Visualización gráfica
✔️ Análisis de rendimiento con distintos tamaños

📈 Visualizaciones
1. Visualización general
Puntos dentro y fuera del radio
Punto de consulta
Punto más cercano
Círculo de búsqueda
2. Visualización acotada (zoom)
Enfoque en la zona de interés
Mejor visualización de los puntos cercanos
3. Gráfica de rendimiento
Comparación de tiempos entre:
Fuerza Bruta
Quadtree
🚀 Ejecución
Clona el repositorio:
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
Ejecuta el script:
python nombre_del_archivo.py
📊 Resultados esperados
Para pocos puntos:
✅ Fuerza Bruta puede ser más rápida (menos overhead)
Para muchos puntos:
✅ Quadtree es significativamente más eficiente
🧪 Análisis de rendimiento

El programa evalúa diferentes tamaños de datos:

tamaños = [5, 50, 100, 300, 600, 1000, 2000, 5000, 10000]

Para cada tamaño:

Ejecuta múltiples pruebas
Promedia tiempos
Determina el método ganador
📌 Conceptos clave implementados
Estructuras de datos espaciales
Subdivisión recursiva
Poda por intersección
Búsqueda por rango
Complejidad algorítmica
🧾 Estructura del código
Generación de datos
Función de distancia
Implementación de Fuerza Bruta
Implementación de Quadtree:
Rectangulo
Quadtree
Visualización
Benchmark de rendimiento
🎯 Conclusión

El Quadtree demuestra ser una solución mucho más eficiente para grandes volúmenes de datos espaciales, reduciendo significativamente el tiempo de búsqueda al evitar evaluaciones innecesarias.

👨‍💻 Autor

Proyecto desarrollado como práctica de estructuras de datos espaciales y análisis de algoritmos.
