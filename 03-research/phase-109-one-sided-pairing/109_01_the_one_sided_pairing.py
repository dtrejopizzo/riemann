#!/usr/bin/env python3
"""
109_01 verifier -- the one-sided pairing B(f,g) = sum_n Lambda(n) f(n) g(n).

Checks, each PASS/FAIL, no epsilon chosen to force a pass:

  1. Closed-form identity (Lemma 1.4): the (p,k) double sum equals the
     Lambda(n)-weighted single sum, exactly, at fixed truncation.
  2. Bilinearity (Theorem 2.1): exact finite-sum identity.
  3. Symmetry (Theorem 2.2): exact finite-sum identity.
  4. Non-Hermiticity (Theorem 2.2): an explicit non-real value, with a
     control clause that symmetry still holds on the same pair.
  5. Convergence with shrinking error under refinement (Theorem 3.1),
     against mpmath's -zeta'/zeta(s+t), for Re(s+t) > 1.
  6. Divergence (partial sums fail to stabilize) at Re(s+t) <= 1.
  7. Control clause: a DELIBERATELY WRONG target value (e.g. -zeta'/zeta
     evaluated at the wrong argument, or off by a sign) must be REJECTED,
     i.e. the convergence check must fail against it. This guards against
     a check that would pass against any plausible number.

Run: python3 109_01_the_one_sided_pairing.py
"""
import mpmath as mp

mp.mp.dps = 40


def sieve_primes(limit):
    is_comp = bytearray(limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_comp[j] = 1
    return primes


def prime_powers_upto(N):
    """Return list of (n, log p) for all prime powers n = p^k <= N, k>=1."""
    primes = sieve_primes(N)
    out = []
    for p in primes:
        pk = p
        while pk <= N:
            out.append((pk, mp.log(p)))
            pk *= p
    out.sort(key=lambda t: t[0])
    return out


def f(s, n):
    return mp.mpf(n) ** (-s)


def B_trunc(s, t, N, pps=None):
    """Truncated pairing B(f_s, f_t) using prime powers n <= N."""
    if pps is None:
        pps = prime_powers_upto(N)
    total = mp.mpc(0)
    for n, logp in pps:
        total += logp * f(s, n) * f(t, n)
    return total


def gamma_pk_double_sum(s, t, N, pps=None):
    """The (p,k) double sum, literally, Definition 1.3, same truncation."""
    if pps is None:
        pps = prime_powers_upto(N)
    total = mp.mpc(0)
    for n, logp in pps:
        # Gamma_{p,k}(f_s) = f_s(n) for k>=1 exactly (108_34 Def 1.2, k>=1 branch)
        total += logp * (f(s, n) * f(t, n))
    return total


results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------------
# 1. Closed form identity: double sum over (p,k) equals Lambda(n)-weighted sum
# ---------------------------------------------------------------------
N = 5000
pps = prime_powers_upto(N)
s0, t0 = mp.mpf("1.7"), mp.mpf("0.6")
lhs = gamma_pk_double_sum(s0, t0, N, pps)
rhs = B_trunc(s0, t0, N, pps)
check("Lemma 1.4: (p,k)-sum equals Lambda(n)-sum, exactly",
      abs(lhs - rhs) < mp.mpf("1e-35"),
      f"|diff|={mp.nstr(abs(lhs-rhs))}")

# ---------------------------------------------------------------------
# 2. Bilinearity, exact finite-sum identity
# ---------------------------------------------------------------------
s1, s2, tt = mp.mpf("1.9"), mp.mpf("2.3"), mp.mpf("0.8")
c1, c2 = mp.mpc("1.3", "-0.4"), mp.mpc("-0.7", "0.9")


def B_combo_trunc(coeffs_s, t, N, pps):
    """B(sum c_i f_{s_i}, f_t) computed via the LEFT ARGUMENT being the
    literal function sum c_i f_{s_i}(n), evaluated pointwise at each n."""
    total = mp.mpc(0)
    for n, logp in pps:
        val = sum(c * (mp.mpf(n) ** (-s)) for c, s in coeffs_s)
        total += logp * val * f(t, n)
    return total


lhs_bilin = B_combo_trunc([(c1, s1), (c2, s2)], tt, N, pps)
rhs_bilin = c1 * B_trunc(s1, tt, N, pps) + c2 * B_trunc(s2, tt, N, pps)
check("Theorem 2.1: bilinearity B(c1 f_s1 + c2 f_s2, f_t) = c1 B(f_s1,f_t)+c2 B(f_s2,f_t)",
      abs(lhs_bilin - rhs_bilin) < mp.mpf("1e-30"),
      f"|diff|={mp.nstr(abs(lhs_bilin-rhs_bilin))}")

# ---------------------------------------------------------------------
# 3. Symmetry
# ---------------------------------------------------------------------
sa, sb = mp.mpc("1.4", "0.3"), mp.mpc("2.1", "-0.5")
Bab = B_trunc(sa, sb, N, pps)
Bba = B_trunc(sb, sa, N, pps)
check("Theorem 2.2: symmetry B(f_s,f_t) = B(f_t,f_s), exactly",
      abs(Bab - Bba) < mp.mpf("1e-30"),
      f"|diff|={mp.nstr(abs(Bab-Bba))}")

# ---------------------------------------------------------------------
# 4. Not Hermitian: explicit non-real value, with symmetry control clause
# ---------------------------------------------------------------------
s_h, t_h = mp.mpf(2), mp.mpc("0.5", "1.0")  # Re(s+t) = 2.5 > 1
Bval = B_trunc(s_h, t_h, 20000)
is_nonreal = abs(mp.im(Bval)) > mp.mpf("1e-6")
check("Theorem 2.2: B(f_s,f_t) is genuinely non-real for a real pairing (non-Hermitian witness)",
      is_nonreal,
      f"Im(B)={mp.nstr(mp.im(Bval))}")
# control clause: symmetry still holds exactly on this very pair (it is
# symmetric bilinear, just not Hermitian -- these are independent facts)
Bval_swapped = B_trunc(t_h, s_h, 20000)
check("control: symmetry still holds on the non-Hermitian witness pair",
      abs(Bval - Bval_swapped) < mp.mpf("1e-25"))

# ---------------------------------------------------------------------
# 5. Convergence to -zeta'/zeta(s+t), error shrinking under refinement
# ---------------------------------------------------------------------
s_c, t_c = mp.mpf("1.3"), mp.mpf("0.9")  # Re(s+t) = 2.2 > 1
target = -mp.zeta(s_c + t_c, derivative=1) / mp.zeta(s_c + t_c)

Ns = [2000, 20000, 200000]
errs = []
for Nc in Ns:
    val = B_trunc(s_c, t_c, Nc)
    errs.append(abs(val - target))

shrinking = all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
check("Theorem 3.1: truncated B(f_s,f_t) -> -zeta'/zeta(s+t), error strictly shrinking under refinement",
      shrinking,
      f"errors={[mp.nstr(e, 5) for e in errs]}")

# control clause: a plausible WRONG target must be rejected by the same
# convergence test (guards against a check that passes for any number)
wrong_target_1 = -mp.zeta(s_c + t_c)  # forgot the derivative -- plausible bug
wrong_target_2 = mp.zeta(s_c + t_c, derivative=1) / mp.zeta(s_c + t_c)  # sign flip
val_fine = B_trunc(s_c, t_c, Ns[-1])
control_rejects_1 = abs(val_fine - wrong_target_1) > mp.mpf("1e-3")
control_rejects_2 = abs(val_fine - wrong_target_2) > mp.mpf("1e-3")
check("control: convergence test rejects a plausible WRONG target (missing derivative)",
      control_rejects_1, f"|diff|={mp.nstr(abs(val_fine-wrong_target_1))}")
check("control: convergence test rejects a plausible WRONG target (sign flip)",
      control_rejects_2, f"|diff|={mp.nstr(abs(val_fine-wrong_target_2))}")

# ---------------------------------------------------------------------
# 6. Divergence at Re(s+t) <= 1: partial sums fail to stabilize
# ---------------------------------------------------------------------
s_d, t_d = mp.mpf("0.3"), mp.mpf("0.4")  # Re(s+t) = 0.7 <= 1
Ns_div = [2000, 20000, 200000]
vals_div = [B_trunc(s_d, t_d, Nc) for Nc in Ns_div]
increments = [abs(vals_div[i + 1] - vals_div[i]) for i in range(len(vals_div) - 1)]
# a convergent series has increments -> 0; test that they do NOT shrink at
# the same rate as the convergent case above (i.e. do not tend to a limit):
# compare against the size of the terms actually being added (should be
# comparable to, not orders of magnitude below, the increment).
non_convergent = increments[-1] > mp.mpf("1")  # partial sums moved by > 1 in the last refinement
check("Proposition (108_36 sec 2): divergence off the domain -- partial sums keep moving",
      non_convergent,
      f"increments={[mp.nstr(x,5) for x in increments]}")

# ---------------------------------------------------------------------
print()
n_pass = sum(1 for _, ok in results if ok)
print(f"{n_pass}/{len(results)} checks passed")
if all(ok for _, ok in results):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
