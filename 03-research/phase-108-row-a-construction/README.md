# Phase 108 — Row (a): the space over ℤ

The phase makes the global rational-function question for row (a) well posed on the DC quotient and
determines which category the descent forces, working through six stages: a zero-free corner
pairing, principal invariance, assembly of the correspondence functionals, the archimedean fibre,
whether the assembly is an intersection number, and (left open) the primitive inequality for row (d).
No definition is allowed to use a zero of ξ, a Li coefficient, or a sign/positive part extracted from
the Weil form.

## Results
- Character classification: nonzero continuous solutions of f(r/n)=χ(n)f(r) are exactly f=c·r^s, χ(n)=n^{-s} (log-periodic factor forced trivial). PROVED.
- Stage 1 bridge making principal invariance well posed, with the divergent constant contributing zero at every finite depth. PROVED.
- Stage 3 assembly: the correspondence functionals assemble to −ζ'/ζ(s). PROVED.
- Stage 4 operator form: det_reg(s−Θ) = c(s)Γ_R(s)^{-1}, c(s) derived not fitted. PROVED.
- Symmetrization collapse: ζ'/ζ(s)+ζ'/ζ(1−s) is elementary (cancels every pole at a zero of ξ); the symmetrized strip function Φ has exactly one simple zero in (0,1). PROVED.
- Embedding no-go: if RH holds, there is no isometric injection of the archimedean block into the corner form. PROVED (conditional statement about the construction, not about RH's truth).
- Stage 2 (principal invariance): FAILS — radical is spanned by point masses at the zeros of Φ. PROVED negative.
- Stage 5 (is the assembly an intersection number?): NO by both the naive and the regularized route; three independent obstructions found. PROVED negative (NO-GO).
- Stage 4 geometry: G3 proved unconditionally; two originally-reported results G2, G4 were found to be circular/contentless definitions-in-disguise, with no verifier able to detect this; recorded as a limitation of the verification method. RETRACTED / NO-GO.
- Overall a/b/c/d ledger over ℤ: unchanged at 0 of 4; row (a) has a space, divisor theory and pairing but no intersection number. OPEN (`ROW_A_STATUS = partial`).

## Documents
- `108_00_PHASE_108_PLAN.md` — mission, inherited state, source rule.
- `108_99_PHASE_108_SUMMARY.md` — full stage-by-stage verdict table and the through-line explanation.
- `108_01`–`108_55`, `108_90`–`108_91` (paired `.md`/`.py` theorem + verifier files) — the individual stage results listed above, in numeric order.

## Relation to other phases
Builds on phase-107 results (character/homomorphism classification, corner pairing, local principal subspace); hands prohibitions and entry conditions for a Stage 6 "primitive inequality" (row d) to later phases, and leaves open whether a non-symmetrizing route to Stage 1 well-posedness exists.
