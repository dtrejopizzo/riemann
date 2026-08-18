#!/usr/bin/env python3
"""Audit the explicit absolute Euler tail bound used in E78.98."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median

import mpmath as mp


HERE = Path(__file__).resolve().parent
OUT_PATH = HERE / "E78_98_safe_gamma_ident_tail_results.json"


def serial(x: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(x, digits)


def von_mangoldt(limit: int) -> list[mp.mpf]:
    vals = [mp.mpf(0) for _ in range(limit + 1)]
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        for m in range(p * p, limit + 1, p):
            sieve[m] = False
        power = p
        logp = mp.log(p)
        while power <= limit:
            vals[power] = logp
            if power > limit // p:
                break
            power *= p
    return vals


def tail_bound(x: mp.mpf, alpha: mp.mpf, s_abs: mp.mpf) -> mp.mpf:
    delta = alpha - 1
    return 2 * (x ** (-delta) + s_abs * x ** (-delta) * (mp.log(x) / delta + 1 / delta**2))


def stats(values: list[mp.mpf]) -> dict[str, str | int]:
    ordered = sorted(values)
    return {
        "count": len(values),
        "min": serial(ordered[0]),
        "median": serial(median(ordered)),
        "max": serial(ordered[-1]),
    }


def main() -> None:
    mp.mp.dps = 80
    limit = 200_000
    lam_values = [6, 12, 20]
    sigmas = [mp.mpf("1.0"), mp.mpf("1.5"), mp.mpf("2.0"), mp.mpf("3.0")]
    data = von_mangoldt(limit)
    rows = []
    ratios = []
    for lam in lam_values:
        x = mp.mpf(lam) ** 2
        for sigma in sigmas:
            s = mp.mpf("0.5") + sigma
            actual = 2 * mp.fsum(
                data[n] * mp.exp(-s * mp.log(n))
                for n in range(int(mp.floor(x)) + 1, limit + 1)
                if data[n]
            )
            bound = tail_bound(x, s, abs(s))
            ratio = abs(actual) / bound if bound else mp.mpf("0")
            ratios.append(ratio)
            rows.append(
                {
                    "lambda": lam,
                    "x_equals_lambda_sq": serial(x),
                    "sigma": serial(sigma),
                    "s": serial(s),
                    "actual_tail_truncated_at_2e6": serial(actual),
                    "explicit_bound": serial(bound),
                    "ratio_actual_over_bound": serial(ratio),
                }
            )

    result = {
        "statement": "Audit of the explicit absolute Euler tail bound on safe compacts for x=lambda^2.",
        "parameters": {
            "dps": 80,
            "lambda_values": lam_values,
            "sigmas": [serial(s) for s in sigmas],
            "prime_power_sum_cutoff": limit,
        },
        "summary_ratio_actual_over_bound": stats(ratios),
        "rows": rows,
    }
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
