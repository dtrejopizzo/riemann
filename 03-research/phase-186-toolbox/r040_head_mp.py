#!/usr/bin/env python3
"""R186_040 — pencil (Neg_T, Pos_T)|P_T in multiple precision (mpmath), for the falsifier at T = 0.9, 1.0.

Usage: python3 r040_head_mp.py T M dps [output.npz]       (T = 1.0, M = 60, dps = 40: ~10-20 min)
Same construction as r034_det.py (orthonormal Legendre Galerkin of degree < M on I_T; form in x-space with
Gauss quadrature in u, 8 panels x 24 nodes; Neg_T by Gauss quadrature (100 nodes) per component of {sigma_T<0},
endpoints refined with findroot), all in mpf.  Prints lambda_A, 1 - beta_j (j = 1..16), counts, ladder steps,
and saves the head eigenvectors (Legendre coordinates, in float) for the postprocessing in r040_head.py.
"""
import sys, numpy as np, mpmath as mp
from numpy.polynomial import legendre as NL
import r034_det as R

def gauss_mp(n):
    """Gauss-Legendre nodes and weights in mpf (Newton from numpy's nodes)."""
    x0, _ = NL.leggauss(n); xs, ws = [], []
    for x in x0:
        x = mp.mpf(x)
        for _ in range(60):
            p0, p1 = mp.mpf(1), x
            for k in range(1, n): p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
            dp = n * (x * p1 - p0) / (x * x - 1); dx = p1 / dp; x -= dx
            if abs(dx) < mp.mpf(10) ** (-mp.mp.dps + 2): break
        p0, p1 = mp.mpf(1), x
        for k in range(1, n): p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        dp = n * (x * p1 - p0) / (x * x - 1); xs.append(x); ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws

def legbasis_mp(T, M, ys):
    """M x len(ys) matrix of orthonormal Legendre polynomials on I_T (lists of lists)."""
    out = []
    for y in ys:
        u = y / T; P = [mp.mpf(1), u]
        for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
        out.append([P[k] * mp.sqrt(mp.mpf(2 * k + 1) / (2 * T)) for k in range(M)])
    return mp.matrix(out).T          # M x n

def sph_jn_mp(M, x):
    """j_k(x), k < M, via Miller's (stable) downward recurrence normalized with j_0 = sin x / x."""
    if x == 0: return [mp.mpf(1)] + [mp.mpf(0)] * (M - 1)
    K = M + 40 + int(abs(x)); jp1, j = mp.mpf(0), mp.mpf(10) ** (-mp.mp.dps)
    vals = [mp.mpf(0)] * (K + 1); vals[K] = j
    for k in range(K, 0, -1):
        jm1 = (2 * k + 1) / x * j - jp1; jp1, j = j, jm1; vals[k - 1] = j
    scale = (mp.sin(x) / x) / vals[0]
    return [v * scale for v in vals[:M]]

def build_mp(T, M):
    T = mp.mpf(T); C0 = mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi)
    xg, wg = gauss_mp(M + 2); I = mp.eye(M)
    def Cmat(u):
        lo, hi = -T + u, T
        if hi <= lo: return mp.zeros(M, M)
        y = [(hi + lo) / 2 + (hi - lo) / 2 * x for x in xg]; w = [(hi - lo) / 2 * ww for ww in wg]
        F1 = legbasis_mp(T, M, y); F2 = legbasis_mp(T, M, [yy - u for yy in y])
        for i in range(M):
            for jq in range(len(y)): F1[i, jq] *= w[jq]
        Mx = F1 * F2.T; return (Mx + Mx.T) / 2
    K = lambda u: 2 * mp.exp(-u / 2) / (1 - mp.exp(-2 * u))
    tail = mp.log(1 / mp.tanh(T / 2)) + mp.pi - 2 * mp.atan(mp.exp(T))
    A0 = mp.zeros(M, M); ug, uw = gauss_mp(24)
    edges = [2 * T * k / 8 for k in range(9)]
    for lo, hi in zip(edges[:-1], edges[1:]):
        for x, w in zip(ug, uw):
            u = (hi + lo) / 2 + (hi - lo) / 2 * x; ws = (hi - lo) / 2 * w
            A0 += (I - Cmat(u)) * (K(u) * ws)
    A0 += I * (tail + C0)
    Pr = mp.zeros(M, M)
    for n, lp in R.contacts(float(T)):
        p = next(q for q in (2, 3, 5, 7, 11, 13) if n % q == 0)
        Pr -= Cmat(mp.log(n)) * (2 * mp.log(p) / mp.sqrt(n))
    xt, wt = gauss_mp(60); y = [T * x for x in xt]; w = [T * ww for ww in wt]; F = legbasis_mp(T, M, y)
    ta = [sum(F[k, q] * w[q] * mp.exp(y[q] / 2) for q in range(60)) for k in range(M)]
    tb = [sum(F[k, q] * w[q] * mp.exp(-y[q] / 2) for q in range(60)) for k in range(M)]
    return A0 + Pr, A0, Pr, ta, tb

def sigma_mp(T, tau):
    s = mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, 1) * tau / 2)) - mp.log(mp.pi)
    for n, lp in R.contacts(float(T)):
        p = next(q for q in (2, 3, 5, 7, 11, 13) if n % q == 0)
        s -= 2 * mp.log(p) / mp.sqrt(n) * mp.cos(tau * mp.log(n))
    return s

def neg_mp(T, M, comps, nq=100):
    T = mp.mpf(T); xg, wg = gauss_mp(nq); N = mp.zeros(M, M)
    ck = [mp.sqrt((2 * k + 1) * 2 * T) for k in range(M)]
    for lo, hi in comps:
        for x, w in zip(xg, wg):
            t = (hi + lo) / 2 + (hi - lo) / 2 * x; ws = (hi - lo) / 2 * w
            sm = -sigma_mp(T, t) * ws / mp.pi
            J = sph_jn_mp(M, t * T); v = [ck[k] * J[k] for k in range(M)]
            for k in range(M):
                vk = v[k] * sm
                for l in range(k % 2, M, 2):          # k+l even; i^{k-l} = (-1)^{(k-l)/2}
                    N[k, l] += vk * v[l] * (1 if ((k - l) // 2) % 2 == 0 else -1)
    return N

def null_basis_mp(rows, M):
    """orthonormal basis of the kernel of the rows (Gram-Schmidt on I - projector)."""
    Q = []
    for r in rows:
        v = mp.matrix(r)
        for q in Q: v -= q * (q.T * v)[0]
        Q.append(v / mp.norm(v))
    cols = []
    for i in range(M):
        v = mp.zeros(M, 1); v[i] = 1
        for _ in range(2):                         # two passes (reorthogonalization)
            for q in Q: v -= q * (q.T * v)[0]
            for q in cols: v -= q * (q.T * v)[0]
        nv = mp.norm(v)
        if nv > mp.mpf('1e-6'): cols.append(v / nv)
    Z = mp.zeros(M, len(cols))
    for j, c in enumerate(cols):
        for i in range(M): Z[i, j] = c[i]
    return Z

def main(T, M, dps, out=None):
    mp.mp.dps = dps
    comps_d, _ = R.neg_set(T, tmax=1.1 * 2 * np.pi * np.exp(sum(2 * lp / np.sqrt(n) for n, lp in R.contacts(T))) + 10)
    comps = []
    for a, b in comps_d:
        a2 = mp.mpf(0) if a == 0 else mp.findroot(lambda t: sigma_mp(T, t), mp.mpf(a))
        b2 = mp.findroot(lambda t: sigma_mp(T, t), mp.mpf(b)); comps.append((a2, b2))
    print(f"T = {T}  M = {M}  dps = {dps}  components = {len(comps)}  tau_last = {mp.nstr(comps[-1][1], 8)}", flush=True)
    A, A0, Pr, ta, tb = build_mp(T, M); print("form built", flush=True)
    N = neg_mp(T, M, comps); print("Neg built", flush=True)
    Pos = A + N; Z = null_basis_mp([ta, tb], M)
    AP, NP, PP = Z.T * A * Z, Z.T * N * Z, Z.T * Pos * Z
    ev, EV = mp.eigsy(AP); lam = [ev[i] for i in range(ev.rows)]; i0 = min(range(len(lam)), key=lambda i: lam[i])
    L = mp.cholesky(PP); Li = mp.inverse(L); B = Li * NP * Li.T
    eb, EB = mp.eigsy(B); beta = [eb[i] for i in range(eb.rows)]; order = sorted(range(len(beta)), key=lambda i: -beta[i])
    beta = [beta[i] for i in order]; om = [1 - b for b in beta]
    print(f"lambda_A = {mp.nstr(lam[i0], 6)}   (next {mp.nstr(sorted(lam)[1], 4)})")
    print("1 - beta_j: " + " ".join(mp.nstr(v, 4) for v in om[:16]))
    print("pasos log((1-b_{j+1})/(1-b_j)): " + " ".join(mp.nstr(mp.log(om[j + 1] / om[j]), 3) for j in range(15)))
    for thr in (1e-3, np.exp(-1), 1e-2, 1e-4): print(f"#(1-beta < {thr:.3g}) = {sum(1 for v in om if v < thr)}", end=";  ")
    print(f"#beta>1 = {sum(1 for b in beta if b > 1)}")
    Posh = (EV[:, i0].T * PP * EV[:, i0])[0]; print(f"Pos(h*) = {mp.nstr(Posh, 6)}   lambda_A/Pos(h*) = {mp.nstr(lam[i0] / Posh, 6)}   1-beta_1 = {mp.nstr(om[0], 6)}")
    if out:
        # head eigenvectors in Legendre coordinates (float), L2-normalized
        vecs = []
        for i in order[:16]:
            y = Li.T * EB[:, i]; c = Z * y; cf = np.array([float(c[k]) for k in range(M)]); vecs.append(cf / np.linalg.norm(cf))
        np.savez(out, T=T, M=M, beta=np.array([float(b) for b in beta]), om=np.array([float(v) for v in om]),
                 lamA=float(lam[i0]), vecs=np.array(vecs), comps=np.array([[float(a), float(b)] for a, b in comps]),
                 om_str=np.array([mp.nstr(v, 8) for v in om[:16]]))

if __name__ == '__main__':
    T = float(sys.argv[1]); M = int(sys.argv[2]); dps = int(sys.argv[3]); out = sys.argv[4] if len(sys.argv) > 4 else None
    main(T, M, dps, out)
