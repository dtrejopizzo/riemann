#!/usr/bin/env python3
"""Finite-dimensional audit of the intertwining identities in 106.173."""

from __future__ import annotations

import math

import numpy as np


def main() -> None:
    p = 17
    c = 2.0 * math.pi / math.log(p)

    # Coordinates are (ell(f), ell(Fg)).  Fourier swaps them with the
    # indicated sign; L rescales the second coordinate by c.
    j_source = np.array([[0.0, -1.0], [1.0, 0.0]])
    localization = np.diag([1.0, c])
    j_tate = np.array([[0.0, -1.0 / c], [c, 0.0]])
    section = np.diag([1.0, 1.0 / c])

    checks = {
        "J_source^2 + I": j_source @ j_source + np.eye(2),
        "J_Tate^2 + I": j_tate @ j_tate + np.eye(2),
        "L J_source - J_Tate L": (
            localization @ j_source - j_tate @ localization
        ),
        "L section - I": localization @ section - np.eye(2),
        "J_source section - section J_Tate": (
            j_source @ section - section @ j_tate
        ),
    }

    for label, value in checks.items():
        print(f"{label:42s} {np.linalg.norm(value):.3e}")


if __name__ == "__main__":
    main()
