"""Enclose K_t(48) uniformly on [1,2] by interval arithmetic."""
from mpmath import iv

iv.dps = 35
z = 48
cells = 1024
factors = [[] for _ in range(z + 1)]
primes = []
for p in range(2, z + 1):
    if factors[p]:
        continue
    primes.append(p)
    for n in range(p, z + 1, p):
        m, e = n, 0
        while m % p == 0:
            m //= p
            e += 1
        factors[n].append((p, e))

weights = {}
for n in range(1, z):
    ratio = iv.mpf(z) / n
    weights[n] = (iv.log(ratio) - 1 + 1 / ratio) / n
logs = {p: iv.log(p) for p in primes}
for i in range(cells):
    t = 1 + iv.mpf([i, i + 1]) / cells
    local = {}
    for p in primes:
        chi = 1 if p == 3 or p % 3 == 1 else -1
        u = 1 - chi * iv.cos(t * logs[p])
        local[p] = (-2 * u, u ** 2)
    value = iv.mpf(0)
    for n, weight in weights.items():
        term = weight
        for p, e in factors[n]:
            if e > 2:
                term = 0
                break
            term *= local[p][e - 1]
        value += term
    if not (value < -iv.mpf(1) / 25):
        raise ArithmeticError((i, str(value)))
print(f"PASS: K_t(48) < -1/25 on all {cells} cells.")
