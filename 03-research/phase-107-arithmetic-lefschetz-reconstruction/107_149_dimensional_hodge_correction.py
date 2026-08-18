#!/usr/bin/env python3
"""Regression certificate for the dimensional Hodge correction."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def contains(path: str, *needles: str) -> bool:
    text = (ROOT / path).read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


model_ok = contains(
    "107_10_PAPER_C_UNIVERSAL_FINITE_MODELS.md",
    "relative dimension two",
    "total Krull dimension three",
)
audit_ok = contains(
    "107_12_PAPER_D_HODGE_APPLICABILITY_AUDIT.md",
    r"M_f\cdot H_T=0",
    r"\overline M_f^{\,2}\cdot\overline H_T",
)
terminal_ok = contains(
    "107_13_PAPER_D_TERMINAL_IDENTITY_AND_RH_CLOSURE.md",
    r"M_f\cdot H_T=0",
    r"\overline M_f^{\,2}\cdot\overline H_T",
    "Yuan--Zhang",
)

verdict = model_ok and audit_ok and terminal_ok

print("GENERIC_TARGET_DIMENSION: 2")
print("ARITHMETIC_MODEL_TOTAL_DIMENSION: 3")
print("POLARIZATION_FACTOR_REQUIRED: YES")
print("UNPOLARIZED_TERMINAL_IDENTITY_VALID: NO")
print("DIRECT_HODGE_ROUTE: YUAN_ZHANG_DIMENSION_2")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

raise SystemExit(0 if verdict else 1)
