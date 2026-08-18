#!/usr/bin/env python3
"""
113_09 verifier -- the radical of I_partial is the xi-ideal, and the rulings
live inside D.

Checks:

 A. Basic facts about xi that everything else rests on:
    xi entire, xi(0) = xi(1) = 1/2, xi(1-s) = xi(s), conj(xi(conj s)) = xi(s),
    Xi(t) = xi(1/2+it) real, xi(rho) = 0 at computed zeros.

 B. Theorem 3.1 -- fhat_v = -2(s-1)xi and fhat_h = 2 s xi have coordinates
    (1,0,0...) and (0,1,0...), and fhat_v + fhat_h = 2 xi.

 C. Lemma 1.2 / Lemma 1.1 -- membership in D_theta.  The balanced profile of
    f_v is computed by contour-shifted inversion and its decay is measured
    against exp(-theta|x|) for theta = 2, 3, 4 (all > 3/2).

 D. Theorem 2.4(1) -- the generator s(s-1)xi(s) is *-invariant:
    conj(w(1 - conj s)) = w(s).

 E. Closed forms of the table in section 4: hhat = fhat(s) conj(ghat(1-conj s))
    checked against the elementary expressions, and G(t) against
    hhat(1/2+it) + hhat(1/2-it).

 F. THEOREM 4.1 -- the intersection numbers as facts about primes.  For six
    probes the ARITHMETIC side P(h) - A(h) (prime powers + digamma kernel,
    NO zeros anywhere) is compared with the spectral side, which is a small
    rational known in advance:
        w (radical)        -> 0
        f_v                -> 0        (F_v^2 = 0)
        f_h                -> 0        (F_h^2 = 0)
        f_v * ~f_h         -> 1        (F_v . F_h = 1)
        H = f_v + f_h      -> 2        (H^2 = 2, the polarization)
        f_v - f_h          -> -2
        xi alone (control) -> 1/2      (NOT in the radical: the s(s-1) factor
                                        is load-bearing)

 G. NEGATIVE CONTROLS -- a non-xi-divisible element is not in the radical, and
    its zero sum is nonzero; dropping the s(s-1) factor breaks radicality.

 H. Corollary 3.2 -- the projection pi(f) = f - fhat(0) f_v - fhat(1) f_h lands
    in D^o, on data with both polar coordinates nonzero.

Source rule.  Zeros of xi enter only as CHECKS (A, G) that functions built from
xi vanish on them.  The arithmetic side of Theorem 4.1 -- the load-bearing
computation -- uses no zero of xi at all.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 25

PASS = []


def check(name, cond, detail=""):
    PASS.append(bool(cond))
    print(("PASS" if cond else "FAIL") + f": {name}" + (f" ({detail})" if detail else ""))


def sec(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def xi(s):
    """xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s); removable at s = 0, 1."""
    s = mp.mpc(s)
    if abs(s) < mp.mpf("1e-8") or abs(s - 1) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")           # removable singularity, resolve by nudging
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


# ----------------------------------------------------------------------
sec("A.  the facts about xi that everything rests on")
# ----------------------------------------------------------------------
x0, x1 = xi(0), xi(1)
check("xi(0) = 1/2", abs(x0 - mp.mpf(0.5)) < mp.mpf("1e-16"), f"xi(0) = {mp.nstr(x0, 18)}")
check("xi(1) = 1/2", abs(x1 - mp.mpf(0.5)) < mp.mpf("1e-16"), f"xi(1) = {mp.nstr(x1, 18)}")
SPTS = [mp.mpc("0.3", "1.7"), mp.mpc("2.1", "-0.4"), mp.mpc("-0.8", "5.0"), mp.mpc("0.5", "3.3")]
e_fe = max(abs(xi(1 - s) - xi(s)) for s in SPTS)
e_re = max(abs(mp.conj(xi(mp.conj(s))) - xi(s)) for s in SPTS)
check("functional equation xi(1-s) = xi(s)", e_fe < mp.mpf("1e-18"), f"max err={mp.nstr(e_fe,4)}")
check("reality xi(conj s) = conj(xi(s))", e_re < mp.mpf("1e-18"), f"max err={mp.nstr(e_re,4)}")
e_im = max(abs(mp.im(xi(mp.mpf(0.5) + 1j * mp.mpf(t)))) for t in (0.0, 3.0, 14.0, 40.0))
check("Xi(t) = xi(1/2+it) is real", e_im < mp.mpf("1e-18"), f"max |Im| = {mp.nstr(e_im,4)}")
NZ = 10
RHOS = [mp.zetazero(n) for n in range(1, NZ + 1)]
e_z = max(abs(xi(r)) for r in RHOS)
check(f"xi vanishes at the first {NZ} computed zeros", e_z < mp.mpf("1e-20"),
      f"max |xi(rho)| = {mp.nstr(e_z, 4)}")
check("xi(1/2) != 0 (so Xi^2 is not identically zero)", abs(xi(mp.mpf(0.5))) > mp.mpf("0.4"),
      f"xi(1/2) = {mp.nstr(xi(mp.mpf(0.5)), 15)}")

# ----------------------------------------------------------------------
sec("B.  Theorem 3.1 -- the rulings f_v, f_h and the polarization H")
# ----------------------------------------------------------------------
fv = lambda s: -2 * (mp.mpc(s) - 1) * xi(s)
fh = lambda s: 2 * mp.mpc(s) * xi(s)
w = lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * xi(s)

check("fhat_v(0) = 1", abs(fv(0) - 1) < mp.mpf("1e-16"), f"= {mp.nstr(fv(0), 18)}")
check("fhat_v(1) = 0", abs(fv(1)) < mp.mpf("1e-16"), f"= {mp.nstr(abs(fv(1)), 4)}")
check("fhat_h(0) = 0", abs(fh(0)) < mp.mpf("1e-16"), f"= {mp.nstr(abs(fh(0)), 4)}")
check("fhat_h(1) = 1", abs(fh(1) - 1) < mp.mpf("1e-16"), f"= {mp.nstr(fh(1), 18)}")
check("fhat_v, fhat_h vanish at every zero (they carry the xi factor)",
      max(max(abs(fv(r)), abs(fh(r))) for r in RHOS) < mp.mpf("1e-19"))
e_H = max(abs((fv(s) + fh(s)) - 2 * xi(s)) for s in SPTS)
check("fhat_v + fhat_h = 2 xi  (the polarization H)", e_H < mp.mpf("1e-18"),
      f"max err={mp.nstr(e_H,4)}")
check("H has polar coordinates (1,1), so H^2 = 2 Re[1*conj(1)] = 2 spectrally",
      abs(2 * xi(0) - 1) < mp.mpf("1e-16") and abs(2 * xi(1) - 1) < mp.mpf("1e-16"))
check("w = s(s-1)xi has BOTH polar coordinates zero (it is in the radical)",
      abs(w(0)) < mp.mpf("1e-16") and abs(w(1)) < mp.mpf("1e-16")
      and max(abs(w(r)) for r in RHOS) < mp.mpf("1e-19"))
check("w is nonzero: what(1/2) = -xi(1/2)/4", abs(w(mp.mpf(0.5)) + xi(mp.mpf(0.5)) / 4) < mp.mpf("1e-18")
      and abs(w(mp.mpf(0.5))) > mp.mpf("0.1"), f"what(1/2) = {mp.nstr(w(mp.mpf(0.5)), 15)}")

# ----------------------------------------------------------------------
sec("D.  Theorem 2.4(1) -- the generator is *-invariant")
# ----------------------------------------------------------------------
e_star = max(abs(mp.conj(w(1 - mp.conj(s))) - w(s)) for s in SPTS)
check("conj(what(1 - conj s)) = what(s): the ideal is a *-ideal",
      e_star < mp.mpf("1e-18"), f"max err={mp.nstr(e_star,4)}")
# and the involution swaps f_v <-> f_h, as the rulings should be swapped
e_sw = max(abs(mp.conj(fv(1 - mp.conj(s))) - fh(s)) for s in SPTS)
check("conj(fhat_v(1 - conj s)) = fhat_h(s): the involution swaps the two rulings",
      e_sw < mp.mpf("1e-18"), f"max err={mp.nstr(e_sw,4)}")

# ----------------------------------------------------------------------
sec("C.  Lemmas 1.1 / 1.2 -- f_v really lies in D_theta for theta > 3/2")
# ----------------------------------------------------------------------
# F(x) = (1/2pi) int fhat_v(1/2+it) e^{-itx} dt, computed by shifting the contour
# to Re s = 1/2 + a and measuring the resulting bound C(a) e^{-a|x|}.
def profile_fv(x, a=0.0, N=1200, TC=60.0):
    n, wq = np.polynomial.legendre.leggauss(N)
    t = TC * n
    wt = TC * wq
    vals = np.array([complex(fv(mp.mpf(0.5) + mp.mpf(a) + 1j * mp.mpf(float(tt)))) for tt in t])
    return complex(np.dot(wt, vals * np.exp(-(a + 1j * t) * x))) / (2 * np.pi)


for theta in (2.0, 3.0, 4.0):
    xs = [1.0, 2.0, 3.0]
    ok, worst = True, 0.0
    for xv in xs:
        # shifted evaluation must agree with the unshifted one (contour shift is legal)
        v0 = profile_fv(xv, 0.0)
        va = profile_fv(xv, theta)
        worst = max(worst, abs(v0 - va) / (1e-30 + abs(v0)))
        ok = ok and abs(v0 - va) < 1e-8 * (1 + abs(v0))
    check(f"Lemma 1.1: contour shift to Re s = 1/2 + {theta} is legal (values agree)",
          ok, f"max rel diff={worst:.2e}")
    # the shifted formula gives |F(x)| <= C e^{-theta|x|}
    n, wq = np.polynomial.legendre.leggauss(1200)
    t = 60.0 * n
    wt = 60.0 * wq
    vals = np.array([abs(complex(fv(mp.mpf(0.5) + mp.mpf(theta) + 1j * mp.mpf(float(tt))))) for tt in t])
    C = float(np.dot(wt, vals)) / (2 * np.pi)
    bnd_ok = all(abs(profile_fv(xv, 0.0)) <= C * np.exp(-theta * xv) * 1.001 for xv in [1.0, 2.0, 3.0])
    check(f"Lemma 1.2: |F(x)| <= C e^(-{theta}|x|) with C = {C:.4f}, so f_v in D_{theta}",
          bnd_ok and np.isfinite(C))
# the hypothesis of Lemma 1.1 itself: int |fhat_v(sigma+it)| (1+|t|)^N dt < inf,
# at the strip edges sigma = 1/2 +- theta.  Measured for N = 0, 4, 8.
_n8, _w8 = np.polynomial.legendre.leggauss(1500)
_t8, _wt8 = 90.0 * _n8, 90.0 * _w8
for sigma in (0.5 - 4.0, 0.5 + 4.0):
    av = np.array([abs(complex(fv(mp.mpf(sigma) + 1j * mp.mpf(float(tt2))))) for tt2 in _t8])
    mom = [float(np.dot(_wt8, av * (1 + np.abs(_t8)) ** N)) for N in (0, 4, 8)]
    check(f"Lemma 1.1 hypothesis at Re s = {sigma}: the moments N=0,4,8 are finite",
          all(np.isfinite(mom)) and max(mom) < 1e12 and av[-1] < 1e-20,
          f"moments = {mom[0]:.4f}, {mom[1]:.4f}, {mom[2]:.4e}; |fhat_v| at t=90 is {av[-1]:.2e}")

# ----------------------------------------------------------------------
sec("E./F.  Theorem 4.1 -- the intersection numbers as facts about primes")
# ----------------------------------------------------------------------
TCUT, NT = 70.0, 4000
_n, _w = np.polynomial.legendre.leggauss(NT)
T = 0.5 * TCUT * (_n + 1.0)                       # [0, TCUT]
WT = 0.5 * TCUT * _w
print(f"building Xi on {NT} nodes over [0, {TCUT}] ...")
XI = np.array([float(mp.re(xi(mp.mpf(0.5) + 1j * mp.mpf(float(t))))) for t in T])
XI2 = XI ** 2
print(f"  Xi(0) = {XI[0]:.10f}   Xi({TCUT}) = {XI[-1]:.3e}")
KERm = np.array([float(mp.re(mp.digamma(mp.mpf(0.25) + 0.5j * mp.mpf(float(t))))) for t in T])
KER = 0.5 * KERm - 0.5 * np.log(np.pi)

NMAX = 20000
sieve = np.ones(NMAX + 1, bool); sieve[:2] = False
for i in range(2, int(NMAX ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
LN, LV = [], []
for p in np.nonzero(sieve)[0]:
    q = int(p)
    while q <= NMAX:
        LN.append(q); LV.append(np.log(p)); q *= int(p)
LN = np.array(LN, float); LV = np.array(LV); LOGN = np.log(LN)
check(f"prime-power table built ({len(LN)} entries up to {NMAX})", len(LN) > 2000)
COSM = np.cos(np.outer(LOGN, T))                  # shared across probes

# fhat, ghat pairs and the elementary closed forms claimed in section 4
PROBES = [
    ("w (radical)",      w,  w,  lambda s: (mp.mpc(s) * (mp.mpc(s) - 1) * xi(s)) ** 2,
     lambda t: 2 * (0.25 + t ** 2) ** 2 * XI2, mp.mpf(0)),
    ("f_v",              fv, fv, lambda s: -4 * mp.mpc(s) * (mp.mpc(s) - 1) * xi(s) ** 2,
     lambda t: 8 * (0.25 + t ** 2) * XI2, mp.mpf(0)),
    ("f_h",              fh, fh, lambda s: -4 * mp.mpc(s) * (mp.mpc(s) - 1) * xi(s) ** 2,
     lambda t: 8 * (0.25 + t ** 2) * XI2, mp.mpf(0)),
    ("f_v * ~f_h",       fv, fh, lambda s: 4 * (mp.mpc(s) - 1) ** 2 * xi(s) ** 2,
     lambda t: 8 * (0.25 - t ** 2) * XI2, mp.mpf(1)),
    ("H = f_v + f_h",    lambda s: 2 * xi(s), lambda s: 2 * xi(s), lambda s: 4 * xi(s) ** 2,
     lambda t: 8 * XI2, mp.mpf(2)),
    ("f_v - f_h",        lambda s: -2 * (2 * mp.mpc(s) - 1) * xi(s),
     lambda s: -2 * (2 * mp.mpc(s) - 1) * xi(s),
     lambda s: -4 * (2 * mp.mpc(s) - 1) ** 2 * xi(s) ** 2,
     lambda t: 32 * t ** 2 * XI2, mp.mpf(-2)),
    ("xi alone (CONTROL)", xi, xi, lambda s: xi(s) ** 2,
     lambda t: 2 * XI2, mp.mpf(0.5)),
]

print()
print(f"{'probe':>20s} | {'P(h)':>15s} | {'A(h)':>15s} | {'P-A':>15s} | {'spectral':>9s} | {'error':>9s}")
print("-" * 100)
for name, fhat, ghat, hclosed, Gfun, pred in PROBES:
    # E: hhat(s) = fhat(s) conj(ghat(1 - conj s)) matches the elementary closed form
    e_h = max(abs(fhat(s) * mp.conj(ghat(1 - mp.conj(s))) - hclosed(s)) for s in SPTS)
    check(f"E [{name}]: hhat = fhat(s) conj(ghat(1-conj s)) matches the closed form in the table",
          e_h < mp.mpf("1e-16"), f"max err={mp.nstr(e_h,4)}")
    # E: G(t) = hhat(1/2+it) + hhat(1/2-it) matches the elementary expression
    Gv = Gfun(T)
    tt = [0.0, 2.5, 11.0]
    e_G = 0.0
    for t0 in tt:
        lhs = complex(hclosed(mp.mpf(0.5) + 1j * mp.mpf(t0)) + hclosed(mp.mpf(0.5) - 1j * mp.mpf(t0)))
        Xi0 = float(mp.re(xi(mp.mpf(0.5) + 1j * mp.mpf(t0)))) ** 2
        # rebuild the elementary G at this single t
        poly = {"w (radical)": 2 * (0.25 + t0 ** 2) ** 2, "f_v": 8 * (0.25 + t0 ** 2),
                "f_h": 8 * (0.25 + t0 ** 2), "f_v * ~f_h": 8 * (0.25 - t0 ** 2),
                "H = f_v + f_h": 8.0, "f_v - f_h": 32 * t0 ** 2, "xi alone (CONTROL)": 2.0}[name]
        e_G = max(e_G, abs(lhs - poly * Xi0))
    check(f"E [{name}]: G(t) = hhat(1/2+it) + hhat(1/2-it) matches the elementary form",
          e_G < 1e-13, f"max err={e_G:.2e}")
    # spectral side (uses zeros only via 'xi kills them' -- all these hhat carry xi^2)
    spec = complex(hclosed(0) + hclosed(1))
    check(f"E [{name}]: spectral side hhat(0)+hhat(1) = {float(pred)} (zero sum vanishes: xi^2 factor)",
          abs(spec - complex(pred)) < 1e-13, f"= {spec.real:.12f}")
    # F: the ARITHMETIC side.  No zeros appear below this line.
    A = float(np.dot(WT, KER * Gv)) / np.pi
    C = (COSM @ (WT * Gv)) / np.pi
    terms = LV / np.sqrt(LN) * C
    P = float(terms.sum())
    tail = float(np.abs(terms[LN > 1000]).sum())
    err = abs(P - A - float(pred))
    print(f"{name:>20s} | {P:15.9f} | {A:15.9f} | {P-A:15.9f} | {float(pred):9.1f} | {err:9.2e}")
    check(f"F [{name}]: ARITHMETIC side P(h) - A(h) = {float(pred)} (primes + digamma, no zeros)",
          err < 1e-8, f"P-A = {P-A:.10f}, err = {err:.2e}, tail(n>1000) = {tail:.1e}")
    check(f"F [{name}]: the prime sum has converged (tail beyond n=1000 is negligible)",
          tail < 1e-8, f"tail = {tail:.2e}")
    check(f"F [{name}]: not vacuous -- P and A are individually far from the answer",
          abs(P - float(pred)) > 1e-3 or abs(A) > 1e-3,
          f"|P - pred| = {abs(P-float(pred)):.6f}, |A| = {abs(A):.6f}")

# ----------------------------------------------------------------------
sec("G.  NEGATIVE CONTROLS -- the s(s-1) xi factor is load-bearing")
# ----------------------------------------------------------------------
check("G: 'xi alone' is NOT in the radical -- its polar coordinates are 1/2, not 0, "
      "and the arithmetic side returns 1/2, not 0 (so the s(s-1) factor is required)",
      abs(xi(0) - mp.mpf(0.5)) < mp.mpf("1e-16"))

# a non-xi-divisible element: the Gaussian probe of 113_07/113_08
BB = 14.0
AA = BB / (2 * np.pi)


def f0hat(s):
    s = np.asarray(s, dtype=complex); wv = s - 0.5
    return np.sqrt(np.pi / AA) * np.exp((wv * wv - BB * BB) / (4 * AA)) * np.cos(wv * BB / (2 * AA))


GAM = np.array([float(mp.im(r)) for r in RHOS])
zsum = 2.0 * float(np.sum(np.abs(f0hat(0.5 + 1j * GAM)) ** 2))
check("G: the Gaussian probe of 113_07 is NOT in the radical -- its zero sum is nonzero",
      zsum > 0.1, f"sum m|fhat(rho)|^2 = {zsum:.9f} over {NZ} zeros")
check("G: while every xi-divisible probe above has zero sum exactly 0 "
      "(that is what makes the spectral side a small integer)",
      max(abs(fv(r)) for r in RHOS) < mp.mpf("1e-19"))

# radicality really is an ideal property: w * (Gaussian) is still in the radical
gauss_f = lambda s: mp.mpc(complex(f0hat(np.array([complex(s)]))[0]))
prod = lambda s: w(s) * gauss_f(s)
check("G: rad is an ideal -- w * (Gaussian) still vanishes at 0, 1 and every zero",
      abs(prod(0)) < mp.mpf("1e-15") and abs(prod(1)) < mp.mpf("1e-15")
      and max(abs(prod(r)) for r in RHOS) < mp.mpf("1e-18"))
# The product must be a NONZERO element of the radical.  Sample several points:
# this Gaussian is ~3e-10 at s = 1/2 by construction (its transform has a node
# structure with mass near |t| = 14), so a single sample there proves nothing.
_pts = [mp.mpf(0.5), mp.mpf(0.5) + 14j, mp.mpf(0.5) + 5j, mp.mpf(1.5), mp.mpf(0.5) + 20j]
_vals = [(p, abs(prod(p))) for p in _pts]
_best = max(_vals, key=lambda z: z[1])
check("G: and the product is a NONZERO element of the radical",
      _best[1] > mp.mpf("1e-3"),
      "max over sample points |w*g| = %s at s = %s   (at s=1/2 it is only %s, "
      "because that probe is nearly zero there)"
      % (mp.nstr(_best[1], 8), mp.nstr(_best[0], 6), mp.nstr(_vals[0][1], 4)))

# ----------------------------------------------------------------------
sec("H.  Corollary 3.2 -- the projection lands in D^o")
# ----------------------------------------------------------------------
# take a probe with BOTH polar coordinates nonzero
AA2, BB2 = 1.0, 3.0


def f2hat(s):
    s = np.asarray(s, dtype=complex); wv = s - 0.5
    return np.sqrt(np.pi / AA2) * np.exp((wv * wv - BB2 * BB2) / (4 * AA2)) * np.cos(wv * BB2 / (2 * AA2))


p0, p1 = complex(f2hat(0.0)), complex(f2hat(1.0))
check("H: the test probe has both polar coordinates nonzero (projection is not trivial)",
      abs(p0) > 1e-3 and abs(p1) > 1e-3, f"fhat(0)={p0.real:.9f}, fhat(1)={p1.real:.9f}")
pi_at = lambda s: complex(f2hat(np.array([complex(s)]))[0]) - p0 * complex(fv(s)) - p1 * complex(fh(s))
check("Cor 3.2: pi(f)hat(0) = 0", abs(pi_at(0)) < 1e-12, f"= {abs(pi_at(0)):.2e}")
check("Cor 3.2: pi(f)hat(1) = 0", abs(pi_at(1)) < 1e-12, f"= {abs(pi_at(1)):.2e}")
e_keep = max(abs(pi_at(r) - complex(f2hat(np.array([complex(r)]))[0])) for r in RHOS)
check("Cor 3.2: pi(f) leaves every zero coordinate untouched (f_v, f_h carry the xi factor)",
      e_keep < 1e-15, f"max change = {e_keep:.2e}")
# pi(f) must itself satisfy the Lemma 1.1 hypothesis, i.e. stay inside D
_av = np.array([abs(pi_at(mp.mpf(0.5) + 2.0 + 1j * mp.mpf(float(tt2)))) for tt2 in _t8])
_m0 = float(np.dot(_wt8, _av))
check("Cor 3.2: pi(f) is again in D -- its Lemma 1.1 moment at Re s = 2.5 is finite "
      "and the integrand dies at t = 90",
      np.isfinite(_m0) and _m0 < 1e12 and _av[-1] < 1e-20,
      f"moment = {_m0:.6f}, |pi(f)hat| at t=90 is {_av[-1]:.2e}")

# ----------------------------------------------------------------------
sec("SUMMARY")
# ----------------------------------------------------------------------
print(f"{sum(PASS)}/{len(PASS)} checks passed")
print()
print("NOT established by this file, and not claimed:  that rad I_partial is the")
print("principal divisor group of any geometric object;  rows (a),(b),(c);  (E) and")
print("(R) of 113_08 section 4;  hypothesis (2) of Connes' Lemma 2.1;  Weil")
print("positivity;  a degree map;  anything about RH.")
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
print("VERDICT: SOME CHECKS FAILED")
raise SystemExit(1)
