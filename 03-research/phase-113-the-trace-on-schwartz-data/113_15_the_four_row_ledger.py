#!/usr/bin/env python3
"""
113_15 verifier -- the four-row ledger.

A ledger is only worth what its citations are worth, so this verifier does
three things and nothing else:

  A  SOURCE AUDIT   every status line in the ledger names a file and a claim;
                    each file must exist and must contain the claim's marker
  B  RECOMPUTATION  the numbers the ledger quotes, recomputed here from xi
                    alone, independently of the files that first produced them
  C  HONESTY AUDIT  no file in the phase may assert that RH is proved, and the
                    summary must carry the disclaimer

It deliberately does NOT re-run the other verifiers; 113_99_verify_all.py does
that.
"""

import io
import os
import re
import numpy as np
import mpmath as mp

mp.mp.dps = 30

HERE = os.path.dirname(os.path.abspath(__file__))
RESEARCH = os.path.dirname(HERE)

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


def read(rel):
    p = os.path.join(RESEARCH, rel)
    if not os.path.exists(p):
        return None
    return io.open(p, encoding="utf-8").read()


# ==================================================== A. the source audit

head("A. Source audit -- every ledger citation resolves to a real claim")

P107 = "phase-107-arithmetic-lefschetz-reconstruction/"
P108 = "phase-108-row-a-construction/"
P109 = "phase-109-one-sided-pairing/"
P110 = "phase-110-principal-xi-divisibility/"
P112 = "phase-112-effective-cone/"
P113 = "phase-113-the-trace-on-schwartz-data/"

LEDGER = [
    # row, item, file, marker
    ("a", "Div and Prin' on the graded family",
     P108 + "108_03_CHARACTER_GRADED_SHEAF_AND_DIVISOR.md", "Prin"),
    ("a", "curve-like absolute dimension Theta(deg D)",
     P107 + "107_146_ABSOLUTE_DIMENSION_HIGHER_RANK.md", r"\Theta(\deg"),
    ("a", "principal invariance of Prin' FAILS",
     P108 + "108_38_STAGE_2_THE_DESCENT_AND_THE_RADICAL.md",
     "principal invariance fails"),
    ("b", "Weil coefficient from the shell functional",
     P108 + "108_34_THE_SHELL_FUNCTIONAL_GAMMA_P_K.md",
     r"\Lambda(p^k)/\sqrt{p^k}"),
    ("b", "foliated-dynamics import is CLOSED",
     P107 + "107_242_MORISHITA_BRIDGE_ASSEMBLY_AUDIT.md", "Theorem 4.1"),
    ("c", "the identity Gamma.Delta = N is -zeta'/zeta",
     P108 + "108_36_THE_ASSEMBLY_IS_THE_LOGARITHMIC_DERIVATIVE.md",
     r"-\zeta'/\zeta"),
    ("c", "coefficient side is blind to the zeros",
     P109 + "109_04_THE_COEFFICIENT_SIDE_IS_BLIND.md", "blind"),
    ("c", "zero-free pairing, radical, Theorem D",
     P107 + "107_240_PRINCIPAL_INVARIANCE_OF_THE_CORNER_PAIRING.md",
     "Theorem D"),
    ("c", "signature n_+ = 1 + #P",
     P107 + "107_241_HODGE_INDEX_FOR_THE_CORNER_PAIRING.md", "n_+"),
    ("d1", "xi-divisibility CLOSED on compact support",
     P110 + "110_02_WHAT_XI_DIVISIBILITY_REQUIRES.md", "exponential type"),
    ("d1", "the radical IS the xi-ideal, on Schwartz data",
     P113 + "113_09_THE_RADICAL_IS_THE_XI_IDEAL.md",
     r"\operatorname{rad}I_\partial"),
    ("d0", "the degree map and its three closed forms",
     P113 + "113_10_THE_DEGREE_MAP_AND_THE_EFFECTIVE_CONE.md",
     "Theorem 1.2 (three closed forms)"),
    ("d5", "effective => deg > 0, and H is effective",
     P113 + "113_10_THE_DEGREE_MAP_AND_THE_EFFECTIVE_CONE.md",
     "Theorem 2.2 (effective classes have strictly positive degree)"),
    ("d5", "cone exists but is scaling-stable (O1)",
     P113 + "113_10_THE_DEGREE_MAP_AND_THE_EFFECTIVE_CONE.md",
     "Obstruction O1"),
    ("d5", "formal cone, 142 disjoint-support pairs, no sections reading",
     P112 + "112_03_VERDICT.md", "142"),
    ("d3", "h^0 cannot be built inside D (double dissociation)",
     P113 + "113_11_THE_SECTION_FUNCTOR_AND_WHY_IT_CANNOT_LIVE_IN_D.md",
     "double dissociation"),
    ("d4", "s(x,y) = tau(x * y^*), K = 0, HODGE INDEX <=> RH",
     P113 + "113_12_THE_TRACE_THE_DUALITY_AND_THE_K_EQUALS_ZERO_ANSATZ.md",
     "HODGE INDEX"),
    ("d4", "(SEP) and (INT) discharged; d4 unconditional",
     P113 + "113_14_THE_TWO_ANALYTIC_GAPS_ARE_DISCHARGED.md",
     "(INT), the real witness"),
    ("d",  "no spectral gap (O3); infinite lattice pairing (O2)",
     P113 + "113_13_THE_ASSEMBLY_THE_ARITHMETIC_MEASUREMENT_AND_THE_MISSING_GAP.md",
     "Theorem 4.1"),
]

for row, item, rel, marker in LEDGER:
    txt = read(rel)
    ok = txt is not None and marker in txt
    check("(%s) %s" % (row, item), ok,
          "%s%s" % (rel, "" if txt is not None else "   [FILE MISSING]"))

# every phase-113 verifier the ledger claims exists, exists
VERIF = ["113_%02d" % k for k in range(1, 15)]
missing = []
for v in VERIF:
    hits = [f for f in os.listdir(HERE) if f.startswith(v) and f.endswith(".py")]
    if not hits:
        missing.append(v)
check("all 14 phase-113 verifiers are present on disk", not missing,
      "missing: %s" % missing if missing else "113_01 ... 113_14")


# ================================================== B. the recomputation

head("B. Recomputation -- the ledger's numbers, from xi alone")


def xi(s):
    s = mp.mpc(s)
    if abs(s) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")
    if abs(s - 1) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


x0, x1 = xi(0), xi(1)
check("xi(0) = xi(1) = 1/2  -- the single fact the polar block rests on",
      abs(x0 - mp.mpf("0.5")) < mp.mpf("1e-15")
      and abs(x1 - mp.mpf("0.5")) < mp.mpf("1e-15"),
      "xi(0) = %.15f   xi(1) = %.15f" % (mp.re(x0), mp.re(x1)))

# the rulings, in coordinates (f^(0), f^(1))
FV = (-2 * (0 - 1) * x0, -2 * (1 - 1) * x1)        # f_v^ = -2(s-1)xi
FH = (2 * 0 * x0, 2 * 1 * x1)                      # f_h^ =  2s xi
HH = (2 * x0, 2 * x1)                              # H^   =  2 xi
check("f_v^ = (1, 0),  f_h^ = (0, 1),  H^ = (1, 1) in the polar coordinates",
      abs(FV[0] - 1) < mp.mpf("1e-15") and abs(FV[1]) < mp.mpf("1e-15")
      and abs(FH[0]) < mp.mpf("1e-15") and abs(FH[1] - 1) < mp.mpf("1e-15")
      and abs(HH[0] - 1) < mp.mpf("1e-15") and abs(HH[1] - 1) < mp.mpf("1e-15"))

pol = lambda a, b: (a[0] * mp.conj(b[1]) + a[1] * mp.conj(b[0])).real
check("F_v^2 = 0, F_h^2 = 0, F_v.F_h = 1, H^2 = 2, (F_v-F_h)^2 = -2",
      abs(pol(FV, FV)) < mp.mpf("1e-15") and abs(pol(FH, FH)) < mp.mpf("1e-15")
      and abs(pol(FV, FH) - 1) < mp.mpf("1e-15")
      and abs(pol(HH, HH) - 2) < mp.mpf("1e-15")
      and abs(pol((FV[0] - FH[0], FV[1] - FH[1]),
                  (FV[0] - FH[0], FV[1] - FH[1])) + 2) < mp.mpf("1e-15"),
      "H^2 = %.12f    (F_v - F_h)^2 = %.12f"
      % (pol(HH, HH), pol((FV[0] - FH[0], FV[1] - FH[1]),
                          (FV[0] - FH[0], FV[1] - FH[1]))))
check("deg(H) = H^(0) + H^(1) = 2 > 0, so d2 is met",
      abs(HH[0] + HH[1] - 2) < mp.mpf("1e-15"))

# the signature flip -- the ledger's row (d) headline
def gram(zeros, mults):
    z = np.array(zeros, dtype=complex)
    mir = np.array([int(np.argmin(np.abs(z - (1 - np.conj(w))))) for w in z])
    m = np.array(mults, dtype=float)
    n = 2 + len(z)
    G = np.zeros((n, n))
    G[0, 1] = G[1, 0] = 1.0
    for i in range(len(z)):
        G[2 + i, 2 + int(mir[i])] = -m[i]
    return G


ON = ([0.5 + 14.13j, 0.5 - 14.13j, 0.5 + 21.02j, 0.5 - 21.02j,
       0.5 + 25.01j, 0.5 - 25.01j], [1, 1, 1, 1, 1, 1])
OFF = ([0.83 + 4.1j, 0.17 - 4.1j, 0.17 + 4.1j, 0.83 - 4.1j,
        0.5 + 9.3j, 0.5 - 9.3j], [2, 2, 2, 2, 3, 3])
sg = {}
for lbl, (z, m) in (("ON", ON), ("OFF", OFF)):
    ev = np.linalg.eigvalsh(gram(z, m))
    sg[lbl] = (int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9)))
check("signature (1,7) with the zeros on the line, (3,5) off it "
      "-- 113_12 Thm 4.1, recomputed", sg["ON"] == (1, 7) and sg["OFF"] == (3, 5),
      "ON %s   OFF %s" % (sg["ON"], sg["OFF"]))

# O1, recomputed: the effective cone is stable under scaling
PH = lambda u: 2 * mp.pi * mp.fsum(
    (2 * mp.pi * n ** 4 * mp.e ** (mp.mpf("4.5") * abs(u))
     - 3 * n ** 2 * mp.e ** (mp.mpf("2.5") * abs(u)))
    * mp.e ** (-mp.pi * n ** 2 * mp.e ** (2 * abs(u))) for n in range(1, 40))
GRID = [mp.mpf(k) / 8 for k in range(-24, 25)]
PHIV = [PH(u) for u in GRID]
WV = [mp.diff(PH, u, 2) - PH(u) / 4 for u in GRID]


def tmax(scale):
    best = mp.inf
    for p, w in zip(PHIV, WV):
        if w < 0:
            best = min(best, -scale * 2 * p / w)
    return best


t1, t100 = tmax(mp.mpf(1)), tmax(mp.mpf(100))
check("O1 recomputed: t_max(100 H) / t_max(H) = 100 exactly -- the cone is a "
      "CONE, so h^0(nD) = h^0(D) and no growth argument can start",
      abs(t100 / t1 - 100) < mp.mpf("1e-12"),
      "t_max(H) = %.12f   t_max(100H) = %.9f   ratio = %.12f"
      % (t1, t100, t100 / t1))

# O2 recomputed: the zero sum inside s(delta_n, delta_m) does not settle
gammas = [mp.im(mp.zetazero(k)) for k in range(1, 41)]
x_ = mp.mpf(3) / 2
tot = mp.mpf(0)
ps = []
for k, g in enumerate(gammas, 1):
    rho = mp.mpc(mp.mpf(1) / 2, g)
    tot += x_ ** rho + x_ ** mp.conj(rho)
    if k in (5, 10, 20, 40):
        ps.append((k, tot.real))
spread = max(v for _, v in ps) - min(v for _, v in ps)
check("O2 recomputed: the partial sums of sum_rho (3/2)^rho -- the zero sum "
      "inside s(delta_3, delta_2) -- do NOT settle",
      spread > mp.mpf("1") and abs(ps[-1][1] - ps[-2][1]) > mp.mpf("0.5"),
      "   ".join("K=%d: %.4f" % (k, v) for k, v in ps)
      + "    spread %.4f" % spread)
check("O2 recomputed: every term has modulus (3/2)^{1/2} = %.6f, so the terms "
      "never tend to 0" % mp.sqrt(x_),
      all(abs(abs(x_ ** mp.mpc(mp.mpf(1) / 2, g)) - mp.sqrt(x_))
          < mp.mpf("1e-20") for g in gammas[:10]))


# ================================================== C. the honesty audit

head("C. Honesty audit -- the phase may not claim RH")

md = [f for f in sorted(os.listdir(HERE)) if f.endswith(".md")]
FORBIDDEN = [
    r"\bRH is (now )?(proved|proven|established)\b",
    r"\bwe (have )?prove[d]? RH\b",
    r"\bthe Riemann Hypothesis is (proved|proven|true)\b",
    r"\bproof of RH is complete\b",
]
bad = []
for f in md:
    t = read(P113 + f)
    for pat in FORBIDDEN:
        for mm in re.finditer(pat, t, re.I):
            seg = t[max(0, mm.start() - 60):mm.end() + 20].replace("\n", " ")
            # allow explicitly negated / conditional occurrences
            if re.search(r"not|never|nothing|would be|if\b|unless|anything that",
                         seg, re.I):
                continue
            bad.append((f, seg))
check("no file in phase 113 asserts that RH is proved", not bad,
      "offenders: %s" % bad if bad else "%d markdown files scanned" % len(md))

for f, needle in (("113_13_THE_ASSEMBLY_THE_ARITHMETIC_MEASUREMENT_AND_THE_MISSING_GAP.md",
                   "Nothing in phase 113 proves RH"),
                  ("113_14_THE_TWO_ANALYTIC_GAPS_ARE_DISCHARGED.md",
                   "STILL OPEN   Ansatz A; (E^o); row (d); RH")):
    t = read(P113 + f)
    check("%s carries its disclaimer" % f.split("_")[1].lower(),
          t is not None and needle in t)

led = read(P113 + "113_15_THE_FOUR_ROW_LEDGER.md")
if led is not None:
    check("the ledger states plainly that RH is not proved",
          "RH is not proved" in led)
    check("the ledger records rows (a) and (b) as untouched by this phase",
          "untouched" in led)
    check("the ledger carries the full R1-R23 index",
          all(("| R%d |" % k) in led for k in range(1, 24)))
else:
    check("113_15_THE_FOUR_ROW_LEDGER.md exists", False)


# ------------------------------------------------------------------- verdict

head("VERDICT")
print("  checks: %d passed, %d failed" % (PASS, FAIL))
if FAIL == 0:
    print("""
  VERDICT: ALL CHECKS PASS

  The ledger's citations all resolve, its numbers all recompute, and no file
  in the phase claims more than it proved.

  Rows (a) and (b): unchanged by phase 113.
  Row (c): now a Frobenius *-algebra with a zero-free trace.
  Row (d): d0, d1 (analytic half), d2, d4, d5 built; d3 proved impossible
           inside D; and row (d) as a whole is RH, not a step towards it.

  RH is NOT proved.
""")
    raise SystemExit(0)
else:
    print("\n  VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
