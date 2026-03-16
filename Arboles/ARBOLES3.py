# =========================================================
# IMPORTACIÓN DE LIBRERÍAS
# =========================================================

# random: permite generar números aleatorios.
# Se usa para crear estudiantes ficticios con nombres y promedios al azar.
import random

# time: permite medir cuánto tiempo tarda el programa en ejecutar ciertas operaciones.
# En este caso se usa para medir el tiempo de las búsquedas.
import time

# bisect_left: función que permite realizar búsqueda binaria en listas ordenadas.
# Se usa para simular el funcionamiento de un índice tipo B+ Tree.
from bisect import bisect_left


# =========================================================
# CONFIGURACIÓN INICIAL
# =========================================================

# Número total de estudiantes que se van a generar para las pruebas
N = 10000

# Lista de nombres posibles para los estudiantes
# Cuando se genere un estudiante, su nombre se escogerá aleatoriamente de esta lista
nombres = ["Ana", "Carlos", "Maria", "Luis", "Pedro", "Sofia", "Laura", "Juan"]


# =========================================================
# GENERAR ESTUDIANTES
# =========================================================

"""
En esta sección se generan estudiantes ficticios para poder
probar los distintos métodos de búsqueda.

Cada estudiante tiene tres datos:
- id: número que identifica al estudiante
- nombre: nombre elegido aleatoriamente
- promedio: nota promedio entre 3.0 y 5.0
"""


def generar_estudiantes_ordenados(n):
    """
    Genera una lista de estudiantes donde los IDs están en orden.
    Es decir: 0, 1, 2, 3, 4, 5...
    
    Esto es importante porque cuando los datos están ordenados,
    algunas estructuras de datos se comportan peor.
    """

    estudiantes = [
        {
            "id": i,  # el ID aumenta de forma ordenada
            "nombre": random.choice(nombres),
            "promedio": round(random.uniform(3.0, 5.0), 2)
        }
        for i in range(n)
    ]

    return estudiantes


def generar_estudiantes_aleatorios(n):
    """
    Genera estudiantes con IDs completamente aleatorios.
    
    Esto simula un caso más realista, donde los datos no llegan ordenados.
    """

    estudiantes = [
        {
            "id": random.randint(1000, 99999),
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
Este es el método de búsqueda más simple.

El programa revisa cada estudiante de la lista uno por uno
hasta encontrar el ID buscado.

Este método puede ser lento si hay muchos datos.
"""


def buscar_lista(lista, id_buscar):

    for e in lista:  # se revisa cada estudiante
        if e["id"] == id_buscar:  # si el ID coincide
            return e

    return None  # si no se encuentra el estudiante


# =========================================================
# ÁRBOL BINARIO DE BÚSQUEDA (ABB)
# =========================================================

"""
Un árbol binario de búsqueda organiza los datos en forma de árbol.

Regla principal:
- valores menores van a la izquierda
- valores mayores van a la derecha

Esto permite reducir el número de comparaciones necesarias para encontrar un dato.
"""


class Nodo:
    """
    Cada nodo del árbol guarda:
    - el estudiante
    - una referencia al hijo izquierdo
    - una referencia al hijo derecho
    """

    def __init__(self, estudiante):

        self.est = estudiante
        self.izq = None
        self.der = None


class ABB:
    """
    Esta clase representa el árbol binario completo.
    """

    def __init__(self):

        self.raiz = None  # el árbol comienza vacío

    def insertar(self, estudiante):
        """
        Inserta un nuevo estudiante en el árbol respetando
        las reglas del árbol binario de búsqueda.
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
        Busca un estudiante en el árbol siguiendo la estructura
        izquierda/derecha hasta encontrarlo.
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
En este programa no se implementa un B+ Tree real.

En cambio, se simula su comportamiento usando:

1. Una lista ordenada de estudiantes
2. Búsqueda binaria

Esto se parece a cómo funcionan muchos índices en bases de datos.
"""


def construir_bplus(estudiantes):

    # ordenar estudiantes por ID
    ids = sorted(estudiantes, key=lambda x: x["id"])

    # crear lista solo con los IDs
    solo_ids = [e["id"] for e in ids]

    return ids, solo_ids


def buscar_bplus(id_buscar, ids, solo_ids):
    """
    Usa búsqueda binaria para encontrar rápidamente
    la posición del ID dentro de la lista ordenada.
    """

    pos = bisect_left(solo_ids, id_buscar)

    if pos < len(ids) and ids[pos]["id"] == id_buscar:
        return ids[pos]

    return None


# =========================================================
# MEDICIÓN DE TIEMPOS
# =========================================================

"""
Esta función mide cuánto tiempo tarda cada método
en realizar varias búsquedas.

Los tiempos se calculan usando el reloj interno del computador.
"""


def medir_busquedas(estudiantes, abb, ids, solo_ids, cantidad):

    print(f"\n{cantidad} búsquedas")
    print("--------------------")

    # generar IDs aleatorios que se van a buscar
    ids_buscar = [random.choice(estudiantes)["id"] for _ in range(cantidad)]

    # =========================
    # MEDIR TIEMPO LISTA
    # =========================

    inicio = time.perf_counter()

    for i in ids_buscar:
        buscar_lista(estudiantes, i)

    tiempo_lista = time.perf_counter() - inicio

    # =========================
    # MEDIR TIEMPO ABB
    # =========================

    inicio = time.perf_counter()

    for i in ids_buscar:
        abb.buscar(i)

    tiempo_abb = time.perf_counter() - inicio

    # =========================
    # MEDIR TIEMPO B+
    # =========================

    inicio = time.perf_counter()

    for i in ids_buscar:
        buscar_bplus(i, ids, solo_ids)

    tiempo_bplus = time.perf_counter() - inicio

    # mostrar resultados
    print("Lista:", round(tiempo_lista, 6), "segundos")
    print("ABB:", round(tiempo_abb, 6), "segundos")
    print("B+:", round(tiempo_bplus, 6), "segundos")


# =========================================================
# EJECUTAR PRUEBAS
# =========================================================

def ejecutar_prueba(estudiantes, titulo):
    """
    Ejecuta todas las pruebas de búsqueda con diferentes
    cantidades de consultas.
    """

    print("\n===================================")
    print(titulo)
    print("===================================")

    abb = ABB()

    # insertar estudiantes en el árbol
    for e in estudiantes:
        abb.insertar(e)

    # construir índice B+
    ids, solo_ids = construir_bplus(estudiantes)

    # realizar pruebas con diferentes cantidades de búsquedas
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
Esta es la parte donde comienza la ejecución del programa.
"""


if __name__ == "__main__":

    print("Generando estudiantes...\n")

    # generar estudiantes con IDs ordenados
    estudiantes_orden = generar_estudiantes_ordenados(N)

    # generar estudiantes con IDs aleatorios
    estudiantes_random = generar_estudiantes_aleatorios(N)

    # ejecutar pruebas
    ejecutar_prueba(estudiantes_orden, "PRUEBA CON IDS EN ORDEN")

    ejecutar_prueba(estudiantes_random, "PRUEBA CON IDS ALEATORIOS")