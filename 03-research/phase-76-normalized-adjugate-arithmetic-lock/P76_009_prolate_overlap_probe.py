#!/usr/bin/env python3
"""Compare resolved CCM ground lines with the zero-independent prolate model."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp


def h_riemann(x):
    x2 = x * x
    return (mp.pi / 2) * x2 * (2 * mp.pi * x2 - 3) * mp.exp(-mp.pi * x2)


def k_lambda_value(y, lam):
    u = mp.exp(y) / lam
    total = mp.mpf(0)
    n = 1
    while True:
        term = h_riemann(n * u)
        total += term
        n += 1
        if n * u > 7 and abs(term) < mp.mpf("1e-45"):
            break
        if n > 10000:
            raise RuntimeError("k_lambda sum did not converge")
    return mp.sqrt(u) * total


def coefficients(lam, nmax, L):
    out = {}
    for n in range(-nmax, nmax + 1):
        freq = 2 * mp.pi * n / L
        re = mp.quad(lambda y: k_lambda_value(y, lam) * mp.cos(freq * y), [0, L]) / L
        im = mp.quad(lambda y: -k_lambda_value(y, lam) * mp.sin(freq * y), [0, L]) / L
        out[n] = re + 1j * im
    return out


def normalized_overlap(a, b):
    na = mp.sqrt(sum(abs(x) ** 2 for x in a))
    nb = mp.sqrt(sum(abs(x) ** 2 for x in b))
    return abs(sum(mp.conj(x) * y for x, y in zip(a, b))) / (na * nb)


def run():
    mp.mp.dps = 50
    lam = mp.mpf(6)
    L = 2 * mp.log(lam)
    nmax = 8
    print("P76.009 prolate overlap probe")
    print("computing zero-independent k_lambda Fourier coefficients", flush=True)
    coeff = coefficients(lam, nmax, L)
    print("N          mu        overlap(k,xi0)   residual/gap       qxi          qk       qdiff")
    for n_modes in (3, 4, 5, 6, 7, 8):
        H, idx, _ = build_mp(6, n_modes, 50)
        vals, vecs = mp.eigsy(H)
        c = [coeff[n] for n in idx]
        ground = [vecs[j, 0] for j in range(vecs.rows)]
        overlap = normalized_overlap(c, ground)
        captured = mp.mpf(0)
        for mode in range(min(4, vecs.cols)):
            v = [vecs[j, mode] for j in range(vecs.rows)]
            captured += normalized_overlap(c, v) ** 2
        cv = mp.matrix(c)
        cv /= mp.sqrt((cv.T.conjugate() * cv)[0].real)
        rayleigh = (cv.T.conjugate() * H * cv)[0].real
        residual = mp.sqrt(sum(abs(z) ** 2 for z in H * cv - rayleigh * cv))
        gap = vals[1] - vals[0]
        xv = mp.matrix(ground)
        phase = (cv.T.conjugate() * xv)[0]
        if phase:
            xv *= mp.conj(phase) / abs(phase)
        gamma = mp.mpf("14.134725141734693790")
        r = mp.matrix([1 / (gamma - 2 * mp.pi * n / L) for n in idx])
        rnorm = mp.sqrt((r.T * r)[0])
        qxi = abs((r.T * xv)[0]) / rnorm
        qk = abs((r.T * cv)[0]) / rnorm
        qdiff = abs((r.T * (xv - cv))[0]) / rnorm
        print(
            f"{n_modes:2d} {mp.nstr(vals[0],9):>13}"
            f" {mp.nstr(overlap,10):>20} {mp.nstr(residual/gap,8):>15}"
            f" {mp.nstr(qxi,7):>12} {mp.nstr(qk,7):>12} {mp.nstr(qdiff,7):>12}"
        )


if __name__ == "__main__":
    run()
