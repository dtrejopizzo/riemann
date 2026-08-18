"""Part A.1-A.2: verify <A_T F,F> = sum_rho h(gamma_rho) numerically against
real zeta zeros, for several primitive F and T = 0.6, 1.2, 2.0, 3.0.

LHS is built independently of rowd_assembly.py / rowd_threshold.py (per
SPEC.md rules -- those two files are never imported here), using the
closed-form machinery in W5_closed_form.py:

    LHS = (1/pi) int_0^inf phi(tau) |Fhat(tau)|^2 dtau  -  2 sum_n w_n g(log n)

where phi(tau) = Re psi(1/4+i tau/2) - log(pi) = g_Gamma(tau) - m_0
(PROOF_ARCHITECTURE.md Sec.2, linchpin verified to 30 digits), and
g(a) = int F(t)F(t+a) dt is the exact autocorrelation.

RHS is built from mpmath zeta zeros cached by W5_cache_zeros.py:

    RHS = 2 * sum_{k>=1} |Fhat(gamma_k)|^2         (gamma_k > 0, rho & conj)

run:  python3 W5_identity_check.py
Needs W5_zeros_cache.json (run W5_cache_zeros.py first; this script will use
however many zeros are cached so far).
"""
import json
import math
import os
import time

import numpy as np
from scipy.integrate import quad

import W5_closed_form as W5

HERE = os.path.dirname(os.path.abspath(__file__))


def load_zeros():
    with open(os.path.join(HERE, "W5_zeros_cache.json")) as f:
        d = json.load(f)
    return np.array([float(g) for g in d["gammas"]]), d["dps"]


def primitive_test_functions(T, kmax=3, n_funcs=2):
    """Return list of (label, coeffs) with M_+ = M_- = 0 to numerical zero."""
    basis = W5.basis_coeffs(T, kmax=kmax)
    nb = len(basis)
    Mm = np.array([W5.real_moment_integral(b, T, -0.5) for b in basis])
    Mp = np.array([W5.real_moment_integral(b, T, +0.5) for b in basis])
    Mt = np.vstack([Mm, Mp])
    u, s, vt = np.linalg.svd(Mt)
    null_dim = nb - np.sum(s > 1e-10 * s.max())
    funcs = []
    for i in range(min(n_funcs, null_dim)):
        v = vt[-(i + 1)]
        coeffs = sum(v[j] * basis[j] for j in range(nb))
        funcs.append((f"null_vec_{i}", coeffs, v))
    return funcs, Mm, Mp


def lhs_closed_form(coeffs, T, quad_limit=400, tau_cutoff=None):
    def integrand(tau):
        phi = W5.phi_gamma(tau)
        z = W5.fourier_moment_integral(coeffs, T, np.array([tau]))[0]
        return phi * (abs(z) ** 2)

    if tau_cutoff is None:
        # C^2 bump: |Fhat|^2 ~ tau^-8; pick a cutoff where the tail is << 1e-12
        tau_cutoff = 4000.0
    gamma_part, gam_err = quad(integrand, 0, tau_cutoff, limit=quad_limit,
                                epsabs=1e-15, epsrel=1e-13)
    # tail estimate beyond cutoff: bound integrand by its value there decaying as tau^-8
    tail_val = abs(integrand(tau_cutoff)) * tau_cutoff / 7.0  # int_Y^inf C/tau^8 ~ C/(7 Y^7) vs C at Y: rough
    gamma_term = gamma_part / math.pi

    prime_terms = W5.prime_power_terms(T)
    prime_sum = 0.0
    contacts = []
    for n, w in prime_terms:
        g = W5.autocorr(coeffs, T, math.log(n))
        prime_sum += w * g
        contacts.append((n, w, g))

    lhs = gamma_term - 2.0 * prime_sum
    return dict(lhs=lhs, gamma_term=gamma_term, prime_sum=prime_sum,
                quad_err=gam_err, tau_cutoff=tau_cutoff, contacts=contacts)


def rhs_from_zeros(coeffs, T, gammas):
    checkpoints = sorted(set(list(range(10, 51, 10)) + list(range(50, len(gammas) + 1, 50))
                              + [len(gammas)]))
    z = W5.fourier_moment_integral(coeffs, T, gammas)
    h = np.abs(z) ** 2
    cum = 2.0 * np.cumsum(h)
    partials = [(k, cum[k - 1]) for k in checkpoints if k <= len(gammas)]
    return partials, cum[-1] if len(cum) else 0.0


def main():
    gammas, dps = load_zeros()
    print(f"loaded {len(gammas)} cached zeta zeros (dps={dps}), "
          f"gamma range [{gammas[0]:.3f}, {gammas[-1]:.3f}]\n")

    for T in (0.6, 1.2, 2.0, 3.0):
        print("=" * 78)
        print(f"T = {T}")
        funcs, Mm, Mp = primitive_test_functions(T, kmax=3, n_funcs=2)
        for label, coeffs, v in funcs:
            mm = W5.real_moment_integral(coeffs, T, -0.5)
            mp_ = W5.real_moment_integral(coeffs, T, +0.5)
            nrm2 = W5.l2_norm_sq(coeffs, T)
            tv = W5.total_variation(coeffs, T)
            print(f"  -- F = {label}  (coeff vector {np.round(v,4)})")
            print(f"     M_- = {mm:.3e}   M_+ = {mp_:.3e}   ||F||^2 = {nrm2:.6f}   TV(F) = {tv:.6f}")

            t0 = time.time()
            L = lhs_closed_form(coeffs, T)
            t1 = time.time()
            print(f"     LHS = {L['lhs']:.12f}   (gamma_term={L['gamma_term']:.8f}, "
                  f"prime_sum(2x)={2*L['prime_sum']:.8f}, quad_err~{L['quad_err']:.2e}, "
                  f"{t1-t0:.2f}s)")
            print(f"     prime contacts n<e^(2T)={math.exp(2*T):.3f}: "
                  f"{[c[0] for c in L['contacts']]}")

            partials, rhs_full = rhs_from_zeros(coeffs, T, gammas)
            print(f"     RHS partial sums (k zeros -> sum):")
            for k, s in partials[-8:]:
                print(f"        k={k:5d}  sum={s:.12f}  diff_to_final={s-rhs_full:.3e}")
            diff = L['lhs'] - rhs_full
            reldiff = diff / abs(L['lhs']) if L['lhs'] != 0 else float('nan')
            print(f"     LHS - RHS({len(gammas)} zeros) = {diff:.3e}   relative = {reldiff:.3e}")
        print()


if __name__ == "__main__":
    main()
