"""r8a_03: independent re-check of the r8a_02 lower-bound certificates from their archived JSON.

usage: python3 r8a_03_recheck_lower.py [inflate=1e-9]

For every r8a_02_*.json it rebuilds the 3x3 bordered matrix
    B3 = [[Gamma[F], Gamma(F,h), <F,g>], [Gamma(F,h), Gamma[h], <h,g>], [<F,g>, <h,g>, 0]]
from the stored enclosures, INFLATES every entry by +-inflate (absolute; covers (i) the rounding
of the stored interval ends to double and (ii) the float rounding of F+h, F-h in the polarisation
Gamma(F,h) = (Gamma[F+h]-Gamma[F-h])/4, bounded by 1e-10 in R155_052 Lemma 3.3), and certifies with
mpmath interval arithmetic that -U^T B3 U is positive definite for EVERY matrix in the inflated box,
U = the two bottom eigenvectors of the midpoint matrix (float, converted exactly).  It also returns a
certified lower bound mu on lambda_min(-U^T B3 U) by bisection.  The range condition T < 0.88137 of
r8a_02 is re-imposed: windows outside it are reported as NOT certified whatever the matrix says.
"""
import sys, os, json, glob
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r8a_lib import iv, mp, cholesky_pd, congruence

ARCCOSH_SQRT2 = 0.881373587019543
def Tval(s):
    return float(np.log(2)) if s == 'log2' else (0.5 * float(np.log(3)) if s == 'halflog3' else float(s))

def box(pair, infl):
    lo_, hi_ = pair
    return iv.mpf([mp.mpf(lo_) - mp.mpf(infl), mp.mpf(hi_) + mp.mpf(infl)])

def main(infl=1e-9):
    rows = []
    for fn in sorted(glob.glob(os.path.join(HERE, 'r8a_02_*.json'))):
        d = json.load(open(fn))
        gF, gFh, gh, pF, ph = (box(d[k], infl) for k in ('GammaF', 'GammaFh', 'Gammah', 'Fg', 'hg'))
        B3 = [[gF, gFh, pF], [gFh, gh, ph], [pF, ph, iv.mpf(0)]]
        Bm = np.array([[0.5 * (float(x.a) + float(x.b)) for x in r] for r in B3])
        e, U = np.linalg.eigh(Bm)
        C = congruence(U[:, :2], [[-x for x in r] for r in B3])
        ok = bool(e[1] < 0 and cholesky_pd(C))
        mu = 0.0
        if ok:
            lo_, hi_ = 0.0, float(-e[1])
            for _ in range(40):
                m_ = 0.5 * (lo_ + hi_)
                if cholesky_pd(C, iv.mpf(repr(m_))):
                    lo_ = m_
                else:
                    hi_ = m_
            mu = lo_
        inrange = Tval(d['T']) < ARCCOSH_SQRT2
        rows.append(dict(file=os.path.basename(fn), T=d['T'], par=d['par'], in_range=inrange,
                         two_negative_box=ok, mu_lower=mu, certified_lower_bound_sector=int(ok and inrange)))
    for r in rows:
        print(r)
    json.dump(dict(inflate=infl, rows=rows), open(os.path.join(HERE, 'r8a_03_recheck.json'), 'w'), indent=1)

if __name__ == '__main__':
    main(float(sys.argv[1]) if len(sys.argv) > 1 else 1e-9)
