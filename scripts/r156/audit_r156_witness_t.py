"""R156_004 (hostile audit): interval-arithmetic re-verification of the load-bearing witness of R156_001 Thm 3.1.

Claim audited: for F_T(t) = t on I_T = (-T,T) (odd, real), with P47 eq:Aform / sec:archstr,
    A_inf(F) = 2A(F)B(F) + C0|F|^2 + Lev(c_F),   Lev(c) = int_0^inf (c(0) - c(u)) K(u) du,
and the elementary bound K(u) <= 1/u + 1/2 on (0, 2T) against g(u) = c_F(0) - c_F(u) >= 0,
    A_inf(F_T) <= U(T) := (2T^3/3)(C0 + log coth(T/2) + pi - 2 arctan e^T) + 2T^3(3T+7)/9 - 2 s(T)^2,
    s(T) = 4T cosh(T/2) - 8 sinh(T/2),   C0 = -gamma - pi/2 - 3 log 2 - log pi.
Load-bearing value: U(0.461) < 0 (then lambda_inf(T) < 0 for all T >= 0.461 by prop:arch(i)).

Everything is evaluated in mpmath interval arithmetic (iv, outward rounding). pi - 2 arctan(e^T) = 2 arctan(e^{-T})
is enclosed by the alternating Taylor series of arctan on (0,1) with the next term as remainder bound.
Part (b) re-derives the polynomial pieces symbolically (sympy, exact) so the closed forms are not taken on trust.
Part (c) is an INDEPENDENT (non-interval, DIAGNOSTIC) evaluation of A_inf(F_T) from the Fourier definition
(1/2pi) int m |F^|^2 + 2AB, m(tau) = Re psi(1/4 + i tau/2) - log pi, bypassing the Levy representation, as a
sign-convention check (auditor doubt 3).  Runtime < 60 s.
"""
import sympy as sp
import mpmath as mp
from mpmath import iv

iv.dps = 40

def iv_atan_small(y, nterms=400):
    # y an interval inside (0,1); arctan y = sum_{k>=0} (-1)^k y^{2k+1}/(2k+1), alternating, terms decreasing
    s = iv.mpf(0)
    for k in range(nterms):
        s += (-1) ** k * y ** (2 * k + 1) / (2 * k + 1)
    rem = y ** (2 * nterms + 1) / (2 * nterms + 1)
    return s + iv.mpf([-1, 1]) * rem

def U_iv(T):
    eT = iv.exp(T); emT = iv.exp(-T)
    ch = (iv.exp(T / 2) + iv.exp(-T / 2)) / 2; sh = (iv.exp(T / 2) - iv.exp(-T / 2)) / 2
    C0 = -iv.euler - iv.pi / 2 - 3 * iv.log(2) - iv.log(iv.pi)
    tail = iv.log((eT + 1) / (eT - 1)) + 2 * iv_atan_small(emT)
    s = 4 * T * ch - 8 * sh
    return (2 * T ** 3 / 3) * (C0 + tail) + 2 * T ** 3 * (3 * T + 7) / 9 - 2 * s ** 2

# (a) interval values
for Ts in ['0.461', '0.4608', '0.47']:
    print(f"U({Ts}) in {U_iv(iv.mpf(Ts))}")
print("U(1/2 log 3) in", U_iv(iv.log(3) / 2))

# (b) symbolic re-derivation of the closed forms
t, u, T = sp.symbols('t u T', positive=True)
c = sp.expand(sp.integrate(t * (t - u), (t, u - T, T)))
print("c_F(u) == (2T-u)(2T^2-2Tu-u^2)/6 :", sp.simplify(c - (2*T - u)*(2*T**2 - 2*T*u - u**2)/6) == 0)
g = sp.expand(c.subs(u, 0) - c)
print("g(u) == u(6T^2-u^2)/6 :", sp.simplify(g - u*(6*T**2 - u**2)/6) == 0, "; ||F||^2 =", sp.factor(c.subs(u, 0)))
body = sp.integrate(sp.expand(g / u + g / 2), (u, 0, 2 * T))
print("int_0^{2T} g (1/u+1/2) == 2T^3(3T+7)/9 :", sp.simplify(body - 2*T**3*(3*T + 7)/9) == 0)
sT = sp.integrate(t * sp.sinh(t / 2), (t, -T, T))
print("s(T) == 4T cosh(T/2) - 8 sinh(T/2) :", sp.simplify((sT - (4*T*sp.cosh(T/2) - 8*sp.sinh(T/2))).rewrite(sp.exp)) == 0)
print("tail check (numeric, T=0.461):", mp.nstr(mp.quad(lambda y: 1/(2*mp.sinh(y/2)) + 1/(2*mp.cosh(y/2)), [mp.mpf('0.922'), mp.inf]), 20),
      mp.nstr(mp.log(mp.coth(mp.mpf('0.461')/2)) + mp.pi - 2*mp.atan(mp.exp(mp.mpf('0.461'))), 20))
print("psi(1/4) == -gamma - pi/2 - 3log2 :", mp.nstr(mp.digamma(0.25) - (-mp.euler - mp.pi/2 - 3*mp.log(2)), 5))

# (c) independent Fourier-side evaluation (DIAGNOSTIC, float64), T = 1/2 log 3 and T = 0.461.
# (1/2pi) int_R m |F^|^2 = (1/pi) int_0^inf m |F^|^2, |F^(tau)|^2 = 4 (sin x - x cos x)^2 / tau^4, x = tau T.
# Integrated on [0, L] period by period; tail beyond L by the asymptotic m ~ log(tau/2) - log pi, <cos^2> = 1/2.
import numpy as np
from scipy.special import psi as cpsi
from scipy.integrate import quad
def Ainf_fourier(Tv, L=4000.0):
    m = lambda tau: np.real(cpsi(0.25 + 0.5j * tau)) - np.log(np.pi)
    def Fh2(tau):
        x = tau * Tv
        if x < 1e-3:
            return (2 * Tv ** 3 / 3 * tau) ** 2 * (1 - x * x / 5) ** 2
        return 4 * (np.sin(x) - x * np.cos(x)) ** 2 / tau ** 4
    per = np.pi / Tv; edges = np.arange(0, L + per, per)
    I = sum(quad(lambda tau: m(tau) * Fh2(tau), a, b, epsabs=1e-14, epsrel=1e-12)[0] for a, b in zip(edges[:-1], edges[1:]))
    Le = edges[-1]
    tail = 2 * Tv ** 2 * (np.log(Le / (2 * np.pi)) + 1) / Le     # int_Le^inf log(tau/2pi) * 2T^2/tau^2
    sv = 4 * Tv * np.cosh(Tv / 2) - 8 * np.sinh(Tv / 2)
    return (I + tail) / np.pi - 2 * sv ** 2          # odd F: A = s, B = -s, 2AB = -2 s^2
for Tv in [np.log(3) / 2, 0.461]:
    print(f"A_inf(t) at T={Tv:.8f} via Fourier side (DIAGNOSTIC) = {Ainf_fourier(Tv):.9f}")
