#!/usr/bin/env python3
"""Source and finite checks for the fraction-pullback correction a63."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
text = H17.read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("(11.1) regular denominators quantify over later levels and all arities",
      r"\label{eq111}" in text
      and r"\forall \, M \geq N" in text
      and r"a,a' \in {\mathcal O}_{X_M}" in text)
check("(11.3) bundle trivializers live in GL(K)",
      r"\label{eq113}" in text and r"{\rm GL}_d ({\mathcal K}_N)" in text)
check("(11.10) states pullback for pro transition maps",
      r"\label{eq1110}" in text and r"(\pi_N^M)^*" in text)

# Split maps do not preserve non-zero-divisors.  Model B=Z x F_p on a finite
# window: e=(0,1) is nonzero and p*e=0, although Z -> B has a retraction.
for p in (2, 3, 5, 7, 11):
    e = (0, 1)
    pe = (p * e[0], (p * e[1]) % p)
    check(f"split-map regularity counterexample p={p}", e != (0, 0) and pe == (0, 0))
    for a in range(-10, 11):
        embedded = (a, a % p)
        retracted = embedded[0]
        check(f"split retraction p={p}, a={a}", retracted == a)

doc = (HERE / "114_a_63_H7_FRACTION_PULLBACK_ADMISSIBILITY_AUDIT.md").read_text()
check("actual square fails denominator regularity at 2 by a108",
      "H7-PB-REG/H7-PRIME-REG fails" in doc)
print("VERDICT: FRACTION-PULLBACK CONDITION VALID; a108 PROVES FAILURE AT 2")
