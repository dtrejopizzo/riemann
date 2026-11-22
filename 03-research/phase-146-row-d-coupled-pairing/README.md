# Phase 146 — Row D: the degree form on `Z[Frob]` with a count interpretation

Option α, redefined after phase 145 (`R145_005` §3). Scope: **Q0 + Q1 only**, with Proposition D.42.5
printed and the two binding warnings carried (W-a: deliver the count, never the positivity; W-b: `g = 1` is
degenerate twice). Rounds 1–2 complete.

| file | contents |
|---|---|
| `R146_000_BLUEPRINT.md` | blueprint: the object, D.44 (Q0), D.45 (Q1, items 1–4), D.46, warnings, falsifier protocol |
| `CORPUS_CHECK_R146.md` | prior art for the "coupled pairing `J`" framing of α |
| `CORPUS_CHECK_R146b.md` | prior art for the redefined α: what is NEW, and that `Δ·Δ = −∞` is settled |
| `R146_001_ROUND1.md` | round 1 — D.44, D.45, D.46, corpus check, paper-facing, open items. **Repaired in place**; every round-2 correction is marked `[R2: …]`. Read only together with `R146_003`. |
| `R146_002_AUDIT.md` | audit: **14 MAJOR, no FATAL**; FATAL screen passes; script clean |
| `R146_003_ROUND2.md` | **round 2** — finding-by-finding disposition (M1–M14, m1–m6), **§D.47 the single-prime tower** (the new work), §D.48 (`Sh_Z` restated), §D.49 (synthesis and the phase-147 recommendation), paper-facing revision, open items, §Label |
| `scripts/cosh_test_cmn.py` | round 1 (`--fast`): cosh-test margins on `c_{m,n}`; the rank-2 would-be norm form; the indefiniteness witness |
| `scripts/tower_gram.py` | round 2 (`--fast`): tower thresholds `τ_±(p)`, finite-section eigenvalues, the `Ξ_a` threshold table, the model-vs-arithmetic kernel comparison, the `ℓ=2` over-determination, the two degree normalizations |

## Where the phase stands after round 2

**Q0** — the Euler product does determine a would-be rank-2 form `m²+(ℓ+1−Λ(ℓ))mn+ℓn²`, but this is a
`DEFINITION`, not a determination: the underlying dictionary is over-determined and inconsistent at every
single prime (`N_2 = 3.678` from the order vs `Λ(4) = 0.693` from the dictionary), and the round-1 "Hasse
failure from `ℓ ≥ 7`" is `HEURISTIC` — it is an artifact of the normalization `d_n = n` (with
`d_n = log n` the test passes at every prime) and moves with the chart constant.

**Q1** — a finite symmetric form on `M = Z⟨Frob_n⟩` **exists** and is unique given the diagonal; it is
degenerate against the count axiom and **indefinite** (one line: `Q_0 = Φ(0)Φ(1) − ½xᵀLx` is a product of
two independent linear functionals minus a zero-diagonal matrix). It is **not** a count on sums.

**The round-2 result — the single-prime tower.** From Paper 44 Thm 8bis.1b the Frobenius diagonal is
*computed*, not assumed: the archimedean divergence cancels exactly in `δ_m − δ_n`, the remainder is
supported on `P(m) △ P(n)`, and `δ_m = δ_n` exactly when `P(m) = P(n)`. On `{Frob_{p^k}}_{k≥1}` the
diagonal is therefore a single number and the chart constant a single positive factor, so the Gram is
`c_p(log p)[T(p^{−1/2}) + (τ_p−1)I]` with one real parameter. It is PSD iff `τ_p ≥ 2/(√p+1)`; the computed
diagonal is **negative**, so the tower form is **not** PSD at any chart, level, smearing or convention —
a computed negative, and a sharpening of Thm 8bis.4a. The `Ξ_a` weights move the threshold by `< 5·10⁻³`
and change no verdict: **A3 does not enter here either.** The model's tower kernel *grows* (`κ(k) ∼ q^{k/2}`)
where the arithmetic one *decays* (`(log p)p^{−k/2}`), and the missing block is named: the pure Frobenius
family carries no archimedean part (Cor 8bis.1d), while the model's `κ` is the whole kernel.

**Honest diagonal.** The form built here is Paper 47's `2ab − W` with the **zero sum deleted**; it is
zero-blind by construction, and every statement of §§D.44–D.47 is `Ξ_a`-uniform. Phase 146's deliverable is
a negative that does **not** separate `ξ` from the falsifier.

**Phase-147 target:** the same tower for object (B), `Frob ⋆ Δ^{rad}` (Paper 44 Thm 8bis.1e), which carries
the full kernel `W_{fin}+ω_∞` — not an imported archimedean model. No label proposed; no label changed.

## Other files in this folder

- `R146_004_CONFIRMATION.md` — Confirmation, phase 146 (final round).
- `R146_005_CLOSING_DECISION.md` — Closing decision, phase 146 (the degree form on `Z[Frob]` with a count interpretation).
