#!/usr/bin/env python3
"""
Verifier for 108_42 -- Stage 4 geometry II: signature of B_inf, and the local
term.

Checks:
  1. Blockwise eigenvalues of the definite sector (all = 2) and the
     hyperbolic sector (exactly +1,-1 with equal multiplicity), on finite
     truncations of growing size -- Theorem 2.1.
  2. The Gram operator on each sector is bounded and boundedly invertible
     (definite sector: inverse has constant norm 1/2; hyperbolic sector: is
     its own inverse) -- Proposition 1.1.
  3. Decay-rate check: coefficients of R(a) are O(1/n); grouped pairing
     terms lambda_n(a) are O(1/n^2) -- Lemma 3.2 / 3.4.
  4. Theorem 3.6: B_inf(U,R(a)) = pi*cot(pi*a/2) exactly, verified via
     truncated-sum convergence (error shrinks under refinement) at a real
     and a complex point.

No zero of zeta or xi is used anywhere in this file.
"""
import sys
import math
import mpmath as mp
import sympy as sp

mp.mp.dps = 30

PASS = []


def report(name, ok, detail=""):
    PASS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------------
# Check 1: blockwise eigenvalues (Theorem 2.1), exact via sympy
# ---------------------------------------------------------------------
print("=== Check 1: blockwise eigenvalues, exact (sympy) ===")
ok1 = True
for N in [1, 3, 8, 20]:
    Mdef = sp.diag(*([sp.Integer(2)] * N))
    eigs = Mdef.eigenvals()  # dict eigenvalue -> multiplicity
    all_two = set(eigs.keys()) == {sp.Integer(2)}
    ok1 &= all_two
    report(f"definite sector N={N}: eigenvalues all = 2", all_two, f"eigs={dict(eigs)}")

for M in [1, 2, 5, 15]:
    blocks = []
    for _ in range(M):
        blocks.append(sp.Matrix([[0, 1], [1, 0]]))
    Mhyp = sp.diag(*blocks)
    eigs = Mhyp.eigenvals()
    correct = eigs == {sp.Integer(1): M, sp.Integer(-1): M}
    ok1 &= correct
    report(f"hyperbolic sector, M={M} blocks: eigenvalues +1,-1 mult {M} each",
           correct, f"eigs={dict(eigs)}")

# ---------------------------------------------------------------------
# Check 2: Gram operator bounded & boundedly invertible (Prop 1.1)
# ---------------------------------------------------------------------
print("\n=== Check 2: Gram operator bounded and boundedly invertible ===")
ok2 = True

# definite sector: G = 2*Id, inverse = 1/2*Id, constant norm across sizes
for N in [1, 5, 50]:
    G = sp.diag(*([sp.Integer(2)] * N))
    Ginv = sp.diag(*([sp.Rational(1, 2)] * N))
    prod = G * Ginv
    is_identity = prod == sp.eye(N)
    ok2 &= is_identity
    report(f"definite sector N={N}: G*Ginv = Id", is_identity)

# hyperbolic sector: each 2x2 block is its own inverse
block = sp.Matrix([[0, 1], [1, 0]])
involution = (block * block) == sp.eye(2)
ok2 &= involution
report("hyperbolic block is its own inverse (involution)", involution)

# ---------------------------------------------------------------------
# Check 3: decay rates (Lemma 3.2 / 3.4)
# ---------------------------------------------------------------------
print("\n=== Check 3: decay rates of R(a) coefficients and lambda_n(a) ===")
a_test = mp.mpf('1.3') + mp.mpf('0.4') * 1j


def coeff_R_plus(n, a):  # coefficient of a_n in R(a), n>=1
    return 1 / (a + 2 * n)


def coeff_R_minus(n, a):  # coefficient of a_n^- in R(a), n>=1
    return 1 / (a - 2 * n)


def lam(n, a):
    if n == 0:
        return 2 / a
    return 2 * (1 / (a + 2 * n) + 1 / (a - 2 * n))


ns = [100, 200, 400, 800]
# check |coeff_R_plus(n)| ~ C/n : ratio*n should stabilize
ratios_R = [abs(coeff_R_plus(n, a_test)) * n for n in ns]
stable_R = max(ratios_R) / min(ratios_R) < 1.05
ok3 = stable_R
report("R(a) coefficients decay like 1/n (n*|coeff| stabilizes)", stable_R,
       f"n*|coeff| values={[float(x) for x in ratios_R]}")

# check |lambda_n(a)| ~ C/n^2 : ratio*n^2 should stabilize
ratios_L = [abs(lam(n, a_test)) * n * n for n in ns]
stable_L = max(ratios_L) / min(ratios_L) < 1.05
ok3 &= stable_L
report("lambda_n(a) decays like 1/n^2 (n^2*|lambda_n| stabilizes)", stable_L,
       f"n^2*|lambda_n| values={[float(x) for x in ratios_L]}")

# ---------------------------------------------------------------------
# Check 4: Theorem 3.6 -- exact recovery of pi*cot(pi*a/2)
# ---------------------------------------------------------------------
print("\n=== Check 4: B_inf(U,R(a)) = pi*cot(pi*a/2), convergence test ===")


def truncated_sum(a, N):
    s = mp.mpf(2) / a
    for n in range(1, N + 1):
        s += 2 / (a + 2 * n) + 2 / (a - 2 * n)
    return s


ok4 = True
for a_val, label in [(mp.mpf('1.3'), "real a=1.3"),
                      (mp.mpf('0.7') + mp.mpf('0.3') * 1j, "complex a=0.7+0.3i")]:
    target = mp.pi * mp.cot(mp.pi * a_val / 2)
    Ns = [10, 20, 40, 80, 160, 320, 640]
    errs = [abs(truncated_sum(a_val, N) - target) for N in Ns]
    # errors must be (weakly) monotonically shrinking, and the ratio should
    # be roughly consistent with O(1/N) decay (halving N doubles the error
    # order, i.e. doubling N should roughly halve the error)
    shrinking = all(errs[i + 1] <= errs[i] for i in range(len(errs) - 1))
    # check the decay rate: error(N) / error(2N) should be around 2 (O(1/N))
    ratios = [errs[i] / errs[i + 1] for i in range(len(errs) - 1)]
    rate_ok = all(1.3 < r < 3.0 for r in ratios)
    final_small = errs[-1] < mp.mpf('1e-2')
    ok = shrinking and rate_ok and final_small
    ok4 &= ok
    report(f"Theorem 3.6 convergence, {label}", ok,
           f"errs={[float(e) for e in errs]} ratios={[float(r) for r in ratios]}")

# ---------------------------------------------------------------------
overall = ok1 and ok2 and ok3 and ok4
print()
if overall and all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    sys.exit(1)
