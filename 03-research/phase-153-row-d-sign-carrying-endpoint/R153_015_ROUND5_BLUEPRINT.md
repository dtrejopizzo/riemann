# R153.015 — Lead blueprint, round 5: construct Φ_N — the symbol-level payment and a conceptual proof of the endpoint

*Lead: Fable 5.1, 2026-09-19. Owner: "no lo enuncies, construilo".*

## 0. The construction to be carried out

On `P_T`, `⟨A_T F,F⟩ = (2π)^{-1}∫ σ_T(τ)|F̂(τ)|² dτ` with the **truncated Weil symbol**
`σ_T(τ) := g_Γ(τ) − m_0 − 2Σ_{n<e^{2T}} w_n cos(τ log n)`, `w_n = Λ(n)/√n` (state and prove the identity with the exact
normalisation of `F̂` and of `g_Γ`; the polar part is absent on `P_T`). Everything in `σ_T` is prime-computable.
Facts to establish: `σ_T(0) = −m_0 − 2Σw_n` (`≈ −7.6` at `T = log 2`); `g_Γ − m_0` alone is negative for `|τ| < τ_0 ≈ 6.3`;
the prime terms are positive exactly where `cos(τ log n) < 0`; for `T = log 2` the two primes are simultaneously positive on
`τ ∈ (π/(2 log 2), 3π/(2 log 3)) ≈ (2.27, 4.29)` and make `σ_T > 0` there although `g_Γ − m_0 < 0`. So the negative set
`N_T := {σ_T < 0}` at `log 2` is a neighbourhood of `0` plus whatever else the computation shows. **Φ_2, Φ_3 := the prime bands**:
`Φ_n(τ) = −2w_n cos(τ log n)`, and "the primes pay Gamma's deficit" means `∫_{N_T^c} σ_T|F̂|² ≥ ∫_{N_T}|σ_T||F̂|²` on `P_T`.

## 1. Corpus check first (mandatory, record hits)

Paper 42 `main.tex` ≈ lines 6330–6420 (deficit window `Ω_Γ`, `g_Γ(τ_Γ) = 1`, weights `w_±`, band coherence with width `log(3/2)`);
phase 60/61 `RH-PROOF-PAPER.md` (archimedean symbol `Ω̃(t)`, prime symbol `D_λ(t)`, band-limited `E_λ`) and its no-go;
phase 46 Doc 142 (deficit `Ω(0) − B_S`, truncation identity) and Doc 143; phase 106_16 (Slepian budget); phase 36 Doc 108
("dominación arquimediana y ceguera son el mismo fenómeno"). State precisely what of §0 is already there and what is new.
Expected: the symbol picture exists for *other* purposes (leakage outputs, spectral models); a symbol-plus-uncertainty proof
of `A_{log 2} ≥ 0` on `P_T` does not.

## 2. Tasks

(T1) **Compute `σ_T` and `N_T`** for `T ∈ {½log3, log 2}` (and `½log5, ½log7` for orientation): zeros of `σ_T`, depth
`D_T = max_{N_T}|σ_T|`, floor `ε_T = min_{N_T^c ∩ [0,Ω]} σ_T` on a stated range, and the large-`τ` behaviour (`g_Γ ~ log τ`,
prime terms bounded, so `σ_T ≥ ε > 0` for `τ ≥ τ_1` — prove it with explicit `τ_1`). Plot-free: tables. `PROVED` where analytic.

(T2) **The uncertainty inequality.** For `F ∈ P_T` (support `[−T,T]`, `F̂(±i/2) = 0`), bound the spectral mass in the well:
`∫_{|τ|<τ_*}|F̂|² ≤ θ(T,τ_*)‖F‖²`. Routes: (a) Bernstein/Paley–Wiener: `F̂` entire of type `T`, `|F̂(τ)| ≤ e^{T/2}‖F‖_1`… too weak; (b)
the two moment zeros: `F̂(τ) = (τ² + ¼)·H(τ)`? no — vanishing at `±i/2` gives `F̂(τ) = (τ²+¼)G(τ)` with `G` entire of type `T`;
then `|F̂|² = (τ²+¼)²|G|²` suppresses low frequencies by `(τ²+¼)²/(…)`: quantify via Parseval on `G` (which is the transform of the
"double primitive" of `F`, cf. Paper 42 Lemma "compact polar potential": `F = (−d²/dt² + ¼)G_0`, `G_0` compactly supported);
(c) prolate/Slepian concentration bound for type `T` in `[−τ_*, τ_*]`, `θ ≤ λ_0(Tτ_*)`. Prove the best `θ` you can rigorously,
compare with the numerical maximal concentration of `P_T` functions (DIAGNOSTIC).

(T3) **Close the endpoint by hand.** The positivity of `A_T` on `P_T` follows if `ε_T(1−θ) ≥ D_T θ` (with the piecewise refinement:
split `N_T^c` into bands with their own floors, and `N_T` into sub-wells). Attempt this at `T = ½log3` first, then `T = log 2`.
If it closes: a **conceptual, mesh-free proof** of Paper 42's certified endpoint(s), `PROVED`, and the explicit display of how
`Φ_2, Φ_3` pay. If it does not close: compute the exact shortfall (how much concentration in the well the actual minimiser has vs
the bound `θ`), and say what finer input would close it (e.g. the `(τ²+¼)²` suppression combined with prolate concentration).

(T4) **The uniform question, precisely.** Write the statement "for every `T`, `∫σ_T|F̂|² ≥ 0` on `P_T`" and show how `N_T` and
`D_T` evolve with `T` (orientation at `½log5, ½log7`); note the size `Σw_n ~ 2e^{T}` of the well at `τ = 0` versus the moment
suppression `(τ²+¼)²` and the prolate bound — where does the hand argument die, and does it die for an analytic reason
(uncertainty) or an arithmetic one (the bands of `cos(τ log n)` stop aligning)? `DIAGNOSTIC` unless proved.

(T5) **Falsifier check.** Same construction for `Ξ_a` (`σ_T^{(a)}` with weights `w_n(n^a+n^{−a})` and doubled shifted Gamma):
does the hand argument at `log 2` fail for `a = 0.45` (as it must, since the form is negative there)? Where exactly — deeper well,
or four moment zeros not suppressing enough? This ties Φ to Theorem A.

## 3. Rules
Labels PROVED / RESTATEMENT / DIAGNOSTIC-NUMERIC / OPEN; FATAL rule; no sign for `ζ` beyond `T ≤ log 2` (the hand proof, if it
works, only re-proves what is certified — that is its point); corpus-check lines; scripts `scripts/round5/`.
Deliverable `R153_016_ROUND5_PHI_CONSTRUCTION.md` (≤ 4000 words), complete proofs for PROVED items.
