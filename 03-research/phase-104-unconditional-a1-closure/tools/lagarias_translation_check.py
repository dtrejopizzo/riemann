"""104_02 verification after the Lagarias-sign erratum.

Checks the corrected residual in `104_02_LAGARIAS_TRANSLATION.md`:

    lambda_n - A_n = +lambda_n(sqrt n) + O(sqrt n log n)          [unconditional]

where lambda_n(T) is Lagarias' *incomplete Li coefficient* (math/0404394, eq. 1.14),

    lambda_n(T) = sum_{|Im rho| < T} [ 1 - (1 - 1/rho)^n ].

Pairing rho with its conjugate, each pair contributes 2*Re[1 - (1-1/rho)^n], so on the
critical line the pair contribution is 2 - 2cos(n theta_rho) in [0, 4].

Thus the residual

    Dtilde_n := lambda_n - A_n - lambda_n(sqrt n) = -tilde_epsilon_n

must be O(sqrt n log n).  The ratio Dtilde_n / (sqrt n log n) is an *empirical* stand-in for the
corrected contour estimate.  It is a diagnostic, NOT a proof of effectivity.

Erratum being checked.  At a nontrivial zero s0=rho-1,

    Res_{s=s0} k_n(s)(-L'/L)(s+1) = -k_n(rho-1),

not +k_n(rho-1).  Consequently the finite-place relation has the opposite sign from
Lagarias' printed equations (1.15), (1.17), and Theorem 6.1.

Inputs reused (not rewritten):
  * lambda_n           <- phase-103-direct-a1-closure/tools/zeta_tools.li_lambda
  * A_n = lambda_n^arch <- phase-103-direct-a1-closure/tools/arch_and_margin.lambda_arch

Zeta zeros: for n <= 2500 we need only |gamma| < sqrt(2500) = 50, i.e. the first ten
ordinates, which are standard reference constants (hard-coded below to 18 digits).

Run:  python3 lagarias_translation_check.py
"""

import math
import os
import sys

import numpy as np

_P103 = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "phase-103-direct-a1-closure", "tools",
)
sys.path.insert(0, os.path.normpath(_P103))

from zeta_tools import li_lambda            # noqa: E402
from arch_and_margin import lambda_arch     # noqa: E402

# First ten ordinates of the nontrivial zeros of zeta (standard reference values).
GAMMAS = [
    14.134725141734693790,
    21.022039638771554993,
    25.010857580145688763,
    30.424876125859513210,
    32.935061587739189691,
    37.586178158825671257,
    40.918719012147495187,
    43.327073280914999519,
    48.005150881167159727,
    49.773832477672302182,
]
GAMMA_MAX = GAMMAS[-1]


def incomplete_li(n, T):
    """lambda_n(T) assuming every zero with |gamma| < T lies on the critical line.

    Conjugate pairs are summed together, so the result is real by construction.
    """
    if T > GAMMA_MAX:
        raise ValueError(
            f"T={T:.3f} exceeds the hard-coded zero table (max {GAMMA_MAX:.3f}); "
            "extend GAMMAS before using this n"
        )
    total = 0.0
    for g in GAMMAS:
        if g >= T:
            break
        rho = complex(0.5, g)
        total += 2.0 * (1.0 - (1.0 - 1.0 / rho) ** n).real
    return total


def main():
    # sqrt(n) must stay under the zero table, so n <= GAMMA_MAX^2 ~= 2477.
    ns = [8, 12, 16, 20, 30, 50, 80, 120, 200, 300, 400, 600,
          800, 1000, 1200, 1600, 2000, 2400]
    nmax = max(ns)

    lam = li_lambda(nmax, r=0.995, M=1 << 19)
    lam_b = li_lambda(nmax, r=0.985, M=1 << 19)

    print("Corrected sign check:")
    print("  Dtilde_n := lambda_n - A_n - lambda_n(sqrt n) = O(sqrt n log n)")
    print()
    print(f"{'n':>5} {'#pairs':>6} {'lambda_n':>14} {'A_n':>14} "
          f"{'lam_n(sqrt n)':>14} {'Dtilde_n':>12} {'|D|/(vn ln n)':>14} {'stab':>9} {'ok':>4}")
    print("-" * 102)

    # A row is trustworthy only if the two-radius disagreement in the Cauchy extraction of
    # lambda_n is far below the residual it is supposed to diagnose.  Otherwise what we would
    # be measuring is the extraction error, not Dtilde_n.  This is the numerical trap flagged in
    # 103_06; the guard is mandatory, not cosmetic.
    STAB_TOL = 0.01          # stab must be < 1% of |Dtilde_n|

    ratios, discarded = [], []
    for n in ns:
        T = math.sqrt(n)
        npairs = sum(1 for g in GAMMAS if g < T)
        ln = lam[n - 1]
        stab = abs(ln - lam_b[n - 1])          # two-radius agreement = Cauchy stability
        an = lambda_arch(n)
        inc = incomplete_li(n, T)
        dn = ln - an - inc
        scale = math.sqrt(n) * math.log(n)
        reliable = abs(dn) > 0 and stab < STAB_TOL * abs(dn)
        if reliable:
            ratios.append((n, abs(dn) / scale))
        else:
            discarded.append(n)
        print(f"{n:>5} {npairs:>6} {ln:>14.6f} {an:>14.6f} {inc:>14.6f} "
              f"{dn:>12.4f} {abs(dn)/scale:>14.4f} {stab:>9.1e} "
              f"{'yes' if reliable else 'NO':>4}")

    print("-" * 102)
    nmax_ok = max(n for n, _ in ratios)
    sup_n, sup_r = max(ratios, key=lambda t: t[1])
    print(f"rows discarded (two-radius disagreement too large): "
          f"{discarded if discarded else 'none'}")
    print(f"two-radius-stable rows tested: up to n = {nmax_ok}")
    print(f"sample sup |Dtilde_n| / (sqrt n log n) = {sup_r:.4f}   (attained at n = {sup_n})")
    print()
    print("Reading (see 104_02 section 7):")
    print("  * A bounded, non-growing ratio column over the two-radius-stable rows is")
    print("    CONSISTENT with the corrected sign. It is not a proof: finite sample, and")
    print("    lambda_n here is a Cauchy-integral diagnostic, not a certified rational interval.")
    print("  * 'stab' = |li_lambda(r=0.995) - li_lambda(r=0.985)|. Where it is not far below")
    print("    |Dtilde_n|, the row measures extraction error, not the identity, and is discarded.")
    print("  * CAVEAT: two-radius agreement is a necessary, NOT a sufficient, reliability")
    print("    test. Both radii share the same Borwein zeta evaluation, the same FFT length")
    print("    and the same float64 arithmetic, so they can carry a COMMON systematic error")
    print("    that agreement will not reveal. 'Stable' here means 'not caught failing',")
    print("    never 'certified'. A real certificate needs interval arithmetic, as in 103_51.")
    print("  * incomplete_li assumes RH below sqrt(n) (true here: sqrt n < 50 << 3e12,")
    print("    Platt-Trudgian). That assumption is what makes this a CHECK, not a theorem.")
    print("  * The ratio is NOT an effective C_*: the corrected contour constant is uniform")
    print("    in n, while this is only a sample maximum.")


if __name__ == "__main__":
    main()
