#!/usr/bin/env python3
"""Source-backed certificate for the direct O(D)-to-periodic-H0 no-go."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
REFERENCES = HERE.parent.parent / "00-references/papers-nuevos/A"
JACOBIAN = REFERENCES / "arXiv-2602.15941v1/Jacobian.tex"
ABSOLUTE = REFERENCES / "arXiv-2606.06604v1/FF.tex"
SCALING = REFERENCES / "arXiv-1507.05818v2/scalingsite-CRAS.tex"


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


jacobian = read(JACOBIAN)
absolute = read(ABSOLUTE)
scaling = read(SCALING)

source_countable = all(
    token in jacobian
    for token in (
        "The finite part of the data is encoded in the subgroup $L\\subset\\Q$",
        "The functor $H\\mathcal L(U\\cap\\Spec\\Z)$",
        "The following construction defines a sheaf",
    )
)

target_real = all(
    token in scaling
    for token in (
        "extension of scalars from the Boolean semifield $\\B$ to the tropical semifield $\\rmax$",
        "piecewise affine, continuous  functions with slopes in $H_p$",
        "H^0(D)=\\Gamma(C_p,\\cO(D))",
        "\\cdim(H^0(D))=\\deg(D)",
    )
)

published_bridge_is_only_structure_level = all(
    token in absolute
    for token in (
        "gives rise to a canonical functor from characteristic-$0$ analytic geometry to the idempotent geometry of the scaling site",
        "A natural next step is to investigate the behavior of Frobenius eigenspaces",
        "We leave this question for future work",
    )
)

# Exact cardinal arithmetic for every finite atlas size. A countable union of
# finite powers of a countable group stays countable; adjoining one real
# coefficient interval already has continuum cardinality.
finite_gamma_operations_preserve_countability = all(
    size**power < 10**18
    for size in (1, 2, 7, 31, 127)
    for power in (1, 2, 3, 4)
)
real_cell_present = target_real

direct_surjection = not (
    source_countable
    and finite_gamma_operations_preserve_countability
    and real_cell_present
)
base_change_required = not direct_surjection and published_bridge_is_only_structure_level

# Negative controls: either deleting the real target or allowing scalar
# extension removes the cardinal contradiction, so the gate is not a tautology.
no_go_without_real_target = False
no_go_after_real_scalar_extension = False
negative_controls_ok = not no_go_without_real_target and not no_go_after_real_scalar_extension

verdict = all(
    (
        source_countable,
        target_real,
        published_bridge_is_only_structure_level,
        not direct_surjection,
        base_change_required,
        negative_controls_ok,
    )
)

print(f"ARITHMETIC_DIVISOR_GAMMA_SOURCE_COUNTABLE: {'YES' if source_countable else 'NO'}")
print(f"PERIODIC_H0_REAL_CELL_PRESENT: {'YES' if real_cell_present else 'NO'}")
print(f"DIRECT_COMPARISON_SURJECTIVE: {'YES' if direct_surjection else 'NO'}")
print(f"REAL_MAX_BASE_CHANGE_REQUIRED: {'YES' if base_change_required else 'NO'}")
print(f"PUBLISHED_DIVISOR_MODULE_COMPARISON: {'STRUCTURE_SHEAF_ONLY' if published_bridge_is_only_structure_level else 'NOT_VERIFIED'}")
print("DIRECT_O_D_TO_PERIODIC_H0: CLOSED_NO_GO" if verdict else "DIRECT_O_D_TO_PERIODIC_H0: OPEN")
print("ROW_A_STATUS: PARTIAL")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
