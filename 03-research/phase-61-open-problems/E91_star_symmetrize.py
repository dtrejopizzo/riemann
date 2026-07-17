"""
W-5: *-simetrizar A_lambda. A = Â + Ǎ con Â=(A+Sst^H A Sst)/2 (*-compatible) y Ǎ el resto (~0.07).
Si Â (parte cuaternionica) es PSD ESTRUCTURALMENTE (via *^2=-1) y CONTROLA el signo de eps_0
(la parte incompatible Ǎ no hunde el ground state) => muro estructural.
Tests: min-eig(A) vs min-eig(Â) vs min-eig(Ǎ); ¿signo(eps_0(A))=signo(min-eig(Â))? ¿Â PSD para zeta
y NO para DH? DH falsador.
"""
import sys, mpmath as mp
from engine_cache import get_matrices

mp.mp.dps = 40


def star_matrix(idx):
    dim = len(idx); S = mp.zeros(dim)
    for a, n in enumerate(idx):
        if n != 0:
            S[idx.index(-n), a] = mp.mpc(0, 1) * (1 if n > 0 else -1)
    return S


def mineig(M):
    E, _ = mp.eigsy(M) if M == M.H and all(M[i, j].imag == 0 for i in range(M.rows) for j in range(M.cols)) else mp.eighe(M)
    return min(float(mp.re(E[i])) for i in range(M.rows))


def run(lam, N, kind='zeta'):
    La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40)
    Ac = mp.matrix(A.rows, A.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            Ac[i, j] = mp.mpc(A[i, j])
    S = star_matrix(idx)
    Asym = (Ac + S.H * Ac * S) / 2     # parte *-compatible (cuaternionica)
    Aasy = (Ac - S.H * Ac * S) / 2     # parte incompatible
    # min eigenvalues (Hermitianas)
    def mineigH(M):
        E, _ = mp.eighe(M)
        return min(float(mp.re(x)) for x in E)
    e0A = mineigH(Ac); e0sym = mineigH(Asym); e0asy = mineigH(Aasy)
    print(f"  {kind} lam={lam} L={L:.2f}: min-eig A={e0A:+.3e}  Â(*-sim)={e0sym:+.3e}  "
          f"Ǎ(resto)={e0asy:+.3e}  => Â {'PSD' if e0sym>=-1e-12 else 'INDEF'}, "
          f"signo coincide: {(e0A>0)==(e0sym>0)}")
    return e0A, e0sym


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18), (15.0, 20), (19.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("W-5 — *-simetrizacion: ¿la parte cuaternionica Â es PSD y controla eps_0?")
    for lam, N in grid:
        run(lam, N, 'zeta')
    print("FALSADOR DH:")
    run(7.0, 14, 'DH')
