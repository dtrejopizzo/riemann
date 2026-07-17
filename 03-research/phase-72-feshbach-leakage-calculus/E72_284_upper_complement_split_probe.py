#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def upper_split(lam, n_modes):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    delta = c_actual - c_model
    va = eigvalsh(c_actual)
    vm = eigvalsh(c_model)
    vd = eigvalsh(delta)
    return {
        "lam": lam,
        "L": L,
        "dim": c_actual.shape[0],
        "op_actual": float(va[-1]),
        "op_model": float(vm[-1]),
        "delta_pos": float(max(vd[-1], 0.0)),
        "delta_abs": float(max(abs(vd[0]), abs(vd[-1]))),
        "delta_min": float(vd[0]),
        "delta_max": float(vd[-1]),
        "min_actual": float(va[0]),
        "min_model": float(vm[0]),
    }


def run():
    print("E72.284 upper-complement split probe")
    print("C_actual=C_model+Delta_arith in the corrected pole-even complement.")
    print("op(C_actual) <= op(C_model)+lambda_max(Delta_arith)_+.")
    print("lam L dim opA/L2 opM/L2 posDelta/L2 absDelta/L2 minA/L2 minM/L2 dMin/L2 dMax/L2")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        r = upper_split(lam, n_modes)
        L2 = r["L"] * r["L"]
        print(
            f"{r['lam']:3.0f} {r['L']:.6f} {r['dim']:3d} "
            f"{r['op_actual'] / L2:.6e} "
            f"{r['op_model'] / L2:.6e} "
            f"{r['delta_pos'] / L2:.6e} "
            f"{r['delta_abs'] / L2:.6e} "
            f"{r['min_actual'] / L2:.6e} "
            f"{r['min_model'] / L2:.6e} "
            f"{r['delta_min'] / L2:.6e} "
            f"{r['delta_max'] / L2:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
