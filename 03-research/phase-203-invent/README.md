# Phase 203 — variation of the extremal with respect to the comb; three proper objects

The phase corrects an earlier numerical premise (a claimed positive "cosh
defect" turns out to be an artifact of comparing ζ's radical datum to a
different comb, not a genuine positivity signal), then asks whether varying
the extremal minimizer g* with respect to the arithmetic comb a(n) — via
Danskin's theorem and three newly proposed auxiliary objects — can supply a
lower bound certifying λ_A(T) > 0 at the window T = ½log15.

## Results
- Correction of the starting datum: the retracted "+0.09e-70" cosh-defect
  reading is refuted; the real interior pairing between g* and a perturbed
  comb (Epstein, Davenport-Heilbronn) is O(1) (≈ +0.063), dominated by the
  erasure of the prime 2, not by a genuine cosh-defect mechanism. **PROVED**
  (one-line observation plus numerical confirmation).
- Danskin differentiability of λ_A(a) in the comb a, and the inequality
  λ_A(a') ≤ λ_A(a) − Σ(a'(n)-a(n))s_n(a) (Proposition 2.1). **PROVED**
  (conditional on minimizer uniqueness/gap for the full class P_T, proved
  unconditionally for the μ=15 truncated class).
- Theorem 2.3: concavity of λ_A in the comb gives only upper bounds; the
  only route to a lower bound is a convex combination of known values
  (already registered elsewhere as "convex decomposition"). **PROVED
  NO-GO** as a source of sign.
- Object I (cone of Euler defects over a common near-kernel of three comb
  families): dies immediately — the extremal g* is not in the near-kernel
  for any small ε, and the residual defect is the already-registered
  "erase a prime" (a_P) mechanism. **NO-GO**.
- Object II (comb-indexed radical defect R_X): gives a non-uniform identity
  but carries no sign for ζ. **NO-GO** as a sign source; retained as a
  calibration tool.
- Object III (hierarchical contact book: the ladder of c_{g*}(log n) values
  and partial residues W^{(N)} across the 13 contacts up to n=14): the only
  surviving object, reduced to a finite, numerically decidable lemma
  (L-III.1) with an explicit death criterion (any negative partial residue,
  or DH/Beurling perturbations reproducing the same sign pattern). **OPEN**.
- Overall ranking: III ≫ II > I. Row D remains **OPEN**; the target lemma
  L'♯ remains **OPEN**.

## Documents
- `AUDIT_203_001.md` — audit of `INVENT_001.md`: confirms the
  Danskin/Theorem 2.3 results with two technical corrections, confirms the
  cΛ-line consistency check (no contradiction found), and confirms Objects
  I–III verdicts.
- `INVENT_001.md` — main construction: correction of the starting datum,
  the Danskin variation theory (§2), and the three proposed objects (§3–5)
  with their verdicts and the final ranking/request list for further
  numerical calibration (§7–8).

## Relation to other phases
Builds on and cites CALIB_R1/R2, MORI15_EXTREMAL, LEMMA_13.1, CPOS_CLASS,
and P47's thm:ext-half / cor:Tarch; the surviving Object III (hierarchical
contact book) is handed off with concrete finite computations (P203.1–3)
requested of a later calibration phase.
