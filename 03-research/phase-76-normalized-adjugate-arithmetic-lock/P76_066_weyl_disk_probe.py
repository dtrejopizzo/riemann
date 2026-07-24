#!/usr/bin/env python3
"""Weyl-disk contraction probe for SAFE-LIMIT-POINT.

Diagnostic: in Weyl limit-point/limit-circle language, uniqueness of the
normalized l2 solution of the infinite bordered CCM system corresponds to
the limit-point case, whose finite-section signature is divergence of the
canonical-solution energy S_N = ||x_N||^2 (Weyl-disk radius ~ 1/S_N) and
escape of the residual mass to the Fourier shell.

This probe measures, on nested finite sections of one build:
  1. S_N and its growth ratio (limit-point: S_N -> infinity);
  2. the shell-mass fraction of x_N (escape-to-shell signature, cf. P76.062).

Both the zeta build and the planted off-line falsifier are run.  LP is an
arithmetic-free stability statement, so BOTH cases are expected to show the
limit-point signature; the arithmetic content lives in IDENT (P76.067), not
here.  A falsifier that failed LP would mean arithmetic is hiding inside the
stability layer and the split of P76.067 would be wrong.
"""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp


def canonical_solution(H):
    """Inner solution x of (A - mu I) x = b for the bordered last column."""
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return A ** -1 * b


def energy(x):
    return sum(abs(x[j]) ** 2 for j in range(x.rows))


def shell_mass(x, k=2):
    total = energy(x)
    idxs = list(range(k)) + list(range(x.rows - k, x.rows))
    shell = sum(abs(x[j]) ** 2 for j in idxs)
    return shell / total


def run():
    mp.mp.dps = 70
    max_modes = 12
    cases = (
        ("zeta", {}),
        ("planted", {"planted": ("14.134725141734693790", "0.30", "5.0")}),
    )
    print("P76.066 Weyl-disk contraction probe")
    print("limit-point signature: S_N grows without bound, radius 1/S_N -> 0")
    for label, kwargs in cases:
        Hmax, idxmax, L = build_mp(6, max_modes, 70, **kwargs)
        print(f"-- {label}")
        print(" N        S_N          radius~1/S_N   shellMass(k=2)   S_N/S_(N-1)")
        prev = None
        for n_modes in range(6, max_modes + 1):
            offset = max_modes - n_modes
            H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
            x = canonical_solution(H)
            s_val = energy(x)
            ratio = s_val / prev if prev is not None else mp.mpf(0)
            print(
                f"{n_modes:2d} {mp.nstr(s_val, 8):>14} {mp.nstr(1 / s_val, 8):>14}"
                f" {mp.nstr(shell_mass(x), 6):>12} {mp.nstr(ratio, 6):>12}"
            )
            prev = s_val


if __name__ == "__main__":
    run()
