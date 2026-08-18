#!/usr/bin/env python3
"""E78.147 - INCREMENTAL-TRANSFER-FLATTENING probe.

New object (candidate new mathematics for SAFE-GAMMA-IDENT / point 6):

  The 2-mode incremental transfer factor
      tau_N(z) = T_{L,N+2}(z) / T_{L,N}(z)
  has, on the safe axis z = i*sigma, the exact log-derivative

      (log tau_N)'(z) = (log T_{N+2})' - (log T_N)'
                      = q_M - q_N = -Delta_N[W'/(1+W)]         (= -q_delta),

  where q_N = W'_{L,N}/(1+W_{L,N}).  So the cofinal sequence of q_delta values
  IS the sequence (log tau_N)'(i*sigma).

  CLAIM (INCREMENTAL-TRANSFER-FLATTENING):
    for the zeta build, |(log tau_N)'(i*sigma)| -> 0 as N -> infinity with a
    summable (geometric) cofinal envelope, uniformly on safe compacta, EVEN
    THOUGH the modulus |tau_N| does not decay (transfer amplification persists).
    I.e. the incremental transfer factor becomes FLAT in z (a pure N-scale).
    For the planted (off-line-zero) build, (log tau_N)' does NOT flatten:
    it stays bounded away from 0 (the off-line pole keeps a moving phase).

  This probe measures, for each consecutive step N -> N+2 and each safe sigma:
    - qd = |(log tau_N)'| = |q_delta|            (the flattening quantity)
    - |tau_N| = |T_{N+2}/T_N| = |1+W_M|/|1+W_N| * |z-d_b|/|z-d_b|
              = |1+W_M| / |1+W_N|                 (z-d_b cancels)   (modulus)
    - |T_N| = |1+W_N| / |z - d_b|                  (transfer scale)
  and reports, per build:
    - max over sigma of qd at each step (envelope)
    - the step-to-step ratio of that envelope (geometric decay rate for zeta,
      ~1 or growing for plant)
    - the modulus |tau_N| (should stay >~1 / not decay for zeta -> proves the
      flattening is NOT just tau_N -> 1).

Reuses the exact verified machinery of E78.9 (build_w_package).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data, serial, two_generator_data  # noqa: E402
from E78_9_w_quotient_delta_probe import build_w_package, section  # noqa: E402


def db_value(H, idx, L, lam, planted, sigma):
    """Return z - d_b for the boundary pole (from right_transfer_data)."""
    _mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
    d, u, v, db, aa, bb, ub, vb = two_generator_data(A, inner, db_idx, L, lam, planted)
    z = 1j * sigma
    return z - db


def run_case(label, planted, lam_int, max_modes, dps, sigmas):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    steps = []
    prev_env = None
    for n_modes in range(8, max_modes - 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_modes, n_modes)
        Hm, idxm = section(Hmax, idxmax, max_modes, n_modes + 2)
        rows = []
        for sigma in sigmas:
            old = build_w_package(Hn, idxn, L, lam, planted, sigma)
            new = build_w_package(Hm, idxm, L, lam, planted, sigma)
            q_old = old["Wp"] / (1 + old["W"])
            q_new = new["Wp"] / (1 + new["W"])
            log_tau_prime = q_new - q_old  # = (log T_{N+2})' - (log T_N)'
            zmdb = db_value(Hn, idxn, L, lam, planted, sigma)
            mod_tau = abs(1 + new["W"]) / abs(1 + old["W"])  # |T_{N+2}/T_N|
            mod_T_N = abs(1 + old["W"]) / abs(zmdb)
            rows.append({
                "sigma": serial(sigma),
                "log_tau_prime_abs": serial(abs(log_tau_prime)),
                "mod_tau": serial(mod_tau),
                "mod_T_N": serial(mod_T_N),
            })
        env = max(mp.mpf(r["log_tau_prime_abs"]) for r in rows)
        ratio = "" if prev_env is None else serial(env / prev_env, 6)
        prev_env = env
        min_mod_tau = min(mp.mpf(r["mod_tau"]) for r in rows)
        max_mod_T = max(mp.mpf(r["mod_T_N"]) for r in rows)
        steps.append({
            "from_N": n_modes, "to_N": n_modes + 2,
            "env_log_tau_prime": serial(env),
            "env_ratio_vs_prev": ratio,
            "min_mod_tau": serial(min_mod_tau),
            "max_mod_T_N": serial(max_mod_T),
            "rows": rows,
        })
        print(f"{label:6s} {n_modes:2d}->{n_modes+2:2d}  "
              f"env|(log tau)'|={serial(env,6)}  ratio={ratio:>12s}  "
              f"min|tau|={serial(min_mod_tau,5)}  max|T_N|={serial(max_mod_T,5)}",
              flush=True)
    return {"label": label,
            "planted": None if planted is None else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
            "steps": steps}


def main():
    dps = 60
    lam_int = 6
    max_modes = 20
    sigmas = [mp.mpf(x) for x in ["0.55", "0.6", "0.75", "1.0", "1.5", "2.0", "3.0"]]
    result = {
        "statement": "INCREMENTAL-TRANSFER-FLATTENING: (log tau_N)' -> 0 summably for zeta, not for plant",
        "parameters": {"lambda": lam_int, "max_modes": max_modes, "dps": dps,
                       "sigmas": [serial(s) for s in sigmas]},
        "cases": [],
    }
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        result["cases"].append(run_case(label, planted, lam_int, max_modes, dps, sigmas))
    out = HERE / "E78_147_incremental_transfer_flattening_results.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
