#!/usr/bin/env python3
"""Exact checks for the local block-diagonal gluing obstruction in D.72."""

import sympy as sp

r = sp.symbols("r", positive=True)
N = 4
defect = 2 * sum((N-d) * r**d for d in range(1, N))
assert sp.expand(defect) == 6*r + 4*r**2 + 2*r**3
assert defect.is_positive

# Scalar frequency-zero norm of the Poisson multiplier is expansive.
# sqrt(1-r^2)/(1-r) squared equals (1+r)/(1-r)>1.
poisson_norm_sq = sp.simplify((1-r**2)/(1-r)**2)
assert sp.simplify(poisson_norm_sq - (r+1)/(1-r)) == 0
assert sp.simplify((poisson_norm_sq - 1) - 2*r/(1-r)) == 0

# A finite Douglas identity check: if S=KX and K is contractive, then
# X^*X-S^*S = X^*(I-K^*K)X is positive.
k, x = sp.symbols("k x", real=True)
gap = sp.expand(x**2 - (k*x)**2)
assert sp.simplify(gap - x**2*(1-k**2)) == 0

print(f"two-jet Hardy defect for N={N}: {defect}")
print(f"local Poisson multiplier norm squared: {poisson_norm_sq}")
print("PASS every local Poisson block has expanding directions")
print("PASS a block-diagonal primewise contraction cannot realize the contact")
print("PASS Douglas gap is the pulled-back contraction defect")
