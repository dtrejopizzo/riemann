#!/usr/bin/env python3
import math

import numpy as np


def run():
    print("E73.229 sector constant probe")
    print("Computes S=max |z|/Re z for z=80+1/4-i omega/2 and C=S^(2K+1).")
    print(" lam     L    N  dim   S        C_K16       log10C")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L = 2.0 * math.log(lam)
        idx = np.arange(-n_modes, n_modes + 1)
        d = 2.0 * np.pi * idx / L
        S = 1.0
        for omega in d:
            z = 80.25 - 0.5j * omega
            S = max(S, abs(z) / z.real)
        C = S ** 33
        print(f"{lam:4d} {L:7.3f} {n_modes:4d} {len(idx):4d} {S:8.6f} {C:12.6f} {math.log10(C):10.6f}")


if __name__ == "__main__":
    run()
