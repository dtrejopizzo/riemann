#!/usr/bin/env python3
"""Test whether consecutive boundary core numerators form a Sturm chain."""

import numpy as np
import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_020_boundary_root_reality import numerator_roots


def real_roots(H, idx, L):
    roots = numerator_roots(H, idx, L, 1)
    if np.max(np.abs(roots.imag)) > 2e-6:
        raise RuntimeError("root solver did not resolve a real divisor")
    return np.sort(roots.real)


def two_step_violations(old, new, tol=2e-6):
    # Necessary order condition for a degree jump of two: the j-th old root
    # must lie between the j-th and (j+2)-th new roots.
    bad = []
    for j, value in enumerate(old):
        if not (new[j] - tol < value < new[j + 2] + tol):
            bad.append((j, value, new[j], new[j + 2]))
    return bad


def run_case(tag, planted):
    max_modes = 9
    Hmax, idxmax, L = build_mp(6, max_modes, 80, planted=planted)
    previous = None
    print(tag)
    print("N degree nonreal/twoStepViol maxOldToNew")
    for n_modes in (5, 6, 7, 8, 9):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        roots = real_roots(H, idx, L)
        if previous is None:
            print(f"{n_modes:2d} {len(roots):6d} {'-':>18} {'-':>13}")
        else:
            bad = two_step_violations(previous, roots)
            nearest = max(min(abs(value - r) for r in roots) for value in previous)
            print(f"{n_modes:2d} {len(roots):6d} {len(bad):18d} {nearest:13.5e}")
            if bad:
                j, value, lo, hi = bad[0]
                print(f"  first violation j={j}: new[{j}]={lo:.8g}, old={value:.8g}, new[{j+2}]={hi:.8g}")
        previous = roots


def run():
    mp.mp.dps = 80
    print("P76.044 consecutive core interlacing")
    run_case("zeta", None)
    run_case("planted", ("14.134725141734693790", "0.30", "5.0"))


if __name__ == "__main__":
    run()
