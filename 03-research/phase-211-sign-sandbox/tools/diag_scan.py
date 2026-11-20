"""Diagonal (single-mode) screen of the band margin (phase 211, ROUND_017_B).  NUMERICAL tool.
By Proposition 1.1 (ROUND_017_B), A_kk(tau) = (1/2T)[d_k + s_k/a_k] with c_n = v_n cos(tau l_n), i.e.
  A_kk(tau) = (1/4T)[F2(tau+a_k) + F2(tau-a_k)] + (1/(4T a_k))[S(tau+a_k) - S(tau-a_k)],
  F2(u) = sum v_n (2T - l_n) cos(u l_n),  S(u) = sum v_n sin(u l_n).
Rayleigh with e_k: lambda_max(A_tau^{(eta)}) >= max_{k<=K} A_kk, so
  mu_diag(tau) = m(tau) - max_{k<=K(tau)} A_kk(tau) >= mu_eta(tau)   (an UPPER bound for the band margin).
Grid u_i = u0 + i*delta, delta = pi/(2T r), so tau_i +- a_k are grid points.  Records the argmax k.
usage: diag_scan.py T eta tau_lo tau_hi r out.npz [nproc]"""
import sys, math, numpy as np
from multiprocessing import Pool
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import comb, m_sym

def FS(args):
    T, us = args; C = comb(T); ln = np.array([math.log(n) for n, _, _ in C]); v = np.array([x for _, _, x in C])
    F, S = [], []
    for i in range(0, len(us), 2048):
        ph = np.outer(us[i:i + 2048], ln); F.append(np.cos(ph) @ (v * (2 * T - ln))); S.append(np.sin(ph) @ v)
    return np.concatenate(F), np.concatenate(S)

def chunk(args):
    T, eta, r, i0, i1 = args
    F, S, u0, delta = np.load(FN + '_F.npy', mmap_mode='r'), np.load(FN + '_S.npy', mmap_mode='r'), U0, DELTA
    idx = np.arange(i0, i1); tau = u0 + delta * idx
    K = np.floor(2 * T * eta * tau / math.pi).astype(int)
    best = np.full(len(idx), -np.inf); kb = np.zeros(len(idx), int)
    for k in range(1, K.max() + 1):
        a = k * math.pi / (2 * T); sel = K >= k
        ip, im = idx[sel] + k * r, idx[sel] - k * r
        val = (F[ip] + F[im]) / (4 * T) + (S[ip] - S[im]) / (4 * T * a)
        cur = best[sel]; upd = val > cur; cur[upd] = val[upd]; best[sel] = cur
        kk = kb[sel]; kk[upd] = k; kb[sel] = kk
    return tau, m_sym(tau) - best, kb

if __name__ == '__main__':
    T, eta, lo, hi = map(float, sys.argv[1:5]); r = int(sys.argv[5]); FN = sys.argv[6]; npr = int(sys.argv[7]) if len(sys.argv) > 7 else 20
    DELTA = math.pi / (2 * T * r); amax = eta * hi + 1
    U0 = lo - amax; nU = int((hi + amax - U0) / DELTA) + 2; us = U0 + DELTA * np.arange(nU)
    with Pool(npr) as p: res = p.map(FS, [(T, c) for c in np.array_split(us, npr * 4)])
    np.save(FN + '_F.npy', np.concatenate([x[0] for x in res])); np.save(FN + '_S.npy', np.concatenate([x[1] for x in res]))
    i0, i1 = int(math.ceil((lo - U0) / DELTA)), int((hi - U0) / DELTA)
    cuts = np.linspace(i0, i1, npr * 4 + 1).astype(int)
    with Pool(npr) as p: res = p.map(chunk, [(T, eta, r, a, b) for a, b in zip(cuts[:-1], cuts[1:])])
    tau = np.concatenate([x[0] for x in res]); mu = np.concatenate([x[1] for x in res]); kb = np.concatenate([x[2] for x in res])
    np.savez(FN + '.npz', tau=tau, margin=mu, k=kb)
    j = np.where((mu[1:-1] < mu[:-2]) & (mu[1:-1] < mu[2:]))[0] + 1; j = j[np.argsort(mu[j])][:12]
    print(f"diag T={T} eta={eta} [{lo:.1f},{hi:.1f}] delta={DELTA:.5f} n={len(tau)} min={mu.min():.6f}")
    for q in j: print(f"   tau={tau[q]:.4f} (tau/2piN={tau[q]/(2*math.pi*math.exp(2*T)):.4f}) mu_diag={mu[q]:.6f} k={kb[q]}")
