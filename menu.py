# main.py

from turismo import turistas_por_pais, turistas_por_mes, eliminar_turista

def main():
    ejecutar = True
    while ejecutar:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Turistas por país")
        print("2. Turistas por mes")
        print("3. Eliminar turista")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                pais = input("Ingrese el país: ").strip()
                turistas_por_pais(pais)
            elif opcion == 2:
                while True:
                    try:
                        mes = int(input("Ingrese el mes (1-12): "))
                        if 1 <= mes <= 12:
                            turistas_por_mes(mes)
                            break
                        else:
                            print("Por favor, ingrese un mes válido entre 1 y 12.")
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número entero.")
            elif opcion == 3:
                eliminar_turista()
            elif opcion == 4:
                print("Programa terminado...")
                ejecutar = False
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
    main()
