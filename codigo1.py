# Definimos el universo de elementos posibles
UNIVERSO = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

# Función para construir un conjunto
def construir_conjunto():
    while True:
        elementos = input("Ingresa los elementos del conjunto (A-Z, 0-9): ").upper()
        if all(e in UNIVERSO for e in elementos):
            return set(elementos)
        else:
            print("Entrada no válida. Por favor, ingresa solo letras de A-Z o dígitos 0-9.")

# Función para calcular el complemento
def complemento(conjunto):
    resultado = set()
    for elemento in UNIVERSO:
        if elemento not in conjunto:
            resultado.add(elemento)
    return resultado

# Función para calcular la unión
def union(conjunto1, conjunto2):
    resultado = set(conjunto1)
    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.add(elemento)
    return resultado

# Función para calcular la intersección
def interseccion(conjunto1, conjunto2):
    resultado = set()
    for elemento in conjunto1:
        if elemento in conjunto2:
            resultado.add(elemento)
    return resultado

# Función para calcular la diferencia
def diferencia(conjunto1, conjunto2):
    resultado = set(conjunto1)
    for elemento in conjunto2:
        if elemento in resultado:
            resultado.remove(elemento)
    return resultado

# Función para calcular la diferencia simétrica
def diferencia_simetrica(conjunto1, conjunto2):
    resultado = set()
    for elemento in conjunto1:
        if elemento not in conjunto2:
            resultado.add(elemento)
    for elemento in conjunto2:
        if elemento not in conjunto1:
            resultado.add(elemento)
    return resultado

# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Finalizar")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            conjunto = construir_conjunto()
            print(f"Conjunto construido: {conjunto}")

        elif opcion == '2':
            print("Selecciona la operación:")
            print("1. Complemento")
            print("2. Unión")
            print("3. Intersección")
            print("4. Diferencia")
            print("5. Diferencia Simétrica")
            operacion = input("Selecciona una opción: ")

            if operacion == '1':
                conjunto = construir_conjunto()
                print(f"Complemento: {complemento(conjunto)}")

            elif operacion == '2':
                conjunto1 = construir_conjunto()
                conjunto2 = construir_conjunto()
                print(f"Unión: {union(conjunto1, conjunto2)}")

            elif operacion == '3':
                conjunto1 = construir_conjunto()
                conjunto2 = construir_conjunto()
                print(f"Intersección: {interseccion(conjunto1, conjunto2)}")

            elif operacion == '4':
                conjunto1 = construir_conjunto()
                conjunto2 = construir_conjunto()
                print(f"Diferencia: {diferencia(conjunto1, conjunto2)}")

            elif operacion == '5':
                conjunto1 = construir_conjunto()
                conjunto2 = construir_conjunto()
                print(f"Diferencia Simétrica: {diferencia_simetrica(conjunto1, conjunto2)}")

        elif opcion == '3':
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
