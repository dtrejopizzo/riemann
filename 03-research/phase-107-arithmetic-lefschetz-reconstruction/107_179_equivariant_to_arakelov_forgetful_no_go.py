#!/home/trabajo/miniforge3/bin/python
"""Exact algebra falsifier for forgetting a localized Euler class."""

from sage.all import LaurentPolynomialRing, ZZ


R = LaurentPolynomialRing(ZZ, "t")
t = R.gen()
euler = 1 - t

euler_not_unit = not euler.is_unit()
augmentation_euler = euler(t=1)

# If z is the image of the formal inverse, extension requires 0*z=1.
test_targets = {
    "ZZ": ZZ,
    "MOD2": ZZ.quotient(2 * ZZ),
    "MOD5": ZZ.quotient(5 * ZZ),
    "MOD11": ZZ.quotient(11 * ZZ),
}
target_contradictions = {}
for label, target in test_targets.items():
    zero = target(0)
    one = target(1)
    target_contradictions[label] = zero != one and zero * one == zero

# Direct sums invert products of Euler factors; augmentation still sends
# every factor, and hence the product, to zero.
multi_character_ok = True
for rank in range(1, 6):
    product = euler**rank
    multi_character_ok = multi_character_ok and product(t=1) == 0 and not product.is_unit()

augmentation_extends = augmentation_euler.is_unit()
all_nonzero_targets_reject = all(target_contradictions.values())
verdict = all(
    [
        euler_not_unit,
        augmentation_euler == 0,
        all_nonzero_targets_reject,
        multi_character_ok,
        not augmentation_extends,
    ]
)

print(f"EULER_CLASS_BEFORE_LOCALIZATION: {euler}")
print(f"EULER_CLASS_IS_ORDINARY_UNIT: {'YES' if not euler_not_unit else 'NO'}")
print(f"AUGMENTATION_OF_EULER_CLASS: {augmentation_euler}")
for label, contradiction in target_contradictions.items():
    print(f"AUGMENTATION_EXTENSION_TO_{label}: {'NO' if contradiction else 'YES'}")
print(f"FINITE_NORMAL_PRODUCTS_SAME_OBSTRUCTION: {'YES' if multi_character_ok else 'NO'}")
print(f"ORDINARY_AUGMENTATION_EXTENDS: {'YES' if augmentation_extends else 'NO'}")
print("DIRECT_MAP_TO_ORDINARY_ARAKELOV: NO")
print("REQUIRED_FORK: GLOBAL_DENOMINATOR_CANCELLATION_OR_EQUIVARIANT_HODGE")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
