# main.py

import mathlib

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Finalizar")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            elementos = input("Ingresa los elementos del conjunto (A-Z, 0-9): ")
            conjunto = mathlib.construir_conjunto(elementos)
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
                elementos = input("Ingresa los elementos del conjunto (A-Z, 0-9): ")
                conjunto = mathlib.construir_conjunto(elementos)
                print(f"Complemento: {mathlib.complemento(conjunto)}")

            elif operacion == '2':
                elementos1 = input("Ingresa los elementos del primer conjunto (A-Z, 0-9): ")
                elementos2 = input("Ingresa los elementos del segundo conjunto (A-Z, 0-9): ")
                conjunto1 = mathlib.construir_conjunto(elementos1)
                conjunto2 = mathlib.construir_conjunto(elementos2)
                print(f"Unión: {mathlib.union(conjunto1, conjunto2)}")

            elif operacion == '3':
                elementos1 = input("Ingresa los elementos del primer conjunto (A-Z, 0-9): ")
                elementos2 = input("Ingresa los elementos del segundo conjunto (A-Z, 0-9): ")
                conjunto1 = mathlib.construir_conjunto(elementos1)
                conjunto2 = mathlib.construir_conjunto(elementos2)
                print(f"Intersección: {mathlib.interseccion(conjunto1, conjunto2)}")

            elif operacion == '4':
                elementos1 = input("Ingresa los elementos del primer conjunto (A-Z, 0-9): ")
                elementos2 = input("Ingresa los elementos del segundo conjunto (A-Z, 0-9): ")
                conjunto1 = mathlib.construir_conjunto(elementos1)
                conjunto2 = mathlib.construir_conjunto(elementos2)
                print(f"Diferencia: {mathlib.diferencia(conjunto1, conjunto2)}")

            elif operacion == '5':
                elementos1 = input("Ingresa los elementos del primer conjunto (A-Z, 0-9): ")
                elementos2 = input("Ingresa los elementos del segundo conjunto (A-Z, 0-9): ")
                conjunto1 = mathlib.construir_conjunto(elementos1)
                conjunto2 = mathlib.construir_conjunto(elementos2)
                print(f"Diferencia Simétrica: {mathlib.diferencia_simetrica(conjunto1, conjunto2)}")

        elif opcion == '3':
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
