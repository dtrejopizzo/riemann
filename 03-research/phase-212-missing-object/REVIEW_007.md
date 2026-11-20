# Review of round 7 (`ROUND_007_A.md`, `ROUND_007_B.md`, `ROUND_007_C.md`)

No candidate passes the gate. Global sign: OPEN. The lemmas marked PROVED that are
cited below were re-derived; the rest keep the label of the memo.

## R7-a. Contact bounds by potential (ROUND_007_A, Lemma 1.1 and Theorem 2.1)

- Lemma 1.1, re-derived: for `φ > 0`, `v F(t)F(s) = (v/2)[(φ(s)/φ(t))F(t)² + (φ(t)/φ(s))F(s)²] −
  (v/2)φ(t)φ(s)(F(t)/φ(t) − F(s)/φ(s))²`. It holds equally with pairings (`T < log p`) and with chains. If `φ`
  changes sign between orbits the potential is still `≥ 0`. PROVED.
- Theorem 2.1, re-derived: if each contact is bounded by a potential `V_p ≥ 0`, the remainder is
  `Arch − ∫ΣV_pF² ⪯ Arch`, which has negative bottom on `P_T` for `T` above the archimedean threshold
  (Paper 47 cor:Tarch, CITED; threshold in `[0.58, 0.60]`). The class dies before `0.60`, with any number
  of primes, any `φ_p`, `θ_p(t,s)` and `W_p(t)`. PROVED relative to the citation. Independent of the weight.
- Consequence: the hypothesis "pairing versus chain" does not explain the threshold `0.695–0.70` of class
  DIR, which does not belong to this class (its pieces keep the contact together with kernel energy).
- Equation for `ℓ`: top eigenvector of `Y₃ − Y₂` for the obstructing pair. PROVED in the discretization,
  ARGUED in the continuum. No formula while the pair is not solved. Circular as a prior rule (J3).

## R7-b. Stage predicates (ROUND_007_B, Lemmas 1 and 2)

- Lemma 1, re-derived: if `𝒫_k(Q)` is "`Q + R_k ∈ 𝒦`" with `𝒦` a convex cone and the step must hold for every
  `Q`, taking `Q = −R_k` gives `R_{k+1} − R_k − Π_n ∈ 𝒦`; the converse is the sum in the cone. The
  induction is a local splitting by contacts. PROVED.
- Lemma 2 (bounded inertia with uniform step): PROVED in finite dimension, ARGUED for the form.
- The six directions examined fall into closed entries (classification ARGUED): §O, L6, BARRIER_W_001,
  lem:degen and §P, R162_802 / R162_2701 / R5-d, P122_018, J3.
- Not excluded: history-dependent step with a stage datum given by its own formula. No object.

## R7-c. Product channel (ROUND_007_C)

- Lemma, re-derived: with `A(ξ) = Σ a_n n^{−1/2+iξ}`, `a_n` real and `g` real even,
  `Σ a_m a_n (mn)^{−1/2} g(log m − log n) = (1/2π)∫ĝ|A|²` and
  `Σ a_m a_n (mn)^{−1/2} g(log mn) = (1/2π)∫ĝ Re A²`. PROVED.
- The signed channel does not depend on the arithmetic; the arithmetic channel has no sign. Repetition of
  R161_034 and of K2–K3. Reading of the term that loses the sign at `c = 2`: ARGUED.
- Reopening: the one already written in R161_034 §0.

## What the round leaves standing

- NUMERICAL without formula: two-position splitting up to `T ≈ 0.695`; deficit of a square past the threshold.
- Above the archimedean threshold no piece that bounds the contacts from above works: the contacts
  must contribute positively in the negative directions of `Arch`.
