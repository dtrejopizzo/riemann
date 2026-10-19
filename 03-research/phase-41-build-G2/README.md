# Phase 41 — Building G2

Having identified in Phase 40 that G1 and G2 share the same missing numerical ingredient — an intersection form of Hodge-index type (signature $(1,\rho-1)$) on the square of the scaling site — this phase attempts to construct that intersection form directly, following Weil's classical template (Hodge index on $C\times C$) via tropical intersection theory (Allermann–Rau), and then asks whether a Hodge-index theorem is even attainable for this tropical object or whether it is forced to be RH-circular.

## Results
- Explicit construction of a Gram matrix for the toy model $C_p\times C_p$ using tropical (Allermann–Rau) intersection theory on three classes $\langle f_1,f_2,\Delta\rangle$: computed explicitly, giving signature $(1,2)$ with a negative-definite primitive part, matching the classical expectation in the toy case. (PROVED, toy model only; real/integer realizability (G-125.A) and persistence of the signature in general (G-125.B) left as explicit gaps)
- Whether a genuine Hodge-index / Kähler-package theorem holds for the (infinite-dimensional, tropical) square: assessed against the Adiprasito–Huh–Katz combinatorial Kähler package (which requires finite rank) and against the Babaee–Huh counterexample (a tropical surface in $\mathbb R^4$ whose intersection form has the wrong Hodge-index signature). The infinite dimension of the square blocks AHK's method, and there is no certificate ruling out a Babaee–Huh-type failure. (OPEN — "undeterminable," with current bias toward circular/unproved rather than attainable)
- Overall verdict: today only a weaker, RH-circular form of positivity (NC2-B) is available; the genuine, non-circular Hodge-index theorem for the square requires two theorems that do not yet exist (the intersection form itself, and an external infinite-dimensional matroidal/Lefschetz theorem excluding Babaee–Huh-type counterexamples). (NO-GO for closure at this stage, precise obstruction isolated)

## Documents
- `125-construction-of-the-intersection-form.md`: tropical intersection-form construction on the square; explicit toy-model Gram matrix and signature computation; gaps G-125.A (real/integer realizability) and G-125.B (signature persistence).
- `126-hodge-index-on-the-square-attainable.md`: analysis of whether a genuine Kähler package (Hodge index) is attainable for the tropical square, via the AHK and Babaee–Huh literature; verdict of indeterminacy with a circularity bias.

## Relation to other phases
Directly continues Phase 40 (G1/G2 identification). The unresolved question of where positivity could come from (continuous flow vs. static structure) is picked up in Phase 42 (dynamical Hodge theory).
