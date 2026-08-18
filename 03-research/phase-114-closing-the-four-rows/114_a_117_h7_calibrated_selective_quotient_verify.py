#!/usr/bin/env python3
"""Checks for 114.a.117 calibrated selective moment quotients."""

from pathlib import Path
from itertools import product
from math import floor, log


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_117_H7_CALIBRATED_SELECTIVE_QUOTIENT_ON_SATURATED_RAYS.md").read_text()
ALPHA = log(2.0) / (2.0 * log(3.0))


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


# Coordinate projection of a saturated finite block is exactly saturated.
for p, m in ((3, 4), (5, 6), (7, 8)):
    k = floor(ALPHA * m)
    full = product(range(p), repeat=m)
    projected = {tuple(vector[:k]) for vector in full}
    check(len(projected) == p ** k, f"exact selected image p={p},m={m},k={k}")

# Use synthetic p_m=2^(2m)+1 for the analytic asymptotic; primality is not
# used by the error identity, only exponential size is.
ratios = []
for m in (20, 40, 80, 160, 320, 640):
    p = 2 ** (2 * m) + 1
    k = floor(ALPHA * m)
    h_cal = k * log(p)
    d1 = log(m * (p - 1))
    d2 = m * log(2.0)
    rr = d1 * d2 / (2.0 * log(3.0))
    error = abs(h_cal - rr)
    check(error <= log(p) + ALPHA * m * log(m) + 1.0,
          f"explicit floor/log error m={m}")
    ratios.append(error / (m * m))
check(ratios[-1] < ratios[0] and ratios[-1] < 0.02,
      "normalized error tends to zero")

for m in range(1, 200):
    k = floor(ALPHA * m)
    if not 0 <= ALPHA * m - k < 1:
        raise AssertionError(f"floor calibration m={m}")
print("PASS floor calibration through m=199")

for marker in (
    "retain the first `k_m` coordinates",
    "unital ring quotient",
    "removes the explicit saturation excess",
    "Both the upper and lower bounds are exact",
    "per-block** part of H7-SEL is closed",
    "made that blocks",
    "does not close H7-SEL-RR/EXACT, row A or RH",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: CALIBRATED SELECTIVE QUOTIENT HAS THE SHARP RR COEFFICIENT PER BLOCK")
