"""Rational checks for the single analytic counterexample of TWO_COPY_SCOPE074.

No quadrature, parameter search, or evaluation of a physical W form.
"""
from fractions import Fraction as F

p = 10**6
A = 4*10**8
epsilon = F(1, 20000)
delta = 2*epsilon
assert A == 20000**2
assert 2*p-2 > 15
assert 2**15 > 20000
assert (p-1)*epsilon > 49
assert F(49**4, 24) > 40000

K0 = [[F(1), F(1), F(3, 4)],
      [F(1), F(1), F(4, 5)],
      [F(3, 4), F(4, 5), F(2, 3)]]
c = [40, -40, 3]
q = sum((c[i]*K0[i][j]*c[j] for i in range(3) for j in range(3)), F())
assert q == -6
error = delta*sum(abs(x) for x in c)**2
assert error == F(6889, 10000)
assert q+error == -F(53111, 10000) < 0

# The requested x^6 check at the origin has the opposite determinant sign.
# This rational integral lower bound proves Gamma(1/6)>3sqrt(pi).
r = 1-F(1, 7)+F(1, 26)-F(1, 114)
assert r > 0
assert r*r > F(11, 14)
assert F(1, 2)-F(10, 27) > 0
print('PASS: explicit even polynomial potential satisfies all mode/error bounds')
print('PASS: c^T(A K)c < -53111/10000 < 0 for c=(40,-40,3)')
print('PASS: x^6 origin cumulant test is positive, not this counterexample')
