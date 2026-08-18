import math
from collections import defaultdict

import numpy as np


def von_mangoldt(N):
    lam = np.zeros(N + 1)
    sieve = np.ones(N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, N + 1):
        if not sieve[p]:
            continue
        q = p
        while q <= N:
            lam[q] = math.log(p)
            if q > N // p:
                break
            q *= p
        sieve[p * p : N + 1 : p] = False
    return lam


def divisors_up_to(N):
    divs = [[] for _ in range(N + 1)]
    for d in range(1, N + 1):
        for n in range(d, N + 1, d):
            divs[n].append(d)
    return divs


def lambda_powers(N, lam, divs):
    powers = []
    prev = np.zeros(N + 1)
    prev[1] = 1.0
    for _k in range(1, int(math.log(N, 2)) + 1):
        cur = np.zeros(N + 1)
        for n in range(2, N + 1):
            cur[n] = sum(prev[d] * lam[n // d] for d in divs[n])
        powers.append(cur)
        prev = cur
    return powers


def leakage_coefficients(N, lam, powers):
    out = []
    logN = math.log(N)
    for k, lk in enumerate(powers, start=1):
        coeff = defaultdict(float)
        for m in range(1, N + 1):
            xm = lk[m] / (math.sqrt(m) * logN**k)
            if xm == 0.0:
                continue
            for n in range(2, N + 1):
                if lam[n] == 0.0 or m % n == 0:
                    continue
                g = math.gcd(m, n)
                a, b = m // g, n // g
                coeff[(a, b)] += lam[n] * xm / math.sqrt(n)
        if coeff:
            out.append(coeff)
    return out


def gamma_multiplier(tau):
    z = 0.25 + 0.5j * tau
    correction = np.zeros_like(z, dtype=np.complex128)
    for _ in range(12):
        correction -= 1.0 / z
        z = z + 1.0
    inv = 1.0 / z
    inv2 = inv * inv
    psi = (
        np.log(z)
        - 0.5 * inv
        - inv2 / 12.0
        + inv2**2 / 120.0
        - inv2**3 / 252.0
        + inv2**4 / 240.0
        - 5.0 * inv2**5 / 660.0
        + correction
    )
    euler_gamma = 0.5772156649015328606
    psi_quarter = -euler_gamma - math.pi / 2.0 - 3.0 * math.log(2.0)
    return np.real(psi) - psi_quarter


def gamma_first_multiplier(tau):
    return 4.0 * tau * tau / (tau * tau + 0.25)


def gram_tate(L, R):
    return np.array(
        [[math.exp(R) - math.exp(L), R - L],
         [R - L, math.exp(-L) - math.exp(-R)]],
        dtype=float,
    )


def test_constant_profile(N, resolution=20, padding_factor=3.0):
    lam = von_mangoldt(N)
    divs = divisors_up_to(N)
    powers = lambda_powers(N, lam, divs)
    coeffs = leakage_coefficients(N, lam, powers)
    delta = 0.5 * math.log((N + 1) / N)
    L = -math.log(N)
    R = math.log(N / 2) + delta
    dt = delta / resolution
    pad = padding_factor * (R - L)
    grid_L = L - pad
    grid_R = R + pad
    size = int(math.ceil((grid_R - grid_L) / dt))
    fft_size = 1 << (size - 1).bit_length()
    t = grid_L + dt * np.arange(fft_size)
    tau = 2 * np.pi * np.fft.fftfreq(fft_size, d=dt)
    ggamma = gamma_multiplier(tau)
    Ginv = np.linalg.inv(gram_tate(L, R))
    total_l2 = 0.0
    total_gamma = 0.0
    total_tate = 0.0
    per_depth = []
    amp_cell = 1.0 / math.sqrt(delta)
    for k, coeff in enumerate(coeffs, start=1):
        f = np.zeros(fft_size, dtype=float)
        for (a, b), val in coeff.items():
            left = math.log(a / b)
            mask = (t >= left) & (t < left + delta)
            f[mask] += val * amp_cell
        l2 = float(np.sum(f * f) * dt)
        fhat = dt * np.fft.fft(f)
        gamma = float(np.sum(ggamma * np.abs(fhat) ** 2) / (fft_size * dt))
        mp = float(np.sum(np.exp(t / 2) * f) * dt)
        mm = float(np.sum(np.exp(-t / 2) * f) * dt)
        m = np.array([mp, mm])
        tate = float(m @ Ginv @ m)
        total_l2 += l2
        total_gamma += gamma
        total_tate += tate
        per_depth.append((k, l2, gamma, tate))
    return {
        "N": N,
        "delta": delta,
        "depths": len(coeffs),
        "l2": total_l2,
        "gamma": total_gamma,
        "tate": total_tate,
        "ratio": (total_gamma + total_tate) / total_l2 if total_l2 else math.inf,
        "per_depth": per_depth,
        "grid": fft_size,
    }


def test_piecewise_extremizer(N, bins=12, points_per_bin=4, padding_factor=1.0):
    lam = von_mangoldt(N)
    divs = divisors_up_to(N)
    powers = lambda_powers(N, lam, divs)
    coeffs = leakage_coefficients(N, lam, powers)
    delta = 0.5 * math.log((N + 1) / N)
    L = -math.log(N)
    R = math.log(N / 2) + delta
    dt = delta / (bins * points_per_bin)
    pad = padding_factor * (R - L)
    grid_L = L - pad
    grid_R = R + pad
    size = int(math.ceil((grid_R - grid_L) / dt))
    fft_size = 1 << (size - 1).bit_length()
    t = grid_L + dt * np.arange(fft_size)
    tau = 2 * np.pi * np.fft.fftfreq(fft_size, d=dt)
    ggamma = gamma_multiplier(tau)
    Ginv = np.linalg.inv(gram_tate(L, R))
    A = np.zeros((bins, bins), dtype=float)
    Qg = np.zeros((bins, bins), dtype=float)
    Qg0 = np.zeros((bins, bins), dtype=float)
    Qt = np.zeros((bins, bins), dtype=float)
    basis_amp = 1.0 / math.sqrt(delta / bins)
    for coeff in coeffs:
        B = np.zeros((fft_size, bins), dtype=float)
        for (a, b), val in coeff.items():
            left = math.log(a / b)
            start = int(round((left - grid_L) / dt))
            for j in range(bins):
                lo = start + j * points_per_bin
                hi = lo + points_per_bin
                if lo < 0 or hi > fft_size:
                    continue
                B[lo:hi, j] += val * basis_amp
        A += dt * (B.T @ B)
        F = dt * np.fft.fft(B, axis=0)
        Qg += np.real(F.conj().T @ (ggamma[:, None] * F)) / (fft_size * dt)
        Qg0 += np.real(F.conj().T @ (gamma_first_multiplier(tau)[:, None] * F)) / (fft_size * dt)
        mp = dt * (np.exp(t / 2) @ B)
        mm = dt * (np.exp(-t / 2) @ B)
        moments = np.vstack([mp, mm])
        Qt += moments.T @ Ginv @ moments
    A = (A + A.T) / 2
    Q = (Qg + Qg.T) / 2 + (Qt + Qt.T) / 2
    vals_a, vecs_a = np.linalg.eigh(A)
    keep = vals_a > max(vals_a[-1] * 1e-10, 1e-12)
    U = vecs_a[:, keep]
    s = vals_a[keep]
    Ainvhalf = U @ np.diag(1.0 / np.sqrt(s))
    reduced = Ainvhalf.T @ Q @ Ainvhalf
    ratios, vecs = np.linalg.eigh((reduced + reduced.T) / 2)
    reduced0 = Ainvhalf.T @ ((Qg0 + Qg0.T) / 2) @ Ainvhalf
    ratios0 = np.linalg.eigvalsh((reduced0 + reduced0.T) / 2)
    mean_zero = np.zeros((bins, bins - 1))
    for j in range(bins - 1):
        mean_zero[j, j] = 1.0
        mean_zero[-1, j] = -1.0
    Az = mean_zero.T @ A @ mean_zero
    Qz = mean_zero.T @ Q @ mean_zero
    za, zu = np.linalg.eigh((Az + Az.T) / 2)
    zkeep = za > max(za[-1] * 1e-10, 1e-12)
    zU = zu[:, zkeep]
    zs = za[zkeep]
    zAinvhalf = zU @ np.diag(1.0 / np.sqrt(zs))
    zred = zAinvhalf.T @ Qz @ zAinvhalf
    zratios = np.linalg.eigvalsh((zred + zred.T) / 2)
    dangerous = Ainvhalf @ vecs[:, 0]
    dangerous /= math.sqrt(float(dangerous @ A @ dangerous))
    # Diagnostic splitting into the constant input direction and its
    # Euclidean mean-zero complement.  Positivity of D=Q-A is equivalent to
    # positivity of the mean-zero block and of its scalar Schur complement.
    Dmat = (Q - A + (Q - A).T) / 2
    cvec = np.ones(bins) / math.sqrt(bins)
    seed = np.column_stack([cvec, np.eye(bins)[:, :-1]])
    ortho, _ = np.linalg.qr(seed)
    if float(ortho[:, 0] @ cvec) < 0:
        ortho[:, 0] *= -1
    dcc = float(ortho[:, 0] @ Dmat @ ortho[:, 0])
    dc0 = ortho[:, 1:].T @ Dmat @ ortho[:, 0]
    d00 = ortho[:, 1:].T @ Dmat @ ortho[:, 1:]
    d00 = (d00 + d00.T) / 2
    d00_eigs = np.linalg.eigvalsh(d00)
    schur = dcc - float(dc0 @ np.linalg.solve(d00, dc0))
    cross_fraction = float(dc0 @ np.linalg.solve(d00, dc0)) / dcc
    return {
        "N": N,
        "bins": bins,
        "ratio_min": float(ratios[0]),
        "ratio_max": float(ratios[-1]),
        "ratio0_min": float(ratios0[0]),
        "mean_zero_ratio_min": float(zratios[0]),
        "eig_A_min": float(s[0]),
        "eig_A_max": float(s[-1]),
        "dangerous": dangerous,
        "dangerous_gamma0": float(dangerous @ Qg0 @ dangerous),
        "dangerous_gamma": float(dangerous @ Qg @ dangerous),
        "dangerous_tate": float(dangerous @ Qt @ dangerous),
        "defect_constant": dcc,
        "defect_meanzero_min": float(d00_eigs[0]),
        "defect_schur": schur,
        "defect_cross_fraction": cross_fraction,
        "grid": fft_size,
    }


if __name__ == "__main__":
    for N in [3, 5, 10, 20, 40, 80, 120, 200, 320]:
        r = test_constant_profile(N)
        print(
            f"N={N:3d} delta={r['delta']:.6g} depths={r['depths']:2d} "
            f"L2={r['l2']:.6g} Gamma={r['gamma']:.6g} Tate={r['tate']:.6g} "
            f"ratio={r['ratio']:.6g} grid={r['grid']}"
        )
