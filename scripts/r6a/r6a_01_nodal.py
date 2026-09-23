"""r6a_01: nodal structure of the even archimedean eigenvectors on P_T at T=log2,
sign prediction of the one-sided overlaps J_n(i,j) from nodes alone, and the
eigenvalue growth law lambda_{2k+1} vs log k.  DIAGNOSTIC (Galerkin, N=18/36).
Lemma N: J_n(i,j) = int_{log n - T}^{T} e_i(z-log n) e_j(z) dz.
"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import arch_core as ac
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}

def run(T, N, nmodes=8):
    G = ac.gamma_matrix(T, N); Pl, a, b = ac.pole_matrix(T, N)
    Z = np.linalg.svd(np.column_stack([a, b]), full_matrices=True)[0][:, 2:]
    Ainf = Z.T @ G @ Z
    ev, V = np.linalg.eigh(Ainf)
    coef = Z @ V
    par = np.array([(-1)**k for k in range(N)])
    pv = [float(np.sum(par*coef[:, j]**2)) for j in range(V.shape[1])]
    E = [j for j in range(V.shape[1]) if pv[j] > 0.5][:nmodes]
    t = np.linspace(-T, T, 8001); B = ac.basis(t, T, N)
    fun = []
    for j in E:
        y = B @ coef[:, j]
        if y[np.argmax(np.abs(y))] < 0: y = -y; V[:, j] = -V[:, j]; coef[:, j] = -coef[:, j]
        fun.append(y)
    def nodes(y):
        s = np.where(np.sign(y[:-1]) != np.sign(y[1:]))[0]
        return [float(t[i] - y[i]*(t[i+1]-t[i])/(y[i+1]-y[i])) for i in s]
    nds = [nodes(y) for y in fun]
    vm = ac.vonmangoldt(int(np.exp(2*T))+1)
    contacts = [n for n in sorted(vm) if 0 < np.log(n) < 2*T]
    res = dict(T=T, N=N, lam=[float(ev[j]) for j in E],
               nodes=[[round(x, 6) for x in nd] for nd in nds],
               npos=[len([x for x in nd if x > 0]) for nd in nds],
               contacts=contacts)
    # exact J and predicted sign from nodes alone
    tab = {}
    for n in contacts:
        A = np.log(n); v = 2*vm[n]/np.sqrt(n)
        J = np.zeros((nmodes, nmodes)); P = np.zeros((nmodes, nmodes))
        lo = A - T
        zz = t[t >= lo]
        for i in range(nmodes):
            shi = np.interp(zz - A, t, fun[i], left=0.0, right=0.0)
            for j in range(nmodes):
                J[i, j] = np.trapz(shi*fun[j][t >= lo], zz)
                # node-only predictor: cut (lo,T) by nodes of e_j and shifted nodes of e_i
                cuts = sorted([lo, T] + [x for x in nds[j] if lo < x < T]
                              + [x + A for x in nds[i] if lo < x + A < T])
                cells = [(cuts[k], cuts[k+1]) for k in range(len(cuts)-1)]
                # sign of integrand on a cell, from node counts (parity), anchored at cell midpoint
                best = max(cells, key=lambda c: c[1]-c[0])
                mid = 0.5*(best[0]+best[1])
                si = np.sign(np.interp(mid - A, t, fun[i], left=0.0, right=0.0))
                sj = np.sign(np.interp(mid, t, fun[j]))
                P[i, j] = si*sj
        tab[str(n)] = dict(v=float(v), a=float(A), J=J.tolist(), pred=P.tolist(),
                           atom=(-v*J).tolist(),
                           agree=int(np.sum(np.sign(J) == P)), total=nmodes*nmodes,
                           fails=[[i, j, float(J[i, j]), float(P[i, j])]
                                  for i in range(nmodes) for j in range(nmodes)
                                  if np.sign(J[i, j]) != P[i, j]])
    res['atoms'] = tab
    # full pi table for cross-check
    PI = np.zeros((nmodes, nmodes))
    for n in contacts:
        v = 2*vm[n]/np.sqrt(n); Cm = Z.T @ ac.Cmat(np.log(n), T, N) @ Z
        PI += -v*np.array([[float(V[:, E[i]] @ Cm @ V[:, E[j]]) for j in range(nmodes)] for i in range(nmodes)])
    res['pi'] = PI.tolist()
    res['pi_vs_lemmaN'] = float(np.max(np.abs(PI - sum(np.array(tab[str(n)]['atom']) for n in contacts))))
    return res

for T, N in [(float(np.log(2)), 18), (float(np.log(2)), 36), (0.65, 18)]:
    out['T%.6f_N%d' % (T, N)] = run(T, N)

# growth of eigenvalues: many even modes at log2, N=60
T = float(np.log(2)); N = 60
G = ac.gamma_matrix(T, N); Pl, a, b = ac.pole_matrix(T, N)
Z = np.linalg.svd(np.column_stack([a, b]), full_matrices=True)[0][:, 2:]
ev, V = np.linalg.eigh(Z.T @ G @ Z)
coef = Z @ V; par = np.array([(-1)**k for k in range(N)])
pv = [float(np.sum(par*coef[:, j]**2)) for j in range(V.shape[1])]
E = [j for j in range(V.shape[1]) if pv[j] > 0.5]
lam = [float(ev[j]) for j in E]
tau = np.linspace(0.01, 400, 40000)
m = ac.msym(tau) if hasattr(ac, 'msym') else None
out['growth'] = dict(N=N, lam_even=lam[:25],
                     k_with_lam_le_2249=int(sum(1 for x in lam if x <= 2.2489)),
                     pred_m_at_pi_k_over_T=[float((2*k+1)*np.pi/(2*T)) for k in range(12)])
json.dump(out, open(os.path.join(HERE, 'r6a_01.json'), 'w'), indent=1)
print(json.dumps({k: (v if k == 'growth' else dict(lam=v['lam'], npos=v['npos'], nodes=v['nodes'],
      agree={n: (v['atoms'][n]['agree'], v['atoms'][n]['total']) for n in v['atoms']},
      chk=v['pi_vs_lemmaN'])) for k, v in out.items()}, indent=1)[:6000])
