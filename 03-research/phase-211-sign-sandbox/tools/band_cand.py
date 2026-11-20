"""Band margin at tone candidates (phase 211, ROUND_017_B).  NUMERICAL tool.
Candidates: local minima w of g_T (tools/tone_scan.py) with g < gthr, and midpoints (w1+w2)/2 of pairs with
|w1-w2| <= 2 eta tau and (g1+g2)/2 < gthr, restricted to [tau_lo, tau_hi]; around each, full Lanczos band margin
on tau in [c - half, c + half] step st (cold start + random mixing, tools/band_lanczos.py).
usage: band_cand.py T eta gfile gthr tau_lo tau_hi out.npz [half st nproc]"""
import sys, math, numpy as np
from multiprocessing import Pool
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import Band, m_sym

def cands(gfile, eta, gthr, tlo, thi):
    d = np.load(gfile); w, g = d['w'], d['g']
    i = np.where((g[1:-1] < g[:-2]) & (g[1:-1] < g[2:]))[0] + 1; i = i[g[i] < gthr]; W, G = w[i], g[i]
    c = [x for x in W if tlo <= x <= thi]
    for a in range(len(W)):
        b = np.where((W > W[a]) & (W - W[a] <= eta * (W[a] + W)) & ((G[a] + G) / 2 < gthr))[0]
        c += [(W[a] + W[j]) / 2 for j in b if tlo <= (W[a] + W[j]) / 2 <= thi]
    c = np.array(sorted(c)); keep = [c[0]] if len(c) else []
    for x in c[1:]:
        if x - keep[-1] > 0.05: keep.append(x)
    return np.array(keep), len(W)

def work(args):
    T, eta, cs, half, st = args
    b = Band(T, int(2 * T * eta * (max(cs) + half) / math.pi) + 2); out = []
    for c in cs:
        v0 = None
        for t in np.arange(c - half, c + half + st / 2, st):
            lam, x, res, K = b.top(t, eta, v0=v0); v0 = x; out.append((t, float(m_sym(t)) - lam, lam, res, K, c))
    return out

if __name__ == '__main__':
    T, eta = float(sys.argv[1]), float(sys.argv[2]); gfile = sys.argv[3]; gthr, tlo, thi = map(float, sys.argv[4:7])
    fn = sys.argv[7]; half = float(sys.argv[8]) if len(sys.argv) > 8 else 0.15; st = float(sys.argv[9]) if len(sys.argv) > 9 else 0.01
    npr = int(sys.argv[10]) if len(sys.argv) > 10 else 20
    c, nw = cands(gfile, eta, gthr, tlo, thi)
    print(f"T={T} eta={eta} gthr={gthr} g-minima={nw} candidates={len(c)}", flush=True)
    parts = [p for p in np.array_split(c, max(1, min(len(c), npr * 6))) if len(p)]
    with Pool(npr) as p: r = [x for q in p.map(work, [(T, eta, q, half, st) for q in parts]) for x in q]
    a = np.array(r); np.savez(fn, tau=a[:, 0], margin=a[:, 1], lam=a[:, 2], res=a[:, 3], K=a[:, 4], cand=a[:, 5])
    o = np.argsort(a[:, 1]); seen = []
    print(f"  maxres={a[:,3].max():.1e} points={len(a)}")
    for k in o:
        if any(abs(a[k, 5] - s) < 1e-9 for s in seen): continue
        seen.append(a[k, 5]); print(f"  tau={a[k,0]:.4f} (tau/2piN={a[k,0]/(2*math.pi*math.exp(2*T)):.4f}) margin={a[k,1]:.6f} K={int(a[k,4])}")
        if len(seen) >= 10: break
