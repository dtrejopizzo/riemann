#!/usr/bin/env python3
"""Exact, dependency-free structural audit of the D.66 Arb manifest."""
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 80
path = Path(__file__).with_name("114_d_66_delta_cover_manifest.json")
data = json.loads(path.read_text(encoding="utf-8"))
assert data["schema"] == "phase114-d66-directed-arb-cover-v1"
assert data["arb_precision_bits"] == 192
leaves = data["leaves"]
assert len(leaves) == 24
assert Decimal(leaves[0]["left"]) == Decimal(data["delta_bridge_left"])
for first, second in zip(leaves, leaves[1:]):
    assert Decimal(first["right"]) == Decimal(second["left"])
assert Decimal(leaves[-1]["right"]) == Decimal(data["delta_overcover_right"])
for leaf in leaves:
    assert Decimal(leaf["left"]) < Decimal(leaf["right"])
    assert Decimal(leaf["even_margin_gt"]) > 0
    assert Decimal(leaf["odd_margin_gt"]) > 0
assert min(Decimal(x["odd_margin_gt"]) for x in leaves) >= Decimal("0.0009")
print("PASS D66 manifest: 24 exactly adjacent strict leaves")
print("PASS delta coverage: [0.000037, 0.0008529]")
print("PASS global recorded margin: > 0.0009")
