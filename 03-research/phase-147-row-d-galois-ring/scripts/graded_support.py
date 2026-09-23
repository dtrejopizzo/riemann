#!/usr/bin/env python3
"""R147 Part B -- support functions on the chi-graded carrier.
   (Round 3 / confirmation C6: this docstring is the file of record and is aligned
    with R147_003b_BUILDER_ROUND3.md.  Round 2's per-chi form and its "may choose
    theta" clearing argument are WITHDRAWN and no longer appear here.)

Carrier (Def. D.55.1', round 3): D_L := (+)_{chi in Ghat} (D^W (x) C) with the real
structure conj(E_chi) = E_chibar, for an ABELIAN L/F with G = Gal(L/F);
Gamma_sigma acts on the chi-slot by chi(sigma), a root of unity of order
m = ord(chi).  The form is PACKET-PAIRED, as phase 139 Thm D.20.2 requires (its
finding H5) -- the chi-slot is paired with the chibar-slot:

    I^{(K)}(E,F) = sum_chi I^{[chi]}(E_chi, F_chibar),
    I^{[chi]}(A,B) = - sum_{rho in Z(Lambda(.,chi))} Phi_A(rho) Phi_B(1-rho)
                     ( + the polar block, for chi = 1 ),

which is bilinear, SYMMETRIC and REAL on the real structure (1-rho lies in
Z(Lambda(.,chibar)), NOT in Z(Lambda(.,chi)) -- which is exactly what the per-chi
form of round 2 got wrong), and for which

    I^{(K)}(Gamma_sigma E, Gamma_tau F) = sum_chi chi(sigma tau^{-1}) I^{[chi]}(E_chi,F_chibar)

falls out of bilinearity with NO adjoint smuggled in (Thm D.55.4').

The effective cone (Def. D.55.5', candidate (ii)) is the isotypic image of the
nonnegative COMPACTLY SUPPORTED SMOOTH tests on the projected model R x G of
C_{F,S}:
    f >= 0, f in C_c^inf(R x G)  |-->  (f_chi)_chi ,  f_chi(u) = sum_g chi(g) f(u,g)
(so f_chi lies in D^W (x) C: NO point masses -- hostile MAJOR 3).  Its support
function is computed in two halves (Lemma D.31.4 per coset for '<=', concentration
of f on one coset near the optimal u for '>='), Thm D.55.6':
    S(gamma,theta,m) = max_{0<=k<m} s(gamma, theta - 2 pi k/m),
    s(gamma,theta)   = sup_u |cos(gamma u + theta)|/cosh(u/2)     (Def D.31.3).

Computed here:
  [1] the CORRECTED cos(pi/m) lemma (Lemma A.6): u = 0 entry alone,
      L(m) = min_theta max_k |cos(theta + 2 pi k/m)| = cos(pi/m) for m even >= 4,
      cos(pi/2m) for m odd >= 3, 0 for m <= 2; argmin d/2;
  [2] S(gamma_1, pi/2, m): the direction in which Thm 19.23's witness F_0 is built
      -- equals 1 exactly when 4 | m.  This is NOT a new value: s(gamma,0) = 1 for
      every gamma and max_theta s = 1 is Paper 46 (19.2); for 4|m the mu_m-orbit of
      pi/2 meets pi Z (Thm D.55.7'(i));
  [3] sigma(gamma,m) = min_theta S(gamma,theta,m) -- the constant that a
      theta-ADJUSTABLE defect theorem WOULD use.  No such theorem is stated for
      L(s,chi), and Paper 46's witness F_0 is ODD and tied to theta = pi/2; see
      O-47.7.  sigma < 1 for every finite m (analytic, via Prop 19.18);
  [4] d_0 = (1-sigma^2)^{-1}: a LOWER bound (a grid underestimates a sup), for the
      hypothetical theorem of [3].  The certified m = 1 value is the corpus's
      s_1 = 0.99846016271880910923..., d_0 = 324.9598266...

Theorem D.55.9' (the phase's result) is NOT computed here: it is exact -- the
chi = 1 slot of the cone is exactly E^inf, since f_1 = sum_g f(.,g) >= 0, so the
support function there is S(gamma,theta,1) = s(gamma,theta), unchanged.

W-a: support functions of convex cones only.  NOTHING here asserts the sign of
I^{[chi]} or of any trace form; a statement "I^{[chi]} <= 0 on the chi-effective
cone" would be GRH for L(s,chi) and is never made.
"""
import sys, math
import numpy as np

FAST  = "--fast" in sys.argv
UMAX  = 8.0
NU    = 40001 if FAST else 160001          # u-grid
NTH   = 2520  if FAST else 5040            # theta-grid on [0,pi); 2*NTH divisible by every m used
MS    = (1,2,3,4,5,6,8,12)
GAMMA1 = 14.134725141734693790             # (X19)

u  = np.linspace(-UMAX, UMAX, NU)
ch = np.cosh(u/2.0)

def s_grid(gamma):
    """s(gamma, theta) on the uniform theta-grid of NTH points over [0,pi)."""
    A = np.cos(gamma*u)/ch
    B = np.sin(gamma*u)/ch
    th = np.pi*np.arange(NTH)/NTH
    out = np.empty(NTH)
    for j in range(NTH):
        out[j] = np.max(np.abs(A*math.cos(th[j]) - B*math.sin(th[j])))
    return th, out

def S_grid(sv, m):
    """S(gamma,theta,m) = max_k s(gamma, theta - 2 pi k/m) on the same grid.
       s is pi-periodic in theta, so 2 pi k/m is the index shift 2*NTH*k/m."""
    assert (2*NTH) % m == 0, (NTH, m)
    sh = (2*NTH)//m
    out = sv.copy()
    for k in range(1, m):
        out = np.maximum(out, np.roll(sv, (k*sh) % NTH))
    return out

print("=== [1] corrected cos(pi/m) lemma  (hostile MAJOR 6; the u = 0 entry alone)")
print("    L(m) := min_theta max_{0<=k<m} |cos(theta + 2 pi k/m)|")
print(f"{'m':>3s} {'L(m) numeric':>14s} {'argmin theta':>13s} {'closed form':>13s} {'name':>12s} {'argmin*':>10s} {'margin':>9s}")
TH = np.pi*np.arange(NTH)/NTH
for m in range(1, 13):
    vals = np.max(np.abs(np.cos(TH[:,None] + 2*np.pi*np.arange(m)[None,:]/m)), axis=1)
    j = int(np.argmin(vals)); best, bt = float(vals[j]), float(TH[j])
    if m <= 2:   cf, nm, ths = 0.0, "0", math.pi/2
    elif m % 2 == 0: cf, nm, ths = math.cos(math.pi/m), "cos(pi/m)", math.pi/m
    else:        cf, nm, ths = math.cos(math.pi/(2*m)), "cos(pi/2m)", math.pi/(2*m)
    print(f"{m:3d} {best:14.9f} {bt:13.9f} {cf:13.9f} {nm:>12s} {ths:10.6f} {abs(best-cf):9.2e}")

print()
print("=== [2] FIXED direction theta = pi/2 (the witness direction of Thm D.31.10 / 19.23)")
th, sv = s_grid(GAMMA1)
j_half = NTH//2
print(f"    s(gamma_1, pi/2) = {sv[j_half]:.9f}   (corpus s_1 = 0.99846016; margin "
      f"{abs(sv[j_half]-0.998460157):.2e})")
print(f"{'m':>3s} {'S(gamma1,pi/2,m)':>18s}   reaches 1?")
for m in MS:
    Sg = S_grid(sv, m)
    print(f"{m:3d} {Sg[j_half]:18.9f}   " + ("YES  (4 | m)" if m % 4 == 0 else "no"))

print()
print("=== [3] sigma(gamma,m) = min_theta S(gamma,theta,m)")
print("    sigma is a LOWER bound (grid underestimates a sup); so is d_0.  Exact argmin = d/2.")
print(f"{'gamma':>10s} {'m':>3s} {'sigma >=':>13s} {'grid th*':>10s} {'exact d/2':>10s} {'1-sigma':>11s} {'d_0 >=':>12s}")
gammas = (GAMMA1, 6.0, 2.5) if not FAST else (GAMMA1, 6.0)
for gamma in gammas:
    th, sv = s_grid(gamma)
    for m in MS:
        Sg = S_grid(sv, m)
        j = int(np.argmin(Sg)); best, bt = float(Sg[j]), float(th[j])
        d0 = 1.0/(1.0-best*best) if best < 1 else float('inf')
        d = (2*math.pi/m) if (m % 2 == 0) else (math.pi/m)     # exact argmin is d/2
        print(f"{gamma:10.5f} {m:3d} {best:13.9f} {bt:10.6f} {d/2:10.6f} {1-best:11.3e} {d0:12.1f}")

print()
print("=== [4] verdict   (round 3 framing)")
print("  * The chi = 1 SLOT of the cone is exactly E^inf (f_1 = sum_g f(.,g) >= 0), so")
print("    its support function is S(gamma,theta,1) = s(gamma,theta): UNCHANGED.  This is")
print("    Thm D.55.9', and it is exact -- no 'unique chi_rho' is used or needed.")
print("  * S(gamma,pi/2,m) = 1 exactly when 4 | m: the mu_m-orbit of pi/2 meets pi Z,")
print("    where s(gamma,0) = 1 ALREADY (Paper 46 (19.2) / Prop 19.18).  No support")
print("    function reaches a value it did not already have.")
print("  * sigma(gamma,m) < 1 for every finite m (analytic, via Prop 19.18).  The")
print("    thresholds d_0 below are LOWER BOUNDS (a grid underestimates a sup), and")
print("    they belong to a theorem that has NOT been stated for L(s,chi) and whose")
print("    witness F_0 is odd and tied to theta = pi/2.  See O-47.7.")
