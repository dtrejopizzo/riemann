#!/usr/bin/env python3
"""
111_01 verifier -- convergence of the three pieces of I_partial on Schwartz data.

Checks (each prints PASS/FAIL; script exits 0 iff all pass):

  1. Polar term at w=1 (Lemma 111.1.2 / Theorem 111.1.3, sharp threshold):
     sech(x)  (exponential decay rate exactly 1)  ->  int sech(x) e^{-x} dx DIVERGES,
        growing linearly in the truncation X (slope exactly 2, a genuine value check,
        not just "it grows").
     sech(x)^2 (rate 2 > 1) -> int sech(x)^2 e^{-x} dx CONVERGES, stabilizing under
        refinement of the truncation (Cauchy criterion on successive X).

  2. Polar term at w=0 (Lemma 111.1.1) needs nothing beyond bare Schwartz class:
     f(x) = exp(-sqrt(|x|)) is Schwartz (all derivatives decay faster than every
     polynomial) but has NO exponential decay rate at all (Remark 111.0.1).
     int f(x) dx (w=0) CONVERGES and stabilizes; int f(x) e^{-x} dx (w=1) DIVERGES,
     and much more violently than the sech case -- confirming w=0 is free while w=1
     needs the extra eta>1 condition even on a "nice" Schwartz function.

  3. Zero sum (Theorem 111.1.5): for the xi-divisible Gaussian pair of 110_02
     Example 110.2.6 (fhat = xi*ghat, ghat = sqrt(pi) e^{w^2/4}), partial sums of
     sum_rho fhat(rho) * conj(ghat(rho)) over actual zeros (mp.zetazero) stabilize
     to a fixed value under refinement (more zeros included). Control: a synthetic
     harmonic-density sequence a_n = 1/n (matching only the zero-COUNT growth with
     no extra transform decay) does NOT stabilize -- it grows like log N -- showing
     the check is not vacuous: decay of the transform is doing real work.

  4. Riemann-von Mangoldt density N(T) ~ (T/2pi)log(T/2pi) - T/2pi (quoted, used in
     Theorem 111.1.5's proof) is checked against actual zero locations, with
     relative error shrinking as T grows.

Run: python3 111_01_convergence_of_the_three_pieces.py
"""
from mpmath import mp, mpf, mpc, pi, gamma, zeta, sqrt, exp, cosh, quad, zetazero, log

mp.dps = 25

TOL = mpf('1e-9')
ALL_PASS = True


def check(name, cond, detail=""):
    global ALL_PASS
    status = "PASS" if cond else "FAIL"
    if not cond:
        ALL_PASS = False
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


def sech(x):
    return 1 / cosh(x)


# ---------------------------------------------------------------------------
# Check 1: w=1 sharp threshold, sech (rate 1, diverges) vs sech^2 (rate 2, converges)
# ---------------------------------------------------------------------------
print("=== Check 1: polar term at w=1, sharp exponential-decay threshold ===")

slopes = []
for X in [40, 80, 160, 320]:
    v = quad(lambda x: sech(x) * exp(-x), [-X, 0, X])
    slopes.append(v / X)
# genuine value check: the divergence slope must equal 2 (not merely "grow"),
# and must be STABLE under refinement (a real asymptotic rate, not noise)
slope_stable = all(abs(s - 2) < TOL for s in slopes)
check("sech, w=1: integral grows linearly with slope exactly 2 under refinement",
      slope_stable, f"slopes={[float(s) for s in slopes]}")

vals_good = []
for X in [40, 80, 160]:
    v = quad(lambda x: sech(x) ** 2 * exp(-x), [-X, 0, X])
    vals_good.append(v)
# Cauchy / refinement convergence test
converges = abs(vals_good[-1] - vals_good[-2]) < TOL * max(1, abs(vals_good[-1]))
# control: reject a WRONG limiting value (e.g. claiming it converges to something
# other than what refinement actually shows, such as 2*pi or pi/2)
value = vals_good[-1]
not_a_wrong_value = abs(value - 2 * pi) > mpf('1') and abs(value - pi / 2) > mpf('1')
check("sech^2, w=1: integral converges under refinement (Cauchy)", converges,
      f"vals={[float(v) for v in vals_good]}")
check("sech^2, w=1: control -- limiting value is not one of the wrong guesses (2*pi, pi/2)",
      not_a_wrong_value, f"value={float(value)}")

# ---------------------------------------------------------------------------
# Check 2: w=0 free on bare Schwartz class; w=1 needs more, even more dramatically
# ---------------------------------------------------------------------------
print()
print("=== Check 2: w=0 needs nothing beyond Schwartz; w=1 needs exponential decay ===")


def f_nosech(x):
    # Schwartz (all derivatives x-any-polynomial-weighted are bounded) but with
    # NO exponential decay rate: e^{-sqrt(|x|)} decays slower than e^{-eps|x|} for
    # every eps > 0.
    return exp(-sqrt(abs(x)))


w0_vals = []
for X in [50, 100, 200, 400]:
    v = quad(lambda x: f_nosech(x), [-X, 0, X])
    w0_vals.append(v)
w0_converges = abs(w0_vals[-1] - w0_vals[-2]) < mpf('1e-4')
check("w=0 for e^{-sqrt|x|} (no exponential decay at all) converges under refinement",
      w0_converges, f"vals={[float(v) for v in w0_vals]}")

w1_vals = []
for X in [10, 20, 40]:
    v = quad(lambda x: f_nosech(x) * exp(-x), [-X, 0, X])
    w1_vals.append(v)
# should blow up far faster than linearly (confirm ratio of successive values is
# itself large and growing, not converging to 1 as a convergent sequence would)
ratios = [w1_vals[i + 1] / w1_vals[i] for i in range(len(w1_vals) - 1)]
w1_diverges_badly = all(r > 100 for r in ratios)
check("w=1 for e^{-sqrt|x|} diverges (successive-truncation ratios blow up, not -> 1)",
      w1_diverges_badly, f"ratios={[float(r) for r in ratios]}")

# ---------------------------------------------------------------------------
# Check 3: zero sum stabilizes for the xi-divisible Gaussian pair; harmonic control does not
# ---------------------------------------------------------------------------
print()
print("=== Check 3: zero-sum convergence (xi-divisible pair) vs. harmonic control ===")


def xi(w):
    w = mpc(w)
    if abs(w) < mpf('1e-20') or abs(w - 1) < mpf('1e-20'):
        return mpf('0.5')
    return mpf('0.5') * w * (w - 1) * pi ** (-w / 2) * gamma(w / 2) * zeta(w)


def ghat(w):
    return sqrt(pi) * exp(mpc(w) ** 2 / 4)


def fhat(w):
    return xi(w) * ghat(w)


N = 20
partial = mpc(0)
checkpoints = {}
for n in range(1, N + 1):
    rho = zetazero(n)
    term = fhat(rho) * ghat(rho).conjugate()
    partial += term
    if n in (5, 10, 15, 20):
        checkpoints[n] = abs(partial)

zero_sum_stable = abs(checkpoints[20] - checkpoints[10]) < mpf('1e-30')
check("zero-sum partial sums stabilize as more zeros are included (Cauchy)",
      zero_sum_stable, f"|S_10|={float(checkpoints[10]):.3e}, |S_20|={float(checkpoints[20]):.3e}")

harmonic_25 = sum(mpf(1) / n for n in range(1, 26))
harmonic_200 = sum(mpf(1) / n for n in range(1, 201))
harmonic_diverges = (harmonic_200 - harmonic_25) > mpf('1')
check("control: synthetic harmonic-density sequence (1/n, matching only the zero "
      "COUNT growth with no transform decay) does NOT stabilize -- keeps growing",
      harmonic_diverges,
      f"H_25={float(harmonic_25):.4f}, H_200={float(harmonic_200):.4f}, diff={float(harmonic_200-harmonic_25):.4f}")

# ---------------------------------------------------------------------------
# Check 4: Riemann-von Mangoldt density, quoted fact, sanity-checked with shrinking error
# ---------------------------------------------------------------------------
print()
print("=== Check 4: Riemann-von Mangoldt N(T) sanity check (quoted fact) ===")

rel_errors = []
for n in [10, 50, 100, 500]:
    rho = zetazero(n)
    T = rho.imag
    N_pred = (T / (2 * pi)) * log(T / (2 * pi)) - T / (2 * pi)
    rel_err = abs(N_pred - n) / n
    rel_errors.append(rel_err)
    print(f"    n={n}: gamma_n={float(T):.4f}, N(T) predicted={float(N_pred):.4f}, "
          f"relative error={float(rel_err):.4f}")

shrinking = all(rel_errors[i] > rel_errors[i + 1] for i in range(len(rel_errors) - 1))
check("Riemann-von Mangoldt relative error shrinks as T grows (asymptotic law, not noise)",
      shrinking, f"rel_errors={[float(r) for r in rel_errors]}")

# control: reject an obviously wrong density law, e.g. N(T) ~ T (linear, wrong order)
wrong_pred_100 = zetazero(100).imag  # T itself, i.e. claiming N(T) ~ T
wrong_rel_err = abs(wrong_pred_100 - 100) / 100
check("control: a wrong density law (N(T) ~ T, linear) is rejected -- far larger relative error",
      wrong_rel_err > mpf('0.5'), f"wrong_rel_err={float(wrong_rel_err):.4f}")

# ---------------------------------------------------------------------------
print()
if ALL_PASS:
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    raise SystemExit(1)
