#!/usr/bin/env python3
import cmath
import numpy as np

from E73_003_critical_source_probe import dd_kernel
from E72_396_cauchy_projection_probe import GAMMAS


def run():
    print("E73.018 mesh rational collapse probe")
    print("   L      gamma      maxAbsErr")
    for L in [4.159, 4.605, 4.970, 5.278, 5.545]:
        idx = np.arange(-25, 26)
        d = 2.0 * np.pi * idx / L
        for gamma in GAMMAS[:3]:
            c = cmath.exp(1j * gamma * L) - 1.0
            err = 0.0
            for dm in d:
                lhs = dd_kernel(-gamma, dm, L)
                rhs = c / (gamma + dm)
                err = max(err, abs(lhs - rhs))
            print(f"{L:6.3f} {gamma:10.6f} {err:14.3e}")


if __name__ == "__main__":
    run()
