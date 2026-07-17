"""
SUB-HILO: a_j = QW(V_j,V_j) > 0 (positividad de Weil DIAGONAL, modo-a-modo).
Descomponer a_j = polo_j - WR_j - primo_j y testear:
 (1) ¿a_j tiene MARGEN uniforme (min a_j >= c > 0, acotado lejos de 0) => RH-NEUTRAL/demostrable,
     a diferencia del muro mu_lambda ~ e^{-cL} ~ 0 (marginal)? Si a_j tiene margen, es mas fuerte.
 (2) ¿la dominancia es polo_j >= WR_j + primo_j modo-a-modo (estructural)?
 (3) margen de a_j vs lambda: ¿estable? DH: a_j NO todos > 0.
polo_j = int q_jj(y) 2cosh(y/2) dy,  q_jj=2(1-y/L)cos(2pi j y/L).
"""
import sys, numpy as np, mpmath as mp
from engine_cache import get_matrices
import engine_cache as EC

mp.mp.dps = 40


def pole_diag(idx, L):
    Lm = mp.mpf(L); out = {}
    for n in idx:
        q = EC.q_func(n, n, Lm)
        out[n] = float(mp.quad(lambda y: q(y) * 2 * mp.cosh(y / 2), [0, Lm]))
    return out


def run(lam, N, kind='zeta'):
    La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40)
    dim = len(idx)
    a = np.array([float(A[i, i]) for i in range(dim)])
    arch = np.array([float(La[i, i]) for i in range(dim)])   # ARCH diag = polo - WR
    prime = np.array([float(Lp[i, i]) for i in range(dim)])  # PRIME diag
    pol = pole_diag(idx, L)
    pold = np.array([pol[idx[i]] for i in range(dim)])
    WR = pold - arch     # WR = polo - ARCH
    # mu_lambda (marginal)
    mu = float(min(np.linalg.eigvalsh(np.array([[float(A[i, j]) for j in range(dim)] for i in range(dim)]))))
    print(f"\n{kind} lam={lam} L={L:.2f}")
    print(f"  min a_j = {a.min():+.4f}  (margen diagonal)   mu_lambda(muro) = {mu:+.3e}")
    print(f"  => a_j {'TODOS >0 con margen ' + f'{a.min():.3f}' if a.min()>1e-6 else 'NO todos >0'}; "
          f"a_j {'TIENE MARGEN (no marginal)' if a.min()>1e-3 else 'marginal'} vs muro marginal")
    # dominancia modo a modo: polo_j vs WR_j + prime_j
    rhs = WR + prime
    dom = pold - rhs   # = a_j
    margin_ratio = pold / np.where(np.abs(rhs) > 1e-12, rhs, 1e-12)
    print(f"  dominancia polo_j vs (WR+prime)_j: min(polo-(WR+prime))={dom.min():+.4f}  "
          f"min ratio polo/(WR+prime)={np.nanmin(margin_ratio[np.isfinite(margin_ratio)]):+.3f}")
    # cuales modos son los mas chicos (margen minimo)
    k = int(np.argmin(a))
    print(f"  modo de menor a_j: n={idx[k]}  a={a[k]:.4f} = polo {pold[k]:.3f} - WR {WR[k]:.3f} - prime {prime[k]:.3f}")
    return a.min(), mu


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18), (15.0, 20), (19.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E95 — sub-hilo: positividad de Weil DIAGONAL a_j>0, ¿margen uniforme (RH-neutral)?")
    rows = []
    for lam, N in grid:
        rows.append(run(lam, N, 'zeta'))
    print(f"\n  margen min a_j vs lambda: {[(round(7+2*i,0), round(r[0],4)) for i,r in enumerate(rows)]}")
    print(f"  (si min a_j se mantiene acotado lejos de 0 mientras mu->0 => a_j>0 es RH-NEUTRAL)")
    run(7.0, 14, 'DH')
