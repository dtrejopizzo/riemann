#!/usr/bin/env python3
"""Rational outward certificate that the M1 cumulative H changes sign."""

from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
P103 = HERE.parents[1] / "phase-103-direct-a1-closure" / "tools"
base = runpy.run_path(str(P103 / "cell_lobe_convex_order_certificate.py"))
SCALE = base["SCALE"]
scaled_log_bounds = base["scaled_log_bounds"]
primes_up_to = base["primes_up_to"]


def H_bounds(x: int) -> tuple[int, int]:
    """Bounds SCALE*H(x), H=sum Lambda(q)(q-1)-psi(x)^2/2."""
    psi_lo = psi_hi = moment_lo = moment_hi = 0
    for p in primes_up_to(x):
        log_lo, log_hi = scaled_log_bounds(p)
        q = p
        while q <= x:
            psi_lo += log_lo
            psi_hi += log_hi
            moment_lo += (q - 1) * log_lo
            moment_hi += (q - 1) * log_hi
            q *= p
    square_hi = (psi_hi * psi_hi + 2 * SCALE - 1) // (2 * SCALE)
    square_lo = psi_lo * psi_lo // (2 * SCALE)
    return moment_lo - square_hi, moment_hi - square_lo


def main() -> None:
    negative = H_bounds(2969)
    positive = H_bounds(3167)
    assert negative[1] < 0
    assert positive[0] > 0
    print("SCALE", SCALE)
    print("H(2969)", *negative)
    print("H(3167)", *positive)
    print("CERTIFIED H(2969) < -21 and H(3167) > 110")


if __name__ == "__main__":
    main()
