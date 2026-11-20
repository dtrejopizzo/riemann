"""Interval tests for the slope and the two endpoints in round 296."""
from mpmath import iv

iv.dps = 35
cells = 1024
factors = [[] for _ in range(26)]
primes = []
for p in range(2, 26):
    if not factors[p]:
        primes.append(p)
        for n in range(p, 26, p):
            m, e = n, 0
            while m % p == 0:
                m //= p
                e += 1
            factors[n].append((p, e))

one = iv.mpf(1)
logs = {p: iv.log(p) for p in primes}
weights = {
    z: [(iv.log(one*z/m)-1+one*m/z)/m for m in range(1, z+1)]
    for z in (8, 25)
}

for i in range(cells):
    t = 1 + iv.mpf([i, i+1])/cells
    values = {}
    for p in primes:
        u = 1 - (1 if p % 3 != 2 else -1)*iv.cos(t*logs[p])
        values[p] = (-2*u, u**2)
    b = [one]*26
    for n in range(1, 26):
        for p, e in factors[n]:
            b[n] = b[n]*values[p][e-1] if e <= 2 else 0
    for z in (8, 25):
        K = sum(b[m]*weights[z][m-1] for m in range(1, z+1))
        if not (K > one/100 if z == 8 else K < -one/100):
            raise ArithmeticError((i, z, str(K)))
    for z in range(8, 26):
        J = sum(b[m]*(one/m-one/z) for m in range(1, z+1))
        if not J < -one/100:
            raise ArithmeticError((i, z, str(J)))
print("PASS: endpoints K and all 18 endpoint slopes on 1024 cells.")
