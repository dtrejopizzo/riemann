"""
W-SYMPLECTIC: segunda relacion bilineal de Hodge-Riemann como certificado del muro.
Peso 1 (H^1 = modos n!=0; el polo n=0 = H^0 aparte). HR dice: la forma g(v,v)=A_lambda(v, *v)
es DEFINIDA sobre H^1, con el signo fijado por la estructura compleja * (*^2=-1).
g PD <=> (Omega=ecuacion funcional, J=*) compatibles = polarizacion = positividad de Weil.

H = parte Hermitiana de A·Sigma (Sigma = parte lineal de *, *e_n = i sgn(n) e_{-n}).
Restringir a H^1 (n!=0). Firma para:
  - ZETA (debe ser definida si HR vale para la forma de Weil aritmetica)
  - CONTROL M aleatoria simetrica con la MISMA simetria A_{-m,-n}=A_{mn}: ¿g_M tambien definida?
       * si SI => positividad ALGEBRAICA (de *), estructural, NO-circular => CRUZA.
       * si NO => la positividad necesita A aritmetica = circular (RH disfrazada).
  - DH (debe fallar).
"""
import sys, numpy as np, mpmath as mp
from engine_cache import get_matrices

mp.mp.dps = 40


def sigma(idx):
    dim = len(idx); S = np.zeros((dim, dim), complex)
    for a, n in enumerate(idx):
        if n != 0:
            S[idx.index(-n), a] = 1j * (1 if n > 0 else -1)
    return S


def hr_signature(Anp, idx, label):
    S = sigma(idx)
    H = Anp.astype(complex) @ S
    H = (H + H.conj().T) / 2          # parte Hermitiana = forma HR
    z = idx.index(0)
    keep = [i for i in range(len(idx)) if i != z]   # H^1 = n!=0
    Hp = H[np.ix_(keep, keep)]
    ev = np.linalg.eigvalsh(Hp)
    npos = int((ev > 1e-9).sum()); nneg = int((ev < -1e-9).sum()); nz = len(ev) - npos - nneg
    definite = (npos == 0 or nneg == 0)
    print(f"  [{label}] firma H^1 (pos,0,neg)=({npos},{nz},{nneg})  min|ev|extremos=[{ev.min():+.3e},{ev.max():+.3e}]"
          f"  => {'DEFINIDA' if definite else 'INDEFINIDA'}")
    return definite, npos, nneg


def run(lam, N):
    La, Lp, A, L, idx = get_matrices(lam, N, 'zeta', dps=40)
    dim = len(idx)
    Anp = np.array([[float(A[i, j]) for j in range(dim)] for i in range(dim)])
    print(f"\nlam={lam} N={N} dim={dim}")
    hr_signature(Anp, idx, "ZETA")
    # CONTROL: M aleatoria simetrica con la misma simetria A_{-m,-n}=A_{mn}
    rng = np.random.default_rng(0)
    M = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(i, dim):
            v = rng.standard_normal()
            M[i, j] = v; M[j, i] = v
    # imponer M_{-m,-n}=M_{mn}
    for i in range(dim):
        for j in range(dim):
            mi, mj = idx[i], idx[j]
            a, b = idx.index(-mi), idx.index(-mj)
            M[a, b] = M[i, j]
    hr_signature(M, idx, "RANDOM-sim (control algebraicidad)")
    # DH
    Ld, Lpd, Ad, Ld2, idxd = get_matrices(lam, N, 'DH', dps=40)
    Adnp = np.array([[float(Ad[i, j]) for j in range(dim)] for i in range(dim)])
    hr_signature(Adnp, idxd, "DH (debe fallar)")


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E92 — Hodge-Riemann: ¿A(v,*v) definida en H^1? ¿algebraica (control) o aritmetica?")
    for lam, N in grid:
        run(lam, N)
