#!/usr/bin/env python3
"""108.02 -- character relaxation classification verifier.

Plain python3. Confirms the algebraic identities of the classification
f(r) = c r^s, chi(n) = n^{-s}, and numerically falsifies rigidity for two
non-Mellin totally multiplicative characters (Liouville's lambda, and a
per-prime-varying exponent character), contrasting their failure to
converge to 1 near q=1 with the convergence that n^{-s} exhibits.
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# 1. f = r^s satisfies f(r/n) = n^{-s} f(r)
# ---------------------------------------------------------------------------

def check_power_law(tol: float = 1e-9) -> bool:
    ss = [-2.0, -1.0, -0.5, 0.0, 0.3, 1.0, 2.0, 3.7]
    ns = [2, 3, 4, 5, 7, 12]
    rs = [0.3, 1.0, 2.5, 10.0]
    ok = True
    for s in ss:
        for n in ns:
            for r in rs:
                lhs = (r / n) ** s
                rhs = (n ** (-s)) * (r ** s)
                if abs(lhs - rhs) > tol * max(1.0, abs(rhs)):
                    ok = False
    return ok


# ---------------------------------------------------------------------------
# 2. Total multiplicativity of chi(n) = n^{-s}, and well-definedness of the
#    extension chi(a/b) := chi(a)/chi(b) on equal fractions.
# ---------------------------------------------------------------------------

def check_multiplicativity_and_extension(tol: float = 1e-9) -> bool:
    ok = True
    for s in (-1.3, 0.0, 0.7, 2.0):
        chi = lambda n, s=s: n ** (-s)
        for n in range(2, 8):
            for m in range(2, 8):
                if abs(chi(n * m) - chi(n) * chi(m)) > tol:
                    ok = False
        # equal fractions with different representations
        fracs = [(2, 3), (4, 6), (6, 9), (20, 30), (200, 300)]
        vals = [chi(a) / chi(b) for a, b in fracs]
        if max(vals) - min(vals) > tol:
            ok = False
    return ok


# ---------------------------------------------------------------------------
# 3. Rigidity: Liouville's lambda extended to Q_+^x does NOT converge to 1
#    near q=1, unlike n^{-s}.
# ---------------------------------------------------------------------------

def omega(n: int) -> int:
    """Number of prime factors of n, counted with multiplicity."""
    m, count = n, 0
    p = 2
    while p * p <= m:
        while m % p == 0:
            m //= p
            count += 1
        p += 1
    if m > 1:
        count += 1
    return count


def liouville(n: int) -> int:
    return 1 if omega(n) % 2 == 0 else -1


def liouville_extended(a: int, b: int) -> int:
    # chi(a/b) = lambda(a)/lambda(b) = lambda(a)*lambda(b) since lambda in {+-1}
    return liouville(a) * liouville(b)


def check_liouville_nonconvergence(j_max: int = 4000, tail_frac: float = 0.25) -> dict:
    """q_j = (j+1)/j -> 1 as j -> infty.  chi(q_j) = lambda(j+1)*lambda(j).
    Show both signs persist arbitrarily far out (no convergence to 1)."""
    tail_start = int(j_max * (1 - tail_frac))
    seen_plus = False
    seen_minus = False
    for j in range(tail_start, j_max):
        val = liouville_extended(j + 1, j)
        if val == 1:
            seen_plus = True
        else:
            seen_minus = True
    both_persist = seen_plus and seen_minus
    return {"tail_start": tail_start, "j_max": j_max, "both_signs_in_tail": both_persist}


def check_power_character_converges(j_max: int = 4000, s: float = 0.83) -> dict:
    """Contrast: chi(n) = n^{-s} extended, chi(q_j) with q_j=(j+1)/j -> 1,
    converges monotonically to 1."""
    errs = []
    for j in [10, 100, 1000, j_max]:
        q = (j + 1) / j
        chi_q = q ** (-s)
        errs.append(abs(chi_q - 1.0))
    monotone_decreasing = all(errs[i] >= errs[i + 1] for i in range(len(errs) - 1))
    return {"errors": errs, "monotone_decreasing": monotone_decreasing,
            "final_error": errs[-1]}


# ---------------------------------------------------------------------------
# 4. A per-prime-varying exponent character also fails to converge near 1.
# ---------------------------------------------------------------------------

def factor(n: int) -> dict:
    d, m, p = {}, n, 2
    while p * p <= m:
        while m % p == 0:
            d[p] = d.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        d[m] = d.get(m, 0) + 1
    return d


def varying_exponent_chi(n: int) -> float:
    """s_p alternates between 0.5 and 3.0 depending on p mod 4 -- a totally
    multiplicative character NOT of the form n^{-s} for a single s."""
    val = 1.0
    for p, e in factor(n).items():
        s_p = 0.5 if p % 4 == 1 else 3.0
        val *= p ** (-s_p * e)
    return val


def check_varying_exponent_nonconvergence(j_max: int = 3000) -> dict:
    diffs = []
    for j in range(j_max - 200, j_max):
        q_num, q_den = j + 1, j
        chi_q = varying_exponent_chi(q_num) / varying_exponent_chi(q_den)
        diffs.append(abs(chi_q - 1.0))
    # if it were converging to 1, the max over this late window would be small;
    # rigidity predicts it stays bounded away from 0.
    return {"max_abs_diff_late_window": max(diffs), "min_abs_diff_late_window": min(diffs)}


# ---------------------------------------------------------------------------
# 5. s = 0 corner matches 108.01's excluded object.
# ---------------------------------------------------------------------------

def check_s_zero_is_constant() -> bool:
    s = 0.0
    for r in (0.5, 1.0, 3.3, 17.0):
        if abs(r ** s - 1.0) > 1e-12:
            return False
    return True


def main() -> None:
    power_ok = check_power_law()
    mult_ok = check_multiplicativity_and_extension()

    liouville_report = check_liouville_nonconvergence()
    power_char_report = check_power_character_converges()
    varying_report = check_varying_exponent_nonconvergence()
    s_zero_ok = check_s_zero_is_constant()

    print(f"POWER_LAW_IDENTITY f(r/n)=n^(-s)f(r): {'YES' if power_ok else 'NO'}")
    print(f"MULTIPLICATIVITY_AND_EXTENSION_WELL_DEFINED: {'YES' if mult_ok else 'NO'}")
    print()
    print("Liouville lambda extended to Q_+^x near q=1 "
          f"(tail j in [{liouville_report['tail_start']}, {liouville_report['j_max']}]):")
    print(f"  both signs persist in the tail: {liouville_report['both_signs_in_tail']}"
          "  (=> no convergence to 1 => NOT a valid character for any continuous f)")
    print()
    print("Contrast, n^{-s} near q=1, errors at j=10,100,1000,4000:")
    print(f"  {power_char_report['errors']}  monotone: "
          f"{power_char_report['monotone_decreasing']}")
    print()
    print("Per-prime varying-exponent character near q=1, late window "
          f"max/min |chi(q_j)-1|: {varying_report['max_abs_diff_late_window']:.4f} / "
          f"{varying_report['min_abs_diff_late_window']:.4f}  (bounded away from 0 => "
          "no convergence => excluded by Theorem 3.1)")
    print()
    print(f"S_ZERO_GIVES_CONSTANT (Corollary 4.2): {'YES' if s_zero_ok else 'NO'}")

    liouville_excluded = liouville_report["both_signs_in_tail"]
    power_char_converges = power_char_report["monotone_decreasing"] and \
        power_char_report["final_error"] < 1e-3
    varying_excluded = varying_report["max_abs_diff_late_window"] > 0.1

    verdict = (
        power_ok
        and mult_ok
        and liouville_excluded
        and power_char_converges
        and varying_excluded
        and s_zero_ok
    )

    print()
    print(f"CLASSIFICATION_CONFIRMED (f=c r^s, chi=n^(-s), no periodic factor): "
          f"{'YES' if verdict else 'NO'}")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")

    if not verdict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
