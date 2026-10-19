#!/usr/bin/env python3
"""Diagnostic for the raw and polar-renormalized finite Poisson defects.

The mathematical statements are proved in R161_003.  This script only makes
the oscillation and the effect of the polar subtraction visible.
"""

import mpmath as mp


mp.mp.dps = 40


def u_infty(tau: mp.mpf) -> mp.mpc:
    return (
        mp.pi ** (-1j * tau)
        * mp.gamma(mp.mpf("0.25") + 0.5j * tau)
        / mp.gamma(mp.mpf("0.25") - 0.5j * tau)
    )


def partial_zeta(n_max: int, s: mp.mpc) -> mp.mpc:
    return mp.fsum(mp.power(n, -s) for n in range(1, n_max + 1))


def polar(n_max: int, s: mp.mpc) -> mp.mpc:
    return mp.power(n_max, 1 - s) / (1 - s)


def defects(n_max: int, tau: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    s = mp.mpf("0.5") + 1j * tau
    reflected = 1 - s
    phase = u_infty(tau)
    d_s = partial_zeta(n_max, s)
    d_r = partial_zeta(n_max, reflected)
    raw = abs(d_s * phase - d_r) ** 2
    z_s = d_s - polar(n_max, s)
    z_r = d_r - polar(n_max, reflected)
    renormalized = abs(z_s * phase - z_r) ** 2
    return raw, renormalized


def main() -> None:
    sample_sizes = [4, 8, 16, 32, 64, 128, 256]
    for tau in [mp.mpf("1"), mp.mpf("3"), mp.mpf("7")]:
        print(f"tau={tau}")
        previous_raw = None
        changes = []
        for n_max in sample_sizes:
            raw, renormalized = defects(n_max, tau)
            if previous_raw is not None:
                changes.append("+" if raw > previous_raw else "-")
            previous_raw = raw
            print(
                f"  N={n_max:3d} raw={float(raw):.8e} "
                f"ren={float(renormalized):.8e}"
            )
        print("  raw changes:", "".join(changes))


if __name__ == "__main__":
    main()
