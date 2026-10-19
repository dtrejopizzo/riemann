"""R156_001: elementary (PROVED-grade) odd witnesses for the one-contact family at T=(1/2)log3,
W_theta(F) = A_inf(F) - theta*v_2*c_F(log 2),  v_2 = 2 log2/sqrt2  (theta=1: zeta; theta=0: prime-free).
F = t + b3 t^3 + b5 t^5 (odd, rational b's).  Upper bound U_theta(F) uses K(u) <= 1/u + 1/2 on (0,2T) against
g = c_F(0) - c_F(u) >= 0 (Cauchy-Schwarz); all other terms are exact closed forms. Prints the largest theta
for which U_theta(F) < 0, i.e. W_theta has a negative direction (so lamW(theta) < 0), with sympy exact evaluation.
Usage: python3 r156_theta_witness.py"""
import sympy as sp, numpy as np
from scipy.optimize import minimize
u, t = sp.symbols('u t', real=True); b3, b5 = sp.symbols('b3 b5', real=True)
T = sp.log(3) / 2
F = t + b3 * t**3 + b5 * t**5
c = sp.expand(sp.integrate(sp.expand(F * F.subs(t, t - u)), (t, u - T, T)))
c0 = sp.expand(c.subs(u, 0)); g = sp.expand(c0 - c)
body = sp.integrate(sp.expand(sp.cancel(g / u)) + g / 2, (u, 0, 2 * T))
s = sp.integrate(sp.expand(F * sp.sinh(t / 2)), (t, -T, T))
C0 = -sp.EulerGamma - sp.pi / 2 - 3 * sp.log(2) - sp.log(sp.pi)
tail = sp.log(1 / sp.tanh(T / 2)) + sp.pi - 2 * sp.atan(sp.exp(T))
v2 = 2 * sp.log(2) / sp.sqrt(2)
U0 = c0 * (C0 + tail) + body - 2 * s**2          # upper bound on A_inf(F)
P = -v2 * c.subs(u, sp.log(2))                   # prime form at theta=1 (exact)
fU0 = sp.lambdify((b3, b5), U0, 'numpy'); fP = sp.lambdify((b3, b5), P, 'numpy')
def theta_max(x):
    U, p = fU0(*x), fP(*x)
    return (-U / p) if (U < 0 and p > 0) else (0.0 if U < 0 and p <= 0 else -1.0)
best = None
for start in [(0, 0), (-1, 0), (-3, 1), (2, -1), (-5, 5)]:
    r = minimize(lambda x: -theta_max(x), start, method='Nelder-Mead', options={'xatol': 1e-8, 'fatol': 1e-10, 'maxiter': 4000})
    if best is None or -r.fun > best[0]: best = (-r.fun, r.x)
th, x = best
q3, q5 = sp.Rational(round(x[0] * 10**6), 10**6), sp.Rational(round(x[1] * 10**6), 10**6)
Ue = sp.N(U0.subs({b3: q3, b5: q5}), 30); Pe = sp.N(P.subs({b3: q3, b5: q5}), 30)
print("F = t + (%s) t^3 + (%s) t^5" % (q3, q5))
print("upper bound on A_inf(F):", Ue, "   prime form P(F) = -v2 c_F(log2):", Pe)
print("W_theta(F) < 0 for every theta <", sp.N(-Ue / Pe, 12) if Pe > 0 else "all theta")
tt = sp.Rational(1, 1)
print("t-witness alone (b3=b5=0): U =", sp.N(U0.subs({b3: 0, b5: 0}), 15), " P =", sp.N(P.subs({b3: 0, b5: 0}), 15),
      " theta bound =", sp.N(-U0.subs({b3: 0, b5: 0}) / P.subs({b3: 0, b5: 0}), 12))
