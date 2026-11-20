"""Band margin at small-prime alignment cells (phase 211, ROUND_021_B).  NUMERICAL tool.
Candidates in [lo, hi]: (a) local minima of h4(t) = sum_{p in 2,3,5,7} (1 - cos(t log p)) (exhaustive grid, step 0.004,
Brent-polished): simultaneous approximation of (t log p / 2pi) to integers; (b) local minima of the flat-tone function
g_T (tools/tone_scan.py definition).  At each candidate: margin mu_eta(t) = m(t) - lambda_max(A_t^{(eta)}) scanned on
t0 +- 0.1 (step 0.02), (half-width ALIGN_WIN env, default 0.1), then bounded Brent (xatol 2e-5) around the best scan point; eta = 1/4 at the minimiser.
s1, dd computed in chunks (no K x #n matrix stored).
usage: align_band.py T n_h4 n_g out.npz [nproc] [lo_factor hi_factor]"""
import sys, math, numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import Band, m_sym
from tone_scan import setup, g as gfun

class LBand(Band):
    def __init__(self, T):
        super().__init__(T, 1)
    def _prep(self, K):
        T = self.T; self.K = K; h = math.pi / (2 * T)
        self.a = h * np.arange(1, K + 1); self.eps = (-1.0) ** np.arange(1, K + 1)
        L = 1 << int(math.ceil(math.log2(2 * K + 2))); self.L = L
        t = np.zeros(L); m = np.arange(1, K); t[m] = 1 / (h * m); t[L - m] = -1 / (h * m); self.Ft = np.fft.rfft(t)
        g = np.zeros(L); s = np.arange(2, 2 * K + 1); g[s] = 1 / (h * s); self.Fg = np.fft.rfft(g)
        self.Fg2 = np.fft.rfft(np.roll(g, -2))
    def set_tau(self, tau, K):
        if K != self.K: self._prep(K)
        c = self.v * np.cos(tau * self.ln); w = c * (2 * self.T - self.ln)
        s1 = np.empty(K); dd = np.empty(K)
        for i in range(0, K, 4096):
            ph = np.outer(self.a[i:i + 4096], self.ln)
            s1[i:i + 4096] = np.sin(ph) @ c; dd[i:i + 4096] = np.cos(ph) @ w
        self.s1, self.dd = s1, dd

P4 = np.log([2., 3., 5., 7.])
def h4(t): return np.sum(1 - np.cos(np.outer(np.atleast_1d(t), P4)), axis=1)
def dev(t): x = t * P4 / (2 * math.pi); return np.abs(x - np.round(x))

def h4_cands(lo, hi, n):
    best = []
    for a in np.arange(lo, hi, 2e5 * 0.004):
        ts = np.arange(a, min(a + 2e5 * 0.004, hi), 0.004); hv = h4(ts)
        i = np.where((hv[1:-1] < hv[:-2]) & (hv[1:-1] < hv[2:]))[0] + 1
        best += [(hv[k], ts[k]) for k in i]
        best.sort(); best = best[:4 * n]
    out = []
    for _, t0 in best:
        r = minimize_scalar(lambda t: float(h4(t)[0]), bounds=(t0 - .004, t0 + .004), method='bounded', options={'xatol': 1e-9})
        out.append((r.fun, r.x))
    out.sort(); return out[:n]

def g_cands(T, lo, hi, n):
    ln, wv = setup(T); best = []
    for a in np.arange(lo, hi, 20000 * 0.02):
        ts = np.arange(a, min(a + 400, hi), 0.02); gv = gfun(T, ts, ln, wv)
        i = np.where((gv[1:-1] < gv[:-2]) & (gv[1:-1] < gv[2:]))[0] + 1
        best += [(gv[k], ts[k]) for k in i]; best.sort(); best = best[:3 * n]
    out = []
    for _, t0 in best:
        r = minimize_scalar(lambda t: float(gfun(T, t, ln, wv)[0]), bounds=(t0 - .02, t0 + .02), method='bounded', options={'xatol': 1e-9})
        out.append((r.fun, r.x))
    out.sort(); return out[:n]

def g_work(args):
    T, lo, hi, n = args; return g_cands(T, lo, hi, n)

_B = {}; _V = {}
def margin(T, t, eta):
    if T not in _B: _B[T] = LBand(T)
    lam, x, res, K = _B[T].top(t, eta, v0=_V.get(eta), tol=1e-9); _V[eta] = x
    return float(m_sym(t)) - lam, res, K

def cell(args):
    T, t0, tag, q = args
    _V.clear(); W = float(__import__('os').environ.get('ALIGN_WIN', '0.1')); ts = np.arange(t0 - W, t0 + W + 1e-4, 0.02); mv = [margin(T, t, 0.125)[0] for t in ts]
    j = int(np.argmin(mv)); a, b = ts[max(j - 1, 0)], ts[min(j + 1, len(ts) - 1)]
    r = minimize_scalar(lambda t: margin(T, t, 0.125)[0], bounds=(a, b), method='bounded', options={'xatol': 2e-5})
    m8, r8, K8 = margin(T, r.x, 0.125); m4, r4, K4 = margin(T, r.x, 0.25)
    gl = gfun(T, r.x, *setup(T))[0]
    return (T, tag, t0, q, r.x, m8, m4, r8, r4, K8, K4, float(h4(r.x)[0]), float(np.max(dev(r.x))), float(gl), min(mv))

if __name__ == '__main__':
    T = float(sys.argv[1]); nh, ng = int(sys.argv[2]), int(sys.argv[3]); fn = sys.argv[4]
    npr = int(sys.argv[5]) if len(sys.argv) > 5 else 10
    lf, hf = (float(sys.argv[6]), float(sys.argv[7])) if len(sys.argv) > 7 else (1.1, 3.0)
    N2 = 2 * math.pi * math.exp(2 * T); lo, hi = lf * N2, hf * N2
    H = h4_cands(lo, hi, nh)
    edges = np.linspace(lo, hi, npr * 2 + 1)
    with Pool(npr) as p: G = sum(p.map(g_work, [(T, edges[i], edges[i + 1], ng) for i in range(len(edges) - 1)]), [])
    G.sort(); G = G[:ng]
    if ng == 0: G = [(np.nan, np.nan)]
    jobs = [(T, t, 'h4', q) for q, t in H] + [(T, t, 'g', q) for q, t in G if ng]
    print(f"T={T} range [{lo:.1f},{hi:.1f}] h4 best {H[0]} g best {G[0]}", flush=True)
    res = []
    with Pool(npr) as p:
        for r in p.imap_unordered(cell, jobs):
            res.append(r); np.save(fn, np.array(res, dtype=object), allow_pickle=True)
            print(' '.join(str(round(x, 6)) if isinstance(x, float) else str(x) for x in r), flush=True)
    res.sort(key=lambda r: r[5]); print('BEST', res[:5])
