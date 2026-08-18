#!/usr/bin/env python3
"""Rational interval verifier for the finite Omega7 exceptional range."""

from fractions import Fraction
from math import comb, factorial


def Q(s: str) -> Fraction:
    return Fraction(s)


class I:
    def __init__(self, lo, hi=None):
        self.lo = Q(str(lo)) if not isinstance(lo, Fraction) else lo
        self.hi = self.lo if hi is None else (Q(str(hi)) if not isinstance(hi, Fraction) else hi)
        if self.lo > self.hi:
            raise ValueError("empty interval")

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other):
        other = as_i(other)
        return I(self.lo - other.hi, self.hi - other.lo)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __mul__(self, other):
        other = as_i(other)
        vals = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return I(min(vals), max(vals))

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("interval crosses zero")
        return self * I(1 / other.hi, 1 / other.lo)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return as_i(other) - self

    def __rmul__(self, other):
        return self * other

    def width(self):
        return self.hi - self.lo

    def dec(self, places=18):
        return f"[{decimal_floor(self.lo, places)}, {decimal_ceil(self.hi, places)}]"


def as_i(x):
    return x if isinstance(x, I) else I(x)


def decimal_from_scaled(n, places):
    sign = "-" if n < 0 else ""
    n = abs(n)
    scale = 10**places
    whole, frac = divmod(n, scale)
    return f"{sign}{whole}.{frac:0{places}d}"


def decimal_floor(x, places):
    scale = 10**places
    return decimal_from_scaled(x.numerator * scale // x.denominator, places)


def decimal_ceil(x, places):
    scale = 10**places
    return decimal_from_scaled(-((-x.numerator * scale) // x.denominator), places)


def poly_mul(a, b, n):
    out = [I(0) for _ in range(n + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= n:
                out[i + j] = out[i + j] + ai * bj
    return out


def log_one_plus(u, n):
    out = [I(0) for _ in range(n + 1)]
    power = [I(0) for _ in range(n + 1)]
    power[0] = I(1)
    for m in range(1, n + 1):
        power = poly_mul(power, u, n)
        c = I(Fraction(1 if m % 2 else -1, m))
        for k in range(n + 1):
            out[k] = out[k] + c * power[k]
    return out


gamma = [
    I("0.57721566490153286060651209008", "0.57721566490153286060651209009"),
    I("-0.072815845483676724860586375875", "-0.072815845483676724860586375874"),
    I("-0.009690363192872318484530386036", "-0.009690363192872318484530386035"),
    I("0.002053834420303345866160046542", "0.002053834420303345866160046543"),
    I("0.002325370065467300057468170177", "0.002325370065467300057468170178"),
    I("0.000793323817301062701753334877", "0.000793323817301062701753334878"),
    I("-0.000238769345430199609872421842", "-0.000238769345430199609872421841"),
    I("-0.000527289567057751046074097505479", "-0.000527289567057751046074097505478"),
]

log4pi = I("2.5310242469692907929778915942", "2.5310242469692907929778915943")
zeta = {
    2: I("1.6449340668482264364724151666", "1.6449340668482264364724151667"),
    3: I("1.2020569031595942853997381615", "1.2020569031595942853997381616"),
    4: I("1.0823232337111381915160036965", "1.0823232337111381915160036966"),
    5: I("1.0369277551433699263313654864", "1.0369277551433699263313654865"),
    6: I("1.0173430619844491397145179297", "1.0173430619844491397145179298"),
    7: I("1.0083492773819228268397975498", "1.0083492773819228268397975499"),
    8: I("1.00407735619794433937868523850865", "1.00407735619794433937868523850866"),
}


def prime_coeffs(n):
    q = [I(0) for _ in range(n + 1)]
    q[0] = I(1)
    for j in range(n):
        sign = 1 if j % 2 == 0 else -1
        q[j + 1] = gamma[j] * I(Fraction(sign, factorial(j)))
    u = q[:]
    u[0] = u[0] - 1
    return log_one_plus(u, n)


def lambda_arch(n):
    val = I(1) - I(Fraction(n, 2)) * (gamma[0] + log4pi)
    for k in range(2, n + 1):
        sign = 1 if k % 2 == 0 else -1
        factor = Fraction(sign * comb(n, k), 1) * (1 - Fraction(1, 2**k))
        val = val + I(factor) * zeta[k]
    return val


def lambda_prime(n):
    p = prime_coeffs(n)
    val = I(0)
    for k in range(1, n + 1):
        val = val + I(n * comb(n - 1, k - 1)) * p[k]
    return val


def main():
    ok = True
    for n in range(1, 9):
        arch = lambda_arch(n)
        lam = arch + lambda_prime(n)
        ok = ok and lam.lo > 0
        print(n, lam.dec(24), "positive=", lam.lo > 0)
        if n == 8:
            margin = lam - arch / 2
            ok = ok and margin.lo > 0
            print("8-half-arch-margin", margin.dec(24), "positive=", margin.lo > 0)
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
