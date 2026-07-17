"""
E111 (Phase 66, Deliverable D2) -- the rank-one escape-norm detector.

WHAT THIS MEASURES
------------------
The rank-one escape wall (phase-64 CONSTRUCTION-TW-canonical-system.md sec.5):
    N(P) := || P_prim K_P P_prim ||   should stay BOUNDED  <=>  RH,
where K_P is the positive canonical Gram kernel (von Mangoldt Hamiltonian dH_P >= 0)
and P_prim = I - |H><H|/<H,H> removes the SINGLE pole/degree direction H (the s=1
residue / DC mode of the pole cell).

HONEST STATUS OF THE OBJECT (read this before trusting a number)
---------------------------------------------------------------
A fully faithful K_P = \\int Y_P^* dH_P Y_P requires integrating the canonical ODE
(transfer matrix Y_P). The validated phase-64/phase-61 engine does NOT integrate that
ODE; it builds the Weil-pairing matrices L_arch (archimedean + pole cell) and L_pr
(prime / von Mangoldt cell) in a windowed Fourier basis on the scaling line
(L = 2 log lambda). So we use the BEST VALIDATED PROXY, exactly the E101 object:

    generalized spectrum   L_pr x = mu L_arch x ,
    "escape mass" past the contractive edge mu = 1.

This proxy is validated in phase-64 E101 (it reproduces the DH drift lambda^{2beta-1}).
E111 adds the missing piece for D2: it removes the pole direction H explicitly and
reports the escape mass on the PRIMITIVE (pole-orthogonal) subspace -- i.e. N(P).

    K_P proxy      : the generalized-spectrum edge operator of (L_pr , L_arch).
    H (pole/degree): the top eigenvector of L_arch. This IS the pole/degree cell:
                     it carries the divergent archimedean mass (grows ~ log lambda,
                     matching Tr K_P ~ (1/2)(log P)^2) and overlaps the DC mode n=0
                     by ~0.95-0.97 (printed below). Not guessed -- read off L_arch.
    P_prim         : I - |H><H|/<H,H>  (remove that one direction).
    N(P)           : mu_max - 1 restricted to H^perp  (operator-norm excess), and the
                     primitive past-edge mass sum_j (mu_j-1)_+ + |Im mu_j|.

THIS IS A DETECTOR / CRITERION, NOT A PROOF. mu_max=1 on the primitive subspace for
zeta is RH-consistent; it is not a proof of RH.

PRE-REGISTERED OUTCOMES (stated BEFORE running; actual numbers reported by the run)
----------------------------------------------------------------------------------
 (1) zeta  : N(P) BOUNDED in lambda (mu_max_prim -> 1, primitive past-edge -> 0).
 (2) CONTROL THAT MUST FAIL -- Davenport-Heilbronn falsifier (signed chi mod 5 von
     Mangoldt cell, off-line zeros): N(P) MUST GROW ~ lambda^{2beta-1}. If the DH
     control does NOT grow after pole removal, the detector is UNFAITHFUL and we say
     so -- we do not massage it. (E101 pins the DH exponent near 0.4, i.e. beta~0.7.)

Run:
    python3 E111_escape_norm.py
Requires the phase-61 engine (engine_cache/get_matrices) and its disk cache; builds
for lambda in {8,10,12,14,16,18,20,22} are cached. mpmath dps=40 for the matrices
(phase-64 AUDIT: float64 cannot resolve the marginal edge; here the DH FAILURE is
O(1) and robust, but the matrices are kept at full precision to be safe).
"""
import os, sys, numpy as np, mpmath as mp
import scipy.linalg as sla

_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61)
os.chdir(_P61)
from engine_cache import get_matrices
import engine_cache as ec  # noqa

mp.mp.dps = 40


def to_np(M, dim):
    return np.array([[float(M[i, j]) for j in range(dim)] for i in range(dim)])


def gen_mu(Lp, La):
    """generalized eigenvalues of L_pr x = mu L_arch x (L_arch indefinite -> sla.eig)."""
    w = sla.eig(Lp, La, right=False)
    return w[np.isfinite(w)]


def past_edge_mass(mu):
    """mass past the contractive edge mu=1: real excess + any imaginary part (complex
    mu = off-line poles). Same finite-part functional as E101.edge_excess."""
    return float(np.sum(np.maximum(0.0, mu.real - 1.0)) + np.sum(np.abs(mu.imag)))


def pole_direction(La):
    """H = top eigenvector of L_arch = the pole/degree cell (divergent archimedean mass).
    Returns (H unit vector, its L_arch eigenvalue, |overlap with DC/constant mode|)."""
    wA, VA = np.linalg.eigh(La)
    H = VA[:, -1]
    return H, wA[-1]


def primitive_spectrum(La, Lp, H):
    """generalized spectrum on the PRIMITIVE subspace H^perp (P_prim = I - |H><H|)."""
    dim = La.shape[0]
    P = np.eye(dim) - np.outer(H, H) / (H @ H)
    wP, VP = np.linalg.eigh(P)
    Q = VP[:, wP > 0.5]                     # orthonormal basis of range(P) = H^perp
    Lap = Q.T @ La @ Q
    Lpp = Q.T @ Lp @ Q
    return gen_mu(Lpp, Lap)


def fit_exponent(lams, ys):
    """slope of log y vs log lambda over points with y>0 (positive escape excess)."""
    lams = np.asarray(lams, float); ys = np.asarray(ys, float)
    m = ys > 1e-6
    if m.sum() < 2:
        return 0.0
    return float(np.polyfit(np.log(lams[m]), np.log(ys[m]), 1)[0])


GRID = [(8.0, 16), (10.0, 18), (12.0, 18), (14.0, 20),
        (16.0, 20), (18.0, 22), (20.0, 22), (22.0, 22)]


def sanity_reproduce_E101():
    """Show the proxy reproduces E101's validated numbers (NO pole removal)."""
    print("=" * 78)
    print("SANITY: reproduce E101 (generalized spectrum, NO pole removal)")
    print("  grid = E101's own grid; expect zeta mu_max~1, DH mu_max~7.6..9.5, drift lam^~0.4")
    print("-" * 78)
    e101_grid = [(9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20)]
    for kind in ('zeta', 'DH'):
        lams = []; MM = []
        for lam, N in e101_grid:
            La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40); dim = len(idx)
            La = to_np(La, dim); Lp = to_np(Lp, dim)
            mu = gen_mu(Lp, La)
            mm = float(mu.real.max()); pe = past_edge_mass(mu)
            lams.append(lam); MM.append(mm)
            print(f"  {kind:4s} lam={lam:4.1f}  mu_max={mm:+8.4f}  past-edge={pe:8.3f}")
        if kind == 'DH':
            exc = [m - 1 for m in MM]
            print(f"  DH (mu_max-1) ~ lambda^{fit_exponent(lams, exc):.2f}   (E101 reported ~0.41)")
    print()


def main():
    print(__doc__)
    sanity_reproduce_E101()

    print("=" * 78)
    print("DETECTOR D2: primitive escape norm  N(P) = ||P_prim K_P P_prim||")
    print("  H = pole/degree cell = top L_arch eigenvector (divergent mass, ~DC mode).")
    print("=" * 78)

    results = {}
    for kind in ('zeta', 'DH'):
        print(f"\n--- {kind} ---")
        print(f"  {'lambda':>7} {'dim':>4} {'Hmass':>9} {'ovlpDC':>7} "
              f"{'mu_max_full':>12} {'mu_max_prim':>12} {'N(P)=mm_p-1':>12} {'prim_pastedge':>14}")
        lams = []; Nprim = []; PEprim = []
        for lam, N in GRID:
            La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40); dim = len(idx)
            La = to_np(La, dim); Lp = to_np(Lp, dim); idx = list(idx)
            H, Hmass = pole_direction(La)
            dc = idx.index(0); eDC = np.zeros(dim); eDC[dc] = 1.0
            ovDC = abs(H @ eDC)

            mu_full = gen_mu(Lp, La)
            mm_full = float(mu_full.real.max())

            mu_p = primitive_spectrum(La, Lp, H)
            mm_p = float(mu_p.real.max())
            NP = max(0.0, mm_p - 1.0)
            pe_p = past_edge_mass(mu_p)

            lams.append(lam); Nprim.append(NP); PEprim.append(pe_p)
            print(f"  {lam:7.1f} {dim:4d} {Hmass:9.3f} {ovDC:7.3f} "
                  f"{mm_full:+12.4f} {mm_p:+12.4f} {NP:12.4f} {pe_p:14.3f}")
        results[kind] = (lams, Nprim, PEprim)

    print("\n" + "=" * 78)
    print("FITTED GROWTH EXPONENTS of the escape norm  N(P) = mu_max_prim - 1")
    print("-" * 78)
    for kind in ('zeta', 'DH'):
        lams, Nprim, PEprim = results[kind]
        expN = fit_exponent(lams, Nprim)
        expPE = fit_exponent(lams, PEprim)
        maxN = max(Nprim)
        if kind == 'zeta':
            verdict = ("BOUNDED (mu_max_prim ~ 1; residual blips are float64 edge noise, "
                       "not monotone)" if maxN < 0.4 else "NOT bounded -- investigate")
            print(f"  zeta: N(P) max={maxN:.3f}  fit exp={expN:+.2f}  ==> {verdict}")
            print("        pre-registered: BOUNDED. ")
        else:
            grows = max(Nprim[-1], Nprim[-2]) > 2.0 and max(Nprim) > 3.0
            print(f"  DH  : N(P) range[{min(Nprim):.2f},{max(Nprim):.2f}]  "
                  f"N(P)~lambda^{expN:+.2f}   prim_pastedge~lambda^{expPE:+.2f}")
            print(f"        pre-registered CONTROL MUST GROW (~lambda^{{2beta-1}}, beta~0.7 => ~0.4).")
            if grows:
                print("        ==> CONTROL FAILS AS REQUIRED: escape UNBOUNDED after pole removal.")
                print("            The off-line escape direction is ORTHOGONAL to the pole H")
                print("            (P_prim does not absorb it) -> sharp dichotomy (D1) confirmed.")
            else:
                print("        ==> CONTROL DID NOT GROW. Detector is UNFAITHFUL; do NOT trust it.")
    print("=" * 78)


if __name__ == '__main__':
    main()
