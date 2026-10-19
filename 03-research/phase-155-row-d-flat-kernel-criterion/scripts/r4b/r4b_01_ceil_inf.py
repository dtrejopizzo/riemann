"""R155 round 4b, (c)(i): the TK ceiling for the ARCHIMEDEAN form alone.

Ceil_inf(M,T) = sup_beta inf_{tau0} lambda_min(C_M(tau0,beta)) with S_beta = m + b0*g0hat + b1*g1hat
(prop:TK of Paper 47 with the prime comb deleted).  Compare with the Galerkin value of
lambda^{inf,P}_min(T) (R155_023 table).  DOUBLE PRECISION -> DIAGNOSTIC.
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                '03-research', 'phase-155-row-d-flat-kernel-criterion', 'scripts'))
from tk_common import m_arch, make_S_parts
from scipy.linalg import toeplitz

def coeff_families_arch(T, M, tau0, n=1 << 16, parts=None):
    d = 2.0 * T / M; P = 2.0 * np.pi / d
    x = np.linspace(tau0, tau0 + P, n + 1)
    w = np.ones(n + 1); w[1:-1:2] = 4.0; w[2:-1:2] = 2.0; w *= (P / n) / 3.0
    ph0 = np.exp(1j * d * tau0 * np.arange(M))
    out = []
    for f in parts:
        fv = f(x) * w
        y = fv[:n].copy(); y[0] += fv[n]
        F = np.fft.ifft(y) * n
        out.append(F[:M] * ph0 / P)
    return out

def lam_min(cs_parts, beta):
    cs = cs_parts[0] + beta[0] * cs_parts[1] + beta[1] * cs_parts[2]
    C = toeplitz(np.conj(cs), cs)
    return np.linalg.eigvalsh(C)[0]

def ceil_inf(T, M, ntau=33, nfft=1 << 15):
    _, g0h, g1h, _ = make_S_parts(T)
    parts = (m_arch, g0h, g1h)
    d = 2.0 * T / M; P = 2.0 * np.pi / d
    taus = np.linspace(-P, 0.0, ntau)
    fam = [coeff_families_arch(T, M, t0, n=nfft, parts=parts) for t0 in taus]
    def obj(beta):
        return min(lam_min(f, beta) for f in fam)
    # concave in beta: coarse grid then Nelder-Mead
    from scipy.optimize import minimize
    best = (-1e9, np.array([0.0, 0.0]))
    for b0 in np.linspace(-1.0, 4.0, 11):
        for b1 in np.linspace(-1.0, 1.0, 5):
            v = obj((b0, b1))
            if v > best[0]:
                best = (v, np.array([b0, b1]))
    r = minimize(lambda b: -obj(b), best[1], method='Nelder-Mead',
                 options=dict(xatol=1e-6, fatol=1e-12, maxiter=400))
    return max(best[0], -r.fun), r.x

if __name__ == '__main__':
    res = {}
    for name, T in [("halflog3", 0.5 * np.log(3.0)), ("log2", np.log(2.0))]:
        res[name] = {}
        for M in [8, 12, 16, 24, 32, 48, 64]:
            v, b = ceil_inf(T, M)
            res[name][M] = [float(v), list(map(float, b))]
            print(f"T={name:9s} M={M:3d}  Ceil_inf={v:+.8e}  beta={b}", flush=True)
    json.dump(res, open(os.path.join(os.path.dirname(__file__), 'r4b_01.json'), 'w'), indent=1)
