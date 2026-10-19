# Phase 20 — the zero–ω bridge question

Phase 19 showed that the mean behavior of ω(n)-statistics (the Keating-Snaith
exponent k² and constant C_k) is a zero-free Poisson invariant. Phase 20 asks
whether objects beyond the mean — fluctuations, correlations, short-interval
statistics of ω(n) — encode any information about the location of the zeros
of ζ, following the advisor's ranked list of four candidate routes (C, A, B,
D), starting with route C (large-deviation rigidity).

## Results
- Step 0 (Dirichlet series analysis of q^ω(n)): the series F_q(s) factors as
  ζ(s)·∏_p(1+(q-1)p^{-s}); the zeros of ζ are **zeros**, not poles, of F_q,
  so the Perron formula for M_k(N) does not pick up residues at the
  nontrivial zeros — M_k is a sum of positive terms and cannot oscillate.
  **PROVED**.
- Theorem T1: the ω-weighted Mangoldt sum Ψ_q(x) = Σ_{n≤x} q^ω(n)Λ(n) reduces
  exactly to q·ψ(x), a classical reformulation with no new information.
  **PROVED** (classified as not a genuinely new object).
- Correction: an initially proposed obstacle (Chowla-Elliott, "wall W4") for
  the convergence rate of the pair-correlation ratio C_k(h,N)/M_k(N)² is
  withdrawn as misidentified; the real obstacle is the classical rate of the
  prime number theorem in arithmetic progressions, which is of the same
  classical type as RH.
- T4 / T4.1: an explicit error formula for C_k(h,N)/M_k(N)², proved
  equivalent in rate to the classical arithmetic-progression analogue of
  RH (rate O(N^{-½+ε})). **PROVED**.
- M_k/M_1^{k²} → C_k with error O(1/log N), unconditional. **PROVED** (new).
- Theorem T5: positivity of q^ω(n) (q ≥ 1, no sign changes) structurally
  prevents any algebraic cancellation that could remove the zero-dependent
  term from the correlation error, unlike signed multiplicative functions
  (μ, λ) where sign alternation permits such cancellation. **PROVED**.
- Conclusion: the search for an "arithmetic resonance" inside the positive
  ω-class that evades the classical zero-dependent error bound fails,
  definitively, for this class. The one remaining open question is purely
  quantitative (finer upper bounds on the error, not a qualitative escape).
  **OPEN** (quantitative only).

## Documents
- `00-PHASE20-DESIGN.md` — design document setting out the four candidate
  routes (C, A, B, D) and the falsifiable Hypothesis C.
- `00b-step-0-analysis-of-the-dirichlet-series.md` — Euler product / Selberg-
  Delange factorization of F_q(s) = Σ q^ω(n)/n^s.
- `01-proof-explicit-formula-omega.md` — Theorem T1 and the identification
  (later corrected) of the governing obstacle.
- `02-proof-error-correlation.md` — correction of the W4 misidentification,
  the explicit error formula (T4/T4.1), the unconditional M_k asymptotic,
  and the structural positivity-blocks-cancellation theorem (T5).
- `experiments/phase20_fluctuation_analysis.py` — fluctuation-amplitude
  numerical check motivating the design.

## Relation to other phases
Direct continuation of phase 19 (forward flow from primes to ω-statistics);
closes the bridge question negatively for the positive ω-class (no escape
from the classical zero-dependent obstacle), leaving only a quantitative
residual question open.
