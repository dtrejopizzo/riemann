#!/usr/bin/env python3
"""Independent scalar audit of a T=log(6)/2 Legendre witness.

This script does not use the directed Schur complement or its reduced
matrix.  Gamma is evaluated from the physical zero-extension difference
form; contacts are evaluated as direct overlap integrals.  An optional FFT
evaluation supplies a second Gamma representation.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss, legval


T = 0.5 * math.log(6.0)
RMAX = 2.0 * T
CONTACTS = ((2, math.log(2.0)), (3, math.log(3.0)),
            (4, math.log(2.0)), (5, math.log(5.0)))
M0 = math.log(math.pi) + float(mp.euler) + math.pi / 2.0 + 3.0 * math.log(2.0)


def load_witness(path: Path, column: int) -> tuple[np.ndarray, np.ndarray | None]:
    z = np.load(path, allow_pickle=True)
    for key in ("witness_C", "witness", "W", "coefficients"):
        if key in z:
            a = np.asarray(z[key], dtype=float)
            if a.ndim == 1:
                w = a
            else:
                w = a[:, column]
            radii = None
            for rk in ("witness_R", "witness_radii", "WR"):
                if rk in z:
                    rr = np.asarray(z[rk], dtype=float)
                    radii = rr if rr.ndim == 1 else rr[:, column]
                    break
            return w, radii
    raise KeyError(f"no witness coefficient array in {path}; keys={z.files}")


def physical_coefficients(w: np.ndarray) -> np.ndarray:
    n = np.arange(len(w), dtype=float)
    return w * np.sqrt((2.0 * n + 1.0) / (2.0 * T))


def eval_f(t: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    return legval(np.asarray(t) / T, coeff)


def integrate_interval_values(
    left: np.ndarray, right: np.ndarray, xi: np.ndarray, wi: np.ndarray,
    coeff: np.ndarray, kind: str, shift: np.ndarray | None = None,
) -> np.ndarray:
    """Vectorized Gauss integrals over one interval per row."""
    left = np.asarray(left)
    right = np.asarray(right)
    mid = 0.5 * (left + right)
    half = 0.5 * (right - left)
    t = mid[:, None] + half[:, None] * xi[None, :]
    ft = eval_f(t, coeff)
    if kind == "square":
        val = ft * ft
    elif kind == "difference":
        assert shift is not None
        fs = eval_f(t + np.asarray(shift)[:, None], coeff)
        val = (fs - ft) ** 2
    else:
        raise ValueError(kind)
    return half * (val @ wi)


def gamma_physical(w: np.ndarray, q_outer: int, q_inner: int) -> float:
    """Gamma quadratic form via positive zero-extension differences."""
    coeff = physical_coefficients(w)
    xo, wo = leggauss(q_outer)
    xi, wi = leggauss(q_inner)
    r_all = T * (xo + 1.0)  # [0,2T]
    wr_all = T * wo
    dvals = np.empty_like(r_all)
    chunk = 32
    for start in range(0, q_outer, chunk):
        r = r_all[start : start + chunk]
        left_boundary = integrate_interval_values(
            np.full_like(r, -T), -T + r, xi, wi, coeff, "square"
        )
        right_boundary = integrate_interval_values(
            T - r, np.full_like(r, T), xi, wi, coeff, "square"
        )
        interior = integrate_interval_values(
            np.full_like(r, -T), T - r, xi, wi, coeff,
            "difference", shift=r,
        )
        dvals[start : start + len(r)] = left_boundary + right_boundary + interior
    kernel = np.exp(-r_all / 2.0) / (-np.expm1(-2.0 * r_all))
    finite = float(np.dot(wr_all, kernel * dvals))

    mp.mp.dps = 60
    y = mp.e ** (-mp.mpf(RMAX) / 2)
    tail_kernel = 2 * mp.quad(lambda z: 1 / (1 - z**4), [0, y])
    norm = float(np.dot(w, w))
    tail = 2.0 * norm * float(tail_kernel)
    return finite + tail


def direct_contacts_and_jets(w: np.ndarray, q: int = 360) -> dict[str, float]:
    coeff = physical_coefficients(w)
    x, weights = leggauss(q)

    # Norm and jets on the full physical interval.
    t = T * x
    f = eval_f(t, coeff)
    norm_quad = T * float(np.dot(weights, f * f))
    jet_plus = T * float(np.dot(weights, np.exp(t / 2.0) * f))
    jet_minus = T * float(np.dot(weights, np.exp(-t / 2.0) * f))

    out: dict[str, float] = {
        "norm_coeff": float(np.dot(w, w)),
        "norm_quad": norm_quad,
        "jet_plus": jet_plus,
        "jet_minus": jet_minus,
    }
    contact_total = 0.0
    for n, lam in CONTACTS:
        shift = math.log(float(n))
        left, right = -T, T - shift
        mid, half = 0.5 * (left + right), 0.5 * (right - left)
        tt = mid + half * x
        corr = half * float(np.dot(weights, eval_f(tt, coeff) * eval_f(tt + shift, coeff)))
        term = -2.0 * lam / math.sqrt(float(n)) * corr
        out[f"corr_{n}"] = corr
        out[f"minusB_contact_{n}"] = term
        contact_total += term
    out["minusB_contacts"] = contact_total
    out["minusB_scalar"] = -M0 * out["norm_coeff"]
    return out


def digamma_real_quarter(tau: np.ndarray) -> np.ndarray:
    """Vectorized Re psi(1/4+i*tau/2)-psi(1/4)."""
    z0 = 0.25 + 0.5j * np.asarray(tau, dtype=float)
    shift = 14
    z = z0 + shift
    # Bernoulli asymptotic through B_16.
    psi = np.log(z) - 0.5 / z
    bernoulli = (
        (2, 1.0 / 6.0), (4, -1.0 / 30.0), (6, 1.0 / 42.0),
        (8, -1.0 / 30.0), (10, 5.0 / 66.0),
        (12, -691.0 / 2730.0), (14, 7.0 / 6.0),
        (16, -3617.0 / 510.0),
    )
    for power, b in bernoulli:
        psi -= b / (power * z**power)
    for k in range(shift):
        psi -= 1.0 / (z0 + k)
    psi_quarter = -float(mp.euler) - math.pi / 2.0 - 3.0 * math.log(2.0)
    return psi.real - psi_quarter


def gamma_fft(w: np.ndarray, nfft: int, half_length: float) -> tuple[float, float]:
    """Independent Fourier-grid Gamma check (truncated at Nyquist)."""
    coeff = physical_coefficients(w)
    dx = 2.0 * half_length / nfft
    t = -half_length + dx * np.arange(nfft)
    f = np.zeros(nfft)
    mask = np.abs(t) <= T
    f[mask] = eval_f(t[mask], coeff)
    fhat = dx * np.fft.fft(f)
    tau = 2.0 * math.pi * np.fft.fftfreq(nfft, d=dx)
    dtau = 2.0 * math.pi / (2.0 * half_length)
    h = digamma_real_quarter(tau)
    gamma = float(dtau / (2.0 * math.pi) * np.dot(h, np.abs(fhat) ** 2))
    parseval = float(dtau / (2.0 * math.pi) * np.dot(np.abs(fhat) ** 2, np.ones(nfft)))
    return gamma, parseval


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--column", type=int, default=0)
    parser.add_argument("--fft", action="store_true")
    parser.add_argument(
        "--certify-artifact",
        action="store_true",
        help="assert the independently audited sign and reject the wide Schur ball",
    )
    args = parser.parse_args()

    w, radii = load_witness(args.path, args.column)
    print(f"witness length={len(w)}, coefficient norm={np.linalg.norm(w):.17e}")
    if radii is not None:
        print(f"max coefficient radius={np.max(radii):.3e}")

    pieces = direct_contacts_and_jets(w)
    for key, value in pieces.items():
        print(f"{key:24s} = {value:.17e}")

    gamma_values = []
    totals = []
    for qo in (320, 480, 640, 800):
        value = gamma_physical(w, qo, 240)
        gamma_values.append(value)
        total = value + pieces["minusB_contacts"] + pieces["minusB_scalar"]
        totals.append(total)
        print(f"Gamma physical q={qo:4d} = {value:.17e};  -B total={total:.17e}")
    print(f"Gamma physical spread = {max(gamma_values)-min(gamma_values):.3e}")

    if args.certify_artifact:
        z = np.load(args.path, allow_pickle=True)
        assert args.column == 0, "the directed artifact certificate is for column zero"
        assert radii is not None and float(np.max(radii)) > 100.0
        assert "rayleigh" in z
        lower = float(z["rayleigh"][0, 0])
        upper = float(z["rayleigh"][0, 1])
        assert lower < 0.0 < upper
        assert min(totals) > 4.0e-9
        assert max(totals) < 5.0e-9
        assert max(gamma_values) - min(gamma_values) < 3.0e-13
        print("PASS: T6 negative Schur centre is an uncertified interval artifact")

    if args.fft:
        for power, scale in ((20, 32.0), (21, 48.0), (22, 64.0)):
            gf, pv = gamma_fft(w, 1 << power, scale * T)
            total = gf + pieces["minusB_contacts"] + pieces["minusB_scalar"]
            print(
                f"Gamma FFT N=2^{power}, L={scale:.0f}T = {gf:.17e}; "
                f"parseval={pv:.17e}; -B total={total:.17e}"
            )


if __name__ == "__main__":
    main()
