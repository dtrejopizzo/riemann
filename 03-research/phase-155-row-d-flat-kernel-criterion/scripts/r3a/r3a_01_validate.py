"""Validation: (1) Levy form of the Gamma term vs direct (1/2pi) int m |Fhat|^2;
(2) W_T >= 0 at windows where positivity is known (T <= log 2)."""
import sys, os, time; sys.path.insert(0, os.path.dirname(__file__))
import numpy as np, arch_core as ac
from scipy.special import psi as digamma
t0 = time.time()
T, N = 0.5, 18
ac.Cmat.__defaults__ = (100,)
G = ac.gamma_matrix(T, N, nu=120)
# direct check: Levy form vs (1/2pi) int m |Fhat|^2 (log-tail => slow convergence in R)
rng = np.random.default_rng(0); x = rng.normal(size=N); x /= np.linalg.norm(x)
xg, wg = np.polynomial.legendre.leggauss(2000); t = T*xg; w = T*wg
F = ac.basis(t, T, N) @ x
m = lambda tau: np.real(digamma(0.25 + 1j*np.asarray(tau)/2)) - np.log(np.pi)
print('gamma  Levy = %.8f' % (x @ G @ x))
for R, M in [(500, 4000), (2000, 16000)]:
    tau = (np.arange(M)+0.5)*R/M; dt = R/M
    Fh = np.exp(1j*np.outer(tau, t)) @ (w*F)
    print('       direct(|tau|<%5d) = %.8f' % (R, 2*np.sum(m(tau)*np.abs(Fh)**2)*dt/(2*np.pi)))

for TT in [0.30, 0.3465, 0.40, 0.45, 0.50, 0.55, 0.60, 0.6931]:
    G = ac.gamma_matrix(TT, N, nu=120); P, a, b = ac.pole_matrix(TT, N)
    Pi, A_T, ct = ac.prime_matrix(TT, N)
    print('T=%.4f  lam_min(W_T)=%+.6e  lam_min(a_T|P_T)=%+.6e  contacts=%s'
          % (TT, np.linalg.eigvalsh(G+P+Pi)[0], np.linalg.eigvalsh(ac.restrict(G+Pi, a, b))[0], ct))
print('runtime %.1fs' % (time.time()-t0))
