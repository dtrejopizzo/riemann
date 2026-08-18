#!/usr/bin/env python3
"""Non-directed sizing of the corrected D8/S190/Q200 Feshbach budget."""

from __future__ import annotations

import os
import numpy as np


T = 0.5 * np.log(6.0)


def digamma_complex(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=np.complex128)
    w = z + 20.0
    out = (
        np.log(w) - 1.0 / (2.0 * w) - 1.0 / (12.0 * w**2)
        + 1.0 / (120.0 * w**4) - 1.0 / (252.0 * w**6)
        + 1.0 / (240.0 * w**8) - 5.0 / (660.0 * w**10)
        + 691.0 / (32760.0 * w**12)
    )
    for j in range(20):
        out -= 1.0 / (z + j)
    return out


def synthesize(u: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    nmax, width = coeff.shape
    p0 = np.ones_like(u)
    ans = np.sqrt(1.0 / (2.0 * T)) * p0[:, None] * coeff[0]
    p1 = u.copy()
    ans += np.sqrt(3.0 / (2.0 * T)) * p1[:, None] * coeff[1]
    for n in range(2, nmax):
        p = ((2 * n - 1) * u * p1 - (n - 1) * p0) / n
        ans += np.sqrt((2 * n + 1) / (2.0 * T)) * p[:, None] * coeff[n]
        p0, p1 = p1, p
    return ans


def main() -> None:
    points = int(os.environ.get("D201_POINTS", str(2**17)))
    box = float(os.environ.get("D201_BOX", "32"))
    batch = int(os.environ.get("D201_BATCH", "16"))
    data = np.load("/tmp/t6_direct_primitive_eigs.npz")
    X = data["Q"] @ data["V"]
    lam = data["e"]

    dx = box / points
    x = (np.arange(points) - points // 2) * dx
    inside = np.flatnonzero(np.abs(x) <= T)
    u = x[inside] / T
    frequency = 2.0 * np.pi * np.fft.fftfreq(points, d=dx)
    psi_quarter = digamma_complex(np.array([0.25]))[0].real
    symbol = digamma_complex(0.25 + 0.5j * frequency).real - psi_quarter
    m0 = np.log(np.pi) - psi_quarter
    contacts = ((2, np.log(2.0)), (3, np.log(3.0)),
                (4, np.log(2.0)), (5, np.log(5.0)))

    total = np.zeros(len(lam))
    for start in range(0, len(lam), batch):
        stop = min(start + batch, len(lam))
        functions = np.zeros((points, stop - start))
        functions[inside] = synthesize(u, X[:, start:stop])
        acted = np.fft.ifft(
            np.fft.fft(functions, axis=0) * symbol[:, None], axis=0
        ).real
        acted -= m0 * functions
        for n, mangoldt in contacts:
            shift = np.log(float(n))
            weight = mangoldt / np.sqrt(float(n))
            for j in range(stop - start):
                acted[inside, j] -= weight * (
                    np.interp(x[inside] + shift, x, functions[:, j], left=0, right=0)
                    + np.interp(x[inside] - shift, x, functions[:, j], left=0, right=0)
                )
        total[start:stop] = dx * np.sum(acted[inside] ** 2, axis=0)
        print("batch", start, stop, flush=True)

    residual_upper = np.maximum(total - lam**2, 0.0)
    ratios = residual_upper / lam
    for slow in (2, 4, 6, 8, 10, 12, 16, 24, 32):
        print(
            "slow", slow,
            "safe_min", lam[slow],
            "trace_kappa_majorant", np.sum(ratios[slow:]),
            "max_ratio", np.max(ratios[slow:]),
        )
    print("first 16 lambda", lam[:16])
    print("first 16 total action2", total[:16])
    print("first 16 residual upper", residual_upper[:16])
    np.savez(
        "/tmp/t6_safe_tail_fft_diagnostic.npz",
        eigenvalues=lam, total_action2=total,
        residual_upper=residual_upper, ratios=ratios,
        points=points, box=box,
    )
    print("D201 diagnostic only; no directed sign asserted")


if __name__ == "__main__":
    main()
