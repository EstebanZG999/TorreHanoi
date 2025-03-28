from functools import lru_cache

def hanoi_dp_count(n: int) -> int:
    """Cuenta movimientos usando DP bottom‑up."""
    if n <= 0:
        return 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1] + 1
    return dp[n]

def hanoi_dp_moves(n: int, source: str, destination: str, auxiliary: str):
    """Generador de movimientos (no almacena en lista)."""
    if n == 0:
        return
    yield from hanoi_dp_moves(n-1, source, auxiliary, destination)
    yield (n, source, destination)
    yield from hanoi_dp_moves(n-1, auxiliary, destination, source)
