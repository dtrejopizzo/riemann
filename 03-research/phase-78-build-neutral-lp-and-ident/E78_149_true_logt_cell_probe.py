#!/usr/bin/env python3
"""E78.149 - CORRECTED true LOGT-CELL = Delta[T'/T] with the MOVING boundary pole.

Bookkeeping correction (audit): the boundary index is idx[-1] = n_modes = N, so
d_{b,N} = 2 pi N / L DEPENDS ON N. Hence the boundary pole 1/(z-d_b) does NOT
cancel across sections. E78.7 (WL-7: LOGT-CELL = W-QUOTIENT-DELTA) is therefore
false as an exact identity, and E78.147's log_tau_prime (= Delta[F'/F], no
boundary) is NOT the true (log tau_N)' = Delta[T'/T].

Correct objects:
  T_{L,N}(z) = F_{L,N}(z)/(z - d_{b,N}),  d_{b,N} = 2 pi N / L.
  T'/T = F'/F - 1/(z - d_{b,N}).
  true (log tau_N)'(z) = (T'/T)_{N+2} - (T'/T)_N
                       = Delta[F'/F] - [1/(z-d_{b,N+2}) - 1/(z-d_{b,N})].
  |tau_N| = |F_{N+2}/F_N| * |z-d_{b,N}|/|z-d_{b,N+2}|.

This probe recomputes, per step and per safe sigma:
  A := |Delta[F'/F]|                (what E78.147 wrongly called |(log tau)'|)
  B := |boundary increment|         (the omitted O(1/N^2) term)
  C := |true (log tau_N)'| = |Delta[T'/T]|   (the object the WL-10 chain needs)
and reports the law N^2 * C to see whether the TRUE object is still summable and
what its constant is.
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
from E77_3c_two_generator_ident_probe import GAMMA, serial  # noqa: E402
from E78_9_w_quotient_delta_probe import build_w_package, section  # noqa: E402


def db_of_section(idx, L):
    return 2 * mp.pi * idx[-1] / L  # idx[-1] = n_modes = N


def run_case(label, planted, lam_int, max_modes, dps, sigmas):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    steps = []
    for n_modes in range(8, max_modes - 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_modes, n_modes)
        Hm, idxm = section(Hmax, idxmax, max_modes, n_modes + 2)
        db_n = db_of_section(idxn, L)
        db_m = db_of_section(idxm, L)
        rows = []
        for sigma in sigmas:
            z = 1j * sigma
            old = build_w_package(Hn, idxn, L, lam, planted, sigma)
            new = build_w_package(Hm, idxm, L, lam, planted, sigma)
            q_old_F = old["Wp"] / (1 + old["W"])            # (F'/F)_N
            q_new_F = new["Wp"] / (1 + new["W"])            # (F'/F)_{N+2}
            dFF = q_new_F - q_old_F                          # Delta[F'/F]
            binc = 1 / (z - db_m) - 1 / (z - db_n)          # boundary increment
            true_tau = dFF - binc                            # Delta[T'/T]
            rows.append({
                "sigma": serial(sigma),
                "A_dFF_abs": serial(abs(dFF)),
                "B_binc_abs": serial(abs(binc)),
                "C_true_abs": serial(abs(true_tau)),
                "N2C": serial(n_modes * n_modes * abs(true_tau), 6),
                "N2A": serial(n_modes * n_modes * abs(dFF), 6),
            })
        envC = max(mp.mpf(r["C_true_abs"]) for r in rows)
        steps.append({"from_N": n_modes, "to_N": n_modes + 2,
                      "env_true_abs": serial(envC), "rows": rows})
        # print N^2*C for two reference sigmas
        r1 = next(r for r in rows if r["sigma"].startswith("1.0"))
        r2 = next(r for r in rows if r["sigma"].startswith("2.0"))
        print(f"{label:6s} {n_modes:2d}->{n_modes+2:2d}  "
              f"env|true|={serial(envC,5)}  "
              f"[s=1] A={r1['A_dFF_abs'][:9]} B={r1['B_binc_abs'][:9]} C={r1['C_true_abs'][:9]} N2C={r1['N2C']}  "
              f"[s=2] N2C={r2['N2C']}", flush=True)
    return {"label": label, "steps": steps}


def main():
    dps = 60
    lam_int = 6
    max_modes = 20
    sigmas = [mp.mpf(x) for x in ["0.55", "0.6", "0.75", "1.0", "1.5", "2.0", "3.0"]]
    result = {"statement": "TRUE LOGT-CELL = Delta[T'/T] with moving boundary pole d_{b,N}=2piN/L",
              "parameters": {"lambda": lam_int, "max_modes": max_modes, "dps": dps},
              "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        result["cases"].append(run_case(label, planted, lam_int, max_modes, dps, sigmas))
    out = HERE / "E78_149_true_logt_cell_results.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
