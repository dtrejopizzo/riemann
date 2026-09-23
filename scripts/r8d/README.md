# scripts/r8d — round 8d, the margin-decay bound (R155_055)

`r8d_margin_bound.py` — one script, runtime **5–13 s** depending on load (auditor measured 12.8 s; numpy/scipy/mpmath). Outputs `r8d_margin_bound.json`.

* (A) constants of Theorem 1: `γ₁⁴ ≥ 14.13⁴`, `21⁹`, the Rosser (1941, Thm 19, constant `1.588`, `t ≥ 2`) and
  Trudgian (2014) upper bounds for `N(t)` at `t = 21` (`4.06`, `4.73`), and the check that `N(t) ≤ (t/2π) log t`
  for `t ≥ 21` (slack `6.11` at `t = 21`, increasing). [Amended per R155_059: the first version used Backlund's
  constants under Rosser's name.]
* (B) the PROVED bound `B(T,k)` of Theorem 1 (memo eq. (3.1)), minimised over `k ≥ 5`, at the requested
  windows and beyond; the crossings `B = 1`, `B = 8.8577·10⁻⁵`, `B = 10⁻⁷`.
* (C) Corollary 1: `sup_{T≥1} ε_k` for `k = ⌈21T/e⌉`, the constant, and the check
  `min_k B(T,k) ≤ 4·10⁹ T e^{−15.449T}` on `T ∈ [1,40]` (ratio ≤ 0.7550).
* (D) DIAGNOSTIC only: the exact value `𝔞_T(F)/‖F‖²` of the *same* test function by quadrature of the
  symbol `σ_T` (digamma + comb, **no zeros**), compared with the PROVED bound (the proof loses 6.3–9.6
  orders of magnitude, see memo §3.4); and a cross-check of the explicit-formula normalisation of
  Lemma 2 against the zero sum over the first 60 zeros from `mpmath.zetazero` — **not an import of
  record**, proves nothing, agreement `10⁻⁵`–`10⁻⁶` relative at `T = 1, 1.5`; at `T = 2` the discrepancy is
  `2.1·10⁻³` (roundoff floor of the symbol quadrature; the `T = 2` ratio `≈ 8·10⁻¹⁵` is roundoff-limited).

Nothing in the memo's PROVED statements depends on (D).

**[Fix 2026-09-22 per `TEX_HOSTILE_REVIEW_R4` R4-1.]** Function `B`, line 61: the log-space rewrite used
`(k/(TH))^{2k}·H⁸`; correct is `H⁹` (`1 − p = 9 − 2k`), so every earlier scripted `B(T,k)` was `21×` too small.
Fixed and re-run (7.6 s); `r8d_margin_bound.json` regenerated. Corrected crossings: `B = 1` at `T = 1.430`,
`B = 8.8577·10⁻⁵` at `T = 2.054`, `B = 10⁻⁷` at `T = 2.506`; (C) worst ratio `0.7550 ≤ 1` (Corollary 1 survives);
(D) proved bounds `9.974·10⁵ / 6.574·10⁴ / 1.280·10⁴` at `½log3 / log 2 / 0.80`. Erratum in `R155_055`.
