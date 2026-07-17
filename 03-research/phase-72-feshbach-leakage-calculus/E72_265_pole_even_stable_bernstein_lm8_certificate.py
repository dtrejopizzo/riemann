#!/usr/bin/env python3
from fractions import Fraction
from math import comb


# E72.264, buffer=0.002, six-decimal rational coefficients.
R0 = [
    "1.001029",
    "-1.951429",
    "-18.253404",
    "-8.529708",
    "263.566056",
    "210.580938",
    "-1548.826040",
    "-746.639401",
    "3247.543544",
]

R1 = [
    "1.000747",
    "-2.513120",
    "-13.197720",
    "21.797818",
    "127.757425",
    "-135.585710",
    "-348.702213",
    "197.008969",
    "325.771912",
]


def frac_list(xs):
    return [Fraction(x) for x in xs]


def trim(coeffs):
    out = coeffs[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_subtract_const(coeffs, c):
    out = coeffs[:]
    out[0] -= Fraction(c)
    return out


def compose_interval_power(coeffs, lo, hi):
    lo = Fraction(lo)
    step = Fraction(hi) - lo
    n = len(coeffs) - 1
    out = [Fraction(0) for _ in range(n + 1)]
    for i, ai in enumerate(coeffs):
        for k in range(i + 1):
            out[k] += ai * Fraction(comb(i, k)) * (lo ** (i - k)) * (step ** k)
    return trim(out)


def power_to_bernstein(coeffs, degree=None):
    coeffs = trim(coeffs)
    if degree is None:
        degree = len(coeffs) - 1
    padded = coeffs + [Fraction(0) for _ in range(degree + 1 - len(coeffs))]
    bern = []
    for k in range(degree + 1):
        total = Fraction(0)
        for i in range(k + 1):
            total += padded[i] * Fraction(comb(k, i), comb(degree, i))
        bern.append(total)
    return bern


def split_bernstein(bern):
    levels = [bern]
    cur = bern
    while len(cur) > 1:
        cur = [(cur[i] + cur[i + 1]) / 2 for i in range(len(cur) - 1)]
        levels.append(cur)
    left = [row[0] for row in levels]
    right = [row[-1] for row in reversed(levels)]
    return left, right


def certify_nonnegative(power_coeffs, lo, hi, max_depth=72):
    bern = power_to_bernstein(compose_interval_power(power_coeffs, lo, hi))
    stack = [(Fraction(lo), Fraction(hi), bern, 0)]
    boxes = 0
    deepest = 0
    accepted_min = None
    while stack:
        a, b, coeffs, depth = stack.pop()
        boxes += 1
        deepest = max(deepest, depth)
        local_min = min(coeffs)
        if local_min >= 0:
            accepted_min = local_min if accepted_min is None else min(accepted_min, local_min)
            continue
        if depth >= max_depth:
            return False, boxes, deepest, accepted_min, (a, b, local_min)
        mid = (a + b) / 2
        left, right = split_bernstein(coeffs)
        stack.append((mid, b, right, depth + 1))
        stack.append((a, mid, left, depth + 1))
    return True, boxes, deepest, accepted_min, None


def fmt(x):
    return f"{float(x):+.12e} ({x})"


def run_case(name, coeffs, const, lo, hi):
    p = poly_subtract_const(coeffs, const)
    ok, boxes, depth, accepted_min, failure = certify_nonnegative(p, lo, hi)
    print(
        f"{name}: {'PASS' if ok else 'FAIL'} boxes={boxes} depth={depth} "
        f"terminal_min_bern={fmt(accepted_min)}"
    )
    if failure is not None:
        a, b, local_min = failure
        print(f"  unresolved [{a}, {b}], local_min={fmt(local_min)}")
    return ok


def run():
    print("E72.265 pole-even stable rational Bernstein LM8 certificate")
    print("All coefficients exact rationals from E72.264 buffer=0.002, six-decimal grid.")
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
