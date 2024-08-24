

UNIVERSO = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

def construir_conjunto(elementos):
    """
    Construye un conjunto a partir de una cadena de caracteres válidos.
    :param elementos: str - Cadena de caracteres (A-Z, 0-9).
    :return: set - Conjunto de elementos válidos.
    """
    conjunto = set(elemento for elemento in elementos.upper() if elemento in UNIVERSO)
    return conjunto

def complemento(conjunto):
    """
    Calcula el complemento de un conjunto con respecto al UNIVERSO.
    :param conjunto: set - Conjunto del cual se desea el complemento.
    :return: set - Complemento del conjunto.
    """
    resultado = set()
    for elemento in UNIVERSO:
        if elemento not in conjunto:
            resultado.add(elemento)
    return resultado

def union(conjunto1, conjunto2):
    """
    Calcula la unión de dos conjuntos.
    :param conjunto1: set - Primer conjunto.
    :param conjunto2: set - Segundo conjunto.
    :return: set - Unión de los dos conjuntos.
    """
    resultado = set(conjunto1)
    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.add(elemento)
    return resultado

def interseccion(conjunto1, conjunto2):
    """
    Calcula la intersección de dos conjuntos.
    :param conjunto1: set - Primer conjunto.
    :param conjunto2: set - Segundo conjunto.
    :return: set - Intersección de los dos conjuntos.
    """
    resultado = set()
    for elemento in conjunto1:
        if elemento in conjunto2:
            resultado.add(elemento)
    return resultado

def diferencia(conjunto1, conjunto2):
    """
    Calcula la diferencia entre dos conjuntos (conjunto1 - conjunto2).
    :param conjunto1: set - Primer conjunto.
    :param conjunto2: set - Segundo conjunto.
    :return: set - Diferencia entre los dos conjuntos.
    """
    resultado = set(conjunto1)
    for elemento in conjunto2:
        if elemento in resultado:
            resultado.remove(elemento)
    return resultado

def diferencia_simetrica(conjunto1, conjunto2):
    """
    Calcula la diferencia simétrica entre dos conjuntos.
    :param conjunto1: set - Primer conjunto.
    :param conjunto2: set - Segundo conjunto.
    :return: set - Diferencia simétrica de los dos conjuntos.
    """
    resultado = set()
    for elemento in conjunto1:
        if elemento not in conjunto2:
            resultado.add(elemento)
    for elemento in conjunto2:
        if elemento not in conjunto1:
            resultado.add(elemento)
    return resultado
