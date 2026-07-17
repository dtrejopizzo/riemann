"""
W-4 refinado: la *-incompatibilidad de A_lambda es "mezcla H1[n!=0] con polo[n=0]" (E52).
El * mata n=0 (es el H^0 real). PREGUNTA: ¿el sector POLE-FREE (H1, n!=0) es *-compatible?
Si al sacar el polo  |Sst^H A Sst - A|  cae a ~0 en el bloque n!=0 => el H1 es CUATERNIONICO
=> su positividad seria ESTRUCTURAL (via *^2=-1, mecanismo E51), no aditiva.
Mide FULL vs H1(pole-free) vs solo-fila-polo, con la forma de Weil FIEL (engine_cache). DH falsador.
"""
import sys, mpmath as mp
from engine_cache import get_matrices

mp.mp.dps = 40


def star_matrix(idx):
    dim = len(idx); S = mp.zeros(dim)
    for a, n in enumerate(idx):
        if n != 0:
            b = idx.index(-n)
            S[b, a] = mp.mpc(0, 1) * (1 if n > 0 else -1)
    return S


def run(lam, N, kind='zeta'):
    La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40)
    Ac = mp.matrix(A.rows, A.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            Ac[i, j] = mp.mpc(A[i, j])
    S = star_matrix(idx)
    M = S.H * Ac * S - Ac
    dim = len(idx); z = idx.index(0)
    full = max(abs(M[i, j]) for i in range(dim) for j in range(dim))
    h1 = max(abs(M[i, j]) for i in range(dim) for j in range(dim) if i != z and j != z)
    polerow = max(abs(M[z, j]) for j in range(dim))
    print(f"  {kind} lam={lam} L={L:.2f}: FULL={float(full):.4f}  H1(pole-free)={float(h1):.4f}  "
          f"fila-polo={float(polerow):.4f}  => {'H1 CUATERNIONICO' if h1<0.01 else 'H1 aun mezcla'}")
    return float(full), float(h1)


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18), (15.0, 20), (19.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("W-4 — *-compatibilidad del sector pole-free H1 (¿cuaterniónico sin el polo?)")
    for lam, N in grid:
        run(lam, N, 'zeta')
    print("FALSADOR DH:")
    run(7.0, 14, 'DH')
