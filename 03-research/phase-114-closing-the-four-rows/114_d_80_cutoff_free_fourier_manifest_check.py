#!/usr/bin/env python3
"""Semantic guard against overstating the D.80 finite-band audit."""
import json
from pathlib import Path

p = Path(__file__).with_name("114_d_80_cutoff_free_fourier_manifest.json")
d = json.loads(p.read_text())
assert d["source"].startswith("https://arxiv.org/src/2607.02828v1/")
assert len(d["source_sha256"]) == 64
assert d["external_code_copied"] is False
assert d["scope"] == "FINITE_GALERKIN_ONLY"
assert d["uses_zero_side_for_sign"] is False
assert d["full_space"] is False and d["row_d_closed"] is False
for run in d["runs"]:
    assert run["status"] == "CERTIFIED_PD"
    assert run["n_neg"] == 0 and run["n_pos"] == run["dimension"]
print("PASS D80 finite-Galerkin-only provenance manifest")
