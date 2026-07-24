#!/usr/bin/env python3
"""Fix for E78.144 plant N=16 self-singularity artifact: use nu0 at N=18 as
the mu_L proxy (instead of N=16's own nu0), then re-evaluate S_N at N=16 with
that DIFFERENT-section proxy, avoiding evaluating a section at its own pole."""
import sys, json
from pathlib import Path
import mpmath as mp

PHASE76 = Path("/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock")
sys.path.insert(0, str(PHASE76))
from P76_002_mp_entry_audit import build_mp

GAMMA = "14.134725141734693790"
BETA = "0.30"
STRENGTH = "5"

def gate_one(lam, n_modes, dps, planted=None):
    H, idx, L = build_mp(lam, n_modes, dps, planted=planted)
    A = H[1:H.rows-1, 1:H.cols-1]
    b = mp.matrix([H[i, H.cols-1] for i in range(1, H.rows-1)])
    vals, vecs = mp.eigsy(A)
    return vals, vecs, b

def S_N_full(vals, vecs, b, mu):
    total = mp.mpf(0); bottom = None
    for j in range(vals.rows):
        vec = vecs[:, j]
        coeff = (vec.T*b)[0]
        term = abs(coeff)**2/(vals[j]-mu)**2
        if j == 0: bottom = term
        total += term
    return total, bottom

def main():
    dps = 70
    planted = (GAMMA, BETA, STRENGTH)
    vals18, vecs18, b18 = gate_one(6, 18, dps, planted=planted)
    mu_proxy18 = vals18[0]
    print("mu_proxy (nu0 at N=18) =", mp.nstr(mu_proxy18, 20))

    vals16, vecs16, b16 = gate_one(6, 16, dps, planted=planted)
    nu0_16 = vals16[0]
    u0_16 = vecs16[:, 0]
    c0_16 = (u0_16.T*b16)[0]
    S_total, S_bottom = S_N_full(vals16, vecs16, b16, mu_proxy18)
    rec = {
        "n_modes": 16,
        "dim_inner": vals16.rows,
        "nu0": mp.nstr(nu0_16, 30),
        "c0": mp.nstr(c0_16, 30),
        "mu_proxy_source": "nu0 at N=18",
        "mu_proxy_value": mp.nstr(mu_proxy18, 30),
        "S_total_at_mu": mp.nstr(S_total, 20),
        "S_bottom_at_mu": mp.nstr(S_bottom, 20),
        "bottom_fraction_of_S": mp.nstr(S_bottom/S_total, 15),
        "c0_over_nu0": mp.nstr(abs(c0_16)/abs(nu0_16), 20),
    }
    print(json.dumps(rec, indent=2))
    with open("E78_145_plant_n16_fixed_results.json", "w") as f:
        json.dump(rec, f, indent=2)

if __name__ == "__main__":
    main()
