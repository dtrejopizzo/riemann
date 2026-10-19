#!/usr/bin/env python3
"""BARRIER_Y_001 independent high-precision check (NUMÉRICO, mpmath 30 digits, not interval):
evaluate a_T^{(Lambda_q)}(F)/||F||^2 by P47 eq:Aform for an explicit polynomial F in P_T (Tate moments
enforced exactly in mp), F taken from a small Galerkin solve.  Negative value => WP_T(Lambda_q) fails
(any F in P_T is an upper bound for the bottom)."""
import sys, numpy as np, mpmath as mp, y001_farkas_signs as Y
mp.mp.dps = 30
def check(T, q, M=14):
    W = Y.Win(T, M); a = {n: np.log(p) for n, p in W.cont}; a[q] = 0.0
    ev, h = W.bottom(a)
    Tm = mp.mpf(T); coef = [mp.mpf(float(x)) for x in h]
    def F0(t):
        u = t / Tm; P = [mp.mpf(1), u]
        for k in range(1, M - 1): P.append(((2*k+1)*u*P[k] - k*P[k-1]) / (k+1))
        return mp.fsum(coef[k]*P[k]*mp.sqrt((2*k+1)/(2*Tm)) for k in range(M))
    # enforce A(F)=B(F)=0 exactly: F = F0 - al*1 - be*t
    I = lambda f: mp.quad(f, [-Tm, 0, Tm])
    A0, B0 = I(lambda t: F0(t)*mp.e**(t/2)), I(lambda t: F0(t)*mp.e**(-t/2))
    a11, a12 = I(lambda t: mp.e**(t/2)), I(lambda t: t*mp.e**(t/2))
    b11, b12 = I(lambda t: mp.e**(-t/2)), I(lambda t: t*mp.e**(-t/2))
    al, be = mp.lu_solve(mp.matrix([[a11, a12], [b11, b12]]), mp.matrix([A0, B0]))
    F = lambda t: F0(t) - al - be*t
    c = lambda u: mp.quad(lambda t: F(t)*F(t-u), [-Tm+u, Tm]) if u < 2*Tm else mp.mpf(0)
    c0 = c(mp.mpf(0)); C0 = mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi)
    K = lambda u: 2*mp.e**(-u/2)/(1-mp.e**(-2*u))
    E = mp.quad(lambda u: (c0 - c(u))*K(u), mp.linspace(0, 2*Tm, 9)) + c0*mp.quad(K, [2*Tm, mp.inf])
    comb = mp.fsum(2*mp.mpf(a[n])/mp.sqrt(n)*c(mp.log(n)) for n, _ in W.cont if a[n] != 0)
    val = (C0*c0 + E - comb)/c0
    print(f"T={T:.6f} delete q={q}: Galerkin(M={M}) {ev[0]:+.6e} | mp Rayleigh quotient {mp.nstr(val, 12)}  (Tate fix |al|,|be|={mp.nstr(abs(al),3)},{mp.nstr(abs(be),3)})", flush=True)
for T, q in ((0.75, 3), (0.5*np.log(5)+0.01, 3), (1.0, 7), (np.log(3)-1e-6, 8)):
    check(T, q)
