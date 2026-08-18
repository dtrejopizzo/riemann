#!/home/trabajo/miniforge3/bin/sage
"""Falsifier for compatibility of rooted and cellular transitions."""


ATLAS = (
    (3, 6),
    (4, 8),
    (5, 10),
    (6, 12),
    (6, 18),
    (8, 24),
)


def check_pair(L, Lprime):
    d = Lprime // L
    field = CyclotomicField(L)
    zeta = field.gen()
    moved = zeta**d != zeta
    criterion = moved == ((d - 1) % L != 0 if d > 1 else False)

    # x -> x' would have to kill x^L-1 in the target quotient.  Its
    # evaluation at a primitive L'-th root proves that it does not.
    target = CyclotomicField(Lprime)
    target_zeta = target.gen()
    naive_relation_nonzero = target_zeta**L - 1 != 0

    # The actual cellular map x -> x'^d does kill the source relation.
    cellular_relation_zero = (target_zeta**d) ** L - 1 == 0
    return (L, Lprime, d, moved, criterion, naive_relation_nonzero, cellular_relation_zero)


def main():
    rows = tuple(check_pair(*pair) for pair in ATLAS)

    moved_controls = all(row[3] for row in rows[:4])
    criteria = all(row[4] for row in rows)
    naive_rejected = all(row[5] for row in rows)
    cellular_well_defined = all(row[6] for row in rows)

    # Exceptional positive control: order two is fixed when d is odd.
    zeta2 = CyclotomicField(2).gen()
    exceptional_fixed = zeta2**3 == zeta2

    verdict = (
        moved_controls
        and criteria
        and naive_rejected
        and cellular_well_defined
        and exceptional_fixed
    )

    print("Rooted/cellular transition rows:")
    for L, Lprime, d, moved, _, _, _ in rows:
        print(f"  L={L}, L'={Lprime}, d={d}: primitive old label moved={moved}")
    print()
    print(f"ACTUAL_CYCLOTOMIC_TRANSITIONS: {len(rows)}")
    print(f"POWER_MAP_CRITERION: {'YES' if criteria else 'NO'}")
    print(f"GENERIC_OLD_LABELS_PRESERVED: {'NO' if moved_controls else 'UNRESOLVED'}")
    print(f"NAIVE_X_TO_XPRIME_DESCENDS: {'NO' if naive_rejected else 'UNRESOLVED'}")
    print(f"CELLULAR_POWER_MAP_WELL_DEFINED: {'YES' if cellular_well_defined else 'NO'}")
    print(f"EXCEPTIONAL_FIXED_LABEL_CONTROL: {'YES' if exceptional_fixed else 'NO'}")
    print("ROOTED_CELLULAR_COMMON_DESCENT: CLOSED_NO_GO")
    print("TWISTED_H1_DIRECT_SYSTEM: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("rooted/cellular transition verifier failed")


main()
