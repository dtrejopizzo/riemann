#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup, von_mangoldt_prime_powers  # noqa: E402


def weight_mass(L, T):
    delta = 1.0 / math.sqrt(T)
    rows = von_mangoldt_prime_powers(int(math.exp(L)))
    exact = 0.0
    s = 0.0
    for n, lamn, u in rows:
        width = max(0.0, min(L, u + delta) - max(0.0, u - delta))
        exact += lamn * n ** -0.5 * width
        s += lamn * n ** -0.5
    return delta, exact, s


def run():
    print("E72.382 local weight scale probe")
    print(" lam     L       Tmoderate  massMod  predMod   Texp       massExp  predExp")
    for lam, n_modes, tmod in [(6, 10, 50.0), (8, 12, 70.0), (10, 14, 90.0), (12, 16, 110.0)]:
        _, _, L, _ = setup(lam, n_modes)
        texp = math.exp(L)
        dmod, mass_mod, _ = weight_mass(L, tmod)
        dexp, mass_exp, _ = weight_mass(L, texp)
        pred_mod = 4 * dmod * math.exp(L / 2)
        pred_exp = 4 * dexp * math.exp(L / 2)
        print(
            f"{lam:4.0f} {L:7.3f} {tmod:10.1f} {mass_mod:8.3e} {pred_mod:8.3e} "
            f"{texp:10.1f} {mass_exp:8.3e} {pred_exp:8.3e}"
        )


if __name__ == "__main__":
    run()
