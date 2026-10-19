# Phase 40 — Closing G1

Following the axiom list ("forced axioms") of Phase 39, this phase attempts to close G1 — a signature/symmetry structure on the cohomology of the square $X\times X$ of the Connes–Consani scaling site — by reading the Connes–Consani "Riemann–Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$" source directly for a duality pairing with a computable character, and by constructing the cohomology of the square via the tolerance-relation technique.

## Results
- The symmetry character of the duality pairing at the self-dual divisor $D_0=-\{2\}$: CC's duality is identified in source as Pontryagin duality (group/dual evaluation), a third kind distinct from both the alternating cup product and symmetrizable Serre duality; the "symmetry character" is not defined for it without an external polarization, and the pointwise computation at $D_0$ is vacuous since both cohomology groups vanish there. (NO-GO — structural gap, not a technical one)
- Construction of $H^1$ of the square via tolerance: reaches outcome "PARTIAL," isolating the core obstruction — the numerical content of the tolerance receptacle (C-rank) is an intersection form, which is exactly the missing G2 ingredient; so G1's numerical part and G2 coincide as one object. (PARTIAL CONSTRUCTION, core isolated, not closed)
- Whether Connes–Consani's Weil positivity supplies the missing Hodge-index ingredient for G2: tested against two CC papers and found to be spectral/operator positivity (positive-definite, on test functions, RH-equivalent and circular), never geometric intersection positivity (indefinite, signature $(1,\rho-1)$, on classes); no intersection-positivity fragment exists in the corpus read. (NO-GO)

## Documents
- `122-symmetry-bit-the-character.md`: duality-pairing character at the self-dual divisor; verdict that CC duality is Pontryagin, not a signature-bearing pairing.
- `123-construction-of-the-cohomology-of-the-square.md`: tolerance-based construction of $H^1(X\times X)$; isolates the C-rank/intersection-form core as identical to G2.
- `124-connes-consani-s-weil-positivity.md`: tests whether CC's Weil positivity is the missing Hodge index; verdict: it is spectral/circular, not intersection positivity.

## Relation to other phases
Executes the axioms derived in Phase 39 (R-SIG, R-FIN, R-NC test). The finding that G1's numerical core equals G2 directly motivates Phase 41's attempt to build the intersection form from scratch.
