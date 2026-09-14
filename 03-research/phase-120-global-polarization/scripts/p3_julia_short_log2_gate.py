#!/usr/bin/env python3
"""Kill/promote gate for the Paley--Wiener Julia-short candidate.

Unlike W3's Douglas contraction, this constructs the specific candidate from
the complex positive-real impedances Z_X,Z_Y.  It tests the pre-landing form
of (17):

    D_Y h_Y = (D_(T_Y*) D_(T_X*) + T_Y T_X*) D_X h_X.

The calculation is a Fourier-box discretization of the continuous compressed
Schur multipliers at T=log(2).  Convergence is checked by changing dt and the
outer box.
"""

import numpy as np
from scipy.special import digamma
import importlib.util
from pathlib import Path


def psd_sqrt(matrix: np.ndarray) -> np.ndarray:
    matrix = 0.5 * (matrix + matrix.conj().T)
    values, vectors = np.linalg.eigh(matrix)
    scale = max(float(np.max(np.abs(values))), 1.0)
    if float(np.min(values)) < -2e-9 * scale:
        raise RuntimeError(f"non-PSD defect: min={np.min(values):.3e}")
    return (vectors * np.sqrt(np.clip(values, 0.0, None))) @ vectors.conj().T


def symbols(tau: np.ndarray) -> tuple[np.ndarray, ...]:
    primes = (2, 3)
    theta = np.log(6.0)
    psi0 = float(digamma(0.25))
    m0 = np.log(np.pi) - psi0

    # Boundary s=-i*tau in the right-half-plane convention of phase 120.
    h_gamma = digamma(0.25 - 0.5j * tau) - psi0
    h_s = np.zeros_like(tau, dtype=complex)
    for prime in primes:
        a = np.log(prime)
        c = prime ** -0.5 * np.exp(1j * a * tau)
        h_s += a * (1.0 + c) / (1.0 - c)
    h_s /= theta

    z_x = h_gamma + theta
    z_y = m0 + theta * h_s
    s_x = (z_x - 1.0) / (z_x + 1.0)
    s_y = (z_y - 1.0) / (z_y + 1.0)
    r_x = 0.5 * (z_x + 1.0)
    r_y = 0.5 * (z_y + 1.0)
    return s_x, s_y, r_x, r_y


def multiplier_matrix(symbol: np.ndarray, indices: np.ndarray, size: int) -> np.ndarray:
    """Compression P M_symbol P in the standard discrete L2 basis."""
    columns = np.zeros((size, len(indices)), dtype=complex)
    columns[indices, np.arange(len(indices))] = 1.0
    acted = np.fft.fft(symbol[:, None] * np.fft.ifft(columns, axis=0), axis=0)
    return acted[indices, :]


def apply_multiplier(symbol: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.fft.fft(symbol * np.fft.ifft(vector))


def load_w3_assembly():
    path = Path(__file__).resolve().parents[2] / "phase-118-the-exact-threshold-inequality" / "scripts" / "rowd_assembly.py"
    spec = importlib.util.spec_from_file_location("w3_rowd_assembly", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def compress_to_cells(symbol: np.ndarray, embedding: np.ndarray) -> np.ndarray:
    acted = np.fft.fft(symbol[:, None] * np.fft.ifft(embedding, axis=0), axis=0)
    return embedding.conj().T @ acted


def potential(t: np.ndarray, radius: float, shift: float) -> np.ndarray:
    x = (t - shift) / radius
    ans = np.zeros_like(t)
    inside = np.abs(x) < 1.0
    ans[inside] = (1.0 - x[inside] ** 2) ** 6
    return ans


def l0_discrete(g: np.ndarray, dt: float) -> np.ndarray:
    tau = 2.0 * np.pi * np.fft.fftfreq(len(g), d=dt)
    # Positive Fourier convention has the same -d^2 multiplier tau^2.
    return np.fft.fft((tau * tau + 0.25) * np.fft.ifft(g))


def run(dt: float, half_box: float) -> None:
    size = int(round(2.0 * half_box / dt))
    size = 1 << (size - 1).bit_length()
    dt = 2.0 * half_box / size
    t = -half_box + dt * np.arange(size)
    tau = 2.0 * np.pi * np.fft.fftfreq(size, d=dt)
    window = np.log(2.0)
    indices = np.flatnonzero(np.abs(t) < window)
    s_x, s_y, r_x, r_y = symbols(tau)

    tx = multiplier_matrix(s_x, indices, size)
    ty = multiplier_matrix(s_y, indices, size)
    eye = np.eye(len(indices))
    dx = psd_sqrt(eye - tx.conj().T @ tx)
    dy = psd_sqrt(eye - ty.conj().T @ ty)
    dx_star = psd_sqrt(eye - tx @ tx.conj().T)
    dy_star = psd_sqrt(eye - ty @ ty.conj().T)
    block = dy_star @ dx_star + ty @ tx.conj().T

    residuals = []
    for shift in (-0.18, 0.0, 0.21):
        g = potential(t, 0.42, shift)
        f = l0_discrete(g, dt)
        hx = apply_multiplier(r_x, f)[indices]
        hy = apply_multiplier(r_y, f)[indices]
        lhs = dy @ hy
        rhs = block @ (dx @ hx)
        residuals.append(np.linalg.norm(lhs - rhs) / max(np.linalg.norm(lhs), 1e-300))

    unitary_block_bound = np.linalg.svd(block, compute_uv=False)[0]
    print(
        f"dt={dt:.8f} half_box={half_box:g} dim={len(indices)} "
        f"||block||={unitary_block_bound:.12f} "
        f"relative_residuals=" + ",".join(f"{x:.9e}" for x in residuals)
    )


def run_w3_basis(refine: int, size: int = 2**15, half_box: float = 40.0) -> None:
    """Operator residual on W3's full primitive piecewise-constant space."""
    ra = load_w3_assembly()
    window = np.log(2.0)
    assembled = ra.assemble(window, refine=refine)
    c, d = assembled["c"], assembled["d"]
    lengths = d - c

    dt = 2.0 * half_box / size
    t = -half_box + dt * np.arange(size)
    tau = 2.0 * np.pi * np.fft.fftfreq(size, d=dt)
    s_x, s_y, r_x, r_y = symbols(tau)

    embedding = np.zeros((size, len(c)), dtype=complex)
    for column, (left, right) in enumerate(zip(c, d)):
        mask = (t >= left) & (t < right)
        embedding[mask, column] = 1.0
    # Standard l2 coordinates representing normalized cell indicators.
    norms = np.sqrt(np.sum(np.abs(embedding) ** 2, axis=0))
    embedding /= norms[None, :]

    tx = compress_to_cells(s_x, embedding)
    ty = compress_to_cells(s_y, embedding)
    rx = compress_to_cells(r_x, embedding)
    ry = compress_to_cells(r_y, embedding)
    eye = np.eye(len(c))
    dx = psd_sqrt(eye - tx.conj().T @ tx)
    dy = psd_sqrt(eye - ty.conj().T @ ty)
    dx_star = psd_sqrt(eye - tx @ tx.conj().T)
    dy_star = psd_sqrt(eye - ty @ ty.conj().T)
    block = dy_star @ dx_star + ty @ tx.conj().T

    tate_normalized = assembled["Tate"] / np.sqrt(lengths)[None, :]
    _, _, vh = np.linalg.svd(tate_normalized)
    primitive = vh[2:].conj().T
    lhs = dy @ ry @ primitive
    rhs = block @ dx @ rx @ primitive
    residual = lhs - rhs
    rel_op = np.linalg.svd(residual, compute_uv=False)[0] / np.linalg.svd(lhs, compute_uv=False)[0]
    rel_fro = np.linalg.norm(residual) / np.linalg.norm(lhs)
    print(
        f"W3 refine={refine} dimP={primitive.shape[1]} dt={dt:.8f} "
        f"||block||={np.linalg.svd(block,compute_uv=False)[0]:.12f} "
        f"relative_operator_residual={rel_op:.9e} relative_frobenius_residual={rel_fro:.9e}"
    )


if __name__ == "__main__":
    for requested_dt, box in ((0.02, 24.0), (0.01, 32.0), (0.005, 40.0)):
        run(requested_dt, box)
    for refinement in (8, 16, 32):
        run_w3_basis(refinement)
