"""Numerical constants of the paper (mpmath, 40 digits).

Prop. prop:s1   : s_1 = s(gamma_1, pi/2), the maximizer u*, 1 - s_1^2.
Thm. thm:bfalse : the degree threshold d > 1/(1 - s_1^2) at chi = 0.
Remark after it : the instance d = 400, t^2 W = 79780.
Lemma lem:F0    : G = 3 sqrt(2 pi)/2, 2G^2 = 9 pi, the tail bound L.
Prop. prop:sC   : the constants of y^2 + xy = x^3 + 1 over F_2.
"""
from mpmath import mp, mpf, sqrt, pi, sin, cos, cosh, log, exp, acos, atan, findroot, diff

mp.dps = 40
g1 = mpf('14.134725141734693790457251983562')

# Prop. prop:s1
f = lambda u: sin(g1 * u) / cosh(u / 2)
u = findroot(lambda x: diff(f, x), mpf('0.111'))
s1 = f(u)
print('u* =', u)
print('s_1 =', s1, ' 1-s_1^2 =', 1 - s1**2)
grid = max(abs(f(mpf(k) / 10**5)) for k in range(-40000, 40001))
print('grid max on |u|<=0.4 =', grid, ' bound outside 1/cosh(0.2) =', 1 / cosh(mpf('0.2')))
s1p = s1 + mpf(10)**-89
print('d-threshold (chi=0) =', 1 / (1 - s1p**2))
print('1/s_1 =', 1 / s1)

# Lemma lem:F0
G = 3 * sqrt(2 * pi) / 2
print('G =', G, ' 2G^2 =', 2 * G**2, ' 9pi =', 9 * pi)
L = G * exp(mpf(9) / 8) * sum(20 * log(T) * exp(-mpf(9) / 2 * (T - g1)**2) for T in range(21, 200))
print('L bound =', mp.nstr(L, 5))

# Remark: instance
d, t2, W = 400, mpf(79780), 9 * pi
t = sqrt(t2 / W)
print('t =', t, ' I(E,E) =', d**2 / mpf(2) - t2, ' R(E) =', d**2 / mpf(4) - t2 / 2 - d / mpf(4))
print('tG =', t * G, ' s_1 d/2 =', s1 * d / 2, ' window lower =', s1p**2 * 80000)

# Prop. prop:sC
q, a = 2, -1
th = acos(mpf(a) / (2 * sqrt(q)))
ts = atan((q + 1 + a) / sqrt(4 * q - a * a))
print('s_C(pi/2) =', sqrt(4 * q - a * a) / (q + 1), ' sqrt7/3 =', sqrt(7) / 3)
print('s_C* =', sqrt(mpf(7) / 11))
ent = [(n, abs(cos(n * th + ts)) / cosh(n * log(q) / 2)) for n in range(-8, 9)]
for n, e in ent:
    print('  n =', n, mp.nstr(e, 8))
print('curve window t in (', sqrt(mpf(7) / 11) * 3 / 2, ',', sqrt(mpf(6)) / 2, ')')
