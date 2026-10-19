# Phase 48 — Audit and Purity

This phase audits the five documents of Phase 47 (the 139.A revival, the LP-141/GAP-141.DH results, the GAP-142.B spectrality decision, and the GAP-135.A frame analysis), then develops a positive theory of "purity" (how far a local factor's divisor sits from its weight-normalized center) and uses it to kill an attempted zero-repulsion mechanism at the critical line.

## Results
- Audit of the 139.A revival (Doc 147): the exponential-dominance repair does NOT revive the ¬RH-branch theorem — audited and found insufficient. (NO-GO — the repair attempt fails)
- Audit of Docs 144 and 146 (LP-141 Hadamard counterexample and the GAP-141.DH fatness verdict): the central propositions (144.2, 144.3) survive the audit intact; the GAP-141.DH verdict is corrected but confirmed in essence. (AUDIT — core results survive, with corrections)
- Audit of Docs 145 and 148 (spectrality collapse of H⁺; GAP-135.A as a frame problem): Theorem 2.2 (the Bochner-type spectrality criterion) is confirmed correct with one erratum; both documents' main findings largely survive adversarial attack. (AUDIT — core results survive, with an erratum)
- Purity theory (Doc 152): the local-purity gap between $\zeta$'s local factor (pure of weight 0, boundary divisor) and the weight-1 normalization used in the program's positivity theorems is resolved in a single clean statement — the global functional equation recenters the archimedean weights but never the zeros, so **RH is precisely the statement that the zero divisor gets recentered from weight 0 to weight 1**, the one piece the functional equation cannot do. A semi-global purity theorem is proved for the Gaussian prime-correlation impurity spectrum $\omega(\tau)$, giving an unconditional closed formula for $\omega(\tau)$ in terms of the off-critical quadruples, with $\mathrm{RH}\iff\omega(\tau)=0$ for all $\tau\ge1$ and the pole identified as the unique unavoidable weight-$1/4$ impurity at frequency 0. (PROVED)
- Attack on Conjecture 144.D / GAP-144.C (transposing the classical zero-free-region repulsion mechanism to the critical line): the attempted "dlVP-at-½" repulsion mechanism dies quantitatively — an off-critical quadruple perturbs the region where the classical positivity argument bites only at second order, and reaching constant cumulative effect would require superlinear zero density, forbidden unconditionally by the Riemann–von Mangoldt formula. A new one-signed, dominant "self-scale excess" quantity is isolated as what survives the wreck. (NO-GO for the classical-mechanism transposition; a new positive partial result identified)

## Documents
- `149-adversarial-audit-of-the-139-a-revival.md`: audit of Doc 147's repair attempt; verdict: does not revive the theorem.
- `150-adversarial-audit-of-docs-144-and-146.md`: audit of the LP-141 counterexample and the GAP-141.DH fatness verdict.
- `151-adversarial-audit-of-docs-145-and-148.md`: audit of the H⁺ spectrality collapse and the GAP-135.A frame analysis.
- `152-attack-purity-rigidity-the-two-purities-semi.md`: purity theory — the weight-0/weight-1 gap as the precise content of RH, and the semi-global purity theorem for the impurity spectrum $\omega(\tau)$.
- `153-attack-on-conjecture-144-d-gap-144.md`: death of the dlVP-at-½ repulsion transposition, with a quantitative certificate; isolation of the surviving self-scale excess quantity.

## Relation to other phases
Audits all five documents of Phase 47. Doc 152's purity theorem and Doc 153's self-scale excess quantity are carried forward into the final synthesis of Phase 49.
