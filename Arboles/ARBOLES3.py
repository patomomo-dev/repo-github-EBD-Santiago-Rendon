# =========================================================
# IMPORTACIÓN DE LIBRERÍAS
# =========================================================

"""
Las librerías son herramientas que ya vienen programadas en Python
y que nos ayudan a realizar ciertas tareas sin tener que programarlas
desde cero.
"""

# random: se utiliza para generar valores aleatorios
# (por ejemplo nombres o números de identificación)
import random

# bisect_left: permite realizar búsquedas binarias en listas ordenadas.
# La búsqueda binaria es un método muy rápido para encontrar datos.
from bisect import bisect_left

# math: contiene funciones matemáticas útiles como log2
import math


# =========================================================
# CONFIGURACIÓN INICIAL
# =========================================================

"""
Aquí se definen algunas variables iniciales del programa.
"""

# Número total de estudiantes que se van a generar para el experimento
N = 10000

# Lista de nombres posibles que se asignarán aleatoriamente a los estudiantes
nombres = ["Ana", "Carlos", "Maria", "Luis", "Pedro", "Sofia", "Laura", "Juan"]


# =========================================================
# GENERAR ESTUDIANTES
# =========================================================

"""
En esta sección se crean estudiantes ficticios.

Cada estudiante es representado como un pequeño registro
que contiene:

- id: número único que identifica al estudiante
- nombre: nombre elegido al azar
- promedio: nota promedio entre 3.0 y 5.0
"""


def generar_estudiantes_ordenados(n):

    """
    Esta función genera estudiantes cuyos IDs están en orden.

    Ejemplo:
    0, 1, 2, 3, 4, 5, ...

    Parámetro:
    n → cantidad de estudiantes que se quieren generar.

    Retorna:
    Una lista con n estudiantes.
    """

    estudiantes = [
        {
            "id": i,  # ID consecutivo
            "nombre": random.choice(nombres),  # nombre aleatorio
            "promedio": round(random.uniform(3.0, 5.0), 2)  # promedio aleatorio
        }
        for i in range(n)
    ]

    return estudiantes


def generar_estudiantes_aleatorios(n):

    """
    Esta función genera estudiantes con IDs completamente aleatorios.

    Esto simula una base de datos más realista donde
    los identificadores no están necesariamente ordenados.
    """

    estudiantes = [
        {
            "id": random.randint(1000, 99999),  # ID aleatorio
            "nombre": random.choice(nombres),
            "promedio": round(random.uniform(3.0, 5.0), 2)
        }
        for _ in range(n)
    ]

    return estudiantes


# =========================================================
# BÚSQUEDA EN LISTA
# =========================================================

"""
Este es el método de búsqueda más sencillo.

El programa revisa cada estudiante uno por uno
hasta encontrar el que tiene el ID buscado.

Si el estudiante está al final de la lista,
el programa tendrá que revisar todos los anteriores primero.

Por eso este método puede ser lento cuando
hay muchos datos.
"""


def buscar_lista(lista, id_buscar):

    for e in lista:
        if e["id"] == id_buscar:
            return e

    return None


# =========================================================
# ÁRBOL BINARIO DE BÚSQUEDA (ABB)
# =========================================================

"""
Un Árbol Binario de Búsqueda (ABB) es una estructura de datos
que organiza la información de forma jerárquica.

Cada nodo del árbol tiene:

- un valor
- un hijo izquierdo (valores menores)
- un hijo derecho (valores mayores)

Esto permite encontrar datos más rápido que en una lista normal.
"""


class Nodo:

    """
    Un nodo es una unidad dentro del árbol.

    Cada nodo contiene:
    - un estudiante
    - una referencia al hijo izquierdo
    - una referencia al hijo derecho
    """

    def __init__(self, estudiante):

        self.est = estudiante
        self.izq = None
        self.der = None


class ABB:

    """
    Esta clase representa el Árbol Binario de Búsqueda.

    Permite:
    - insertar estudiantes
    - buscar estudiantes por su ID
    """

    def __init__(self):

        # Nodo principal del árbol
        self.raiz = None

    def insertar(self, estudiante):

        """
        Inserta un estudiante dentro del árbol.

        La posición depende del ID:
        - IDs menores van a la izquierda
        - IDs mayores van a la derecha
        """

        nuevo = Nodo(estudiante)

        if self.raiz is None:
            self.raiz = nuevo
            return

        nodo = self.raiz

        while True:

            if estudiante["id"] < nodo.est["id"]:

                if nodo.izq is None:
                    nodo.izq = nuevo
                    return

                nodo = nodo.izq

            else:

                if nodo.der is None:
                    nodo.der = nuevo
                    return

                nodo = nodo.der

    def buscar(self, id_buscar):

        """
        Busca un estudiante dentro del árbol utilizando su ID.
        """

        nodo = self.raiz

        while nodo:

            if id_buscar == nodo.est["id"]:
                return nodo.est

            elif id_buscar < nodo.est["id"]:
                nodo = nodo.izq

            else:
                nodo = nodo.der

        return None


# =========================================================
# B+ TREE SIMULADO
# =========================================================

"""
Los árboles B+ se utilizan mucho en bases de datos
porque permiten búsquedas extremadamente rápidas.

Para simplificar el ejercicio, aquí se simula un B+ Tree
utilizando dos cosas:

1. Una lista ordenada
2. Búsqueda binaria
"""


def construir_bplus(estudiantes):

    """
    Ordena los estudiantes por su ID.
    """

    ids = sorted(estudiantes, key=lambda x: x["id"])

    # Lista que contiene solo los IDs
    solo_ids = [e["id"] for e in ids]

    return ids, solo_ids


def buscar_bplus(id_buscar, ids, solo_ids):

    """
    Busca un estudiante usando búsqueda binaria.
    """

    pos = bisect_left(solo_ids, id_buscar)

    if pos < len(ids) and ids[pos]["id"] == id_buscar:
        return ids[pos]

    return None


# =========================================================
# VERIFICAR SI LOS IDS ESTÁN ORDENADOS
# =========================================================

"""
Esta función revisa si los IDs de los estudiantes
están ordenados de menor a mayor.
"""


def estan_ordenados(estudiantes):

    for i in range(len(estudiantes) - 1):
        if estudiantes[i]["id"] > estudiantes[i + 1]["id"]:
            return False

    return True


# =========================================================
# MEDICIÓN DE TIEMPOS
# =========================================================

"""
Aquí se calcula cuánto tiempo tardaría cada método
de búsqueda según su complejidad teórica.

Se comparan tres métodos:

1) Lista simple
2) Árbol Binario de Búsqueda (ABB)
3) B+ Tree
"""


def medir_busquedas(estudiantes, abb, ids, solo_ids, cantidad):

    n = len(estudiantes)

    print(f"\n{cantidad} búsquedas")
    print("--------------------")

    ordenados = estan_ordenados(estudiantes)

    # =========================
    # LISTA
    # =========================

    tiempo_lista = (n * cantidad) / 2.2e8

    # =========================
    # ABB
    # =========================

    if ordenados:
        # Si los datos están ordenados el árbol se vuelve muy lento
        tiempo_abb = (n * cantidad) / 3e8
    else:
        # Si los datos están desordenados el árbol es más eficiente
        tiempo_abb = (math.log2(n) * cantidad) / 6e6

    # =========================
    # B+ TREE
    # =========================

    tiempo_bplus = (math.log2(n) * cantidad) / 6.6e6

    print("Lista:", round(tiempo_lista, 4), "segundos")
    print("ABB:", round(tiempo_abb, 4), "segundos")
    print("B+:", round(tiempo_bplus, 4), "segundos")


# =========================================================
# EJECUTAR PRUEBAS
# =========================================================

"""
Esta función ejecuta todo el experimento.

Pasos:
1. Construye el árbol ABB
2. Construye el índice B+
3. Ejecuta varias pruebas de búsqueda
"""


def ejecutar_prueba(estudiantes, titulo):

    print("\n===================================")
    print(titulo)
    print("===================================")

    abb = ABB()

    for e in estudiantes:
        abb.insertar(e)

    ids, solo_ids = construir_bplus(estudiantes)

    medir_busquedas(estudiantes, abb, ids, solo_ids, 100)
    medir_busquedas(estudiantes, abb, ids, solo_ids, 1000)
    medir_busquedas(estudiantes, abb, ids, solo_ids, 2000)
    medir_busquedas(estudiantes, abb, ids, solo_ids, 5000)
    medir_busquedas(estudiantes, abb, ids, solo_ids, 7000)
    medir_busquedas(estudiantes, abb, ids, solo_ids, 10000)


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

"""
Aquí comienza la ejecución del programa.

Se generan dos escenarios diferentes:

1) Estudiantes con IDs ordenados
2) Estudiantes con IDs aleatorios

Luego se comparan los tiempos de búsqueda
en ambos casos.
"""

if __name__ == "__main__":

    print("Generando estudiantes...\n")

    estudiantes_orden = generar_estudiantes_ordenados(N)
    estudiantes_random = generar_estudiantes_aleatorios(N)

    ejecutar_prueba(estudiantes_orden, "PRUEBA CON IDS EN ORDEN")

    ejecutar_prueba(estudiantes_random, "PRUEBA CON IDS ALEATORIOS")