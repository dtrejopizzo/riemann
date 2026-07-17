"""
E93 — QUATERNIONIC Hodge-Riemann certificate (Phase 62, MW-5 / positivity lever).

Fixes E92: E92 used Sigma e_n = i sgn(n) e_{-n}, which on H^1 (n!=0) is an INVOLUTION
(Sigma^2 = +1, a REAL structure) — and gave an indefinite form for zeta. Deninger
(2204.02714, via E48/E50) says the object that forces RH is QUATERNIONIC: a complex
structure J with J^2 = -1, with the symplectic/alternating companion of A being the
J-compatible piece. The REAL symmetric A is "the wrong shadow" (E48: [A,P]=0, P^2=+1).

Correct structure: J e_n = sgn(n) e_{-n} (real), so J^2 e_n = sgn(n) sgn(-n) e_n = -e_n.
Polarization / Hodge-Riemann (weight-1 polarized HS): the Weil form is
    omega(v,w) = v^T A J w.
HR 2nd bilinear relation => omega is DEFINITE on H^1 iff (A, J) is a polarization
(<=> the functional equation Omega and the complex structure J are compatible = Weil positivity).

NON-CIRCULARITY GATE (the whole point):
  - ZETA: is omega definite on H^1?
  - RANDOM-sym control with the SAME parity symmetry A_{-m,-n}=A_{mn}: if it is ALSO
    definite => positivity is ALGEBRAIC (a property of J + the symmetry), structural,
    NON-circular => this CROSSES the wall.  If random is INDEFINITE but zeta is definite
    => positivity is ARITHMETIC = RH in disguise = circular (does NOT cross).
  - DH falsador (off-line zeros): must be INDEFINITE.

Honesty: dps>=40; DH mandatory; report signatures verbatim; a definite zeta alone proves
nothing unless the random control resolves the circular/algebraic question. No proof claimed.
"""
import os, sys, numpy as np, mpmath as mp
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices

mp.mp.dps = 40


def Jmat(idx):
    """real quaternionic complex structure: J e_n = sgn(n) e_{-n}, J^2 = -1 on n!=0."""
    dim = len(idx); J = np.zeros((dim, dim))
    for a, n in enumerate(idx):
        if n != 0:
            J[idx.index(-n), a] = 1.0 if n > 0 else -1.0
    return J


def hr_signature(Anp, idx, label):
    J = Jmat(idx)
    W = Anp @ J                      # Weil/HR form omega(v,w)=v^T A J w
    Wsym = (W + W.T) / 2             # symmetric part (the quadratic form)
    Wasym = np.max(np.abs((W - W.T) / 2))
    z = idx.index(0)
    keep = [i for i in range(len(idx)) if i != z]   # H^1 = n!=0
    Hp = Wsym[np.ix_(keep, keep)]
    ev = np.linalg.eigvalsh(Hp)
    npos = int((ev > 1e-9).sum()); nneg = int((ev < -1e-9).sum()); nz = len(ev) - npos - nneg
    definite = (npos == 0 or nneg == 0)
    print(f"  [{label}] sig H^1 (pos,0,neg)=({npos},{nz},{nneg})  ev=[{ev.min():+.3e},{ev.max():+.3e}]"
          f"  asym|AJ|={Wasym:.2e}  => {'DEFINITE' if definite else 'indefinite'}")
    return definite, npos, nz, nneg


def parity_random(idx, seed=0):
    """random symmetric matrix with the SAME parity symmetry M_{-m,-n}=M_{mn} as A."""
    rng = np.random.default_rng(seed); dim = len(idx)
    M = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(i, dim):
            v = rng.standard_normal(); M[i, j] = v; M[j, i] = v
    for i in range(dim):
        for j in range(dim):
            a, b = idx.index(-idx[i]), idx.index(-idx[j])
            M[a, b] = M[i, j]
    return M


def run(lam, N):
    La, Lp, A, L, idx = get_matrices(lam, N, 'zeta', dps=40)
    dim = len(idx)
    Anp = np.array([[float(A[i, j]) for j in range(dim)] for i in range(dim)])
    print(f"\nlam={lam} N={N} dim={dim}")
    hr_signature(Anp, idx, "ZETA          ")
    # non-circularity control: random-sym with same parity symmetry (avg over seeds)
    defs = []
    for s in range(5):
        d, *_ = hr_signature(parity_random(idx, s), idx, f"RANDOM-sym s={s} ")
        defs.append(d)
    print(f"    -> random definite in {sum(defs)}/5 seeds "
          f"({'ALGEBRAIC/non-circular if high' if sum(defs)>=4 else 'ARITHMETIC/circular if 0'})")
    Ld, Lpd, Ad, Ld2, idxd = get_matrices(lam, N, 'DH', dps=40)
    Adnp = np.array([[float(Ad[i, j]) for j in range(dim)] for i in range(dim)])
    hr_signature(Adnp, idxd, "DH (must fail) ")


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E93 — Quaternionic (J^2=-1) Hodge-Riemann: is v^T A J v definite? algebraic or arithmetic?")
    for lam, N in grid:
        run(lam, N)
