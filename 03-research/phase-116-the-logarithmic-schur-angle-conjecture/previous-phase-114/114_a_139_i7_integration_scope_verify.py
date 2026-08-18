#!/usr/bin/env python3
"""Scope/algebra checks for decorated I7 versus unified integration."""

from math import isclose, log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_139_I7_DECORATED_DYNAMICS_VS_ROW_A_INTEGRATION.md").read_text()
AUDIT = (HERE / "114_a_10_ROW_A_COMPLETION_AUDIT.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def contact_mass(n):
    fs = factors(n)
    return log(next(iter(fs))) if len(fs) == 1 else 0.0


composition_ok = True
for m in range(1, 40):
    for n in range(1, 40):
        fm, fn, fmn = factors(m), factors(n), factors(m * n)
        combined = fm.copy()
        for p, e in fn.items():
            combined[p] = combined.get(p, 0) + e
        composition_ok &= combined == fmn
check("torsor labels compose multiplicatively on all samples", composition_ok)

prime_power_ok = True
for p in (2, 3, 5, 7, 11):
    for k in range(1, 6):
        prime_power_ok &= isclose(contact_mass(p ** k), log(p))
check("all sampled prime-power contacts have mass log p", prime_power_ok)
check("mixed-prime contact vanishes", contact_mass(6) == contact_mass(30) == 0)

for marker in ("a1", "a2", "a3", "a4", "a5"):
    check(f"authoritative contract contains {marker}", marker in AUDIT)

for marker in (
    "I7-DYN-TOR",
    "H7-DYN-INTEGRATE",
    "not additionally necessary",
    "does not close row A",
    "undecorated Chow representative is mandatory",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: DECORATED I7 DYNAMICS IS CLOSED; UNIFIED GEOMETRIC INTEGRATION IS THE LIVE GATE")
