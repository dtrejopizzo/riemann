#!/usr/bin/env python3
"""
109_02 verifier -- the radical of B: rad B = V_PP = {f : f(p^k) = 0 for all
prime powers}, and the explicit witness F(x) = sin(pi x) that refutes the
zero-determined hypothesis.

Checks, each PASS/FAIL:

  1. F(n) = 0 (to available precision) at every tested prime power.
  2. B(F, g) = 0 (to machine precision) for several partner g, tracking the
     residual from check 1 -- not an unconditional zero.
  3. Control clause: perturbing F at one prime power n0 by an explicit bump
     produces B equal to the EXACT predicted value Lambda(n0)*c*g(n0), not
     merely "some nonzero number".
  4. The Mellin-pair closed form for F, checked against direct oscillatory
     numerical integration, at several real s in (0,1).
  5. hat F(rho) != 0, bounded away from zero by an explicit margin, at the
     first five nontrivial zeros of zeta.
  6. Control clause: hat F(2) = 0 EXACTLY (an actual zero of the transform,
     at an even integer that is not a zero of zeta) -- shows the check can
     detect a real zero when one is present, not just always report "far
     from zero".

Run: python3 109_02_the_radical.py
"""
import mpmath as mp

mp.mp.dps = 50


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
    primes = sieve_primes(N)
    out = []
    for p in primes:
        pk = p
        while pk <= N:
            out.append((pk, mp.log(p)))
            pk *= p
    out.sort(key=lambda t: t[0])
    return out


def F(x):
    return mp.sin(mp.pi * x)


results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------------
# 1. F(n) = 0 at prime powers
# ---------------------------------------------------------------------
N = 2000
pps = prime_powers_upto(N)
max_residual = max(abs(F(n)) for n, _ in pps)
check("Theorem 2.1/3.3(a): F(p^k) = 0 to available precision at every tested prime power",
      max_residual < mp.mpf("1e-45"),
      f"max|F(n)|={mp.nstr(max_residual)}")

# ---------------------------------------------------------------------
# 2. B(F, g) = 0 for several partners g, tracking the residual (not
#    unconditionally zero: bound is derived FROM check 1's residual)
# ---------------------------------------------------------------------
def B_trunc_general(fvals_times_g, pps):
    return sum(logp * val for (_, logp), val in zip(pps, fvals_times_g))


def B_of(fun_f, fun_g, pps):
    total = mp.mpc(0)
    for n, logp in pps:
        total += logp * fun_f(n) * fun_g(n)
    return total


def g_monomial(t):
    return lambda x: mp.mpf(x) ** (-t)


partners = {
    "f_2": g_monomial(mp.mpf(2)),
    "f_1.5+0.3i": g_monomial(mp.mpc("1.5", "0.3")),
    "constant_1": lambda x: mp.mpf(1),
}

# expected bound: sum_n logp * |F(n)| * |g(n)| <= max_residual * sum_n logp*|g(n)|
worst_case_scale = sum(logp * abs(g_monomial(mp.mpf(2))(n)) for n, logp in pps)  # loose common scale
all_small = True
for name, g in partners.items():
    val = B_of(F, g, pps)
    bound = max_residual * sum(logp * abs(g(n)) for n, logp in pps) * mp.mpf(10)  # 10x safety
    ok = abs(val) < bound
    all_small = all_small and ok
    print(f"    B(F, {name}) = {mp.nstr(val, 6)}  (bound {mp.nstr(bound,6)})")
check("Theorem 2.1: B(F,g) = 0 to machine precision, for several partners g "
      "(residual traced to check 1, not an unconditional zero)",
      all_small)

# ---------------------------------------------------------------------
# 3. Control clause: perturb F at one prime power, get the EXACT predicted
#    nonzero value, not merely "some" nonzero number.
# ---------------------------------------------------------------------
n0, logp0 = pps[10]  # some prime power well inside the tested range
c = mp.mpf("0.37")


def F_perturbed(x):
    bump = c if x == n0 else mp.mpf(0)
    return F(x) + bump


g_test = lambda x: mp.mpf(1)  # constant partner: g(n0) = 1, keeps the predicted value O(1)
val_perturbed = B_of(F_perturbed, g_test, pps)
predicted = logp0 * c * g_test(n0)  # F(n0)~0 contributes ~0, bump contributes exactly this
check("control: perturbing F at one prime power n0 gives B = Lambda(n0)*c*g(n0) exactly",
      abs(val_perturbed - predicted) < mp.mpf("1e-40"),
      f"n0={n0}, |diff|={mp.nstr(abs(val_perturbed-predicted))}, predicted={mp.nstr(predicted,8)}")
# and this predicted value is itself clearly nonzero (not a vacuous "small" check)
check("control: the predicted perturbation value is not itself numerically tiny",
      abs(predicted) > mp.mpf("1e-3"), f"|predicted|={mp.nstr(abs(predicted))}")

# ---------------------------------------------------------------------
# 4. Mellin-pair closed form for F, vs direct oscillatory integration
# ---------------------------------------------------------------------
def hatF_closed(s):
    return mp.pi ** (-s) * mp.gamma(s) * mp.sin(mp.pi * s / 2)


def hatF_numeric(s):
    integrand = lambda x: x ** (s - 1) * mp.sin(mp.pi * x)
    return mp.quadosc(integrand, [0, mp.inf], period=2)


mellin_ok = True
for s_val in [mp.mpf("0.3"), mp.mpf("0.5"), mp.mpf("0.7")]:
    closed = hatF_closed(s_val)
    numeric = hatF_numeric(s_val)
    diff = abs(closed - numeric)
    ok = diff < mp.mpf("1e-6")
    mellin_ok = mellin_ok and ok
    print(f"    s={mp.nstr(s_val)}: closed={mp.nstr(closed,10)} numeric={mp.nstr(numeric,10)} diff={mp.nstr(diff)}")
check("Theorem 3.3(c): Mellin-pair closed form pi^-s Gamma(s) sin(pi s/2) matches "
      "direct oscillatory integration on 0<Re s<1",
      mellin_ok)

# ---------------------------------------------------------------------
# 5. hat F(rho) != 0 at the first five nontrivial zeros of zeta
# ---------------------------------------------------------------------
margins = []
for k in range(1, 6):
    rho = mp.zetazero(k)
    val = hatF_closed(rho)
    margins.append(abs(val))
    print(f"    zero #{k}: rho={mp.nstr(rho,10)}  |hatF(rho)|={mp.nstr(abs(val),10)}")

check("Theorem 3.3(c): |hat F(rho)| bounded away from 0 at the first five nontrivial zeros",
      all(m > mp.mpf("0.01") for m in margins),
      f"min margin={mp.nstr(min(margins))}")

# ---------------------------------------------------------------------
# 6. Control clause: hat F DOES vanish at s=2 (an actual, non-zeta-related
#    zero of the transform) -- proves the test can detect a real zero.
# ---------------------------------------------------------------------
val_at_2 = hatF_closed(mp.mpf(2))
check("control: hat F(2) = 0 exactly (sin(pi) = 0, Gamma(2)=1 finite and nonzero) "
      "-- the detector fires on an actual zero",
      abs(val_at_2) < mp.mpf("1e-45"),
      f"hatF(2)={mp.nstr(val_at_2)}")
# and Gamma(2) itself is indeed finite and nonzero, confirming the zero is
# from sin, not a coincidental Gamma pole/zero
check("control: Gamma(2) is finite and nonzero (the zero at s=2 is genuinely from sin, not Gamma)",
      abs(mp.gamma(mp.mpf(2)) - 1) < mp.mpf("1e-45"))

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
