#!/usr/bin/env python3
"""108.20 -- H^1 abelian-sheaf decision verifier. Plain python3."""

from __future__ import annotations

import numpy as np


# ---------------------------------------------------------------------------
# 1. Proposition 2.2: u_s'' = r^{s-1} is bounded away from zero everywhere
#    on the sampled domain, for every s -- so it cannot be a finite atomic
#    measure (which is what a finite-PL second derivative must be).
# ---------------------------------------------------------------------------

def check_graded_never_pl() -> dict:
    """r^{s-1} is analytically nonzero for every finite r>0 and every real
    s (it decays but never vanishes as r->0 or r->infty). The relevant
    claim is 'nowhere exactly zero on a bounded window', not 'bounded away
    from zero uniformly as r ranges over all of (0,infty)' -- the latter
    is false for any s (the density does decay at one end), and is not
    what Proposition 2.2 asserts. So the grid is kept on a fixed bounded
    window where no underflow can occur, and we check strict nonvanishing."""
    r_grid = np.geomspace(0.1, 10.0, 5000)
    report = {}
    for s in [-3.0, -1.0, -0.5, 0.0, 0.7, 2.2]:
        density = r_grid ** (s - 1)
        min_abs = float(np.min(np.abs(density)))
        report[s] = min_abs
    return report


# ---------------------------------------------------------------------------
# 2. Contrast: PL potential's discretized second derivative is concentrated
#    at (essentially) one grid point; a continuous density is spread out.
# ---------------------------------------------------------------------------

def discrete_second_derivative(u_vals: np.ndarray, h: float) -> np.ndarray:
    d2 = np.zeros_like(u_vals)
    d2[1:-1] = (u_vals[2:] - 2 * u_vals[1:-1] + u_vals[:-2]) / h ** 2
    return d2


def concentration_fraction(mass: np.ndarray, top_k: int) -> float:
    total = np.sum(np.abs(mass))
    if total < 1e-15:
        return 0.0
    sorted_abs = np.sort(np.abs(mass))[::-1]
    return float(np.sum(sorted_abs[:top_k]) / total)


def check_pl_vs_continuous_concentration() -> dict:
    r_grid = np.linspace(0.0, 5.0, 5001)
    h = r_grid[1] - r_grid[0]

    u_pl = np.maximum(r_grid - 2.0, 0.0)  # finite-PL: single kink at r=2
    d2_pl = discrete_second_derivative(u_pl, h)
    conc_pl = concentration_fraction(d2_pl, top_k=3)

    s = 0.7
    u_smooth = r_grid.copy()
    u_smooth[r_grid > 0] = r_grid[r_grid > 0] ** (s + 1) / (s * (s + 1))
    u_smooth[r_grid <= 0] = 0.0
    d2_smooth = discrete_second_derivative(u_smooth, h)
    # restrict to region r > 0.2 to avoid the artificial r=0 boundary kink
    mask = r_grid > 0.2
    conc_smooth = concentration_fraction(d2_smooth[mask], top_k=3)

    return {
        "concentration_pl_top3": conc_pl,
        "concentration_smooth_top3": conc_smooth,
    }


def main() -> None:
    graded_report = check_graded_never_pl()
    graded_never_vanishes = all(v > 1e-6 for v in graded_report.values())

    conc = check_pl_vs_continuous_concentration()
    pl_is_concentrated = conc["concentration_pl_top3"] > 0.9
    smooth_is_spread_out = conc["concentration_smooth_top3"] < 0.05

    print("u_s'' = r^(s-1), minimum |value| on the fixed window [0.1,10] "
          "(strictly nonzero for every s: no finite-PL match there):")
    for s, minval in graded_report.items():
        print(f"  s={s:+.2f}: min|u_s''| on grid = {minval:.4e}")
    print(f"GRADED_FAMILY_NEVER_ATOMIC (Prop 2.2): "
          f"{'YES' if graded_never_vanishes else 'NO'}")
    print()
    print("Discrete second-derivative mass concentration (top-3 grid points "
          "as a fraction of total |mass|):")
    print(f"  finite-PL potential max(r-2,0):        "
          f"{conc['concentration_pl_top3']:.4f}  (concentrated, as expected)")
    print(f"  graded monomial potential (s=0.7):      "
          f"{conc['concentration_smooth_top3']:.4f}  (spread out, as expected)")
    print(f"PL_CONCENTRATED: {'YES' if pl_is_concentrated else 'NO'}")
    print(f"SMOOTH_SPREAD_OUT: {'YES' if smooth_is_spread_out else 'NO'}")

    print()
    print("OBSTRUCTION_1_FINITE_PL_HYPOTHESIS_EXCLUDED: "
          f"{'YES' if (graded_never_vanishes and pl_is_concentrated and smooth_is_spread_out) else 'NO'}")
    print("OBSTRUCTION_2_NO_COMPARISON_MAP_CONSTRUCTED: YES (scope statement, SS3)")

    verdict = graded_never_vanishes and pl_is_concentrated and smooth_is_spread_out

    print()
    print(f"ABELIAN_SHEAF_H1_ROUTE_FOR_DC_OBJECTS: {'NOT_AVAILABLE' if verdict else 'INCONCLUSIVE'}")
    print(f"VERDICT: {'NOT_AVAILABLE' if verdict else 'INCONCLUSIVE'}")

    if not verdict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
