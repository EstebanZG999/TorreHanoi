#!/usr/bin/env python3

from hanoi_dac import hanoi_dac_moves
from hanoi_dp import hanoi_dp_moves
from utils.timer import time_function

def ejecutar_hanoi(metodo, discos):
    print(f"\nResolviendo Torre de Hanoi con {discos} discos usando {metodo}...\n")
    # Selección del algoritmo según método
    if metodo == "DaC":
        funcion = hanoi_dac_moves
    else:
        funcion = hanoi_dp_moves
    
    # Medir tiempo de ejecución
    duracion, movimientos = medir_tiempo_y_ejecutar(funcion, discos)

    # Mostrar movimientos
    for i, (disk, src, dst) in enumerate(movimientos, 1):
        print(f"Mover disco {disk} de {src} a {dst}")

    total = len(movimientos)
    print(f"\nTotal de movimientos: {total}")
    print(f"Tiempo de ejecución: {duracion:.6f} segundos\n")

def medir_tiempo_y_ejecutar(funcion, discos):
    """Ejecuta la función y mide el tiempo, devolviendo duración y resultado."""
    from functools import partial
    wrapped = partial(funcion, discos, 'A', 'C', 'B')
    duracion = time_function(wrapped)
    resultado = wrapped()
    return duracion, resultado

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
