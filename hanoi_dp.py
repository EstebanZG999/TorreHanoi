#!/usr/bin/env python3
from functools import lru_cache

def hanoi_dp_count(n: int) -> int:
    """Cuenta movimientos usando DP bottom‑up."""
    if n <= 0:
        return 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1] + 1
    return dp[n]

@lru_cache(maxsize=None)
def hanoi_dp_moves(n: int, source: str, destination: str, auxiliary: str):
    """Genera lista de movimientos usando memoización."""
    if n == 0:
        return []
    moves = []
    moves += hanoi_dp_moves(n-1, source, auxiliary, destination)
    moves.append((n, source, destination))
    moves += hanoi_dp_moves(n-1, auxiliary, destination, source)
    return moves

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Torre de Hanoi — Programación Dinámica")
    parser.add_argument("n", type=int, help="Número de discos")
    parser.add_argument("--print", action="store_true", help="Mostrar todos los movimientos")
    args = parser.parse_args()

    if args.print:
        for disk, src, dst in hanoi_dp_moves(args.n, 'A', 'C', 'B'):
            print(f"Move disk {disk} from source {src} to destination {dst}")
    else:
        print(f"Hanoi DP ({args.n} discos) → {hanoi_dp_count(args.n)} movimientos")
