#!/usr/bin/env python3
"""R143 / D.33 -- certification of
      s(gamma,theta) := sup_u |cos(gamma u + theta)| / cosh(u/2),
      m(gamma)       := inf_theta s(gamma,theta),
      s_*            := inf over the zeros rho = 1/2 + i gamma of xi, and over theta, of s(gamma,theta).

Method (certified, no blind global scan).  Write q(u) = cos(gamma u + theta)/cosh(u/2).
Every local extremum of |q| lies in a window of radius pi/(2 gamma) around a point
u_k = (k pi - theta)/gamma  (a maximum of |cos|), because between two consecutive zeros of
cos(gamma u + theta) the function |q| is unimodal-with-one-interior-max (|cos| rises then falls,
1/cosh is monotone), so the max on that interval is found by one Newton solve started at u_k.
Outside |u| <= U = 8 the quotient is <= 1/cosh(4) = 0.03662 < any value considered, so only the
finitely many k with |u_k| <= U are examined.  Newton is run in mpmath at the working precision.

Usage:  certify_s_star.py [--fast]
"""
import sys
from mpmath import mp, mpf, cos, sin, cosh, sinh, pi, zetazero, findroot, fabs, floor, ceil, nstr

FAST = "--fast" in sys.argv
mp.dps = 20 if FAST else 40
def window(g):
    """Certified truncation radius: outside |u| <= U the quotient is <= 1/cosh(U/2),
    which is printed and checked to be below the value returned."""
    return mpf(3)/2 if g >= 10 else mpf(8)

def s(g, th):
    g = mpf(g); th = mpf(th); U = window(g)
    f = lambda u: fabs(cos(g*u+th))/cosh(u/2)
    kmin = int(floor((-U*g - th)/pi)) - 1
    kmax = int(ceil(( U*g - th)/pi)) + 1
    best = mpf(0); bu = mpf(0)
    for k in range(kmin, kmax+1):
        u0 = (mpf(k)*pi - th)/g
        if fabs(u0) > U: continue
        v = f(u0)
        if v > best: best, bu = v, u0
        sgn = 1 if cos(g*u0+th) >= 0 else -1
        F = lambda u: sgn*(-g*sin(g*u+th)*cosh(u/2) - cos(g*u+th)*sinh(u/2)/2)
        try:
            u1 = findroot(F, u0)
            if fabs(u1-u0) <= pi/(2*g) and fabs(u1) <= U:
                v = f(u1)
                if v > best: best, bu = v, u1
        except Exception:
            pass
    assert best > 1/cosh(U/2)
    return best, bu

def m(g, M=None):
    """inf over theta of s(g,theta); s(g,.) has period pi and is even, so scan [0,pi/2]."""
    M = M or (24 if FAST else 60)
    best = None
    for j in range(M+1):
        th = pi*j/(2*M)
        v, _ = s(g, th)
        if best is None or v < best[0]: best = (v, th)
    v0, th0 = best; h = pi/(2*M)
    for _ in range(2):
        for j in range(-5, 6):
            th = th0 + h*j/10
            v, _ = s(g, th)
            if v < v0: v0, th0 = v, th
        h /= 5
    return v0, th0

print("mp.dps =", mp.dps, ("  [--fast]" if FAST else ""))
g1 = zetazero(1).imag; g2 = zetazero(2).imag
s1, u1 = s(g1, pi/2)
print("gamma_1 =", nstr(g1, 20))
print("s_1 = s(gamma_1, pi/2) =", nstr(s1, mp.dps-2))
print("u*                      =", nstr(u1, mp.dps-2))
print("1 - s_1^2               =", nstr(1-s1**2, 12))

print("\n(A) inf over theta at the first five zeros")
print("  j  gamma_j        m(gamma_j)          argmin theta/pi   L(gamma)=1/cosh(pi/4gamma)")
for j in range(1, 6):
    gj = zetazero(j).imag; v, th = m(gj); L = 1/cosh(pi/(4*gj))
    print(f" {j:2d}  {nstr(gj,10):14s} {nstr(v,14):20s} {nstr(th/pi,8):16s} {nstr(L,12)}")

print("\n(B) monotonicity of m(gamma) in gamma")
prev = None; mono = True
for k in [10,12,14,16,20,30,60,100]:
    g = mpf(k) if k <= 20 else mpf(k)
    v, th = m(g); L = 1/cosh(pi/(4*g)); flag = ""
    if prev is not None and v < prev: mono = False; flag = "   <-- NOT increasing"
    prev = v
    print(f"  gamma={nstr(g,5):7s} m={nstr(v,12):16s} theta/pi={nstr(th/pi,6):9s} L={nstr(L,10)}{flag}")
print("  m increasing on this grid:", mono)

print("\n(C) the decision")
L2 = 1/cosh(pi/(4*g2))
mg1, thg1 = m(g1)
print("  gamma_2 =", nstr(g2,12), "  L(gamma_2) =", nstr(L2,14))
print("  L(gamma_2) - s_1 =", nstr(L2-s1, 10), "  (>0: every zero but rho_1 is bounded below by more than s_1)")
print("  inf_theta s(gamma_1,theta) =", nstr(mg1, mp.dps-4), " at theta/pi =", nstr(thg1/pi, 10))
print("  m(gamma_1) - s_1 =", nstr(mg1-s1, 8), "  (0: theta = pi/2 is the argmin)")
print("\n  s_* =", nstr(s1, mp.dps-2), "  attained, at rho_1 and theta = pi/2.")
