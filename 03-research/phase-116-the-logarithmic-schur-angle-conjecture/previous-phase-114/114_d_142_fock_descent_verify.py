#!/usr/bin/env python3
"""Finite factorial certificates for D.142."""

from __future__ import annotations

import math

for r in range(1, 13):
    source_norm_sq = math.factorial(r)
    normalized_image_norm = math.sqrt(math.factorial(r))
    assert math.isclose(
        normalized_image_norm**2, source_norm_sq, rel_tol=2e-15
    )

for r in range(1, 8):
    for s in range(1, 8):
        boson_factor = math.sqrt(
            math.factorial(r + s)
            / (math.factorial(r) * math.factorial(s))
        )
        assert boson_factor > 1

# No fixed exponential damping controls sqrt(r!).
for c in (0.9, 0.5, 0.1):
    log_values = [
        0.5 * math.lgamma(r + 1) + r * math.log(c)
        for r in range(1, 2001)
    ]
    assert max(log_values[-100:]) > max(log_values[:10])

print("D142 Fock-descent certificates: PASS")
