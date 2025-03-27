#!/usr/bin/env python3

from hanoi_dac import hanoi_dac_moves, hanoi_dac_count
from hanoi_dp import hanoi_dp_moves, hanoi_dp_count

def ejecutar_hanoi(metodo, discos):
    print(f"\nResolviendo Torre de Hanoi con {discos} discos usando {metodo}...")
    if metodo == "DaC":
        movimientos = hanoi_dac_moves(discos, 'A', 'C', 'B')
    else:
        movimientos = hanoi_dp_moves(discos, 'A', 'C', 'B')
    
    for i, (disk, src, dst) in enumerate(movimientos, 1):
        print(f"Paso {i}: Mover disco {disk} de {src} a {dst}")

    total = len(movimientos)
    print(f"\nTotal de movimientos: {total}\n")

def menu():
    print("🔷 Bienvenido al juego de la Torre de Hanoi 🔷")

    while True:
        print("\n¿Cómo deseas resolver el problema?")
        print("1. Usar Divide and Conquer (DaC)")
        print("2. Usar Programación Dinámica (DP)")
        opcion = input("\nElige una opción (1 o 2): ").strip()

        if opcion not in {"1", "2"}:
            print("\nOpción no válida. Intenta de nuevo.")
            continue

        metodo = "DaC" if opcion == "1" else "DP"

        try:
            discos = int(input("\n¿Con cuántos discos deseas trabajar? (número entero positivo): "))
            if discos <= 0:
                raise ValueError
        except ValueError:
            print("\nEntrada no válida. Debes ingresar un número entero positivo.")
            continue

        ejecutar_hanoi(metodo, discos)

        repetir = input("¿Deseas intentarlo nuevamente? (s/n): ").strip().lower()
        if repetir != "s":
            print("\nGracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    menu()
