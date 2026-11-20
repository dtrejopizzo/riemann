"""Parallel tau-scan of the band margin m(tau) - lambda_max(A_tau^{(eta)}) (phase 211, ROUND_017_B).  NUMERICAL tool.
usage: band_scan.py T eta tau_lo tau_hi step out.npz [nproc]
Each worker scans a contiguous chunk with warm-started Lanczos; stores tau, margin, lambda, Lanczos residual, K."""
import sys, math, numpy as np
from multiprocessing import Pool
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import Band, m_sym

def work(args):
    T, eta, taus = args
    b = Band(T, int(2 * T * eta * taus[-1] / math.pi) + 2); v0 = None; out = []
    for t in taus:
        lam, x, res, K = b.top(t, eta, v0=v0); v0 = x
        out.append((t, float(m_sym(t)) - lam, lam, res, K))
    return out

if __name__ == '__main__':
    T, eta, lo, hi, step = map(float, sys.argv[1:6]); fn = sys.argv[6]
    npr = int(sys.argv[7]) if len(sys.argv) > 7 else 20
    taus = np.arange(lo, hi + step / 2, step)
    chunks = np.array_split(taus, npr * 8)
    res = []
    with Pool(npr) as p:  # incremental save: a timeout keeps every finished chunk
        for c in p.imap_unordered(work, [(T, eta, c) for c in chunks if len(c)]):
            res += c; a = np.array(sorted(res))
            np.savez(fn, tau=a[:, 0], margin=a[:, 1], lam=a[:, 2], res=a[:, 3], K=a[:, 4])
    a = np.array(sorted(res)); np.savez(fn, tau=a[:, 0], margin=a[:, 1], lam=a[:, 2], res=a[:, 3], K=a[:, 4])
    i = int(np.argmin(a[:, 1]))
    print(f"T={T} eta={eta} [{lo:.2f},{hi:.2f}] step={step} n={len(a)} min margin={a[i,1]:.6f} at tau={a[i,0]:.4f} "
          f"(tau-lo={a[i,0]-lo:.2f}) K={int(a[i,4])} maxres={a[:,3].max():.2e}")
