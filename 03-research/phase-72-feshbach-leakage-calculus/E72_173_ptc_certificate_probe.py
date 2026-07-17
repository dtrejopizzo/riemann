#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_166_residual_sign_gram_probe import spectral_parts  # noqa: E402
from E72_172_polynomial_majorant_certificate import C0, C1  # noqa: E402


def trace_poly(mat, coeff):
    total = coeff[0] * mat.shape[0]
    power = np.eye(mat.shape[0])
    for k in range(1, len(coeff)):
        power = power @ mat
        total += coeff[k] * np.trace(power)
    return float(np.real(total))


def block_energy(mat, a):
    pos, neg = spectral_parts(mat)
    return ((1.0 - a) ** 2) * norm(pos, "fro") ** 2 + norm(neg, "fro") ** 2


def row(lam, n_modes):
    idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
    k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
    p0, n0 = spectral_parts(k0)
    p1, n1 = spectral_parts(k1)
    residual = 0.30 * p0 + n0 + 0.40 * p1 + n1
    e0 = 0.09 * norm(p0, "fro") ** 2 + norm(n0, "fro") ** 2
    e1 = 0.16 * norm(p1, "fro") ** 2 + norm(n1, "fro") ** 2
    bse = e0 + e1
    dist2 = norm(residual, "fro") ** 2
    cross_plus = max(0.0, dist2 - bse)
    poly0 = trace_poly(k0, C0)
    poly1 = trace_poly(k1, C1)
    op0 = float(np.max(np.abs(eigvalsh(k0))))
    op1 = float(np.max(np.abs(eigvalsh(k1))))
    return {
        "lam": lam,
        "L": L,
        "dim": k0.shape[0],
        "op0": op0,
        "op1": op1,
        "poly": poly0 + poly1,
        "poly0": poly0,
        "poly1": poly1,
        "bse": bse,
        "cross_plus": cross_plus,
        "ptc_total": poly0 + poly1 + cross_plus,
        "dist": np.sqrt(dist2),
        "margin": 1.0 - dist2,
    }


def run():
    print("E72.173 PTC certificate probe")
    print("cut=0.60; weights=(0.70,0.60); intervals K0<=0.90,K1<=0.60")
    print(" lam    L  dim   op0   op1  traceP  cross+  PTCsum  dist  margin  pass")
    windows = [
        (6, 18),
        (8, 24),
        (10, 28),
        (12, 32),
        (14, 36),
        (16, 40),
        (18, 44),
        (20, 48),
        (22, 52),
        (24, 56),
    ]
    worst = {"ptc_total": -np.inf, "lam": None}
    for lam, n_modes in windows:
        s = row(lam, n_modes)
        ok = s["op0"] <= 0.90 and s["op1"] <= 0.60 and s["ptc_total"] < 1.0
        if s["ptc_total"] > worst["ptc_total"]:
            worst = s
        print(
            f"{lam:4.0f} {s['L']:5.2f} {s['dim']:4d} "
            f"{s['op0']:5.3f} {s['op1']:5.3f} "
            f"{s['poly']:7.3f} {s['cross_plus']:7.3f} "
            f"{s['ptc_total']:7.3f} {s['dist']:5.3f} "
            f"{s['margin']:7.3f} {'YES' if ok else 'NO'}"
        )
        sys.stdout.flush()
    print(
        f"worst_PTCsum={worst['ptc_total']:.3f} "
        f"at lambda={worst['lam']:.0f}; "
        f"traceP={worst['poly']:.3f}; cross+={worst['cross_plus']:.3f}"
    )


if __name__ == "__main__":
    run()
