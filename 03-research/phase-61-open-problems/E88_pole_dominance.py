"""
W-2 (plan WALL): el muro <=> eps_0 = P(u_0) - WR(u_0) - PRIME(u_0) >= 0 sobre el ground state u_0,
donde P = termino de POLO (la fuente de positividad: int q 2cosh(u/2) du; ausente en DH).
Tesis: el polo P(u_0) (~ masa concentrada, manifiestamente >=0) DOMINA a WR+PRIME para el
ground state prolato-concentrado => sobrepaso => muro.

GATE: separar eps_0 en P(u_0), WR(u_0), PRIME(u_0); medir el MARGEN P-(WR+PRIME) y la razon
P/(WR+PRIME) y su tendencia en lambda. Si P/(WR+PRIME) -> 1+ por arriba con cota => pole-dominance.
Falsador DH (sin polo: P=0, eps_0<0).
"""
import sys, mpmath as mp
from engine_cache import get_matrices
import engine_cache as EC

mp.mp.dps = 45


def pole_matrix(idx, L):
    """P_mn = int_0^L q_mn(u) 2 cosh(u/2) du  (termino de polo = W02)."""
    dim = len(idx); Lm = mp.mpf(L); M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            q = EC.q_func(idx[a], idx[b], Lm)
            v = mp.quad(lambda u: q(u) * 2 * mp.cosh(u / 2), [0, Lm])
            M[a, b] = v; M[b, a] = v
    return M


def quad_form(M, u):
    return float((u.T * M * u)[0])


def run(lam, N, kind='zeta'):
    Larch, Lpr, A, L, idx = get_matrices(lam, N, kind, dps=45)
    E, V = mp.eigsy(A)
    order = sorted(range(A.rows), key=lambda j: float(E[j]))
    u0 = mp.matrix([V[i, order[0]] for i in range(A.rows)])
    nrm = float((u0.T * u0)[0])
    # pole y WR:  ARCH = W02(pole) - WR  =>  WR = W02 - ARCH
    W02 = pole_matrix(idx, L)
    P = quad_form(W02, u0) / nrm
    WR = quad_form(W02 - Larch, u0) / nrm
    PR = quad_form(Lpr, u0) / nrm
    e0 = quad_form(A, u0) / nrm
    print(f"\n{kind} lam={lam} L={L:.3f}")
    print(f"  P(polo)={P:+.5f}  WR(arq)={WR:+.5f}  PRIME={PR:+.5f}")
    print(f"  eps_0 = P - WR - PRIME = {e0:+.4e}   (check inf-spec)")
    print(f"  pole-dominance: P vs (WR+PRIME) = {P:+.5f} vs {WR+PR:+.5f}   "
          f"margen={P-(WR+PR):+.4e}  ratio P/(WR+PR)={P/(WR+PR):.6f}")
    return P, WR, PR, e0, L


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18), (15.0, 20), (19.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("W-2 GATE — pole-dominance sobre el ground state u_0")
    rows = []
    for lam, N in grid:
        rows.append(run(lam, N, 'zeta'))
    print("\n  tendencia ratio P/(WR+PRIME) vs lambda:",
          [(r[4].__round__(2), round(r[0] / (r[1] + r[2]), 5)) for r in rows])
    print("\nFALSADOR DH:")
    run(7.0, 14, 'DH')
