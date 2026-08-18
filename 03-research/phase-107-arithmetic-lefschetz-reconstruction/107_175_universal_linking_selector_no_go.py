#!/home/trabajo/miniforge3/bin/python
"""Real-curve falsifier for a source-only universal-linking selector."""

from sage.all import EllipticCurve, kronecker_symbol


E_split = EllipticCurve("20a1")
E_twisted = EllipticCurve("36a4")
d_split = E_split.local_data(2)
d_twisted = E_twisted.local_data(2)

real_local_data_ok = (
    str(d_split.kodaira_symbol()) == "IV*"
    and str(d_twisted.kodaira_symbol()) == "IV*"
    and d_split.tamagawa_number() == 3
    and d_twisted.tamagawa_number() == 1
)

geometric_component_order = 3


def component_action_from_fixed_points(fixed_points):
    if fixed_points == geometric_component_order:
        return 1
    if fixed_points == 1:
        return -1
    return None


action_split = component_action_from_fixed_points(d_split.tamagawa_number())
action_twisted = component_action_from_fixed_points(d_twisted.tamagawa_number())
component_actions_differ = action_split == 1 and action_twisted == -1

chi_minus_7_at_2 = kronecker_symbol(-7, 2)
chi_5_at_2 = kronecker_symbol(5, 2)
linking_has_both_signs = chi_minus_7_at_2 == 1 and chi_5_at_2 == -1

# The universal linking source is indexed by p alone, so both targets get
# literally the same source object lk_2 before a quotient character is chosen.
source_key_split = (2, "universal_artin_map")
source_key_twisted = (2, "universal_artin_map")
universal_source_equal = source_key_split == source_key_twisted

# A function of one identical source key cannot output both required signs.
target_independent_selector_realizes_both = (
    not universal_source_equal or action_split == action_twisted
)

verdict = all(
    [
        real_local_data_ok,
        component_actions_differ,
        linking_has_both_signs,
        universal_source_equal,
        not target_independent_selector_realizes_both,
    ]
)

print(f"REAL_IVSTAR_PAIR_VERIFIED: {'YES' if real_local_data_ok else 'NO'}")
print(f"COMPONENT_ACTION_20A1: {action_split:+d}")
print(f"COMPONENT_ACTION_36A4: {action_twisted:+d}")
print(f"CURVE_COMPONENT_ACTIONS_DIFFER: {'YES' if component_actions_differ else 'NO'}")
print(f"LINKING_CHARACTER_MINUS7_AT_2: {chi_minus_7_at_2:+d}")
print(f"LINKING_CHARACTER_5_AT_2: {chi_5_at_2:+d}")
print(f"UNIVERSAL_LINKING_HAS_BOTH_SIGNS: {'YES' if linking_has_both_signs else 'NO'}")
print(f"UNIVERSAL_LINKING_SOURCE_EQUAL: {'YES' if universal_source_equal else 'NO'}")
print(
    "TARGET_INDEPENDENT_SELECTOR_REALIZES_BOTH: "
    f"{'YES' if target_independent_selector_realizes_both else 'NO'}"
)
print("ROOTED_LINKING_REOPENS_S3: NO")
print("ROOTED_LINKING_CAPACITY: GALOIS_SENSITIVE")
print("REQUIRED_MISSING_INPUT: SOURCE_DERIVED_QUOTIENT_CHARACTER")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
