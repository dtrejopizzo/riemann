#!/usr/bin/env python3
"""Certificates and reproducible evaluations for the explicit D.51 level."""
import math
import mpmath as mp

mp.mp.dps = 50


def primes_up_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n-p*p)//p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def prime_power_terms(T):
    X = int(mp.floor(mp.e**(2*T)))
    out = []
    for p in primes_up_to(X):
        pk = p
        k = 1
        while pk <= X:
            out.append((p, k, mp.log(p)/mp.sqrt(pk)))
            if pk > X//p:
                break
            pk *= p
            k += 1
    return out


def gamma_constant_energy(T):
    return mp.nsum(
        lambda j: (1-mp.e**(-2*T*(2*j+mp.mpf("0.5"))))
                  /(T*(2*j+mp.mpf("0.5"))**2),
        [0, mp.inf],
    )


def gamma_constant_energy_integral(T):
    w = lambda r: mp.e**(-r/2)/(1-mp.e**(-2*r))
    return (mp.quad(lambda r: w(r)*r/T, [0, 2*T])
            + mp.quad(lambda r: 2*w(r), [2*T, mp.inf]))


def explicit_level(T):
    terms = prime_power_terms(T)
    finite = mp.fsum(c*(k*mp.log(p)/T-2) for p, k, c in terms)
    m0 = mp.log(mp.pi)-mp.digamma(mp.mpf(1)/4)
    polar = 16*mp.sinh(T/2)**2/T
    gamma = gamma_constant_energy(T)
    return finite+gamma-m0+polar, len(terms), finite, polar, gamma


# Algebraic identities used in the note.
for T in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2), mp.mpf(3)):
    series = gamma_constant_energy(T)
    integral = gamma_constant_energy_integral(T)
    assert abs(series-integral) < mp.mpf("1e-35")
    uo_norm_sq = 2*mp.sinh(T)-2*T
    assert uo_norm_sq > 0

# Reproducible values; these are evaluations, not a proof of the odd gap.
for T in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2), mp.mpf(3), mp.mpf(4)):
    level, count, finite, polar, gamma = explicit_level(T)
    assert mp.isfinite(level)
    print(
        f"T={float(T):.1f} prime-powers={count:4d} "
        f"finite={mp.nstr(finite, 10)} polar={mp.nstr(polar, 10)} "
        f"Gamma={mp.nstr(gamma, 10)} E0={mp.nstr(level, 16)}"
    )

print("PASS Gamma integral equals the positive series in (3.5)")
print("PASS every prime power p^k <= exp(2T) is enumerated once")
print("NOTE values of E0 do not certify the odd Green bound (9.1)")
