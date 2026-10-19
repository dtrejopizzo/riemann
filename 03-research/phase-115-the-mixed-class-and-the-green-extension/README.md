# Phase 115 — The mixed class and the Green extension

Phase 114 diagnosed row (d) as missing not an inequality but an object: for each test function f, a
perfect object M_f with derived contact reproducing the row-(b) prime family in cross form, periodic
cohomology scaling like B_nuc(f,f), a normalized determinant with the right metric exponent, and an
effectivity property. This phase tries to build that object (the "mixed lattice/Green extension"),
works through a sequence of axiom checks and no-go results, and ends by auditing five independently
produced external attempts at the same row-(d) programme.

## Results
- Axiom 1 (positivity of the normalized theta invariant), initially claimed to fail, is shown to actually hold once the zero-lattice case in negative degree is handled correctly; axioms 1 and 2 are proved. PROVED (after a retraction of the original negative claim).
- The mixed-class extension reduces, via Poisson summation, to one scalar condition: producing a lattice whose covolume matches (t²/2)B_nuc(f,f) + O(t); everything else (h⁰,h¹,h², all four axioms) then follows mechanically. PROVED (reduction).
- The needed mixed lattice cannot come from row (a)'s existing code; its covolume must be supplied from elsewhere. NO-GO (for the natural source), OPEN for an alternative source.
- A slack lemma and a prime-free window are identified; a semilocal route via shell decomposition is explored. PROVED/ARGUED pieces, not a full construction.
- Three claimed routes (Künneth reading, radix identification, a duality repair) are refuted by proof; one cross-check (previously non-generic) is shown to pass generically. NO-GO (three routes) / PROVED (the cross-check).
- The phase-derivative approach closes the dimensional gap in H but leaves the sign of the key quantity open; later, three independent arguments resolve the sign favorably, but the trace identity used to reach it turns out not to exist, and the correct intrinsic form shows the governing hypothesis (H) can only be asymptotic, not an exact identity at fixed λ. PROVED (sign, favorable) / NO-GO (exact trace identity) / revised to CONDITIONAL-ASYMPTOTIC (H).
- Audit of five external row-(d) attempts (v3–v7: Sonin bridge, threshold-defect induction, spectral transversality, conservative/scattering reconstruction, Rosati-metric routes), plus a sixth (v8, Sonin excursion): several individual true lemmas are recovered and recorded, but a general unitarity obstruction (Proposition 3) is proved that closes the entire family v6–v7 at once — any construction making the relevant scaling group unitary has already, in effect, assumed the zeros lie on the critical line, so unitarity cannot be the source of the needed positivity. PROVED (general obstruction) — NO-GO for the whole family of routes. v8 relocates the gap into a falsifiable coefficient, which is itself then falsified.
- Byproduct: a cheap, full-space computational falsifier for the overall target (n₋(A_T) ≥ 2 would refute the target) is identified as a leftover useful tool. OPEN (not run here).

## Documents
- `115_00_PHASE_115_PLAN.md` — the target object and inherited axioms from phase 114.
- `115_01`–`115_10` (+ `scripts/`) — the Green-term rank-cut, row-D architecture, literature comparison, theta construction, axiom proofs/corrections, the mixed-lattice obstruction, slack lemma, and semilocal route.
- `115_11`–`115_16` (+ `scripts/`) — the three refuted routes, gap measurement in H, the phase-derivative partial closure, eigenvalue-count question, and the sign/trace-identity resolution.
- `115_17_THE_EXTERNAL_ROSATI_ROUTE_AND_THE_UNITARITY_OBSTRUCTION.md` — full audit of five (plus one) externally produced row-(d) attempts, culminating in the general unitarity obstruction.

## Relation to other phases
Directly continues phase 114 (builds the object phase 114's closure note identified as missing); its general unitarity obstruction (115_17 Proposition 3) is intended as a standing filter for any future row-(d) construction route, inside or outside this programme.
