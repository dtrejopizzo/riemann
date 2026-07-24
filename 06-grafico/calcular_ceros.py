"""Calcula los primeros 10000 ceros no triviales de zeta y los cachea a disco."""
import mpmath as mp
import time

mp.mp.dps = 15
N = 10000
OUT = "zeros_10000.txt"

t0 = time.time()
with open(OUT, "w") as f:
    for n in range(1, N + 1):
        g = float(mp.zetazero(n).imag)
        f.write(f"{g:.10f}\n")
        if n % 500 == 0:
            print(f"  {n} ceros  ({time.time()-t0:.0f}s)", flush=True)
print(f"Listo: {N} ceros en {time.time()-t0:.0f}s -> {OUT}")
