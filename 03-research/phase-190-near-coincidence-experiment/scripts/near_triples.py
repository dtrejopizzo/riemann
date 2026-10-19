"""Which (m,k,n) triples / additive shifts h=m-kn carry Near(v) at the bottom eigenvector v, for Lambda and controls."""
import numpy as np, json, sys
from profile import Profile
from am import *
T0 = float(sys.argv[1]); M = int(sys.argv[2])
P = Profile(T0, 1.0); x = np.log(np.arange(1, M+1)); nmax = int(M*np.exp(2*T0)) + 2
def analyse(A, label):
    lam, V = np.linalg.eigh(A.A); v = V[:, 0]
    byn, byh, bylag = {}, {}, {}
    tot = 0.0
    for ai, k, m, d in A.triples:
        contrib = v[m]*v[k]*A.w[ai]*A.P.c0(d)     # (both (m,k) and (k,m) entries: 1/2 w c0 each -> total w c0 v_m v_k)
        n = A.pos[ai]; nint = int(round(np.exp(n)))
        byn[nint] = byn.get(nint, 0.0) + float(contrib.sum())
        if A.x[0] == 0.0 and abs(np.exp(A.x[1]) - 2) < 1e-9:   # integer lattice
            h = (m+1) - (k+1)*nint
            for hh, c in zip(h, contrib):
                byh[int(hh)] = byh.get(int(hh), 0.0) + float(c)
        lag = np.round((A.x[m] - A.x[k]), 0)
        for l, c in zip(lag, contrib): bylag[float(l)] = bylag.get(float(l), 0.0) + float(c)
        tot += float(contrib.sum())
    byn = dict(sorted(byn.items())); byh = dict(sorted(byh.items()))
    r = dict(label=label, lam_min=float(lam[0]), Near_v=float(v@A.Near@v), Div_v=float(v@A.Div@v), Arch_v=float(v@A.Arch@v), check_tot=tot,
             by_n_top=dict(list(byn.items())[:25]), by_h=dict(list(byh.items())), by_lag=dict(sorted(bylag.items())),
             vec_top=[(int(i+1), float(v[i])) for i in np.argsort(-np.abs(v))[:8]], v_sign_frac=float((v*np.sign(v[np.argmax(np.abs(v))]) > 0).mean()), part_ratio=float(1/np.sum(v**4)))
    # Div by n
    divn = {}
    nn = np.round(np.exp(A.pos)).astype(int)
    for ai, (xa, wa) in enumerate(zip(A.pos, A.w)):
        n = nn[ai]
        if n > M: break
        ks = np.arange(1, M//n + 1); ms = ks*n
        divn[int(n)] = float(wa*np.sum(v[ms-1]*v[ks-1]))
    r['div_by_n_top'] = dict(list(divn.items())[:25])
    print(label, 'lam %.3e Near %.4f Div %.4f Arch %.4f | by n (Near, Div):' % (lam[0], r['Near_v'], r['Div_v'], r['Arch_v']),
          [(n, round(byn.get(n, 0), 3), round(divn.get(n, 0), 3)) for n in (2, 3, 4, 5, 7, 8, 9, 11, 13)],
          '| by h:', [(h, round(byh.get(h, 0), 3)) for h in (-3, -2, -1, 1, 2, 3)] if byh else '-', '| top v:', r['vec_top'][:4], 'PR %.1f' % r['part_ratio'], flush=True)
    return r
out = {}
posL, wL, _ = lambda_comb(nmax); out['Lambda'] = analyse(AM(P, x, posL, wL), 'Lambda')
pos, w, _ = lambda_comb(nmax, delete_below=3); out['a_3'] = analyse(AM(P, x, pos, w), 'a_3')
pos, w, _ = lambda_comb(nmax, perturb=(2, 1.01)); out['pert2_1.01'] = analyse(AM(P, x, pos, w), 'pert2_1.01')
pos, w, _ = lambda_comb(nmax, perturb=(2, 1+1e-5)); out['pert2_1+1e-5'] = analyse(AM(P, x, pos, w), 'pert2_1+1e-5')
pos, w, _ = lambda_comb(nmax, amp2=0.05); out['amp2_0.05'] = analyse(AM(P, x, pos, w), 'amp2_0.05')
pos, w, _ = poisson_comb(np.log(M)+2*T0+0.1, 1.0, 0); out['poisson_0'] = analyse(AM(P, x, pos, w), 'poisson_0')
pos, w, qs = beurling_comb(nmax, 0.02, 0); out['beurling_int_0'] = analyse(AM(P, x, pos, w), 'beurling_int_0')
json.dump(out, open(f'../data/near_triples_T0{T0}_M{M}.json', 'w'), indent=1, default=float)
