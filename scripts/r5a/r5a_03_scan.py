"""r5a_03: the sign-flip locus a_c of the atom overlap I(a) = <Re(R tau_a R) F*, e3>,
and the edge-lobe threshold a* = T + z_e (z_e = outermost node of e3).
The contact set {2,3} must straddle a_c for the two atoms to cancel.  DIAGNOSTIC.
"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import arch_core as ac
HERE = os.path.dirname(os.path.abspath(__file__)); out = {}
for T in [float(np.log(2)), 0.62, 0.65]:
    N = 18
    G = ac.gamma_matrix(T, N); Pl, a0, b0 = ac.pole_matrix(T, N)
    Z = np.linalg.svd(np.column_stack([a0, b0]), full_matrices=True)[0][:, 2:]
    ev, V = np.linalg.eigh(Z.T @ G @ Z); coef = Z @ V
    par = np.array([(-1)**k for k in range(N)])
    E = [j for j in range(V.shape[1]) if float(np.sum(par*coef[:, j]**2)) > 0.5][:2]
    t = np.linspace(-T, T, 6001); B = ac.basis(t, T, N)
    fs = [B @ coef[:, j] for j in E]
    fs = [y if y[np.argmax(np.abs(y))] > 0 else -y for y in fs]
    for j, y in zip(E, fs):
        if (B @ coef[:, j])[np.argmax(np.abs(B @ coef[:, j]))] < 0: coef[:, j] *= -1
    Fs, e3 = fs
    def nodes(y):
        s = np.where(np.sign(y[:-1]) != np.sign(y[1:]))[0]
        return [float(t[i]-y[i]*(t[i+1]-t[i])/(y[i+1]-y[i])) for i in s]
    ze = max(nodes(e3)); zf = max(nodes(Fs))
    aa = np.linspace(0.02, 2*T-0.005, 220)
    I = []
    for A in aa:
        C = Z.T @ ac.Cmat(A, T, N) @ Z
        I.append(float(V[:, E[0]] @ C @ V[:, E[1]]))
    I = np.array(I)
    zc = [float(aa[i]-I[i]*(aa[i+1]-aa[i])/(I[i+1]-I[i]))
          for i in np.where(np.sign(I[:-1]) != np.sign(I[1:]))[0]]
    rec = dict(T=T, ze=ze, zf=zf, a_star_e=T+ze, a_star_F=T+zf, zeros_I=zc,
               I_log2=float(np.interp(np.log(2), aa, I)),
               I_log3=float(np.interp(np.log(3), aa, I)) if np.log(3) < 2*T else None,
               straddle=bool(any(np.log(2) < z < np.log(3) for z in zc)))
    out['T%.6f' % T] = rec
    print('T=%.5f  z_e=%.4f z_F=%.4f  a*(e3)=%.4f  zeros of I(a): %s  I(log2)=%+.4f I(log3)=%s straddle=%s'
          % (T, ze, zf, T+ze, ['%.4f' % z for z in zc], rec['I_log2'],
             ('%+.4f' % rec['I_log3']) if rec['I_log3'] is not None else 'n/a', rec['straddle']))
json.dump(out, open(os.path.join(HERE, 'r5a_03.json'), 'w'), indent=1)
