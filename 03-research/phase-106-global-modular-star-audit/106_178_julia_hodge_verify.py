#!/usr/bin/env python3
"""Finite-dimensional audit of the Julia identities in 106.178."""

import numpy as np


def main() -> None:
    rng = np.random.default_rng(106178)
    n = 9
    eig = rng.uniform(-0.95, 0.95, size=n)
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, _ = np.linalg.qr(z)
    t_op = q @ np.diag(eig) @ q.conj().T
    d_op = q @ np.diag(np.sqrt(1.0 - eig**2)) @ q.conj().T
    s_op = np.block([[t_op, d_op], [d_op, -t_op]])
    ident = np.eye(2 * n)

    c_mass = 7.3
    f = rng.normal(size=n) + 1j * rng.normal(size=n)
    g = rng.normal(size=n) + 1j * rng.normal(size=n)
    i0f = np.concatenate([f, np.zeros(n, dtype=complex)])
    i0g = np.concatenate([g, np.zeros(n, dtype=complex)])
    compression = -c_mass * np.vdot(i0g, s_op @ i0f)
    expected = -c_mass * np.vdot(g, t_op @ f)

    k_plus = q @ np.diag((1.0 - eig) / np.sqrt(1.0 - eig**2)) @ q.conj().T
    graph = np.concatenate([f, k_plus @ f])
    graph_error = np.linalg.norm(s_op @ graph - graph)

    # Odd doubling: the swap anticommutes with diag(T,-T) and solves (23d).
    zero = np.zeros_like(t_op)
    t_hat = np.block([[t_op, zero], [zero, -t_op]])
    d_hat = np.block([[d_op, zero], [zero, d_op]])
    swap = np.block([[zero, np.eye(n)], [np.eye(n), zero]])
    anti_error = np.linalg.norm(swap @ t_hat + t_hat @ swap)
    riccati_error = np.linalg.norm(
        d_hat - t_hat @ swap - swap @ (t_hat + d_hat @ swap)
    )

    print(f"self-adjoint error: {np.linalg.norm(s_op-s_op.conj().T):.3e}")
    print(f"involution error: {np.linalg.norm(s_op@s_op-ident):.3e}")
    print(f"compression error: {abs(compression-expected):.3e}")
    print(f"positive-graph error: {graph_error:.3e}")
    print(f"odd anticommutator error: {anti_error:.3e}")
    print(f"odd Riccati error: {riccati_error:.3e}")


if __name__ == "__main__":
    main()
