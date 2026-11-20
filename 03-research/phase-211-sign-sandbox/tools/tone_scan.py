"""Flat-window tone function g_T(w) = m(w) - sum_{n<N} v_n (1 - l_n/2T) cos(w l_n)  (phase 211, ROUND_017_B).  NUMERICAL tool.
Diagonal of A_tau^{(eta)}: A_kk = (1/2T)[d_k + s_k/a_k] = (1/2)[F(tau+a_k) + F(tau-a_k)] + s_k/(2T a_k),
F(w) = sum v_n (1 - l_n/2T) cos(w l_n), so m(tau) - A_kk = (1/2)[g(tau+a_k) + g(tau-a_k)] + curvature + O(sum|v_n|/(T a_k)).
usage: tone_scan.py T w_lo w_hi step out.npz [nproc]  -> grid + Brent-polished local minima."""
import sys, math, numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import comb, m_sym

def setup(T):
    C = comb(T); ln = np.array([math.log(n) for n, _, _ in C]); v = np.array([x for _, _, x in C])
    return ln, v * (1 - ln / (2 * T))

def g(T, w, ln, wv):
    w = np.atleast_1d(w); return m_sym(w) - np.cos(np.outer(w, ln)) @ wv

def work(args):
    T, ws = args; ln, wv = setup(T)
    return np.concatenate([g(T, ws[i:i + 4096], ln, wv) for i in range(0, len(ws), 4096)])

if __name__ == '__main__':
    T, lo, hi, step = map(float, sys.argv[1:5]); fn = sys.argv[5]; npr = int(sys.argv[6]) if len(sys.argv) > 6 else 20
    ws = np.arange(lo, hi, step); parts = np.array_split(ws, npr * 4)
    with Pool(npr) as p: gv = np.concatenate(p.map(work, [(T, c) for c in parts]))
    ln, wv = setup(T)
    i = np.where((gv[1:-1] < gv[:-2]) & (gv[1:-1] < gv[2:]))[0] + 1; i = i[np.argsort(gv[i])][:40]
    pol = []
    for k in i:
        r = minimize_scalar(lambda w: float(g(T, w, ln, wv)[0]), bounds=(ws[k] - step, ws[k] + step), method='bounded',
                            options={'xatol': 1e-9}); pol.append((r.fun, r.x))
    pol.sort(); np.savez(fn, w=ws, g=gv, pol=np.array(pol))
    print(f"T={T} [{lo:.1f},{hi:.1f}] step={step} n={len(ws)} sum v(1-l/2T)={wv.sum():.3f} grid min={gv.min():.6f}")
    for f, x in pol[:8]: print(f"   w={x:.6f} (w/2piN={x/(2*math.pi*math.exp(2*T)):.4f}) g={f:.6f}")
