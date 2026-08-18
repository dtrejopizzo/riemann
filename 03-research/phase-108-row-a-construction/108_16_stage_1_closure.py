#!/usr/bin/env python3
"""
108_16 verifier -- Stage 1 closure. Re-runs the verifiers this closure note
depends on (108_11, 108_12, 108_13, 108_14, 108_15) as subprocesses and
confirms each exits 0, then re-checks, standalone, the three headline
numeric facts the closure leans on most directly.
"""

import math
import subprocess
import sys
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

DEPENDENCIES = [
    "108_11_global_assembly_locally_integrable.py",
    "108_12_the_constant_cp_and_its_sum.py",
    "108_13_route_a_counterterm_incommensurate.py",
    "108_14_route_b_zeta_regularization.py",
    "108_15_route_c_primitive_no_go.py",
]


def run_dependency(name):
    path = os.path.join(HERE, name)
    if not os.path.exists(path):
        return None, f"MISSING FILE: {path}"
    try:
        result = subprocess.run(
            [sys.executable, path],
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    last_line = ""
    for line in reversed(result.stdout.strip().splitlines()):
        if line.strip():
            last_line = line.strip()
            break
    return result.returncode, last_line


def main():
    print("=" * 70)
    print("PART 1: re-run all dependency verifiers, confirm exit 0")
    print("=" * 70)
    all_pass = True
    for name in DEPENDENCIES:
        code, last_line = run_dependency(name)
        ok = (code == 0)
        all_pass &= ok
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}  (exit={code})")
        print(f"        {last_line}")
    print(f"\nAll dependency verifiers exit 0: {all_pass}")

    print("\n" + "=" * 70)
    print("PART 2: standalone re-check of the three headline facts")
    print("=" * 70)

    # --- Fact 1: Chebyshev theta(x) = Theta(x), independent re-derivation
    # using a fresh sieve at a scale different from 108_13's.
    print("\n--- Fact 1: theta(x) = Theta(x) (Chebyshev) ---")
    Xmax = 500_000
    is_prime = np.ones(Xmax + 1, dtype=bool)
    is_prime[0:2] = False
    for i in range(2, int(Xmax ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i:: i] = False
    primes = np.nonzero(is_prime)[0]
    log_primes = np.log(primes.astype(float))
    theta_cum = np.cumsum(log_primes)
    sample_idx = [1000, 5000, 10000, len(primes) - 1]
    ratios = []
    for idx in sample_idx:
        x = primes[idx]
        ratio = theta_cum[idx] / x
        ratios.append(ratio)
        print(f"  x={x:8d}  theta(x)={theta_cum[idx]:12.2f}  "
              f"theta(x)/x={ratio:.4f}")
    fact1_ok = all(0.5 < r < 1.5 for r in ratios)

    # --- Fact 2: -zeta'/zeta(0) = -log(2 pi), fresh Euler-Maclaurin impl.
    print("\n--- Fact 2: -zeta'/zeta(0) = -log(2 pi) ---")
    BERNOULLI_EVEN = {2: 1/6, 4: -1/30, 6: 1/42, 8: -1/30, 10: 5/66}

    def zeta(s, N=12, M=5):
        total = 0.0
        for n in range(1, N):
            total += n ** (-s)
        total += (N ** (1 - s)) / (s - 1)
        total += 0.5 * N ** (-s)
        for k in range(1, M + 1):
            b2k = BERNOULLI_EVEN[2 * k]
            prod = 1.0
            for j in range(2 * k - 1):
                prod *= (s + j)
            total += (b2k / math.factorial(2 * k)) * prod * N ** (-s - 2 * k + 1)
        return total

    h = 1e-4
    zp0 = (-zeta(2 * h) + 8 * zeta(h) - 8 * zeta(-h) + zeta(-2 * h)) / (12 * h)
    z0 = zeta(0.0)
    val = -zp0 / z0
    target = -math.log(2 * math.pi)
    print(f"  zeta(0) = {z0:.10f}  (theory -0.5)")
    print(f"  -zeta'/zeta(0) = {val:.8f}  (theory {target:.8f})")
    fact2_ok = abs(val - target) < 1e-5

    # --- Fact 3: the 108_15 counterexample is non-degenerate, i.e. its
    # governing 2x2 linear system is well-conditioned (not an artifact of
    # a near-singular solve).
    print("\n--- Fact 3: 108_15's counterexample linear system is "
          "well-conditioned ---")

    def window(t):
        w = np.zeros_like(t)
        mask = (t >= 1.0) & (t <= 2.0)
        w[mask] = 0.5 * (1.0 - np.cos(2.0 * np.pi * (t[mask] - 1.0)))
        return w

    def moment(k, n=100_000):
        t = np.linspace(1.0, 2.0, n + 1)
        y = window(t) * t ** k
        hh = (t[-1] - t[0]) / n
        s = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
        return s * hh / 3.0

    I = {k: moment(k) for k in (-2, -1, 0, 1)}
    M = np.array([[I[-2], I[-1]], [I[-1], I[0]]])
    cond = np.linalg.cond(M)
    print(f"  condition number of the 2x2 system = {cond:.4f} "
          f"(not near-singular: 108_15's own quadrature confirmed exact "
          f"constraint residuals ~1e-16, consistent with this)")
    fact3_ok = cond < 1.0e4

    all_facts_ok = fact1_ok and fact2_ok and fact3_ok
    print(f"\nAll three standalone facts confirmed: {all_facts_ok}")

    overall = all_pass and all_facts_ok
    print()
    if overall:
        print("VERDICT: STAGE_1_CLOSURE_CONFIRMED "
              "(a-dependent part closed per 108_11; constant term remains "
              "open; Routes A, B, C all fail per 108_13/108_14/108_15, "
              "each verifier re-run and passing, and the three headline "
              "numeric facts independently reconfirmed)")
    else:
        print("VERDICT: STAGE_1_CLOSURE_CHECK_FAILED "
              "(a dependency verifier or a standalone fact did not "
              "reconfirm -- investigate before trusting 108_16's claims)")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
