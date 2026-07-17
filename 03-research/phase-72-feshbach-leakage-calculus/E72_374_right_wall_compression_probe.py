#!/usr/bin/env python3
import cmath


def Tfun(a, u):
    return u * cmath.sinh(a * u)


def D(a, z, w):
    den = w * w - z * z
    if abs(den) < 1e-9:
        h = 1e-6 * (1 + abs(w))
        return D(a, z, w + h)
    return (cmath.cosh(a * z) * Tfun(a, w) - Tfun(a, z) * cmath.cosh(a * w)) / den


def G(w, L):
    return cmath.exp(w * L / 2) * (1 + w * w)


def H(z, w, L):
    a = L / 2
    return 4 * cmath.exp(a * (z - w)) * D(a, z, w) * G(w, L)


def logder_even_divisor(w, roots):
    zeros = []
    for r in roots:
        zeros.extend([r, -r])
    return sum(1 / (w - r) for r in zeros)


def F(z, w, L, roots):
    return H(z, w, L) * logder_even_divisor(w, roots)


def integrate_segment(fn, a0, a1, n):
    step = (a1 - a0) / n
    total = 0j
    for k in range(n):
        total += fn(a0 + (k + 0.5) * step) * step
    return total


def run_case(L, z, c, height, roots, n=3000):
    fn = lambda w: F(z, w, L, roots)
    right = integrate_segment(fn, c - 1j * height, c + 1j * height, n)
    top = integrate_segment(fn, c + 1j * height, -c + 1j * height, n)
    left = integrate_segment(fn, -c + 1j * height, -c - 1j * height, n)
    bottom = integrate_segment(fn, -c - 1j * height, c - 1j * height, n)
    full = right + top + left + bottom
    compressed = 2 * right + top + bottom
    return full, compressed, right, top + bottom


def main():
    print("E72.374 right-wall compression probe")
    print(" L    c    T      relCompress     pairFull          pairCompressed")
    roots = [0.7 + 1.1j, 1.2 + 2.2j, 0.45 + 3.0j]
    cases = [
        (3.0, 0.2 + 0.6j, 1.8, 4.5),
        (4.0, -0.1 + 0.8j, 1.7, 4.8),
        (5.0, 0.3 + 0.4j, 2.0, 5.0),
    ]
    for L, z, c, height in cases:
        full, compressed, _, _ = run_case(L, z, c, height, roots)
        pair_full = full / (4j * cmath.pi)
        pair_compressed = compressed / (4j * cmath.pi)
        rel = abs(pair_full - pair_compressed) / max(1.0, abs(pair_full), abs(pair_compressed))
        print(
            f"{L:3.1f} {c:4.1f} {height:4.1f}   {rel:12.3e} "
            f"{pair_full:18.8e} {pair_compressed:18.8e}"
        )


if __name__ == "__main__":
    main()
