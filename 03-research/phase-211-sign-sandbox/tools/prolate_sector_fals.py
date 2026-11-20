"""Falsifier test for the selection of the bottom: minimiser of a^w_T on P_T (even sector) against the span of the
class-(+1) prolate images Pi_T P_+ E psi_{4j}, 4j <= KTOP.  (NUMERICAL tool)  Usage: T Nb dps KMAX KTOP"""
import sys, os, pickle, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4]); KTOP = int(sys.argv[5])
D = G.build(T, Nb, dps=dps, verbose=False); mp.mp.dps = dps + 20
P = pickle.load(open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb')); ks = P['ks']
g = pickle.load(open(os.path.join(G.CACHE, f'sector_g_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb'))['g']
g = [mp.matrix([mp.mpf(x) for x in v]) for v in g]
def dot(a, b): return mp.fsum(a[i]*b[i] for i in range(Nb))
def pplus(v):
    w = mp.matrix(v)
    for j in range(1, Nb, 2): w[j] = 0
    return w
for cls, lab in ((0, '+1'), (2, '-1')):
    U = [pplus(g[i]) for i, k in enumerate(ks) if k % 4 == cls and k <= KTOP]
    n = len(U); Gm = mp.matrix(n, n)
    for a in range(n):
        for b in range(n): Gm[a, b] = dot(U[a], U[b])
    E, W = mp.eigsy(Gm); keep = [i for i in range(n) if E[i] > max(E)*mp.mpf(10)**(-(dps-5))]
    Ob = [sum((U[a]*(W[a, i]/mp.sqrt(E[i])) for a in range(n)), mp.matrix(Nb, 1)) for i in keep]
    def angle(u):
        u = u/mp.sqrt(dot(u, u)); pr = mp.fsum(dot(o, u)**2 for o in Ob); return mp.acos(min(1, mp.sqrt(pr)))
    def atoms_pi(atoms):
        L = 2*D['T']; al = [k*mp.pi/L for k in range(1, Nb+1)]; Pm = mp.matrix(Nb, Nb)
        for j in range(1, Nb+1):
            for k in range(j, Nb+1):
                Pm[j-1, k-1] = Pm[k-1, j-1] = mp.fsum(w*G._c_sym(j, k, x, L, al) for x, w in atoms)
        return Pm
    v2 = 2*mp.log(2)/mp.sqrt(2)
    cases = [('Lambda', D['Pi']), ('0.99 Lambda', 0.99*D['Pi']), ('1.01 Lambda', 1.01*D['Pi'])]
    if cls == 0:
        P2 = atoms_pi([(mp.log(2**a), 2*mp.log(2)/mp.sqrt(2**a)) for a in range(1, 6) if a*mp.log(2) < 2*D['T']])
        cases += [('a_3 (prime 2 deleted)', D['Pi'] - P2), ('Lambda + 0.1 v_2 at n=2', D['Pi'] + atoms_pi([(mp.log(2), mp.mpf('0.1')*v2)]))]
    globals()['cases_saved'] = cases
    print(f"# T={T}: class {lab} span (k <= {KTOP}, dim {len(Ob)}), even sector of P_T")
    Q = G.sector_basis(D, 'ev')
    for name, Pm in cases:
        H = Q.T*(D['Arch'] - Pm)*Q; E2, W2 = mp.eigsy(H); i0 = min(range(len(E2)), key=lambda i: E2[i]); u = Q*W2[:, i0]
        print(f"  {name:26s}: lambda^ev = {mp.nstr(E2[i0],4)}, angle(minimiser, class {lab} span) = {mp.nstr(angle(u),4)}")
