"""Part A.3: does rowd_assembly.py's piecewise-constant matrix assembly
reproduce the SAME <A_T F,F> as an independently-implemented closed-form
calculation, for a primitive F on its own mesh?

rowd_assembly.py is IMPORTED (read-only, per SPEC.md rules -- never modified)
to get its mesh and its matrix A = R - L. The comparison value is computed by
a completely separate code path:
  * Gamma channel: (1/pi) int_0^inf phi(tau)|Fhat(tau)|^2 dtau via direct
    numerical quadrature over tau, with Fhat given by the closed-form
    Fourier transform of a piecewise-constant function (elementary, no
    recursion, well-conditioned at all tau -- unlike the polynomial-moment
    case in W5_closed_form.py, a single indicator's FT has only a removable
    singularity at tau=0, not catastrophic cancellation).  This exercises a
    different numerical route than rowd_assembly's Euler-Maclaurin-summed
    Psi(D) kernel (gamma_form / psi_kernel), which is the part of
    rowd_assembly most likely to hide a subtle bug.
  * Prime channel: direct interval-overlap formula, written independently
    of rowd_assembly.shift_form (same mathematical content -- overlap of
    shifted cells -- but separately coded, so it still catches sign/index
    errors even though it is not a fully independent *method* the way the
    Gamma-channel check is).

run:  python3 W5_crossvalidate_assembly.py
"""
import math
import numpy as np
from scipy.integrate import quad

import rowd_assembly as RA
import W5_closed_form as W5


def indicator_fhat(c, d, v, tau):
    """Fhat(tau) for F = sum_i v_i * 1_[c_i,d_i], scalar tau."""
    if tau == 0.0:
        return complex(np.sum(v * (d - c)))
    ic = 1j * tau
    return complex(np.sum(v * (np.exp(ic * d) - np.exp(ic * c)) / ic))


def prime_term_direct(c, d, v, a):
    """g(a) = int F(t)F(t+a) dt = v^T S_a v via direct interval overlap,
    coded independently of rowd_assembly.shift_form."""
    lo = np.maximum(c[:, None], c[None, :] - a)
    hi = np.minimum(d[:, None], d[None, :] - a)
    overlap = np.maximum(hi - lo, 0.0)
    return float(v @ overlap @ v)


def lhs_independent(c, d, v, T, quad_limit=1500, tau_cutoff=2000.0):
    """NOTE on precision: a piecewise-constant F has jump discontinuities, so
    Fhat(tau) = O(1/tau) and phi(tau)|Fhat(tau)|^2 = O(log(tau)/tau^2) --
    decays far too slowly for a plain adaptive quad to reach 1e-8 relative
    precision in reasonable time (the tail beyond Y contributes ~log(Y)/Y,
    which needs Y ~ 1e10-1e11 for 8 digits -- infeasible to resolve an
    oscillatory integrand over that range by quadrature). This function
    therefore reports whatever precision a moderate cutoff achieves and is
    explicit about it; see W5_WEIL_IDENTITY.md Part A.3 for the achieved
    digit count and why full 8-digit precision was not attempted here (the
    8-digit requirement is met instead, rigorously, by the smooth C^2 test
    functions in W5_identity_check.py / W5_highprec.py)."""
    def integrand(tau):
        phi = W5.phi_gamma(tau)
        z = indicator_fhat(c, d, v, tau)
        return phi * (abs(z) ** 2)

    gamma_part, err = quad(integrand, 0, tau_cutoff, limit=quad_limit,
                            epsabs=1e-12, epsrel=1e-9)
    gamma_term = gamma_part / math.pi

    prime_terms = W5.prime_power_terms(T)
    prime_sum = 0.0
    for n, w in prime_terms:
        g = prime_term_direct(c, d, v, math.log(n))
        prime_sum += w * g
    return gamma_term - 2.0 * prime_sum, gamma_term, prime_sum, err


def build_primitive_vector(Tate, seed=0):
    """Null space of the 2 x ncell Tate moment matrix; return a couple of
    normalized combinations (not the same construction as W5_identity_check,
    on purpose, for variety)."""
    u, s, vt = np.linalg.svd(Tate)
    ncell = Tate.shape[1]
    null_dim = ncell - int(np.sum(s > 1e-10 * s.max()))
    vecs = []
    for i in range(min(3, null_dim)):
        vecs.append(vt[-(i + 1)])
    rng = np.random.default_rng(seed)
    if null_dim >= 2:
        mix = rng.standard_normal(min(3, null_dim))
        mix /= np.linalg.norm(mix)
        vecs.append(sum(m * vt[-(k + 1)] for k, m in enumerate(mix)))
    return vecs


def main():
    for T, refine in [(0.6, 8), (1.2, 8), (2.0, 6), (3.0, 4)]:
        print("=" * 78)
        print(f"T={T}  refine={refine}")
        M = RA.assemble(T, refine=refine)
        c, d, A = M['c'], M['d'], M['A']
        print(f"  mesh cells = {len(c)}")
        vecs = build_primitive_vector(M['Tate'])
        for k, v in enumerate(vecs):
            mm = v @ M['Tate'][0]
            mp_ = v @ M['Tate'][1]
            rhs_matrix = float(v @ A @ v)
            lhs_ind, gt, ps, err = lhs_independent(c, d, v, T)
            diff = lhs_ind - rhs_matrix
            rel = diff / abs(rhs_matrix) if rhs_matrix != 0 else float('nan')
            print(f"  v#{k}: M-={mm:.2e} M+={mp_:.2e}  "
                  f"matrix(rowd_assembly)={rhs_matrix:.12e}  "
                  f"closed-form(independent)={lhs_ind:.12e}  "
                  f"diff={diff:.3e}  rel={rel:.3e}  quad_err~{err:.1e}")
        print()


if __name__ == "__main__":
    main()
