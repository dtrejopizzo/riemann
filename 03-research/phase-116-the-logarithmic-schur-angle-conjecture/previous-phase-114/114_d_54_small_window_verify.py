#!/usr/bin/env python3
"""Certificates for the unconditional D.54 small-window threshold."""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
m0 = mp.log(mp.pi)-mp.digamma(mp.mpf(1)/4)

def twice_tail(T):
    x = mp.e**(-T)
    return mp.log((1+x)/(1-x))+2*mp.atan(x)

def delta(T):
    return twice_tail(T)-m0-4*mp.sinh(T)

T0 = mp.findroot(delta, (mp.mpf("0.03"), mp.mpf("0.05")))
assert mp.mpf("0.0371") < T0 < mp.mpf("0.0372")
assert T0 < mp.log(2)/2
assert delta(mp.mpf("0.03")) > 0
assert delta(mp.mpf("0.04")) < 0
assert abs(delta(T0)) < mp.mpf("1e-50")

# Symbolic derivative of the exact threshold function.
T = sp.symbols("T", positive=True)
x = sp.exp(-T)
d = sp.log((1+x)/(1-x))+2*sp.atan(x)-4*sp.sinh(T)
claimed = -1/sp.sinh(T)-1/sp.cosh(T)-4*sp.cosh(T)
assert sp.simplify((sp.diff(d, T)-claimed).rewrite(sp.exp)) == 0

# Exact TP2-sign failure for the Gamma density.
r, h = sp.symbols("r h", positive=True)
w = lambda z: sp.exp(-z/2)/(1-sp.exp(-2*z))
minor = sp.factor(w(r)**2-w(r-h)*w(r+h))
# A numerical rational-point certificate complements the symbolic formula.
assert sp.N(minor.subs({r: 2, h: sp.Rational(1, 2)}), 40) < 0

# Exact polar estimate in a finite Hilbert model: 2 Re(a conjugate b)
# is bounded below by -|a|^2-|b|^2.
a, b = sp.symbols("a b", real=True)
assert sp.expand(2*a*b+a**2+b**2-(a+b)**2) == 0

print(f"PASS unique small-window threshold T0={mp.nstr(T0, 24)}")
print("PASS delta is strictly decreasing and changes sign across T0")
print("PASS Gamma density has the wrong strict TP2 minor sign")
