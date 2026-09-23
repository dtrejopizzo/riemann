"""R155.032 round 4a, task (2): RIGOROUS positive-definiteness of the Weil form W_T
on the explicit nested even subspaces span{e_1, e_3, ..., e_{2k+1}} at T = log 2
(and, for comparison, 0.62 and 0.65).

The e's are the ARCHIVED degree-17 polynomials of r4a_01.json (Legendre coefficients
of the N = 18 Galerkin archimedean eigenvectors of A_inf|P_T, even sector, e_1 = F*).
How they were obtained is irrelevant to the statement: they are given data.

Method.  For each pair (i,j) the matrix entry is obtained by POLARISATION,
   M_ij = ( W[e_i + e_j] - W[e_i - e_j] ) / 4 ,
so that only QUADRATIC values of the form are ever enclosed -- which is what makes
the affine-sandwich bound of r4a_lib legitimate (it needs G = c(0) - c >= 0, true for
an autocorrelation by Cauchy-Schwarz, false for a cross-correlation).
Positive definiteness of the resulting interval matrix is certified by interval
Cholesky, and a lower bound on its smallest eigenvalue by bisection on mu in
Cholesky(M - mu I).  The Gram matrix of the basis is enclosed too, so the bound is
transferred to the Rayleigh quotient: W[F] >= (lam_min(M)/lam_max(Gram)) ||F||^2.
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mpmath import iv, mp
import r4a_lib as lib

t0 = time.time()
PANELS = int(os.environ.get('R4A_PANELS', 8000))
KMAX = int(os.environ.get('R4A_KMAX', 6))
TAG = os.environ.get('R4A_T', 'log2')
TS = {'log2': ('0.693147180559945309417232121458176568075500134360255254120680', 'N18_T0.693147'),
      '0.62': ('0.62', 'N18_T0.620000'),
      '0.65': ('0.65', 'N18_T0.650000')}
Tstr, key = TS[TAG]
arch = json.load(open(os.path.join(HERE, 'r4a_01.json')))[key]
E = arch['even_coef'][:KMAX]
N = arch['N']
print('T = %s   N = %d   panels = %d   basis vectors = %d' % (TAG, N, PANELS, len(E)))

LF = lib.LevyForm(Tstr, N, panels=PANELS)
print('panel functionals built, %.1fs' % (time.time()-t0))

def add(u, v, s=1):  return [x + s*y for x, y in zip(u, v)]

cache = {}
def Wq(vec, tag):
    if tag in cache: return cache[tag]
    val, _ = LF.W(vec)
    cache[tag] = val
    return val

k = len(E)
M = [[None]*k for _ in range(k)]
for i in range(k):
    M[i][i] = Wq(E[i], 'd%d' % i)
for i in range(k):
    for j in range(i+1, k):
        p = Wq(add(E[i], E[j]), 'p%d_%d' % (i, j))
        m = Wq(add(E[i], E[j], -1), 'm%d_%d' % (i, j))
        M[i][j] = M[j][i] = (p - m)/iv.mpf(4)
print('matrix entries enclosed, %.1fs' % (time.time()-t0))

# Gram matrix (exact: orthonormal Legendre basis)
Gm = [[None]*k for _ in range(k)]
Ei = [[iv.mpf(repr(x)) for x in v] for v in E]
for i in range(k):
    for j in range(k):
        s = iv.mpf(0)
        for x, y in zip(Ei[i], Ei[j]): s = s + x*y
        Gm[i][j] = s
gdev = max(max(abs((Gm[i][j] - (iv.mpf(1) if i == j else iv.mpf(0))).b),
               abs((Gm[i][j] - (iv.mpf(1) if i == j else iv.mpf(0))).a))
           for i in range(k) for j in range(k))
print('max |Gram - I| entry <= %.2e' % float(gdev))

res = {'T': TAG, 'N': N, 'panels': PANELS, 'gram_dev': float(gdev), 'blocks': []}
print('\n k  dim  lam_min lower bound (rigorous)   entry widths   status')
for kk in range(1, k+1):
    B = [[M[i][j] for j in range(kk)] for i in range(kk)]
    wmax = max(float(B[i][j].b - B[i][j].a) for i in range(kk) for j in range(kk))
    lo = lib.lam_min_lower(B, 0.0, 0.1, iters=45)
    mid = [[0.5*(float(B[i][j].a)+float(B[i][j].b)) for j in range(kk)] for i in range(kk)]
    try:
        import numpy as np
        fl = float(np.linalg.eigvalsh(np.array(mid))[0])
    except Exception:
        fl = None
    ok = lo is not None
    res['blocks'].append(dict(k=kk, lam_min_lower=lo, float_lam_min=fl,
                              max_entry_width=wmax, certified=ok))
    print(' %d   %d   %s   %.2e   %s  (float mid: %.3e)' %
          (kk, kk, ('%.6e' % lo) if ok else 'NOT CERTIFIED', wmax,
           'PD' if ok else 'fail', fl))
res['matrix'] = [[[float(M[i][j].a), float(M[i][j].b)] for j in range(k)] for i in range(k)]
res['runtime_s'] = time.time()-t0
json.dump(res, open(os.path.join(HERE, 'r4a_02_%s_M%d_k%d.json' % (TAG, PANELS, KMAX)), 'w'), indent=1)
print('runtime %.1fs' % (time.time()-t0))
