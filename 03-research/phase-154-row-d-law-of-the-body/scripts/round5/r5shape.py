"""R154 round 5 -- transfer an atom SHAPE from one T to another.

The certificate class only requires supp nu subset {|u| >= 2T} on a lattice u_j = j*2T/M.
A profile (a_j) certified at T0 is therefore a legitimate CANDIDATE shape at T1 once the
lattice is rescaled (same M, same j-range, d = 2T1/M).  The block polish then re-optimises
G block scalings and (beta0,beta1) against the rows of T1.  This replaces the 40-minute
atom LP at every step of the staircase but the first.
"""
import argparse, math, pickle
import numpy as np
import r5core as C

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('--T', type=float, required=True)
ap.add_argument('--tau1', type=float, default=None)
ap.add_argument('--N', type=int, default=None)
ap.add_argument('--out', required=True)
A = ap.parse_args()
r = pickle.load(open(A.src, 'rb'))
M = int(r['M']); us0 = np.asarray(r['us']); a = np.asarray(r['a'])
j0 = int(round(us0[0]/(2*float(r['T'])/M)))
n = len(us0)
T = A.T; d = 2*T/M
us = np.arange(j0, j0+n)*d
P = 2*math.pi/d
tau1 = A.tau1 if A.tau1 else float(r['tau1'])
N = A.N if A.N else int(r['N'])
v = C.vdict(T)
out = dict(T=T, M=M, U=float(r.get('U', 20.0)), d=d, us=us, a=a, b0=float(r['b0']),
           b1=float(r['b1']), lp=float(r['lp']), tau1=tau1, N=N, P=P, v=v,
           tag=A.out, graded2=True, shape_from=A.src)
pickle.dump(out, open(f'lp_{A.out}.pkl', 'wb'))
print(f"{A.out}: T={T} M={M} atoms={n} u in [{us[0]:.4f},{us[-1]:.4f}] 2T={2*T:.4f} "
      f"P={P:.4f} tau1={tau1} N={N} v={ {k: round(x,6) for k,x in v.items()} } "
      f"worst-case floor m(tau1+NP)-Sv = {float(C.m(np.array([tau1+N*P]))[0])-sum(v.values()):.4f}")
