#!/usr/bin/env python3
"""
109_99 verifier -- condensed re-check of Phase 109's load-bearing claims,
standalone (does not import 109_01/109_02, to be independently runnable).

  1. B(f_s, f_0) = -zeta'/zeta(s) (108_36's object, recovered at t=0),
     error shrinking under refinement.
  2. B is bilinear and symmetric (exact finite-sum identities).
  3. rad B = {f : f(p^k) = 0 at all prime powers}: the witness
     F(x) = sin(pi x) pairs to (numerically) zero with a generic partner,
     while a perturbed version (nonzero at one prime power) does not,
     matching the exact predicted value -- this is the two-sided control
     that makes the radical claim a real test, not a one-directional check.
  4. The refutation witness: hat F(rho) != 0 at a nontrivial zero of zeta,
     while hat F(2) = 0 exactly -- proving the radical is not contained in
     the zero-determined space, with a control showing the detector can
     find a genuine zero.

Run: python3 109_99_phase_109_summary_verifier.py
"""
import mpmath as mp

mp.mp.dps = 40

results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


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


def B_trunc(fun_f, fun_g, pps):
    total = mp.mpc(0)
    for n, logp in pps:
        total += logp * fun_f(n) * fun_g(n)
    return total


# ----------------------------------------------------------------
# 1. B(f_s, f_0) -> -zeta'/zeta(s), shrinking error
# ----------------------------------------------------------------
s0 = mp.mpf("1.6")
f_s = lambda x: mp.mpf(x) ** (-s0)
f_0 = lambda x: mp.mpf(1)
target = -mp.zeta(s0, derivative=1) / mp.zeta(s0)
errs = []
for N in [3000, 30000, 300000]:
    pps = prime_powers_upto(N)
    val = B_trunc(f_s, f_0, pps)
    errs.append(abs(val - target))
check("B(f_s, f_0) -> -zeta'/zeta(s), error strictly shrinking",
      all(errs[i + 1] < errs[i] for i in range(len(errs) - 1)),
      f"errors={[mp.nstr(e, 4) for e in errs]}")

# ----------------------------------------------------------------
# 2. bilinear + symmetric, exact
# ----------------------------------------------------------------
pps_small = prime_powers_upto(4000)
sA, sB, tC = mp.mpc("1.7", "0.2"), mp.mpc("2.1", "-0.3"), mp.mpf("1.9")
c1, c2 = mp.mpc("0.6", "1.1"), mp.mpc("-1.2", "0.4")
fA = lambda x: mp.mpf(x) ** (-sA)
fB = lambda x: mp.mpf(x) ** (-sB)
fC = lambda x: mp.mpf(x) ** (-tC)
combo = lambda x: c1 * fA(x) + c2 * fB(x)
lhs = B_trunc(combo, fC, pps_small)
rhs = c1 * B_trunc(fA, fC, pps_small) + c2 * B_trunc(fB, fC, pps_small)
check("bilinearity: B(c1 fA + c2 fB, fC) = c1 B(fA,fC) + c2 B(fB,fC), exact",
      abs(lhs - rhs) < mp.mpf("1e-30"))
check("symmetry: B(fA,fC) = B(fC,fA), exact",
      abs(B_trunc(fA, fC, pps_small) - B_trunc(fC, fA, pps_small)) < mp.mpf("1e-30"))

# ----------------------------------------------------------------
# 3. radical two-sided control: F=sin(pi x) pairs to ~0; a perturbed
#    version does not, matching the exact predicted value
# ----------------------------------------------------------------
F = lambda x: mp.sin(mp.pi * x)
pps_rad = prime_powers_upto(1000)
g_partner = lambda x: mp.mpf(x) ** (-mp.mpf(2))
val_F = B_trunc(F, g_partner, pps_rad)
check("F=sin(pi x) is in the radical: B(F, f_2) ~ 0",
      abs(val_F) < mp.mpf("1e-30"), f"|B(F,f_2)|={mp.nstr(abs(val_F))}")

n0, logp0 = pps_rad[5]
c = mp.mpf("0.9")
F_pert = lambda x: F(x) + (c if x == n0 else mp.mpf(0))
val_pert = B_trunc(F_pert, g_partner, pps_rad)
predicted = logp0 * c * g_partner(n0)
check("control: perturbing F at one prime power breaks radical membership, "
      "matching the exact predicted value (not just 'some nonzero number')",
      abs(val_pert - predicted) < mp.mpf("1e-25") and abs(predicted) > mp.mpf("1e-6"),
      f"n0={n0}, predicted={mp.nstr(predicted)}, got={mp.nstr(val_pert)}")

# ----------------------------------------------------------------
# 4. refutation witness: hat F(rho) != 0 at a nontrivial zero, but
#    hat F(2) = 0 exactly (control: detector finds a real zero)
# ----------------------------------------------------------------
hatF = lambda s: mp.pi ** (-s) * mp.gamma(s) * mp.sin(mp.pi * s / 2)
rho1 = mp.zetazero(1)
val_rho = hatF(rho1)
check("refutation witness: hat F(rho_1) != 0 at the first nontrivial zero of zeta",
      abs(val_rho) > mp.mpf("0.1"), f"rho_1={mp.nstr(rho1,10)}, |hatF(rho1)|={mp.nstr(abs(val_rho))}")

val_2 = hatF(mp.mpf(2))
check("control: hat F(2) = 0 exactly -- the detector can find a genuine zero",
      abs(val_2) < mp.mpf("1e-35"), f"hatF(2)={mp.nstr(val_2)}")

# ----------------------------------------------------------------
print()
n_pass = sum(1 for _, ok in results if ok)
print(f"{n_pass}/{len(results)} checks passed")
if all(ok for _, ok in results):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
