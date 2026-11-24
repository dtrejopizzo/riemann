"""Resonance weights R_rho = Res_{s=rho/2} phi(s), phi(s) = Lambda(2s-1)/Lambda(2s),
Lambda(s) = pi^{-s/2} Gamma(s/2) zeta(s), so R_rho = Lambda(rho-1)/(2 Lambda'(rho))
= (rho/(rho-2)) xi(rho-1)/(2 xi'(rho)), for the first nontrivial zeros of zeta
(Proposition 4.1).  Requires mpmath."""
from mpmath import mp, zetazero, zeta, gamma, pi, diff, nstr

mp.dps = 30


def xi(s):
    return s * (s - 1) / 2 * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def Lam(s):
    return pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def weight(n):
    rho = zetazero(n)
    return rho, rho / (rho - 2) * xi(rho - 1) / (2 * diff(xi, rho))


if __name__ == "__main__":
    vals = []
    for n in list(range(1, 16)) + [50, 100, 300]:
        rho, R = weight(n)
        vals.append((n, abs(R)))
        print(f"{n:4d}  gamma={nstr(rho.imag, 10):>14}  |R|={nstr(abs(R), 6)}")
    first = [v for n, v in vals if n <= 15]
    print("first fifteen: min", nstr(min(first), 4), "max", nstr(max(first), 4))
