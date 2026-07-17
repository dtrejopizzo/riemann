#!/usr/bin/env python3
import cmath
import math


def packet(t, L):
    if abs(t) > L:
        return 0.0
    y = abs(t)
    return (1 - y / L) * (1 + 0.3 * math.cos(2.0 * y) + 0.15 * math.sin(3.0 * y))


def F(w, L, n_grid=6000):
    h = 2 * L / n_grid
    total = 0j
    for k in range(n_grid):
        t = -L + (k + 0.5) * h
        total += cmath.exp(w * t) * packet(t, L) * h
    return total


def I_wall(c, T, u, L, n_grid=8000):
    h = 2 * T / n_grid
    total = 0j
    for k in range(n_grid):
        t = -T + (k + 0.5) * h
        total += F(c + 1j * t, L) * cmath.exp(-1j * t * u) * h
    return total / (2 * math.pi)


def run():
    print("E72.377 wall Paley inversion probe")
    print(" L    c     T      u        wallCoeff         target            relErr")
    cases = [
        (4.0, 0.8, 40.0, 0.7),
        (4.0, 0.8, 60.0, 2.2),
        (5.0, 1.1, 60.0, 1.5),
        (5.0, 1.1, 80.0, 4.2),
    ]
    for L, c, T, u in cases:
        coeff = I_wall(c, T, u, L)
        target = math.exp(c * u) * packet(u, L)
        rel = abs(coeff - target) / max(1.0, abs(coeff), abs(target))
        print(f"{L:3.1f} {c:4.1f} {T:6.1f} {u:6.2f} {coeff:18.8e} {target:18.8e} {rel:10.3e}")


if __name__ == "__main__":
    run()
