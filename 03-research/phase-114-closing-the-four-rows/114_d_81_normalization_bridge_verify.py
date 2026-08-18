#!/usr/bin/env python3
"""Independent symbolic audit of the D.81 sign/normalization components.

This checks the formulas on a small Fourier band without importing the
external ancillary.  The archimedean nonconstant entries remain sourced to
the primary closed-form lemma; this script checks their constant convention.
"""
import sympy as sp

L = sp.symbols("L", positive=True, real=True)
pi = sp.pi
I = sp.I

# Rephase the centered normalized Fourier modes by (-1)^n.  Their two
# boundary moments are then the following rational functions.
def moment_plus(n):
    return 2*sp.sinh(L/4)/(sp.sqrt(L)*(sp.Rational(1, 2)+2*pi*I*n/L))

def moment_minus(n):
    return sp.conjugate(moment_plus(n))

pref = 32*L*sp.sinh(L/4)**2
for m in range(-3, 4):
    for n in range(-3, 4):
        # M^* C M with C exchanging the + and - moments.
        direct = (sp.conjugate(moment_plus(m))*moment_minus(n)
                  + sp.conjugate(moment_minus(m))*moment_plus(n))
        closed = pref*(L**2-16*pi**2*m*n)/(
            (L**2+16*pi**2*m*m)*(L**2+16*pi**2*n*n))
        assert sp.simplify(sp.together(direct-closed)) == 0

# Prime source: its divided-difference matrix is exactly the contact entry.
y = sp.symbols("y", real=True)
for m in range(-3, 4):
    for n in range(-3, 4):
        if m == n:
            direct = 2*(1-y/L)*sp.cos(2*pi*n*y/L)
        else:
            direct = ((sp.sin(2*pi*m*y/L)-sp.sin(2*pi*n*y/L))
                      /(pi*(n-m)))
        # This is the derivative/divided difference of
        # psi_y(x)=sin(2*pi*x*(1-y/L))/pi, with the sign convention W_p.
        x = sp.symbols("x")
        psi = sp.sin(2*pi*x*(1-y/L))/pi
        if m == n:
            source = sp.diff(psi, x).subs(x, n)
        else:
            source = (psi.subs(x, m)-psi.subs(x, n))/(m-n)
        assert sp.simplify(sp.trigsimp(direct-source)) == 0
        # At q=4, y=L, both the source and every contact entry vanish.
        assert sp.simplify(direct.subs(y, L)) == 0

# Gamma constant convention used in D.77/D.79.
m0_phase114 = sp.log(pi)+sp.EulerGamma+pi/2+3*sp.log(2)
quarter_value = -sp.EulerGamma-pi/2-3*sp.log(2)
assert sp.simplify(m0_phase114-(sp.log(pi)-quarter_value)) == 0

print("PASS D81 polar, prime, q=4-boundary, and Gamma-constant bridge")
