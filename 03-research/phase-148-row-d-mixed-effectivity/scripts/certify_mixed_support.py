#!/usr/bin/env python3
"""
R148 / D.56 -- support-function comparison at rho_1 for the MIXED effective cone.

Question decided here (numerically, as a check on the proof of Theorem D.56.6):
  is  s_1^{(M)} := sup { |Re(e^{i theta} Phi_Phi(rho_1))| / (1/2 deg Phi) :
                         Phi in D^W, exists phi,psi with Phi(v-u) >= phi(u)psi(v) all u,v }
  at theta = pi/2 strictly larger than the radial constant
        s_1 = s(gamma_1, pi/2) = sup_u |sin(gamma_1 u)| / cosh(u/2) ?

Theorem D.56.3 says NO: the tropical condition  Phi >= phi (*) psi  with
(phi (*) psi)(w) := sup_u phi(u)psi(u+w) >= 0 forces Phi >= 0, so the mixed
shadow is exactly the frame's effective cone E and s_1^{(M)} = s_1.

This script prints the margins for that identity:
  (a) s_1 and u* to 40 digits;
  (b) for a family of mixed effective classes k = k_Phi - phi(x)psi(y) >= 0
      the ratio r(Phi) = |Im Phi_Phi(rho_1)| / (1/2 deg Phi) and the margin
      s_1 - r(Phi) (must be >= 0);
  (c) the approach to s_1 from below by narrowing bumps at u*, with and
      without a rank-one part -- both approach s_1, neither exceeds it.

Usage:  python3 certify_mixed_support.py [--fast]
"""
import sys
from mpmath import mp, mpf, sin, cos, cosh, sinh, exp, quad, findroot, sqrt, pi, inf

FAST = "--fast" in sys.argv
mp.dps = 25 if FAST else 40

GAMMA1 = mpf("14.134725141734693790457251983562470270784257115699")

def s_of(gamma, theta):
    """sup_u |cos(gamma u + theta)| / cosh(u/2), by scan + Newton.

    The scan below covers only |u| <= 1.6.  That is RIGOROUS, by the a-priori
    enclosure  |cos(gamma u + theta)| / cosh(u/2) <= 1 / cosh(0.8) = 0.747699...
    valid for every |u| > 1.6 -- the same device Paper 46 Prop. 19.18 uses at
    |u| >= 0.2.  Since 1/cosh(0.8) < s_1, no supremum can hide outside the
    window.  The enclosure is asserted below (R-7 of R148_002), not left to the
    reader.
    """
    f = lambda u: abs(cos(gamma*u + theta)) / cosh(u/2)
    best, bu = mpf(0), mpf(0)
    N = 4000 if FAST else 20000
    for i in range(-N, N+1):
        u = mpf(i)*mpf("0.4")/N * 4        # scan |u| <= 1.6
        v = f(u)
        if v > best:
            best, bu = v, u
    # Newton on the critical equation g'(u) = 0 for the smooth branch
    g = lambda u: cos(gamma*u+theta)/cosh(u/2)
    dg = lambda u: (-gamma*sin(gamma*u+theta)*cosh(u/2)
                    - mpf(1)/2*cos(gamma*u+theta)*sinh(u/2))/cosh(u/2)**2
    try:
        u0 = findroot(dg, bu)
        if abs(g(u0)) > best:
            best, bu = abs(g(u0)), u0
    except Exception:
        pass
    return best, bu

# ---------------------------------------------------------------- (a)
s1, ustar = s_of(GAMMA1, pi/2)
TAIL = 1/cosh(mpf("0.8"))          # bound on the quotient for |u| > 1.6
assert TAIL < s1, (TAIL, s1)       # R-7: the scan window |u| <= 1.6 is rigorous
print("=== (a) the radial constant at rho_1, theta = pi/2 ===")
print("gamma_1 =", GAMMA1)
print("s_1     =", s1)
print("u*      =", ustar)
print("1 - s_1 =", 1 - s1, "   (the frame defect margin, Paper 46 Thm 19.22)")
print("1 - s_1^2 =", 1 - s1**2, "   d_0 = 1/(1-s_1^2) =", 1/(1-s1**2))
print("tail enclosure for |u| > 1.6 : 1/cosh(0.8) =", mp.nstr(TAIL, 12),
      "  <  s_1   (scan window justified)")
print("  [CERTIFIED: part (a) only.  Parts (b)-(e) below sample only Phi >= 0,")
print("   which Lemma 19.17 bounds by s_1 A PRIORI, so their margins cannot be")
print("   negative whatever the grid does: they are consistency checks on the")
print("   code, not evidence for Theorem D.56.6.  See R148_003 section R8.]")
print()

# ---------------------------------------------------------------- helpers
LIM = mpf(30)
def _nodes(extra):
    """quadrature nodes: the ends, 0, and a tight nest around each hot point."""
    pts = {-LIM, mpf(0), LIM}
    for x in extra:
        for h in (mpf(0), mpf("0.005"), mpf("0.05"), mpf("0.5"), mpf(2)):
            for sgn in (1, -1):
                y = x + sgn*h
                if -LIM < y < LIM:
                    pts.add(y)
    return sorted(pts)

def ratio(Phi, hot=()):
    """|Im Phi_Phi(rho_1)| / (1/2 deg Phi)   for a nonnegative Phi."""
    nd = _nodes(list(hot) + [ustar])
    num = quad(lambda u: Phi(u)*sin(GAMMA1*u), nd)
    den = quad(lambda u: Phi(u)*2*cosh(u/2),   nd)
    return abs(num)/(den/2), den

def tropical(phi, psi, w):
    """(phi (*) psi)(w) = sup_u phi(u) psi(u+w), by scan."""
    best = mpf("-inf")
    N = 400 if FAST else 2000
    for i in range(-N, N+1):
        u = mpf(i)*mpf(8)/N
        v = phi(u)*psi(u+w)
        if v > best:
            best = v
    return best

# ---------------------------------------------------------------- (b)
print("=== (b) CONSISTENCY PRINT (not a certificate): mixed effective classes k = k_Phi - phi(x)psi(y) >= 0 ===")
print("    Phi := (phi (*) psi) + t * B_delta(. - u*)   (admissible by construction)")
print("    B_delta a nonnegative bump at u*, t >= 0.  Ratio must stay <= s_1.")
print()
print("  %-6s %-6s %-6s  %-26s %-14s" % ("L", "c", "t", "ratio r(Phi)", "s_1 - r"))
worst = mpf("-inf")
for L in [mpf("0.5"), mpf(1), mpf(2)]:
    for c in [mpf(0), mpf(1)]:
        phi = lambda u, L=L: exp(-u**2/(2*L**2))
        psi = lambda u, L=L, c=c: exp(-(u-c)**2/(2*L**2))
        # closed form for these Gaussians: (phi(*)psi)(w) = exp(-(w-c)^2/(4L^2))
        trop = lambda w, L=L, c=c: exp(-(w-c)**2/(4*L**2))
        # spot-check the closed form against the scan
        chk = abs(trop(mpf("0.3")) - tropical(phi, psi, mpf("0.3")))
        assert chk < mpf("1e-3"), chk   # grid-resolution tolerance on the sup-scan
        for t in [mpf(0), mpf(1), mpf(10), mpf(100)]:
            delta = mpf("0.02")
            bump = lambda u, d=delta: exp(-(u-ustar)**2/(2*d**2))
            Phi = lambda u, t=t, tr=trop, b=bump: tr(u) + t*b(u)
            r, dg = ratio(Phi, hot=[c, mpf(0)])
            worst = max(worst, r)
            print("  %-6s %-6s %-6s  %-26s %-14s" %
                  (mp.nstr(L,3), mp.nstr(c,3), mp.nstr(t,4),
                   mp.nstr(r, 12), mp.nstr(s1 - r, 6)))
print()
print("  worst ratio over the family :", mp.nstr(worst, 15))
print("  s_1                          :", mp.nstr(s1, 15))
print("  margin s_1 - worst           :", mp.nstr(s1 - worst, 8),
      " (>= 0  <=>  NO improvement)")
print()

# ---------------------------------------------------------------- (c)
print("=== (c) CONSISTENCY PRINT: approach to s_1 from below, purely radial bumps at u* ===")
print("  %-10s %-26s %-16s" % ("delta", "ratio", "s_1 - ratio"))
for d in [mpf("0.2"), mpf("0.05"), mpf("0.01"), mpf("0.002")]:
    Phi = lambda u, d=d: exp(-(u-ustar)**2/(2*d**2))
    r, _ = ratio(Phi)
    print("  %-10s %-26s %-16s" % (mp.nstr(d,3), mp.nstr(r,15), mp.nstr(s1-r,8)))
print()
print("=== (d) CONSISTENCY PRINT: MIXED classes attain s_1 from below and never exceed it ===")
print("    Phi = (phi (*) psi) + t B_delta(.-u*),  L=1, c=1, delta=0.002")
print("  %-10s %-26s %-16s" % ("t", "ratio", "s_1 - ratio"))
trop1 = lambda w: exp(-(w-mpf(1))**2/4)
for t in [mpf(10)**k for k in (2,4,6,8)]:
    d = mpf("0.002")
    Phi = lambda u, t=t, d=d: trop1(u) + t*exp(-(u-ustar)**2/(2*d**2))
    r, _ = ratio(Phi, hot=[mpf(1), mpf(0)])
    print("  %-10s %-26s %-16s" % (mp.nstr(t,3), mp.nstr(r,15), mp.nstr(s1-r,8)))
print()
print("=== (e) CONSISTENCY PRINT: the two normalisations (Thm D.55.8') ===")
print("    B(A_L(phi@psi), k_Phi) = int Phi.chi is CONSTANT in L (T_a-invariance);")
print("    the 2L below is the rescaling that makes the pointwise limit land on")
print("    k_chi.  The divergence is inserted by that normalisation, not found:")
print("    the normalisation making (R) -> (T) pointwise is not the one under")
print("    which B converges.  Printing 2L * const is multiplication.")
phi1 = lambda u: exp(-u**2/2); psi1 = lambda u: exp(-(u-1)**2/2)
chi  = lambda w: sqrt(pi)*exp(-(w-mpf(1))**2/4)          # = (phi1^vee * psi1)(w)
PhiT = lambda u: exp(-(u-ustar)**2/(2*mpf("0.25")**2))   # a fixed (T) test
IP = quad(lambda w: PhiT(w)*chi(w), _nodes([mpf(1), ustar]))
print("  int Phi.chi =", mp.nstr(IP, 12))
for L in [mpf(10)**k for k in (1,2,3,4)]:
    print("    L = %-8s  2L * int Phi.chi = %s" % (mp.nstr(L,3), mp.nstr(2*L*IP, 12)))
print()
print("DECISION (D.56): outcome (i) -- the support-function constant at rho_1 is")
print("UNCHANGED at s_1 = %s ; no FATAL flag." % mp.nstr(s1, 20))
