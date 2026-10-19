"""
Camino 2, step 2: explicit-formula coupling probe (Phase 18).

Question (from 01-...-portrait.md sec 3): a single off-line quartet at gamma_0 gives a
SHALLOW (O(b^2)) negative direction localized at frequency gamma_0 (P1-P3). But the zeros
are NOT free: they belong to one entire function xi. Near gamma_0 there are ON-LINE zeros
(at spacing Delta), each contributing a POSITIVE term at nearby frequencies. Does that
neighbourhood PROTECT against the dent?

  Case A: the dent can be isolated -> on-line neighbours do NOT protect (null, informative).
  Case B: the neighbours protect locally -> there is a threshold b*(Delta) below which the
          embedded bottom eigenvalue stays >= 0; off-line displacement must beat the spacing.
  Case C: protection is collective, not local (would show up as Delta-scaling of b*).

Construction (bilinear Weil-Gram in an orthonormal even Hermite basis):
  on-line zero gamma   -> block 2 * uu^T,  u_k = <psi_k, cos(gamma t)>      (PSD)
  off-line quartet     -> block 4*(UU^T - VV^T),  U_k=<psi_k,cosh(bt)cos(gamma t)>,
                          V_k=<psi_k,sinh(bt)sin(gamma t)>                  (signature (1,1))
We compare lambda_min of: ISOLATED (quartet only) vs EMBEDDED (quartet + on-line neighbours),
as functions of b and the neighbour spacing Delta.
"""
import numpy as np
np.seterr(all="ignore")

L, NPTS, NMAX = 26.0, 4500, 180
u = np.linspace(-L, L, NPTS); du = u[1]-u[0]
psi = np.zeros((NMAX+1, NPTS))
psi[0] = np.pi**-0.25*np.exp(-u**2/2)
psi[1] = np.sqrt(2.0)*u*np.pi**-0.25*np.exp(-u**2/2)
for n in range(1, NMAX):
    psi[n+1] = np.sqrt(2.0/(n+1))*u*psi[n] - np.sqrt(n/(n+1))*psi[n-1]
B = psi[np.arange(0, NMAX+1, 2)]                  # orthonormal even Hermite functions

def hatU(b, g): return (B @ (np.cosh(b*u)*np.cos(g*u)))*du
def hatV(b, g): return (B @ (np.sinh(b*u)*np.sin(g*u)))*du
def online(g):
    uu = hatU(0.0, g); return 2.0*np.outer(uu, uu)            # PSD
def offline(b, g):
    U, V = hatU(b, g), hatV(b, g); return 4.0*(np.outer(U, U) - np.outer(V, V))
def lam_min(M): return float(np.linalg.eigvalsh((M+M.T)/2).min())
def bottom_vec(M):
    w, V = np.linalg.eigh((M+M.T)/2); return w[0], V[:, 0]
def freq_profile(c):
    """peak frequency and FWHM of |f^(xi)| for the eigenvector c."""
    f = c @ B
    xis = np.linspace(0.5, 22, 1600)
    fh = np.abs((np.cos(np.outer(xis, u)) @ f)*du)
    pk = xis[np.argmax(fh)]; half = fh.max()/2
    above = xis[fh >= half]
    return pk, (above.max()-above.min() if len(above) else 0.0)

G0 = 8.0          # putative off-line ordinate
KN = 4            # number of on-line neighbours each side

print("="*74)
print("STEP 2  |  Does the on-line neighbourhood protect against the off-line dent?")
print("="*74)
print(f"   putative off-line zero at gamma_0={G0}; {KN} on-line neighbours each side at spacing Delta")

print("\n(1) ISOLATED quartet vs EMBEDDED (quartet + on-line neighbours), Delta=2.0")
Delta = 2.0
neigh = [G0 + k*Delta for k in range(-KN, KN+1) if k != 0]
print("      b      lambda_min ISOLATED   lambda_min EMBEDDED   protected?")
for b in [0.40, 0.25, 0.15, 0.08, 0.04, 0.02]:
    iso = lam_min(offline(b, G0))
    emb = lam_min(offline(b, G0) + sum(online(g) for g in neigh))
    print(f"   {b:5.2f}   {iso:18.5e}   {emb:18.5e}   {'YES (>=0)' if emb> -1e-9 else 'no (<0)'}")

print("\n(2) DIAGNOSTIC: where does the embedded negative eigenvector live, and how much do")
print("    the on-line neighbours actually lift it? (Delta=2.0)")
Delta = 2.0
neigh = [G0 + k*Delta for k in range(-KN, KN+1) if k != 0]
base = sum(online(g) for g in neigh)
print("      b     lam_iso     lam_emb    neighbour-lift   eigvec peak / FWHM")
for b in [0.25, 0.10, 0.04]:
    li = lam_min(offline(b, G0))
    le, c = bottom_vec(offline(b, G0) + base)
    lift = float(sum(2*(c @ hatU(0.0, g))**2 for g in neigh))   # <c, neighbour blocks, c>
    pk, fw = freq_profile(c)
    print(f"   {b:4.2f}  {li:10.3e}  {le:10.3e}   {lift:12.3e}    peak={pk:5.2f} FWHM={fw:4.2f}")
print(f"   (on-line zero spacing Delta={Delta}; if FWHM < Delta the packet fits BETWEEN the")
print("    on-line zeros, so the neighbour-lift is ~0 and lam_emb ~ lam_iso -> Case A.)")

print("\n(3) Threshold b*(Delta): smallest b with EMBEDDED lambda_min < 0, vs neighbour spacing")
print("      Delta    b*  (does shrinking the spacing protect?)")
for Delta in [4.0, 3.0, 2.0, 1.5, 1.0, 0.7]:
    base = sum(online(g) for g in [G0 + k*Delta for k in range(-KN, KN+1) if k != 0])
    bstar = next((b for b in np.linspace(0.005, 0.8, 160)
                  if lam_min(offline(b, G0) + base) < -1e-9), None)
    print(f"   {Delta:5.2f}    {('%.3f'%bstar) if bstar else '> 0.8 (protected in range)'}")

print("\n(4) Control: with NO off-line zero (all on-line), lambda_min should be >= 0")
allon = sum(online(g) for g in [G0 + k*2.0 for k in range(-KN, KN+1)])
print(f"   all-on-line lambda_min = {lam_min(allon):.3e}  (>=0 expected: no negative direction)")

print("\n" + "="*74)
print("READING:")
print("  * EMBEDDED lambda_min ~ ISOLATED, neighbour-lift ~ 0, eigvec FWHM < Delta")
print("    => Case A: the on-line neighbourhood does NOT protect. The negative direction is a")
print("       frequency packet NARROWER than the zero spacing; it fits between the on-line zeros")
print("       (and is orthogonal to their cos-modes), so no finite set of them lifts the dent.")
print("  * Consequence: protection, if any, is NOT local in gamma. The only coupling that could")
print("    protect is the GLOBAL one (all zeros + archimedean term + primes) = the full Weil")
print("    criterion = the standing CAP. Local arithmetic does not see the off-line dent.")
print("="*74)
