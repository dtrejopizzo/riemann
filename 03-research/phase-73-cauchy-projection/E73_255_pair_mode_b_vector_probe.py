#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import bexp, quotient_defects  # noqa: E402


def safe_bexp(z, L):
    return bexp(z, L)


def pair_modes(b):
    rt2 = math.sqrt(2.0)
    return (b[0] + b[1]) / rt2, (b[0] - b[1]) / rt2


def four_modes(b):
    # gamma-parity x Cauchy-row-parity coordinates.
    return {
        "ss": (b[0] + b[1] + b[2] + b[3]) / 2.0,
        "sa": (b[0] - b[1] + b[2] - b[3]) / 2.0,
        "as": (b[0] + b[1] - b[2] - b[3]) / 2.0,
        "aa": (b[0] - b[1] - b[2] + b[3]) / 2.0,
    }


def audit_case(lam, n_modes, rat_power):
    _H, _idx, _d, L, _mu, xi, D, labels, ranks = quotient_defects(
        lam, n_modes, rat_power
    )
    b = D @ xi
    out = {
        "lam": lam,
        "L": L,
        "pow": rat_power,
        "ranks": ranks,
        "b": b,
        "labels": labels,
        "four": four_modes(b),
    }
    pairs = []
    for g in range(2):
        block = b[2 * g : 2 * g + 2]
        sym, anti = pair_modes(block)
        row_max = np.max(np.abs(block))
        mode_max = max(abs(sym), abs(anti))
        mode_min = min(abs(sym), abs(anti))
        # Largest cancellation available in either parity channel.
        parity_cancel = row_max / max(mode_min, 1e-300)
        # Whether the full pair is small only after combining rows. If this is O(1),
        # then rowwise smallness is already the real mechanism.
        dominant_mode_loss = row_max / max(mode_max, 1e-300)
        pairs.append(
            {
                "gamma_id": g,
                "row0": block[0],
                "row1": block[1],
                "sym": sym,
                "anti": anti,
                "row_max": row_max,
                "pair_norm": norm(block),
                "parity_cancel": parity_cancel,
                "dominant_mode_loss": dominant_mode_loss,
                "dominant": "sym" if abs(sym) >= abs(anti) else "anti",
            }
        )
    out["pairs"] = pairs
    return out


def run():
    cases = [(8, 6), (10, 8), (12, 10), (16, 20)]
    powers = [0, 1, 2]
    print("E73.255 pair-mode audit for b=D_Q xi_L")
    print(
        "Question: is bordered-vector smallness caused by Cauchy-row parity "
        "inside each gamma pair, or are the rows already small separately?"
    )
    print()
    print("Pair modes")
    print(
        " lam      L pow  g dom  row0B  row1B   symB  antiB pairNormB "
        "cancelB domLossB"
    )
    for lam, n_modes in cases:
        for rat_power in powers:
            out = audit_case(lam, n_modes, rat_power)
            L = out["L"]
            for p in out["pairs"]:
                print(
                    f"{lam:4d} {L:8.3f} {rat_power:3d}"
                    f" {p['gamma_id']:2d} {p['dominant']:>4s}"
                    f" {safe_bexp(p['row0'], L):6.2f}"
                    f" {safe_bexp(p['row1'], L):7.2f}"
                    f" {safe_bexp(p['sym'], L):6.2f}"
                    f" {safe_bexp(p['anti'], L):6.2f}"
                    f" {safe_bexp(p['pair_norm'], L):9.2f}"
                    f" {safe_bexp(p['parity_cancel'], L):7.2f}"
                    f" {safe_bexp(p['dominant_mode_loss'], L):8.2f}"
                )
    print()
    print("Four parity modes: gamma-parity x Cauchy-row-parity")
    print(" lam      L pow   bMaxB  bNormB    ssB    saB    asB    aaB  maxMode")
    for lam, n_modes in cases:
        for rat_power in powers:
            out = audit_case(lam, n_modes, rat_power)
            L = out["L"]
            b = out["b"]
            modes = out["four"]
            max_name = max(modes, key=lambda k: abs(modes[k]))
            print(
                f"{lam:4d} {L:8.3f} {rat_power:3d}"
                f" {safe_bexp(np.max(np.abs(b)), L):7.2f}"
                f" {safe_bexp(norm(b), L):7.2f}"
                f" {safe_bexp(modes['ss'], L):6.2f}"
                f" {safe_bexp(modes['sa'], L):6.2f}"
                f" {safe_bexp(modes['as'], L):6.2f}"
                f" {safe_bexp(modes['aa'], L):6.2f}"
                f" {max_name:>8s}"
            )


if __name__ == "__main__":
    run()
