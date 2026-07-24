#!/usr/bin/env python3
"""E78.3 - mu_ref reconciliation probe.

Well-posed BTG-DIV-L object:
  S_N(mu) = ||A_N(mu)^{-1} b_N||^2 = sum_j |<u_j^(N), b_N>|^2 / (nu_j^(N) - mu)^2
with
  H     = build_mp(lam, N)      on indices -N..N     (size 2N+1),
  inner = H[1:-1, 1:-1]         on indices -N+1..N-1  (= A_N(0), size 2N-1),
  b_N   = H[1:-1, last col]     = boundary column at index +N restricted to inner,
  (nu_j, u_j) = eigenpairs of inner.

We store (nu_j, coeff_j=<u_j,b_N>) for every N so that S_N(mu) can be evaluated
for ANY mu in post-processing:
  - mu = mu_ref  (frozen N=18 full-matrix ground, the E77.7f surrogate),
  - mu = mu_L_est (extrapolated true limit of nu_0^(N)),
  - the moving-floor distance delta_N = nu_0^(N) - mu_L_est and coupling c0.

Reuses P76.002 build_mp verbatim.  Building H directly at each N reproduces the
centered section of any larger reference matrix (entries depend only on m,n,L).
"""

import sys
import json
import time
import argparse
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(
    0,
    "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock",
)
from P76_002_mp_entry_audit import build_mp  # noqa: E402

PLANT = ("14.134725141734693790", "0.30", "5.0")


def ser(x, d=30):
    return mp.nstr(x, d)


def centered_section(Hmax, Nmax, N):
    """Centered submatrix of Hmax (indices -Nmax..Nmax) on indices -N..N."""
    off = Nmax - N
    return Hmax[off:Hmax.rows - off, off:Hmax.cols - off]


def full_ground(Hmax, Nmax, N):
    """Ground/2nd eigenvalue of the FULL size-(2N+1) section (E77.7f mu_ref object)."""
    H = centered_section(Hmax, Nmax, N)
    vals, _ = mp.eigsy(H)
    xs = sorted(vals[i] for i in range(vals.rows))
    return xs[0], xs[1]


def section_data(Hmax, Nmax, N):
    """Return per-N raw data: inner eigenvalues nu_j and couplings coeff_j=<u_j,b_N>."""
    H = centered_section(Hmax, Nmax, N)
    n = H.rows
    inner = H[1:n - 1, 1:n - 1]
    b = mp.matrix([H[j + 1, n - 1] for j in range(n - 2)])  # boundary column +N on inner rows
    vals, vecs = mp.eigsy(inner)
    m = vals.rows
    order = sorted(range(m), key=lambda i: vals[i])
    nus = [vals[i] for i in order]
    coeffs = []
    for i in order:
        vec = vecs[:, i]
        coeffs.append((vec.T * b)[0])
    bnorm = mp.sqrt(mp.fsum(abs(b[j]) ** 2 for j in range(b.rows)))
    return {
        "N": N,
        "dim_inner": m,
        "nus": nus,
        "coeffs": coeffs,
        "b_norm": bnorm,
        "nu0": nus[0],
        "nu1": nus[1],
        "intra_gap": nus[1] - nus[0],   # E78.1 style gap (two lowest inner eigs)
        "c0": abs(coeffs[0]),
    }


def S_of_mu(data, mu):
    """S_N(mu) = sum_j coeff_j^2 / (nu_j - mu)^2 from stored spectral data."""
    tot = mp.mpf(0)
    for nu, c in zip(data["nus"], data["coeffs"]):
        tot += abs(c) ** 2 / (nu - mu) ** 2
    return tot


def dominant_term(data, mu):
    return abs(data["coeffs"][0]) ** 2 / (data["nus"][0] - mu) ** 2


def aitken_limit(seq):
    """Aitken delta^2 extrapolation on last three terms; returns extrapolated limit."""
    if len(seq) < 3:
        return None
    a, b, c = seq[-3], seq[-2], seq[-1]
    denom = (c - b) - (b - a)
    if denom == 0:
        return None
    return c - (c - b) ** 2 / denom


def run(lam, dps, Ns, ref_N):
    mp.mp.dps = dps
    out = {
        "statement": "E78.3 mu_ref reconciliation: S_N at frozen surrogate vs true limit",
        "parameters": {"lambda": lam, "dps": dps, "Ns": Ns, "ref_N": ref_N,
                       "plant": {"gamma": PLANT[0], "beta": PLANT[1], "strength": PLANT[2]}},
        "builds": {},
    }
    Nmax = max(max(Ns), ref_N)
    for label, planted in (("zeta", None), ("plant", PLANT)):
        print(f"===== {label} dps={dps} =====", flush=True)
        t0 = time.time()
        Hmax, idxmax, L = build_mp(lam, Nmax, dps, planted=planted)
        print(f"  built Hmax Nmax={Nmax} dim={Hmax.rows} [{time.time()-t0:.1f}s]", flush=True)
        # frozen mu_ref = full-matrix ground at ref_N (centered section)
        mu_ref, mu_ref_1 = full_ground(Hmax, Nmax, ref_N)
        print(f"  mu_ref (full ground N={ref_N}) = {ser(mu_ref)}", flush=True)
        rows = []
        nu0_seq = []
        for N in Ns:
            t0 = time.time()
            d = section_data(Hmax, Nmax, N)
            nu0_seq.append(d["nu0"])
            rows.append(d)
            print(f"  N={N:2d} nu0={ser(d['nu0'],16):>22s} "
                  f"intra_gap={ser(d['intra_gap'],8):>12s} "
                  f"c0={ser(d['c0'],8):>12s}  [{time.time()-t0:.1f}s]", flush=True)
        # extrapolate mu_L from nu0 sequence (Aitken on last three)
        mu_L_est = aitken_limit(nu0_seq)
        # also a couple of running Aitken estimates for stability
        aitken_track = []
        for k in range(3, len(nu0_seq) + 1):
            a = aitken_limit(nu0_seq[:k])
            aitken_track.append(ser(a) if a is not None else None)
        print(f"  mu_L_est (Aitken) = {ser(mu_L_est) if mu_L_est else None}", flush=True)

        build_rows = []
        for d in rows:
            N = d["N"]
            S_ref = S_of_mu(d, mu_ref)
            S_L = S_of_mu(d, mu_L_est) if mu_L_est is not None else None
            delta_N = d["nu0"] - mu_L_est if mu_L_est is not None else None
            row = {
                "N": N,
                "dim_inner": d["dim_inner"],
                "nu0": ser(d["nu0"]),
                "nu1": ser(d["nu1"]),
                "intra_gap_nu1_minus_nu0": ser(d["intra_gap"]),
                "c0_coupling_abs": ser(d["c0"]),
                "b_norm": ser(d["b_norm"]),
                "S_at_mu_ref": ser(S_ref),
                "dominant_term_at_mu_ref": ser(dominant_term(d, mu_ref)),
                "nu0_minus_mu_ref": ser(d["nu0"] - mu_ref),
                "S_at_mu_L_est": ser(S_L) if S_L is not None else None,
                "dominant_term_at_mu_L_est": ser(dominant_term(d, mu_L_est)) if mu_L_est is not None else None,
                "delta_N_nu0_minus_muL": ser(delta_N) if delta_N is not None else None,
                "c0_over_delta_N": ser(d["c0"] / delta_N) if (delta_N is not None and delta_N != 0) else None,
            }
            build_rows.append(row)
        out["builds"][label] = {
            "mu_ref_full_ground_at_ref_N": ser(mu_ref),
            "mu_ref_full_gap": ser(mu_ref_1 - mu_ref),
            "nu0_sequence": [ser(x) for x in nu0_seq],
            "aitken_running_track": aitken_track,
            "mu_L_est": ser(mu_L_est) if mu_L_est is not None else None,
            "rows": build_rows,
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lambda", dest="lam", type=int, default=6)
    ap.add_argument("--dps", type=int, default=80)
    ap.add_argument("--Ns", type=str, default="6,8,10,12,14,16,18,20,22")
    ap.add_argument("--ref-N", type=int, default=18)
    ap.add_argument("--output", type=Path, default=HERE / "E78_3_mu_ref_reconciliation_results.json")
    args = ap.parse_args()
    Ns = [int(x) for x in args.Ns.split(",")]
    res = run(args.lam, args.dps, Ns, args.ref_N)
    args.output.write_text(json.dumps(res, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}", flush=True)


if __name__ == "__main__":
    main()
