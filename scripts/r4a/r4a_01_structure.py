"""R155.032 round 4a, task (1)+(3): structure of Pi_T on the EVEN archimedean
eigenbasis of A_inf|P_T, the vector b = Pi_T F*|_V, and the Galerkin trend of
lambda_min(W) on nested even subspaces span{e_1,e_3,...,e_{2k+1}}.
DIAGNOSTIC (double precision, Galerkin).  Reuses scripts/r3a/arch_core.py verbatim.
Archives the Legendre coefficient vectors of every even eigenvector used.
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import numpy as np, arch_core as ac

t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__))
LOG2 = float(np.log(2)); out = {}
RUNS = [(18, 0.62, 120, 100), (18, 0.65, 120, 100), (18, LOG2, 120, 100), (36, LOG2, 200, 160)]

for N, T, nu, nq in RUNS:
    ac.Cmat.__defaults__ = (nq,)
    G = ac.gamma_matrix(T, N, nu=nu)
    Pl, a, b = ac.pole_matrix(T, N)
    Pi, A_T, contacts = ac.prime_matrix(T, N)
    # the two shift pieces separately: Pi = -(v2 C(log2) + v3 C(log3))
    shifts = {}
    for n in contacts:
        v = 2*ac.vonmangoldt(n)[n]/np.sqrt(n) if n in ac.vonmangoldt(n) else None
    vm = ac.vonmangoldt(int(np.exp(2*T))+1)
    Cn = {n: (2*vm[n]/np.sqrt(n), ac.Cmat(np.log(n), T, N)) for n in contacts}
    Q = np.column_stack([a, b]); U, s, _ = np.linalg.svd(Q, full_matrices=True); Z = U[:, 2:]
    Ainf = Z.T @ G @ Z; PiP = Z.T @ Pi @ Z; W = Ainf + PiP
    ev, V = np.linalg.eigh(Ainf)
    # parity of each eigenvector in the Legendre coefficient space: P_k(-x)=(-1)^k P_k(x)
    par = np.array([(-1)**k for k in range(N)])
    coef = Z @ V                                   # columns = eigenvectors in Legendre coords
    pv = [float(np.sum(par*coef[:, j]*coef[:, j])) for j in range(V.shape[1])]
    even_idx = [j for j in range(V.shape[1]) if pv[j] > 0.5]
    odd_idx  = [j for j in range(V.shape[1]) if pv[j] < -0.5]
    ne = min(8, len(even_idx)); E = even_idx[:ne]
    f = V[:, 0]; assert 0 in E
    w11 = float(f @ W @ f)
    # b = P_V W F*  vs  P_V Pi F*   (Theorem 4a.1)
    bW = W @ f - (f @ W @ f)*f
    bPi = PiP @ f - (f @ PiP @ f)*f
    rec = dict(N=N, T=T, contacts=contacts, A_T=float(A_T), w11=w11,
               lam=[float(x) for x in ev[:12]],
               parity=[round(x, 4) for x in pv[:12]],
               even_idx=even_idx[:12], odd_idx=odd_idx[:8],
               b_eq_PiF_relerr=float(np.linalg.norm(bW-bPi)/np.linalg.norm(bW)),
               norm_b=float(np.linalg.norm(bW)),
               arch_part_of_Wf=float(np.linalg.norm((Ainf@f) - ev[0]*f)))
    # Pi on the first 8 even eigenvectors, and the two shift forms separately
    Ye = V[:, E]
    PiE = Ye.T @ PiP @ Ye
    rec['lam_even'] = [float(ev[j]) for j in E]
    rec['PiE'] = [[float(x) for x in row] for row in PiE]
    for n, (vn, Cm) in Cn.items():
        Sn = Z.T @ Cm @ Z
        rec['shift_%d' % n] = dict(v=float(vn),
                                   M=[[float(x) for x in row] for row in (Ye.T @ (-vn*Sn) @ Ye)])
    rec['AinfE'] = [float(ev[j]) for j in E]
    # b in the even eigenbasis (components on e_3, e_5, ...)
    rec['b_even_components'] = [float(bW @ V[:, j]) for j in E]
    rec['b_odd_components'] = [float(bW @ V[:, j]) for j in odd_idx[:6]]
    # (3) nested even subspaces span{e_1,...,e_{2k+1}}
    trend = []
    for k in range(1, len(even_idx)+1):
        idx = even_idx[:k]; Yk = V[:, idx]
        Wk = Yk.T @ W @ Yk
        evk = np.linalg.eigvalsh(Wk)
        trend.append(dict(k=k, dim=k, lam_min=float(evk[0]), det=float(np.linalg.det(Wk))))
    rec['trend_even'] = trend
    Yev = V[:, even_idx]; Yod = V[:, odd_idx]
    rec['lam_min_W_even_full'] = float(np.linalg.eigvalsh(Yev.T @ W @ Yev)[0])
    rec['lam_min_W_odd_full'] = float(np.linalg.eigvalsh(Yod.T @ W @ Yod)[0])
    rec['lam_min_W_full'] = float(np.linalg.eigvalsh(W)[0])
    # archive polynomial (Legendre) coefficients of the even eigenvectors used
    rec['even_coef'] = [[float(x) for x in coef[:, j]] for j in E]
    out['N%d_T%.6f' % (N, T)] = rec
    print('N=%d T=%.5f w11=%+.6f |b|=%.5f b=PiF* relerr=%.2e  lam_even=%s' %
          (N, T, w11, rec['norm_b'], rec['b_eq_PiF_relerr'],
           ' '.join('%+.4f' % x for x in rec['lam_even'][:5])))
    print('   trend lam_min(W|span k even): ' +
          ' '.join('k=%d:%+.3e' % (d['k'], d['lam_min']) for d in trend[:8]))
    print('   full even %+.4e  odd %+.4e  all %+.4e' %
          (rec['lam_min_W_even_full'], rec['lam_min_W_odd_full'], rec['lam_min_W_full']))

json.dump(out, open(os.path.join(HERE, 'r4a_01.json'), 'w'), indent=1)
print('runtime %.1fs' % (time.time()-t0))
