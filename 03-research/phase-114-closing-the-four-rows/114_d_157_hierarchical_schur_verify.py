#!/usr/bin/env python3
"""Check the hierarchical Schur congruence and perturbation budget."""

import numpy as np


def main() -> None:
    rng = np.random.default_rng(157)
    r, s = 5, 31
    z = rng.normal(size=(s, s))
    lss = z.T @ z + 0.08 * np.eye(s)
    lds = 2.0e-4 * rng.normal(size=(r, s))
    schur = np.diag(np.linspace(3.0e-5, 7.0e-3, r))
    ldd = schur + lds @ np.linalg.solve(lss, lds.T)
    full = np.block([[ldd, lds], [lds.T, lss]])

    recovered = ldd - lds @ np.linalg.solve(lss, lds.T)
    assert np.linalg.norm(recovered - schur) < 2.0e-14
    assert np.linalg.eigvalsh(full)[0] > 0.0

    eta = np.linalg.eigvalsh(lss)[0]
    correction = lds @ np.linalg.solve(lss, lds.T)
    upper = np.linalg.norm(lds, 2) ** 2 / eta
    assert np.linalg.eigvalsh(correction)[0] >= -2.0e-14
    assert np.linalg.norm(correction, 2) <= upper * (1 + 2.0e-13)

    print("D157 hierarchical directed Schur identities: PASS")
    print(f"safe gap = {eta:.12g}")
    print(f"Schur minimum = {np.linalg.eigvalsh(recovered)[0]:.12g}")


if __name__ == "__main__":
    main()
