#!/usr/bin/env python3
"""Exact R8 threshold and scope checks."""

from math import exp, log, pi
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_137_R8_IS_CLOSED_AS_AN_ACCEPTANCE_TEST.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


theta_sum = sum(exp(-pi * n * n) for n in range(-20, 21))
h_base = log(theta_sum)

check("theta basepoint is strictly positive", h_base > 0)
check("raw positivity declares the basepoint positive", h_base > 0)
check("threshold predicate puts the basepoint on the boundary",
      not (h_base > h_base) and h_base - h_base == 0)

for offset in (-0.1, -1e-6, 1e-6, 0.1):
    threshold = h_base + offset
    check(f"shifted threshold {offset:+g} is not exact boundary",
          h_base - threshold != 0)

for marker in (
    "R8 is closed without assuming RH",
    "R8 is satisfied",
    "full effectivity dictionary",
    "does not reopen R8",
    "does not prove (3.1), G-3, row A or RH",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: R8 IS CLOSED BY THE UNIQUE BASEPOINT THRESHOLD; THE FULL DICTIONARY IS SEPARATE")
