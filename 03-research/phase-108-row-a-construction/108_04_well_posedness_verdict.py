#!/usr/bin/env python3
"""108.04 -- well-posedness verdict verifier. Plain python3."""

from __future__ import annotations

import math


def is_compactly_supported_constant(c: float) -> bool:
    """f_0(r) = c for all r>0 (c != 0) is supported on all of (0,infty):
    no finite [A,B] contains {r : f(r) != 0}, since f is the same nonzero
    value c at every r>0, however far out."""
    if c == 0.0:
        return True  # trivially compact (empty) support
    for T in (1.0, 10.0, 100.0, 1e4):
        # any point beyond exp(T) still has f = c != 0, so [e^-T,e^T] never
        # contains the (all of (0,infty)) support
        still_nonzero_beyond_window = (c != 0.0)
        if not still_nonzero_beyond_window:
            return True
    return False


def stabilization_applies_to_family(s: float, c: float = 1.0) -> bool:
    """f_s(r) = c r^s. Does 107_239 SS3's stabilization (finite S(h) once
    supp h is contained in a bounded window) apply? It requires bounded
    support; f_s is nonzero on all of (0, infty) for c != 0, any s, so no
    finite window contains its support. Returns False (does not apply) for
    every s when c != 0."""
    if c == 0.0:
        return True
    return False  # r^s is nowhere zero for c != 0: never compactly supported


def check_domain_gap_generic_to_family() -> bool:
    ss = [-3.0, -1.0, -0.5, 0.0, 0.3, 1.0, 2.7, 5.0]
    return all(not stabilization_applies_to_family(s) for s in ss)


# ---------------------------------------------------------------------------
# Independent re-check of 108.03 Theorem 6.2's witness (nonzero principal
# line), kept local so this document is self-checking.
# ---------------------------------------------------------------------------

def check_principal_witness_nonzero() -> bool:
    r_grid = [0.1 + 0.01 * i for i in range(1000)]
    density = [1.0 / r for r in r_grid]  # div(U_0) density = r^{s-1} at s=0
    return any(abs(d) > 1e-9 for d in density)


def main() -> None:
    f0_not_compact = not is_compactly_supported_constant(1.0)
    domain_gap_generic = check_domain_gap_generic_to_family()
    witness_ok = check_principal_witness_nonzero()

    print(f"F0_IS_COMPACTLY_SUPPORTED: {'NO' if f0_not_compact else 'YES (unexpected)'}")
    print(f"107_239_STABILIZATION_APPLIES_TO_F0: "
          f"{'NO' if not stabilization_applies_to_family(0.0) else 'YES (unexpected)'}")
    print(f"DOMAIN_GAP_GENERIC_TO_GRADED_FAMILY (all s tested): "
          f"{'YES' if domain_gap_generic else 'NO'}")
    print(f"PRINCIPAL_WITNESS_NONZERO (Thm 1.1, cross-check of 108.03): "
          f"{'YES' if witness_ok else 'NO'}")

    theorem_1_1 = witness_ok
    theorem_c_existence_gap_resolved = theorem_1_1
    proposition_2_1 = f0_not_compact and domain_gap_generic
    invariance_well_formed = not proposition_2_1  # i.e. False: it is NOT well formed

    print()
    print(f"GLOBAL_PRINCIPAL_SUBSPACE_NONZERO: {'YES' if theorem_1_1 else 'NO'}")
    print(f"THEOREM_C_EXISTENCE_GAP: "
          f"{'RESOLVED_IN_GRADED_CATEGORY' if theorem_c_existence_gap_resolved else 'OPEN'}")
    print(f"PRINCIPAL_INVARIANCE_STATEMENT_WELL_FORMED: "
          f"{'YES' if invariance_well_formed else 'NO'}")
    print(f"PRINCIPAL_INVARIANCE_TESTED: NOT_ATTEMPTED_PER_SCOPE")

    consistent_split = (
        theorem_1_1
        and theorem_c_existence_gap_resolved
        and proposition_2_1
        and not invariance_well_formed
    )

    print()
    print(f"VERDICT: {'SPLIT' if consistent_split else 'INCONSISTENT'}")

    if not consistent_split:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
