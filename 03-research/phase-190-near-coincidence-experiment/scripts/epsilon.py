"""The correction: r_m := v_m sqrt(m) / (v_1) for the minimizer v (so r = 1 for pure m^{-1/2}). Is r_m a fixed function of m (arithmetic) or of m/M (cutoff)?"""
import numpy as np, json, sys
from profile import Profile
from am import *
T0 = float(sys.argv[1]); Ms = [int(t) for t in sys.argv[2].split(',')]
P = Profile(T0, 1.0); R = {}
for M in Ms:
    x = np.log(np.arange(1, M+1)); pos, w, _ = lambda_comb(int(M*np.exp(2*T0))+2)
    A = AM(P, x, pos, w); lam, V = np.linalg.eigh(A.A); v = V[:, 0]*np.sign(V[0, 0])
    R[M] = v*np.sqrt(np.arange(1, M+1))/v[0]
m = np.arange(1, 31)
print('r_m = v_m sqrt(m)/v_1 for m<=30, T0=%s' % T0)
for M in Ms: print('M=%5d' % M, ' '.join('%.4f' % R[M][i-1] for i in m))
# multiplicativity test on the largest M: r_{ab} vs r_a r_b for coprime a,b
M = Ms[-1]; r = R[M]
pairs = [(2,3),(2,5),(3,5),(2,7),(3,7),(4,3),(4,5),(2,9),(5,7),(8,3),(2,11),(3,11)]
print('multiplicativity r_ab/(r_a r_b):', ['(%d,%d):%.4f' % (a, b, r[a*b-1]/(r[a-1]*r[b-1])) for a, b in pairs])
# fixed in m or in m/M?  compare r at fixed m across M, and at fixed m/M
print('r at fixed m across M (m=2,3,5,10,20,50):', {mm: ['%.4f' % R[M][mm-1] for M in Ms] for mm in (2, 3, 5, 10, 20, 50)})
print('r at fixed m/M=0.1,0.3,0.5,0.8 across M:', {f: ['%.4f' % R[M][int(f*M)-1] for M in Ms] for f in (0.1, 0.3, 0.5, 0.8)})
# shape of r over the whole range: percentiles
for M in Ms:
    rr = R[M]; print('M=%d r percentiles (5,25,50,75,95):' % M, ['%.3f' % np.percentile(rr, q) for q in (5, 25, 50, 75, 95)], ' r at m=M/2, M:', '%.4f %.4f' % (rr[M//2-1], rr[-1]), ' corr(r_m, log m) %.3f' % np.corrcoef(rr, np.log(np.arange(1, M+1)))[0, 1])
json.dump({str(M): R[M].tolist() for M in Ms}, open(f'../data/epsilon_T0{T0}.json', 'w'))
