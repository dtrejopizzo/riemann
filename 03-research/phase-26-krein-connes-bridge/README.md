# Phase 26 — the Kreĭn-Connes bridge theorem

The phase attempts to formulate, precisely, a new bridge identifying the
Kreĭn negative index κ of the Weil quadratic form with the non-self-
adjointness (number of non-real eigenvalues) of the Connes scaling
operator H_C on the adèle class space. A literature audit first confirms
no such precise identification exists; the phase then tries to prove the
bridge's central technical step.

## Results
- Bibliographic audit: no prior work (Connes, Connes-Consani, Burnol,
  Kreĭn-Langer) states a precise identification κ(Q) = neg.ind(H_C); the
  bridge theorem, if true, would be new. **Confirmed absent from
  literature**.
- Proposition 26-A.1/Definition 26-A.2 restate the classical Weil
  positivity criterion and the Kreĭn negative index κ (= 2m under
  Hypothesis D, citing earlier phases). **PROVED/CITED** (classical).
- Theorem 26-A.1 (Kreĭn-Langer spectral theorem applied to H_C): a
  Q-self-adjoint operator on a Pontryagin space of index κ has **at most**
  κ/2 pairs of non-real eigenvalues; this direction is free. **PROVED**
  (classical theorem, cited).
- The harder direction — that H_C has **at least** as many non-real
  eigenvalues as off-line orbits (item V.2, identified as the true heart of
  the bridge, not a routine verification) — is analyzed and found
  obstructed: the natural candidate eigenvector (the character x^{b_j+iγ_j})
  formally satisfies the right eigenvalue equation but is **not** in
  L²(adèle class group) — its norm diverges. **PROVED** (divergence
  computation); the eigenvector-existence claim is therefore **OPEN**,
  not merely technical.
- Two strategies are left open: (A) a distributional/regularized extension
  of the Weil form on which the characters have finite regularized norm, or
  (B) reformulating the bridge in localized form, connecting it to the
  numerical localized-Weil-form negativity measured in an earlier "main
  arc" of the program. Neither is completed. **OPEN**.
- Explicit two-way success criterion stated for the phase: either the
  bridge theorem is proved (opening an adelic route to RH) or it is proved
  impossible in this form with a precise diagnosis (refining the question);
  the phase stops at the diagnosis stage, having shown the direct approach
  (Strategy A, literal L² eigenvectors) fails.

## Documents
- `00-bridge-theorem.md` — literature audit, precise statement of the two
  structures (Weil form / Kreĭn index on one side, Connes operator H_C on
  the other), and the proposed bridge conjecture with its work plan.
- `01-attack-V2.md` — direct attack on the bridge's central item V.2:
  the abstract Kreĭn-Langer bound, the non-L² obstruction for the natural
  eigenvector candidate, the two proposed repair strategies, and a status
  table for all bridge components (V.1-V.4).

## Relation to other phases
Builds on the Kreĭn-index / Lorentz-decomposition machinery of phases
21-23; the localization strategy (B) is explicitly connected to an earlier
numerical "main arc" of the broader program that measures negativity of a
localized Weil form near a candidate off-line zero.
