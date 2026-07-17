#!/usr/bin/env python3
"""Verify and resolve the mixed Cauchy/CCM shell cocycle."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import transfer
from P76_035_safe_log_derivative_probe import transfer_prime


def norm2(v):
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def run():
    mp.mp.dps = 100
    max_modes = 10
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    z = mp.mpc(0, 1)
    print("P76.049 mixed shell cocycle at z=i, mu=0")
    print("N       |t0|       |corr|       |Tnew|      relId       |tau|    |Sinv*k|")
    for n_modes in range(5, 10):
        # Hbig is H_{N+1}; its inner principal block is H_N.
        off_big = max_modes - (n_modes + 1)
        Hbig = Hmax[off_big : Hmax.rows - off_big, off_big : Hmax.cols - off_big]
        idxbig = idxmax[off_big : len(idxmax) - off_big]
        Hn = Hbig[1:-1, 1:-1]
        idxn = idxbig[1:-1]

        # Reorder H_N as (A, shell) with shell (-N,+N).
        A = Hn[1:-1, 1:-1]
        Ainv = A ** -1
        U = mp.matrix(A.rows, 2)
        for j in range(A.rows):
            U[j, 0] = Hn[j + 1, 0]
            U[j, 1] = Hn[j + 1, Hn.cols - 1]
        C = mp.matrix([[Hn[0, 0], Hn[0, Hn.cols - 1]], [Hn[Hn.rows - 1, 0], Hn[Hn.rows - 1, Hn.cols - 1]]])
        Sigma = C - U.T * Ainv * U

        # Coupling from H_N to the new right node +(N+1).
        g_full = mp.matrix([Hbig[j + 1, Hbig.cols - 1] for j in range(Hbig.rows - 2)])
        gA = g_full[1:-1, :]
        ge = mp.matrix([g_full[0], g_full[g_full.rows - 1]])
        kappa = ge - U.T * Ainv * gA

        inner_nodes = [2 * mp.pi * k / L for k in idxn[1:-1]]
        shell_nodes = [2 * mp.pi * idxn[0] / L, 2 * mp.pi * idxn[-1] / L]
        dw = 2 * mp.pi * idxbig[-1] / L
        rA = mp.matrix([[1 / (z - d) for d in inner_nodes]])
        rAprime = mp.matrix([[-1 / (z - d) ** 2 for d in inner_nodes]])
        re = mp.matrix([[1 / (z - d) for d in shell_nodes]])
        reprime = mp.matrix([[-1 / (z - d) ** 2 for d in shell_nodes]])
        t0 = 1 / (z - dw) - (rA * Ainv * gA)[0]
        t0prime = -1 / (z - dw) ** 2 - (rAprime * Ainv * gA)[0]
        tau = re - rA * Ainv * U
        tauprime = reprime - rAprime * Ainv * U
        sinvk = Sigma ** -1 * kappa
        correction = (tau * sinvk)[0]
        generated = t0 - correction
        generated_prime = t0prime - (tauprime * sinvk)[0]

        direct_x = Hn ** -1 * g_full
        direct = transfer(z, idxbig[-1], idxn, direct_x, L)
        direct_prime = transfer_prime(z, idxbig[-1], idxn, direct_x, L)
        identity = max(abs(generated - direct), abs(generated_prime - direct_prime))
        scale = max(mp.mpf(1), abs(direct), abs(direct_prime))
        print(
            f"{n_modes:2d} {mp.nstr(abs(t0),8):>10} {mp.nstr(abs(correction),8):>12}"
            f" {mp.nstr(abs(direct),8):>12} {mp.nstr(identity/scale,5):>10}"
            f" {mp.nstr(norm2(tau.T),7):>11} {mp.nstr(norm2(sinvk),7):>12}"
        )


if __name__ == "__main__":
    run()
