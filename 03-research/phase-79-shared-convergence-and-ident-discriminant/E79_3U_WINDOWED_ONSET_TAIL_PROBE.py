#!/usr/bin/env python3
"""E79.3u - windowed onset selector for the deep terminal tail.

Use the recurrent tau=0.4 onset, then score each later start by a short window
that combines two internal signals:

    - average normalized shell height over the next w shells,
    - geometric-mean local decay ratio over that same window.

The selector never looks at ZERO^extra when choosing the tail. ZERO^extra is
used only afterward to audit whether this less brittle mesoscopic geometry
selects a better deep-edge tail than the one-step slope rule.
"""

from __future__ import annotations

import json
import math
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
TAU = mp.mpf("0.4")
WINDOWS = [2, 3, 4]


def p_kernel(a, sigma):
    return 2 * sigma / (a * a + sigma * sigma)


def window_key(w):
    return str(w)


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


def geom_mean(vals):
    if not vals:
        return mp.mpf("1")
    return mp.e ** (mp.fsum(mp.log(v) for v in vals) / len(vals))


def choose_start(active, onset, n):
    amps = [abs((n**2) * term) for term in active]
    peak = max(amps) if amps else mp.mpf("0")
    results = {}
    for w in WINDOWS:
        best = None
        if not active:
            results[window_key(w)] = {
                "start": 0,
                "take": 0,
                "window_seen": 0,
                "avg_height_over_peak": "0.0",
                "geom_decay": "1.0",
                "score": "0.0",
            }
            continue
        start0 = min(onset, len(active) - 1)
        for start in range(start0, len(active)):
            stop = min(len(active), start + w)
            window_amps = amps[start:stop]
            if not window_amps or peak == 0:
                avg_height = mp.mpf("0")
            else:
                avg_height = mp.fsum(window_amps) / (len(window_amps) * peak)
            ratios = []
            for j in range(start + 1, stop):
                prev_amp = amps[j - 1]
                curr_amp = amps[j]
                if prev_amp == 0:
                    ratios.append(mp.mpf("1"))
                else:
                    ratios.append(curr_amp / prev_amp)
            decay = geom_mean(ratios)
            score = avg_height * decay
            candidate = (float(score), start, avg_height, decay, stop - start)
            if best is None or candidate < best:
                best = candidate
        assert best is not None
        _, start, avg_height, decay, seen = best
        results[window_key(w)] = {
            "start": start,
            "take": len(active) - start,
            "window_seen": seen,
            "avg_height_over_peak": mp.nstr(avg_height, 12),
            "geom_decay": mp.nstr(decay, 12),
            "score": mp.nstr(mp.mpf(best[0]), 12),
        }
    return results


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
        dim_n = len(k_n)
        dim_m = len(k_m)
        dim_common = min(dim_n, dim_m)
        row = {"N": n, "dim_common": dim_common, "sigmas": {}}
        for sigma in SIGMAS:
            common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_common)]
            common_total = mp.fsum(common_terms)
            extra_total = mp.fsum(p_kernel(k_m[j], sigma) for j in range(dim_common, dim_m))

            active = []
            running = mp.mpf("0")
            for r in range(dim_common):
                term = common_terms[dim_common - 1 - r]
                active.append(term)
                running += term
                if common_total != 0 and abs(running / common_total) >= mp.mpf("0.99"):
                    break

            amps = [abs((n**2) * term) for term in active]
            peak = max(amps) if amps else mp.mpf("0")
            onset = len(active) - 1
            cutoff = TAU * peak
            while onset >= 0 and amps[onset] <= cutoff:
                onset -= 1
            onset += 1

            windows = choose_start(active, onset, n)
            for data in windows.values():
                start = data["start"]
                tail = mp.fsum(active[start:])
                minus = tail - extra_total
                scale = max(abs(tail), abs(extra_total))
                data["tail"] = mp.nstr(tail, 12)
                data["minus"] = mp.nstr(minus, 12)
                data["mismatch"] = None if scale == 0 else mp.nstr(abs(minus) / scale, 12)
                data["N2_abs_minus"] = mp.nstr((n**2) * abs(minus), 12)

            row["sigmas"][str(sigma)] = {
                "extra": mp.nstr(extra_total, 12),
                "active_len": len(active),
                "onset": onset,
                "windows": windows,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["windows"]
        best = min((float(v["mismatch"]), k, v) for k, v in s1.items())
        print(
            f"{label:5s} N={n:2d} onset={row['sigmas']['1.0']['onset']} "
            f"best_w={best[1]} take={best[2]['take']} mismatch={best[2]['mismatch']} "
            f"score={best[2]['score']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3u windowed onset tail selector", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3U_windowed_onset_tail_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
