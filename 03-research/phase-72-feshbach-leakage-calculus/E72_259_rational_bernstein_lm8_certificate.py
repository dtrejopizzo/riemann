#!/usr/bin/env python3
from fractions import Fraction
from math import comb


R0 = [
    "1.000199",
    "-2.612680",
    "-19.804312",
    "12.299851",
    "299.698952",
    "14.347638",
    "-1797.470005",
    "-192.790165",
    "3715.980490",
]

R1 = [
    "1.000732",
    "-1.539636",
    "-8.755675",
    "-5.533524",
    "46.182864",
    "84.054306",
    "3.002174",
    "-77.401146",
    "-40.848595",
]


def frac_list(xs):
    return [Fraction(x) for x in xs]


def poly_subtract_const(coeffs, c):
    out = coeffs[:]
    out[0] -= Fraction(c)
    return out


def compose_interval_power(coeffs, lo, hi):
    """Return power coefficients of p(lo+(hi-lo)t), exactly."""
    lo = Fraction(lo)
    step = Fraction(hi) - lo
    n = len(coeffs) - 1
    out = [Fraction(0) for _ in range(n + 1)]
    for i, ai in enumerate(coeffs):
        for k in range(i + 1):
            out[k] += ai * Fraction(comb(i, k)) * (lo ** (i - k)) * (step ** k)
    return trim(out)


def trim(coeffs):
    out = coeffs[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def power_to_bernstein(coeffs, degree=None):
    """Convert p(t)=sum a_i t^i on [0,1] to Bernstein degree n coefficients."""
    coeffs = trim(coeffs)
    if degree is None:
        degree = len(coeffs) - 1
    if degree < len(coeffs) - 1:
        raise ValueError("degree too small")
    padded = coeffs + [Fraction(0) for _ in range(degree + 1 - len(coeffs))]
    bern = []
    for k in range(degree + 1):
        s = Fraction(0)
        for i in range(k + 1):
            s += padded[i] * Fraction(comb(k, i), comb(degree, i))
        bern.append(s)
    return bern


def split_bernstein(bern):
    """Split Bernstein coefficients at t=1/2 by exact de Casteljau."""
    levels = [bern]
    cur = bern
    two = Fraction(2)
    while len(cur) > 1:
        cur = [(cur[i] + cur[i + 1]) / two for i in range(len(cur) - 1)]
        levels.append(cur)
    left = [row[0] for row in levels]
    right = [row[-1] for row in reversed(levels)]
    return left, right


def certify_bernstein_nonnegative(power_coeffs, lo, hi, max_depth=64):
    bern = power_to_bernstein(compose_interval_power(power_coeffs, lo, hi))
    stack = [(Fraction(lo), Fraction(hi), bern, 0)]
    boxes = 0
    accepted_min = None
    deepest = 0
    while stack:
        a, b, coeffs, depth = stack.pop()
        boxes += 1
        deepest = max(deepest, depth)
        local_min = min(coeffs)
        if local_min >= 0:
            accepted_min = local_min if accepted_min is None else min(accepted_min, local_min)
            continue
        if depth >= max_depth:
            return False, boxes, accepted_min, deepest, (a, b, local_min)
        mid = (a + b) / 2
        left, right = split_bernstein(coeffs)
        stack.append((mid, b, right, depth + 1))
        stack.append((a, mid, left, depth + 1))
    return True, boxes, accepted_min, deepest, None


def fmt_frac(x):
    return f"{float(x):+.12e} ({x})"


def run_case(name, coeffs, const, lo, hi):
    p = poly_subtract_const(coeffs, const)
    ok, boxes, cert_min, deepest, failure = certify_bernstein_nonnegative(p, lo, hi)
    print(
        f"{name}: {'PASS' if ok else 'FAIL'} boxes={boxes} depth={deepest} "
        f"terminal_min_bern={fmt_frac(cert_min)}"
    )
    if failure is not None:
        a, b, local_min = failure
        print(f"  unresolved interval [{a}, {b}] local_min={fmt_frac(local_min)}")
    return ok


def run():
    print("E72.259 rational Bernstein LM8 certificate")
    print("All coefficients are exact rationals from E72.258 with denominator 10^6.")
    r0 = frac_list(R0)
    r1 = frac_list(R1)
    cases = [
        ("R0-1 on [-1,0]", r0, Fraction(1), Fraction(-1), Fraction(0)),
        ("R0-0.09 on [0,1]", r0, Fraction(9, 100), Fraction(0), Fraction(1)),
        ("R1-1 on [-1,0]", r1, Fraction(1), Fraction(-1), Fraction(0)),
        ("R1-0.16 on [0,1]", r1, Fraction(4, 25), Fraction(0), Fraction(1)),
    ]
    oks = [run_case(*case) for case in cases]
    print(f"overall {'PASS' if all(oks) else 'FAIL'}")


if __name__ == "__main__":
    run()
