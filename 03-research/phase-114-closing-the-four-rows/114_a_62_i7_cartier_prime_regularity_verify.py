#!/usr/bin/env python3
"""Source/type checks for corrected a62; H7-PRIME-REG remains open."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
text = H17.read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("Haran (9.7) gives the ordinary local intersection description",
      r"\label{eq97}" in text and r"{\mathbb Z}_{(p)}" in text)
check("Haran Section 6 makes the module category abelian",
      "complete and co-complete abelian category" in text
      and r"\to Ab$" in text)
check("Haran (11.1) defines regularity on operation sets in all arities",
      r"\label{eq111}" in text
      and r"a,a' \in {\mathcal O}_{X_M}" in text
      and r"\Rightarrow a=a'" in text)
check("Haran (11.7) gives only a right-action subsheaf",
      r"\label{eq117}" in text
      and r"\circ ({\mathcal O}_{X_N})_{d',d''} \subseteq" in text)
check("Haran (11.17)--(11.19) gives the adelic bundle and Picard models",
      all(fr"\label{{eq11{k}}}" in text for k in (17, 18, 19)))

# Over Z, 0 -> (p) -> Z -> F_p -> 0 has the expected finite quotient.
for p in (2, 3, 5, 7, 11, 13):
    residues = {a % p for a in range(4 * p)}
    check(f"ordinary prime quotient has size {p}", len(residues) == p)

# Direct regularity model: integer multiplication is cancellative.  This is
# evidence for the curve chart only, not a Tor statement on the square.
for p in (2, 3, 5, 7):
    for a in range(-20, 21):
        for b in range(-20, 21):
            check(f"integer cancellation p={p}, a={a}, b={b}",
                  (p * a != p * b) or (a == b))

print("VERDICT: DENOMINATOR GATE IS H7-PRIME-REG; CARTIER/TOR CLAIMS RETRACTED")
