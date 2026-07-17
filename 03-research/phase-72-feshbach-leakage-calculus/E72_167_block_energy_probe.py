#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_166_residual_sign_gram_probe import row  # noqa: E402


def run():
    print("E72.167 block sign-energy probe")
    print("cut=0.60, a=0.70, b=0.60")
    print(" lam    L     E0      E1    E0+E1   dist^2  crossE")
    worst_after_12 = (0.0, None)
    for lam, n_modes in [
        (6, 18),
        (8, 24),
        (10, 28),
        (12, 32),
        (14, 36),
        (16, 40),
        (18, 44),
        (20, 48),
        (22, 52),
        (24, 56),
    ]:
        s = row(lam, n_modes)
        e0 = s["r0p"] ** 2 + s["n0"] ** 2
        e1 = s["r1p"] ** 2 + s["n1"] ** 2
        total = e0 + e1
        if lam >= 12 and total > worst_after_12[0]:
            worst_after_12 = (total, lam)
        print(
            f"{lam:4.0f} {s['L']:5.2f} "
            f"{e0:7.3f} {e1:7.3f} {total:8.3f} "
            f"{s['dist'] ** 2:8.3f} {s['cross']:7.3f}"
        )
        sys.stdout.flush()
    print(f"worst_E0plusE1_after_lambda12={worst_after_12[0]:.3f} at lambda={worst_after_12[1]:.0f}")


if __name__ == "__main__":
    run()
