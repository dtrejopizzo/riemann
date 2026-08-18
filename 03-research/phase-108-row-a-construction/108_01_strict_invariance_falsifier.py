#!/usr/bin/env python3
"""108.01 -- strict Frobenius invariance falsifier.

Plain python3, no numpy/scipy dependency beyond numpy (available) used only
for convenience; nothing here needs it structurally.  Exits 0 and prints an
explicit VERDICT line.
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


# ---------------------------------------------------------------------------
# 1. Candidate compactly supported test functions on (0, infty)
# ---------------------------------------------------------------------------

def triangle_bump(r: np.ndarray, a: float = 2.0, b: float = 3.0) -> np.ndarray:
    mid = 0.5 * (a + b)
    left = (r - a) / (mid - a)
    right = (b - r) / (b - mid)
    val = np.minimum(left, right)
    val = np.clip(val, 0.0, None)
    val[(r <= a) | (r >= b)] = 0.0
    return val


def cosine_bump(r: np.ndarray, a: float = 2.0, b: float = 3.0) -> np.ndarray:
    val = np.zeros_like(r)
    inside = (r > a) & (r < b)
    x = (r[inside] - a) / (b - a)
    val[inside] = 0.5 * (1 - np.cos(2 * np.pi * x))
    return val


def gaussian_window_bump(r: np.ndarray, a: float = 2.0, b: float = 3.0) -> np.ndarray:
    # a genuinely C^infty compactly supported bump (mollifier), not just C^0
    val = np.zeros_like(r)
    mid = 0.5 * (a + b)
    half = 0.5 * (b - a)
    inside = (r > a) & (r < b)
    if np.any(inside):
        u = (r[inside] - mid) / half
        val[inside] = np.exp(-1.0 / (1.0 - u ** 2))
        val[inside] /= val[inside].max()
    return val


def asym_bump(r: np.ndarray, a: float = 2.0, b: float = 3.0) -> np.ndarray:
    # asymmetric: cube of triangle, still compactly supported and nonzero
    return triangle_bump(r, a, b) ** 3


def offcenter_bump(r: np.ndarray) -> np.ndarray:
    return cosine_bump(r, 2.2, 2.9)


CANDIDATES = {
    "triangle": triangle_bump,
    "cosine": cosine_bump,
    "gaussian_window": gaussian_window_bump,
    "asym_cube": asym_bump,
    "offcenter_cosine": offcenter_bump,
}

SUPPORT_A, SUPPORT_B = 2.0, 3.0
TEST_N = [2, 3, 4, 5]


def falsify_strict_invariance() -> dict:
    """For each candidate and each n, confirm f(r/n) != f(r) somewhere,
    i.e. strict invariance genuinely fails (not just 'is unproved')."""
    r_grid = np.linspace(SUPPORT_A + 1e-6, SUPPORT_B - 1e-6, 20001)
    report = {}
    for name, fn in CANDIDATES.items():
        f_r = fn(r_grid.copy())
        assert f_r.max() > 1e-6, f"{name}: candidate is degenerate (max too small)"
        per_n = {}
        for n in TEST_N:
            f_rn = fn((r_grid / n).copy())
            diff = np.max(np.abs(f_rn - f_r))
            per_n[n] = float(diff)
        report[name] = {
            "max_abs_f": float(f_r.max()),
            "min_deviation_over_n": min(per_n.values()),
            "per_n": per_n,
        }
    return report


# ---------------------------------------------------------------------------
# 2. Lemma 3.1: unique factorization gives log n as an exact Z-combination
#    of {log p}, verified exactly via integer factorization.
# ---------------------------------------------------------------------------

def factor(n: int) -> dict:
    d = {}
    m = n
    p = 2
    while p * p <= m:
        while m % p == 0:
            d[p] = d.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        d[m] = d.get(m, 0) + 1
    return d


def check_group_closure(bound: int = 40) -> bool:
    ok = True
    for n in range(2, bound + 1):
        fac = factor(n)
        reconstructed = sum(e * math.log(p) for p, e in fac.items())
        if abs(reconstructed - math.log(n)) > 1e-9:
            ok = False
        # every prime factor of n must itself lie in PRIMES for our finite
        # generating-set demonstration to cover it; record but do not fail
    return ok


def check_no_accidental_power_coincidence(bound_exp: int = 200) -> bool:
    """2^k = 3^m forces k = m = 0 (used in Lemma 3.2). Exact bigint check."""
    for k in range(1, bound_exp):
        two_k = 2 ** k
        # 3^m grows faster; only need to check m up to a comparable size
        m = 1
        three_m = 3
        while three_m < two_k:
            three_m *= 3
            m += 1
        if three_m == two_k:
            return False
    return True


# ---------------------------------------------------------------------------
# 3. Numerical density of G = log(Q_+^x): equidistribution of m*log2 mod
#    log3, giving arbitrarily close approximation to any real target.
# ---------------------------------------------------------------------------

def density_demo(targets: list[float], search_range: int) -> dict:
    log2, log3 = math.log(2), math.log(3)
    out = {}
    for t in targets:
        t_mod = t % log3
        best = None
        best_m = None
        for m in range(1, search_range + 1):
            val = (m * log2) % log3
            d = min(abs(val - t_mod), log3 - abs(val - t_mod))
            if best is None or d < best:
                best = d
                best_m = m
        out[t] = {"best_abs_error_mod_log3": best, "witness_m": best_m}
    return out


def density_improves_with_range(target: float) -> bool:
    small = density_demo([target], 200)[target]["best_abs_error_mod_log3"]
    large = density_demo([target], 20000)[target]["best_abs_error_mod_log3"]
    return large <= small


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    falsifier_report = falsify_strict_invariance()
    all_candidates_falsified = all(
        row["min_deviation_over_n"] > 1e-3 for row in falsifier_report.values()
    )

    closure_ok = check_group_closure(60)
    no_coincidence = check_no_accidental_power_coincidence(200)

    targets = [0.1, 0.5, 1.0, 2.0, -1.3, 3.7]
    density_report = density_demo(targets, 5000)
    density_ok = all(
        row["best_abs_error_mod_log3"] < 5e-3 for row in density_report.values()
    )
    monotone_ok = all(density_improves_with_range(t) for t in targets)

    print("Falsifier (max_r |f(r/n) - f(r)| over n=2..5, must stay bounded")
    print("away from zero for every nonzero compactly supported candidate):")
    for name, row in falsifier_report.items():
        print(
            f"  {name:18s} max|f|={row['max_abs_f']:.4f}  "
            f"min over n of max deviation = {row['min_deviation_over_n']:.4f}"
        )
    print()
    print(f"GROUP_CLOSURE_EXACT (Lemma 3.1, n=2..60 factor reconstruction): "
          f"{'YES' if closure_ok else 'NO'}")
    print(f"NO_2K_EQ_3M_COINCIDENCE (Lemma 3.2 input, k up to 200): "
          f"{'YES' if no_coincidence else 'NO'}")
    print()
    print("Density demo: best approximation of target by m*log(2) mod log(3),")
    print("m in [1, 5000]:")
    for t, row in density_report.items():
        print(f"  target={t:+.2f}  best_error={row['best_abs_error_mod_log3']:.2e}"
              f"  witness m={row['witness_m']}")
    print(f"DENSITY_NUMERICAL_EVIDENCE: {'YES' if density_ok else 'NO'}")
    print(f"DENSITY_IMPROVES_WITH_SEARCH_RANGE: {'YES' if monotone_ok else 'NO'}")

    verdict_no_go = (
        all_candidates_falsified
        and closure_ok
        and no_coincidence
        and density_ok
        and monotone_ok
    )

    print()
    print(f"STRICT_INVARIANT_NONZERO_F_EXISTS: {'NO' if verdict_no_go else 'INCONCLUSIVE'}")
    print(f"INCOMPATIBLE_HYPOTHESIS: COMPACT_ANGULAR_SUPPORT")
    print(f"VERDICT: {'NO' if verdict_no_go else 'INCONCLUSIVE'}")

    if not verdict_no_go:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
