"""Transversality of K on 1.5 <= t <= 1.51 and 13 <= z <= 15."""
from mpmath import iv

iv.dps = 35
one = iv.mpf(1)
for i in range(10):
    t = (1500 + iv.mpf([i, i + 1])) / 1000
    b, db = [], []
    for n in range(1, 16):
        m, v, d = n, one, 0
        for p in (2, 3, 5, 7, 11, 13):
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            if e:
                chi = -1 if p % 3 == 2 else 1
                u = 1 - chi * iv.cos(t * iv.log(p))
                du = chi * iv.log(p) * iv.sin(t * iv.log(p))
                f, df = (-2*u, -2*du) if e == 1 else (u*u, 2*u*du) if e == 2 else (0, 0)
                v, d = v*f, d*f + v*df
        b.append(v)
        db.append(d)

    def profile(z, coefficients, limit):
        return sum(coefficients[n-1]*(iv.log(z/n)-1+n/z)/n for n in range(1, limit+1))

    assert profile(13*one, b, 13) > one/1000
    assert profile(15*one, b, 15) < -one/1000
    for k in range(1300, 1500):
        z = iv.mpf([k, k+1])/100
        # At the upper integer endpoint the additional summand is zero.
        assert profile(z, db, k//100) > one/20
print("PASS: both endpoint signs and derivative on 2000 rectangles")
