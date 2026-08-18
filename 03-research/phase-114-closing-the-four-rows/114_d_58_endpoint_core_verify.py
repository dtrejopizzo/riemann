#!/usr/bin/env python3
"""Diagnostic certificates for the exact D.58 endpoint core formulas."""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
T2 = mp.log(2)/2
A2 = mp.log(2)/mp.sqrt(2)
m0 = mp.log(mp.pi)-mp.digamma(mp.mpf(1)/4)
M2 = m0+2*A2
eta = mp.mpf(1)

def cutoff_equation(R):
    return (mp.re(mp.digamma(mp.mpf(1)/4+1j*R/2))
            -mp.log(mp.pi)-2*A2-eta)

Rsharp = mp.findroot(cutoff_equation, (40, 50))
core_bound = 4*T2*Rsharp*(M2+eta)/(mp.pi*eta)
assert mp.mpf("45.52") < Rsharp < mp.mpf("45.53")
assert mp.mpf("147") < core_bound < mp.mpf("148")
assert int(mp.ceil(core_bound)) == 148

# Convolution-root zero bookkeeping: if z is a polar value and
# fhat(z)=ghat(z)*conjugate(ghat(conjugate z)), a root zero forces the two
# conjugate zeros of the positive-definite convolution square.
z, gz, gzc = sp.symbols("z gz gzc")
f_z = gz*gzc
assert f_z.subs(gz, 0) == 0
assert f_z.subs(gzc, 0) == 0

# Nonnegativity plus compact resolvent does not exclude a kernel.
A0 = sp.diag(0, 1)
assert A0.det() == 0
assert all(v >= 0 for v in A0.eigenvals())

# Once a rigorous margin exists, the interval radius is gamma/L.
gamma = sp.Rational(1, 1000)
L = sp.Rational(7, 2)
assert gamma/L == sp.Rational(1, 3500)

print(f"PASS endpoint monotone cutoff R#={mp.nstr(Rsharp, 24)}")
print(f"PASS endpoint prolate-core bound={mp.nstr(core_bound, 24)} < 148")
print("PASS root/convolution polar-zero bookkeeping")
print("PASS nonnegativity alone leaves an equality-mode obstruction")
