#!/usr/bin/env python3
"""Visual diagnostic for the Deep-Lambda limit.

This is deliberately not a certificate.  It compares:

* the ordinary zeta Li coefficients extracted at two Cauchy radii;
* the exact critical quartet (deep density identically zero);
* the exact exterior quartet of 104_81 (deep density tending to 1/8).

No plotting package is required; the program writes an SVG directly.
"""

from math import exp, log, log1p, sqrt
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PHASE = HERE.parent
P103 = PHASE.parent / "phase-103-direct-a1-closure" / "tools"
sys.path.insert(0, str(P103))

from zeta_tools import li_lambda  # noqa: E402


WIDTH = 1280
HEIGHT = 900
EULER_GAMMA = 0.5772156649015329


def harmonic_prefix(nmax):
    out = [0.0] * (nmax + 1)
    value = 0.0
    for n in range(1, nmax + 1):
        value += 1.0 / n
        out[n] = value
    return out


def exterior_density_samples(xs, radius):
    """Compute D_X at all requested X in one pass."""
    xmax = max(xs)
    log_r = log(radius)
    harmonic = harmonic_prefix(xmax)
    harmonic_quarters = harmonic_prefix(xmax // 4)

    def log_depth(n):
        a = n * log_r
        log_total = log(2.0) + a + log1p(exp(-2.0 * a))
        correction = 4.0 + log(n + 1.0)
        scaled = correction * exp(-log_total)
        if scaled >= 1.0:
            return float("-inf")
        return log_total + log1p(-scaled)

    values = []
    for x in xs:
        threshold = sqrt(x)
        qmax = x // 4
        if qmax == 0 or log_depth(4 * qmax) < threshold:
            values.append(0.0)
            continue
        lo, hi = 1, qmax
        while lo < hi:
            mid = (lo + hi) // 2
            if log_depth(4 * mid) >= threshold:
                hi = mid
            else:
                lo = mid + 1
        bad = 0.25 * (harmonic_quarters[qmax] - harmonic_quarters[lo - 1])
        values.append(bad / harmonic[x])
    return values


def line(points, color, width=2.0, dash=None, opacity=1.0):
    attrs = [f'fill="none"', f'stroke="{color}"', f'stroke-width="{width}"',
             f'opacity="{opacity}"']
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    return f'<polyline {" ".join(attrs)} points="{coords}"/>'


def text(x, y, value, size=16, color="#17202a", anchor="start", weight="normal"):
    safe = (str(value).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))
    return (f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" '
            f'font-size="{size}" fill="{color}" text-anchor="{anchor}" '
            f'font-weight="{weight}">{safe}</text>')


def map_linear(v, lo, hi, p0, p1):
    return p0 + (v - lo) * (p1 - p0) / (hi - lo)


def map_log(v, lo, hi, p0, p1):
    return map_linear(log(v), log(lo), log(hi), p0, p1)


def main():
    nmax = 2000
    mfft = 1 << 19
    lam_a = li_lambda(nmax, r=0.997, M=mfft)
    lam_b = li_lambda(nmax, r=0.990, M=mfft)
    discrepancy = abs(lam_a - lam_b)
    xvals = [float(lam_a[n - 1] + log(n + 1.0)) for n in range(1, nmax + 1)]

    # Logarithmic X-grid for the exact exterior control.
    raw = [int(round(exp(log(1600) + j * (log(2_560_000) - log(1600)) / 39)))
           for j in range(40)]
    xs = sorted(set(max(16, 4 * (x // 4)) for x in raw))
    radius = 201.0 / 200.0
    dens = exterior_density_samples(xs, radius)
    log_radius = log(radius)
    accelerated = [
        d * (log(x) + EULER_GAMMA) / log(x)
        - log(log_radius) / (4.0 * log(x))
        for x, d in zip(xs, dens)
    ]

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<rect width="100%" height="100%" fill="#fbfcfc"/>',
        text(50, 42, "Diagnóstico visual del límite Deep-Λ", 26, weight="bold"),
        text(50, 68, "Zeta ordinaria (rango finito) frente al falsificador exterior exacto", 15,
             color="#566573"),
    ]

    # Panel 1: ordinary Li coefficients.
    x0, x1, y0, y1 = 82, 1225, 115, 425
    svg += [
        f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="white" '
        'stroke="#ccd1d1"/>',
        text(x0, y0 - 15, "A. Coeficientes de Li ordinarios calculados", 18, weight="bold"),
    ]
    ymin = 0.0
    ymax = max(xvals) * 1.04
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        yy = map_linear(frac, 0, 1, y1, y0)
        val = ymin + frac * (ymax - ymin)
        svg.append(f'<line x1="{x0}" y1="{yy:.2f}" x2="{x1}" y2="{yy:.2f}" '
                   'stroke="#e5e7e9"/>')
        svg.append(text(x0 - 10, yy + 5, f"{val:.0f}", 13, anchor="end", color="#566573"))
    pts = [(map_linear(n, 1, nmax, x0, x1), map_linear(xvals[n-1], ymin, ymax, y1, y0))
           for n in range(1, nmax + 1)]
    svg.append(line(pts, "#1565c0", 2.2))
    for n in (1, 400, 800, 1200, 1600, 2000):
        xx = map_linear(n, 1, nmax, x0, x1)
        svg.append(f'<line x1="{xx:.2f}" y1="{y1}" x2="{xx:.2f}" y2="{y1+6}" '
                   'stroke="#566573"/>')
        svg.append(text(xx, y1 + 24, str(n), 13, anchor="middle", color="#566573"))
    svg.append(text((x0+x1)/2, y1 + 48, "grado n", 14, anchor="middle"))
    svg.append(text(x0 + 18, y0 + 28, "xₙ = λₙ + log(n+1)", 15, color="#1565c0",
                    weight="bold"))
    svg.append(text(x0 + 18, y0 + 52,
                    f"mínimo={min(xvals):.6g}; discrepancia máx. entre radios={max(discrepancy):.3g}",
                    13, color="#566573"))

    # Panel 2: Deep density for the exact exterior control.
    x0b, x1b, y0b, y1b = 82, 1225, 535, 825
    svg += [
        f'<rect x="{x0b}" y="{y0b}" width="{x1b-x0b}" height="{y1b-y0b}" fill="white" '
        'stroke="#ccd1d1"/>',
        text(x0b, y0b - 15, "B. Densidad logarítmica del evento profundo", 18, weight="bold"),
    ]
    dmax = 0.135
    for val in (0.0, 0.025, 0.05, 0.075, 0.10, 0.125):
        yy = map_linear(val, 0, dmax, y1b, y0b)
        svg.append(f'<line x1="{x0b}" y1="{yy:.2f}" x2="{x1b}" y2="{yy:.2f}" '
                   'stroke="#e5e7e9"/>')
        svg.append(text(x0b - 10, yy + 5, f"{val:.3f}", 13, anchor="end", color="#566573"))
    for xv in (2_000, 10_000, 100_000, 1_000_000, 2_560_000):
        xx = map_log(xv, xs[0], xs[-1], x0b, x1b)
        svg.append(f'<line x1="{xx:.2f}" y1="{y1b}" x2="{xx:.2f}" y2="{y1b+6}" '
                   'stroke="#566573"/>')
        svg.append(text(xx, y1b + 24, f"{xv:g}", 12, anchor="middle", color="#566573"))
    extpts = [(map_log(x, xs[0], xs[-1], x0b, x1b),
               map_linear(d, 0, dmax, y1b, y0b)) for x, d in zip(xs, dens)]
    svg.append(line(extpts, "#c62828", 2.4))
    # The first-order acceleration is asymptotic; omit its small-X values
    # when they lie outside the displayed density window.
    accpts = [(map_log(x, xs[0], xs[-1], x0b, x1b),
               map_linear(d, 0, dmax, y1b, y0b))
              for x, d in zip(xs, accelerated) if 0.0 <= d <= dmax]
    svg.append(line(accpts, "#ef6c00", 2.0, "7 5"))
    target_y = map_linear(0.125, 0, dmax, y1b, y0b)
    svg.append(line([(x0b, target_y), (x1b, target_y)], "#c62828", 1.3, "8 6", 0.7))
    zero_y = map_linear(0.0, 0, dmax, y1b, y0b)
    svg.append(line([(x0b, zero_y), (x1b, zero_y)], "#1565c0", 3.0))
    svg.append(text(x0b + 18, y0b + 72, "cuarteto exterior R=201/200 → 1/8", 14,
                    color="#c62828", weight="bold"))
    svg.append(text(x0b + 18, y0b + 94,
                    "renormalización exacta de (5b) → 1/8", 14,
                    color="#ef6c00", weight="bold"))
    svg.append(text(x0b + 18, y0b + 116,
                    "cuarteto crítico = 0 exactamente; zeta calculada = 0 solo hasta X=2000",
                    14, color="#1565c0", weight="bold"))
    svg.append(text((x0b+x1b)/2, y1b + 52, "X (escala logarítmica)", 14,
                    anchor="middle"))

    svg.append(text(1230, 885,
                    "Diagnóstico float64: no certificado y no extrapolable al límite X→∞.",
                    13, color="#7b241c", anchor="end"))
    svg.append("</svg>")

    target = PHASE / "deep_lambda_visual_diagnostic.svg"
    target.write_text("\n".join(svg), encoding="utf-8")
    print(f"wrote {target}")
    print(f"ordinary range: 1 <= n <= {nmax}")
    print(f"min x_n={min(xvals):.12g}, max x_n={max(xvals):.12g}")
    print(f"two-radius max discrepancy={max(discrepancy):.12g}")
    print(f"exterior density at X={xs[-1]}: {dens[-1]:.12g} (limit 0.125)")
    print(f"accelerated exterior statistic at X={xs[-1]}: {accelerated[-1]:.12g}")
    print("ordinary finite Deep density: 0 on the computed range")
    print("WARNING: finite zero density is not a proof of the limiting value")


if __name__ == "__main__":
    main()
