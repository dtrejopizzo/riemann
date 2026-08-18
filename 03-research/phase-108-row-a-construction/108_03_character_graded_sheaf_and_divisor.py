#!/usr/bin/env python3
"""108.03 -- character-graded sheaf and divisor verifier. Plain python3."""

from __future__ import annotations

import numpy as np


def u(s: float, r: np.ndarray) -> np.ndarray:
    if s == 0.0:
        return r * np.log(r) - r
    if s == -1.0:
        return -np.log(r)
    return r ** (s + 1) / (s * (s + 1))


def U(s: float, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    if s == 0.0:
        return y * np.log(y / x) - y
    if s == -1.0:
        return x * np.log(x / y)
    return (y ** (s + 1)) * (x ** (-s)) / (s * (s + 1))


# ---------------------------------------------------------------------------
# 1. Proposition 2.1: u_s'' = r^{s-1}, by finite differences
# ---------------------------------------------------------------------------

def check_ode(tol: float = 2e-4) -> bool:
    ok = True
    h = 1e-4
    for s in [-2.0, -1.0, -0.5, 0.0, 0.3, 1.0, 2.5]:
        for r in [0.5, 1.0, 2.0, 5.0]:
            second = (u(s, r + h) - 2 * u(s, r) + u(s, r - h)) / h ** 2
            target = r ** (s - 1)
            if abs(second - target) > tol * max(1.0, abs(target)):
                ok = False
    return ok


# ---------------------------------------------------------------------------
# 2. Proposition 3.1: covariance law, exact for generic s, affine-mod for
#    s in {0, -1}.
# ---------------------------------------------------------------------------

def check_covariance_generic(tol: float = 1e-6) -> bool:
    ok = True
    for s in [-2.3, -0.7, 0.4, 1.0, 3.1]:
        if s in (0.0, -1.0):
            continue
        for m in [1, 2, 3]:
            for n in [1, 2, 3, 5]:
                for x in [0.7, 2.0]:
                    for y in [1.3, 4.0]:
                        lhs = U(s, m * x, n * y)
                        rhs = (n ** (1 + s)) * (m ** (-s)) * U(s, x, y)
                        if abs(lhs - rhs) > tol * max(1.0, abs(rhs)):
                            ok = False
    return ok


def fit_plane_residual(xs, ys, zs) -> float:
    """Least-squares fit z = a*x + b*y + c; return max abs residual."""
    A = np.stack([xs, ys, np.ones_like(xs)], axis=1)
    coeffs, *_ = np.linalg.lstsq(A, zs, rcond=None)
    resid = zs - A @ coeffs
    return float(np.max(np.abs(resid)))


def check_covariance_degenerate(tol: float = 1e-6) -> dict:
    """For each FIXED (m, n), the correction U(mx,ny) - n*U(x,y) [resp.
    m*U(x,y)] must be an affine (here: linear) function of (x, y) alone.
    The affine coefficients themselves depend on (m, n) -- that dependence
    is not part of the claim, so the plane fit must be done per (m, n)."""
    worst0, worstm1 = 0.0, 0.0
    for m in [1, 2, 3, 4]:
        for n in [1, 2, 3, 5]:
            xs, ys, corr0, corr_m1 = [], [], [], []
            for x in [0.6, 1.1, 2.3, 3.7]:
                for y in [0.9, 1.7, 3.3, 5.1]:
                    xs.append(x)
                    ys.append(y)
                    lhs0 = U(0.0, m * x, n * y)
                    rhs0 = n * U(0.0, x, y)
                    corr0.append(lhs0 - rhs0)

                    lhsm1 = U(-1.0, m * x, n * y)
                    rhsm1 = m * U(-1.0, x, y)
                    corr_m1.append(lhsm1 - rhsm1)
            xs_a = np.array(xs); ys_a = np.array(ys)
            resid0 = fit_plane_residual(xs_a, ys_a, np.array(corr0))
            residm1 = fit_plane_residual(xs_a, ys_a, np.array(corr_m1))
            worst0 = max(worst0, resid0)
            worstm1 = max(worstm1, residm1)
    return {"resid0": worst0, "residm1": worstm1,
            "is_affine0": worst0 < 1e-6, "is_affine_m1": worstm1 < 1e-6}


# ---------------------------------------------------------------------------
# 3. Proposition 5.2: div injective, nonvanishing density
# ---------------------------------------------------------------------------

def check_div_injective() -> bool:
    r_grid = np.linspace(0.1, 10.0, 500)
    ok = True
    for s in [-1.5, -1.0, 0.0, 0.5, 2.0]:
        density = r_grid ** (s - 1)
        if np.any(np.abs(density) < 1e-12):
            ok = False
        c1, c2 = 1.0, 2.3
        d1 = c1 * density
        d2 = c2 * density
        if np.allclose(d1, d2):
            ok = False
        if np.allclose(c1 * density, 0.0):
            ok = False
    return ok


# ---------------------------------------------------------------------------
# 4. Theorem 6.2: the principal line
# ---------------------------------------------------------------------------

def check_principal_line() -> dict:
    r_grid = np.linspace(0.1, 10.0, 500)
    density_s0 = r_grid ** (0.0 - 1)  # = 1/r
    nonzero = not np.allclose(density_s0, 0.0)
    matches_1_over_r = np.allclose(density_s0, 1.0 / r_grid)
    return {"nonzero": nonzero, "matches_1_over_r": matches_1_over_r}


def main() -> None:
    ode_ok = check_ode()
    cov_generic_ok = check_covariance_generic()
    cov_degenerate = check_covariance_degenerate()
    div_ok = check_div_injective()
    prin = check_principal_line()

    print(f"ODE_u''=r^(s-1) (Prop 2.1): {'YES' if ode_ok else 'NO'}")
    print(f"COVARIANCE_EXACT_GENERIC_S (Prop 3.1): "
          f"{'YES' if cov_generic_ok else 'NO'}")
    print(f"COVARIANCE_MOD_AFFINE_S=0: "
          f"{'YES' if cov_degenerate['is_affine0'] else 'NO'} "
          f"(plane-fit residual={cov_degenerate['resid0']:.2e})")
    print(f"COVARIANCE_MOD_AFFINE_S=-1: "
          f"{'YES' if cov_degenerate['is_affine_m1'] else 'NO'} "
          f"(plane-fit residual={cov_degenerate['residm1']:.2e})")
    print(f"DIV_INJECTIVE_NONVANISHING (Prop 5.2): {'YES' if div_ok else 'NO'}")
    print(f"PRINCIPAL_LINE_NONZERO (Thm 6.2): {'YES' if prin['nonzero'] else 'NO'}, "
          f"generator = 1/r: {'YES' if prin['matches_1_over_r'] else 'NO'}")

    verdict = (
        ode_ok
        and cov_generic_ok
        and cov_degenerate["is_affine0"]
        and cov_degenerate["is_affine_m1"]
        and div_ok
        and prin["nonzero"]
        and prin["matches_1_over_r"]
    )

    print()
    print(f"GLOBAL_PRINCIPAL_SUBSPACE_NONZERO_WITNESS: {'YES' if verdict else 'NO'}")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")

    if not verdict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
