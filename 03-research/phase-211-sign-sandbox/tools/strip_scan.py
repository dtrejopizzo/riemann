"""Full Lanczos scan of the band margin mu_eta(tau) = m(tau) - lambda_max(A_tau^{(eta)}) on a strip
r = tau/(2 pi e^{2T}) in [r_lo, r_hi] (phase 211, ROUND_022_B).  NUMERICAL tool.
Speed-up: with tau on the grid w0 + j*delta, delta = h/m (h = pi/2T), every frequency tau +- a_k (a_k = k h) lies on the
same grid, and  s1_k = (1/2)[S(tau+a_k) - S(tau-a_k)],  d_k = (1/2)[D(tau+a_k) + D(tau-a_k)]  with
S(w) = sum v_n sin(w l_n), D(w) = sum v_n (2T - l_n) cos(w l_n), tabulated once on the grid (blocked matrix products).
Same operator as tools/band_lanczos.py (checked against LBand of tools/align_band.py).
usage: strip_scan.py T m r_lo r_hi out_prefix [nproc] [eta]   (resumable: finished chunks stored in out_prefix_chunks/)"""
import sys, os, math, time, numpy as np
import scipy.fft as sfft
from multiprocessing import Pool
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import Band, m_sym, comb

def tabulate(T, w0, J, delta, B=512):
    C = comb(T); l = np.array([math.log(n) for n, _, _ in C]); v = np.array([x for _, _, x in C])
    E = np.exp(1j * np.outer(np.arange(B) * delta, l)); Z = np.empty(J, complex); Y = np.empty(J, complex)
    for b in range(0, J, B):
        ph = np.exp(1j * (w0 + b * delta) * l); nb = min(B, J - b)
        Z[b:b + nb] = E[:nb] @ (v * ph); Y[b:b + nb] = E[:nb] @ (v * (2 * T - l) * ph)
    return Z.imag.copy(), Y.real.copy()

class GBand(Band):
    def __init__(self, T):
        self.T = T; self.K = None; self.Kmax = 10**9
    def _prep(self, K):
        T = self.T; self.K = K; h = math.pi / (2 * T)
        self.a = h * np.arange(1, K + 1); self.eps = (-1.0) ** np.arange(1, K + 1)
        L = 1 << int(math.ceil(math.log2(2 * K + 2))); self.L = L
        t = np.zeros(L); mm = np.arange(1, K); t[mm] = 1 / (h * mm); t[L - mm] = -1 / (h * mm); self.Ft = np.fft.rfft(t)
        g = np.zeros(L); s = np.arange(2, 2 * K + 1); g[s] = 1 / (h * s); self.Fg = np.fft.rfft(g)
        self.Fg2 = np.fft.rfft(np.roll(g, -2))
    def A(self, x):  # same fused matvec as band_lanczos.Band.A, scipy.fft
        s, e, K, L = self.s1, self.eps, self.K, self.L
        X = sfft.rfft(np.stack([s * x, e * x, x, s * e * x]), L, axis=1)
        Ft, Fg = self.Ft, self.Fg2
        Y = np.stack([Ft * X[0] + Fg * np.conj(X[0]), -Ft * X[1] + Fg * np.conj(X[1]),
                      -Ft * X[2] + Fg * np.conj(X[2]), Ft * X[3] + Fg * np.conj(X[3])])
        y = sfft.irfft(Y, L, axis=1)[:, :K]
        return (y[0] + e * s * y[1] + s * y[2] + e * y[3] + 2 * self.dd * x) / (4 * self.T)
    def set_grid(self, tau, j, K):
        if K != self.K: self._prep(K)
        k = np.arange(1, K + 1) * M
        self.s1 = 0.5 * (S[j + k] - S[j - k]); self.dd = 0.5 * (D[j + k] + D[j - k])
    def top_grid(self, tau, j, eta, v0):
        K = int(math.floor(2 * self.T * eta * tau / math.pi))
        self.set_tau = lambda tau_, K_: self.set_grid(tau, j, K_)
        return self.top(tau, eta, v0=v0)

S = D = None; M = None; W0 = DEL = None; TT = None; ETA = 0.125
def work(idx):
    b = GBand(TT); v0 = None; out = []
    for j in idx:
        tau = W0 + j * DEL; lam, x, res, K = b.top_grid(tau, j, ETA, v0); v0 = x
        out.append((tau, float(m_sym(tau)) - lam, lam, res, K))
    return out

def _w(ic): return ic[0], work(ic[1])

if __name__ == '__main__':
    TT = float(sys.argv[1]); M = int(sys.argv[2]); rl, rh = float(sys.argv[3]), float(sys.argv[4]); pre = sys.argv[5]
    npr = int(sys.argv[6]) if len(sys.argv) > 6 else 20; ETA = float(sys.argv[7]) if len(sys.argv) > 7 else 0.125
    tlim = float(os.environ.get('TLIM', '1380')); t_start = time.time()
    h = math.pi / (2 * TT); DEL = h / M; N2 = 2 * math.pi * math.exp(2 * TT)
    lo, hi = rl * N2, rh * N2; Kmax = int(2 * TT * ETA * hi / math.pi) + 2
    j0 = Kmax * M + 2; W0 = lo - j0 * DEL; jhi = j0 + int((hi - lo) / DEL) + 1; J = jhi + Kmax * M + 3
    tab = pre + '_tab.npz'
    if os.path.exists(tab):
        d = np.load(tab); S, D = d['S'], d['D']
    else:
        S, D = tabulate(TT, W0, J, DEL); np.savez(tab, S=S, D=D)
    print(f"T={TT} delta={DEL:.5f} tau [{lo:.2f},{hi:.2f}] npts={jhi-j0+1} Kmax={Kmax} tab {time.time()-t_start:.0f}s", flush=True)
    cd = pre + '_chunks'; os.makedirs(cd, exist_ok=True)
    allidx = np.arange(j0, jhi + 1); chunks = np.array_split(allidx, max(1, len(allidx) // int(os.environ.get('CHUNK', '50'))))
    todo = [(i, c) for i, c in enumerate(chunks) if not os.path.exists(f"{cd}/{i:05d}.npy")]
    print(f"chunks {len(chunks)} todo {len(todo)}", flush=True)
    with Pool(npr) as p:
        for i, out in p.imap_unordered(_w, todo):
            np.save(f"{cd}/{i:05d}.npy", np.array(out))
            if time.time() - t_start > tlim: p.terminate(); print('time limit', flush=True); break
    fs = sorted(os.listdir(cd)); a = np.concatenate([np.load(f"{cd}/{f}") for f in fs]); a = a[np.argsort(a[:, 0])]
    np.savez(pre + '.npz', tau=a[:, 0], margin=a[:, 1], lam=a[:, 2], res=a[:, 3], K=a[:, 4])
    i = int(np.argmin(a[:, 1]))
    print(f"done {len(fs)}/{len(chunks)} chunks n={len(a)} min {a[i,1]:.6f} at tau={a[i,0]:.4f} r={a[i,0]/N2:.4f} maxres={a[:,3].max():.1e}", flush=True)
