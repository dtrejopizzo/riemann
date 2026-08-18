#!/usr/bin/env python3
"""Finite-dimensional audit of the identities in 106.177."""

import numpy as np


def random_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    phase = np.diag(r)
    phase = np.where(np.abs(phase) > 0, phase / np.abs(phase), 1.0)
    return q @ np.diag(np.conjugate(phase))


def main() -> None:
    rng = np.random.default_rng(106177)
    n = 7
    base = [random_unitary(rng, n) for _ in range(5)]
    unitaries = base + [u.conj().T for u in base]
    half_weights = rng.uniform(0.1, 2.0, size=len(base))
    weights = np.concatenate([half_weights, half_weights])
    c_mass = float(np.sum(weights))
    a_op = sum(w * u for w, u in zip(weights, unitaries))

    f = rng.normal(size=n) + 1j * rng.normal(size=n)
    psi_x = [np.sqrt(w / 2.0) * f for w in weights]
    psi_y = [np.sqrt(w / 2.0) * (u @ f)
             for w, u in zip(weights, unitaries)]
    mean_x = sum(np.sqrt(w) * x for w, x in zip(weights, psi_x)) / c_mass
    mean_y = sum(np.sqrt(w) * y for w, y in zip(weights, psi_y)) / c_mass
    proj_x = [x - np.sqrt(w) * mean_x for w, x in zip(weights, psi_x)]
    proj_y = [y - np.sqrt(w) * mean_y for w, y in zip(weights, psi_y)]
    projected_norm = sum(np.vdot(x, x).real for x in proj_x)
    projected_norm += sum(np.vdot(y, y).real for y in proj_y)

    formula_13 = c_mass * np.vdot(f, f).real / 2.0
    formula_13 -= np.vdot(a_op @ f, a_op @ f).real / (2.0 * c_mass)

    energy = c_mass * np.vdot(f, f).real - np.vdot(f, a_op @ f).real
    residual_square = np.vdot((c_mass * np.eye(n) - a_op) @ f,
                              (c_mass * np.eye(n) - a_op) @ f).real
    formula_15 = projected_norm + residual_square / (2.0 * c_mass)

    selfadjoint_error = np.linalg.norm(a_op - a_op.conj().T)
    print(f"self-adjoint pairing error: {selfadjoint_error:.3e}")
    print(f"identity (13) error: {abs(projected_norm - formula_13):.3e}")
    print(f"identity (15) error: {abs(energy - formula_15):.3e}")
    print(f"projected norm: {projected_norm:.12e}")
    print(f"regression square: {residual_square / (2.0 * c_mass):.12e}")


if __name__ == "__main__":
    main()
