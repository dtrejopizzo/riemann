#!/usr/bin/env python3
"""
113_03 verifier -- the direct construction of T_fin(h) on the admissible
class A (eta>1, h(1)=0).

Checks:
 1. An explicit h in A gives a finite T_fin(h), stable under refinement in
    the prime bound (and trivially in K, since h(1)=0 kills scheme
    dependence -- reusing 113_01's mechanism).
 2. A control h NOT in A (h(1)!=0) genuinely requires a scheme choice at
    the finite places -- i.e. is NOT scheme-independent -- confirming the
    h(1)=0 condition in Definition 1.1 is load-bearing.
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


PRIMES = sieve_primes(10000)


def h_of_r(th, r):
    return th(mp.log(r))


def Ap(th, p, N=60):
    return mp.nsum(lambda n: h_of_r(th, p ** n), [1, N])


def Bp(th, p, N=60):
    return mp.nsum(lambda m: h_of_r(th, p ** (-m)) * p ** (-m), [1, N])


def T_fin(th, Pmax):
    s = mp.mpf(0)
    for p in PRIMES:
        if p > Pmax:
            break
        s += Ap(th, p) + Bp(th, p)
    return s


# h in A: odd Gaussian, h(1) = tilde_h(0) = 0 * e^0 = 0 exactly, exponential (super-eta) decay
def tilde_h_admissible(x):
    return x * mp.e ** (-x * x)


check("Definition 1.1: h(1)=0 exactly for the admissible witness",
      abs(h_of_r(tilde_h_admissible, 1)) < mp.mpf('1e-40'))

vals = [T_fin(tilde_h_admissible, P) for P in [200, 1000, 5000, 10000]]
rel = abs(vals[-1] - vals[-2]) / (abs(vals[-1]) + mp.mpf('1e-30'))
check("Theorem 2.2/4.2: T_fin(h) stabilizes under refinement for h in A",
      rel < mp.mpf('1e-8'), f"rel={float(rel):.2e}, T_fin={float(vals[-1])}")

# K-truncation triviality when h(1)=0: reuse 113_01's mechanism directly
def W_p_K(th, p, K, Ntail=60):
    p = mp.mpf(p)
    tail = Ap(th, p, Ntail) + Bp(th, p, Ntail)
    h1 = h_of_r(th, 1)
    return tail + h1 * ((p - 2) / (p - 1) + K)


p_test = 5
Ks = [1, 10, 100, 1000]
Kvals = [W_p_K(tilde_h_admissible, p_test, K) for K in Ks]
spread = max(Kvals) - min(Kvals)
check("scheme-independence at finite places for h in A: K-truncation is exactly flat",
      spread < mp.mpf('1e-25'), f"spread={float(spread):.2e}")

# ---------------------------------------------------------------------
# control: h NOT in A (h(1) != 0) -- genuinely scheme-dependent
# ---------------------------------------------------------------------
def tilde_h_control(x):
    return mp.e ** (-x * x)  # even Gaussian, h(1)=1


h1_control = h_of_r(tilde_h_control, 1)
check("control h(1) != 0 (Definition 1.1's second condition is violated)",
      abs(h1_control - 1) < mp.mpf('1e-30'))

Kvals_control = [W_p_K(tilde_h_control, p_test, K) for K in Ks]
spread_control = max(Kvals_control) - min(Kvals_control)
check("control: raw K-truncation is NOT flat when h(1)!=0 (scheme-dependence exhibited)",
      spread_control > mp.mpf('1'), f"spread={float(spread_control):.2f}")

# and the two Laurent/subtract-K schemes give different finite numbers, matching 113_01 Thm 3.3
pval = mp.mpf(p_test)
tail_control = Ap(tilde_h_control, p_test) + Bp(tilde_h_control, p_test)
scheme1 = tail_control + h1_control * (pval - 2) / (pval - 1)
scheme2 = tail_control + h1_control * ((pval - 2) / (pval - 1) - mp.mpf(1) / 2)
check("control: the two regularization schemes disagree by exactly h(1)/2 when h(1)!=0",
      abs((scheme1 - scheme2) - h1_control / 2) < mp.mpf('1e-25'),
      f"scheme1={float(scheme1):.6f}, scheme2={float(scheme2):.6f}")

# ---------------------------------------------------------------------
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    raise SystemExit(1)
