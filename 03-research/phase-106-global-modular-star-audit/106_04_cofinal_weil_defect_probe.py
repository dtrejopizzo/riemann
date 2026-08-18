#!/usr/bin/env python3
"""Numerical gate for the canonical cofinal shifted-Weil connection.

This is a diagnostic, not a certificate.  It implements E101.093 (2.6)--(3.10)
and Phase 106.03 (33)--(44) using NumPy only.  A single largest Weil matrix is
built and every lower level is obtained by principal compression.  Therefore

    W_N = I_N^* W_{N+1} I_N

holds to machine precision without comparing independently quadrature-built
matrices.

At consecutive levels it computes

    Delta_N = epsilon_N - epsilon_{N+1},
    j_N     = C_N (S_N + Delta_N I)^(-1/2) S_N^(1/2),
    R_N     = D_{N+1} j_N - j_N D_N,

as well as the two exact pieces

    R_N = (D_{N+1} C_N - C_N D_N) B_N
          + C_N (D_N B_N - B_N D_N).

All reported operator/Schatten norms use the positive quotient metrics, after
unitary transport to Euclidean coordinates.  The last columns test the exact
first-resolvent and second-resolvent shell identities.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import math

import numpy as np


EULER_GAMMA = 0.577215664901532860606512090082402431


def von_mangoldt(limit: int) -> np.ndarray:
    """Return Lambda(k), 0 <= k <= limit, by a prime-power sieve."""
    values = np.zeros(limit + 1, dtype=float)
    prime = np.ones(limit + 1, dtype=bool)
    if limit >= 0:
        prime[0] = False
    if limit >= 1:
        prime[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            prime[p * p :: p] = False
    for p in np.flatnonzero(prime):
        pk = int(p)
        lp = math.log(pk)
        while pk <= limit:
            values[pk] = lp
            if pk > limit // int(p):
                break
            pk *= int(p)
    return values


def omega_matrix(x: float, indices: np.ndarray, length: float) -> np.ndarray:
    """The matrix omega_nm(x)=q(U_n,U_m)(x) from E101.093 (2.4)."""
    n = indices[:, None]
    m = indices[None, :]
    diff = n - m
    phase_n = 2.0 * np.pi * n * x / length
    phase_m = 2.0 * np.pi * m * x / length
    out = np.empty(diff.shape, dtype=float)
    diagonal = diff == 0
    np.fill_diagonal(
        out,
        2.0 * (1.0 - x / length)
        * np.cos(2.0 * np.pi * indices * x / length),
    )
    # [sin(2 pi m x/L)-sin(2 pi n x/L)]/[pi(n-m)].
    out[~diagonal] = (
        (np.sin(phase_m) - np.sin(phase_n))[~diagonal]
        / (np.pi * diff[~diagonal])
    )
    return out


def build_weil_matrix(lam: float, max_n: int, quadrature_order: int) -> tuple[np.ndarray, float]:
    """Build W_(lambda,max_n) from E101.093 (2.6)--(2.9)."""
    if lam <= 1.0:
        raise ValueError("lambda must exceed 1")
    if max_n < 1:
        raise ValueError("max_n must be positive")
    length = 2.0 * math.log(lam)
    indices = np.arange(-max_n, max_n + 1, dtype=float)
    n = indices[:, None]
    m = indices[None, :]

    # Polar block, E101.093 (2.7).
    numerator = (
        32.0
        * length
        * math.sinh(length / 4.0) ** 2
        * (length**2 - 16.0 * np.pi**2 * m * n)
    )
    denominator = (
        (length**2 + 16.0 * np.pi**2 * m**2)
        * (length**2 + 16.0 * np.pi**2 * n**2)
    )
    polar = numerator / denominator

    # Archimedean block, E101.093 (2.8).  Gauss nodes avoid x=0, while
    # expm1 stabilizes 2*sinh(x)=exp(x)-exp(-x) near the origin.
    nodes, weights = np.polynomial.legendre.leggauss(quadrature_order)
    xs = 0.5 * length * (nodes + 1.0)
    ws = 0.5 * length * weights
    omega_zero = omega_matrix(0.0, indices, length)
    arch_integral = np.zeros_like(polar)
    for x, weight in zip(xs, ws):
        omega = omega_matrix(float(x), indices, length)
        denominator_x = math.exp(float(x)) - math.exp(-float(x))
        arch_integral += weight * (
            math.exp(float(x) / 2.0) * omega - omega_zero
        ) / denominator_x
    arch_constant = 0.5 * omega_zero * (
        EULER_GAMMA
        + math.log(4.0 * np.pi * (math.exp(length) - 1.0) / (math.exp(length) + 1.0))
    )
    archimedean = arch_constant + arch_integral

    # Complete Euler block through exp(L)=lambda^2, E101.093 (2.9).
    arithmetic = np.zeros_like(polar)
    cutoff = int(math.floor(math.exp(length) + 1.0e-12))
    mangoldt = von_mangoldt(cutoff)
    for k in np.flatnonzero(mangoldt):
        if k <= 1:
            continue
        arithmetic += (
            mangoldt[k]
            / math.sqrt(int(k))
            * omega_matrix(math.log(int(k)), indices, length)
        )

    matrix = polar - archimedean - arithmetic
    matrix = 0.5 * (matrix + matrix.T)
    return matrix, length


@dataclass
class QuotientLevel:
    n: int
    epsilon: float
    gap: float
    parity_error: float
    source_overlap: float
    xi: np.ndarray
    xi_eta: np.ndarray
    d_zero: np.ndarray
    d_prime: np.ndarray
    basis: np.ndarray
    s: np.ndarray
    d: np.ndarray
    d_euclidean: np.ndarray
    metric_symmetry_error: float


def positive_sqrt_diagonal(diagonal: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if np.min(diagonal) <= 0.0:
        raise ValueError("quotient metric is not numerically positive")
    root = np.diag(np.sqrt(diagonal))
    inverse = np.diag(1.0 / np.sqrt(diagonal))
    return root, inverse


def quotient_level(big_w: np.ndarray, max_n: int, n: int, length: float) -> QuotientLevel:
    """Construct the E101.093 positive quotient at Fourier cutoff n."""
    start = max_n - n
    stop = max_n + n + 1
    w = big_w[start:stop, start:stop]
    eigenvalues, eigenvectors = np.linalg.eigh(w)
    epsilon = float(eigenvalues[0])
    xi = eigenvectors[:, 0].copy()
    reversal = xi[::-1]
    parity_error = float(min(np.linalg.norm(xi - reversal), np.linalg.norm(xi + reversal)))
    eta = np.ones(2 * n + 1)
    overlap = float(eta @ xi)
    if overlap < 0.0:
        xi = -xi
        overlap = -overlap
    if overlap <= 1.0e-10:
        raise ValueError(
            f"level N={n}: ground state has negligible eta overlap ({overlap:.3e})"
        )

    # K_N=(ker T_N)^perp, in the standard source inner product.  Since the
    # columns are W-eigenvectors, S_N is diagonal in these coordinates.
    basis = eigenvectors[:, 1:]
    s = eigenvalues[1:] - epsilon
    gap = float(s[0])

    indices = np.arange(-n, n + 1, dtype=float)
    d_zero = np.diag(indices)
    xi_eta = xi / overlap
    scale = 2.0 * np.pi / length
    d_zero = scale * d_zero
    d_prime = d_zero - np.outer(d_zero @ xi_eta, eta)
    d = basis.T @ d_prime @ basis

    sqrt_s, inv_sqrt_s = positive_sqrt_diagonal(s)
    d_euclidean = sqrt_s @ d @ inv_sqrt_s
    d_euclidean = np.real_if_close(d_euclidean)
    metric_error = float(
        np.linalg.norm(np.diag(s) @ d - d.T @ np.diag(s), ord="fro")
        / max(1.0, np.linalg.norm(np.diag(s) @ d, ord="fro"))
    )
    return QuotientLevel(
        n=n,
        epsilon=epsilon,
        gap=gap,
        parity_error=parity_error,
        source_overlap=overlap,
        xi=xi,
        xi_eta=xi_eta,
        d_zero=d_zero,
        d_prime=d_prime,
        basis=basis,
        s=s,
        d=d,
        d_euclidean=d_euclidean,
        metric_symmetry_error=metric_error,
    )


@dataclass
class DefectRow:
    n: int
    delta: float
    isometry_error: float
    r_operator: float
    r_hs: float
    edge_hs: float
    commutator_hs: float
    edge_rank2_error: float
    r_after_rank2_hs: float
    resolvent_s1: float
    shell_rank: float
    shell_resolvent_hs2: float
    first_resolvent_error: float
    second_resolvent_error: float
    trace_increment_abs: float


def schatten_one(matrix: np.ndarray) -> float:
    return float(np.sum(np.linalg.svd(matrix, compute_uv=False)))


def consecutive_defect(old: QuotientLevel, new: QuotientLevel, z: complex) -> DefectRow:
    if new.n != old.n + 1:
        raise ValueError("levels must be consecutive")
    delta = old.epsilon - new.epsilon
    if delta < -1.0e-9:
        raise ValueError(f"min-max monotonicity failed: Delta={delta}")
    delta = max(0.0, float(delta))

    # Standard Fourier inclusion: coefficients [-N,N] occupy the middle of
    # [-(N+1),N+1].
    inclusion = np.zeros((2 * new.n + 1, 2 * old.n + 1))
    inclusion[1:-1, :] = np.eye(2 * old.n + 1)
    c = new.basis.T @ inclusion @ old.basis
    b_diagonal = np.sqrt(old.s / (old.s + delta))
    b = np.diag(b_diagonal)
    j = c @ b

    sqrt_old, inv_sqrt_old = positive_sqrt_diagonal(old.s)
    sqrt_new, inv_sqrt_new = positive_sqrt_diagonal(new.s)
    j_euclidean = sqrt_new @ j @ inv_sqrt_old
    isometry_error = float(
        np.linalg.norm(j_euclidean.T @ j_euclidean - np.eye(j_euclidean.shape[1]), ord="fro")
    )

    r = new.d @ j - j @ old.d
    edge = (new.d @ c - c @ old.d) @ b
    commutator = c @ (old.d @ b - b @ old.d)
    decomposition_error = np.linalg.norm(r - edge - commutator, ord="fro")
    if decomposition_error > 2.0e-8 * max(1.0, np.linalg.norm(r, ord="fro")):
        raise RuntimeError(f"defect decomposition failed: {decomposition_error:.3e}")

    # Exact rank-two factorization of D_{N+1} C_N-C_N D_N.  In source
    # coordinates, with A_N=D'_N and P_+=P_{K_{N+1}}, it is
    #
    #   |P_+(I D0_N xi_eta,N-D0,+ xi_eta,+)><eta_N|
    #   + |P_+ I xi_N><(A_N)^* xi_N|,
    #
    # restricted to K_N.  Multiplication by B_N gives ``edge``.
    p_new = new.basis @ new.basis.T
    eta_old = np.ones(2 * old.n + 1)
    d0_old_xi = old.d_zero @ old.xi_eta
    d0_new_xi = new.d_zero @ new.xi_eta
    embedded_d0_old_xi = inclusion @ d0_old_xi
    u = p_new @ (embedded_d0_old_xi - d0_new_xi)
    v = p_new @ (inclusion @ old.xi)
    eta_on_k = eta_old @ old.basis
    astar_xi_on_k = (old.d_prime.T @ old.xi) @ old.basis
    edge_rank2_unscaled = (
        np.outer(new.basis.T @ u, eta_on_k)
        + np.outer(new.basis.T @ v, astar_xi_on_k)
    )
    edge_rank2 = edge_rank2_unscaled @ b
    edge_rank2_error = float(
        np.linalg.norm(edge - edge_rank2, ord="fro")
        / max(1.0, np.linalg.norm(edge, ord="fro"))
    )

    r_euclidean = sqrt_new @ r @ inv_sqrt_old
    edge_euclidean = sqrt_new @ edge @ inv_sqrt_old
    commutator_euclidean = sqrt_new @ commutator @ inv_sqrt_old
    r_singular = np.linalg.svd(r_euclidean, compute_uv=False)

    identity_old = np.eye(old.d_euclidean.shape[0])
    identity_new = np.eye(new.d_euclidean.shape[0])
    g_old = np.linalg.inv(old.d_euclidean - z * identity_old)
    g_new = np.linalg.inv(new.d_euclidean - z * identity_new)
    resolvent_defect = g_new @ r_euclidean @ g_old
    e = g_new @ j_euclidean - j_euclidean @ g_old
    first_error = float(
        np.linalg.norm(e + resolvent_defect, ord="fro")
        / max(1.0, np.linalg.norm(e, ord="fro"))
    )

    q = identity_new - j_euclidean @ j_euclidean.T
    shell_rank = float(np.trace(q).real)
    shell_hs2 = float(np.linalg.norm(g_new @ q, ord="fro") ** 2)

    trace_increment = np.trace(g_new @ g_new) - np.trace(g_old @ g_old)
    transported = np.trace(
        j_euclidean.T @ (g_new @ e + e @ g_old)
    )
    shell_trace = np.trace(q @ g_new @ g_new @ q)
    second_error = float(abs(trace_increment - transported - shell_trace))

    return DefectRow(
        n=old.n,
        delta=delta,
        isometry_error=isometry_error,
        r_operator=float(r_singular[0]),
        r_hs=float(np.linalg.norm(r_euclidean, ord="fro")),
        edge_hs=float(np.linalg.norm(edge_euclidean, ord="fro")),
        commutator_hs=float(np.linalg.norm(commutator_euclidean, ord="fro")),
        edge_rank2_error=edge_rank2_error,
        r_after_rank2_hs=float(np.linalg.norm(r_singular[2:])),
        resolvent_s1=schatten_one(resolvent_defect),
        shell_rank=shell_rank,
        shell_resolvent_hs2=shell_hs2,
        first_resolvent_error=first_error,
        second_resolvent_error=second_error,
        trace_increment_abs=float(abs(trace_increment)),
    )


def log_slope(rows: list[DefectRow], field: str) -> float:
    xs = np.array([row.n for row in rows], dtype=float)
    ys = np.array([getattr(row, field) for row in rows], dtype=float)
    mask = np.isfinite(ys) & (ys > 0.0)
    if np.sum(mask) < 3:
        return float("nan")
    return float(np.polyfit(np.log(xs[mask]), np.log(ys[mask]), 1)[0])


def internally_stable(level: QuotientLevel, row: DefectRow) -> bool:
    """Heuristic float64 guard; this is not an a posteriori error bound."""
    return (
        level.gap > 1.0e-11
        and level.parity_error < 1.0e-4
        and level.metric_symmetry_error < 1.0e-6
        and row.isometry_error < 1.0e-4
        and abs(row.shell_rank - 2.0) < 1.0e-3
        and row.second_resolvent_error < 1.0e-6
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lambda", dest="lam", type=float, default=2.2)
    parser.add_argument("--n-min", type=int, default=1)
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--quadrature", type=int, default=384)
    parser.add_argument(
        "--z-imag", type=float, default=1.0,
        help="use the nonreal resolvent point z=i*z_imag",
    )
    args = parser.parse_args()
    if args.n_min < 1 or args.n_max <= args.n_min:
        parser.error("require 1 <= n-min < n-max")
    if args.quadrature < 32:
        parser.error("quadrature order must be at least 32")
    if args.z_imag == 0.0:
        parser.error("z-imag must be nonzero")

    big_w, length = build_weil_matrix(args.lam, args.n_max, args.quadrature)
    compression_error = 0.0
    # This is structurally exact because levels are slices of big_w; retain an
    # executable check to catch an indexing regression.
    for n in range(args.n_min, args.n_max):
        old_slice = big_w[args.n_max - n : args.n_max + n + 1,
                          args.n_max - n : args.n_max + n + 1]
        new_slice = big_w[args.n_max - n - 1 : args.n_max + n + 2,
                          args.n_max - n - 1 : args.n_max + n + 2]
        compression_error = max(
            compression_error,
            float(np.max(np.abs(old_slice - new_slice[1:-1, 1:-1]))),
        )

    levels = {
        n: quotient_level(big_w, args.n_max, n, length)
        for n in range(args.n_min, args.n_max + 1)
    }
    z = 1j * args.z_imag
    rows = [
        consecutive_defect(levels[n], levels[n + 1], z)
        for n in range(args.n_min, args.n_max)
    ]

    print("Cofinal shifted-Weil defect diagnostic (float64; not certified)")
    print(
        f"lambda={args.lam:g}, L={length:.12g}, N={args.n_min}..{args.n_max}, "
        f"Gauss order={args.quadrature}, z={z}"
    )
    print(f"principal-compression error: {compression_error:.3e}")
    print(
        " q N   Delta_eps    gap_N     parity      metric      isometry   "
        "||R||op    ||R||HS    edgeHS    commHS   rank2err  Rtail>2"
    )
    for row in rows:
        level = levels[row.n]
        quality = "S" if internally_stable(level, row) else "U"
        print(
            f" {quality} {row.n:2d}  {row.delta:10.3e} {level.gap:9.2e} "
            f"{level.parity_error:9.1e} {level.metric_symmetry_error:9.1e} "
            f"{row.isometry_error:9.1e} {row.r_operator:9.2e} "
            f"{row.r_hs:9.2e} {row.edge_hs:9.2e} {row.commutator_hs:9.2e} "
            f"{row.edge_rank2_error:9.1e} {row.r_after_rank2_hs:9.2e}"
        )

    print()
    stable_ns = [
        row.n for row in rows if internally_stable(levels[row.n], row)
    ]
    stable_rows = [
        row for row in rows if internally_stable(levels[row.n], row)
    ]
    unstable_ns = [row.n for row in rows if row.n not in stable_ns]
    print(
        "float64 internal guard (S=stable, U=unstable; heuristic only): "
        f"stable N={stable_ns}, unstable N={unstable_ns}"
    )
    print()
    print(
        " N   ||G+ R G||_1  shell-rank  ||G+Q||HS^2  "
        "|Delta Tr G^2|  res-id err  shell-id err"
    )
    for row in rows:
        print(
            f"{row.n:2d}   {row.resolvent_s1:12.4e}  {row.shell_rank:10.6f} "
            f"{row.shell_resolvent_hs2:12.4e} {row.trace_increment_abs:13.4e} "
            f"{row.first_resolvent_error:10.1e} {row.second_resolvent_error:12.1e}"
        )

    print()
    for field in (
        "delta", "r_operator", "r_hs", "edge_hs", "commutator_hs",
        "resolvent_s1", "shell_resolvent_hs2", "trace_increment_abs",
    ):
        print(
            f"stable-row log-log slope {field:>22s}: "
            f"{log_slope(stable_rows, field):+.4f}"
        )
    print(
        "PASS: compression, quotient self-adjointness, canonical isometry, "
        "defect decomposition, and both resolvent identities were evaluated."
    )


if __name__ == "__main__":
    main()
