#!/usr/bin/env python3
import math

from E73_055_far3_nodewise_verifier import GAMMAS, certificate_rows


def effective_exponent(value, L):
    if value <= 0 or L <= 1:
        return float("-inf")
    return math.log(value) / math.log(L)


def run():
    print("E73.057 FAR3 budget exponent probe")
    print("Computes effective B with value=L^B for main/tail/total.")
    print(" lam     L sigma     tau    mainB    tailB   totalB      main      tail     total")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = certificate_rows(lam, n_modes, sigma, tau, m, 12)
            main = sum(row["term"] for row in rows if row["part"] == "main")
            tail = sum(row["term"] for row in rows if row["part"] == "tail")
            total = main + tail
            print(
                f"{lam:4d} {L:7.3f} {sigma:5.2f} {tau:7.2f}"
                f" {effective_exponent(main, L):8.3f} {effective_exponent(tail, L):8.3f}"
                f" {effective_exponent(total, L):8.3f} {main:9.3e} {tail:9.3e} {total:9.3e}"
            )


if __name__ == "__main__":
    run()
