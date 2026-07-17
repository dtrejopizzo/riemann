#!/usr/bin/env python3
import cmath


def T(a, u):
    return u * cmath.sinh(a * u)


def D(a, z, w):
    if abs(w * w - z * z) < 1e-8:
        h = 1e-6 * (1 + abs(w))
        return D(a, z, w + h)
    return (cmath.cosh(a * z) * T(a, w) - T(a, z) * cmath.cosh(a * w)) / (w * w - z * z)


def G(w, L):
    return cmath.exp(w * L / 2) * (1 + w * w)


def H(z, w, L):
    a = L / 2
    return 4 * cmath.exp(a * (z - w)) * D(a, z, w) * G(w, L)


def zlogder(w, zeros):
    return sum(1 / (w - r) for r in zeros)


def contour_integral(z, L, zeros, R=5.0, n_side=3000):
    # Counterclockwise rectangle with corners +-R +- iR.
    corners = [R - 1j * R, R + 1j * R, -R + 1j * R, -R - 1j * R, R - 1j * R]
    total = 0j
    for a0, a1 in zip(corners[:-1], corners[1:]):
        step = (a1 - a0) / n_side
        for k in range(n_side):
            w = a0 + (k + 0.5) * step
            total += H(z, w, L) * zlogder(w, zeros) * step
    return total / (4j * cmath.pi)


def run():
    print("E72.373 pair trace residue probe")
    print(" L      z                  pairSum             contour            relErr")
    pair_roots = [0.7 + 1.1j, 1.3 + 2.0j, 0.4 + 3.2j]
    zeros = []
    for w in pair_roots:
        zeros.extend([w, -w])
    for L, z in [(3.0, 0.2 + 0.6j), (4.0, -0.1 + 0.8j), (5.0, 0.3 + 0.4j)]:
        pair_sum = sum(H(z, w, L) for w in pair_roots)
        cont = contour_integral(z, L, zeros, R=5.0, n_side=2500)
        rel = abs(pair_sum - cont) / max(1.0, abs(pair_sum), abs(cont))
        print(f"{L:4.1f}  {z!s:18s} {pair_sum:18.8e} {cont:18.8e} {rel:10.3e}")


if __name__ == "__main__":
    run()
