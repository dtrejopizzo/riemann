"""
Camino 2, step 1: PORTRAIT of the negative directions of the localized Weil form (Phase 18).

P25: RH false <=> there is an explicit negative direction of Q_off, supported on the
off-axis evaluation of an off-line quartet rho = 1/2 + b + i*gamma (b = beta-1/2 != 0).
The quartet form on even real test functions f is
    Q_quartet(f) = 4 ( u^2 - v^2 ),   u = <f,K_u>,  v = <f,K_v>,
    K_u = cosh(b u) cos(gamma u),  K_v = sinh(b u) sin(gamma u).
The form is RANK 2 (depends on f only through (u,v)); its single negative direction is the
combination that kills u and lives on v. We dissect that direction's properties.

Numerics: orthonormal even Hermite-function basis psi_n (L^2, G = I, stable 3-term recurrence).
The negative direction is computed analytically in span{u_vec, v_vec} (no large diagonalization).
The basis must reach frequency gamma: psi_n carries frequencies up to ~sqrt(2n), so we take n up
to ~gamma^2.  (The earlier failure was an ill-conditioned monomial basis with a too-low freq ceiling.)
"""
import numpy as np
np.seterr(all="ignore")   # high-order Hermite functions underflow to 0 at grid edges (harmless)

# ---- grid + orthonormal Hermite functions via stable recurrence ---------------------
L, NPTS, NMAX = 40.0, 7000, 560          # NMAX high enough that sqrt(2*NMAX)~33 > gamma tested
u = np.linspace(-L, L, NPTS); du = u[1]-u[0]
psi = np.zeros((NMAX+1, NPTS))
psi[0] = np.pi**-0.25 * np.exp(-u**2/2)
psi[1] = np.sqrt(2.0) * u * np.pi**-0.25 * np.exp(-u**2/2)
for n in range(1, NMAX):
    psi[n+1] = np.sqrt(2.0/(n+1))*u*psi[n] - np.sqrt(n/(n+1))*psi[n-1]
EVEN = np.arange(0, NMAX+1, 2)           # even Hermite functions (even test functions)
B = psi[EVEN]                            # (Nb, NPTS), orthonormal in L^2
# sanity: orthonormality
ortho_err = np.max(np.abs((B @ B.T)*du - np.eye(len(EVEN))))

def uv_vectors(b, gamma):
    Ku = np.cosh(b*u)*np.cos(gamma*u)
    Kv = np.sinh(b*u)*np.sin(gamma*u)
    return (B @ Ku)*du, (B @ Kv)*du       # coordinates of K_u, K_v in the orthonormal basis

def negative_direction(b, gamma):
    """rank-2 form 4(uu^T - vv^T): return (lambda_neg, coefficient vector c, u.c, v.c)."""
    uv, vv = uv_vectors(b, gamma)
    # reduced 2x2 of A = u u^T - v v^T on basis {u,v}:  [[u.u, u.v],[-u.v, -v.v]]
    uu, uvd, vvd = uv@uv, uv@vv, vv@vv
    P = np.array([[uu, uvd], [-uvd, -vvd]])
    w, V = np.linalg.eig(P)
    i = int(np.argmin(w.real))
    a, bcoef = V[:, i].real
    c = a*uv + bcoef*vv                    # coefficient vector in the orthonormal basis
    c = c/np.linalg.norm(c)
    return 4*w[i].real, c, c@uv, c@vv

print(f"(basis: {len(EVEN)} even Hermite functions, orthonormality error {ortho_err:.1e})")
print("="*72)
print("P1  |  Shallowness: along a FIXED direction, Q ~ -C b^2 (the delta^2 law)")
print("="*72)
print("   Honest caveat: the SUP of -Q over L^2 is +infinity (off-axis evaluation is unbounded")
print("   in L^2 -- the Phase-4 fact). Shallowness is a per-DIRECTION statement: fix a test")
print("   function f0 orthogonal to the on-line mode cos(gamma u), freeze it, and vary b.")
gamma = 14.134
p = (B @ np.cos(gamma*u))*du; p = p/np.linalg.norm(p)        # on-line mode coordinates
_, c_ref, _, _ = negative_direction(0.10, gamma)             # a v-rich direction at a reference b
f0 = c_ref - (c_ref @ p)*p; f0 = f0/np.linalg.norm(f0)       # remove on-line component, then FREEZE
print("\n      b         Q(f0;b)        Q/b^2")
for b in [0.08, 0.04, 0.02, 0.01, 0.005, 0.0025]:
    uv, vv = uv_vectors(b, gamma)
    Q = 4*((f0 @ uv)**2 - (f0 @ vv)**2)
    print(f"   {b:6.4f}   {Q:13.5e}   {Q/b**2:13.5e}")
print("   -> for the FIXED f0, Q(f0;b)/b^2 -> constant and Q<0: each negative direction is")
print("      SHALLOW, O(b^2), vanishing as beta->1/2 (recovers the delta^2 law, P7). The")
print("      unbounded sup is a separate (bandwidth) effect -> why a weighted space is needed.")

print("\n" + "="*72)
print("P2  |  The negative eigenvector kills u and lives on v (the sinh-sine / imaginary mode)")
print("="*72)
for b in [0.20, 0.05]:
    lam, c, uc, vc = negative_direction(b, gamma)
    print(f"   b={b:4.2f}: u(f)={uc:+.3e}  v(f)={vc:+.3e}  |u/v|={abs(uc/vc):.2e}  "
          f"-> u suppressed; the direction is the v (imaginary) mode")

print("\n" + "="*72)
print("P3  |  Frequency localization: |f^(xi)| of the negative direction peaks near gamma")
print("="*72)
xis = np.linspace(0.5, 35, 1400)
for gamma in [10.0, 14.134, 21.022, 25.011]:
    _, c, _, _ = negative_direction(0.15, gamma)
    f = c @ B
    fhat = (np.cos(np.outer(xis, u)) @ f) * du
    peak = xis[np.argmax(np.abs(fhat))]
    print(f"   gamma={gamma:7.3f}:  argmax_xi |f^(xi)| = {peak:7.3f}   "
          f"(|peak-gamma|={abs(peak-gamma):.2f}, near gamma? {abs(peak-gamma)<1.5})")

print("\n" + "="*72)
print("P4  |  Cross-quartet near-orthogonality: overlaps decay with |gamma_i - gamma_j|")
print("="*72)
gam_list = [14.134, 17.0, 21.022, 25.011, 30.0]
cs = [negative_direction(0.15, g_)[1] for g_ in gam_list]
ov = np.abs(np.array([[ci@cj for cj in cs] for ci in cs]))
np.set_printoptions(precision=2, suppress=True)
print("   |<dir_i,dir_j>| (orthonormal-basis coords; 1 on diagonal):")
print(ov)
off = ov[~np.eye(len(cs), dtype=bool)]
print(f"   nearest-neighbour gap ~3-4 in gamma; max off-diagonal overlap = {off.max():.3f}, "
      f"min = {off.min():.3f}")
print("   -> well-separated gamma give near-orthogonal directions (independent); close gamma overlap.")

print("\n" + "="*72)
print("PORTRAIT of a negative direction (what it MUST be, if RH is false):")
print("  P1 shallow:         lambda_neg = O(b^2), vanishing as beta -> 1/2;")
print("  P2 imaginary mode:  suppresses the real part u, lives on the sinh-sine part v;")
print("  P3 frequency-local: its transform concentrates near the ordinate gamma;")
print("  P4 near-orthogonal: well-separated off-line zeros give independent directions.")
print("  => the negative cone is a sum of shallow, gamma-localized, near-orthogonal lines,")
print("     one per off-line quartet. THE REAL HANDLE (next): are these directions mutually")
print("     compatible with xi being ONE entire function (Hadamard/explicit formula), or does")
print("     that coupling forbid a free collection of them?")
print("="*72)
