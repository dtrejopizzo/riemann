#!/usr/bin/env python3
"""Exact rational certificates used in the D.57 interval audit."""
from fractions import Fraction
import sympy as sp

def log_interval(n, terms):
    """Rational enclosure from the atanh series for log(n)."""
    z = Fraction(n-1, n+1)
    lower = Fraction(0)
    for r in range(terms+1):
        lower += 2*z**(2*r+1)/Fraction(2*r+1)
    remainder = 2*z**(2*terms+3)/(
        Fraction(2*terms+3)*(1-z*z))
    return lower, lower+remainder

# Prove the rational test interval is strictly in (log2/2, log3/2).
l2, u2 = log_interval(2, 20)
l3, u3 = log_interval(3, 40)
left = Fraction(347, 1000)
right = Fraction(87, 250)
assert u2/2 < left < right < l3/2

# Exact startup no-go: semidefinite base plus an arbitrarily small
# indefinite entering direction need not stay nonnegative.
eps = sp.symbols("eps", positive=True)
A0 = sp.diag(0, 1)
H = sp.diag(-1, 0)
assert (A0+eps*H).det() == -eps
assert (sp.Matrix([1, 0]).T*(A0+eps*H)*sp.Matrix([1, 0]))[0] == -eps

# Symbolic derivative of the Feshbach matrix.
t = sp.symbols("t", real=True)
a = sp.Function("a")(t)
c = sp.Function("c")(t)
d = sp.Function("d")(t)
S = a-c**2/d
claimed = sp.diff(a, t)-2*c*sp.diff(c, t)/d+c**2*sp.diff(d, t)/d**2
assert sp.simplify(sp.diff(S, t)-claimed) == 0

# Exact scalar propagation example: a margin mu and Lipschitz constant L
# certify the interval |t-tc|<mu/L.
mu = Fraction(3, 20)
L = Fraction(7, 5)
radius = mu/L
assert radius == Fraction(3, 28)

print("PASS rational log enclosures place J0 strictly between 2 and 3")
print("PASS semidefinite startup plus an arbitrarily small hinge can turn negative")
print("PASS exact Feshbach derivative formula")
print("PASS margin-over-derivative interval radius is rationally certified")
