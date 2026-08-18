#!/usr/bin/env python3
"""Dependency-free arithmetic audit of the conservative D.77 manifest."""
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 50
p = Path(__file__).with_name("114_d_77_log3_endpoint_manifest.json")
d = json.loads(p.read_text(encoding="utf-8"))
assert d["schema"] == "phase114-d77-log3-endpoint-v1"
assert d["status"] == "PASS"
assert d["cells"] == [28, 20, 28]
assert sum(d["cells"])*(d["legendre_degree"]+1) == 2*d["parity_dimension"]
projected = Decimal(d["projected_lower_gt"])
loss = Decimal(d["schur_loss_lt"])
tail_e = Decimal(d["tail_even_gt"])
tail_o = Decimal(d["tail_odd_gt"])
assert tail_e+projected-loss > Decimal(d["final_even_gt"])
assert tail_o+projected-loss > Decimal(d["final_odd_gt"])
assert Decimal(d["final_even_gt"]) > 0
assert Decimal(d["final_odd_gt"]) > 0
print("PASS D77 manifest dimensions and conservative arithmetic")
print("PASS endpoint primitive margin >", d["final_odd_gt"])
