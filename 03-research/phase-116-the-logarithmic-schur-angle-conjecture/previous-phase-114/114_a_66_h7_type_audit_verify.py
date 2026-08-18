#!/usr/bin/env python3
"""Source/type and finite Cech checks for the a66 correction."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
text = H17.read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("Section 6 modules are Ab-valued",
      r"an $A$-module is a functor" in text and r"\to Ab$" in text)
check("Section 6 has scalar extension adjunction", r"\label{eq63}" in text)
check("completed bundles use K-valued local multipliers",
      r"\label{eq113}" in text and r"f_{\alpha} \in {\rm GL}_d ({\mathcal K}_N)" in text)
check("completed transition functions are O-units",
      r"f_{\alpha}^{-1} \circ f_{\beta} \in {\rm GL}_d ({\mathcal O}_{X_N})" in text)
check("11.7 states a right action, not an Ab-module structure",
      r"\label{eq117}" in text
      and r"\circ ({\mathcal O}_{X_N})_{d',d''} \subseteq {\mathcal O}_{X_N} (D)_{d''}" in text)
check("completed Picard is quotient by global K units",
      r"\label{eq1119}" in text and r"K^* \backslash {\mathbb A}_K^*" in text)


# A finite abelian group models GL_1.  Pullback is a group homomorphism.
mod_source, mod_target, multiplier = 6, 18, 3


def phi(x):
    return (multiplier * x) % mod_target


for x in range(mod_source):
    for y in range(mod_source):
        check(f"unit-map homomorphism x={x}, y={y}",
              phi((x + y) % mod_source) == (phi(x) + phi(y)) % mod_target)


# Cech cocycle on three opens: u_ab=t_b-t_a.  Mapping it remains a cocycle.
triv = (1, 4, 5)
for a in range(3):
    for b in range(3):
        for c in range(3):
            u_ab = (triv[b] - triv[a]) % mod_source
            u_bc = (triv[c] - triv[b]) % mod_source
            u_ac = (triv[c] - triv[a]) % mod_source
            check(f"pulled Cech cocycle {a}{b}{c}",
                  (phi(u_ab) + phi(u_bc)) % mod_target == phi(u_ac))


# Multiplicative notation linearized additively:
# u_ab=f_b-f_a=v_b-v_a implies h_a=f_a-v_a is independent of a.
f = (2, 5, 0)
v = (1, 4, 5)
hs = tuple((f[a] - v[a]) % mod_source for a in range(3))
check("coboundary transition functions glue one global K multiplier",
      len(set(hs)) == 1)

print("VERDICT: UNIT-TORSOR PULLBACK PASS; PIC_QC/TOR CLAIMS RETRACTED")
