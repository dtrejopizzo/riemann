#!/usr/bin/env python3
import cmath


def pair_bracket(z, w, L):
    ez = cmath.exp(z * L)
    ew_inv = cmath.exp(-w * L)
    return w * (1 + ez) * (1 - ew_inv) + z * (1 - ez) * (1 + ew_inv)


def hyper_bracket(z, w, L):
    a = L / 2
    return 4 * cmath.exp(a * (z - w)) * (
        w * cmath.cosh(a * z) * cmath.sinh(a * w)
        - z * cmath.sinh(a * z) * cmath.cosh(a * w)
    )


def T(a, u):
    return u * cmath.sinh(a * u)


def D(a, z, w):
    den = w * w - z * z
    num = cmath.cosh(a * z) * T(a, w) - T(a, z) * cmath.cosh(a * w)
    return num / den


def removable_limit(a, z):
    # d/dv [C(z)T(v)-T(z)C(v)] at v=z, divided by d/dv(v^2-z^2)=2z.
    C_z = cmath.cosh(a * z)
    T_z = T(a, z)
    T_prime = cmath.sinh(a * z) + a * z * cmath.cosh(a * z)
    C_prime = a * cmath.sinh(a * z)
    return (C_z * T_prime - T_z * C_prime) / (2 * z)


def fake_G(w, L):
    # Any function with G(-w)=e^(-wL)G(w) has the form e^(wL/2) times an even function.
    return cmath.exp(w * L / 2) * (1 + w * w)


def pair_kernel_from_D(z, w, L):
    a = L / 2
    return 4 * cmath.exp(a * (z - w)) * fake_G(w, L) * D(a, z, w)


def run():
    print("E72.372 hyperbolic pair-kernel probe")
    print(" L      z                  w                  relBracket      DnearErr    orientErr")
    cases = [
        (6.0, 0.25 + 1.4j, 0.33 + 2.1j),
        (8.0, -0.2 + 1.7j, 0.41 + 3.2j),
        (10.0, 0.15 + 2.3j, -0.37 + 1.9j),
        (12.0, 0.30 + 1.2j, 0.55 + 2.7j),
    ]
    for L, z, w in cases:
        b0 = pair_bracket(z, w, L)
        b1 = hyper_bracket(z, w, L)
        rel = abs(b0 - b1) / max(1.0, abs(b0), abs(b1))

        a = L / 2
        eps = 1e-5 * (1 + abs(z))
        d_near = D(a, z, z + eps)
        d_lim = removable_limit(a, z)
        derr = abs(d_near - d_lim) / max(1.0, abs(d_near), abs(d_lim))
        orient = abs(pair_kernel_from_D(z, w, L) - pair_kernel_from_D(z, -w, L))
        orient /= max(1.0, abs(pair_kernel_from_D(z, w, L)), abs(pair_kernel_from_D(z, -w, L)))

        print(f"{L:4.1f}  {z!s:18s} {w!s:18s} {rel:12.3e} {derr:12.3e} {orient:12.3e}")


if __name__ == "__main__":
    run()
