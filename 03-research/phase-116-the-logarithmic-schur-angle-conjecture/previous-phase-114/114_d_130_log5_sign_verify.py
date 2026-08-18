#!/usr/bin/env python3
"""Verifier for the D.130 sign/normalization audit.

This verifies one selected floating candidate; it is not an endpoint
positivity certificate.  If the saved Galerkin assembly is absent, the
script regenerates it with the corrected common-refinement contacts.
"""

from __future__ import annotations

import math
import os
from pathlib import Path
import subprocess
import sys

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander


HERE = Path(__file__).resolve().parent
DATA = Path("/tmp/d83_degree9.npz")

if not DATA.exists():
    env = dict(os.environ)
    env.update(D83_LOG5="1", D83_SAVE="1")
    subprocess.run(
        [sys.executable, str(HERE / "114_d_83_log2_complement_float_diagnostic.py")],
        check=True,
        env=env,
    )

# Exact two-jet/Mellin-coordinate convention.
assert abs((0.5 - 1j * (-0.5j)) - 0.0) < 1e-15
assert abs((0.5 - 1j * (0.5j)) - 1.0) < 1e-15

# Reconstruct the original selected vector.  The saved AP now contains the
# corrected common-refinement contacts.  To audit the original candidate,
# replace those blocks by the old midpoint-matched blocks *only for the
# selection step*.  All reported contact values are then recomputed by the
# correct common-refinement integral.
D = 10
NC = 109
T = 0.5 * math.log(5)
g1, g2, g3 = math.log(5 / 4), math.log(4 / 3), math.log(6 / 5)
hs = np.asarray(
    [g1 / 15] * 15
    + [g2 / 20] * 20
    + [g3 / 12] * 12
    + [g1 / 15] * 15
    + [g3 / 12] * 12
    + [g2 / 20] * 20
    + [g1 / 15] * 15
)
left = np.r_[-T, -T + np.cumsum(hs)[:-1]]
right = left + hs
mid = left + hs / 2
t, w = leggauss(80)
P = legvander(t, D - 1)


def contact_matrix(shift: float) -> np.ndarray:
    """Exact common-refinement translation matrix in the Galerkin basis."""
    tq, wq = leggauss(D)
    C = np.zeros((NC * D, NC * D))
    for i in range(NC):
        for j in range(NC):
            lo = max(left[i], left[j] - shift)
            hi = min(right[i], right[j] - shift)
            if not hi > lo + 2e-15:
                continue
            x = (lo + hi) / 2 + (hi - lo) * tq / 2
            wi = (hi - lo) * wq / 2
            ui = 2 * (x - mid[i]) / hs[i]
            uj = 2 * (x + shift - mid[j]) / hs[j]
            Bi = legvander(ui, D - 1) * np.sqrt(np.arange(1, 2 * D, 2) / hs[i])
            Bj = legvander(uj, D - 1) * np.sqrt(np.arange(1, 2 * D, 2) / hs[j])
            C[i * D : (i + 1) * D, j * D : (j + 1) * D] = Bi.T @ (
                wi[:, None] * Bj
            )
    return C


def midpoint_matrix(shift: float) -> np.ndarray:
    C = np.zeros((NC * D, NC * D))
    for i in range(NC):
        hit = np.where(np.abs(mid - (mid[i] + shift)) < 1e-12)[0]
        if len(hit):
            j = int(hit[0])
            C[i * D : (i + 1) * D, j * D : (j + 1) * D] = np.eye(D)
    return C


labels = [
    (2, math.log(2), math.log(2) / math.sqrt(2)),
    (3, math.log(3), math.log(3) / math.sqrt(3)),
    (4, 2 * math.log(2), math.log(2) / 2),
]
AP = np.load(DATA)["AP"].copy()
for _, shift, coeff in labels:
    C = contact_matrix(shift)
    M = midpoint_matrix(shift)
    AP += coeff * (C + C.T)
    AP -= coeff * (M + M.T)

# Exact Galerkin moments and exact numerical kernel in the even block.
mom = []
for sig in (0.5, -0.5):
    gv = []
    for h, m in zip(hs, mid):
        B = P * np.sqrt(np.arange(1, 2 * D, 2) / h)
        gv.extend(math.exp(sig * m) * B.T @ (h * w / 2 * np.exp(sig * h * t / 2)))
    mom.append(gv)
G = np.asarray(mom).T
A0 = AP - 1000 * G @ G.T
U = np.zeros((NC * D, 545))
col = 0
for i in range(54):
    for k in range(D):
        U[i * D + k, col] = 2**-0.5
        U[(NC - 1 - i) * D + k, col] = (-1) ** k * 2**-0.5
        col += 1
for k in range(D):
    if k % 2 == 0:
        U[54 * D + k, col] = 1
        col += 1
Bp, Cp = U.T @ A0 @ U, U.T @ G
_, _, vh = np.linalg.svd(Cp.T, full_matrices=True)
N = vh[1:].T
ev, V = np.linalg.eigh(N.T @ Bp @ N)
coef = U @ (N @ V[:, 0])
coef /= np.linalg.norm(coef)
assert np.linalg.norm(G.T @ coef) < 1e-13


def translated_correlation(shift: float, vector=coef) -> float:
    C = contact_matrix(shift)
    return float(vector @ C @ vector)


# Exact support and von Mangoldt weights at 2T=log(5).
contacts = []
for n, shift, coeff in labels:
    corr = translated_correlation(shift)
    contacts.append((n, corr, -2 * coeff * corr))
assert [n for n, _, _ in contacts] == [2, 3, 4]
assert abs(math.log(2) / math.sqrt(4) - math.log(2) / 2) < 1e-15

expected_corr = {
    2: 0.34836921944074883,
    3: -0.28308550468218385,
    4: 0.24362951941270861,
}
for n, corr, _ in contacts:
    assert abs(corr - expected_corr[n]) < 3e-13, (n, corr)

contact_total = sum(term for _, _, term in contacts)

# Direct Fourier evaluation of the complete Gamma multiplier on the same
# original selected vector.
tg, qg = leggauss(900)
tau, qw = 200 * (tg + 1) / 2, 100 * qg
mp.mp.dps = 25
symbol = np.asarray(
    [
        float(
            mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * mp.mpf(str(x))))
            - mp.log(mp.pi)
        )
        for x in tau
    ]
)


def gamma_value(vector: np.ndarray) -> float:
    X, W, F = [], [], []
    for i, (h, m) in enumerate(zip(hs, mid)):
        B = P * np.sqrt(np.arange(1, 2 * D, 2) / h)
        X.extend(m + h * t / 2)
        W.extend(h * w / 2)
        F.extend(B @ vector[i * D : (i + 1) * D])
    X, W, F = np.asarray(X), np.asarray(W), np.asarray(F)
    Fhat = np.exp(-1j * tau[:, None] * X[None, :]) @ (W * F)
    return float(np.sum(qw * abs(Fhat) ** 2 * symbol) / math.pi)


gamma_total = gamma_value(coef)
completed = contact_total + gamma_total
assert abs(contact_total - (-0.1512496093135758)) < 3e-13
assert abs(gamma_total - 0.20107034192592052) < 3e-13
assert abs(completed - 0.0498207326123447) < 5e-13
assert completed > 0

# Repeat the audit for the new lowest vector selected after correcting the AP
# contact blocks.  Its margin is tiny and floating, so it is only a stricter
# normalization stress test, never an endpoint certificate.
AP_correct = np.load(DATA)["AP"]
A0_correct = AP_correct - 1000 * G @ G.T
Bp_correct = U.T @ A0_correct @ U
ev_correct, V_correct = np.linalg.eigh(N.T @ Bp_correct @ N)
coef_correct = U @ (N @ V_correct[:, 0])
coef_correct /= np.linalg.norm(coef_correct)
assert np.linalg.norm(G.T @ coef_correct) < 1e-13
contacts_correct = []
for n, shift, coeff in labels:
    corr = translated_correlation(shift, coef_correct)
    contacts_correct.append((n, corr, -2 * coeff * corr))
contact_correct = sum(term for _, _, term in contacts_correct)
gamma_correct = gamma_value(coef_correct)
completed_correct = contact_correct + gamma_correct
assert abs(contact_correct - 0.12107035747200505) < 4e-13
assert abs(gamma_correct - (-0.12106998158145951)) < 4e-13
assert abs(completed_correct - 3.7589054554e-7) < 8e-13
assert completed_correct > 0

# The complete Gamma jump symbol, independently checked against its integral.
mp.mp.dps = 40
for tau in (mp.mpf("0.2"), mp.mpf("1.1"), mp.mpf("3.0")):
    integral = mp.quad(
        lambda r: 2 * mp.e ** (-r / 2) / (1 - mp.e ** (-2 * r))
        * (1 - mp.cos(tau * r)),
        [0, 1, mp.inf],
    )
    digamma = mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * tau)) - mp.digamma(
        mp.mpf(1) / 4
    )
    assert abs(integral - digamma) < mp.mpf("2e-16")

print("D130 log(5)/2 sign and normalization audit: PASS")
print(f"contact={contact_total:.16g}")
print(f"Gamma={gamma_total:.16g}")
print(f"QW={completed:.16g} > 0")
print(f"corrected-AP contact={contact_correct:.16g}")
print(f"corrected-AP Gamma={gamma_correct:.16g}")
print(f"corrected-AP QW={completed_correct:.16g} > 0 (floating audit only)")
