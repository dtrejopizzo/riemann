#!/usr/bin/env python3
"""Generate an intuitive prime -> A1 -> zero pipeline visualization."""

from __future__ import annotations

import html
import math
from pathlib import Path

import numpy as np


PHASE = Path(__file__).resolve().parents[1]
ASSETS = PHASE / "assets"


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


def mangoldt_and_psi(limit: int) -> tuple[np.ndarray, np.ndarray]:
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            prime[p * p : limit + 1 : p] = False
    mangoldt = np.zeros(limit + 1, dtype=float)
    for p in np.flatnonzero(prime):
        power = int(p)
        weight = math.log(power)
        while power <= limit:
            mangoldt[power] = weight
            if power > limit // int(p):
                break
            power *= int(p)
    return mangoldt, np.cumsum(mangoldt)


def tx(x, y, value, size=18, color="#172033", weight="400", anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" '
        f'font-size="{size}" fill="{color}" font-weight="{weight}" '
        f'text-anchor="{anchor}">{html.escape(str(value))}</text>'
    )


def polyline(points, color, width=2.5, dash=None, opacity=1.0):
    coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<polyline points="{coords}" fill="none" stroke="{color}" '
        f'stroke-width="{width}" stroke-linecap="round" '
        f'stroke-linejoin="round" opacity="{opacity}"{extra}/>'
    )


def panel(svg, x, y, w, h, title, subtitle):
    svg += [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#ffffff" stroke="#d7dce5"/>',
        tx(x + 25, y + 38, title, 23, "#111827", "700"),
        tx(x + 25, y + 66, subtitle, 16, "#4b5563"),
    ]


def generate() -> Path:
    mangoldt, psi = mangoldt_and_psi(5000)
    width, height = 1800, 1200
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="1800" height="1200" fill="#f7f8fb"/>',
        tx(70, 58, "Qué significa A1: de los primos a la línea crítica", 34, "#111827", "700"),
        tx(70, 94, "La misma señal se puede leer como saltos de primos, ondas de ceros o coeficientes de Li.", 20, "#4b5563"),
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#6366f1"/></marker></defs>',
    ]

    # Panel 1: prime staircase.
    p1 = (60, 135, 800, 405)
    panel(svg, *p1, "1 · Los primos construyen una escalera", "ψ(x) salta en cada potencia prima; x es la referencia lisa.")
    x0, y0, w, h = p1[0] + 70, p1[1] + 95, p1[2] - 105, p1[3] - 150
    mx = lambda value: x0 + (value - 1.0) / 99.0 * w
    my = lambda value: y0 + h - value / 105.0 * h
    svg += [
        f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="#64748b"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="#64748b"/>',
        polyline([(mx(1), my(1)), (mx(100), my(100))], "#dc2626", 2.5, "7 6"),
    ]
    step = []
    for integer in range(1, 101):
        value = float(psi[integer])
        if integer == 1:
            step.append((mx(integer), my(value)))
        else:
            step.append((mx(integer), my(float(psi[integer - 1]))))
            step.append((mx(integer), my(value)))
    svg.append(polyline(step, "#2563eb", 3.0))
    for power in np.flatnonzero(mangoldt[:101] > 0):
        svg.append(f'<circle cx="{mx(float(power)):.2f}" cy="{my(float(psi[power])):.2f}" r="2.4" fill="#2563eb"/>')
    for tick in (1, 20, 40, 60, 80, 100):
        svg += [
            f'<line x1="{mx(tick):.2f}" y1="{y0+h}" x2="{mx(tick):.2f}" y2="{y0+h+6}" stroke="#64748b"/>',
            tx(mx(tick), y0 + h + 25, tick, 13, "#64748b", anchor="middle"),
        ]
    svg += [
        tx(x0 + w - 6, my(100) + 19, "x", 16, "#b91c1c", "700", "end"),
        tx(x0 + w - 6, my(float(psi[100])) - 9, "ψ(x)", 16, "#1d4ed8", "700", "end"),
        tx(p1[0] + 25, p1[1] + p1[3] - 20, "La diferencia vertical E(x)=ψ(x)-x es la señal que A1 debe cancelar.", 17, "#374151", "600"),
    ]

    # Panel 2: log-scale filter and signed product.
    p2 = (900, 135, 840, 405)
    panel(svg, *p2, "2 · A1 pasa esa señal por un filtro oscilante", "Ejemplo n=20 para que los lóbulos sean visibles; la operación es la misma para n≥150.")
    u = np.linspace(math.log(2.0), math.log(5000.0), 1800)
    x = np.exp(u)
    index = np.floor(x).astype(int)
    error_ratio = psi[index] / x - 1.0
    filt = laguerre(19, 2.0, u)
    filt_scaled = filt / max(1e-15, float(np.max(np.abs(filt))))
    product = error_ratio * filt
    product_scaled = product / max(1e-15, float(np.max(np.abs(product))))
    x0, y0, w, h = p2[0] + 70, p2[1] + 98, p2[2] - 105, p2[3] - 155
    mx2 = lambda value: x0 + (value - u[0]) / (u[-1] - u[0]) * w
    lanes = [y0 + 35, y0 + 105, y0 + 180]
    for lane in lanes:
        svg.append(f'<line x1="{x0}" y1="{lane}" x2="{x0+w}" y2="{lane}" stroke="#cbd5e1"/>')
    error_scale = max(1e-15, float(np.max(np.abs(error_ratio))))
    error_points = [(mx2(float(a)), lanes[0] - 28 * float(b) / error_scale) for a, b in zip(u[::3], error_ratio[::3])]
    filter_points = [(mx2(float(a)), lanes[1] - 28 * float(b)) for a, b in zip(u[::3], filt_scaled[::3])]
    product_points = [(mx2(float(a)), lanes[2] - 31 * float(b)) for a, b in zip(u[::3], product_scaled[::3])]
    svg += [
        polyline(error_points, "#2563eb", 2.0),
        polyline(filter_points, "#7c3aed", 2.0),
        polyline(product_points, "#111827", 2.0),
        tx(x0 + 4, lanes[0] - 38, "señal: ψ(x)/x − 1", 14, "#1d4ed8", "600"),
        tx(x0 + 4, lanes[1] - 38, "filtro: Laguerre", 14, "#6d28d9", "600"),
        tx(x0 + 4, lanes[2] - 40, "producto: áreas + y −", 14, "#111827", "600"),
    ]
    # Signed area bars in product lane.
    baseline = lanes[2]
    for a, b, c in zip(u[:-1:8], u[1::8], product_scaled[:-1:8]):
        left, right = mx2(float(a)), mx2(float(b))
        top = baseline - 31 * float(c)
        color = "#22c55e" if c >= 0 else "#ef4444"
        svg.append(f'<rect x="{left:.2f}" y="{min(top, baseline):.2f}" width="{max(0.5,right-left):.2f}" height="{abs(top-baseline):.2f}" fill="{color}" opacity="0.32"/>')
    svg += [
        tx(p2[0] + 25, p2[1] + p2[3] - 38, "J_n(T) = área verde − área roja.  A1 exige: J_n(T_n) ≤ q_n.", 17, "#374151", "700"),
        tx(p2[0] + 25, p2[1] + p2[3] - 14, "No se acotan tamaños separados: hay que conservar la cancelación de los lóbulos.", 15, "#4b5563"),
    ]

    # Arrow between prime and filter panels.
    svg.append('<line x1="855" y1="335" x2="892" y2="335" stroke="#6366f1" stroke-width="4" marker-end="url(#arrow)"/>')

    # Panel 3: zeros.
    p3 = (60, 585, 800, 405)
    panel(svg, *p3, "3 · Los ceros son las frecuencias escondidas", "La fórmula explícita descompone ψ(x)−x en ondas, una por cada cero ρ=β+iγ.")
    x0, y0, w, h = p3[0] + 105, p3[1] + 95, 340, p3[3] - 205
    ms = lambda beta: x0 + (beta - 0.30) / 0.40 * w
    mg = lambda gamma: y0 + h - (gamma - 12.0) / 24.0 * h
    svg += [
        f'<rect x="{ms(0.5):.2f}" y="{y0}" width="2" height="{h}" fill="#16a34a"/>',
        f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="#64748b"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="#64748b"/>',
        tx(ms(0.5) + 10, y0 + 22, "línea crítica β=1/2", 15, "#15803d", "700"),
    ]
    known = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351]
    for gamma in known:
        svg.append(f'<circle cx="{ms(0.5):.2f}" cy="{mg(gamma):.2f}" r="6" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>')
    for beta in (0.38, 0.62):
        svg.append(f'<circle cx="{ms(beta):.2f}" cy="{mg(24):.2f}" r="8" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>')
    svg += [
        f'<line x1="{ms(0.38):.2f}" y1="{mg(24):.2f}" x2="{ms(0.62):.2f}" y2="{mg(24):.2f}" stroke="#dc2626" stroke-dasharray="6 5"/>',
        tx(ms(0.62) + 14, mg(24) + 5, "cero hipotético", 15, "#b91c1c", "700"),
        tx(x0 + w / 2, y0 + h + 34, "β = Re ρ", 15, "#475569", anchor="middle"),
        tx(p3[0] + 485, p3[1] + 130, "Cada cero aporta aproximadamente", 16, "#374151", "600"),
        tx(p3[0] + 485, p3[1] + 165, "e^(βu) · cos(γu + fase)", 21, "#111827", "700"),
        tx(p3[0] + 485, p3[1] + 210, "γ = frecuencia", 17, "#1d4ed8", "600"),
        tx(p3[0] + 485, p3[1] + 242, "β = envolvente", 17, "#b91c1c", "600"),
        tx(p3[0] + 485, p3[1] + 292, "Si β>1/2, esa onda gana", 17, "#b91c1c", "700"),
        tx(p3[0] + 485, p3[1] + 318, "un factor e^((β−1/2)u)", 17, "#b91c1c", "700"),
        tx(p3[0] + 25, p3[1] + p3[3] - 18, "Los puntos azules conocidos están en 1/2; la prueba debe excluir todo punto rojo, a cualquier altura.", 16, "#374151", "600"),
    ]

    # Panel 4: Li modes.
    p4 = (900, 585, 840, 405)
    panel(svg, *p4, "4 · El filtro convierte un cero exterior en excursiones", "Modo de un cuarteto: on-line queda acotado; off-line crece exponencialmente.")
    ns = np.arange(1, 121, dtype=float)
    theta, radial = 0.70, 0.035
    online = 4.0 - 4.0 * np.cos(ns * theta)
    offline = 4.0 - 4.0 * np.cosh(ns * radial) * np.cos(ns * theta)
    x0, y0, w, h = p4[0] + 75, p4[1] + 98, p4[2] - 110, p4[3] - 205
    mx4 = lambda value: x0 + (value - 1.0) / 119.0 * w
    my4 = lambda value: y0 + h - (value + 150.0) / 300.0 * h
    svg += [
        f'<rect x="{x0}" y="{my4(8):.2f}" width="{w}" height="{my4(0)-my4(8):.2f}" fill="#dcfce7"/>',
        f'<line x1="{x0}" y1="{my4(0):.2f}" x2="{x0+w}" y2="{my4(0):.2f}" stroke="#64748b"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="#64748b"/>',
        polyline([(mx4(float(a)), my4(float(b))) for a, b in zip(ns, online)], "#2563eb", 2.5),
        polyline([(mx4(float(a)), my4(float(b))) for a, b in zip(ns, offline)], "#dc2626", 2.2),
        tx(x0 + 12, my4(8) - 8, "on-line: siempre entre 0 y 8", 15, "#1d4ed8", "700"),
        tx(x0 + w - 8, y0 + 22, "off-line: ±exp(c n)", 15, "#b91c1c", "700", "end"),
    ]
    for n_tick in (1, 30, 60, 90, 120):
        svg += [
            f'<line x1="{mx4(n_tick):.2f}" y1="{y0+h}" x2="{mx4(n_tick):.2f}" y2="{y0+h+6}" stroke="#64748b"/>',
            tx(mx4(n_tick), y0 + h + 25, n_tick, 13, "#64748b", anchor="middle"),
        ]
    for val in (-100, 0, 100):
        svg += [
            f'<line x1="{x0-6}" y1="{my4(val):.2f}" x2="{x0}" y2="{my4(val):.2f}" stroke="#64748b"/>',
            tx(x0 - 10, my4(val) + 5, val, 13, "#64748b", anchor="end"),
        ]
    svg += [
        tx(x0 + w / 2, y0 + h + 50, "grado n", 15, "#475569", anchor="middle"),
        tx(p4[0] + 25, p4[1] + p4[3] - 17, "Un solo cero rojo terminaría dominando A_n ~ (n/2) log n y forzaría λ_n<0 repetidamente.", 16, "#374151", "600"),
    ]
    svg.append('<line x1="855" y1="785" x2="892" y2="785" stroke="#6366f1" stroke-width="4" marker-end="url(#arrow)"/>')

    # Bottom conclusion.
    bx, by, bw, bh = 60, 1030, 1680, 125
    svg += [
        f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="18" fill="#eef2ff" stroke="#c7d2fe"/>',
        tx(bx + 28, by + 38, "Lo que realmente debemos demostrar", 23, "#312e81", "700"),
        tx(bx + 28, by + 76, "Para los pesos reales Λ(m), todas las áreas firmadas del panel 2 deben satisfacer J_n(T_n) ≤ q_n.", 19, "#172033", "600"),
        tx(bx + 28, by + 105, "Equivalente: demostrar que no existe ningún cero rojo (β>1/2), ni siquiera a una altura jamás calculada.", 19, "#b91c1c", "700"),
    ]
    svg.append("</svg>")

    ASSETS.mkdir(parents=True, exist_ok=True)
    output = ASSETS / "prime_zero_a1_pipeline.svg"
    output.write_text("\n".join(svg), encoding="utf-8")
    return output


def main() -> None:
    print(generate())


if __name__ == "__main__":
    main()
