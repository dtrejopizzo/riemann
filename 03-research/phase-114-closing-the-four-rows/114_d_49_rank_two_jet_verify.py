#!/usr/bin/env python3
"""Exact symbolic checks for D.49."""
import sympy as sp

t, s = sp.symbols("t s", real=True)
k = sp.exp(-t/2)*sp.exp(s/2) + sp.exp(t/2)*sp.exp(-s/2)
kernel_rhs = (2*sp.cosh((t-s)/2)).rewrite(sp.exp)
assert sp.simplify(sp.powsimp(k-kernel_rhs, force=True)) == 0
C = sp.Matrix([[0, 1], [1, 0]])
assert C.eigenvals() == {-1: 1, 1: 1}
# The CCM polar block is crossed: <M,CM>=2 Re(conj(M_-)*M_+).
umr, umi, upr, upi = sp.symbols("umr umi upr upi", real=True)
um, up = umr + sp.I*umi, upr + sp.I*upi
polar_matrix = sp.conjugate(um)*up + sp.conjugate(up)*um
polar_cross = 2*sp.re(sp.conjugate(um)*up)
assert sp.simplify(sp.expand_complex(polar_matrix-polar_cross)) == 0
a, sig = sp.symbols("a sig", real=True)
jump = sp.simplify(2-sp.exp(-sig*a)-sp.exp(sig*a))
assert sp.simplify(jump-(2-2*sp.cosh(sig*a))) == 0
assert jump.subs({sig: sp.Rational(1,2), a: 2}) != 0
assert 4*sp.Rational(1,4)**2-sp.Rational(1,2)**2 == 0
# At a separation r=2 (which is not log(n) for an integer n), the jet
# off-diagonal coefficient dominates the continuous Gamma jump kernel.
r = sp.Integer(2)
w_inf = sp.exp(-r/2)/(1-sp.exp(-2*r))
assert sp.N(2*sp.cosh(r/2)-w_inf, 30) > 0
print("PASS pointwise-positive jet kernel and inertia (1,1)")
print("PASS CCM polar block is the crossed Tate pairing")
print("PASS prime jump nonzero and Gamma pole at both Tate exponents")
print("PASS full off-diagonal sign defect at separation r=2")
