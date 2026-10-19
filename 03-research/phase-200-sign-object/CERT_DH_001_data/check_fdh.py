#!/usr/bin/env python3
"""CERT_DH_001 step 1: F_DH exact data, FE check, off-line zero check, b_n = coefficients of -F'/F."""
import mpmath as mp
mp.mp.dps = 30
s5 = mp.sqrt(5); kap = (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)
chi = {0: 0, 1: 1, 2: 1j, 4: -1, 3: -1j}          # chi(2)=i, chi(4)=-1, chi(3)=chi(2)^3=-i
a = {r: mp.re((1 - 1j*kap)*chi[r]) for r in range(5)}
print('kappa =', kap); print('a_1..a_5 =', [a[r % 5] for r in range(1, 6)])
# check: a_n = 1/2(1-ik)chi + 1/2(1+ik)conj(chi) is real
for r in range(5):
    v = (1-1j*kap)/2*chi[r] + (1+1j*kap)/2*mp.conj(chi[r]); assert abs(mp.im(v)) < 1e-25 and abs(mp.re(v)-a[r]) < 1e-25
F = lambda s: sum(a[r]*mp.zeta(s, mp.mpf(r)/5) for r in range(1, 5)) / mp.power(5, s)
Lam = lambda s: mp.power(5/mp.pi, s/2)*mp.gamma((s+1)/2)*F(s)
for s in [mp.mpc(0.3, 2), mp.mpc(0.8, 17.5), mp.mpc(2, -5)]:
    print('FE check s=', s, ' |Lam(s)-Lam(1-s)|/|Lam(s)| =', mp.nstr(abs(Lam(s)-Lam(1-s))/abs(Lam(s)), 5))
rho = mp.findroot(F, mp.mpc(0.808517, 85.699348)); print('off-line zero rho =', rho, '|F(rho)| =', mp.nstr(abs(F(rho)), 3))
print('dual zero 1-conj(rho):', mp.nstr(abs(F(1-mp.conj(rho))), 3))
# b_n recursion
N = 60; b = {}
for n in range(2, N+1):
    b[n] = a[n % 5]*mp.log(n) - sum(a[d % 5]*b[n//d] for d in range(2, n) if n % d == 0)
# check against -F'/F at s=3
s = mp.mpf(3); lhs = -mp.diff(F, s)/F(s)
rhs = sum(b[n]*mp.power(n, -s) for n in range(2, N+1)); print('-F\'/F(3)=', lhs, ' partial sum b_n n^-3 (n<=60)=', rhs)
print('b_n n<=40:', [(n, mp.nstr(b[n], 6)) for n in range(2, 41)])
