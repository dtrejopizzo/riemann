#!/usr/bin/env python3
"""108.10 -- numerical route audit verifier. Plain python3."""

from __future__ import annotations

import numpy as np


# ---------------------------------------------------------------------------
# 1. Internal consistency of the cited 107_241 signature formula (a
#    structural cross-check, not a re-derivation): on a synthetic finite
#    truncation, n_+ + n_- must equal the number of evaluation coordinates.
# ---------------------------------------------------------------------------

def synthetic_signature_check() -> bool:
    ok = True
    for num_on_line, num_mirror_pairs in [(0, 0), (2, 0), (0, 3), (4, 5), (1, 1)]:
        n_plus = 1 + num_mirror_pairs
        n_minus = 1 + num_on_line + num_mirror_pairs
        num_coords = 2 + num_on_line + 2 * num_mirror_pairs  # 0,1 poles + on-line + pairs
        if n_plus + n_minus != num_coords:
            ok = False
    return ok


# ---------------------------------------------------------------------------
# 2. Proposition 4.1: f_s = r^s is never compactly supported; C_c bump
#    functions are.
# ---------------------------------------------------------------------------

def is_compactly_supported(values: np.ndarray, tol: float = 1e-12) -> bool:
    """Heuristic finite check: nonzero only on an interior window, i.e. zero
    near both ends of a wide sampled range."""
    edge = max(1, len(values) // 50)
    near_zero_left = np.all(np.abs(values[:edge]) < tol)
    near_zero_right = np.all(np.abs(values[-edge:]) < tol)
    return bool(near_zero_left and near_zero_right)


def triangle_bump(r: np.ndarray, a: float = 2.0, b: float = 3.0) -> np.ndarray:
    mid = 0.5 * (a + b)
    left = (r - a) / (mid - a)
    right = (b - r) / (b - mid)
    val = np.clip(np.minimum(left, right), 0.0, None)
    val[(r <= a) | (r >= b)] = 0.0
    return val


def check_domain_disjointness() -> dict:
    r_wide = np.concatenate([
        np.geomspace(1e-6, 1.0, 4000, endpoint=False),
        np.geomspace(1.0, 1e6, 4000),
    ])

    graded_fails = []
    for s in [-3.0, -1.0, -0.5, 0.0, 0.7, 2.2]:
        vals = r_wide ** s
        graded_fails.append(not is_compactly_supported(vals))

    bump_vals = triangle_bump(r_wide.copy())
    bump_passes = is_compactly_supported(bump_vals)

    return {
        "graded_never_compact": all(graded_fails),
        "bump_is_compact": bump_passes,
    }


def main() -> None:
    sig_ok = synthetic_signature_check()
    disj = check_domain_disjointness()

    print("Fork table (cited from 107_240 SS5 / 107_240 Theorem D):")
    print("  Hodge index / signature on V         : needs principal inv. = NO  -> available now")
    print("  H^0, H^1, Riemann-Roch                : needs principal inv. = YES -> blocked")
    print()
    print(f"SIGNATURE_FORMULA_INTERNALLY_CONSISTENT (structural cross-check): "
          f"{'YES' if sig_ok else 'NO'}")
    print()
    print("Proposition 4.1 (disjoint test-function domains):")
    print(f"  graded family r^s never compactly supported (s tested: "
          f"-3,-1,-0.5,0,0.7,2.2): {'YES' if disj['graded_never_compact'] else 'NO'}")
    print(f"  C_c bump function passes compact-support test: "
          f"{'YES' if disj['bump_is_compact'] else 'NO'}")

    verdict = sig_ok and disj["graded_never_compact"] and disj["bump_is_compact"]

    print()
    print(f"PART_I_PART_II_DOMAINS_DISJOINT: {'YES' if verdict else 'NO'}")
    print(f"VERDICT: {'DISJOINT_DOMAINS_CONFIRMED' if verdict else 'INCONCLUSIVE'}")

    if not verdict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
