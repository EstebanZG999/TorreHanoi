import time

def time_function(func, *args, **kwargs) -> float:
    """
    Ejecuta func(*args, **kwargs) y devuelve el tiempo transcurrido en segundos.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start

if __name__ == "__main__":
    # Ejemplo rápido de uso
    from hanoi_dac import hanoi_dac
    duration = time_function(hanoi_dac, 15)
    print(f"Tiempo DaC para 15 discos: {duration:.6f}s")
