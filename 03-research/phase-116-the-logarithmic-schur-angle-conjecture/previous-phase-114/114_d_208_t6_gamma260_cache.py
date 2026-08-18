#!/usr/bin/env python3
"""Directed cache of the complete 260 by 260 Gamma-difference block."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import numpy as np
from flint import arb, ctx


HERE = Path(__file__).resolve().parent
N = 260
DPS = int(os.environ.get("D208_DPS", "1600"))
ctx.dps = DPS
T = arb(6).log() / 2

spec = importlib.util.spec_from_file_location(
    "d147", HERE / "114_d_147_hurwitz_gamma_arb.py"
)
d147 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(d147)

print("computing directed Gamma260", flush=True)
G = d147.exact_gamma_block(N, DPS, T)
centre = np.array(
    [[float(G[i, j].mid()) for j in range(N)] for i in range(N)]
)
radius = np.array(
    [[float(G[i, j].rad()) for j in range(N)] for i in range(N)]
)
saved_radius = np.nextafter(
    radius + np.abs(np.spacing(centre)) / 2,
    np.inf,
)
assert np.isfinite(centre).all()
assert np.isfinite(saved_radius).all()
save = os.environ.get("D208_SAVE", "/tmp/t6_gamma260_arb.npz")
np.savez(
    save,
    C=centre,
    R=saved_radius,
    N=np.array(N),
    digits=np.array(DPS),
)
print("Gamma260 max serialized radius", saved_radius.max(), flush=True)
print("saved", save)
print("D208 DIRECTED GAMMA260 CACHE: PASS")
