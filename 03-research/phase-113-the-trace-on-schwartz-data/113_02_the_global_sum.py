#!/usr/bin/env python3
"""
113_02 verifier -- the global sum over all primes (Task 2).

Checks:
 1. Proposition 1.1: bare-polynomial-decay h gives a partial sum over primes
    that keeps growing (does not stabilize) as the prime bound is refined --
    contrasted with a genuinely convergent control, so the test discriminates.
 2. Theorem 2.1: sum_p (A_p(h)+B_p(h)) converges absolutely (Cauchy-style
    stabilization under refinement) for h in S_eta, eta>1.
 3. Proposition 3.1: the Lambda(n) sum (111_03-style) and this phase's
    unweighted prime-power sum are numerically DIFFERENT for the same h,
    both individually convergent.
"""
import mpmath as mp

mp.mp.dps = 30
PASS = []


def check(name, cond, detail=""):
    PASS.append(cond)
    print(("PASS" if cond else "FAIL") + f": {name}" + (f" ({detail})" if detail else ""))


def sieve_primes(limit):
    is_c = bytearray(limit + 1)
    ps = []
    for i in range(2, limit + 1):
        if not is_c[i]:
            ps.append(i)
            for j in range(i * i, limit + 1, i):
                is_c[j] = 1
    return ps


def smallest_prime_factor_table(limit):
    spf = list(range(limit + 1))
    for i in range(2, int(limit ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


LIMIT = 20000
PRIMES = sieve_primes(LIMIT)
SPF = smallest_prime_factor_table(LIMIT)


def is_prime_power(n):
    """Return (p, k) if n = p^k, k>=1, else None."""
    if n < 2:
        return None
    p = SPF[n]
    m = n
    k = 0
    while m % p == 0:
        m //= p
        k += 1
    if m == 1:
        return (p, k)
    return None


def lambda_of(n):
    pp = is_prime_power(n)
    if pp is None:
        return mp.mpf(0)
    p, k = pp
    return mp.log(p)


def tilde_h_gauss(x):
    return mp.e ** (-x * x)


def tilde_h_poly(x):
    """Bare polynomial decay only, no exponential margin -- control."""
    return 1 / (1 + x * x) ** 3


def h_of_r(th, r):
    return th(mp.log(r))


def Ap(th, p, N=60):
    return mp.nsum(lambda n: h_of_r(th, p ** n), [1, N])


def Bp(th, p, N=60):
    return mp.nsum(lambda m: h_of_r(th, p ** (-m)) * p ** (-m), [1, N])


def partial_sum_tails(th, Pmax):
    s = mp.mpf(0)
    for p in PRIMES:
        if p > Pmax:
            break
        s += Ap(th, p) + Bp(th, p)
    return s


# ---------------------------------------------------------------------
# 1. Proposition 1.1: bare-polynomial control does not stabilize
# ---------------------------------------------------------------------
bounds = [50, 500, 5000, 20000]
poly_vals = [partial_sum_tails(tilde_h_poly, P) for P in bounds]
gauss_vals = [partial_sum_tails(tilde_h_gauss, P) for P in bounds]

poly_increments = [poly_vals[i + 1] - poly_vals[i] for i in range(len(poly_vals) - 1)]
gauss_increments = [gauss_vals[i + 1] - gauss_vals[i] for i in range(len(gauss_vals) - 1)]

check("Proposition 1.1: bare-polynomial partial sums keep growing (do not shrink to 0)",
      all(inc > mp.mpf('1e-4') for inc in poly_increments),
      f"increments={[float(i) for i in poly_increments]}")

check("control: the Gaussian (convergent) increments DO shrink toward 0 (discriminates the test)",
      gauss_increments[-1] < gauss_increments[0] and gauss_increments[-1] < mp.mpf('1e-10'),
      f"increments={[float(i) for i in gauss_increments]}")

# ---------------------------------------------------------------------
# 2. Theorem 2.1: absolute convergence under eta>1 (Gaussian is in every S_eta)
# ---------------------------------------------------------------------
rel_change = abs(gauss_vals[-1] - gauss_vals[-2]) / abs(gauss_vals[-1])
check("Theorem 2.1: sum_p(A_p+B_p) stabilizes (Cauchy) for Gaussian h, eta>1",
      rel_change < mp.mpf('1e-10'), f"rel_change={float(rel_change):.2e}, value={float(gauss_vals[-1])}")

# also check with a narrower-exponential (still eta>1 comfortably) profile as a second witness
def tilde_h_exp2(x):
    return mp.e ** (-2 * x * x)

exp2_vals = [partial_sum_tails(tilde_h_exp2, P) for P in bounds]
rel_change2 = abs(exp2_vals[-1] - exp2_vals[-2]) / abs(exp2_vals[-1])
check("Theorem 2.1: second witness (narrower Gaussian) also stabilizes",
      rel_change2 < mp.mpf('1e-10'), f"rel_change={float(rel_change2):.2e}")

# ---------------------------------------------------------------------
# 3. Proposition 3.1: Lambda(n) sum vs unweighted prime-power sum -- distinct
# ---------------------------------------------------------------------
lambda_sum = mp.nsum(lambda n: lambda_of(int(n)) * h_of_r(tilde_h_gauss, int(n)) / mp.sqrt(int(n)),
                      [2, LIMIT])
prime_power_sum = mp.mpf(0)
for p in PRIMES:
    prime_power_sum += Ap(tilde_h_gauss, p)

check("Proposition 3.1: Lambda(n) sum matches 111_03's reported value (~0.6241927...)",
      abs(lambda_sum - mp.mpf('0.62419273')) < mp.mpf('1e-6'),
      f"value={float(lambda_sum)}")

rel_diff = abs(lambda_sum - prime_power_sum) / abs(prime_power_sum)
check("Proposition 3.1: the two sums are numerically DIFFERENT (not the same object)",
      rel_diff > mp.mpf('0.1'),
      f"lambda_sum={float(lambda_sum)}, prime_power_sum={float(prime_power_sum)}, rel_diff={float(rel_diff):.3f}")

check("Proposition 3.1: both sums are individually finite (no NaN/inf)",
      mp.isfinite(lambda_sum) and mp.isfinite(prime_power_sum))

# ---------------------------------------------------------------------
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    raise SystemExit(1)
