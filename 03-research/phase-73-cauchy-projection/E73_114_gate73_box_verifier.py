#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_100_gate73_verifier import gate_values  # noqa: E402
from E73_113_possible_set_box_verifier import verify_box  # noqa: E402


def run():
    print("E73.114 GATE-73 box verifier")
    print("MAIN uses possible-set box certificate; LOCK/TAIL/OUT shown at box center.")
    print("Targets: center LOCK<=L^-5, TAIL<=L^-5, OUT<=L^-9; box MAIN<=1.")
    print(" lam     L box                         lockB  tailB    outB  mainBox status")
    boxes = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        boxes.append((0.15, 0.25, tau - 0.50, tau + 0.50))
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for alpha0, alpha1, tau0, tau1 in boxes:
            alpha_c = 0.5 * (alpha0 + alpha1)
            tau_c = 0.5 * (tau0 + tau1)
            vals = gate_values(lam, n_modes, alpha_c, tau_c, 3)
            L = vals["L"]
            _, _, _, main_box = verify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, 3)
            lock_b = bexp(vals["lock"], L)
            tail_b = bexp(vals["tail"], L)
            out_b = bexp(vals["out"], L)
            ok = lock_b <= -5.0 and tail_b <= -5.0 and out_b <= -9.0 and main_box <= 1.0
            print(
                f"{lam:4d} {L:7.3f} [{alpha0:.2f},{alpha1:.2f}]x[{tau0:5.2f},{tau1:5.2f}]"
                f" {lock_b:7.3f} {tail_b:7.3f} {out_b:7.3f} {main_box:8.3e}"
                f" {'PASS' if ok else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
