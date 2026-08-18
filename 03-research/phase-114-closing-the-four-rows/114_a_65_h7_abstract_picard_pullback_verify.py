#!/usr/bin/env python3
"""Compatibility verifier for the a65 correction superseded by a66."""

from pathlib import Path
import subprocess
import sys


here = Path(__file__).resolve().parent
doc = (here / "114_a_65_H7_ABSTRACT_PICARD_PULLBACK_VS_COMPLETED_LATTICE.md").read_text()

required = (
    "Pic_tor",
    "Pic_qc` and the claimed forgetful map",
    "H7-PRIME-REG",
    "retracted by `a_66`",
)
for token in required:
    if token not in doc:
        raise AssertionError(token)
    print("PASS", token)

result = subprocess.run(
    [sys.executable, str(here / "114_a_66_h7_type_audit_verify.py")],
    check=True,
    capture_output=True,
    text=True,
)
if "VERDICT: UNIT-TORSOR PULLBACK PASS" not in result.stdout:
    raise AssertionError("a66 verdict")
print("PASS authoritative a66 type audit")
print("VERDICT: PIC_TOR LABELS PASS; PIC_QC/TOR CLAIMS RETRACTED")
