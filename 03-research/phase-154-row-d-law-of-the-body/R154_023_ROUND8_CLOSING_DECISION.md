# R154.023 — Closing decision, round 8 (the clustering falsifier) and state of phase 154.

## 1. Round 8 (R154_022, DIAGNOSTIC-NUMERIC, one process, 63 s)
Clustered atoms on `[2T, 2T+1.98]` (175 atoms) vs matched control (175 atoms on `2T/10` spacing to `u ≈ 21.3`) at `T = 0.58`:
true minima `−0.900` vs `−0.224`; F1 tail slack `0.600` vs `0.096` (vs `0.018` at `M = 24`). **Clustering REFUTED** (deficit 4× worse).
Independent finding: **the tail lemma's conservatism is the binding object**; it scales with the period of `ν̂`. Nothing certified.

## 2. State of the construction after rounds 1–8
- Standing theorems: A, W, O, D1, Lemmas D2.1/D2.3/F1, Theorem C(½log3) with `c = 8.8577·10⁻⁵` (F3-verified). Identities E, P; Theorem K
  as a support bound; refutation of the incommensurability hypothesis.
- The staircase past `½log3` is blocked by **two analytic problems**, both pure mathematics and both OPEN:
  (P154.7) **the tail problem**: certify `Ψ_T + ν̂ ≥ c` on `[τ₁, ∞)` without worst-casing `ν̂` by `−ρ` — the slack is `10²`–`10⁴` times the
  targets and grows with the period; needs either a non-periodic `ν` with an analytically controlled tail, or a sharper lemma using
  the joint structure of `ν̂` and the prime term (their frequencies are incommensurable, so no common period exists);
  (P154.8) **mass-vs-value** (R154_020): the exchange between relaxed-primal mass outside `[−τ₁,τ₁]` and the certificate value is
  logarithmic, `R ≳ τ₁e^{B/ε}`; without a better lemma no rate theorem exists and the atom budget cannot be predicted.
- The uniform route (all `T`) is closed by the doubly exponential growth of `τ₁(T)` (`≍ 2πe^{2S_T}`): the certificate class must grow with it.

## 3. Decision
Round 8 closed; the clustered-atom line closed. Phase 154 remains open only on (P154.7)/(P154.8) as pure-mathematics problems; no further
LP or B&B work is authorised until one of them is solved on paper. The phase's deliverables of record are R154_012 (as amended),
R154_021 and this document.
