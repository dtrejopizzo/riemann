#!/usr/bin/env python3
"""Finite disk-model audit of the resonant Hardy quotient in 106.206."""

import numpy as np


def blaschke(z: complex, zero: complex) -> complex:
    return (z - zero) / (1.0 - np.conjugate(zero) * z)


def szego(z: complex, w: complex) -> complex:
    return 1.0 / (1.0 - z * np.conjugate(w))


def model_kernel(z: complex, w: complex, zeros: np.ndarray) -> complex:
    bz = np.prod([blaschke(z, zero) for zero in zeros])
    bw = np.prod([blaschke(w, zero) for zero in zeros])
    return (1.0 - bz * np.conjugate(bw)) * szego(z, w)


def main() -> None:
    # Symmetric planted divisor used only to audit the general model-space
    # identities; the construction in the document is defined by M_Xi.
    zeros = np.array([0.17 + 0.31j, -0.17 + 0.31j, 0.0 - 0.42j])
    gram = np.array(
        [[model_kernel(z, w, zeros) for w in zeros] for z in zeros]
    )
    hermitian_error = np.linalg.norm(gram - gram.conj().T)
    minimum_eigenvalue = float(np.min(np.linalg.eigvalsh(gram)))

    divisor_error = max(
        abs(np.prod([blaschke(z, zero) for zero in zeros])) for z in zeros
    )

    # Evaluation vectors are eigenvectors of the adjoint multiplier.
    time = 1.7
    diagonal = np.diag(np.exp(time * np.conjugate(zeros)))
    initial_norms = np.real(np.diag(gram))
    evolved_norms = np.real(np.diag(diagonal.conj().T @ gram @ diagonal))
    expected_ratios = np.exp(2.0 * time * np.real(zeros))
    scale_ratio_error = np.linalg.norm(
        evolved_norms / initial_norms - expected_ratios
    )

    print("model-kernel Hermitian error:", f"{hermitian_error:.3e}")
    print("model-kernel minimum eigenvalue:", f"{minimum_eigenvalue:.6e}")
    print("divisor annihilation error:", f"{divisor_error:.3e}")
    print("evaluation scale-ratio error:", f"{scale_ratio_error:.3e}")


if __name__ == "__main__":
    main()
