#!/usr/bin/env python3
"""Generate the Phase-105 visual map of A1 and the Deep limit.

No plotting dependency is required.  The script computes the visible A1
segment, the explicit off-line quartet diagnostic, and writes a standalone
SVG plus a small CSV ledger.
"""

from __future__ import annotations

import csv
import html
import math
from pathlib import Path
import runpy

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
PHASE = Path(__file__).resolve().parents[1]
ASSETS = PHASE / "assets"
ARCH_TOOL = ROOT / "phase-103-direct-a1-closure" / "tools" / "arch_and_margin.py"
THETA_TOOL = ROOT / "phase-104-unconditional-a1-closure" / "tools" / "theta_family_check.py"


def laguerre(degree: int, alpha: float, x: np.ndarray) -> np.ndarray:
    if degree == 0:
        return np.ones_like(x)
    lm1 = np.ones_like(x)
    l0 = alpha + 1.0 - x
    if degree == 1:
        return l0
    for k in range(1, degree):
        lp1 = ((2.0 * k + alpha + 1.0 - x) * l0 - (k + alpha) * lm1) / (k + 1.0)
        lm1, l0 = l0, lp1
    return l0


def chebyshev_psi(xmax: int) -> np.ndarray:
    prime = np.ones(xmax + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(xmax) + 1):
        if prime[p]:
            prime[p * p : xmax + 1 : p] = False
    mangoldt = np.zeros(xmax + 1, dtype=float)
    for p in np.flatnonzero(prime):
        value = int(p)
        weight = math.log(value)
        while value <= xmax:
            mangoldt[value] = weight
            if value > xmax // int(p):
                break
            value *= int(p)
    return np.cumsum(mangoldt)


def a1_data(n: int = 150, xmax: int = 1_000_000, points: int = 7000):
    arch = runpy.run_path(str(ARCH_TOOL))
    theta = runpy.run_path(str(THETA_TOOL))
    a_value = float(arch["lambda_arch"](n))
    log2 = math.log(2.0)
    boundary = float(laguerre(n, 1.0, np.array([log2]))[0])
    reserve = 0.75 * a_value + 1.0 - boundary
    cutoff = float(theta["T_n"](n, 0.25, a_value))

    psi = chebyshev_psi(xmax)
    u = np.linspace(log2, math.log(xmax), points)
    x = np.exp(u)
    indices = np.minimum(np.floor(x).astype(int), xmax)
    kernel = laguerre(n - 1, 2.0, u)
    integrand = (psi[indices] / x - 1.0) * kernel
    du = np.diff(u)
    cumulative = np.empty_like(u)
    cumulative[0] = 0.0
    cumulative[1:] = np.cumsum(0.5 * (integrand[:-1] + integrand[1:]) * du)
    return u, cumulative, a_value, boundary, reserve, cutoff


def deep_density(x: int, ratio: float = 201.0 / 200.0) -> float:
    harmonic = sum(1.0 / n for n in range(1, x + 1))
    log_r = math.log(ratio)
    threshold = math.sqrt(x)
    mass = 0.0
    for n in range(4, x + 1, 4):
        exponent = n * log_r
        log_main = math.log(2.0) + exponent + math.log1p(math.exp(-2.0 * exponent))
        correction_ratio = (4.0 + math.log(n + 1.0)) * math.exp(-log_main)
        if correction_ratio >= 1.0:
            continue
        log_magnitude = log_main + math.log1p(-correction_ratio)
        if log_magnitude >= threshold:
            mass += 1.0 / n
    return mass / harmonic


def polyline(points, color, width=3.0, dash=None, opacity=1.0):
    coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<polyline points="{coords}" fill="none" stroke="{color}" '
        f'stroke-width="{width}" stroke-linejoin="round" '
        f'stroke-linecap="round" opacity="{opacity}"{extra}/>'
    )


def text(x, y, value, size=20, color="#172033", weight="400", anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" '
        f'font-size="{size}" fill="{color}" font-weight="{weight}" '
        f'text-anchor="{anchor}">{html.escape(str(value))}</text>'
    )


def generate_svg() -> tuple[Path, dict]:
    u, cumulative, a_value, boundary, reserve, cutoff = a1_data()
    deep_x = np.unique(np.logspace(3, math.log10(2_560_000), 42).astype(int))
    deep_y = np.array([deep_density(int(value)) for value in deep_x])

    width, height = 1600, 1000
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="1600" height="1000" fill="#f7f8fb"/>',
        text(70, 62, "Phase 105 — A1 y el límite que decide RH", 34, "#111827", "700"),
        text(70, 98, "A1 es una barrera por grado; Deep es una convergencia a cero.", 20, "#4b5563"),
    ]

    # Panel A.
    px, py, pw, ph = 70, 145, 930, 535
    svg += [
        f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#ffffff" stroke="#d7dce5"/>',
        text(px + 28, py + 42, "A · A1 para n = 150", 25, "#111827", "700"),
        text(px + 28, py + 72, "J_150(U) debe quedar debajo de q_150 hasta U = T_150", 18, "#4b5563"),
    ]
    gx, gy, gw, gh = px + 72, py + 105, pw - 115, ph - 210
    ymin = min(-0.08 * reserve, float(cumulative.min()) * 1.15)
    ymax = reserve * 1.12
    ux0, ux1 = float(u[0]), float(u[-1])
    mapx = lambda value: gx + (value - ux0) / (ux1 - ux0) * gw
    mapy = lambda value: gy + gh - (value - ymin) / (ymax - ymin) * gh
    forbidden_y = mapy(reserve)
    svg += [
        f'<rect x="{gx}" y="{gy}" width="{gw}" height="{max(0, forbidden_y-gy):.2f}" fill="#fee2e2" opacity="0.72"/>',
        f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="#64748b"/>',
        f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="#64748b"/>',
        f'<line x1="{gx}" y1="{forbidden_y:.2f}" x2="{gx+gw}" y2="{forbidden_y:.2f}" stroke="#dc2626" stroke-width="3"/>',
        text(gx + gw - 8, forbidden_y - 10, f"q_150 = {reserve:.3f}", 17, "#b91c1c", "700", "end"),
        text(gx + 18, gy + 25, "REGIÓN PROHIBIDA", 16, "#b91c1c", "700"),
    ]
    curve = [(mapx(float(xv)), mapy(float(yv))) for xv, yv in zip(u[::8], cumulative[::8])]
    svg.append(polyline(curve, "#2563eb", 3.0))
    for tick in (math.log(2), 4, 7, 10, 13, math.log(1_000_000)):
        if ux0 <= tick <= ux1:
            tx = mapx(tick)
            svg += [
                f'<line x1="{tx:.2f}" y1="{gy+gh}" x2="{tx:.2f}" y2="{gy+gh+7}" stroke="#64748b"/>',
                text(tx, gy + gh + 28, f"{tick:.1f}", 14, "#64748b", anchor="middle"),
            ]
    for val in (0.0, reserve):
        ty = mapy(val)
        svg += [
            f'<line x1="{gx-7}" y1="{ty:.2f}" x2="{gx}" y2="{ty:.2f}" stroke="#64748b"/>',
            text(gx - 12, ty + 5, f"{val:.1f}", 14, "#64748b", anchor="end"),
        ]
    svg += [
        text(gx + gw / 2, gy + gh + 55, "U = log x  (tramo calculado hasta log 10⁶)", 16, "#475569", anchor="middle"),
        text(gx + 13, mapy(float(cumulative[-1])) - 13, "integral acumulada calculada", 16, "#1d4ed8", "600"),
        f'<path d="M {gx+gw-130} {gy+gh-42} C {gx+gw-70} {gy+gh-80}, {gx+gw-30} {gy+gh-110}, {gx+gw+5} {gy+gh-135}" fill="none" stroke="#6b7280" stroke-width="3" stroke-dasharray="8 7"/>',
        text(gx + gw - 12, gy + gh - 150, "después: desconocido", 15, "#6b7280", "600", "end"),
        text(px + 28, py + ph - 25, f"Corte de escala: log(10⁶) = {math.log(1_000_000):.2f}, pero T₁₅₀ ≈ {cutoff:.3e}.", 17, "#374151", "600"),
    ]

    # Zoom inset for the visible oscillations, otherwise compressed by q_150.
    ix, iy, iw, ih = gx + 80, gy + 78, 355, 145
    zmin = float(cumulative.min()) - 0.35
    zmax = float(cumulative.max()) + 0.35
    zmapx = lambda value: ix + (value - ux0) / (ux1 - ux0) * iw
    zmapy = lambda value: iy + ih - (value - zmin) / (zmax - zmin) * ih
    zoom_curve = [(zmapx(float(xv)), zmapy(float(yv))) for xv, yv in zip(u[::8], cumulative[::8])]
    svg += [
        f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="8" fill="#f8fafc" stroke="#94a3b8"/>',
        f'<line x1="{ix}" y1="{zmapy(0):.2f}" x2="{ix+iw}" y2="{zmapy(0):.2f}" stroke="#cbd5e1"/>',
        polyline(zoom_curve, "#2563eb", 2.3),
        text(ix + 12, iy + 22, f"zoom: {cumulative.min():.2f} ≤ J_150 ≤ {cumulative.max():.2f}", 14, "#1e40af", "600"),
    ]

    # Panel B.
    px, py, pw, ph = 1030, 145, 500, 535
    svg += [
        f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#ffffff" stroke="#d7dce5"/>',
        text(px + 26, py + 42, "B · El límite Deep", 25, "#111827", "700"),
        text(px + 26, py + 72, "Hay que probar Ωₓ → 0", 18, "#4b5563"),
    ]
    gx, gy, gw, gh = px + 68, py + 105, pw - 100, ph - 210
    lx0, lx1 = math.log10(float(deep_x[0])), math.log10(float(deep_x[-1]))
    mapx2 = lambda value: gx + (math.log10(value) - lx0) / (lx1 - lx0) * gw
    mapy2 = lambda value: gy + gh - value / 0.14 * gh
    svg += [
        f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" fill="#fff7ed" opacity="0.45"/>',
        f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="#64748b"/>',
        f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="#64748b"/>',
        f'<line x1="{gx}" y1="{mapy2(0.125):.2f}" x2="{gx+gw}" y2="{mapy2(0.125):.2f}" stroke="#f97316" stroke-width="2" stroke-dasharray="7 6"/>',
        text(gx + gw - 3, mapy2(0.125) - 8, "límite off-line = 1/8", 15, "#c2410c", "600", "end"),
        f'<line x1="{gx}" y1="{mapy2(0):.2f}" x2="{gx+gw}" y2="{mapy2(0):.2f}" stroke="#16a34a" stroke-width="4"/>',
        text(gx + 8, mapy2(0) - 12, "on-line / objetivo: 0", 15, "#15803d", "700"),
    ]
    deep_curve = [(mapx2(float(xv)), mapy2(float(yv))) for xv, yv in zip(deep_x, deep_y)]
    svg.append(polyline(deep_curve, "#ea580c", 3.0))
    for exponent in (3, 4, 5, 6):
        value = 10**exponent
        if deep_x[0] <= value <= deep_x[-1]:
            tx = mapx2(value)
            svg += [
                f'<line x1="{tx:.2f}" y1="{gy+gh}" x2="{tx:.2f}" y2="{gy+gh+7}" stroke="#64748b"/>',
                text(tx, gy + gh + 28, f"10^{exponent}", 14, "#64748b", anchor="middle"),
            ]
    for value in (0.0, 0.05, 0.10, 0.125):
        ty = mapy2(value)
        svg += [
            f'<line x1="{gx-7}" y1="{ty:.2f}" x2="{gx}" y2="{ty:.2f}" stroke="#64748b"/>',
            text(gx - 11, ty + 5, f"{value:.3f}", 13, "#64748b", anchor="end"),
        ]
    svg += [
        text(gx + gw / 2, gy + gh + 55, "X (escala logarítmica)", 16, "#475569", anchor="middle"),
        text(gx + 10, gy + 24, "cuarteto off-line de control", 15, "#c2410c", "600"),
        text(px + 26, py + ph - 25, "Si un modo exterior existe: liminf Ωₓ > 0.", 17, "#374151", "600"),
    ]

    # Bottom logical map.
    bx, by, bw, bh = 70, 715, 1460, 225
    svg += [
        f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="18" fill="#eef2ff" stroke="#c7d2fe"/>',
        text(bx + 28, by + 42, "Qué hay que demostrar", 24, "#312e81", "700"),
        text(bx + 35, by + 92, "A1", 24, "#1d4ed8", "700"),
        text(bx + 105, by + 92, "∀ n ≥ 150:  Jₙ(Tₙ) ≤ qₙ", 22, "#172033", "600"),
        text(bx + 515, by + 92, "⇒", 28, "#6366f1", "700"),
        text(bx + 575, by + 92, "λₙ ≥ 0 para todo n", 22, "#172033", "600"),
        text(bx + 885, by + 92, "⇒ RH", 24, "#312e81", "700"),
        text(bx + 35, by + 148, "Deep", 24, "#15803d", "700"),
        text(bx + 120, by + 148, "Ωₓ → 0", 22, "#172033", "600"),
        text(bx + 300, by + 148, "⇔", 28, "#6366f1", "700"),
        text(bx + 365, by + 148, "ningún factor de Blaschke interior", 22, "#172033", "600"),
        text(bx + 790, by + 148, "⇔ RH", 24, "#312e81", "700"),
        text(bx + 35, by + 195, "Azul/naranja = diagnóstico o modelo explícito. Ninguna continuación desconocida se dibuja como dato.", 16, "#4b5563"),
    ]
    svg.append("</svg>")

    ASSETS.mkdir(parents=True, exist_ok=True)
    svg_path = ASSETS / "a1_and_deep_limit.svg"
    svg_path.write_text("\n".join(svg), encoding="utf-8")

    csv_path = ASSETS / "a1_and_deep_limit_data.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["kind", "x", "y"])
        for xv, yv in zip(u[::20], cumulative[::20]):
            writer.writerow(["A1_visible_n150", f"{xv:.12g}", f"{yv:.12g}"])
        for xv, yv in zip(deep_x, deep_y):
            writer.writerow(["deep_offline_R_201_200", int(xv), f"{yv:.12g}"])

    metadata = {
        "A_150": a_value,
        "L_150_1_log2": boundary,
        "q_150": reserve,
        "T_150": cutoff,
        "J_visible_min": float(cumulative.min()),
        "J_visible_max": float(cumulative.max()),
        "J_visible_end": float(cumulative[-1]),
        "deep_last": float(deep_y[-1]),
    }
    return svg_path, metadata


def main() -> None:
    path, metadata = generate_svg()
    print(path)
    for key, value in metadata.items():
        print(f"{key}={value:.12g}")


if __name__ == "__main__":
    main()
