#!/usr/bin/env python3

def hanoi_dac_count(n: int) -> int:
    """Devuelve solo el número de movimientos."""
    if n <= 0:
        return 0
    return 2 * hanoi_dac_count(n - 1) + 1

def hanoi_dac_moves(n: int, source: str, destination: str, auxiliary: str, moves=None):
    """Genera la lista de movimientos (tupla: (disco, origen, destino))."""
    if moves is None:
        moves = []
    if n == 0:
        return moves

    hanoi_dac_moves(n-1, source, auxiliary, destination, moves)
    moves.append((n, source, destination))
    hanoi_dac_moves(n-1, auxiliary, destination, source, moves)
    return moves

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Torre de Hanoi — Divide & Conquer")
    parser.add_argument("n", type=int, help="Número de discos")
    parser.add_argument("--print", action="store_true", help="Mostrar todos los movimientos")
    args = parser.parse_args()

    if args.print:
        for disk, src, dst in hanoi_dac_moves(args.n, 'A', 'C', 'B'):
            print(f"Move disk {disk} from source {src} to destination {dst}")
    else:
        print(f"Hanoi DaC ({args.n} discos) → {hanoi_dac_count(args.n)} movimientos")
