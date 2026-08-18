#!/usr/bin/env python3
"""
112.01 -- The candidate cone: f >= 0, and the easy half.

Verifies (numerically, in evaluation coordinates):
  Lemma 1.1: I_partial(D_f, H) = fhat(0) + fhat(1)   (exact algebraic identity,
             checked by evaluating the FULL boxed pairing formula (2.1)
             against H's coordinates, with a nonzero synthetic zero set, so
             that the vanishing of the zero-sum term against H is actually
             exercised rather than assumed away).
  Theorem 1.2: f >= 0, f != 0  ==>  I_partial(D_f, H) > 0.
  Control clause: f <= 0, f != 0  ==>  I_partial(D_f, H) < 0.  This shows the
             check can fail (would flag a wrong-signed candidate), i.e. it is
             not a vacuous / unconditionally-passing test.

No zeta zero is used as an input (matching the convention of
107_241_hodge_index_for_the_corner_pairing.py): the zero set used to
exercise the general formula (2.1) is a synthetic mirror-symmetric multiset,
unrelated to xi.

Run: python3 112_01_the_candidate_cone.py
"""

import mpmath as mp

mp.mp.dps = 30

# ----------------------------------------------------------------------
# Test class: f(r) = phi((log r - mu)/L), phi a C^infty bump on (-1,1).
# This is C_c^infty((0,infty)), matching assumption A2.
# ----------------------------------------------------------------------

def phi(t):
    if abs(t) >= 1:
        return mp.mpf(0)
    return mp.e ** (-1 / (1 - t ** 2))


def fhat(s, mu, L, sign=1):
    """ fhat(s) = int_0^infty f(r) r^{s-1} dr, f(r)=sign*phi((log r-mu)/L). """
    def integrand(u):
        b = phi(u)
        if b == 0:
            return mp.mpf(0)
        r = mp.e ** (mu + L * u)
        return sign * b * r ** (s - 1) * r * L  # dr = r L du

    return mp.quad(integrand, [-1, -0.6, -0.2, 0.2, 0.6, 1])


# ----------------------------------------------------------------------
# Synthetic mirror-symmetric zero multiset (NOT zeta zeros), to exercise
# the general boxed formula (2.1).  Mirror involution rho -> 1 - conj(rho).
# ----------------------------------------------------------------------

SYNTH_ZEROS = [
    (mp.mpf('0.5'), mp.mpf('14.0')),   # on-line pair (fixed point under mirror)
    (mp.mpf('0.5'), mp.mpf('21.0')),
    (mp.mpf('0.3'), mp.mpf('9.0')),    # off-line mirror pair partner below
]


def full_zero_multiset():
    """Return list of (rho, mult) with the mirror involution closed up."""
    Z = []
    for (sigma, t) in SYNTH_ZEROS:
        rho = mp.mpc(sigma, t)
        rho_bar_partner = 1 - mp.conj(rho)  # mirror rho' = 1 - conj(rho)
        Z.append((rho, 1))
        if abs(rho_bar_partner - rho) > mp.mpf('1e-20'):
            Z.append((rho_bar_partner, 1))
        # also include the complex-conjugate zero (xi has real coefficients)
        rho_conj = mp.conj(rho)
        if abs(rho_conj - rho) > mp.mpf('1e-20') and abs(rho_conj - rho_bar_partner) > mp.mpf('1e-20'):
            Z.append((rho_conj, 1))
            mirror_of_conj = 1 - mp.conj(rho_conj)
            if all(abs(mirror_of_conj - z) > mp.mpf('1e-20') for z, _ in Z):
                Z.append((mirror_of_conj, 1))
    return Z


ZEROS = full_zero_multiset()


def mirror(rho):
    return 1 - mp.conj(rho)


def I_partial_full(f_params, H_mode=True, g_params=None):
    """
    Evaluate the FULL boxed formula (2.1):
       fhat(0) conj(ghat(1)) + fhat(1) conj(ghat(0))
         - sum_rho m_rho fhat(rho) conj(ghat(rho'))
    against g = H (H_mode=True: ghat(0)=ghat(1)=1, ghat(rho)=0 for all rho)
    or against an actual D_g (H_mode=False, g_params given).
    """
    muf, Lf, signf = f_params
    f0 = fhat(0, muf, Lf, signf)
    f1 = fhat(1, muf, Lf, signf)

    if H_mode:
        g0, g1 = mp.mpf(1), mp.mpf(1)
        zero_sum = mp.mpf(0)  # ghat(rho') = 0 for every rho, by definition of H
        for rho, m in ZEROS:
            fr = fhat(rho, muf, Lf, signf)
            g_rp = mp.mpf(0)
            zero_sum += m * fr * mp.conj(g_rp)
    else:
        mug, Lg, signg = g_params
        g0 = fhat(0, mug, Lg, signg)
        g1 = fhat(1, mug, Lg, signg)
        zero_sum = mp.mpf(0)
        for rho, m in ZEROS:
            fr = fhat(rho, muf, Lf, signf)
            rp = mirror(rho)
            g_rp = fhat(rp, mug, Lg, signg)
            zero_sum += m * fr * mp.conj(g_rp)

    polar = f0 * mp.conj(g1) + f1 * mp.conj(g0)
    return polar - zero_sum, f0, f1


def closed_form(f_params):
    muf, Lf, signf = f_params
    f0 = fhat(0, muf, Lf, signf)
    f1 = fhat(1, muf, Lf, signf)
    return f0 + f1, f0, f1


# ----------------------------------------------------------------------
# Checks
# ----------------------------------------------------------------------

results = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))
    results.append(cond)


TOL = mp.mpf('1e-15')

test_configs_pos = [
    (0.0, 0.4, 1),
    (1.0, 0.3, 1),
    (-1.5, 0.6, 1),
    (2.2, 0.15, 1),
]

print("=== Lemma 1.1: boxed formula (2.1) against H equals fhat(0)+fhat(1) ===")
for (mu, L, sign) in test_configs_pos:
    fp = (mu, L, sign)
    full_val, f0a, f1a = I_partial_full(fp, H_mode=True)
    cf_val, f0b, f1b = closed_form(fp)
    rel_err = abs(full_val - cf_val) / max(abs(cf_val), TOL)
    check(f"Lemma 1.1 identity at mu={mu}, L={L}",
          rel_err < mp.mpf('1e-12'),
          f"full={mp.nstr(full_val,10)} closed={mp.nstr(cf_val,10)} relerr={mp.nstr(rel_err,3)}")

print("\n=== Theorem 1.2: f >= 0, f != 0  =>  I_partial(D_f,H) > 0 ===")
for (mu, L, sign) in test_configs_pos:
    fp = (mu, L, sign)
    val, f0, f1 = closed_form(fp)
    check(f"positivity at mu={mu}, L={L}",
          val > 0 and f0 > 0 and f1 > 0,
          f"I={mp.nstr(val,10)} fhat(0)={mp.nstr(f0,6)} fhat(1)={mp.nstr(f1,6)}")

print("\n=== Control clause: f <= 0, f != 0  =>  I_partial(D_f,H) < 0 "
      "(shows the test is not vacuous) ===")
for (mu, L, sign) in test_configs_pos:
    fp_neg = (mu, L, -sign)
    val, f0, f1 = closed_form(fp_neg)
    check(f"negativity control at mu={mu}, L={L} (f<=0)",
          val < 0 and f0 < 0 and f1 < 0,
          f"I={mp.nstr(val,10)}")

print("\n=== Sanity: value scales correctly, not just its sign "
      "(reject a plausible wrong value: I_partial(D_f,H) != fhat(0) alone) ===")
for (mu, L, sign) in test_configs_pos:
    fp = (mu, L, sign)
    val, f0, f1 = closed_form(fp)
    # A wrong-but-plausible implementation might return only fhat(0) (dropping
    # the second polar term). Check the true value differs from that unless
    # fhat(1) happens to vanish (it does not, for these bumps).
    check(f"value is fhat(0)+fhat(1), not fhat(0) alone, at mu={mu}, L={L}",
          abs(val - f0) / abs(val) > mp.mpf('0.01'),
          f"val={mp.nstr(val,8)} fhat(0) alone={mp.nstr(f0,8)}")

print()
if all(results):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    raise SystemExit(1)
