"""Evaluate (interval arithmetic) the window form with four combs on the SAME certified Lemma-E vector (T=8/5, full, deg<49):
Q (Epstein), K (Dedekind zeta of Q(sqrt-5): same Gamma factor, conductor, pole), Qprime, Kcomp. Rebuilds g from cert_T1.6_full49.txt."""
import os, ast, re
os.environ.setdefault('IVDPS', '120')
import cert_epstein as C
from cert_epstein import iv, Fr, ivf, tate_mom
txt = open('cert_T1.6_full49.txt').read()
g0 = [Fr(x) for x in ast.literal_eval(txt.split('(x^0..):')[1].strip())]
T = iv.mpf(8) / 5; Mdeg = len(g0); R = 2 * Mdeg + 2
cp, cm = T / 2, -T / 2
r1 = -sum(ivf(g0[j]) * tate_mom(cp, j) for j in range(Mdeg) if g0[j] != 0)
r2 = -sum(ivf(g0[j]) * tate_mom(cm, j) for j in range(Mdeg) if g0[j] != 0)
a11, a12, a21, a22 = tate_mom(cp, 0), tate_mom(cp, 1), tate_mom(cm, 0), tate_mom(cm, 1); det = a11 * a22 - a12 * a21
g = [ivf(x) if x != 0 else 0 for x in g0]; g[0] = (r1 * a22 - a12 * r2) / det; g[1] = (a11 * r2 - a21 * r1) / det
mom = C.Kmoments(T, R)
LQ0 = C.LQ; K = C._LK(500)
from sympy import factorint
from sympy import jacobi_symbol
def chi(D, n):
    if D == -4: return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
    return 0 if n % 5 == 0 else jacobi_symbol(n, 5)
Psi = {}
for n in range(2, 501):
    f = factorint(n)
    if len(f) == 1:
        p, k = list(f.items())[0]; c = chi(-4, p) ** k + chi(5, p) ** k
        if c: Psi[n] = {p: Fr(c)}
combs = {'psi': Psi, 'Q': LQ0, 'K': K, 'Qprime': {n: d for n, d in LQ0.items() if len(factorint(n)) == 1},
         'Kcomp': {**K, **{n: d for n, d in LQ0.items() if len(factorint(n)) > 1}}}
vals = {}
for name, lam in combs.items():
    C.LQ = lam
    Q, c0, pc = C.quotient(T, g, C.contacts(T), mom, R, pieces=True)
    vals[name] = Q
    print(name, 'contacts', C.contacts(T), 'value in [%s, %s]' % (iv.mpf(Q.a), iv.mpf(Q.b)), 'comb', pc['comb'].mid,
          {n: float(t.mid) for n, t in pc['terms'].items()}, flush=True)
m = (vals['K'] + vals['psi']) / 2
print('mean of Euler forms (K+psi)/2 in [%s, %s]' % (iv.mpf(m.a), iv.mpf(m.b)))
d = vals['Q'] - m
print('cosh-defect contribution Q - (K+psi)/2 in [%s, %s]' % (iv.mpf(d.a), iv.mpf(d.b)))
