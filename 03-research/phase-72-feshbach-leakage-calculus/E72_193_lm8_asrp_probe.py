#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_192_low_moment_envelope_certificate import C0, C1  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]


def eval_env(vals, coeff, m_bound):
    u = vals / m_bound
    return (m_bound**2) * float(sum(c * np.sum(u**k) for k, c in enumerate(coeff)))


def split_energy(vals, a):
    return float(np.sum(np.where(vals >= 0.0, (1.0 - a) ** 2 * vals * vals, vals * vals)))


def run():
    print("E72.193 LM8-ASRP probe")
    print("certified degree-8 low-moment envelopes; target 0.9409")
    print(" lam    L dim exactBSE  LM8env  slack  pass")
    worst = (0.0, None)
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
        env = eval_env(v0, C0, 0.90) + eval_env(v1, C1, 0.60)
        if env > worst[0]:
            worst = (env, lam)
        print(
            f"{lam:4.0f} {L:5.2f} {len(v0):3d} "
            f"{exact:8.3f} {env:7.3f} {env-exact:6.3f} "
            f"{'YES' if env < 0.9409 else 'NO'}",
            flush=True,
        )
    print(f"worst_LM8={worst[0]:.3f} at lambda={worst[1]:.0f}")


if __name__ == "__main__":
    run()
