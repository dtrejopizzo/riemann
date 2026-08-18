"""Double-precision complex zeta / xi tools (numpy only).

Provides
    zeta_and_dzeta(s)   Riemann zeta and its derivative (vectorised)
    digamma(z)          complex digamma (vectorised)
    xi_logderiv(s)      xi'(s)/xi(s)
    li_lambda(nmax,r,M) Li coefficients lambda_1..lambda_nmax by Cauchy integral

The Li generating identity used is

    sum_{n>=1} lambda_n z^{n-1} = (d/dz) log xi(1/(1-z))
                                = (xi'/xi)(1/(1-z)) / (1-z)^2 .

It holds with the zeros paired rho <-> 1-rho, which is exactly the standard
symmetric summation in Li's criterion: z_{1-rho} = 1/z_rho.  The statement
that every transformed singularity lies on |z| = 1 is equivalent to RH and
must not be assumed here.  The Cauchy extraction at a chosen radius r is
valid only after certifying that |1-1/rho|>r for every nontrivial zero rho.
For r=0.995 this finite-radius condition can only fail at an off-line zero
with |Im rho|<1/sqrt(1-r^2)=10.0125..., but this module does not itself
provide that zero-free certification.  The output is therefore diagnostic
unless that separate finite verification is supplied.

Validation: lambda_8 = 1.46575567714706..., agreeing to 13 digits with the
certified rational interval of phase-102 `217_N8_BASE_MARGIN_CERTIFICATE.md`.
"""

import numpy as np

# ---------------------------------------------------------------- Borwein eta


def _borwein_d(N):
    d = np.zeros(N + 1, dtype=float)
    c = 0.0
    tot = 0.0
    for i in range(N + 1):
        if i == 0:
            c = 1.0 / N                      # (N-1)!/N!
        else:
            c *= 4.0 * (N + i - 1) * (N - i + 1) / ((2.0 * i) * (2.0 * i - 1.0))
        tot += c
        d[i] = N * tot
    return d


_NB = 42
_D = _borwein_d(_NB)
_W = np.array([((-1.0) ** k) * (_D[k] - _D[_NB]) for k in range(_NB)])
_LOGB = np.log(np.arange(1, _NB + 1, dtype=float))


def zeta_and_dzeta(s):
    """Vectorised zeta(s), zeta'(s) for Re(s) > 0, s != 1."""
    s = np.asarray(s, dtype=complex)
    # eta(s) = -(1/d_N) sum_k w_k (k+1)^{-s}
    e = np.exp(-np.multiply.outer(s, _LOGB))          # (..., NB)
    eta = -(e * _W).sum(axis=-1) / _D[_NB]
    deta = -(e * _W * (-_LOGB)).sum(axis=-1) / _D[_NB]
    p = np.exp((1.0 - s) * np.log(2.0))
    dp = -np.log(2.0) * p
    den = 1.0 - p
    return eta / den, (deta * den + eta * dp) / (den * den)


# ---------------------------------------------------------------- digamma

_B2 = np.array([1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510])


def digamma(z):
    z = np.asarray(z, dtype=complex).copy()
    acc = np.zeros_like(z)
    for _ in range(200):
        m = np.abs(z) < 24.0
        if not m.any():
            break
        acc[m] -= 1.0 / z[m]
        z[m] += 1.0
    out = np.log(z) - 0.5 / z
    zz = z * z
    p = zz.copy()
    for k, b in enumerate(_B2, start=1):
        out -= b / (2.0 * k * p)
        p = p * zz
    return acc + out


# ---------------------------------------------------------------- xi


def xi_logderiv(s):
    s = np.asarray(s, dtype=complex)
    z, dz = zeta_and_dzeta(s)
    return (1.0 / s + 1.0 / (s - 1.0) - 0.5 * np.log(np.pi)
            + 0.5 * digamma(s / 2.0) + dz / z)


def li_lambda(nmax, r=0.99, M=None):
    """Diagnostic Cauchy extraction on |z|=r; requires a certified zero-free
    transformed disk |1-1/rho|>r to equal the Li Taylor coefficients."""
    if M is None:
        M = 1 << int(np.ceil(np.log2(max(4096, 400 / (1.0 - r)))))
    th = 2.0 * np.pi * np.arange(M) / M
    z = r * np.exp(1j * th)
    s = 1.0 / (1.0 - z)
    h = xi_logderiv(s) / (1.0 - z) ** 2
    # lambda_n = (1/M) sum_j h_j z_j^{-(n-1)} ; use one FFT
    c = np.fft.fft(h) / M                  # c[k] = (1/M) sum_j h_j e^{-2pi i jk/M}
    n = np.arange(1, nmax + 1)
    return (c[(n - 1) % M] / r ** (n - 1)).real


if __name__ == "__main__":
    for r, M in ((0.90, 8192), (0.97, 32768), (0.995, 262144)):
        lam = li_lambda(10, r=r, M=M)
        print(f"r={r}: lambda_1={lam[0]:.15f}  lambda_8={lam[7]:.15f}")
    print("certified lambda_8 in [1.465755677147060632655514, ...515]")
