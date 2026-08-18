#!/usr/bin/env python3
"""Numerical/algebraic certificates for the explicit D.55 cutoff."""
import math
import mpmath as mp
import sympy as sp

mp.mp.dps = 50

def von_mangoldt(n):
    fac = sp.factorint(n)
    if len(fac) != 1:
        return mp.mpf("0")
    p = next(iter(fac))
    return mp.log(p)

def prime_power_mass(T):
    limit = int(mp.floor(mp.e**(2*T)))
    return mp.fsum(von_mangoldt(n)/mp.sqrt(n) for n in range(2, limit+1))

T = mp.mpf("0.5")
eta = mp.mpf(1)
m0 = mp.log(mp.pi)-mp.digamma(mp.mpf(1)/4)
A = prime_power_mass(T)
M = m0+2*A
C = M+eta
N = max(0, int(mp.ceil((mp.e**(2*C)-5)/4)))
R = 2*(mp.mpf(N)+mp.mpf(1)/4)

# Sharp monotone-digamma cutoff (3.8).  The proof uses the positive series;
# here we certify the scalar equation at high precision and compare sizes.
target = 2*A+eta
def mathfrak_a(tau):
    return mp.re(mp.digamma(mp.mpf(1)/4+mp.j*tau/2))-mp.log(mp.pi)

guess = 2*mp.pi*mp.e**target
R_sharp = mp.findroot(lambda x: mathfrak_a(x)-target, guess)
assert R_sharp > 0
assert abs(mathfrak_a(R_sharp)-target) < mp.mpf("1e-40")
assert R_sharp < R

def a_derivative_series(tau, terms=200000):
    x = tau/2
    return (tau/2)*mp.fsum(
        (mp.mpf(j)+mp.mpf(1)/4)/
        ((mp.mpf(j)+mp.mpf(1)/4)**2+x*x)**2
        for j in range(terms)
    )

assert a_derivative_series(R_sharp, 20000) > 0

# The integral lower bound used in (3.3), and the exact partial digamma sum.
integral_bound = mp.log(4*N+5)/2
partial_sum = (mp.digamma(N+mp.mpf(5)/4)-mp.digamma(mp.mpf(1)/4))/2
assert integral_bound >= C
assert partial_sum >= integral_bound

# At tau=R every retained summand has its ratio at least 1/2.
for j in (0, 1, N//2, N):
    a = mp.mpf(j)+mp.mpf(1)/4
    ratio = R**2/(4*a*a+R**2)
    assert ratio >= mp.mpf(1)/2

# Exact finite Schur-complement certificate in a model with D <= -eta/2.
A0 = sp.Matrix([[2, sp.Rational(1, 3)], [sp.Rational(1, 3), -1]])
C0 = sp.Matrix([[1, 0], [sp.Rational(1, 2), 1]])
D0 = sp.diag(-2, -3)
B0 = A0.row_join(C0).col_join(C0.T.row_join(D0))
S0 = sp.simplify(A0-C0*D0.inv()*C0.T)

def inertia(mat):
    import numpy as np
    arr = np.array(mat.evalf(50).tolist(), dtype=float)
    eig = np.linalg.eigvalsh(arr)
    return (int((eig > 1e-10).sum()), int((eig < -1e-10).sum()))

assert inertia(B0)[0] == inertia(S0)[0]
assert max(abs(float(x)) for x in D0.inv().diagonal()) <= 2/float(eta)

# Time-band trace and resulting core bound are finite and explicit.
beta = eta/(2*(M+eta))
trace_C = 2*T*R/mp.pi
dimension_bound = trace_C/beta
sharp_trace_C = 2*T*R_sharp/mp.pi
sharp_dimension_bound = sharp_trace_C/beta
assert beta > 0 and beta < 1
assert dimension_bound > 0 and mp.isfinite(dimension_bound)
assert sharp_dimension_bound < dimension_bound

print(f"PASS complete p^k mass A_T={mp.nstr(A, 16)} at T={T}")
print(f"PASS explicit cutoff N={N}, R={mp.nstr(R, 16)} gives margin eta=1")
print(f"PASS sharp digamma cutoff R#={mp.nstr(R_sharp, 16)} gives the same margin")
print(f"PASS finite prolate-core bound d<={mp.nstr(dimension_bound, 16)}")
print(f"PASS sharp prolate-core bound d<={mp.nstr(sharp_dimension_bound, 16)}")
print("PASS exact Schur complement preserves the positive index")
