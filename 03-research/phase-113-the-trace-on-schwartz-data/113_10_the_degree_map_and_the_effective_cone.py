#!/usr/bin/env python3
"""
113_10 -- The degree map, the effective cone, and the reduction of row (d).

Verifies 113_10_THE_DEGREE_MAP_AND_THE_EFFECTIVE_CONE.md.

Conventions (113_05):
    fhat(s) = int_0^inf f(u) u^s d^x u,   d^x u = du/u
    F(x)    = e^{x/2} f(e^x),             f(u) = u^{-1/2} F(log u)
    fhat(s) = Fhat(s - 1/2),              Fhat(z) = int_R F(x) e^{zx} dx

Objects (113_09):
    fhat_v(s) = -2(s-1) xi(s)      fhat_h(s) = 2 s xi(s)
    Hhat(s)   = 2 xi(s)            what(s)   = s(s-1) xi(s)   [radical generator]

Sections:
    A  three closed forms of deg
    B  deg on the geometric classes; linearity; deg(rad) = 0 by quadrature
    C  Riemann's Phi: evenness, Xi = Fourier(Phi), positivity, moments
    D  F_v = Phi + 2Phi', F_h = Phi - 2Phi', W = Phi'' - Phi/4: sign changes
    E  Thm 2.2, Cor 2.3, Cor 2.4 on explicit data
    F  Thm 2.5 = requirement (R), in the coordinate model, zero-data independent
    G  Prop 5.1 (O1) and negative controls

No zero of xi is used in any definition.  Section F uses zero *lists* only to
build two contrasting coordinate models and show the answer does not depend on
them; that is a robustness control, not a definition.
"""

import sys
import numpy as np
import mpmath as mp

mp.mp.dps = 30

NPASS = 0
NFAIL = 0


def check(label, cond, detail=""):
    global NPASS, NFAIL
    ok = bool(cond)
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")
    return ok


def head(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ---------------------------------------------------------------- xi and Phi

def xi(s):
    """Riemann xi.  s=0 and s=1 are removable singularities of the product
    form (gamma pole / zeta pole); nudge at dps=30 to resolve them."""
    s = mp.mpc(s)
    if abs(s) < mp.mpf("1e-8") or abs(s - 1) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


NPHI = 60


def Phi_raw(u, N=NPHI):
    """Titchmarsh 10.1:  Xi(t) = int Phi(u) e^{iut} du."""
    u = mp.mpf(u)
    tot = mp.mpf(0)
    for n in range(1, N + 1):
        n = mp.mpf(n)
        tot += (2 * mp.pi * n ** 4 * mp.e ** (9 * u / 2)
                - 3 * n ** 2 * mp.e ** (5 * u / 2)) * mp.e ** (-mp.pi * n ** 2 * mp.e ** (2 * u))
    return 2 * mp.pi * tot


def Phi(u):
    """Phi is even.  The raw series needs n >~ e^{-u} terms, so for u << 0 a
    fixed truncation returns garbage; evaluate at |u| instead, where N=60 is
    ample (exp(-pi n^2) at n=60 is ~1e-4900)."""
    return Phi_raw(abs(mp.mpf(u)))


dPhi = lambda u: mp.diff(Phi, mp.mpf(u), 1)
d2Phi = lambda u: mp.diff(Phi, mp.mpf(u), 2)

QRANGE = [-4, -1, 0, 1, 4]          # Phi(4) ~ 1.8e-4058: far beyond enough
quadF = lambda g: mp.quad(g, QRANGE)

# closed-form transforms of the geometric classes
FHAT = {
    "H       (2 xi)":        lambda s: 2 * xi(s),
    "f_v     (-2(s-1)xi)":   lambda s: -2 * (mp.mpc(s) - 1) * xi(s),
    "f_h     (2 s xi)":      lambda s: 2 * mp.mpc(s) * xi(s),
    "f_v-f_h (-2(2s-1)xi)":  lambda s: -2 * (2 * mp.mpc(s) - 1) * xi(s),
    "w       (s(s-1)xi)":    lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * xi(s),
}
DEG_EXPECT = {
    "H       (2 xi)": 2,
    "f_v     (-2(s-1)xi)": 1,
    "f_h     (2 s xi)": 1,
    "f_v-f_h (-2(2s-1)xi)": 0,
    "w       (s(s-1)xi)": 0,
}
# balanced profiles, derived in 113_10 Thm 3.2 / Prop 3.3
PROFILE = {
    "H       (2 xi)":        lambda x: 2 * Phi(x),
    "f_v     (-2(s-1)xi)":   lambda x: Phi(x) + 2 * dPhi(x),
    "f_h     (2 s xi)":      lambda x: Phi(x) - 2 * dPhi(x),
    "f_v-f_h (-2(2s-1)xi)":  lambda x: 4 * dPhi(x),
    "w       (s(s-1)xi)":    lambda x: d2Phi(x) - Phi(x) / 4,
}

TOL = mp.mpf("1e-12")


# =============================================================== A

head("A.  Theorem 1.2 -- the three closed forms of deg")

print("  deg(f) = fhat(0)+fhat(1) = int f(u)(1+u) d^x u = 2 int F(x) cosh(x/2) dx")
print()
for a in [mp.mpf("0.5"), mp.mpf(1), mp.mpf(2)]:
    # F(x) = exp(-a x^2)  ->  fhat(s) = sqrt(pi/a) exp((s-1/2)^2/(4a))
    fh = lambda s, a=a: mp.sqrt(mp.pi / a) * mp.e ** (((mp.mpc(s) - mp.mpf(0.5)) ** 2) / (4 * a))
    d1 = fh(0) + fh(1)
    d2 = 2 * mp.quad(lambda x, a=a: mp.e ** (-a * x * x) * mp.cosh(x / 2), [-mp.inf, 0, mp.inf])
    d3 = mp.quad(lambda u, a=a: (mp.e ** (-a * mp.log(u) ** 2) / mp.sqrt(u)) * (1 + u) / u,
                 [0, 1, mp.inf])
    e12, e13 = abs(d1 - d2), abs(d1 - d3)
    check(f"a={float(a)}: transform = x-space = u-space",
          e12 < TOL and e13 < TOL,
          f"sum={mp.nstr(mp.re(d1),18)}  2int F cosh={mp.nstr(d2,18)}  "
          f"int f(1+u)d^x u={mp.nstr(d3,18)}   |diff| {mp.nstr(e12,3)}, {mp.nstr(e13,3)}")

# discriminating power: the WRONG x-space weight (1+e^x) must NOT agree
a = mp.mpf(1)
fh = lambda s: mp.sqrt(mp.pi) * mp.e ** (((mp.mpc(s) - mp.mpf(0.5)) ** 2) / 4)
wrong = mp.quad(lambda x: mp.e ** (-x * x) * (1 + mp.e ** x), [-mp.inf, 0, mp.inf])
check("negative control: the weight (1+e^x) is NOT the x-space weight",
      abs(fh(0) + fh(1) - wrong) > mp.mpf("0.2"),
      f"correct = {mp.nstr(mp.re(fh(0)+fh(1)),12)}   with (1+e^x) = {mp.nstr(wrong,12)}   "
      f"gap = {mp.nstr(abs(fh(0)+fh(1)-wrong),6)}  (the factor is 2cosh(x/2), not 1+e^x)")


# =============================================================== B

head("B.  Prop 1.4 / Thm 1.3 -- deg on the geometric classes")

print(f"  {'class':<24s} {'fhat(0)':>12s} {'fhat(1)':>12s} {'deg':>14s} {'expect':>7s}")
print("  " + "-" * 74)
degs = {}
for name, fn in FHAT.items():
    v0, v1 = fn(0), fn(1)
    d = v0 + v1
    degs[name] = d
    print(f"  {name:<24s} {mp.nstr(mp.re(v0),8):>12s} {mp.nstr(mp.re(v1),8):>12s} "
          f"{mp.nstr(mp.re(d),12):>14s} {DEG_EXPECT[name]:>7d}")
print()
for name in FHAT:
    check(f"deg({name.split()[0]}) = {DEG_EXPECT[name]}",
          abs(degs[name] - DEG_EXPECT[name]) < TOL,
          f"|error| = {mp.nstr(abs(degs[name]-DEG_EXPECT[name]),3)}")

check("Prop 1.5: D^o is STRICTLY inside ker(deg)  --  f_v-f_h witnesses it",
      abs(degs["f_v-f_h (-2(2s-1)xi)"]) < TOL
      and abs(FHAT["f_v-f_h (-2(2s-1)xi)"](0) - 1) < TOL,
      f"deg(f_v-f_h) = 0 but (f_v-f_h)^(0) = "
      f"{mp.nstr(mp.re(FHAT['f_v-f_h (-2(2s-1)xi)'](0)),12)} != 0, so it is not in D^o")

# linearity, on random complex combinations of the five classes
rng = np.random.default_rng(101_113)
worst = mp.mpf(0)
for _ in range(20):
    c = [mp.mpc(float(z.real), float(z.imag)) for z in (rng.normal(size=5) + 1j * rng.normal(size=5))]
    lhs = sum(ci * (fn(0) + fn(1)) for ci, fn in zip(c, FHAT.values()))
    rhs = sum(ci * fn(0) for ci, fn in zip(c, FHAT.values())) \
        + sum(ci * fn(1) for ci, fn in zip(c, FHAT.values()))
    worst = max(worst, abs(lhs - rhs))
check("deg is linear (20 random complex combinations)", worst < TOL,
      f"worst |deg(sum) - sum(deg)| = {mp.nstr(worst,3)}")

# Thm 1.3 by QUADRATURE, not by reading off the s(s-1) factor:
# deg(w) = 2 int W(x) cosh(x/2) dx must cancel to 0 although W is large.
Wq = 2 * quadF(lambda x: PROFILE["w       (s(s-1)xi)"](x) * mp.cosh(x / 2))
Wmax = max(abs(PROFILE["w       (s(s-1)xi)"](mp.mpf(t) / 10)) for t in range(0, 21))
check("Thm 1.3 by quadrature: deg(w) = 2 int W cosh(x/2) dx = 0",
      abs(Wq) < mp.mpf("1e-10"),
      f"value = {mp.nstr(Wq,6)}  while max|W| on [0,2] = {mp.nstr(Wmax,8)} "
      f"-- a genuine cancellation, not a small integrand")

for name in ["H       (2 xi)", "f_v     (-2(s-1)xi)", "f_h     (2 s xi)"]:
    q = 2 * quadF(lambda x, n=name: PROFILE[n](x) * mp.cosh(x / 2))
    check(f"deg({name.split()[0]}) by quadrature of the profile = {DEG_EXPECT[name]}",
          abs(q - DEG_EXPECT[name]) < mp.mpf("1e-10"),
          f"2 int F cosh(x/2) dx = {mp.nstr(q,15)}")


# =============================================================== C

head("C.  Riemann's Phi -- evenness, Xi = Fourier(Phi), positivity, moments")

for u, dps in [(mp.mpf(1), 30), (mp.mpf("1.5"), 30), (mp.mpf("1.5"), 90)]:
    # At u = -1.5 the series has ~22 digits of catastrophic cancellation: the
    # largest term is ~8e-2 while the sum is ~1.3e-23.  dps=30 therefore
    # retains only ~8 digits, dps=90 retains ~68.  Both are recorded, because
    # the first would otherwise read as a failure of evenness rather than of
    # precision.
    with mp.workdps(dps):
        a_, b_ = Phi_raw(u, 400), Phi_raw(-u, 400)
        rel = abs(a_ - b_) / abs(a_)
    check(f"raw series is even at u={float(u)} (N=400, dps={dps}): "
          f"agreement to {max(0, -int(mp.floor(mp.log10(rel + mp.mpf('1e-99'))))):d} digits",
          rel < mp.mpf("1e-7") if dps == 30 else rel < mp.mpf("1e-30"),
          f"Phi(+u)={mp.nstr(a_,12)}  Phi(-u)={mp.nstr(b_,12)}  rel={mp.nstr(rel,3)}")

bad = Phi_raw(mp.mpf(-4), NPHI)
check("diagnosis: the raw series at u=-4 with N=60 is unusable (sign is wrong)",
      bad < 0,
      f"Phi_raw(-4, 60) = {mp.nstr(bad,8)} < 0, while Phi(4) = {mp.nstr(Phi(4),8)} > 0; "
      f"exp(-pi n^2 e^{{2u}}) needs n >~ e^{{-u}} ~ 55 terms.  We evaluate at |u|.")

# independent Fourier inversion of xi
TC, NT = 90.0, 6000
_n, _w = np.polynomial.legendre.leggauss(NT)
TT = 0.5 * TC * (_n + 1.0)
WT = 0.5 * TC * _w
XIL = np.array([float(mp.re(xi(mp.mpf(0.5) + 1j * mp.mpf(float(t))))) for t in TT])
invXi = lambda x: float(np.dot(WT, XIL * np.cos(TT * x))) / np.pi

print()
print(f"  {'x':>6s} {'(1/2pi) int Xi e^{-itx}':>24s} {'Phi(x)':>22s} {'rel':>10s}")
print("  " + "-" * 66)
worst = 0.0
for x in [0.0, 0.2, 0.4, 0.6, -0.4]:
    a_, b_ = invXi(x), float(Phi(x))
    r = abs(a_ - b_) / abs(b_)
    worst = max(worst, r)
    print(f"  {x:6.2f} {a_:24.15f} {b_:22.15f} {r:10.2e}")
check("Xi = Fourier(Phi): Phi matches the inversion of an independent xi",
      worst < 2e-10,
      f"worst relative deviation on |x|<=0.6 is {worst:.2e}; the Gauss-Legendre "
      f"noise floor is ~2e-12 and Phi(0.6) ~ 1.5e-2")

grid = [mp.mpf(k) / 10 for k in range(0, 81)]
vals = [Phi(g) for g in grid]
check("Phi > 0 at 81 points of [0,8]  (mpmath: Phi(4) and Phi(8) underflow float64)",
      all(v > 0 for v in vals),
      f"Phi(0)={mp.nstr(vals[0],10)}  Phi(4)={mp.nstr(Phi(4),8)}  Phi(8)={mp.nstr(Phi(8),8)}")

m0 = quadF(Phi)
mp_ = quadF(lambda x: Phi(x) * mp.e ** (x / 2))
mm_ = quadF(lambda x: Phi(x) * mp.e ** (-x / 2))
check("int Phi dx = xi(1/2)", abs(m0 - mp.re(xi(mp.mpf(0.5)))) < TOL,
      f"{mp.nstr(m0,15)} vs xi(1/2) = {mp.nstr(mp.re(xi(mp.mpf(0.5))),15)}")
check("int Phi e^{+x/2} dx = xi(1) = 1/2", abs(mp_ - mp.mpf(0.5)) < TOL,
      f"{mp.nstr(mp_,18)}")
check("int Phi e^{-x/2} dx = xi(0) = 1/2", abs(mm_ - mp.mpf(0.5)) < TOL,
      f"{mp.nstr(mm_,18)}")
check("Thm 3.2: deg(H) = 4 int Phi cosh(x/2) dx = 2",
      abs(4 * quadF(lambda x: Phi(x) * mp.cosh(x / 2)) - 2) < TOL,
      f"{mp.nstr(4*quadF(lambda x: Phi(x)*mp.cosh(x/2)),18)}")


# =============================================================== D

head("D.  Prop 3.3 -- the profiles of the rulings and of the radical generator")

print("  {:>6s} {:>16s} {:>18s} {:>18s} {:>16s}".format(
    "x", "F_H = 2Phi", "F_v = Phi+2Phi'", "F_h = Phi-2Phi'", 'W = Phi"-Phi/4'))
print("  " + "-" * 78)
sv, sh, sw = [], [], []
for x in [0.0, 0.2, 0.4, 0.6, 1.0, 1.5]:
    x = mp.mpf(x)
    a_ = 2 * Phi(x)
    b_ = Phi(x) + 2 * dPhi(x)
    c_ = Phi(x) - 2 * dPhi(x)
    d_ = d2Phi(x) - Phi(x) / 4
    sv.append(b_); sh.append(c_); sw.append(d_)
    print(f"  {float(x):6.2f} {mp.nstr(a_,8):>16s} {mp.nstr(b_,8):>18s} "
          f"{mp.nstr(c_,8):>18s} {mp.nstr(d_,8):>16s}")
print()
check("F_v changes sign (so f_v is NOT nonnegative)",
      max(sv) > 0 and min(sv) < 0,
      f"F_v(0) = {mp.nstr(sv[0],8)} > 0,  F_v(0.2) = {mp.nstr(sv[1],8)} < 0")
check("W changes sign (Cor 2.3: no nonzero radical element is nonnegative)",
      max(sw) > 0 and min(sw) < 0,
      f"W(0) = {mp.nstr(sw[0],8)} < 0,  W(0.4) = {mp.nstr(sw[2],8)} > 0")
check("F_h(x) = F_v(-x)  (the involution swaps the rulings, 113_09 section D)",
      all(abs(Phi(x) - 2 * dPhi(x) - (Phi(-x) + 2 * dPhi(-x))) < mp.mpf("1e-14")
          for x in [mp.mpf("0.3"), mp.mpf("0.7"), mp.mpf("1.1")]),
      "checked at x = 0.3, 0.7, 1.1")
check("F_H = F_v + F_h",
      all(abs(2 * Phi(x) - ((Phi(x) + 2 * dPhi(x)) + (Phi(x) - 2 * dPhi(x)))) < mp.mpf("1e-20")
          for x in [mp.mpf("0.2"), mp.mpf("0.9")]),
      "Phi' cancels, as H = f_v + f_h requires")


# =============================================================== E

head("E.  Thm 2.2, Cor 2.3, Cor 2.4 -- the effective cone")

# nonnegative data: Gaussians, and H itself
NONNEG = [("F = exp(-x^2)", lambda x: mp.e ** (-x * x)),
          ("F = exp(-2x^2)", lambda x: mp.e ** (-2 * x * x)),
          ("F = 2 Phi  (= H)", lambda x: 2 * Phi(x)),
          ("F = Phi^2", lambda x: Phi(x) ** 2)]
for name, F in NONNEG:
    lo = min(F(mp.mpf(t) / 5) for t in range(-15, 16))
    v0 = quadF(lambda x, F=F: F(x) * mp.e ** (-x / 2))
    v1 = quadF(lambda x, F=F: F(x) * mp.e ** (x / 2))
    check(f"Thm 2.2 on {name}: fhat(0) > 0, fhat(1) > 0, deg > 0",
          lo >= 0 and v0 > 0 and v1 > 0,
          f"min F on [-3,3] = {mp.nstr(lo,6)};  fhat(0) = {mp.nstr(v0,12)}, "
          f"fhat(1) = {mp.nstr(v1,12)},  deg = {mp.nstr(v0+v1,12)}")

# Cor 2.4: the standard D^o probe must change sign
aD, bD = mp.mpf(14) / (2 * mp.pi), mp.mpf(14)
FD = lambda x: mp.e ** (-aD * x * x) * mp.cos(bD * x)
fhD = lambda s: mp.sqrt(mp.pi / aD) * mp.e ** (((mp.mpc(s) - mp.mpf(0.5)) ** 2 - bD ** 2) / (4 * aD)) \
    * mp.cos((mp.mpc(s) - mp.mpf(0.5)) * bD / (2 * aD))
vD = [FD(mp.mpf(t) / 10) for t in range(0, 12)]
check("Cor 2.4: the standard D^o probe (a=b/2pi, b=14) is in D^o ...",
      abs(fhD(0)) < mp.mpf("1e-15") and abs(fhD(1)) < mp.mpf("1e-15"),
      f"fhat(0) = {mp.nstr(abs(fhD(0)),4)},  fhat(1) = {mp.nstr(abs(fhD(1)),4)}")
check("... and it necessarily changes sign, as Cor 2.4 forces",
      max(vD) > 0 and min(vD) < 0,
      f"F(0) = {mp.nstr(vD[0],8)},  F(0.3) = {mp.nstr(vD[3],8)};  deg = "
      f"{mp.nstr(abs(fhD(0)+fhD(1)),4)} = 0")

check("Cor 2.3 restated: deg(w) = 0 and W != 0, hence W must change sign",
      abs(Wq) < mp.mpf("1e-10") and Wmax > 1,
      f"deg(w) = {mp.nstr(Wq,4)}, max|W| = {mp.nstr(Wmax,8)} -- consistent with D above")


# =============================================================== F

head("F.  Thm 2.5 -- requirement (R), and its independence from the zero data")


def s_form(x, y, mirror, m):
    """s(x,y) = x0 conj(y1) + x1 conj(y0) - sum_rho m_rho x(rho) conj(y(rho'))."""
    x0, x1, xz = x[0], x[1], x[2:]
    y0, y1, yz = y[0], y[1], y[2:]
    return x0 * np.conj(y1) + x1 * np.conj(y0) - np.sum(m * xz * np.conj(yz[mirror]))


def model(zeros, mults):
    """Build the mirror permutation rho -> rho' = 1 - conj(rho) for a zero list."""
    z = np.array(zeros, dtype=complex)
    mir = np.array([int(np.argmin(np.abs(z - (1 - np.conj(w))))) for w in z])
    return mir, np.array(mults, dtype=float)


ON = ([0.5 + 14.13j, 0.5 - 14.13j, 0.5 + 21.02j, 0.5 - 21.02j, 0.5 + 25.01j, 0.5 - 25.01j],
      [1, 1, 1, 1, 1, 1])
OFF = ([0.83 + 4.1j, 0.17 - 4.1j, 0.17 + 4.1j, 0.83 - 4.1j, 0.5 + 9.3j, 0.5 - 9.3j],
       [2, 2, 2, 2, 3, 3])

for tag, (zs, ms) in [("all zeros ON the line", ON), ("zeros OFF the line, mults 2,3", OFF)]:
    mir, m = model(zs, ms)
    nz = len(zs)
    Fv = np.zeros(2 + nz, dtype=complex); Fv[0] = 1.0     # (1, 0, 0)
    Fh = np.zeros(2 + nz, dtype=complex); Fh[1] = 1.0     # (0, 1, 0)
    rng2 = np.random.default_rng(7719)
    e0 = e1 = 0.0
    for _ in range(50):
        x = rng2.normal(size=2 + nz) + 1j * rng2.normal(size=2 + nz)
        e0 = max(e0, abs(s_form(x, Fv, mir, m) - x[1]))
        e1 = max(e1, abs(s_form(x, Fh, mir, m) - x[0]))
    check(f"113_08 (2.2) holds in the model with {tag}: s(x,F_v)=x^(1), s(x,F_h)=x^(0)",
          e0 < 1e-13 and e1 < 1e-13,
          f"worst error over 50 random x: {e0:.2e}, {e1:.2e}  -- the zero block "
          f"never contributes, because F_v and F_h have zero rho-coordinates")

# (R) itself: an effective class has BOTH pairings nonzero and positive
mir, m = model(*ON)
for name, F in NONNEG:
    v0 = complex(quadF(lambda x, F=F: F(x) * mp.e ** (-x / 2)))
    v1 = complex(quadF(lambda x, F=F: F(x) * mp.e ** (x / 2)))
    x = np.zeros(2 + 6, dtype=complex); x[0], x[1] = v0, v1
    pv, ph = s_form(x, np.eye(8, dtype=complex)[0], mir, m), s_form(x, np.eye(8, dtype=complex)[1], mir, m)
    check(f"Thm 2.5 on {name}: s(.,F_v) != 0 AND s(.,F_h) != 0",
          abs(pv) > 1e-10 and abs(ph) > 1e-10 and pv.real > 0 and ph.real > 0,
          f"s(.,F_v) = {pv.real:.12f},  s(.,F_h) = {ph.real:.12f}  -- both strictly "
          f"positive, so (R) holds with both alternatives true")


# =============================================================== G

head("G.  Prop 5.1 (obstruction O1) and negative controls")

# Prop 5.1: scaling cannot create or destroy effectivity
for n in [2, 5, 100]:
    lo_pos = min(n * mp.e ** (-(mp.mpf(t) / 5) ** 2) for t in range(-15, 16))
    sv_scaled = [n * (Phi(mp.mpf(x)) + 2 * dPhi(mp.mpf(x))) for x in [0, 0.2]]
    check(f"Prop 5.1 at n={n}: scaling preserves both nonnegativity and its failure",
          lo_pos > 0 and sv_scaled[0] > 0 and sv_scaled[1] < 0,
          f"n*Gaussian stays >= 0;  n*F_v still changes sign "
          f"({mp.nstr(sv_scaled[0],6)} / {mp.nstr(sv_scaled[1],6)}) -- "
          f"h^0(nD) = h^0(D), so no growth argument is available")

# O1 stated as a measurement: deg scales linearly but effectivity does not change
check("O1: deg(nH) = 2n grows, yet h^0 is unchanged -- degree cannot drive a growth argument",
      all(abs(n * degs["H       (2 xi)"] - 2 * n) < TOL for n in [2, 5, 100]),
      "deg(2H)=4, deg(5H)=10, deg(100H)=200, while nH is effective for every n>0 "
      "and for no reason that depends on n")

# negative control 1: deg is not s(.,F_v) alone
check("negative control: deg is not the F_v pairing alone",
      abs(FHAT["f_v     (-2(s-1)xi)"](1)) < TOL
      and abs(degs["f_v     (-2(s-1)xi)"] - 1) < TOL,
      f"s(f_v,F_v) = f_v^(1) = 0 but deg(f_v) = 1; the two functionals differ")

# negative control 2: the Thm 4.2 contradiction is real, not vacuous.
# In an off-line model, exhibit x in D^o (polar slots zero) with s(x,x) > 0.
mirO, mO = model(*OFF)
mirN, mN = model(*ON)
# The witness must occupy a MIRRORED pair of slots (a, mirror[a]); putting the
# +1 and -1 on two unrelated zeros makes every term of the zero sum vanish and
# gives s(x,x) = 0, which tests nothing.
a_idx = 0
b_idx = int(mirO[a_idx])                    # = 2 for OFF (0.83+4.1i <-> 0.17+4.1i)
w = np.zeros(8, dtype=complex)
w[2 + a_idx] = 1.0
w[2 + b_idx] = -1.0
q_off = s_form(w, w, mirO, mO).real
deg_off = (w[0] + w[1]).real
q_on = s_form(w, w, mirN, mN).real
check("negative control: off-line zeros give x in D^o with s(x,x) > 0 and deg(x) = 0",
      q_off > 0 and abs(deg_off) < 1e-14,
      f"witness on the mirrored pair (rho={OFF[0][a_idx]}, rho'={OFF[0][b_idx]}), "
      f"mults {int(mO[a_idx])},{int(mO[b_idx])}:  s(x,x) = {q_off:+.6f} > 0 with "
      f"deg(x) = {deg_off:.1e} -- exactly the configuration Thm 4.2 rules out")
check("... and the witness really is in D^o (both polar slots empty)",
      abs(w[0]) == 0 and abs(w[1]) == 0 and np.abs(w[2:]).max() > 0,
      "x^(0) = x^(1) = 0, so deg(x) = 0 while the zero block carries all the mass")
check("... and the same witness with all zeros ON the line gives s(x,x) < 0",
      q_on < 0,
      f"s(x,x) = {q_on:+.6f} -- the sign flip is caused by the zero locations, "
      f"nothing else changed")

# negative control 3: Phi positivity is not an artifact of a coarse grid
fine = [Phi(mp.mpf(k) / 100) for k in range(0, 121)]
check("negative control: Phi > 0 also on a 10x finer grid of [0,1.2]",
      all(v > 0 for v in fine),
      f"121 points, min = {mp.nstr(min(fine),8)} at x = 1.20")


# =============================================================== verdict

print()
print("=" * 78)
print(f"  checks: {NPASS} passed, {NFAIL} failed")
if NFAIL == 0:
    print("  VERDICT: ALL CHECKS PASS")
    print("=" * 78)
    sys.exit(0)
else:
    print("  VERDICT: FAILURES PRESENT")
    print("=" * 78)
    sys.exit(1)
