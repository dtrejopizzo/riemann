#!/usr/bin/env python3
"""E78.1 - Ground-state simplicity / sign-structure probe for H_L = D_L + B_L.

Decisive empirical facts for interface subclause (e) (item 4):
  (i)   is mu_L = inf spec simple, with a gap that is robust (not collapsing to 0)?
  (ii)  is the off-diagonal sign pattern of H_L gauge-balanced, i.e. does there
        exist a diagonal D in {+-1} with all off-diagonals of D H D of one sign
        (the Perron-Frobenius / positivity-improving prerequisite)?
  (iii) is the ground eigenvector nodeless after that gauge (PF signature)?

Reuses the P76.002 build_mp infrastructure verbatim (zeta build + planted
falsifier). No new operator is constructed.
"""

import sys
import mpmath as mp

sys.path.insert(
    0,
    "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock",
)
from P76_002_mp_entry_audit import build_mp  # noqa: E402

PLANT = ("14.134725141734693790", "0.30", "5.0")


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def analyze(H, idx):
    d = H.rows
    # --- off-diagonal sign census ---
    npos = nneg = nzero = 0
    minabs_off = None
    for a in range(d):
        for b in range(a + 1, d):
            s = sign(H[a, b])
            if s > 0:
                npos += 1
            elif s < 0:
                nneg += 1
            else:
                nzero += 1
            av = abs(H[a, b])
            if minabs_off is None or av < minabs_off:
                minabs_off = av

    # --- gauge balance test ---
    # want D in {+-1} with D_a D_b sign(H[a,b]) <= 0 for all a!=b, i.e. all
    # off-diagonals of D H D nonpositive. Build D from row 0 spanning star,
    # then verify every pair.
    D = [1] * d
    for b in range(1, d):
        sb = sign(H[0, b])
        # want D_0 D_b sign(H[0,b]) < 0  => D_b = -sign(H[0,b]) (D_0=+1)
        D[b] = -sb if sb != 0 else 1
    violations = 0
    checked = 0
    for a in range(d):
        for b in range(a + 1, d):
            s = sign(H[a, b])
            if s == 0:
                continue
            checked += 1
            if D[a] * D[b] * s > 0:  # positive off-diagonal after gauge => bad
                violations += 1
    balanced = violations == 0

    # --- spectrum ---
    vals, vecs = mp.eigsy(H)
    lam = [vals[j] for j in range(vals.rows)]
    gap = lam[1] - lam[0]
    rel_gap = gap / (abs(lam[0]) + 1) if True else gap
    v0 = [vecs[j, 0] for j in range(d)]

    # --- nodeless test after gauge ---
    gv = [D[j] * v0[j] for j in range(d)]
    gpos = sum(1 for x in gv if x > 0)
    gneg = sum(1 for x in gv if x < 0)
    minabs_v0 = min(abs(x) for x in v0)

    return {
        "dim": d,
        "npos_off": npos,
        "nneg_off": nneg,
        "nzero_off": nzero,
        "minabs_off": minabs_off,
        "gauge_balanced": balanced,
        "gauge_violations": violations,
        "gauge_checked": checked,
        "lam0": lam[0],
        "lam1": lam[1],
        "gap": gap,
        "gauged_v0_pos": gpos,
        "gauged_v0_neg": gneg,
        "minabs_v0": minabs_v0,
    }


def run():
    mp.mp.dps = 70
    for build_name, planted in (("zeta", None), ("plant", PLANT)):
        print(f"===== build={build_name} =====")
        for n_modes in (4, 6, 8, 10):
            H, idx, L = build_mp(6, n_modes, 70, planted=planted)
            r = analyze(H, idx)
            print(
                f"N={n_modes:2d} dim={r['dim']:3d} "
                f"off+/-/0={r['npos_off']}/{r['nneg_off']}/{r['nzero_off']} "
                f"balanced={r['gauge_balanced']} viol={r['gauge_violations']}/{r['gauge_checked']}"
            )
            print(
                f"      lam0={mp.nstr(r['lam0'],8)} lam1={mp.nstr(r['lam1'],8)} "
                f"gap={mp.nstr(r['gap'],6)} minoff={mp.nstr(r['minabs_off'],4)}"
            )
            print(
                f"      gauged v0 signs +/-={r['gauged_v0_pos']}/{r['gauged_v0_neg']} "
                f"min|v0|={mp.nstr(r['minabs_v0'],4)}"
            )


if __name__ == "__main__":
    run()
