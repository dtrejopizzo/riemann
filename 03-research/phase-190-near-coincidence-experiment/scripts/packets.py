"""Packet family: u_m = exp(-(log m - log m0)^2/(2 w^2)) (Gaussian bump in log m, width w) -> test G_u = sum u_m V_{log m} F0.
Ratio R(m0,w) = (Div+Near)(u)/Arch(u); margin 1-R. Positivity needs R<=1 for all packets. Lambda vs controls."""
import numpy as np, json, sys
from profile import Profile
from am import *
T0 = float(sys.argv[1]); M = int(sys.argv[2])
P = Profile(T0, 1.0); x = np.log(np.arange(1, M+1)); nmax = int(M*np.exp(2*T0)) + 2
GAMMA1 = 14.134725141734693
def quartet_kernel(delta, gamma):
    zs = [delta+1j*gamma, delta-1j*gamma, -delta+1j*gamma, -delta-1j*gamma]
    coef = [(z, P.Fhat(-1j*z)**2) for z in zs]
    def Q(d):
        out = np.zeros(np.shape(d), complex)
        for z, c in coef: out += c*np.exp(z*d)
        return out.real
    return Q
combs = {'Lambda': lambda_comb(nmax), 'a_3': lambda_comb(nmax, delete_below=3), 'pert2_+1e-5': lambda_comb(nmax, perturb=(2, 1+1e-5)),
         'pert2_-1e-5': lambda_comb(nmax, perturb=(2, 1-1e-5)), 'pert2_+1e-2': lambda_comb(nmax, perturb=(2, 1.01)), 'pert7_-1e-2': lambda_comb(nmax, perturb=(7, 0.99)),
         'poisson_0': poisson_comb(np.log(M)+2*T0+0.1, 1.0, 0)}
ws = [0.2, 0.4, 0.7, 1.0, 1.5, 2.0, 2.5]
m0s = np.exp(np.arange(0.0, np.log(M)-0.3, 0.1))
out = {}
for name, (pos, w, _) in combs.items():
    A = AM(P, x, pos, w, extra_kernel=None)
    R = np.zeros((len(ws), len(m0s))); Ar = np.zeros_like(R); Nr = np.zeros_like(R); Dr = np.zeros_like(R); Q = np.zeros_like(R)
    for i, wd in enumerate(ws):
        for j, m0 in enumerate(m0s):
            u = np.exp(-(x-np.log(m0))**2/(2*wd*wd)); u /= np.linalg.norm(u)
            a = u@A.Arch@u; d = u@A.Div@u; n = u@A.Near@u; g = u@A.Gram@u
            R[i, j] = (d+n)/a if a != 0 else np.nan; Ar[i, j] = a/g; Nr[i, j] = n/g; Dr[i, j] = d/g; Q[i, j] = (a-d-n)/g
    out[name] = dict(ws=ws, m0s=m0s.tolist(), R=R.tolist(), arch_over_gram=Ar.tolist(), near_over_gram=Nr.tolist(), div_over_gram=Dr.tolist(), quotient=Q.tolist())
    print(name, 'min quotient (a_T/||G||^2) over packets per width:', [(wd, '%.3e' % Q[i].min(), 'at m0=%.0f' % m0s[Q[i].argmin()]) for i, wd in enumerate(ws)], flush=True)
if True:
    A = AM(P, x, *combs['Lambda'][:2], extra_kernel=quartet_kernel(0.1, GAMMA1))
    Q = np.zeros((len(ws), len(m0s)))
    for i, wd in enumerate(ws):
        for j, m0 in enumerate(m0s):
            u = np.exp(-(x-np.log(m0))**2/(2*wd*wd)); u /= np.linalg.norm(u); Q[i, j] = (u@A.A@u)/(u@A.Gram@u)
    out['M1_delta0.1'] = dict(ws=ws, m0s=m0s.tolist(), quotient=Q.tolist())
    print('M1_delta0.1', [(wd, '%.3e' % Q[i].min(), 'at m0=%.0f' % m0s[Q[i].argmin()]) for i, wd in enumerate(ws)], flush=True)
json.dump(out, open(f'../data/packets_T0{T0}_M{M}.json', 'w'), indent=1)
