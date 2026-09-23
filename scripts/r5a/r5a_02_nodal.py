"""r5a_02: nodal geometry of the atom signs in pi_13 at log 2 (and 0.62, 0.65).

Identity used (PROVED, see the note):  <Re(R_T tau_a R_T) F, e> = int F(y) * e_a(y) dy
with e_a(y) = 1/2 ( e~(y+a) + e~(y-a) ), e~ = e extended by zero off (-T,T).
So the sign of each prime atom is the sign of the shifted-and-averaged eigenfunction e
sampled against the weight F (= F*, the archimedean ground state).
DIAGNOSTIC (double precision, Galerkin); the identity itself is PROVED.
"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import arch_core as ac

HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for T in [float(np.log(2)), 0.62, 0.65]:
    N = 18
    G = ac.gamma_matrix(T, N); Pl, a, b = ac.pole_matrix(T, N)
    Z = np.linalg.svd(np.column_stack([a, b]), full_matrices=True)[0][:, 2:]
    Ainf = Z.T @ G @ Z
    ev, V = np.linalg.eigh(Ainf)
    coef = Z @ V
    par = np.array([(-1)**k for k in range(N)])
    pv = [float(np.sum(par*coef[:, j]**2)) for j in range(V.shape[1])]
    E = [j for j in range(V.shape[1]) if pv[j] > 0.5][:4]
    vm = ac.vonmangoldt(int(np.exp(2*T))+1)
    contacts = [n for n in sorted(vm) if np.log(n) < 2*T]
    # sample the eigenfunctions
    t = np.linspace(-T, T, 4001); B = ac.basis(t, T, N)
    fun = {}
    for r, j in enumerate(E):
        y = B @ coef[:, j]
        if y[np.argmax(np.abs(y))] < 0: y = -y; coef[:, j] = -coef[:, j]
        fun[r] = y
    Fs, e3 = fun[0], fun[1]
    # nodes of e3 and of F*
    def nodes(y):
        s = np.where(np.sign(y[:-1]) != np.sign(y[1:]))[0]
        return [float(t[i] - y[i]*(t[i+1]-t[i])/(y[i+1]-y[i])) for i in s]
    rec = dict(T=T, contacts=contacts, lam_even=[float(ev[j]) for j in E],
               nodes_e3=nodes(e3), nodes_Fstar=nodes(Fs),
               Fstar_min=float(Fs.min()), Fstar_max=float(Fs.max()),
               Fstar_mass=float(np.trapz(Fs, t)),
               Fstar_negmass=float(np.trapz(np.minimum(Fs, 0.0), t)))
    atoms = {}
    for n in contacts:
        v = 2*vm[n]/np.sqrt(n); A = np.log(n)
        Cm = Z.T @ ac.Cmat(A, T, N) @ Z
        pi13 = -v*float(V[:, E[0]] @ Cm @ V[:, E[1]])
        pi11 = -v*float(V[:, E[0]] @ Cm @ V[:, E[0]])
        pi33 = -v*float(V[:, E[1]] @ Cm @ V[:, E[1]])
        # pointwise check: e3_a(y) = 1/2(e3~(y+a)+e3~(y-a)), sampled value at 0 = e3(a)
        e3a = np.zeros_like(t)
        for sgn in (+1, -1):
            yy = t + sgn*A; ok = np.abs(yy) < T
            e3a[ok] += 0.5*np.interp(yy[ok], t, e3)
        ip = float(np.trapz(Fs*e3a, t))
        atoms[str(n)] = dict(v=float(v), a=float(A), pi13_atom=pi13, pi11_atom=pi11,
                             pi33_atom=pi33, overlap_direct=ip, minus_v_times=-v*ip,
                             e3_at_a=float(np.interp(A, t, e3)) if A < T else 0.0,
                             sign_pred_by_e3_at_a=int(np.sign(np.interp(A, t, e3))) if A < T else 0)
    rec['atoms'] = atoms
    out['T%.6f' % T] = rec
    print('T=%.5f contacts=%s nodes(e3)=%s nodes(F*)=%s F*mass=%.4f negmass=%.4f'
          % (T, contacts, ['%.4f' % z for z in rec['nodes_e3']],
             ['%.4f' % z for z in rec['nodes_Fstar']], rec['Fstar_mass'], rec['Fstar_negmass']))
    for n, d in atoms.items():
        print('   n=%s a=%.4f  atom(1,3)=%+.4f  direct=%+.4f  e3(a)=%+.4f' %
              (n, d['a'], d['pi13_atom'], d['minus_v_times'], d['e3_at_a']))
json.dump(out, open(os.path.join(HERE, 'r5a_02.json'), 'w'), indent=1)
