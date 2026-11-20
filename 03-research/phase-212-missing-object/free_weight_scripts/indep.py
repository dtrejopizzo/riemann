"""independent evaluation of a^w_T(F) for a saved minimizer: c_F(u) by Gauss on element overlaps,
u-integral by adaptive quadrature (scipy.quad) with breakpoints; constraint residuals; profile."""
import sys, numpy as np
from scipy.integrate import quad
from hp import Basis, shiftblock, Kf, C0, Gf
from forms import vonmangoldt
from math import log, sqrt, pi
f = np.load(sys.argv[1]); k = float(sys.argv[2]); T = float(sys.argv[3])
x, p, c = f['x'], int(f['p']), f['c']; B = Basis(x, p); E = B.E
cc = c.reshape(E, p)
def cF(u):
    s = 0.0
    for e in range(E):
        for g in range(E):
            C = shiftblock(B, e, g, u, p + 1)
            if C is not None: s += cc[e] @ C @ cc[g]
    return s
n0 = cF(0.0)
# int_0^2T (c0-c(u))K + c0*G(2T)
bps = np.unique(np.abs(x[:, None] - x[None, :]).ravel()); bps = bps[(bps > 0) & (bps < 2*T)]
pts = np.concatenate([[0], bps, [2*T]])
arch = C0*n0 + n0*Gf(2*T)
for a, b in zip(pts[:-1], pts[1:]):
    if b - a < 1e-13: continue
    arch += quad(lambda u: (n0 - cF(u))*Kf(u), a, b, epsabs=1e-14, epsrel=1e-12, limit=200)[0]
ns = [n for n in range(2, int(np.exp(2*T))+2) if log(n) < 2*T and vonmangoldt(n) > 0]
ar = sum(2*vonmangoldt(n)/sqrt(n)*(np.cos(k*pi*log(n)/(4*T)) if k > 0 else 1)*cF(log(n)) for n in ns)
print(f"norm^2={n0:.12f} arch={arch:.10f} arith={ar:.10f} a={arch-ar:+.6e} saved lam={f['lam'][0]:+.6e}")
# constraints
xg, wg = np.polynomial.legendre.leggauss(40); A = Bc = 0.0; prof = []
for e in range(E):
    a, b = x[e], x[e+1]; t = (b-a)/2*xg+(a+b)/2; w = wg*(b-a)/2; F = B.ev(e, t) @ cc[e]
    A += np.sum(w*F*np.exp(t/2)); Bc += np.sum(w*F*np.exp(-t/2)); prof.append((a, b, np.sum(w*F*F)))
print(f"constraints A={A:+.2e} B={Bc:+.2e}")
prof = np.array(prof); cum = np.cumsum(prof[:, 2])
for q in (0.05, 0.25, 0.5, 0.75, 0.95): print(f"mass quantile {q}: t={prof[np.searchsorted(cum, q*cum[-1]), 0]:+.4f}")
edge = prof[np.abs(prof[:, 0]) > T-0.5, 2].sum(); print(f"mass in |t|>T-0.5: {edge:.4f}; in |t|>T-0.05: {prof[np.abs(prof[:,0])>T-0.05,2].sum():.4f}")
