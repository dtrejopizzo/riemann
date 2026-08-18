#!/usr/bin/env python3
"""Directed full Gamma matrix from D.146 using python-flint.

Run with:
  PYTHONPATH=/tmp/d61-flint D147_N=170 D147_DPS=750 python3 this_file.py

The public function exact_gamma_block returns the matrix of
Re psi(1/4+i tau/2)-psi(1/4) on the first N normalized Legendre modes.
It does not subtract m0 or the finite contacts.
"""

from __future__ import annotations

import math
import os

from flint import arb, arb_mat, ctx


def endpoint_derivative(n: int, r: int) -> int:
    if r > n:
        return 0
    return math.factorial(n + r) // (
        2**r * math.factorial(r) * math.factorial(n - r)
    )


def lerch_positive(z: arb, s: int, a: arb, digits: int) -> arb:
    """Enclose Phi(z,s,a) for 0<z<1, s>=2, a>0."""
    # z=1/25 in the target application.  This choice leaves at least
    # 25 decimal guard digits in the geometric tail.
    terms = max(20, math.ceil((digits + 25) / math.log10(25)))
    total = arb(0)
    zj = arb(1)
    for j in range(terms):
        total += zj / (arb(j) + a) ** s
        zj *= z
    tail = zj / ((arb(terms) + a) ** s * (1 - z))
    # The true tail is positive and no larger than tail.  A symmetric
    # error is slightly wider but remains a rigorous enclosure.
    return total + arb(0, tail.upper())


def scalar_sequences(N: int, T: arb, digits: int) -> tuple[list[arb], list[arb]]:
    quarter = arb(1) / 4
    z = (-4 * T).exp()
    pref = (-T).exp()
    S = [arb(0) for _ in range(2 * N + 1)]
    X = [arb(0) for _ in range(2 * N + 1)]
    for r in range(2, 2 * N + 1):
        scale = (2 * T) ** (-r)
        S[r] = scale * arb(r).zeta(quarter)
        X[r] = pref * scale * lerch_positive(z, r, quarter, digits)
    return S, X


def endpoint_matrices(N: int) -> tuple[arb_mat, arb_mat, arb_mat]:
    bminus = arb_mat(N, N)
    bplus = arb_mat(N, N)
    qendpoint = arb_mat(N, N)
    for n in range(N):
        row_sign = -1 if n % 2 else 1
        for r in range(n + 1):
            value = endpoint_derivative(n, r)
            bplus[n, r] = value
            bminus[n, r] = (-1 if (n + r) % 2 else 1) * value
            # coefficient of x^(r+1) in Q_n(-1):
            # (-1)^r P_n^(r)(-1)=(-1)^n P_n^(r)(1).
            qendpoint[n, r] = row_sign * value
    return bminus, bplus, qendpoint


def derivative_resolvent_matrix(N: int, S: list[arb]) -> arb_mat:
    """Return L=2W sum_{r>=1} (-1)^r S[r+1] D^r."""
    L = arb_mat(N, N)
    for n in range(N):
        # v is the coefficient vector of D^r P_n in the Legendre basis.
        v = [0] * N
        v[n] = 1
        for r in range(1, n + 1):
            dv = [0] * N
            suffix = [0, 0]
            for j in range(n, -1, -1):
                # P_l'=sum_{j<l, l-j odd}(2j+1)P_j.  The two suffix
                # registers therefore contain precisely the coefficients
                # of v with each parity and index strictly larger than j.
                dv[j] = (2 * j + 1) * suffix[1 - j % 2]
                suffix[j % 2] += v[j]
            v = dv
            coefficient = S[r + 1] if r % 2 == 0 else -S[r + 1]
            for m in range(n - r + 1):
                if v[m]:
                    L[m, n] += arb(2 * v[m]) * coefficient / (2 * m + 1)
    return L


def exact_gamma_block(N: int, digits: int = 250, T: arb | None = None) -> arb_mat:
    ctx.dps = digits
    if T is None:
        T = arb(5).log() / 2
    Sseq, Xseq = scalar_sequences(N, T, digits)
    bminus, bplus, qendpoint = endpoint_matrices(N)

    HS = arb_mat(N, N)
    HX = arb_mat(N, N)
    for r in range(N):
        for s in range(N):
            HS[r, s] = Sseq[r + s + 2]
            HX[r, s] = Xseq[r + s + 2]

    boundary = (
        bminus * HS * qendpoint.transpose()
        - bplus * HX * qendpoint.transpose()
    )
    L = derivative_resolvent_matrix(N, Sseq)
    raw = -L - L.transpose() + boundary + boundary.transpose()

    answer = arb_mat(N, N)
    roots = [arb(2 * n + 1).sqrt() for n in range(N)]
    for m in range(N):
        for n in range(N):
            answer[m, n] = T * roots[m] * roots[n] * raw[m, n] / 2
    return answer


def main() -> None:
    N = int(os.environ.get("D147_N", "12"))
    digits = int(os.environ.get("D147_DPS", "160"))
    gamma = exact_gamma_block(N, digits)

    # Symmetry and positivity of every diagonal entry are mandatory
    # sanity checks for the positive Gamma difference form.
    for m in range(N):
        assert gamma[m, m] > 0
        for n in range(N):
            assert gamma[m, n].overlaps(gamma[n, m])

    print("D147 directed Hurwitz--Lerch Gamma block: PASS")
    print("N,digits =", N, digits)
    print("diagonal endpoints =", gamma[0, 0], gamma[N - 1, N - 1])


if __name__ == "__main__":
    main()
