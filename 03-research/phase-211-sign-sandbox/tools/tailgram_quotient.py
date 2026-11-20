"""Gauge-quotient analysis of the class-blind tail Gram (NUMERICAL tool; ROUND_015_A).
Input: the SAVE=<file.npz> output of prolate_tailgram.py. In D-normalised coordinates b^ = D^{1/2} b:
(1) constraint compression: P_C = projector onto {C^T b = 0}; P_C Ghat P_C equals the tail Gram on that subspace exactly
    (radical correction R = C Gam^T + Gam C^T + C Q C^T is killed); reports its band profile (offsets q = 1..12)
    and the band profile of the removed part Ghat - P_C Ghat P_C (rank <= 10);
(2) gauge quotient: X = C^perp ∩ (SDJ)^perp; band profile of P_X Ghat P_X, its bottom vs K (sub-blocks);
(3) diagonal Rayleigh quotients of P_X e_k / |P_X e_k| vs m(k) (chirp turning frequency) and m(k)+1/3, m(k)+1.
Usage: python3 tailgram_quotient.py file.npz [TOPS comma list]"""
import sys, numpy as np, scipy.linalg as sl, mpmath as mp
Z = np.load(sys.argv[1]); GH, DH, Cb, Jn, kH, DgH = Z['GH'], Z['DH'], Z['Cb'], Z['Jn'], Z['kH'], Z['DgH']
mm = lambda t: float(mp.re(mp.digamma(mp.mpf(1)/4 + 0.5j*t)) - mp.log(mp.pi))
def proj_out(A):
    Q, _ = np.linalg.qr(A); return np.eye(A.shape[0]) - Q@Q.T
def band(A, qs=range(1, 13)):
    n = A.shape[0]; return [(q, np.mean([A[a, a+q] for a in range(n-q)]), np.mean([abs(A[a, a+q]) for a in range(n-q)])) for q in qs if q < n]
def analyse(I, verbose):
    G = GH[np.ix_(I, I)]; d = DH[I]; s = 1/np.sqrt(d); Gh = G*s[:, None]*s[None, :]
    Ch = Cb[I]*s[:, None]; Jh = Jn[I]*s[:, None]   # functionals c^T b = (D^{-1/2}c)^T b^ ; gauge functionals (SDJ)^T b likewise
    PC = proj_out(Ch); PX = proj_out(np.hstack([Ch, PC@Jh]))
    GC = PC@Gh@PC; GX = PX@Gh@PX
    eC = sl.eigh(GC, eigvals_only=True); eX = sl.eigh(GX, eigvals_only=True)
    botC = np.min(eC[np.abs(eC) > 1e-10]) if False else np.sort(eC)[5:][0]   # drop the 5 trivial zeros on range(C)
    nX = len(I) - np.linalg.matrix_rank(np.hstack([Ch, Jh]), tol=1e-10)
    botX = np.sort(eX)[len(I)-nX:][0]
    # bottom on X in D-units, via orthonormal basis of X
    Qx = sl.null_space(np.hstack([Ch, Jh]).T); botX2 = np.min(np.linalg.eigvalsh(Qx.T@Gh@Qx))
    Qc = sl.null_space(Ch.T); botC2 = np.min(np.linalg.eigvalsh(Qc.T@Gh@Qc))
    Lg = DgH[np.ix_(I, I)]*s[:, None]*s[None, :]; botL = np.min(sl.eigh(Qc.T@Gh@Qc, Qc.T@Lg@Qc, eigvals_only=True))
    if verbose:
        print(f"  n={len(I)} k={kH[I[0]]}..{kH[I[-1]]}")
        print("  band of Ghat (raw S M S)          q:mean signed / mean|.|:", [(q, round(a, 3), round(b, 3)) for q, a, b in band(Gh)])
        print("  band of P_C Ghat P_C (= tail Gram) :", [(q, round(a, 3), round(b, 3)) for q, a, b in band(GC)])
        print("  band of removed part (rank<=10)    :", [(q, round(a, 3), round(b, 3)) for q, a, b in band(Gh-GC)])
        print("  band of P_X Ghat P_X (gauge quot.) :", [(q, round(a, 3), round(b, 3)) for q, a, b in band(GX)])
        sv = np.linalg.svd(Gh-GC, compute_uv=False); print("  sing. values removed part:", np.round(sv[:12], 3))
        # long-range part offsets >= 8: rank-r residual
        n = len(I); LR = np.array([[Gh[a, b] if abs(a-b) >= 4 else 0 for b in range(n)] for a in range(n)])
        LRc = np.array([[GC[a, b] if abs(a-b) >= 4 else 0 for b in range(n)] for a in range(n)])
        print(f"  |long-range (offset>=8)|_op raw {np.linalg.norm(LR, 2):.3f}  after constraint compression {np.linalg.norm(LRc, 2):.3f}")
        svl = np.linalg.svd(LR, compute_uv=False); print("  sing. values of raw long-range part:", np.round(svl[:8], 3))
        Gs = sorted(np.linalg.eigvalsh(Qx.T@Gh@Qx))[:5]; print("  lowest 5 on X:", np.round(Gs, 3))
        Ex, Vx = np.linalg.eigh(Qx.T@Gh@Qx); v = Qx@Vx[:, 0]
        print("  bottom vector on X (k, b^_k):", [(int(kH[I[a]]), round(v[a], 2)) for a in range(0, n, 2)])
        rq = []
        for a in range(0, n, max(1, n//10)):
            e = PX[:, a]; nr = np.linalg.norm(e)
            if nr > 0.3: rq.append((int(kH[I[a]]), round(e@Gh@e/nr**2, 3), round(Gh[a, a], 3), round(mm(kH[I[a]]), 3), round(nr, 2)))
        print("  (k, RQ of P_X e_k, Ghat_kk, m(k), |P_X e_k|):", rq)
    return botC2, botX2, nX, botL
tops = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [int(kH[-1])]
for t in tops:
    I = [a for a in range(len(kH)) if kH[a] <= t]
    bC, bX, nX, bL = analyse(I, t == tops[-1])
    print(f" TOP {t}: dim {len(I)} | D-bottom on C^perp (= tail Gram on S{{constraints}}) {bC:.4f} | D-bottom on gauge quotient X (dim {nX}) {bX:.4f} | l_g^S-bottom on C^perp (exact gauge quotient metric) {bL:.4f}")
