"""R156_001 DIAGNOSTIC: parity Green/Schur channels of the complete Weil form at a window.

Galerkin (orthonormal Legendre basis of L^2(-T,T)) evaluation of
  a_T(F)  = C0|F|^2 + int_0^inf (|F|^2 - c_F(u)) K(u) du - sum_{n<e^{2T}} v_n c_F(log n)   (P47 eq:Aform)
  W_T(F)  = a_T(F) + 2 A(F) B(F)                                                            (P47 eq:W)
and of the channel constants
  kappa_+ = inf{ a_T(F) : F even, int F cosh(t/2) = 1 },  kappa_- = inf{ a_T(F) : F odd, int F sinh(t/2) = 1 }.
Galerkin values are variational UPPER bounds on every infimum printed (lambda's and kappa's).
Flags: --noprimes  (prime-free model v=0, i.e. the archimedean form A_inf of P47 sec:archstr).
Usage: python3 r156_green_matrix.py T N [--noprimes]
"""
import sys
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from scipy.special import digamma
from sympy import primerange  # only for Lambda(n)
import math

def vonmangoldt(n):
    for p in primerange(2, n + 1):
        k = n
        e = 0
        while k % p == 0:
            k //= p; e += 1
        if e > 0:
            return math.log(p) if k == 1 else 0.0
    return 0.0

def basis(t, T, N):
    # orthonormal Legendre e_j(t) = sqrt((2j+1)/2T) P_j(t/T), rows j
    V = legvander(t / T, N - 1).T
    return V * np.sqrt((2 * np.arange(N) + 1) / (2 * T))[:, None]

def Mshift(u, T, N, q):
    # M_jk(u) = int e_j(t) e_k(t-u) dt over t in (u-T, T), u in [0,2T]
    x, w = leggauss(q)
    a, b = u - T, T
    t = 0.5 * (b - a) * x + 0.5 * (b + a); wt = 0.5 * (b - a) * w
    E1 = basis(t, T, N); E2 = basis(t - u, T, N)
    return (E1 * wt) @ E2.T

def build(T, N, primes=True):
    q = N + 4
    C0 = digamma(0.25) - math.log(math.pi)
    tail = math.log(1 / math.tanh(T / 2)) + math.pi - 2 * math.atan(math.exp(T))
    K = lambda u: 1 / (2 * np.sinh(u / 2)) + 1 / (2 * np.cosh(u / 2))
    xu, wu = leggauss(120)
    u = T * (xu + 1); wuu = T * wu
    G = (C0 + tail) * np.eye(N)
    for ui, wi in zip(u, wuu):
        M = Mshift(ui, T, N, q); S = 0.5 * (M + M.T)
        G += wi * K(ui) * (np.eye(N) - S)
    P = np.zeros((N, N))
    if primes:
        for n in range(2, int(math.exp(2 * T)) + 2):
            if math.log(n) < 2 * T:
                L = vonmangoldt(n)
                if L > 0:
                    M = Mshift(math.log(n), T, N, q); S = 0.5 * (M + M.T)
                    P -= 2 * L / math.sqrt(n) * S
    x, w = leggauss(q + 40)
    t = T * x; wt = T * w
    E = basis(t, T, N)
    Avec = E @ (wt * np.exp(t / 2)); Bvec = E @ (wt * np.exp(-t / 2))
    a = G + P
    Wm = a + np.outer(Avec, Bvec) + np.outer(Bvec, Avec)
    return a, Wm, Avec, Bvec

def bordered_kappa(a, c):
    n = len(c)
    M = np.zeros((n + 1, n + 1)); M[:n, :n] = a; M[:n, n] = c; M[n, :n] = c
    return -np.linalg.inv(M)[n, n]

def restricted_min(a, C):
    # bottom of a on {x : C x = 0}
    Q, _ = np.linalg.qr(C.T, mode='complete')
    Z = Q[:, C.shape[0]:]
    return np.linalg.eigvalsh(Z.T @ a @ Z)[0]

if __name__ == '__main__':
    T = float(sys.argv[1]); N = int(sys.argv[2]); primes = '--noprimes' not in sys.argv
    a, Wm, A, B = build(T, N, primes)
    ev = np.arange(0, N, 2); od = np.arange(1, N, 2)
    c = 0.5 * (A + B); s = 0.5 * (A - B)          # int e_j cosh(t/2), int e_j sinh(t/2)
    ae, ao = a[np.ix_(ev, ev)], a[np.ix_(od, od)]
    lamW_e = np.linalg.eigvalsh(Wm[np.ix_(ev, ev)])[0]; lamW_o = np.linalg.eigvalsh(Wm[np.ix_(od, od)])[0]
    lamA_e = restricted_min(ae, c[ev][None, :]); lamA_o = restricted_min(ao, s[od][None, :])
    kp = bordered_kappa(ae, c[ev]); km = bordered_kappa(ao, s[od])
    lama_e = np.linalg.eigvalsh(ae)[0]; lama_o = np.linalg.eigvalsh(ao)[0]
    print(f"T={T} N={N} primes={primes}")
    print(f"  bottom a_T on L2  even {lama_e:+.6f}  odd {lama_o:+.6f}")
    print(f"  lamA (a on P_T)   even {lamA_e:+.4e}  odd {lamA_o:+.4e}")
    print(f"  lamW (W on L2)    even {lamW_e:+.3e}  odd {lamW_o:+.3e}")
    print(f"  kappa_+ = {kp:+.6f}  g_+ = kappa_+ + 2 = {kp + 2:+.3e}")
    print(f"  kappa_- = {km:+.6f}  g_- = kappa_- - 2 = {km - 2:+.3e}")
    print(f"  |cosh|^2 = {math.sinh(T) + T:.6f}   |sinh|^2 = {math.sinh(T) - T:.6f}")
