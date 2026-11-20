"""ROUND_032_A: V*(X,T)=max_w lam_min(a^{X,w}_T) for several lattices X (numerical).
Reuses forms.py (Legendre Galerkin on P_T). Maximization: soft-min (log-sum-exp, beta continuation)
with L-BFGS(-B); reported value = exact lam_min at returned w (a certified lower bound of V* in the
Galerkin space)."""
import sys, json, numpy as np
from math import log, exp
from scipy.optimize import minimize
from forms import build, corr, basis
from numpy.polynomial.legendre import leggauss

def setup(T, N, xs):
    M0, _, _, _ = build(T, N)            # arch part, projected (lattice from build discarded)
    xg, wg = leggauss(N + 40); t = T * xg; ww = wg * T
    P = basis(T, N, t)
    A = P.T @ (ww * np.exp(t / 2)); B = P.T @ (ww * np.exp(-t / 2))
    Z = np.linalg.svd(np.vstack([A, B]))[2][2:].T
    C = np.array([(lambda c: (c + c.T) / 2)(Z.T @ corr(T, N, x) @ Z) for x in xs])
    return M0, C

def lmin(M0, C, w):
    return np.linalg.eigvalsh(M0 - np.tensordot(w, C, 1))

def vstar(M0, C, pos):
    m = len(C); w = np.zeros(m)
    for beta in [10, 30, 100, 300, 1000, 3000, 1e4, 3e4]:
        def f(w):
            lam, V = np.linalg.eigh(M0 - np.tensordot(w, C, 1))
            a = -beta * (lam - lam[0]); p = np.exp(a); s = p.sum(); p /= s
            val = lam[0] - np.log(s) / beta
            G = (V * p) @ V.T; g = -np.einsum('mij,ij->m', C, G)
            return -val, -g
        r = minimize(f, w, jac=True, method='L-BFGS-B',
                     bounds=[(0, None)] * m if pos else None, options={'maxiter': 3000})
        w = r.x
    lam = lmin(M0, C, w)
    mult = int(np.sum(lam - lam[0] < 1e-2 * abs(lam[0]) + 1e-6))
    return lam[0], w, mult

def lattices(T):
    L = np.exp(2 * T); out = {}
    ints = list(range(2, int(L) + 2))
    out['enteros'] = [n for n in ints if n < L]
    out['impares'] = [n for n in out['enteros'] if n % 2]
    out['coprimos3'] = [n for n in out['enteros'] if n % 3]
    def beurling(g):
        odd = [p for p in range(3, int(L) + 2) if all(p % q for q in range(2, int(p**.5) + 1))]
        S = {1.0}
        for p in [g] + odd:
            new = set()
            for s in S:
                v = s * p
                while v < L: new.add(v); v *= p
            S |= new
        return sorted(x for x in S if x > 1)
    out['beurling2.2'] = beurling(2.2); out['beurling2.02'] = beurling(2.02)
    out['n+0.3'] = [n + 0.3 for n in ints if n + 0.3 < L]
    for sd in (1, 2, 3):
        rng = np.random.default_rng(sd); xs = []
        for n in out['enteros']:
            gap = log(n + 1) - log(n)
            xs.append(log(n) + rng.uniform(-.2, .2) * gap)
        out[f'ruido{sd}'] = [exp(x) for x in xs if x < 2 * T]
    isprime = lambda n: n > 1 and all(n % q for q in range(2, int(n**.5) + 1))
    out['primos'] = [n for n in out['enteros'] if isprime(n)]
    def ppow(n):
        for p in range(2, n + 1):
            if n % p == 0:
                while n % p == 0: n //= p
                return n == 1
    out['potprimos'] = [n for n in out['enteros'] if ppow(n)]
    return out

if __name__ == '__main__':
    T = float(sys.argv[1]); N = int(sys.argv[2]); only = sys.argv[3:] or None
    res = {}
    for name, ys in lattices(T).items():
        if only and name not in only: continue
        xs = [log(y) for y in ys]
        M0, C = setup(T, N, xs)
        base = np.linalg.eigvalsh(M0)[0]
        v, w, mu = vstar(M0, C, False); vp, wp, mup = vstar(M0, C, True)
        res[name] = dict(n=len(xs), base=base, V=v, mult=mu, Vp=vp, multp=mup,
                         wp12=[round(x, 4) for x in wp[:12]], pts12=[round(y, 3) for y in ys[:12]])
        print(f"T={T} N={N} {name:13s} m={len(xs):3d} base={base:+.5f} V*={v:+.5f}(mult {mu}) "
              f"V*+={vp:+.5f}(mult {mup})", flush=True)
    json.dump(res, open(f'out_032A/T{T}_N{N}.json', 'w'), indent=1)
