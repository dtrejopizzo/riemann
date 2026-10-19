"""R155.026 round 3c: Schur reduction of W_T = A_inf + Pi_T on P_T at the archimedean
ground state F* of A_inf|P_T.  DIAGNOSTIC (double precision, Galerkin).
Reuses scripts/r3a/arch_core.py verbatim (no r3a file is modified)."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import numpy as np, arch_core as ac

t0 = time.time()
TS = [0.58, 0.62, 0.65, float(np.log(2))]
out = {}
for N, nu, nq in [(18, 120, 100), (36, 200, 160)]:
    ac.Cmat.__defaults__ = (nq,)
    for T in TS:
        G = ac.gamma_matrix(T, N, nu=nu)
        Pl, a, b = ac.pole_matrix(T, N)
        Pi, A_T, contacts = ac.prime_matrix(T, N)
        # basis Z of P_T (orthonormal columns)
        Q = np.column_stack([a, b]); U, s, _ = np.linalg.svd(Q, full_matrices=True); Z = U[:, 2:]
        Ainf = Z.T @ G @ Z                 # pole term vanishes on P_T
        PiP = Z.T @ Pi @ Z
        W = Ainf + PiP
        ev, V = np.linalg.eigh(Ainf)
        lam1, lam2 = ev[0], ev[1]
        f = V[:, 0]                        # F*, unit norm, prime-independent
        w11 = float(f @ W @ f)
        # V = f-perp inside P_T
        Y = V[:, 1:]                       # orthonormal basis of f-perp (archimedean eigenbasis)
        WV = Y.T @ W @ Y
        bvec = Y.T @ (W @ f)
        cnorm = float(np.linalg.norm(bvec))
        S = WV - np.outer(bvec, bvec)/w11 if w11 != 0 else None
        evS = np.linalg.eigvalsh(S)
        evW = np.linalg.eigvalsh(W)
        PiV = Y.T @ PiP @ Y
        rec = dict(N=N, T=T, contacts=contacts, A_T=float(A_T),
                   lam1_arch=float(lam1), lam2_arch=float(lam2),
                   n_neg_arch=int((ev < 0).sum()),
                   arch_on_F=float(f @ Ainf @ f), prime_on_F=float(f @ PiP @ f),
                   w11=w11, c_cross=cnorm, normPi=float(np.linalg.norm(PiP, 2)),
                   normPiV=float(np.linalg.norm(PiV, 2)),
                   crude=float(lam2 - np.linalg.norm(PiP, 2) - cnorm**2/w11),
                   crude_sharper=float(lam2 - np.linalg.norm(PiV, 2) - cnorm**2/w11),
                   lam_min_S=float(evS[0]), lam_min_W=float(evW[0]),
                   dim=int(W.shape[0]))
        # where is S smallest: overlap of S-ground state with archimedean eigenvectors of V
        _, VS = np.linalg.eigh(S)
        g = VS[:, 0]                       # in the Y (archimedean eigenvector) coordinates
        rec['S_gs_overlaps'] = [round(float(x), 4) for x in g[:6]]
        rec['S_gs_top_index'] = int(np.argmax(np.abs(g)))
        out[f"N{N}_T{T:.4f}"] = rec
        print(f"N={N} T={T:.4f} lam1={lam1:+.5f} lam2={lam2:+.5f} w11={w11:+.6f} "
              f"c={cnorm:.4f} |PiV|={rec['normPiV']:.4f} crude={rec['crude']:+.4f} "
              f"lmin(S)={evS[0]:+.3e} lmin(W)={evW[0]:+.3e} gs_idx={rec['S_gs_top_index']}")
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r3c_01.json'), 'w'), indent=1)
print('runtime %.1fs' % (time.time()-t0))
