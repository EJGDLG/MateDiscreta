import mathlib

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")

def ingresar_conjunto(nombre):
    universo = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    while True:
        elementos = input(f"Ingrese los elementos del conjunto {nombre} (A-Z, 0-9, separados por comas): ").strip()
        elementos_lista = [e.strip().upper() for e in elementos.split(',')]
        if all(e in universo and len(e) == 1 for e in elementos_lista):
            return set(elementos_lista)
        else:
            print("Entrada no válida. Asegúrese de ingresar solo letras (A-Z) o dígitos (0-9), separados por comas.")

def operar_conjuntos(conjunto_a, conjunto_b):
    while True:
        print("\nSeleccione la operación de conjuntos:")
        print("1. Complemento")
        print("2. Unión")
        print("3. Intersección")
        print("4. Diferencia")
        print("5. Diferencia Simétrica")
        print("6. Volver al menú principal")

        opcion = input("Ingrese la opción deseada: ").strip()

        if opcion == '1':
            print(f"Complemento de A: {mathlib.complemento(conjunto_a)}")
            print(f"Complemento de B: {mathlib.complemento(conjunto_b)}")
        elif opcion == '2':
            print(f"Unión de A y B: {mathlib.union(conjunto_a, conjunto_b)}")
        elif opcion == '3':
            print(f"Intersección de A y B: {mathlib.interseccion(conjunto_a, conjunto_b)}")
        elif opcion == '4':
            print(f"Diferencia A - B: {mathlib.diferencia(conjunto_a, conjunto_b)}")
            print(f"Diferencia B - A: {mathlib.diferencia(conjunto_b, conjunto_a)}")
        elif opcion == '5':
            print(f"Diferencia Simétrica de A y B: {mathlib.diferencia_simetrica(conjunto_a, conjunto_b)}")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, elija un número del 1 al 6.")

def main():
    conjunto_a = None
    conjunto_b = None

    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ").strip()

        if opcion == '1':
            conjunto_a = ingresar_conjunto("A")
            conjunto_b = ingresar_conjunto("B")
            print(f"Conjunto A: {conjunto_a}")
            print(f"Conjunto B: {conjunto_b}")
        elif opcion == '2':
            if conjunto_a is None or conjunto_b is None:
                print("Debe construir los conjuntos A y B primero.")
            else:
                operar_conjuntos(conjunto_a, conjunto_b)
        elif opcion == '3':
            print("Finalizando el programa...")
            break
        else:
            print("Opción no válida. Por favor, elija un número del 1 al 3.")

if _name_ == "_main_":
    main()