#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_219_scalar_transcell_budget import bexp, center_data, scalar_budget  # noqa: E402


def run():
    print("E73.261 reduced-adjugate ETA-ADJ budget")
    print("Normalized ETA-ADJ radius equals the certified scalar radius for rho xi=qHeta.")
    print(
        " lam     L    N  dim Csec gamma row etaAdjB radB certB "
        "ratio verdict"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        center = center_data(lam, n_modes)
        for csec_label in ["1", "1e6"]:
            L, dim, rows = scalar_budget(center, csec_label)
            for row in rows:
                val = abs(row["center"])
                rad = row["rad_total"]
                cert = val + rad
                verdict = "radius-small" if rad < val else "radius-dominates"
                print(
                    f"{lam:4d} {L:7.3f} {n_modes:4d} {dim:4d}"
                    f" {csec_label:>4s} {row['gamma']:7.2f} {row['row_id']:3d}"
                    f" {bexp(val, L):8.2f}"
                    f" {bexp(rad, L):6.2f}"
                    f" {bexp(cert, L):7.2f}"
                    f" {row['ratio']:8.1e}"
                    f" {verdict}"
                )


if __name__ == "__main__":
    run()
