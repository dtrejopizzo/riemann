"""Bisection for T*_inf (bottom of A_inf on L^2(-T,T)) and T*_{inf,P} (on P_T); tau_0 with m(tau_0)=0."""
import sys, os, time; sys.path.insert(0, os.path.dirname(__file__))
import numpy as np, arch_core as ac
from scipy.special import psi as digamma
from scipy.optimize import brentq
t0 = time.time(); N = 18; ac.Cmat.__defaults__ = (100,)
m = lambda tau: np.real(digamma(0.25+1j*tau/2)) - np.log(np.pi)
tau0 = brentq(m, 1.0, 200.0, xtol=1e-12)
print('C0 = %.10f   tau_0 (m(tau_0)=0) = %.8f   m(0)=%.6f' % (ac.C0, tau0, m(0)))
def lam(T, restricted):
    G = ac.gamma_matrix(T, N, nu=120); P, a, b = ac.pole_matrix(T, N)
    return np.linalg.eigvalsh(ac.restrict(G, a, b))[0] if restricted else np.linalg.eigvalsh(G+P)[0]
for restricted, lo, hi, name in [(False, 0.36, 0.38, 'T*_inf'), (True, 0.56, 0.60, 'T*_{inf,P}')]:
    for _ in range(9):
        mid = 0.5*(lo+hi)
        if lam(mid, restricted) > 0: lo = mid
        else: hi = mid
    print('%-12s in [%.6f, %.6f]   (width %.1e)' % (name, lo, hi, hi-lo))
print('runtime %.1fs' % (time.time()-t0))
