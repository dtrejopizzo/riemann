#!/usr/bin/env python3
"""Sanity checks for the idempotent-collapse and product-dimension formulas."""


def trop_add(a: float, b: float) -> float:
    return max(a, b)


def main() -> None:
    unit = 0.0  # multiplicative unit in max-plus logarithmic notation
    images = []
    for n in range(1, 101):
        value = unit
        for _ in range(n - 1):
            value = trop_add(value, unit)
        images.append(value)
    assert set(images) == {unit}

    for p, q, alpha, beta in ((2, 3, 2, 3), (3, 5, 4, 2), (5, 7, 3, 6)):
        errors = []
        for depth in range(2, 10):
            d = alpha * p**depth - p + 1
            e = beta * q**depth - q + 1
            errors.append(abs(d * e / (p**depth * q**depth) - alpha * beta))
        assert all(a > b for a, b in zip(errors, errors[1:]))
        assert errors[-1] < errors[0]

    print("VERDICT: SCALING DIMENSION / DIRECT BRIDGE CHECKS PASS")


if __name__ == "__main__":
    main()
