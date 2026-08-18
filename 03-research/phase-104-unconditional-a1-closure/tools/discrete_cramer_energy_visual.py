#!/usr/bin/env python3
"""Numerical diagnostics for the exact discrete Cramer energy of 104_93.

Only ordinary von Mangoldt weights are used.  The arithmetic identity

    Lambda(p**k) / log(p**k) = 1/k

lets us avoid evaluating Lambda itself.  The script also runs critical and
off-critical power-law controls and audits float64 against longdouble.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
PHASE = HERE.parent


def prime_sieve(limit: int) -> np.ndarray:
    is_prime = np.ones(limit + 1, dtype=np.bool_)
    is_prime[:2] = False
    top = math.isqrt(limit)
    for p in range(2, top + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = False
    return np.flatnonzero(is_prime)


def prime_power_data(limit: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return primes and the higher prime powers p**k with weights 1/k.

    Keeping a dense float array up to ``limit`` costs eight bytes per
    integer and makes the diagnostic memory-bound.  Primes are inserted
    chunkwise with weight one; only powers k>=2 need a sparse table.
    """
    primes = prime_sieve(limit)
    powers: list[int] = []
    weights: list[float] = []
    for p0 in primes:
        p = int(p0)
        if p > limit // p:
            break
        power = p * p
        k = 2
        while power <= limit:
            powers.append(power)
            weights.append(1.0 / k)
            if power > limit // p:
                break
            power *= p
            k += 1
    order = np.argsort(np.asarray(powers, dtype=np.int64))
    power_array = np.asarray(powers, dtype=np.int64)[order]
    weight_array = np.asarray(weights, dtype=np.float64)[order]
    return primes, power_array, weight_array


def audit_prime_power_table(limit: int = 10_000) -> None:
    """Independent trial-division audit of Lambda(n)/log(n)."""
    primes, powers, weights = prime_power_data(limit)
    table = np.zeros(limit + 1, dtype=np.float64)
    table[primes] = 1.0
    table[powers] = weights
    for n in range(2, limit + 1):
        q = n
        expected = 0.0
        for p0 in primes:
            p = int(p0)
            if p * p > q:
                if q > 1:
                    expected = 1.0 if q == n else 0.0
                break
            if q % p == 0:
                k = 0
                while q % p == 0:
                    q //= p
                    k += 1
                expected = 1.0 / k if q == 1 else 0.0
                break
        else:
            expected = 1.0
        if table[n] != expected:
            raise AssertionError((n, table[n], expected))


def ordinary_energy(limit: int, chunk: int = 1_000_000, audit_longdouble: bool = False):
    primes, powers, power_weights = prime_power_data(limit)
    pp_count = len(primes) + len(powers)
    b64 = np.float64(0.0)
    e64 = np.float64(0.0)
    bld = np.longdouble(0.0)
    eld = np.longdouble(0.0)
    checkpoints: list[dict[str, float]] = []
    dyadic: list[dict[str, float]] = []
    next_pow = 2
    block_start_e = np.longdouble(0.0)
    min_b = (math.inf, -1)
    max_b = (-math.inf, -1)

    for lo in range(2, limit + 1, chunk):
        hi = min(limit + 1, lo + chunk)
        n64 = np.arange(lo, hi, dtype=np.float64)
        invlog64 = 1.0 / np.log(n64)
        delta64 = -invlog64
        p0 = int(np.searchsorted(primes, lo, side="left"))
        p1 = int(np.searchsorted(primes, hi, side="left"))
        delta64[primes[p0:p1] - lo] += 1.0
        q0 = int(np.searchsorted(powers, lo, side="left"))
        q1 = int(np.searchsorted(powers, hi, side="left"))
        delta64[powers[q0:q1] - lo] += power_weights[q0:q1]
        B64 = b64 + np.cumsum(delta64, dtype=np.float64)
        inc64 = B64 * B64 / (n64 * (n64 + 1.0))
        E64 = e64 + np.cumsum(inc64, dtype=np.float64)

        if audit_longdouble:
            nld = n64.astype(np.longdouble)
            delta_ld = -1 / np.log(nld)
            delta_ld[primes[p0:p1] - lo] += 1
            delta_ld[powers[q0:q1] - lo] += power_weights[q0:q1].astype(np.longdouble)
            Bld = bld + np.cumsum(delta_ld, dtype=np.longdouble)
            inc_ld = Bld * Bld / (nld * (nld + 1))
            Eld = eld + np.cumsum(inc_ld, dtype=np.longdouble)
        else:
            # The large run is float64.  A separate prefix run below audits
            # it against longdouble without paying the longdouble-log cost at
            # every requested large cutoff.
            Bld, Eld = B64, E64

        local_min = int(np.argmin(Bld))
        local_max = int(np.argmax(Bld))
        if float(Bld[local_min]) < min_b[0]:
            min_b = (float(Bld[local_min]), lo + local_min)
        if float(Bld[local_max]) > max_b[0]:
            max_b = (float(Bld[local_max]), lo + local_max)

        while next_pow <= hi - 1:
            idx = next_pow - lo
            e_here = Eld[idx]
            b_here = Bld[idx]
            j = int(round(math.log2(next_pow)))
            delta_e = e_here - block_start_e
            dyadic.append(
                {
                    "j": j,
                    "N": next_pow,
                    "B": float(b_here),
                    "E": float(e_here),
                    "Delta": float(delta_e),
                    "j2_Delta": float(j * j * delta_e),
                }
            )
            block_start_e = e_here
            next_pow *= 2

        b64, e64 = B64[-1], E64[-1]
        bld, eld = Bld[-1], Eld[-1]

        checkpoints.append(
            {
                "N": hi - 1,
                "B": float(bld),
                "E": float(eld),
                "abs_B64_ld": abs(float(b64 - bld)),
                "abs_E64_ld": abs(float(e64 - eld)),
            }
        )

    return {
        "prime_power_count": pp_count,
        "B": float(bld),
        "E": float(eld),
        "B64_error": abs(float(b64 - bld)) if audit_longdouble else math.nan,
        "E64_error": abs(float(e64 - eld)) if audit_longdouble else math.nan,
        "min_B": min_b,
        "max_B": max_b,
        "dyadic": dyadic,
        "checkpoints": checkpoints,
    }


def model_energy(beta: float, limit: int, gamma: float = 7.0):
    """Energy with prescribed primitive B_m=m^beta*cos(gamma log m)/log m."""
    e = np.longdouble(0)
    rows = []
    for j in range(2, int(math.log2(limit)) + 1):
        lo = 1 << (j - 1)
        hi = (1 << j) - 1
        n = np.arange(lo, hi + 1, dtype=np.float64)
        B = n**beta * np.cos(gamma * np.log(n)) / np.log(n)
        d = np.sum(B * B / (n * (n + 1)), dtype=np.float64)
        e += d
        # At beta>1/2, Delta_j * j^2 / 2^((2 beta - 1)j)
        # should stay on a constant scale.  At beta=1/2 use j^2 Delta_j.
        scale = j * j * float(d) / (2.0 ** ((2.0 * beta - 1.0) * j))
        rows.append((j, float(d), float(e), scale))
    return rows


def write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def write_svg(path: Path, ordinary, critical, exterior) -> None:
    width, height = 1120, 720
    left, right, top, bottom = 90, 35, 45, 78
    pw, ph = width - left - right, height - top - bottom
    ordinary_rows = ordinary["dyadic"]
    jmin = min(r["j"] for r in ordinary_rows if r["j"] >= 3)
    jmax = max(r["j"] for r in ordinary_rows)

    series = {
        "ordinary Lambda": [(r["j"], r["j2_Delta"]) for r in ordinary_rows if r["j"] >= 3],
        "critical control beta=1/2": [(j, j * j * d) for j, d, _e, _s in critical],
        "off-line control beta=0.65": [(j, j * j * d) for j, d, _e, _s in exterior],
    }
    vals = [max(v, 1e-12) for pts in series.values() for j, v in pts if jmin <= j <= jmax]
    ymin, ymax = min(vals), max(vals)
    ly0, ly1 = math.log10(ymin) - 0.15, math.log10(ymax) + 0.15

    def xy(j, v):
        x = left + pw * (j - jmin) / max(1, jmax - jmin)
        y = top + ph * (ly1 - math.log10(max(v, 1e-300))) / (ly1 - ly0)
        return x, y

    colors = {"ordinary Lambda": "#1565c0", "critical control beta=1/2": "#2e7d32", "off-line control beta=0.65": "#c62828"}
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="560" y="25" text-anchor="middle" font-family="sans-serif" font-size="18">Dyadic discrete Cramer energy: j² Δ_j</text>',
    ]
    for k in range(math.floor(ly0), math.ceil(ly1) + 1):
        y = top + ph * (ly1 - k) / (ly1 - ly0)
        out.append(f'<line x1="{left}" y1="{y:.2f}" x2="{left+pw}" y2="{y:.2f}" stroke="#dddddd"/>')
        out.append(f'<text x="{left-8}" y="{y+5:.2f}" text-anchor="end" font-family="monospace" font-size="12">10^{k}</text>')
    for j in range(jmin, jmax + 1):
        x, _ = xy(j, 1)
        out.append(f'<line x1="{x:.2f}" y1="{top}" x2="{x:.2f}" y2="{top+ph}" stroke="#f0f0f0"/>')
        out.append(f'<text x="{x:.2f}" y="{top+ph+22}" text-anchor="middle" font-family="monospace" font-size="12">{j}</text>')
    for name, pts in series.items():
        pts2 = [xy(j, v) for j, v in pts if jmin <= j <= jmax]
        path_d = " ".join(("M" if i == 0 else "L") + f" {x:.2f} {y:.2f}" for i, (x, y) in enumerate(pts2))
        out.append(f'<path d="{path_d}" fill="none" stroke="{colors[name]}" stroke-width="2.4"/>')
        for x, y in pts2:
            out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.5" fill="{colors[name]}"/>')
    out.append(f'<line x1="{left}" y1="{top+ph}" x2="{left+pw}" y2="{top+ph}" stroke="black"/>')
    out.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+ph}" stroke="black"/>')
    out.append(f'<text x="{left+pw/2}" y="{height-25}" text-anchor="middle" font-family="sans-serif" font-size="14">dyadic index j (N=2^j)</text>')
    legend_y = top + 18
    for i, name in enumerate(series):
        x0 = left + 20 + 285 * i
        out.append(f'<line x1="{x0}" y1="{legend_y}" x2="{x0+28}" y2="{legend_y}" stroke="{colors[name]}" stroke-width="3"/>')
        out.append(f'<text x="{x0+35}" y="{legend_y+5}" font-family="sans-serif" font-size="13">{name}</text>')
    out.append('</svg>')
    path.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10_000_000)
    ap.add_argument("--chunk", type=int, default=1_000_000)
    ap.add_argument("--audit-limit", type=int, default=1_000_000)
    args = ap.parse_args()
    if args.limit < 16:
        raise SystemExit("--limit must be at least 16")

    audit_prime_power_table()
    ordinary = ordinary_energy(args.limit, args.chunk, audit_longdouble=False)
    audit_limit = min(args.limit, args.audit_limit)
    audit = ordinary_energy(audit_limit, min(args.chunk, 100_000), audit_longdouble=True)
    audit_alt = ordinary_energy(audit_limit, 131_071, audit_longdouble=False)
    critical = model_energy(0.5, args.limit)
    exterior = model_energy(0.65, args.limit)

    write_csv(PHASE / "discrete_cramer_energy_dyadic.csv", ordinary["dyadic"])
    write_svg(PHASE / "discrete_cramer_energy_visual.svg", ordinary, critical, exterior)

    print("DISCRETE CRAMER ENERGY DIAGNOSTIC")
    print(f"limit={args.limit}")
    print(f"prime-power count={ordinary['prime_power_count']}")
    print(f"B(N)={ordinary['B']:.15g}")
    print(f"E(N)={ordinary['E']:.15g}")
    print(f"min B={ordinary['min_B'][0]:.15g} at n={ordinary['min_B'][1]}")
    print(f"max B={ordinary['max_B'][0]:.15g} at n={ordinary['max_B'][1]}")
    print(f"audit prefix={audit_limit}")
    print(f"float64/longdouble |dB|={audit['B64_error']:.3e}")
    print(f"float64/longdouble |dE|={audit['E64_error']:.3e}")
    print(f"chunk audit |dB|={abs(audit_alt['B'] - audit['B']):.3e}")
    print(f"chunk audit |dE|={abs(audit_alt['E'] - audit['E']):.3e}")
    print("dyadic rows: j N B E Delta j^2*Delta")
    for r in ordinary["dyadic"]:
        print(f"{r['j']:2d} {r['N']:9d} {r['B']: .8e} {r['E']: .8e} {r['Delta']: .8e} {r['j2_Delta']: .8e}")
    tail = [r for r in ordinary["dyadic"] if r["j"] >= max(4, ordinary["dyadic"][-1]["j"] - 7)]
    print(f"tail max j^2 Delta={max(r['j2_Delta'] for r in tail):.12g}")
    print(f"tail min j^2 Delta={min(r['j2_Delta'] for r in tail):.12g}")
    tested = [r for r in ordinary["dyadic"] if r["j"] >= 9]
    candidate_ok = all(r["j2_Delta"] <= 1 / 8 for r in tested)
    monotone = all(tested[k + 1]["j2_Delta"] <= tested[k]["j2_Delta"] for k in range(len(tested) - 1))
    stronger_1_20 = all(r["j2_Delta"] <= 1 / 20 for r in tested)
    print(f"candidate Delta_j <= 1/(8 j^2), tested j=9..{tested[-1]['j']}: {candidate_ok}")
    print(f"candidate j^2 Delta_j nonincreasing: {monotone}")
    print(f"stronger Delta_j <= 1/(20 j^2): {stronger_1_20}")
    if not candidate_ok:
        raise AssertionError("the registered finite candidate failed")
    if audit["B64_error"] > 1e-9 or audit["E64_error"] > 1e-12:
        raise AssertionError("float64/longdouble audit failed")
    print("control tail scaled values (critical, off-line normalized):")
    for rc, ro in zip(critical[-5:], exterior[-5:]):
        print(f"j={rc[0]:2d} critical={rc[3]:.8g} offline={ro[3]:.8g}")


if __name__ == "__main__":
    main()
