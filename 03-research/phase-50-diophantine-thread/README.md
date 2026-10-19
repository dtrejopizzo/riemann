# Phase 50 — The Diophantine thread: does ℚ-independence of {log p} cross the positivity wall?

The phase asks whether a specific structural input — the ℚ-linear independence of {log p},
equivalently the completeness of the system {p^{iτ}} — can serve as the transversality certificate
that collapses the average→individual (individuation) defect of the Weil form, without reintroducing
the Riemann Hypothesis as a hidden premise. This was the only crack left open by the preceding
phase's no-go theorem (GAP-157.A), and here it is first formalized constructively and then attacked
adversarially.

## Results
- Exact formalization of the Diophantine input and three nested equivalent statements about it,
  with their unconditional equivalences proved: PROVED (Doc 158, §1).
- Diagnosis that the thread, if it collapses to anything, collapses into either a disguised form of
  Nyman–Beurling or a statement confined to the value side (Bohr/Voronin): ARGUED (Doc 158).
- Adversarial destruction (Doc 159): the claim that completeness of {p^{iτ}} is an RH-free crossing
  of the average→individual wall is attacked via three independent routes; the document separates
  two readings of "completeness" that the hopeful claim conflates and evaluates each: NO-GO (the
  claim as stated is refuted/killed on the routes examined; see Doc 159 for the precise residual, if
  any, left open).

## Documents
- `158-diophantine-thread-is-the-linear-independence.md` — constructive formalization of the Diophantine thread and its candidate role as transversality certificate.
- `159-destroyer-of-the-diophantine-thread.md` — adversarial document attempting to kill the thread via three routes.

## Relation to other phases
Builds on the no-go catalog of the phase that produced GAP-157.A and on Doc 112 (Bagchi's limit
theorem, Kronecker–Weyl on {log p}); its outcome (and any surviving gap) feeds `phase-51-functor-construction`.
