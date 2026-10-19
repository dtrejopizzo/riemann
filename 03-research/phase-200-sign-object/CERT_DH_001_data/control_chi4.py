#!/usr/bin/env python3
"""NUMERICAL control: same template, same delta=1 kernel K_{3/4}, for L(s,chi_{-4}) (q=4, Euler product, zeros on the line
numerically to large height). Expect bottom >= -noise where DH is clearly negative. Usage: control_chi4.py N T1,T2,..."""
import sys, numpy as np
import explore_leg as E
def bcoef4(nmax):
    a = lambda n: [0, 1, 0, -1][n % 4]; b = {}
    for n in range(2, nmax+1): b[n] = a(n)*np.log(n) - sum(a(d)*b[n//d] for d in range(2, n) if n % d == 0)
    return b
E.bcoef = bcoef4; E.C0 = np.log(4/np.pi) + E.digamma(0.75)
N = int(sys.argv[1])
for T in [float(x) for x in sys.argv[2].split(',')]:
    for sec in ('odd', 'full'):
        e0, v, es = E.bottom(T, N, sec); print('chi_-4', sec, N, T, 'lowest:', ' '.join('%.4e' % x for x in es), flush=True)
