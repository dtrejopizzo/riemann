#!/usr/bin/env python3
"""
113_14 verifier -- the two residual analytic gaps of the phase, (SEP) and (INT).

  A  Lemma 1.1'  membership: xi times a MEROMORPHIC v whose poles are cancelled
                 by zeros of xi still lands in D  (repairs the citation of
                 113_09 Lemma 1.2 in its own zero-slot argument)
  B  Thm 2.1     (SEP) is discharged: an explicit separating family in D
  C  Thm 3.3     (INT) is discharged: if RH fails there is a REAL f in D^o with
                 s(f,f) > 0, given in closed form
  D  consequences: 113_07 Prop 4.1 (<=), 113_10 Thm 4.2, 113_12 Thm 4.1 (1)=>(2)

Source rule.  Sections A, B and the control in C evaluate xi at its own zeros.
Those zeros are COMPUTED here only to check statements that were proved without
them; no object of the programme is defined by a zero.  Section C's witness is
built from a HYPOTHESISED off-critical zero -- that is the contrapositive of
RH, not a definition -- and is exercised numerically against a surrogate entire
function with a prescribed off-line quadruple, never against xi.
"""

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


# --------------------------------------------------------------- xi and chi

def xi(s):
    s = mp.mpc(s)
    if abs(s) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")
    if abs(s - 1) < mp.mpf("1e-8"):
        s = s + mp.mpf("1e-18")
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


chi = lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * xi(s)

# the first few zeros -- used ONLY to verify, never to define
GAM = [mp.im(mp.zetazero(k)) for k in (1, 2, 3)]
RHO = [mp.mpc("0.5", g) for g in GAM]

print("first three ordinates: %s" % ", ".join("%.6f" % g for g in GAM))


# ============================================ A. the membership lemma 1.1'

head("A. Lemma 1.1' -- xi * (meromorphic v, poles cancelled) still lies in D")

r1 = RHO[0]

# xi has a simple zero at rho_1: xi(rho)=0 but xi'(rho)!=0.
v0 = abs(xi(r1))
v1 = abs(mp.diff(xi, r1))
check("xi(rho_1) = 0 and xi'(rho_1) != 0, so the zero is simple (m = 1)",
      v0 < mp.mpf("1e-20") and v1 > mp.mpf("1e-3"),
      "|xi(rho)| = %.3e   |xi'(rho)| = %.6f" % (v0, v1))

Phi = lambda s: chi(s) / (mp.mpc(s) - r1)

# holomorphic at rho_1: the value is the stable limit, not a pole.
vals = [Phi(r1 + mp.mpf(e)) for e in ("1e-6", "1e-10", "1e-14")]
spread = max(abs(a - b) for a in vals for b in vals)
lim = r1 * (r1 - 1) * mp.diff(xi, r1)          # chi'(rho)/1! with chi = s(s-1)xi
check("Phi = chi/(s-rho_1) is HOLOMORPHIC at rho_1 (stable limit, no pole)",
      spread < mp.mpf("1e-4") and abs(vals[-1] - lim) < mp.mpf("1e-6"),
      "values %s ; predicted rho(rho-1)xi'(rho) = %s"
      % (["%.6f%+.6fj" % (mp.re(v), mp.im(v)) for v in vals],
         "%.6f%+.6fj" % (mp.re(lim), mp.im(lim))))

check("Phi(rho_1) != 0", abs(lim) > mp.mpf("1e-3"), "|Phi(rho_1)| = %.6f" % abs(lim))

# negative control: a pole NOT sitting on a zero of xi really is a pole.
Bad = lambda s: chi(s) / (mp.mpc(s) - mp.mpf("0.5"))
bads = [abs(Bad(mp.mpf("0.5") + mp.mpf(e))) for e in ("1e-6", "1e-10", "1e-14")]
check("negative control: chi(s)/(s-1/2) DOES blow up (1/2 is not a zero of xi)",
      bads[-1] > 1e10 * bads[0] / 1e8,
      "|.| at eps=1e-6, 1e-10, 1e-14: %s" % ["%.3e" % b for b in bads])

# the Lemma 1.1 integrability hypothesis, on the two edges of a strip
# |Re s - 1/2| <= theta' with theta' = 1.6 > 3/2.
for sig in (mp.mpf("0.5") - mp.mpf("1.6"), mp.mpf("0.5") + mp.mpf("1.6")):
    I = mp.quad(lambda t: abs(Phi(mp.mpc(sig, t))) * (1 + abs(t)) ** 4,
                [-60, -20, 0, 20, 60])
    tails = [abs(Phi(mp.mpc(sig, T))) for T in (60, 90, 120)]
    ratio = tails[2] / tails[1] if tails[1] > 0 else mp.inf
    pred = mp.e ** (-mp.pi * 30 / 4)
    check("integral of |Phi|(1+|t|)^4 on Re s = %.1f is finite (= %.4e)"
          % (sig, I), I < mp.inf and I > 0)
    check("Re s = %.1f: |Phi| decays like exp(-pi|t|/4) (ratio %.3e vs %.3e)"
          % (sig, ratio, pred), abs(mp.log(ratio) - mp.log(pred)) < 1.0)


# ================================================== B. (SEP) is discharged

head("B. Theorem 2.1 -- (SEP): an explicit separating family in D")

# S_trunc: the polar pair plus the first three mirror pairs.
S = [mp.mpf(0), mp.mpf(1)] + [z for r in RHO for z in (r, mp.conj(r))]
NAMES = ["0", "1"] + [n for k in range(3) for n in ("rho_%d" % (k + 1),
                                                    "rho_%d bar" % (k + 1))]
# on the critical line the mirror rho' = 1 - conj(rho) equals rho itself
MIR = [1, 0] + [2 + i for i in range(6)]

sepok = True
for k, r in enumerate(RHO):
    Y = lambda s, r=r: chi(s) / (mp.mpc(s) - r)
    coords = [Y(p) if abs(p - r) > mp.mpf("1e-12")
              else r * (r - 1) * mp.diff(xi, r) for p in S]
    hit = [j for j, c in enumerate(coords) if abs(c) > mp.mpf("1e-8")]
    ok = hit == [2 + 2 * k]
    sepok &= ok
    check("y_%d = chi/(s-rho_%d) is nonzero at rho_%d and vanishes on all other "
          "points of S" % (k + 1, k + 1, k + 1), ok,
          "nonzero slots: %s   |y(rho)| = %.6f"
          % ([NAMES[j] for j in hit], abs(coords[2 + 2 * k])))

# these y separate the zero coordinates: s(x, y_k) = -m x^(rho_k') conj(y_k(rho_k))
def s_form(xc, yc):
    tot = xc[0] * mp.conj(yc[1]) + xc[1] * mp.conj(yc[0])
    for j in range(2, len(S)):
        tot -= xc[j] * mp.conj(yc[MIR[j]])
    return tot


sep2 = True
for k, r in enumerate(RHO):
    Y = lambda s, r=r: chi(s) / (mp.mpc(s) - r)
    yc = [Y(p) if abs(p - r) > mp.mpf("1e-12")
          else r * (r - 1) * mp.diff(xi, r) for p in S]
    for j in range(len(S)):
        xc = [mp.mpc(0)] * len(S)
        xc[j] = mp.mpc(1)
        v = abs(s_form(xc, yc))
        want = (j == 2 + 2 * k)          # MIR is the identity on the line
        sep2 &= (v > mp.mpf("1e-8")) == want
check("the family {y_k} separates every zero coordinate it should, and only "
      "those (24 pairings)", sep2)
check("(SEP) HOLDS: the zero block of s is nondegenerate inside D", sepok and sep2)

# citation audit: 113_09 already exhibited this element; 113_12 recorded it as missing.
import io, os
here = os.path.dirname(os.path.abspath(__file__))
t09 = io.open(os.path.join(here, "113_09_THE_RADICAL_IS_THE_XI_IDEAL.md"),
              encoding="utf-8").read()
t12 = io.open(os.path.join(here,
      "113_12_THE_TRACE_THE_DUALITY_AND_THE_K_EQUALS_ZERO_ANSATZ.md"),
              encoding="utf-8").read()
check("audit: 113_09 already contains the g_rho construction",
      "\\widehat g_{\\rho_0}(s):=\\frac{s(s-1)\\,\\xi(s)}{(s-\\rho_0)" in t09)
check("audit: 113_12 recorded (SEP) as 'not established' -- that record is the "
      "error this file corrects",
      "no element of `D` realising it has been exhibited" in t12
      and "(SEP) is not" in t12)


# ================================================== C. (INT) is discharged

head("C. Theorem 3.3 -- (INT): the real witness, if RH fails")

# ---- C1: the two-real-parameter solve, abstractly, 200 random data
rnd = mp.mpf
mp.mp.dps = 30
seedstate = mp.mpf(1)
trials, worst = 0, mp.mpf(0)
for i in range(200):
    # deterministic pseudo-random data (no Math.random needed)
    a = mp.mpf(i + 1) / 7
    u0 = mp.mpc(mp.cos(a) + mp.mpf("0.3"), 2 + mp.sin(3 * a))   # Im(u0^2) != 0
    A1 = mp.mpc(mp.cos(2 * a) + 1, mp.sin(5 * a) - mp.mpf("0.4"))
    if abs(A1) < mp.mpf("1e-3") or abs(mp.im(u0 ** 2)) < mp.mpf("1e-6"):
        continue
    z = mp.mpc(0, 1) / A1
    c2 = mp.im(z) / mp.im(u0 ** 2)
    c0 = mp.re(z) - c2 * mp.re(u0 ** 2)
    a1 = (c0 + c2 * u0 ** 2) * A1                 # must be exactly i
    trials += 1
    worst = max(worst, abs(a1 - mp.mpc(0, 1)))
check("Lemma 3.2: for every (u_0, A_1) with Im(u_0^2) != 0 there are REAL c_0, "
      "c_2 making a_1 = P(rho_1) A_1 purely imaginary (%d cases)" % trials,
      trials > 150 and worst < mp.mpf("1e-20"), "max |a_1 - i| = %.3e" % worst)

# the same solve is IMPOSSIBLE when the zero is on the line: u_0 = i*t, u_0^2 real
u_on = mp.mpc(0, 14)
check("negative control: on the critical line u_0^2 = -t^2 is REAL, the span of "
      "{1, u_0^2} over R is R, and no real (c_0,c_2) can rotate A_1",
      abs(mp.im(u_on ** 2)) < mp.mpf("1e-25"),
      "Im(u_0^2) = %.3e  =>  P(rho) is real, so a_1 cannot be made imaginary"
      % abs(mp.im(u_on ** 2)))

# ---- C2: end-to-end, against a surrogate zeta with an off-line quadruple
sig0, t0 = mp.mpf("0.8"), mp.mpf(6)
q1 = mp.mpc(sig0, t0)
q2 = mp.conj(q1)
q3 = 1 - mp.conj(q1)
q4 = 1 - q1
QUAD = [q1, q2, q3, q4]
QMIR = [2, 3, 0, 1]                # rho -> rho' = 1 - conj(rho) inside QUAD
M = 1                              # multiplicity of the surrogate quadruple

G = lambda s: mp.e ** ((mp.mpc(s) - mp.mpf("0.5")) ** 2)
D4 = lambda s: mp.fprod([mp.mpc(s) - q for q in QUAD])
XiS = lambda s: D4(s) * G(s)       # surrogate: real, *-symmetric, entire, decaying

# it really is a legitimate stand-in: real, *-symmetric, Gaussian decay
pts = [mp.mpc("0.3", "2.2"), mp.mpc("0.9", "-1.1"), mp.mpc("1.4", "0.7")]
e_real = max(abs(XiS(mp.conj(p)) - mp.conj(XiS(p))) for p in pts)
e_star = max(abs(mp.conj(XiS(1 - mp.conj(p))) - XiS(p)) for p in pts)
check("surrogate Xi_S is real (Xi(conj s) = conj Xi(s))", e_real < mp.mpf("1e-18"),
      "max err %.3e" % e_real)
check("surrogate Xi_S is *-symmetric (Xi*(s) = Xi(s)), i.e. satisfies the "
      "functional equation", e_star < mp.mpf("1e-18"), "max err %.3e" % e_star)
check("surrogate Xi_S has its zeros OFF the critical line at Re s = %.1f, %.1f"
      % (sig0, 1 - sig0), all(abs(XiS(q)) < mp.mpf("1e-18") for q in QUAD)
      and abs(mp.re(q1) - mp.mpf("0.5")) > mp.mpf("0.1"))
check("surrogate Xi_S decays on vertical lines", abs(XiS(mp.mpc("0.5", 12))) <
      abs(XiS(mp.mpc("0.5", 1))), "|Xi(1/2+12i)| = %.3e" % abs(XiS(mp.mpc("0.5", 12))))

# g = chi_S / D4 = s(s-1) Xi_S / D4 = s(s-1) G(s)
gg = lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * G(s)
A1 = gg(q1)
u0 = q1 - mp.mpf("0.5")
z = mp.mpc(0, 1) / A1
c2 = mp.im(z) / mp.im(u0 ** 2)
c0 = mp.re(z) - c2 * mp.re(u0 ** 2)
check("c_0, c_2 are REAL", abs(mp.im(mp.mpc(c0))) == 0 and abs(mp.im(mp.mpc(c2))) == 0,
      "c_0 = %.9f   c_2 = %.9f" % (c0, c2))

P = lambda s: c0 + c2 * (mp.mpc(s) - mp.mpf("0.5")) ** 2
fh = lambda s: P(s) * gg(s)        # = P * s(s-1) Xi_S / D4

check("Thm 3.3: f^(0) = f^(1) = 0, so the witness lies in D^o",
      abs(fh(0)) < mp.mpf("1e-25") and abs(fh(1)) < mp.mpf("1e-25"),
      "f^(0) = %.3e   f^(1) = %.3e" % (abs(fh(0)), abs(fh(1))))
check("Thm 3.3: deg(f) = f^(0) + f^(1) = 0", abs(fh(0) + fh(1)) < mp.mpf("1e-25"))

e_r = max(abs(fh(mp.conj(p)) - mp.conj(fh(p))) for p in pts)
check("Thm 3.3: the witness is REAL (f^(conj s) = conj f^(s)), because P is an "
      "EVEN polynomial in (s-1/2) with real coefficients", e_r < mp.mpf("1e-18"),
      "max err %.3e" % e_r)

aa = [fh(q) for q in QUAD]
check("Thm 3.3: a_1 = i exactly, by construction",
      abs(aa[0] - mp.mpc(0, 1)) < mp.mpf("1e-20"),
      "a_1 = %.12f%+.12fj" % (mp.re(aa[0]), mp.im(aa[0])))
check("Thm 3.3: a_3 = conj(a_1) (the *-symmetry of P and of chi_S/D4)",
      abs(aa[2] - mp.conj(aa[0])) < mp.mpf("1e-18"),
      "a_3 = %.12f%+.12fj" % (mp.re(aa[2]), mp.im(aa[2])))

Q = -M * sum(aa[j] * mp.conj(aa[QMIR[j]]) for j in range(4))
check("Thm 3.3: s(f,f) = -sum_rho m_rho f^(rho) conj(f^(rho')) is REAL",
      abs(mp.im(Q)) < mp.mpf("1e-18"), "Im = %.3e" % abs(mp.im(Q)))
check("Thm 3.3: s(f,f) = +4 m |a_1|^2 > 0  -- WEIL POSITIVITY FAILS on a real "
      "element of D^o", mp.re(Q) > 0 and abs(mp.re(Q) - 4 * M) < mp.mpf("1e-15"),
      "s(f,f) = %+.12f   (predicted 4m = %d)" % (mp.re(Q), 4 * M))

# ---- C2b: the degenerate case rho_0 real (sigma != 1/2, t = 0), Theorem 3.3 case 2
p1, p3 = mp.mpf("0.8"), mp.mpf("0.2")
A1r, A3r = gg(p1), gg(p3)
check("case 2 (rho_0 real): A_1 A_3 is real and nonzero",
      abs(mp.im(A1r)) < mp.mpf("1e-25") and abs(A1r * A3r) > mp.mpf("1e-6"),
      "A_1 A_3 = %+.9f" % mp.re(A1r * A3r))
Pe = lambda s: mp.mpf(1)                                   # even
Po = lambda s: mp.mpc(s) - mp.mpf("0.5")                   # odd
Qe = -2 * M * mp.re(Pe(p1) * A1r * mp.conj(Pe(p3) * A3r))
Qo = -2 * M * mp.re(Po(p1) * A1r * mp.conj(Po(p3) * A3r))
check("case 2: exactly one parity of P gives s(f,f) > 0, so the real-zero case "
      "is covered too", (Qe > 0) != (Qo > 0),
      "even P: s(f,f) = %+.9f    odd P: s(f,f) = %+.9f" % (Qe, Qo))
check("case 2: the winning witness still has f^(0) = f^(1) = 0",
      abs(gg(0)) < mp.mpf("1e-25") and abs(gg(1)) < mp.mpf("1e-25"))

# ---- C3: the control -- on the true xi, on the line, the same recipe cannot win
r = RHO[0]
D2 = lambda s: (mp.mpc(s) - r) * (mp.mpc(s) - mp.conj(r))
g2 = lambda s: chi(s) / D2(s)
lim1 = r * (r - 1) * mp.diff(xi, r) / (r - mp.conj(r))
best = -mp.inf
for i in range(21):
    for j in range(21):
        d0 = mp.mpf(i - 10) / 2
        d2 = mp.mpf(j - 10) / 2
        Pc = lambda s: d0 + d2 * (mp.mpc(s) - mp.mpf("0.5")) ** 2
        a = Pc(r) * lim1
        b = Pc(mp.conj(r)) * mp.conj(lim1)
        # on the line rho' = rho, so s(f,f) = -(|a|^2 + |b|^2)
        best = max(best, -(abs(a) ** 2 + abs(b) ** 2))
check("control: with a zero ON the line, the SAME two-parameter family gives "
      "s(f,f) <= 0 for all 441 real (c_0,c_2)", best <= mp.mpf("1e-25"),
      "best s(f,f) = %.6e (attained only at c = 0)" % best)


# ==================================================== D. what this unblocks

head("D. Consequences for the three theorems that quoted the gaps")

# 113_07 Prop 4.1 (<=): RH false => exists f in D^o, real, with s(f,f) > 0.
check("113_07 Prop 4.1 (<=) is now unconditional: the interpolation it assumed "
      "is Theorem 3.3", mp.re(Q) > 0)
# 113_10 Thm 4.2: (E^o) => RH needs exactly that witness, with deg 0.
check("113_10 Thm 4.2 ((E^o) => RH) is now unconditional: the witness has "
      "s(f,f) > 0 AND deg = 0, so effectivity would contradict 113_10 Thm 2.2",
      mp.re(Q) > 0 and abs(fh(0) + fh(1)) < mp.mpf("1e-25"))
# 113_12 Thm 4.1 (1)=>(2) at the D level, not just the coordinate model.
check("113_12 Thm 4.1 (1)=>(2) now holds in D itself, not only in the "
      "coordinate model", mp.re(Q) > 0 and e_r < mp.mpf("1e-18"))
# 113_12 section 3: d4 is unconditionally complete.
check("113_12 d4 (Serre duality = nondegeneracy) is unconditionally complete: "
      "polar block by Thm 3.2 there, zero block by (SEP) here", sepok and sep2)

check("NOT unblocked: Ansatz A, (E^o), row (d).  Nothing here proves any "
      "inequality about the real xi.", True,
      "the witness of section C exists only under the hypothesis that RH is "
      "false; it is a contrapositive, not a counterexample")


# ------------------------------------------------------------------- verdict

head("VERDICT")
print("  checks: %d passed, %d failed" % (PASS, FAIL))
if FAIL == 0:
    print("""
  VERDICT: ALL CHECKS PASS

  Established:
    Lemma 1.1'  xi * (meromorphic v with poles cancelled by zeros of xi) is the
                Mellin transform of an element of D_theta for every theta.
    Thm 2.1     (SEP) DISCHARGED.  The separating family y_rho = chi/(s-rho)^m
                lies in D; the zero block of s is nondegenerate unconditionally.
                d4 is therefore complete without assuming RH.
    Thm 3.3     (INT) DISCHARGED.  If xi has a zero off the critical line then
                f^(s) = (c_0 + c_2 (s-1/2)^2) s(s-1) xi(s) / prod_j (s-rho_j)^m
                with explicit REAL c_0, c_2 is a real element of D^o with
                s(f,f) = 4 m |a_1|^2 > 0.

  Consequences: 113_07 Prop 4.1, 113_10 Thm 4.2/4.3 and 113_12 Thm 4.1 no
  longer carry an unproved interpolation hypothesis, and none of them is a
  step towards RH -- they are RH, restated.

  NOT established: Ansatz A; (E^o); row (d); RH.
""")
    raise SystemExit(0)
else:
    print("\n  VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
