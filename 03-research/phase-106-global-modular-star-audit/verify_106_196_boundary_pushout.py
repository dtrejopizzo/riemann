#!/usr/bin/env python3
"""Finite-dimensional algebra audit for 106.196."""

import numpy as np


def main():
    rng = np.random.default_rng(106196)
    kappa = 2.7
    boundary_dim = 5
    extra_dim = 7

    # B*B = kappa I, with B embedding into a larger archimedean page.
    q, _ = np.linalg.qr(rng.normal(size=(extra_dim, boundary_dim)))
    b_inf = np.sqrt(kappa) * q
    beta = b_inf.T

    # A complex-linear Tate boundary row is represented by two copies.
    domain_dim = 9
    r = rng.normal(size=(boundary_dim, domain_dim))
    rj = rng.normal(size=(boundary_dim, domain_dim))
    boundary = np.vstack([rj, r])
    b_double = np.block(
        [[b_inf, np.zeros_like(b_inf)], [np.zeros_like(b_inf), b_inf]]
    )
    beta_double = b_double.T

    # Canonical archimedean lift of -boundary.
    lift = -(b_double @ boundary) / kappa
    pushout_error = np.linalg.norm(boundary + beta_double @ lift)

    # Schur/minimum-norm identity.
    graph_energy = lift.T @ lift
    expected = boundary.T @ boundary / kappa
    metric_error = np.linalg.norm(graph_energy - expected)

    projector_error = np.linalg.norm(beta @ b_inf - kappa * np.eye(boundary_dim))
    print("boundary constraint error:", f"{pushout_error:.3e}")
    print("minimum graph-metric error:", f"{metric_error:.3e}")
    print("B*B normalization error:", f"{projector_error:.3e}")


if __name__ == "__main__":
    main()
