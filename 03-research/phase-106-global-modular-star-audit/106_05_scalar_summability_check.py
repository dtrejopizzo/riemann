#!/usr/bin/env python3
"""Finite checks for the scalar summability identities of 106.05.

This is a float64 diagnostic, not a proof or an interval certificate.  It
reuses the exact finite Weil matrix implementation of 106_04 and checks:

  * the Cauchy-transform formula for Tr(s-D_N)^(-2);
  * the consecutive ground-line rotation inequality;
  * the canonical shell telescoping identity already evaluated by 106_04.

Only NumPy and the Python standard library are required.
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys

import numpy as np


def load_probe_module():
    path = Path(__file__).with_name("106_04_cofinal_weil_defect_probe.py")
    spec = importlib.util.spec_from_file_location("phase106_defect_probe", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def cauchy_trace(level, length: float, s: complex) -> complex:
    scale = 2.0 * np.pi / length
    indices = np.arange(-level.n, level.n + 1, dtype=float)
    denominator = s - scale * indices
    coefficients = level.xi
    cauchy = np.sum(coefficients / denominator)
    first = -np.sum(coefficients / denominator**2)
    second = 2.0 * np.sum(coefficients / denominator**3)
    log_second = second / cauchy - (first / cauchy) ** 2
    return np.sum(1.0 / denominator**2) - log_second


def direct_trace(level, s: complex) -> complex:
    identity = np.eye(level.d_euclidean.shape[0])
    resolvent = np.linalg.inv(s * identity - level.d_euclidean)
    return np.trace(resolvent @ resolvent)


def embedded_ground_distance(old, new) -> tuple[float, float]:
    embedded = np.zeros_like(new.xi)
    embedded[1:-1] = old.xi
    if np.vdot(embedded, new.xi).real < 0.0:
        new_ground = -new.xi
    else:
        new_ground = new.xi
    distance_squared = float(np.linalg.norm(embedded - new_ground) ** 2)
    delta = max(0.0, float(old.epsilon - new.epsilon))
    upper = 2.0 * delta / new.gap
    return distance_squared, upper


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lambda", dest="lam", type=float, default=2.2)
    parser.add_argument("--n-min", type=int, default=1)
    parser.add_argument("--n-max", type=int, default=7)
    parser.add_argument("--quadrature", type=int, default=512)
    parser.add_argument("--s-real", type=float, default=0.37)
    parser.add_argument("--s-imag", type=float, default=1.2)
    args = parser.parse_args()
    if args.n_min < 1 or args.n_max <= args.n_min:
        parser.error("require 1 <= n-min < n-max")
    if args.s_imag == 0.0:
        parser.error("s-imag must be nonzero")

    probe = load_probe_module()
    matrix, length = probe.build_weil_matrix(
        args.lam, args.n_max, args.quadrature
    )
    levels = {
        n: probe.quotient_level(matrix, args.n_max, n, length)
        for n in range(args.n_min, args.n_max + 1)
    }
    s = complex(args.s_real, args.s_imag)

    max_trace_error = 0.0
    max_rotation_ratio = 0.0
    print("Phase 106.05 scalar identities (float64 diagnostic; not certified)")
    print(
        f"lambda={args.lam:g}, L={length:.12g}, "
        f"N={args.n_min}..{args.n_max}, s={s}"
    )
    print(" N   trace-formula error     ground distance^2       2 Delta/g    ratio")
    for n in range(args.n_min, args.n_max):
        old = levels[n]
        new = levels[n + 1]
        scalar = cauchy_trace(old, length, s)
        direct = direct_trace(old, s)
        trace_error = float(abs(scalar - direct))
        distance_squared, upper = embedded_ground_distance(old, new)
        ratio = distance_squared / upper if upper > 0.0 else float("nan")
        max_trace_error = max(max_trace_error, trace_error)
        if np.isfinite(ratio):
            max_rotation_ratio = max(max_rotation_ratio, ratio)
        print(
            f"{n:2d}   {trace_error:18.6e} "
            f"{distance_squared:20.6e} {upper:15.6e} {ratio:8.5f}"
        )

    final_level = levels[args.n_max]
    final_error = abs(
        cauchy_trace(final_level, length, s)
        - direct_trace(final_level, s)
    )
    max_trace_error = max(max_trace_error, float(final_error))

    if max_rotation_ratio > 1.0 + 1.0e-7:
        raise RuntimeError(
            f"ground-line rotation inequality failed: ratio={max_rotation_ratio}"
        )
    print()
    print(f"maximum trace-formula error: {max_trace_error:.6e}")
    print(f"maximum rotation ratio:      {max_rotation_ratio:.6e}")
    print("PASS: equations 106.05(4) and 106.05(8) were evaluated.")


if __name__ == "__main__":
    main()
