#!/usr/bin/env python3
"""Build CCM entries themselves in multiprecision and resolve the low cascade."""

import mpmath as mp


EULER = mp.euler


def primes_upto(n):
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
        p += 1
    return [p for p in range(2, n + 1) if sieve[p]]


def q_value(m, n, L, y):
    if m == n:
        return 2 * (1 - y / L) * mp.cos(2 * mp.pi * n * y / L)
    return (
        mp.sin(2 * mp.pi * m * y / L)
        - mp.sin(2 * mp.pi * n * y / L)
    ) / (mp.pi * (n - m))


def q0_and_derivative(m, n, L):
    if m == n:
        return mp.mpf(2), -2 / L
    return mp.mpf(0), -2 / L


def entry(m, n, L, lam, include_arith=True, planted=None):
    q0, qp0 = q0_and_derivative(m, n, L)

    def q(y):
        return q_value(m, n, L, y)

    w02 = mp.quad(lambda y: q(y) * (mp.exp(y / 2) + mp.exp(-y / 2)), [0, L])

    def wr_integrand(y):
        if y == 0:
            return (qp0 + q0 / 2) / 2
        return (mp.exp(y / 2) * q(y) - q0) / (2 * mp.sinh(y))

    wra = mp.quad(wr_integrand, [0, L])
    wrb = q0 * mp.log(mp.tanh(L / 2)) / 2
    wr = (mp.log(4 * mp.pi) + EULER) * q0 / 2 + wra + wrb

    arith = mp.mpf(0)
    if include_arith:
        maxn = int(lam * lam)
        for p in primes_upto(maxn):
            lp = mp.log(p)
            pm = p
            exponent = 1
            while pm <= maxn:
                arith += lp * mp.power(pm, mp.mpf("-0.5")) * q(exponent * lp)
                pm *= p
                exponent += 1
    value = w02 - wr - arith
    if planted is not None:
        gamma0, beta, strength = (mp.mpf(x) for x in planted)
        spectral_point = gamma0 - 1j * beta
        qhat = mp.quad(lambda y: q(y) * mp.cos(spectral_point * y), [0, L])
        value += strength * 2 * mp.re(qhat)
    return value


def build_mp(lam_int, n_modes, dps, include_arith=True, planted=None):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    L = 2 * mp.log(lam)
    idx = list(range(-n_modes, n_modes + 1))
    H = mp.matrix(len(idx))
    for a, m in enumerate(idx):
        for b in range(a, len(idx)):
            value = entry(
                m,
                idx[b],
                L,
                lam,
                include_arith=include_arith,
                planted=planted,
            )
            H[a, b] = value
            H[b, a] = value
    return H, idx, L


def vec_norm(v):
    return mp.sqrt(sum(abs(v[j]) ** 2 for j in range(v.rows)))


def normalized_cauchy(gamma, idx, L, xi):
    d = [2 * mp.pi * n / L for n in idx]
    r = mp.matrix([1 / (gamma - dn) for dn in d])
    return abs((r.T * xi)[0]) / vec_norm(r)


def run_case(lam, n_modes, dps):
    H, idx, L = build_mp(lam, n_modes, dps)
    vals, vecs = mp.eigsy(H)
    xi = vecs[:, 0]
    residual = vec_norm(H * xi - vals[0] * xi)
    gamma = mp.mpf("14.134725141734693790")
    qcrit = normalized_cauchy(gamma, idx, L, xi)
    qnear = normalized_cauchy(gamma + mp.mpf("0.125"), idx, L, xi)
    print(f"dps={dps} lam={lam} N={n_modes} dim={len(idx)} L={mp.nstr(L, 10)}")
    print("lowest_eigenvalues", " ".join(mp.nstr(vals[j], 12) for j in range(min(6, vals.rows))))
    print("gap", mp.nstr(vals[1] - vals[0], 12))
    print("eig_residual", mp.nstr(residual, 8))
    print("q_gamma", mp.nstr(qcrit, 12))
    print("q_neighbor", mp.nstr(qnear, 12))
    return vals, qcrit, qnear


def run():
    print("P76.002 multiprecision CCM-entry audit")
    print("All integrals and matrix entries are rebuilt at the requested precision.")
    for n_modes in (3, 4, 5, 6):
        run_case(lam=6, n_modes=n_modes, dps=50)
    # Repeat the largest case at higher precision to distinguish convergence
    # from a working-precision floor.
    run_case(lam=6, n_modes=6, dps=80)


if __name__ == "__main__":
    run()
