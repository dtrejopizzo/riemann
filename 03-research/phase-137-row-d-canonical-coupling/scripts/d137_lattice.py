#!/usr/bin/env python3
"""d137_lattice.py -- certified constant checks for phase 137, D.11 (Paper 46 Sec 13 lattice).

ROUND 2 (repairs H1, H5b, H18 of R137_002_HOSTILE_AUDIT.md).  Round 1's C2 defined u0 as the
last GRID point with PiK > 0 and then tested PiK < 0 only ABOVE that point, so the interval
(0.235, 0.2386) where PiK is still positive was never probed and the reported u0 = 0.235 was
false.  In round 2 the two facts that carry the theorems are PROVED analytically in
R137_003_BUILDER_ROUND2.md Sec 2.0 and are only VERIFIED here:

  (A)  PiK(u) < 0 for every u >= u0 := (1/2) log(5.1/pi) = 0.2422553269...,
       because K''(u) > K(u)/4 term by term once x := pi n^2 e^{2u} >= 5.1
       (the polynomial p(x) = 8x^3 - 56x^2 + 82x - 18 is positive and increasing there).
  (B)  K(t) >= 2 pi^2 e^{9t/2} exp(-pi e^{2t}) for every t >= 0 (n = 1 term, all others positive).

Only ONE constant is certified numerically and only an UPPER bound for it is needed:
M_+ := sup PiK, bounded by a fine grid on [0, u0] plus a Lipschitz margin (PiK is even and
PiK <= 0 off (-u0, u0) by (A), so the sup is attained there).

Checks:
  C1  K > 0 on [-3,3]; int K = xi(1/2)  (this pins Paper 46's normalisation Phi_K = xi).
  C2  the polynomial certificate of (A); PiK < 0 on a fine grid over [u0, 3];
      and PiK > 0 somewhere in (0.235, u0) -- the interval round 1 never probed.
  C3  the bound (B) on a grid over [0, 4].
  C4  M_+ <= 17 by grid + Lipschitz margin on [0, u0].  The margin STRUCTURE bounds the sup on the
      whole interval; L itself is a sampled max of |PiK'|, not a proved bound -- so the honest
      statement is the robustness one: max_grid PiK = 16.953849 at h = 2e-4, so the conclusion
      holds for ANY L <= 460, against a sampled L ~ 101.5 (a factor 4.5 of head-room).
  C5  the certified single-generator threshold m0(q) = M_+ w_q / kappa_q of Theorem D.11.2,
      with kappa_q from (B), and a direct verification that m K - w_q tau_{log q}(PiK) >= 0.

Nothing here proves anything; (A) and (B) are proved in the report and the script only
verifies them.  Usage:  python3 d137_lattice.py [--fast]
"""
import sys
from mpmath import mp, mpf, exp, pi, log, diff, nstr, quad, zeta, gamma, mpmathify

FAST = "--fast" in sys.argv
mp.dps = 30 if not FAST else 20
NMAX = 8 if not FAST else 5

def K(t):
    """Paper 46 (11.7) normalisation, fixed by Phi_K = xi (check C1).  K is even."""
    t = abs(mpf(t)); s = mpf(0)
    for n in range(1, NMAX+1):
        n2 = mpf(n)**2
        s += (2*pi**2*n2**2*exp(mpf(9)/2*t) - 3*pi*n2*exp(mpf(5)/2*t))*exp(-pi*n2*exp(2*t))
    return 2*s

def PiK(t):
    return -diff(K, t, 2) + K(t)/4

XI12 = (mpf(1)/2*(mpf(1)/2-1)/2)*pi**(-mpf(1)/4)*gamma(mpf(1)/4)*zeta(mpf(1)/2)
XSTAR = mpf("5.1")                      # certified: p(x) > 0 and increasing for x >= 5.1
U0 = log(XSTAR/pi)/2                    # = 0.2422553269...
BETA = pi*exp(2*U0)                     # = XSTAR = 5.1 exactly
MPLUS_CLAIM = mpf(17)

ok = True
def chk(name, cond, extra=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + extra if extra else ""))

# ---- C1
step = mpf("0.25") if FAST else mpf("0.1")
ts = [-3 + i*step for i in range(int(6/step)+1)]
chk("C1 K > 0 on [-3,3]", all(K(t) > 0 for t in ts))
IK = quad(K, [-4, 0, 4])
chk("C1 int K = xi(1/2)  (normalisation Phi_K = xi)", abs(IK - XI12) < mpf(10)**(-12),
    "int K = %s" % nstr(IK, 12))

# ---- C2
p = lambda x: 8*x**3 - 56*x**2 + 82*x - 18
dp = lambda x: 24*x**2 - 112*x + 82
xs = [XSTAR + mpf(i)/10 for i in range(0, 400)]
chk("C2 p(x) = 8x^3-56x^2+82x-18 > 0 and p'(x) > 0 for x >= 5.1",
    p(XSTAR) > 0 and all(dp(x) > 0 for x in xs), "p(5.1) = %s" % nstr(p(XSTAR), 6))
print("     u0 = (1/2)log(5.1/pi) = %s,  beta = pi e^{2u0} = %s" % (nstr(U0, 10), nstr(BETA, 6)))
g2 = mpf("0.002") if FAST else mpf("0.0005")
neg = [U0 + i*g2 for i in range(int((3-U0)/g2)+1)]
chk("C2 PiK < 0 on [u0, 3]", all(PiK(t) < 0 for t in neg),
    "max PiK on [u0,3] = %s" % nstr(max(PiK(t) for t in neg), 6))
probe = [mpf("0.235") + i*mpf("0.0005") for i in range(0, 8)]
witness = [(t, PiK(t)) for t in probe if PiK(t) > 0]
chk("C2 PiK > 0 somewhere in [0.235, u0)  (the interval round 1 never probed)",
    len(witness) > 0,
    "" if not witness else "PiK(%s) = +%s" % (nstr(witness[0][0], 5), nstr(witness[0][1], 6)))

# ---- C3
def Klow(t):
    return 2*pi**2*exp(mpf(9)/2*t)*exp(-pi*exp(2*t))
g3 = mpf("0.05") if FAST else mpf("0.01")
c3 = [i*g3 for i in range(0, int(4/g3)+1)]
chk("C3 K(t) >= 2 pi^2 e^{9t/2} e^{-pi e^{2t}} on [0,4]", all(K(t) >= Klow(t) for t in c3),
    "min ratio = %s" % nstr(min(K(t)/Klow(t) for t in c3), 8))

# ---- C4
g4 = mpf("0.0005") if FAST else mpf("0.0002")
grid = [i*g4 for i in range(0, int(U0/g4)+2)]
vals = [PiK(t) for t in grid]
L = max(abs(diff(PiK, t)) for t in grid[::(40 if FAST else 100)])
margin = L*g4/2
chk("C4 M_+ = sup PiK <= 17  (grid + Lipschitz margin on [0,u0]; PiK even, <= 0 off (-u0,u0))",
    max(vals) + margin <= MPLUS_CLAIM,
    "max on grid = %s, Lipschitz bound = %s, margin = %s"
    % (nstr(max(vals), 8), nstr(L, 4), nstr(margin, 3)))

# ---- C5
def w(q, pr):
    return log(pr)/mp.sqrt(q)
qs = [(2, 2)] if FAST else [(2, 2), (3, 3)]
for q, pr in qs:
    lq = log(q)
    kap = 2*pi**2*mpf(q)**mpf("4.5")*exp(mpf("4.5")*U0)*exp(-BETA*mpf(q)**2)   # from (B)
    kap_true = min(K(lq+U0), K(lq-U0))
    m0 = MPLUS_CLAIM*w(q, pr)/kap
    m = int(mp.ceil(m0))
    print("     q = %d : w_q = %s, kappa_q >= %s (true min on window %s), certified m0 = %d"
          % (q, nstr(w(q, pr), 6), nstr(kap, 6), nstr(kap_true, 6), m))
    chk("C5 kappa_q lower bound is valid", kap <= kap_true)
    g5 = mpf("0.05") if FAST else mpf("0.01")
    T = 4
    tt = [-T + i*g5 for i in range(int(2*T/g5)+1)]
    bad = [t for t in tt if m*K(t) - w(q, pr)*PiK(t-lq) < 0]
    chk("C5 m*K - w_q*tau_{log q}(PiK) >= 0 on [-4,4], q = %d, m = %d" % (q, m),
        not bad, "" if not bad else "first failure t = %s" % nstr(bad[0], 4))

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
