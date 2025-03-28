def hanoi_dac_count(n: int) -> int:
    """Devuelve solo el número de movimientos."""
    if n <= 0:
        return 0
    return 2 * hanoi_dac_count(n - 1) + 1

def hanoi_dac_moves(n, source, destination, auxiliary):
    """Genera la lista de movimientos (tupla: (disco, origen, destino))."""
    if n == 0:
        return
    yield from hanoi_dac_moves(n-1, source, auxiliary, destination)
    yield (n, source, destination)
    yield from hanoi_dac_moves(n-1, auxiliary, destination, source)