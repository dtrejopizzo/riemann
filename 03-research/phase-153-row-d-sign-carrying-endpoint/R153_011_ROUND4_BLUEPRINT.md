# R153.011 — Blueprint, round 4: the decay law of the sign in the certified window

* Everything inside `T ≤ log 2`; FATAL-safe by construction.*

## 0. Corpus facts that bind this round (read them first)

- **D.133** `03-research/phase-114-closing-the-four-rows/114_d_133_THRESHOLD_HADAMARD_CAPACITY_AUDIT.md`: exact right-Hadamard
  formula for `T = T_N + δ` after dilation to `(−1,1)`: Gamma shape derivative + transport derivative of each earlier contact +
  rank-two endpoint form for the contact born at `N`, `−(2w_N/T_N)(f̄(−1)g(1)+f̄(1)g(−1))`, + derivative of the two-Tate projection.
  Verdict there: rigorous on smooth vectors, **not** a bounded derivative on the Gamma form domain; the crossing form has no
  uniform sign; "no uniform signed Hadamard induction follows"; short-cell positivity needs a non-perturbative capacity estimate.
  **Do not rebuild the formula; do not attempt a signed induction.**
- **Doc 143** `03-research/phase-46-audit-and-attacks/143-attack-on-problem-136-a-quantitative-localized.md`: `λ_min` of the localized Weil form is the
  Riesz (Ingham) lower bound of `{e^{iγx}}` on the window; uniform module ⟺ vertical repulsion LP-143; module computable from
  zeros, not from primes (§4.4). Our object is the *global* window `P_T`, where the relevant gap is the origin gap `(−γ_1, γ_1)`,
  `γ_1 = 14.1347…`, not Lehmer pairs — say so and keep the distinction.
- **W4** (phase 118) §4: whether `lam_min_norm → 0⁺` or to a positive limit was left open (different normalisation).
- Phase 153 rounds 1–3: `λ_min(A_{log 2}|P_T) ∈ (0, 1.05·10⁻⁷]`; Theorem A; `T*(a) ≈ 0.624 + 0.0268·log(1/a)`;
  parity blocks and Hellmann–Feynman in `b` (R153_008); mesh-free spectral assembly `scripts/audit/aud_spectral.py`.

## 1. The question

Let `λ(T) := λ_min(A_T|P_T)` (L² Rayleigh normalisation) and `c(T) := −d log λ/dT`. Determine `λ(T)` on
`T ∈ [0.30, log 2]` and `c(T)`, and confront with three independent predictions:

(P-Slepian) Under RH the symbol of `A_∞` is the zero measure, with no mass on `(−γ_1, γ_1)`. A function of `P_T` whose transform
concentrates in the origin gap leaks like the first Slepian eigenvalue with parameter `c_S = γ_1 T`: predicts `λ(T) ≍ poly(T)·e^{−2γ_1 T}`,
i.e. `c(T) → 2γ_1 ≈ 28.3`. Derive the prediction properly (Slepian/Landau–Widom asymptotics `1−λ_0(c) ~ 4√π √c e^{−2c}`, with the
zero-density weight near `γ_1` and the two moment constraints), label it DIAGNOSTIC/heuristic, and note that A_T is computed
unconditionally from Gamma + primes (no RH used in the computation; RH only motivates the prediction).

(P-Xi) Theorem A to second order: `A_T^{(a)} = 2A_T + a²·D_T + O(a⁴)`, `D_T = [t,[t,A_T]]`: prime weights `× (log n)²`,
archimedean multiplier `−g_Γ''(τ)`, polar/moment part to be derived. Prove this expansion (PROVED) with the exact form of `D_T`.
Then `T*(a)` satisfies `2λ(T*) ≈ −a²⟨D F,F⟩` so `T*(a) = const + (2/c)·log(1/a)`: the measured slope `0.0268` predicts `c ≈ 75`.
Check: compute `⟨D_T F_T, F_T⟩` at the minimiser and verify the relation `2λ(T*(a)) = −a²⟨D F,F⟩ (1+o(1))` numerically for small `a`
(`a = 0.001, 0.005, 0.01`). Resolve the discrepancy 28 vs 75: which is right, and why (is the minimiser of `A_T` NOT the
minimiser of the Ξ_a form? is `T ≤ log 2` pre-asymptotic? is the moment constraint changing the gap?).

(P-Rate) Hellmann–Feynman at the minimiser (simple eigenvalue in its parity block, away from thresholds): `dλ/dT` as a boundary
functional of `F_T`, using D.133's formula with `f = g = F_T`. Determine the boundary behaviour of the minimiser: exponent `α`
in `F_T(t) ~ C (T−|t|)^α` near `±T` (DIAGNOSTIC-NUMERIC from the spectral minimiser; and an analytic argument from the
`log|τ|` growth of the symbol — which Sobolev regularity does the form domain impose at the boundary, and does point evaluation
of `F_T` exist?). If `F_T(±T) = 0`, the rank-two contact term vanishes at first order and the rate is driven by the Gamma shape
derivative and transport terms only: compute each term at `T ∈ {0.60, 0.65, 0.69}` and compare their sum with the measured `c(T)·λ(T)`.
State exactly how D.133's obstruction (unboundedness of point evaluation) is or is not bypassed by evaluating at the minimiser.

## 2. Deliverables

`R153_012_ROUND4_DECAY_LAW.md` (≤ 4000 words): (i) table `λ(T), c(T)` on ≥ 12 values with K-refinement (K = 160, 240, 320) and
stated precision (λ is `~10⁻⁷` at the right end: state how many digits are trustworthy); (ii) the parity block in which the minimiser
lives at each `T`; (iii) the three confrontations with verdicts; (iv) Theorem (PROVED): second-order expansion of `A_T^{(a)}`;
(v) the boundary exponent and the term-by-term rate; (vi) honest statement of what a bound `c(T) ≤ c_0` would mean (a restatement of
RH with rate; Doc 143 says its module is zero-computable) and whether anything found here is prime-computable. Scripts in
`scripts/round4/`. Labels PROVED / RESTATEMENT / DIAGNOSTIC-NUMERIC / OPEN / WITHDRAWN; corpus-check lines; FATAL rule; no sign for
ζ beyond `log 2`.
