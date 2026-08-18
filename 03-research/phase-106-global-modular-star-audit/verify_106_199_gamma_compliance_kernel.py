#!/usr/bin/env python3
"""Finite spectral audit for the Gamma-compliance kernel of 106.199."""

import numpy as np


def main() -> None:
    rng = np.random.default_rng(106199)

    frequencies = np.linspace(-7.0, 7.0, 401)
    dgamma = frequencies[1] - frequencies[0]
    cauchy = (1.0 / (2.0 * np.pi)) / (frequencies**2 + 0.25)

    gamma_times = np.array([0.09, 0.21, 0.52, 1.1, 2.4, 4.8])
    gamma_weights = np.exp(-gamma_times / 2.0) / (
        1.0 - np.exp(-2.0 * gamma_times)
    )
    multiplier = 1.7 + np.sum(
        4.0
        * gamma_weights[:, None]
        * (1.0 - np.cos(gamma_times[:, None] * frequencies[None, :])),
        axis=0,
    )
    spectral_weight = cauchy * dgamma / multiplier

    sample_times = np.array([-1.4, -0.8, -0.15, 0.3, 0.95, 1.7])
    phases = np.exp(1j * frequencies[:, None] * sample_times[None, :])
    gram = phases.conj().T @ (spectral_weight[:, None] * phases)
    hermitian_error = np.linalg.norm(gram - gram.conj().T)
    minimum_eigenvalue = np.min(np.linalg.eigvalsh(gram)).real

    coefficients = rng.normal(size=sample_times.size) + 1j * rng.normal(
        size=sample_times.size
    )
    feature = phases @ coefficients
    spectral_norm = np.sum(spectral_weight * np.abs(feature) ** 2)
    gram_norm = np.vdot(coefficients, gram @ coefficients).real
    norm_error = abs(spectral_norm - gram_norm)

    shift = 0.417
    shifted_phases = np.exp(
        1j * frequencies[:, None] * (sample_times[None, :] + shift)
    )
    shifted_feature = shifted_phases @ coefficients
    equivariance_error = np.linalg.norm(
        shifted_feature - np.exp(1j * shift * frequencies) * feature
    )
    shifted_norm = np.sum(spectral_weight * np.abs(shifted_feature) ** 2)
    invariance_error = abs(shifted_norm - spectral_norm)

    print("kernel Hermitian error:", f"{hermitian_error:.3e}")
    print("kernel minimum eigenvalue:", f"{minimum_eigenvalue:.6e}")
    print("Gram/spectral norm error:", f"{norm_error:.3e}")
    print("translation equivariance error:", f"{equivariance_error:.3e}")
    print("translation invariance error:", f"{invariance_error:.3e}")


if __name__ == "__main__":
    main()
