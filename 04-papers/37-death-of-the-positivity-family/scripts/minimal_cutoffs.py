"""Minimal admissible cutoffs T_n(theta) of Lemma lem:upward (Paper 37).

Convention: A=1 (Johnston--Yang constant), eta(u)=0.1853 u^(3/5) (log u)^(-1/5) - 1.801 log u,
admissibility at u: eta(u) >= (n+1) log(1+u) + log(3 A n^2 / (theta A_n)), theta = 1/4,
A_n from the odd-harmonic formula eq:An.  Prints n, A_n, T_n, A_n/(1+T_n), (1+T_n)/1001.
"""
from mpmath import mp, mpf, nsum, inf, euler, log, pi, findroot, nstr
mp.dps = 30
def A(n):
    s = nsum(lambda k: (1 - mpf(1)/(2*k+1))**n - 1 + mpf(n)/(2*k+1), [1, inf])
    return 1 - mpf(n)/2*(euler + log(4*pi)) + s + (n - 1)   # r=1 term equals n-1
theta = mpf(1)/4
for n in [8, 150, 1000]:
    An = A(n)
    f = lambda u: 0.1853*u**0.6*log(u)**(-0.2) - 1.801*log(u) - (n+1)*log(1+u) - log(3*n**2/(theta*An))
    T = findroot(f, (1e3, 1e14), solver='bisect')
    print(n, nstr(An, 8), nstr(T, 4), nstr(An/(1+T), 4), nstr((1+T)/1001, 4))
