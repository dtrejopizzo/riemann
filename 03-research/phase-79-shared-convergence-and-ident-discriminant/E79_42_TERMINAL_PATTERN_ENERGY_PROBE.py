#!/usr/bin/env python3
"""E79.42 - short relational energies on terminal supports.

Search a very small support class (size <= 3 inside the last 4 active shells),
but choose it by maximizing an internal energy, not by matching ZERO^extra.
This tests whether a genuinely short relational score can recover the sparse
packet geometry without full subset search.
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PHASE78 = HERE.parent / "phase-78-build-neutral-lp-and-ident"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))
sys.path.insert(0, str(PHASE78))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402

SIGMAS = [mp.mpf("1.0"), mp.mpf("2.0")]
WINDOW = 4
CARDINALITIES = [1, 2, 3]
ALPHAS = [mp.mpf("0.25"), mp.mpf("0.50"), mp.mpf("1.0")]
BETAS = [mp.mpf("0.0"), mp.mpf("0.25"), mp.mpf("0.50"), mp.mpf("1.0")]


def p_kernel(a, sigma):
    return 2 * sigma / (a * a + sigma * sigma)


def param_key(alpha, beta):
    return f"A{mp.nstr(alpha,4)}-B{mp.nstr(beta,4)}"


def kappas_for_section(H, idx, L):
    _, _, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    n = len(d)
    xv = mp.matrix([x[j] for j in range(n)])
    q = mp.matrix([d[j] - db for j in range(n)])
    c = 1 - mp.fsum(x[j] for j in range(n))
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf("0")) + xv[a] * q[b] / c
    eigvals, _ = mp.eig(K)
    return sorted([mp.re(ev) for ev in eigvals], key=lambda z: abs(z))


def active_common_terms(k_n, k_m, sigma):
    dim_common = min(len(k_n), len(k_m))
    common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_common)]
    common_total = mp.fsum(common_terms)
    active = []
    running = mp.mpf("0")
    for r in range(dim_common):
        term = common_terms[dim_common - 1 - r]
        active.append(term)
        running += term
        if common_total != 0 and abs(running / common_total) >= mp.mpf("0.99"):
            break
    extra_total = mp.fsum(p_kernel(k_m[j], sigma) for j in range(dim_common, len(k_m)))
    return active, extra_total, dim_common


def audit_support(active, extra_total, support):
    support = sorted(set(j for j in support if 0 <= j < len(active)))
    packet = mp.fsum(active[j] for j in support)
    minus = packet - extra_total
    scale = max(abs(packet), abs(extra_total))
    return {
        "support": support,
        "packet": mp.nstr(packet, 12),
        "minus": mp.nstr(minus, 12),
        "mismatch": None if scale == 0 else mp.nstr(abs(minus) / scale, 12),
    }


def energy(local_amps, subset, alpha, beta):
    # reward mass, penalize span, mildly reward separation among chosen sites
    mass = mp.fsum(local_amps[i] for i in subset)
    span = max(subset) - min(subset) if len(subset) >= 2 else 0
    sep_bonus = mp.fsum(abs(subset[j] - subset[i]) for i in range(len(subset)) for j in range(i + 1, len(subset)))
    return mass - alpha * span + beta * sep_bonus


def best_support_by_energy(active, alpha, beta):
    w = min(WINDOW, len(active))
    start = len(active) - w
    local_amps = [abs(active[start + i]) for i in range(w)]
    best = None
    for k in CARDINALITIES:
        if k > w:
            continue
        for subset in itertools.combinations(range(w), k):
            e = energy(local_amps, subset, alpha, beta)
            candidate = (e, -k, tuple(-i for i in subset), subset)
            if best is None or candidate > best:
                best = candidate
    assert best is not None
    subset = best[3]
    return [start + i for i in subset]


def run_case(label, planted, lam_int=6, max_n=18, dps=60):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam_int, max_n, dps, planted=planted)
    cache = {}

    def get_kappas(n):
        if n not in cache:
            Hn, idxn = section(H, idx, max_n, n)
            cache[n] = kappas_for_section(Hn, idxn, L)
        return cache[n]

    rows = []
    for n in range(8, max_n - 1, 2):
        k_n = get_kappas(n)
        k_m = get_kappas(n + 2)
        row = {"N": n, "sigmas": {}}
        for sigma in SIGMAS:
            active, extra_total, dim_common = active_common_terms(k_n, k_m, sigma)
            rules = {}
            for alpha in ALPHAS:
                for beta in BETAS:
                    support = best_support_by_energy(active, alpha, beta)
                    out = audit_support(active, extra_total, support)
                    out["window"] = min(WINDOW, len(active))
                    out["alpha"] = mp.nstr(alpha, 6)
                    out["beta"] = mp.nstr(beta, 6)
                    rules[param_key(alpha, beta)] = out
            row["sigmas"][str(sigma)] = {
                "dim_common": dim_common,
                "active_len": len(active),
                "extra": mp.nstr(extra_total, 12),
                "rules": rules,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["rules"]
        best = min((float(v["mismatch"]), k, v) for k, v in s1.items())
        print(f"{label:5s} N={n:2d} best={best[1]} support={best[2]['support']} mismatch={best[2]['mismatch']}", flush=True)
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.42 short relational pattern energies", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_42_terminal_pattern_energy_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
