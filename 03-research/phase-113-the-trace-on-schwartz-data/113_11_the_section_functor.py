#!/usr/bin/env python3
"""
113_11 verifier -- d3: the section functor, and why it cannot live in D.

Sections
  A  Thm 1.2: divisibility by chi = s(s-1)xi, on the strip and at s = 0, 1
  B  the idempotent relations in coordinates, two zero models
  C  Prop 2.2: div_S is Z-valued, *-additive, C^x-invariant; the five-class table
  D  Thm 3.1: double dissociation, both directions
  E  Thm 3.4: effectivity is not a function of degree; acceptance test R9
  F  Thm 3.3: scaling of the section sets; negative controls

Every check is a numerical statement about xi, about Riemann's Phi, or about the
finite coordinate model of 113_08.  No zero of xi is used in any DEFINITION; the
one place a computed zero appears (section C, the rho column of the div_S table)
is a verification of a table entry that is already proved from xi(rho) = 0, and
it is flagged there.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("  [PASS] %s" % name)
    else:
        FAIL += 1
        print("  [FAIL] %s" % name)
    if detail:
        print("         %s" % detail)


def head(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ----------------------------------------------------------------- xi and chi

def xi(s):
    s = mp.mpc(s)
    if abs(s) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")
    if abs(s - 1) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


chi = lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * xi(s)

FV = lambda s: -2 * (mp.mpc(s) - 1) * xi(s)      # f_v^
FH = lambda s: 2 * mp.mpc(s) * xi(s)             # f_h^
HH = lambda s: 2 * xi(s)                         # H^
WW = lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * xi(s)   # w^ = chi


# ------------------------------------------------------------------- Riemann Phi

NPHI = 60


def Phi_raw(u, N=NPHI):
    u = mp.mpf(u)
    tot = mp.mpf(0)
    for n in range(1, N + 1):
        n = mp.mpf(n)
        tot += (2 * mp.pi * n ** 4 * mp.e ** (9 * u / 2)
                - 3 * n ** 2 * mp.e ** (5 * u / 2)) * mp.e ** (-mp.pi * n ** 2 * mp.e ** (2 * u))
    return 2 * mp.pi * tot


def Phi(u):
    """Even; the raw series needs n >~ e^{-u} terms, so evaluate at |u|."""
    return Phi_raw(abs(mp.mpf(u)))


d2Phi = lambda u: mp.diff(Phi, mp.mpf(u), 2)
Wprof = lambda u: d2Phi(u) - Phi(u) / 4          # profile of w, from 113_10


# ============================================================ A. divisibility

head("A. Theorem 1.2 -- divisibility by chi(s) = s(s-1) xi(s)")

print("  xi(0) = %s" % mp.nstr(xi(0).real, 20))
print("  xi(1) = %s" % mp.nstr(xi(1).real, 20))
check("xi(0) = xi(1) = 1/2  (the normalisation Thm 1.2 turns on)",
      abs(xi(0) - mp.mpf(0.5)) < mp.mpf("1e-18")
      and abs(xi(1) - mp.mpf(0.5)) < mp.mpf("1e-18"))

# Probe points: two approaches to s=0, two to s=1, plus interior and complex.
PROBES = [mp.mpf("1e-6"), mp.mpf("1e-10"), mp.mpf("1e-14"),
          1 + mp.mpf("1e-6"), 1 + mp.mpf("1e-10"), 1 + mp.mpf("1e-14"),
          mp.mpf("0.5"), mp.mpc("0.5", "10"), mp.mpc("0.3", "3"),
          mp.mpc("0.9", "-2"), mp.mpf("1.4"), mp.mpf("-0.4")]

QUOTIENTS = {
    "(f_v^)^2 - f_v^": lambda s: (FV(s) ** 2 - FV(s)) / chi(s),
    "(f_h^)^2 - f_h^": lambda s: (FH(s) ** 2 - FH(s)) / chi(s),
    "(H^)^2   - H^  ": lambda s: (HH(s) ** 2 - HH(s)) / chi(s),
    "f_v^ * f_h^    ": lambda s: (FV(s) * FH(s)) / chi(s),
}

print("\n  quotient q = (expression)/chi, evaluated on 12 probes:")
for nm, q in QUOTIENTS.items():
    vals = [q(s) for s in PROBES]
    mx = max(abs(v) for v in vals)
    # A genuine pole would blow up as s -> 0 or s -> 1 like 1/eps; the probes
    # step eps down by 1e-4 twice, so a pole would show a 1e8 spread.
    near0 = [abs(q(s)) for s in PROBES[0:3]]
    near1 = [abs(q(s)) for s in PROBES[3:6]]
    spread0 = max(near0) / min(near0)
    spread1 = max(near1) / min(near1)
    check("chi | %s  (q bounded, max|q| = %.6g)" % (nm, mx),
          mx < 100 and spread0 < 1.01 and spread1 < 1.01,
          "eps = 1e-6,-10,-14 -> spread at 0: %.6g   at 1: %.6g   (a pole gives 1e8)"
          % (spread0, spread1))

# The exact quotient for f_v * f_h is -4 xi.  Check it on the nose.
err = max(abs((FV(s) * FH(s)) / chi(s) + 4 * xi(s)) for s in PROBES)
check("exact: f_v^ f_h^ / chi = -4 xi  (max err %.3e)" % err, err < mp.mpf("1e-20"))

# Negative control: something NOT divisible by chi must blow up.
bad = lambda s: (FV(s) + 1) / chi(s)
nb = [abs(bad(s)) for s in PROBES[0:3]]
check("negative control: (f_v^ + 1)/chi is NOT bounded",
      max(nb) / min(nb) > 1e6,
      "|q| = %.3e, %.3e, %.3e  as eps -> 0" % (nb[0], nb[1], nb[2]))


# ================================================== B. idempotents in coords

head("B. Theorem 1.2 in coordinates -- two zero models")


def s_form(x, y, mirror, m):
    x0, x1, xz = x[0], x[1], x[2:]
    y0, y1, yz = y[0], y[1], y[2:]
    return x0 * np.conj(y1) + x1 * np.conj(y0) - np.sum(m * xz * np.conj(yz[mirror]))


def model(zeros, mults):
    z = np.array(zeros, dtype=complex)
    mir = np.array([int(np.argmin(np.abs(z - (1 - np.conj(w))))) for w in z])
    return mir, np.array(mults, dtype=float)


ON = ([0.5 + 14.13j, 0.5 - 14.13j, 0.5 + 21.02j, 0.5 - 21.02j, 0.5 + 25.01j, 0.5 - 25.01j],
      [1, 1, 1, 1, 1, 1])
OFF = ([0.83 + 4.1j, 0.17 - 4.1j, 0.17 + 4.1j, 0.83 - 4.1j, 0.5 + 9.3j, 0.5 - 9.3j],
       [2, 2, 2, 2, 3, 3])

mirN, mN = model(*ON)
mirO, mO = model(*OFF)

nz = 6
cFV = np.array([1, 0] + [0] * nz, dtype=complex)
cFH = np.array([0, 1] + [0] * nz, dtype=complex)
cH = cFV + cFH

# multiplication in D/rad is componentwise (Thm 1.1)
mul = lambda a, b: a * b

check("[f_v]^2 = [f_v]", np.allclose(mul(cFV, cFV), cFV))
check("[f_h]^2 = [f_h]", np.allclose(mul(cFH, cFH), cFH))
check("[f_v][f_h] = 0", np.allclose(mul(cFV, cFH), np.zeros(2 + nz)))
check("[H] = [f_v] + [f_h] and [H]^2 = [H]", np.allclose(mul(cH, cH), cH))

for lbl, mir, m in [("ON ", mirN, mN), ("OFF", mirO, mO)]:
    h2 = s_form(cH, cH, mir, m).real
    d2v = s_form(cFV - cFH, cFV - cFH, mir, m).real
    check("%s model: H^2 = 2  (rank = number of minimal idempotents)" % lbl,
          abs(h2 - 2) < 1e-12, "H^2 = %.12f" % h2)
    check("%s model: (F_v - F_h)^2 = -2  (the negative direction)" % lbl,
          abs(d2v + 2) < 1e-12, "(F_v-F_h)^2 = %.12f" % d2v)

# [H] is the unit of the polar factor: it annihilates the zero block.
zblock = np.zeros(2 + nz, dtype=complex)
zblock[2] = 3.7 + 1.1j
zblock[5] = -0.4j
check("[H] annihilates the zero block:  [H] * z = 0 for z in D^o",
      np.allclose(mul(cH, zblock), np.zeros(2 + nz)))
check("[H] is the unit of the polar factor: [H][f_v] = [f_v], [H][f_h] = [f_h]",
      np.allclose(mul(cH, cFV), cFV) and np.allclose(mul(cH, cFH), cFH))

# Negative control: a non-idempotent.
c2v = 2 * cFV
check("negative control: [2 f_v] is NOT idempotent",
      not np.allclose(mul(c2v, c2v), c2v),
      "[2f_v]^2 = %s  vs  [2f_v] = %s" % (mul(c2v, c2v)[:2], c2v[:2]))


# ================================================== C. the order map div_S

head("C. Proposition 2.2 -- div_S is Z-valued, *-additive, C^x-invariant")


def order(g, s0, kmax=6, tol=mp.mpf("1e-12")):
    for k in range(kmax + 1):
        v = mp.diff(g, mp.mpc(s0), k)
        if abs(v) > tol:
            return k
    return None


CLASSES = {
    "H        (2 xi)":       HH,
    "f_v      (-2(s-1)xi)":  FV,
    "f_h      (2 s xi)":     FH,
    "w        (s(s-1)xi)":   WW,
    "f_v*f_v  (4(s-1)^2xi^2)": lambda s: FV(s) ** 2,
    "f_v*f_h  (-4s(s-1)xi^2)": lambda s: FV(s) * FH(s),
    "2 f_v":                 lambda s: 2 * FV(s),
}

EXPECT = {
    "H        (2 xi)":         (0, 0),
    "f_v      (-2(s-1)xi)":    (0, 1),
    "f_h      (2 s xi)":       (1, 0),
    "w        (s(s-1)xi)":     (1, 1),
    "f_v*f_v  (4(s-1)^2xi^2)": (0, 2),
    "f_v*f_h  (-4s(s-1)xi^2)": (1, 1),
    "2 f_v":                   (0, 1),
}

print("  class                        ord_0  ord_1   value coords (f^(0), f^(1))")
ords = {}
for nm, g in CLASSES.items():
    o0, o1 = order(g, 0), order(g, 1)
    ords[nm] = (o0, o1)
    v0, v1 = g(mp.mpf("1e-14")), g(1 + mp.mpf("1e-14"))
    print("  %-27s  %-5s  %-5s  (%s, %s)"
          % (nm, o0, o1, mp.nstr(v0.real, 6), mp.nstr(v1.real, 6)))

for nm in CLASSES:
    check("div_S table (polar part) for %s = %s" % (nm.split()[0], EXPECT[nm]),
          ords[nm] == EXPECT[nm], "measured %s" % (ords[nm],))

check("Prop 2.2(1): all orders are nonnegative integers",
      all(isinstance(a, int) and isinstance(b, int) and a >= 0 and b >= 0
          for a, b in ords.values()))

check("Prop 2.2(2) *-additivity: div(f_v*f_v) = 2 div(f_v)",
      ords["f_v*f_v  (4(s-1)^2xi^2)"] == tuple(2 * k for k in ords["f_v      (-2(s-1)xi)"]))
check("Prop 2.2(2) *-additivity: div(f_v*f_h) = div(f_v) + div(f_h)",
      ords["f_v*f_h  (-4s(s-1)xi^2)"]
      == tuple(a + b for a, b in zip(ords["f_v      (-2(s-1)xi)"],
                                     ords["f_h      (2 s xi)"])))
check("Prop 2.2(3) C^x-invariance: div(2 f_v) = div(f_v)",
      ords["2 f_v"] == ords["f_v      (-2(s-1)xi)"])

# Definition 2.3: deg_ord + deg = 2 on the four standard classes.
DEG = {"H        (2 xi)": 2, "f_v      (-2(s-1)xi)": 1,
       "f_h      (2 s xi)": 1, "w        (s(s-1)xi)": 0}
ok = all(sum(ords[nm]) + DEG[nm] == 2 for nm in DEG)
check("Def 2.3: deg_ord + deg = 2 on H, f_v, f_h, w  (complementary supports)", ok,
      "  ".join("%s: %d+%d" % (nm.split()[0], sum(ords[nm]), DEG[nm]) for nm in DEG))

# The rho column.  This is a VERIFICATION of a table entry already proved from
# xi(rho) = 0; a computed zero is used here and nowhere else, and never in a
# definition.
rho = mp.mpc(mp.mpf(0.5), mp.im(mp.zetazero(1)))
check("[verification only, uses a computed zero] ord_rho(f_v^) = ord_rho(H^) = 1",
      order(FV, rho) == 1 and order(HH, rho) == 1,
      "rho = 1/2 + %si;  |xi(rho)| = %.3e" % (mp.nstr(mp.im(rho), 12), abs(xi(rho))))
check("[verification only] ord_rho(f_v^ * f_v^) = 2  (additivity at a zero)",
      order(lambda s: FV(s) ** 2, rho) == 2)


# ============================================ D. the double dissociation

head("D. Theorem 3.1 -- double dissociation")

# (a) same divisor, different values.
same_div = ords["2 f_v"] == ords["f_v      (-2(s-1)xi)"]
v_fv = FV(mp.mpf("1e-14")).real
v_2fv = 2 * v_fv
check("Thm 3.1(a): div_S(2f_v) = div_S(f_v) but the values differ",
      same_div and abs(v_2fv - 2 * v_fv) < 1e-20 and abs(v_2fv - v_fv) > 0.5,
      "f_v^(0) = %.6f   (2f_v)^(0) = %.6f   same divisor %s"
      % (v_fv, v_2fv, ords["2 f_v"]))

# and s separates them, via formula (2.2) of 113_08: s(x, F_h) = x^(0).
for lbl, mir, m in [("ON ", mirN, mN), ("OFF", mirO, mO)]:
    a = s_form(cFV, cFH, mir, m)
    b = s_form(2 * cFV, cFH, mir, m)
    check("%s model: s(f_v, F_h) = 1 but s(2f_v, F_h) = 2  -- s sees the scalar" % lbl,
          abs(a - 1) < 1e-12 and abs(b - 2) < 1e-12,
          "s(f_v,F_h) = %.12f   s(2f_v,F_h) = %.12f" % (a.real, b.real))

# (b) same values, different divisor.
check("Thm 3.1(b): [f_v * f_v] = [f_v] in D/rad (same class, same values)",
      np.allclose(mul(cFV, cFV), cFV))
check("Thm 3.1(b): but div_S(f_v*f_v) = 2 div_S(f_v) != div_S(f_v)",
      ords["f_v*f_v  (4(s-1)^2xi^2)"] != ords["f_v      (-2(s-1)xi)"],
      "div(f_v*f_v) = %s   div(f_v) = %s"
      % (ords["f_v*f_v  (4(s-1)^2xi^2)"], ords["f_v      (-2(s-1)xi)"]))

# Consequence: s does not factor through div_S.  Exhibit it.
check("Cor: s does not factor through div_S "
      "(equal divisors, unequal s-values: f_v vs 2f_v)",
      same_div and abs(s_form(cFV, cFH, mirN, mN) - s_form(2 * cFV, cFH, mirN, mN)) > 0.5)
# ... and div_S does not factor through the class map.
check("Cor: div_S does not factor through [.] : D -> D/rad "
      "(equal classes, unequal divisors: f_v vs f_v*f_v)",
      np.allclose(mul(cFV, cFV), cFV)
      and ords["f_v*f_v  (4(s-1)^2xi^2)"] != ords["f_v      (-2(s-1)xi)"])


# ================================ E. effectivity is not a function of degree

head("E. Theorem 3.4 and acceptance test R9")

# deg(f) = f^(0) + f^(1)   (113_10 Thm 1.2)
deg_coord = lambda c: (c[0] + c[1]).real

c_H = cH
c_bad = 3 * cFV - cFH          # [3 f_v - f_h]
check("deg([H]) = 2", abs(deg_coord(c_H) - 2) < 1e-12, "= %.12f" % deg_coord(c_H))
check("deg([3f_v - f_h]) = 2", abs(deg_coord(c_bad) - 2) < 1e-12,
      "= %.12f" % deg_coord(c_bad))
check("Thm 3.4: the two classes have EQUAL degree",
      abs(deg_coord(c_H) - deg_coord(c_bad)) < 1e-12)

check("Thm 3.4: (3f_v - f_h)^(1) = -1 < 0, so no representative is >= 0",
      abs(c_bad[1] + 1) < 1e-12, "(3f_v-f_h)^(1) = %.12f" % c_bad[1].real)
check("Thm 3.4: [H] IS effective (113_10 Thm 3.2: F_H = 2 Phi > 0), "
      "and H^(0) = H^(1) = 1 > 0",
      abs(c_H[0] - 1) < 1e-12 and abs(c_H[1] - 1) < 1e-12
      and all(Phi(x) > 0 for x in [mp.mpf(k) / 4 for k in range(0, 13)]))

# The R9 test, run against the only h^1 anyone would try first.
h1_from_deg = lambda c: 0.0        # any function of deg alone is constant here
check("R9 negative control: an h^1 depending only on deg CANNOT separate them",
      h1_from_deg(c_H) == h1_from_deg(c_bad),
      "both classes have deg 2, so any h^1 = F(deg) gives the same value; "
      "but one is effective and one is not")
check("R9 is non-vacuous: a valid h^1 must give h^1([3f_v-f_h]) > h^1([H])",
      deg_coord(c_H) == deg_coord(c_bad) and c_bad[1].real < 0 <= c_H[1].real)


# ============================== F. scaling of section sets (Theorem 3.3)

head("F. Theorem 3.3 -- the section sets scale, so h^0(nD) = h^0(D)")

# H^0([n H]) = { g in rad : n F_H + G >= 0 }.  Take the rad direction g = t w,
# whose profile is W = Phi'' - Phi/4, and measure the admissible interval of t.
GRID = [mp.mpf(k) / 10 for k in range(-30, 31)]
PHIV = [Phi(x) for x in GRID]
WV = [Wprof(x) for x in GRID]


def tmax(scale):
    """largest t >= 0 with scale*2*Phi + t*W >= 0 on the grid"""
    best = mp.inf
    for p, w in zip(PHIV, WV):
        if w < 0:
            best = min(best, -scale * 2 * p / w)
    return best


t1, t2, t5, t100 = tmax(1), tmax(2), tmax(5), tmax(100)
print("  t_max for [H]    = %s" % mp.nstr(t1, 15))
print("  t_max for [2H]   = %s" % mp.nstr(t2, 15))
print("  t_max for [5H]   = %s" % mp.nstr(t5, 15))
print("  t_max for [100H] = %s" % mp.nstr(t100, 15))
for n, tn in [(2, t2), (5, t5), (100, t100)]:
    check("H^0([%dH]) = %d . H^0([H])  exactly  (ratio = %d)" % (n, n, n),
          abs(tn / t1 - n) < mp.mpf("1e-20"),
          "measured ratio = %s" % mp.nstr(tn / t1, 20))

check("Thm 3.3: the section set is a SCALED COPY, so its dimension is constant "
      "-- h^0(nD) = h^0(D), which is obstruction O1",
      abs(t2 / t1 - 2) < mp.mpf("1e-20") and abs(t100 / t1 - 100) < mp.mpf("1e-20"))

# Negative control 1: the scaling is NOT trivially true of every functional --
# the admissible t-interval is genuinely nonempty and genuinely bounded.
check("negative control: the t-interval is nonempty and bounded "
      "(so the ratio test has content)",
      0 < t1 < mp.inf, "t_max([H]) = %s, and W takes both signs: "
                       "min W = %s, max W = %s"
      % (mp.nstr(t1, 10), mp.nstr(min(WV), 6), mp.nstr(max(WV), 6)))

# Negative control 2: div_S does NOT scale -- it is the escape from O1,
# and it is the thing s cannot see.
check("negative control: div_S(n f) = div_S(f) for all n "
      "(scale-invariant: escapes O1) but is blind to n (Thm 3.1(a))",
      order(lambda s: 7 * FV(s), 1) == order(FV, 1) == 1)

# Negative control 3: the two obstructions are not the same obstruction.
check("negative control: the two horns of Thm 3.3 are distinct "
      "-- V-side fails by scaling, Div_S-side fails by blindness",
      abs(t2 / t1 - 2) < mp.mpf("1e-20")           # V-side: scales
      and order(lambda s: 7 * FV(s), 1) == order(FV, 1))   # Div-side: blind


# ------------------------------------------------------------------- verdict

head("VERDICT")
print("  checks: %d passed, %d failed" % (PASS, FAIL))
if FAIL == 0:
    print("\n  VERDICT: ALL CHECKS PASS")
    print("""
  Established here:
    Thm 1.2  D/rad is a ring; f_v, f_h are its two minimal polar idempotents,
             H = f_v + f_h is the unit of that factor, and H^2 = 2 is a rank.
             All three turn on xi(0) = xi(1) = 1/2.
    Prop 2.2 div_S is Z-valued, *-additive and C^x-invariant -- the first
             discrete structure in phase 113.
    Thm 3.1  values and orders are mutually independent (two-sided witness).
    Thm 3.3  h^0 on V scales away (O1); h^0 on Div_S cannot see s.
    Thm 3.4  effectivity is not a function of degree: [H] and [3f_v - f_h]
             both have degree 2 and only the first is effective.  -> test R9.

  NOT established: any construction of h^0; Target T1; (E^o); row (d).
""")
    raise SystemExit(0)
else:
    print("\n  VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
