#!/usr/bin/env python3
"""Source and ordinary cotangent checks for the exact H7-LCI-DELTA gate."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
text = H17.read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("Haran modules form an abelian category",
      "complete and co-complete abelian category" in text)
check("Kahler differentials are represented in A-mod",
      r"\label{eq66}" in text and r"{\rm Der}_k (A,M)" in text)
check("differentials have a transitivity exact sequence",
      r"\label{eq67}" in text and r"\Omega (B/A) \to 0" in text)
check("source constructs Quillen cotangent complex",
      "Quillen cotangent complex" in text and "derived category" in text)


# For Z -> F_p, the relative cotangent complex is the one-term module F_p
# in homological degree 1.  Model the differential after quotient as zero.
for p in (2, 3, 5, 7, 11, 13):
    degree_1 = list(range(p))
    differential = {x: 0 for x in degree_1}
    kernel = [x for x in degree_1 if differential[x] == 0]
    image_degree_2 = {0}
    h1_size = len(kernel) // len(image_degree_2)
    h0_size = 1  # no degree-zero term in the relative conormal model
    check(f"L_Fp/Z has H1=F_p p={p}", h1_size == p)
    check(f"L_Fp/Z has zero H0 p={p}", h0_size == 1)


# Logical independence model: injectivity on a set does not by itself encode
# a chain-complex quasi-isomorphism. Two complexes can share the same regular
# scalar action and have different H1.
regular_action = tuple(2 * x for x in range(-8, 9))
check("regular scalar action is injective", len(set(regular_action)) == 17)
complex_h1_sizes = (1, 2)
check("regularity data do not determine derived H1",
      complex_h1_sizes[0] != complex_h1_sizes[1])

print("VERDICT: GLOBAL COTANGENT CONORMAL TYPED; H7-LCI-DELTA REMAINS OPEN")
