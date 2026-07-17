#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_117_exact_local_box_verifier import verify_box as verify_standard_box  # noqa: E402
from E73_119_low_lock_alpha_interval import verify_low_box as verify_base16_lock  # noqa: E402


def manifest():
    rows = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        rows.append(
            {
                "name": f"lambda16-base-{tau:.2f}",
                "kind": "base16_exact_lock",
                "lam": 16,
                "n_modes": 20,
                "alpha0": 0.15,
                "alpha1": 0.25,
                "tau0": tau - 0.50,
                "tau1": tau + 0.50,
            }
        )

    tau = GAMMAS[0]
    for a0, a1 in [(0.15, 0.20), (0.20, 0.25)]:
        for j in range(4):
            rows.append(
                {
                    "name": f"lambda20-cover-g1-a{a0:.2f}-{a1:.2f}-t{j}",
                    "kind": "standard_box",
                    "lam": 20,
                    "n_modes": 24,
                    "alpha0": a0,
                    "alpha1": a1,
                    "tau0": tau - 0.50 + 0.25 * j,
                    "tau1": tau - 0.50 + 0.25 * (j + 1),
                }
            )

    tau = GAMMAS[1]
    for j in range(4):
        rows.append(
            {
                "name": f"lambda20-cover-g2-t{j}",
                "kind": "standard_box",
                "lam": 20,
                "n_modes": 24,
                "alpha0": 0.15,
                "alpha1": 0.25,
                "tau0": tau - 0.50 + 0.25 * j,
                "tau1": tau - 0.50 + 0.25 * (j + 1),
            }
        )

    for tau in [GAMMAS[0], GAMMAS[1]]:
        for lam, n_modes in [(24, 28), (28, 32)]:
            rows.append(
                {
                    "name": f"lambda{lam}-wide-{tau:.2f}",
                    "kind": "standard_box",
                    "lam": lam,
                    "n_modes": n_modes,
                    "alpha0": 0.15,
                    "alpha1": 0.25,
                    "tau0": tau - 0.50,
                    "tau1": tau + 0.50,
                }
            )
    return rows


def verify_entry(entry):
    if entry["kind"] == "base16_exact_lock":
        L, main_box, ntri, lock = verify_base16_lock(
            entry["lam"],
            entry["n_modes"],
            entry["alpha0"],
            entry["alpha1"],
            entry["tau0"],
            entry["tau1"],
            3,
        )
        return {
            "L": L,
            "lock": lock,
            "tail": 0.0,
            "out": 0.0,
            "main": main_box,
            "ntriples": ntri,
            "ok": bexp(lock, L) <= -5.0 and main_box <= 1.0,
        }

    vals = verify_standard_box(
        entry["lam"],
        entry["n_modes"],
        entry["alpha0"],
        entry["alpha1"],
        entry["tau0"],
        entry["tau1"],
        3,
    )
    L = vals["L"]
    return {
        "L": L,
        "lock": vals["lock"],
        "tail": vals["tail"],
        "out": vals["out"],
        "main": vals["main"],
        "ntriples": vals["ntriples"],
        "ok": (
            bexp(vals["lock"], L) <= -5.0
            and bexp(vals["tail"], L) <= -5.0
            and bexp(vals["out"], L) <= -9.0
            and vals["main"] <= 1.0
        ),
    }


def run():
    print("E73.120 finite GATE-73 manifest verifier")
    print("Each row declares the certificate kind; thresholds are enforced by kind.")
    print(" name                                kind              L   lockB  tailB    outB mainBox nTri status")
    failures = 0
    for entry in manifest():
        vals = verify_entry(entry)
        L = vals["L"]
        lock_b = bexp(vals["lock"], L)
        tail_b = bexp(vals["tail"], L)
        out_b = bexp(vals["out"], L)
        ok = vals["ok"]
        failures += 0 if ok else 1
        print(
            f"{entry['name'][:35]:35s} {entry['kind'][:17]:17s}"
            f" {L:6.3f} {lock_b:7.3f} {tail_b:7.3f} {out_b:7.3f}"
            f" {vals['main']:7.3e} {vals['ntriples']:4d} {'PASS' if ok else 'FAIL'}"
        )
    print(f"manifest_status {'PASS' if failures == 0 else 'FAIL'} failures={failures}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()

