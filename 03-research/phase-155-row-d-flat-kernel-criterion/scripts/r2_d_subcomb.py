"""Phase 155 round 2, task (d): Theorem SC (sub-comb theorem) and its numbers.

Paper 47 Cor. 2.6:  for ANY nonnegative weights v = (v_n)_{n in N_T},
    lamA(v) <= C0 + A + phi((3 pi / 2T)^2),     A = sum_n v_n,   phi = Paper 47 Thm 2.2,
    phi(x) = sum_{k>=0} x / (a_k (x + 4 a_k^2)),  a_k = k + 1/4.
phi is increasing with phi(0+) = 0, so if A < -C0 = 5.3721834... there is an explicit
T0(A), the root of phi((3pi/2T)^2) = -C0 - A, beyond which the form is NEGATIVE.
"""
import json
import numpy as np
from mpmath import mp, mpf, findroot, digamma, log, pi, sqrt

mp.dps = 25
C0 = digamma(mpf(1)/4) - log(pi)


def phi(x):
    """phi(tau^2) = Re psi(1/4 + i tau/2) - psi(1/4)   (Paper 47 Thm 2.2(i))."""
    x = mpf(x)
    return mp.re(digamma(mpf(1)/4 + 1j*sqrt(x)/2)) - digamma(mpf(1)/4)


def T0_of_A(A):
    A = mpf(A)
    tgt = -C0 - A
    if tgt <= 0: return None
    lo, hi = mpf('1e-6'), mpf(1)
    while phi(hi) < tgt: hi *= 2
    x = findroot(lambda x: phi(x) - tgt, (lo, hi), solver='anderson')
    return (3*pi/2)/sqrt(x), x


def lam_bound(A, T):
    return C0 + mpf(A) + phi((3*pi/(2*mpf(T)))**2)


def comb_mass(primes, upto=None):
    """A = sum 2 Lambda(n)/sqrt(n) over prime powers of the listed primes with
    log n < 2T (upto = e^{2T}); upto=None means the primes themselves only."""
    A = mpf(0); terms = []
    for p in primes:
        q = p
        while upto is None or q < upto:
            A += 2*log(p)/sqrt(mpf(q)); terms.append(q)
            if upto is None: break
            q *= p
    return A, terms


if __name__ == '__main__':
    out = {}
    TEN = [12049, 124909, 149333, 322573, 324011, 373963, 417491, 630229, 782209, 908861]
    A, _ = comb_mass(TEN)
    T = log(mpf(908861))/2 + mpf('0.01')
    lam = lam_bound(A, T)
    T0, x0 = T0_of_A(A)
    print("(i) ten random primes < 10^6")
    print("    A = %.6f   (-C0 = %.7f, so A < -C0)" % (float(A), float(-C0)))
    print("    T0(A) = %.6f   (x0 = %.6f)" % (float(T0), float(x0)))
    print("    at T = (1/2)log(908861) + 0.01 = %.6f :  phi((3pi/2T)^2) = %.6f,  lam <= %.6f"
          % (float(T), float(phi((3*pi/(2*T))**2)), float(lam)))
    out['ten_random'] = dict(primes=TEN, A=float(A), T0=float(T0), T=float(T), lam_ub=float(lam))

    print("(ii) the faithful window containing exactly the first ten primes: T = (1/2)log 31")
    Tf = log(mpf(31))/2
    Af, terms = comb_mass([2,3,5,7,11,13,17,19,23,29], upto=31)
    print("    contacts n < 31 : %s" % sorted(terms))
    print("    A_T = %.6f ;  Cor 2.6 bound  lam <= %.6f  (positive: no information)"
          % (float(Af), float(lam_bound(Af, Tf))))
    env = 2*pi*mp.e**Af
    print("    envelope threshold 2 pi e^{A_T} = %.4e" % float(env))
    out['first_ten'] = dict(T=float(Tf), A_T=float(Af), contacts=sorted(terms),
                            cor26=float(lam_bound(Af, Tf)), envelope=float(env))

    print("(iii) T0(A) for a few masses")
    tab = []
    for a in [0.0, 0.25, 0.5, 0.5637, 1.0, 2.0, 4.0, 5.0, 5.3]:
        r = T0_of_A(a)
        tab.append((a, float(r[0])))
        print("     A = %6.4f -> T0 = %10.5f" % (a, float(r[0])))
    out['T0_table'] = tab
    json.dump(out, open('r2_d_subcomb.json', 'w'), indent=1)
