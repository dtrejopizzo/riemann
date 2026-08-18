#!/usr/bin/env python3
"""Exact semantic checks for the deliberately projected-only D.79 manifest."""
import json
from decimal import Decimal
from pathlib import Path

p = Path(__file__).with_name("114_d_79_projected_tangency_manifest.json")
d = json.loads(p.read_text())
assert d["status"] == "PASS_PROJECTED_ONLY"
assert d["full_space_feshbach"] is False
assert d["row_d_closed"] is False
assert d["gamma_depth"] == 160 and d["parity_dimension"] == 480
assert d["independent_full_runs"] == 2
assert d["outputs_identical_at_recorded_precision"] is True
assert Decimal(d["claimed_lower_bound"]) == Decimal("-1e-7")
assert Decimal(d["even_preconditioned_disk_lower"]) > 0
assert Decimal(d["odd_preconditioned_disk_lower"]) > 0
print("PASS D79 projected-only manifest semantics")
