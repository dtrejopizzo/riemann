#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, lstsq, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    prime = h_model - h_actual
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    return h_actual, h_model, prime, vals[0], d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def residual_against_plane(row, plane_rows):
    coeff, *_ = lstsq(plane_rows.T, row, rcond=None)
    fit = coeff @ plane_rows
    return coeff, row - fit


def rce_components(plane, op, xi):
    coeffs = []
    residuals = []
    evals = []
    for j in range(2):
        row = plane[j] @ op
        coeff, residual = residual_against_plane(row, plane)
        coeffs.append(coeff)
        residuals.append(residual)
        evals.append(residual @ xi)
    return np.array(coeffs), np.array(residuals), np.array(evals)


def run():
    print("E73.155 RCE component probe")
    print("Splits Cauchy-plane evaluated residual into model and prime parts.")
    print("actual = model - prime, prime=h_model-h_actual.")
    print("modelB/primeB/signedB are log_L l1 evaluated residuals over the two Cauchy rows.")
    print(" lam     L gamma   modelB  primeB signedB cancelB   hB  invB status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        h_actual, h_model, prime, mu, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:3]:
            w = -1j * gamma
            plane = cauchy_rows(w, d)
            coeff_actual, _, eval_actual = rce_components(plane, h_actual, xi)
            _, _, eval_model = rce_components(plane, h_model, xi)
            _, _, eval_prime = rce_components(plane, prime, xi)
            signed = eval_model - eval_prime
            recon = norm(signed - eval_actual)
            model_l1 = np.sum(np.abs(eval_model))
            prime_l1 = np.sum(np.abs(eval_prime))
            signed_l1 = np.sum(np.abs(signed))
            cancel_ratio = signed_l1 / max(model_l1 + prime_l1, 1e-300)
            hvec = np.array([plane[0] @ xi, plane[1] @ xi])
            h_l1 = np.sum(np.abs(hvec))
            inv_norm = norm(np.linalg.inv(mu * np.eye(2) - coeff_actual), ord=2)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(model_l1, L):8.3f}"
                f" {bexp(prime_l1, L):7.3f}"
                f" {bexp(signed_l1, L):7.3f}"
                f" {bexp(cancel_ratio, L):8.3f}"
                f" {bexp(h_l1, L):6.3f}"
                f" {bexp(inv_norm, L):6.3f}"
                f" {'PASS' if signed_l1 * inv_norm <= L**-17 else 'FAIL'}"
            )
            if recon > 1e-8:
                raise RuntimeError(f"component reconstruction failed: {recon}")


if __name__ == "__main__":
    run()
