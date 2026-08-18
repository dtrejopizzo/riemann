#!/usr/bin/env python3
"""Rebuild the directed V200 centre used by the T=log(6)/2 certificates.

The serialized centre is used only to choose frozen frames.  Every final
sign must be recomputed in Arb by D.199 (or a later directed certificate).
"""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import numpy as np
from flint import arb, ctx


HERE = Path(__file__).resolve().parent
N = 200
DPS = int(os.environ.get("D215_DPS", "300"))
ctx.dps = DPS
T = arb(6).log() / 2


def ball(c: float, r: float) -> arb:
    rr = np.nextafter(float(r), np.inf)
    rr += abs(np.spacing(float(c))) / 2 + np.nextafter(0.0, 1.0)
    return arb(repr(float(c)), repr(float(rr)))


spec = importlib.util.spec_from_file_location(
    "d147", HERE / "114_d_147_hurwitz_gamma_arb.py"
)
d147 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(d147)

contact_path = os.environ.get("D215_CONTACT", "/tmp/d185_contacts6_arb.npz")
contact = np.load(contact_path)
assert contact["C"].shape == (N, N)
assert int(contact["endpoint"]) == 6

print("D215 computing Gamma V200", flush=True)
gamma = d147.exact_gamma_block(N, DPS, T)
m0 = arb.pi().log() + arb.const_euler() + arb.pi() / 2 + 3 * arb(2).log()

centre = np.empty((N, N), dtype=float)
radius = np.empty((N, N), dtype=float)
for i in range(N):
    for j in range(N):
        value = gamma[i, j] + ball(contact["C"][i, j], contact["R"][i, j])
        if i == j:
            value -= m0
        centre[i, j] = float(value.mid())
        radius[i, j] = float(value.rad()) + abs(np.spacing(centre[i, j])) / 2

radius = np.nextafter(radius, np.inf)
centre = (centre + centre.T) / 2
radius = np.maximum(radius, radius.T)
assert np.isfinite(centre).all() and np.isfinite(radius).all()


def tate(n: int, sign: int) -> float:
    k = T / 2
    value = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2 * n + 1) / 2)
    if sign < 0 and n % 2:
        value = -value
    value *= (T * arb(2 * n + 1) / 2).sqrt()
    return float(value.mid())


jets = np.array([[tate(n, 1) for n in range(N)],
                 [tate(n, -1) for n in range(N)]])
_, _, vh = np.linalg.svd(jets, full_matrices=True)
Q = vh[2:].T
evals, V = np.linalg.eigh(Q.T @ centre @ Q)

operator_save = os.environ.get(
    "D215_OPERATOR_SAVE", "/tmp/t6_complete_operator_legendre.npz"
)
frame_save = os.environ.get(
    "D215_FRAME_SAVE", "/tmp/t6_direct_primitive_eigs.npz"
)
np.savez(operator_save, C=centre, R=radius, endpoint=np.array(6),
         digits=np.array(DPS))
np.savez(frame_save, Q=Q, V=V, e=evals, endpoint=np.array(6))

print("D215 max serialized operator radius", radius.max(), flush=True)
print("D215 primitive centre eigenvalues", evals[:8], flush=True)
print("saved", operator_save, frame_save, flush=True)
print("D215 DIRECTED SOURCE REBUILD: PASS (centres select frames only)")
