#!/usr/bin/env python3
"""Direct Arb audit of the two candidate T=(log 6)/2 witnesses.

This deliberately bypasses every Schur inverse.  It freezes only the tail
Legendre coefficients selected by the exploratory hierarchy, solves the two
Tate equations afresh, and evaluates the complete Gamma/contact matrix as a
single quadratic form.
"""
import importlib.util
import os
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx


HERE = Path(__file__).resolve().parent
N = 200
DPS = int(os.environ.get("D189_DPS", "1100"))
ctx.dps = DPS
T = arb(6).log() / 2

sp = importlib.util.spec_from_file_location(
    "gamma_direct", HERE / "114_d_147_hurwitz_gamma_arb.py"
)
gamma_direct = importlib.util.module_from_spec(sp)
sp.loader.exec_module(gamma_direct)

candidate = np.load(os.environ.get("D189_CANDIDATE", "/tmp/t6_negative_candidate.npz"))
contacts = np.load(os.environ.get("D189_CONTACT", "/tmp/d185_contacts6_arb.npz"))
assert int(contacts["endpoint"]) == 6
assert contacts["C"].shape == (N, N)


def ball(center, radius):
    radius = np.nextafter(float(radius), np.inf) + abs(np.spacing(float(center))) / 2
    return arb(repr(float(center)), repr(float(radius)))


def tate(n, sign):
    k = T / 2
    integ = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2 * n + 1) / 2)
    if sign < 0 and n % 2:
        integ = -integ
    return (T * arb(2 * n + 1) / 2).sqrt() * integ


gp = [tate(n, 1) for n in range(N)]
gm = [tate(n, -1) for n in range(N)]
moment_head = arb_mat([[gp[0], gp[1]], [gm[0], gm[1]]])

# One exact complete matrix, evaluated without any ill-conditioned Schur map.
gamma = gamma_direct.exact_gamma_block(N, DPS, T)
contact = arb_mat(N, N)
for i in range(N):
    for j in range(N):
        contact[i, j] = ball(contacts["C"][i, j], contacts["R"][i, j])
m0 = arb.pi().log() + arb.const_euler() + arb.pi() / 2 + 3 * arb(2).log()

for column in range(2):
    # The binary64 tail is declared exact input; only c_0,c_1 are changed.
    tail = [arb(repr(float(candidate["witness_C"][j, column]))) for j in range(2, N)]
    rhs = arb_mat([
        [-sum((gp[j] * tail[j - 2] for j in range(2, N)), arb(0))],
        [-sum((gm[j] * tail[j - 2] for j in range(2, N)), arb(0))],
    ])
    head = moment_head.inv() * rhs
    coeff = [head[0, 0], head[1, 0]] + tail
    v = arb_mat([[x] for x in coeff])
    norm = (v.transpose() * v)[0, 0]
    q_gamma = (v.transpose() * gamma * v)[0, 0]
    q_contact = (v.transpose() * contact * v)[0, 0]
    q_total = q_gamma + q_contact - m0 * norm
    rayleigh = q_total / norm
    jet_plus = sum((gp[j] * coeff[j] for j in range(N)), arb(0))
    jet_minus = sum((gm[j] * coeff[j] for j in range(N)), arb(0))
    print("candidate", column, flush=True)
    print("  norm =", norm, flush=True)
    print("  gamma_minus_m0 =", q_gamma - m0 * norm, flush=True)
    print("  contacts_2_3_4_5 =", q_contact, flush=True)
    print("  total =", q_total, flush=True)
    print("  physical_Rayleigh =", rayleigh, flush=True)
    print("  Tate_plus =", jet_plus, flush=True)
    print("  Tate_minus =", jet_minus, flush=True)

print("D189 direct T6 candidate audit completed (no sign asserted)")
