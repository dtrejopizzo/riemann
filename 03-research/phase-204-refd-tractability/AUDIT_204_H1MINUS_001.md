# AUDIT_204_H1MINUS_001 —

Phase 204. Sources: CALIB_R4_001.md and `CALIB_001_data/WT_H1.py`,
`WT_H1_interval.json` (phase 202); P47 lem:K/eq:m (l.363), thm:S(iii), thm:A/eq:Aform (l.412), lem:monoT, prop:WT (l.4358).

## Verdict: **H1⁻ PROVED** for ζ: n₋(𝔄_ev(T)) ≥ 1 for all T ≥ 0.12 (certified by intervals at T₀ = 0.12).

## (1) Closed formula for c_χ — CORRECT
χ_ev = cosh(t/2)·1_{[−T,T]} (unnormalized, convention of prop:WT / subsec:conv). For 0 ≤ u ≤ 2T,
c(u) = ∫_{−T}^{T−u} cosh(t/2)cosh((t+u)/2)dt = ½∫[cosh(t+u/2) + cosh(u/2)]dt = ½[2sinh(T−u/2) + (2T−u)cosh(u/2)]
= sinh(T−u/2) + (T−u/2)cosh(u/2); c ≡ 0 for u ≥ 2T. Control: c(0) = sinh T + T = ∫cosh²(t/2) = ‖χ_ev‖². ✓
χ_ev is in the form domain: the jump at ±T gives |χ̂| = O(1/τ) and ∫log(2+|τ|)τ^{−2} < ∞.

## (2) The comb only helps — CORRECT
eq:Aform: 𝔞_T(F) = C₀‖F‖² + Lév(c_F) − Σ_{n∈𝒩_T} v_n c_F(log n), with v_n = 2Λ(n)/√n > 0. For u ∈ (0,2T) both summands of c
are > 0, so the comb term is ≤ 0 and the archimedean part alone suffices for the sign. The script also subtracts exactly the
n = 2 term when T > ½log2 (applies at T = 0.5 and ½log3; n = 3 does not enter at ½log3 because 𝒩_T requires log n < 2T).
At T₀ = 0.12 there is no comb.

## (3) Implementation, the [0, 10⁻¹²] piece and the tail — CORRECT
- **Constants against P47.** C₀ = ψ(¼) − log π = −γ − π/2 − 3log2 − log π ✓ (script). K = 1/(2sinh(u/2)) + 1/(2cosh(u/2)) ✓
  (lem:K).
- **Tail.** Lév(c) = ∫_0^{2T}(c₀ − c)K + c₀∫_{2T}^∞K; thm:S(iii) gives ∫_{2T}^∞K = log coth(T/2) + π − 2arctan e^T, and the
  script uses log coth(T/2) + 2arctan e^{−T}, identical (arctan x + arctan(1/x) = π/2). Convergence: K = O(e^{−u/2}); the
  tail is closed, not truncated.
- **Piece [0, ε].** 0 ≤ (c₀ − c(u))K(u) ≤ sup|c′|·uK(u), and uK(u) = u/(2sinh(u/2)) + u/(2cosh(u/2)) ≤ 1 + u/2; so the piece
  lies in [0, sup|c′|·ε(1+ε/4)]. With |c′(u)| ≤ ½cosh(T−u/2) + ½cosh(u/2) + ½(T−u/2)sinh(u/2) ≤ cosh T + T + 1, the script's
  symmetric ball arb(0, ε(1+ε/2)(cosh T + T + 1)) contains it (it is more generous). ≈ 2·10⁻¹², negligible against the
  2–3.5·10⁻⁴ radius.
- **Rest of the integral.** Each subinterval is evaluated with U = a ball containing the subinterval; arb encloses the
  range of the integrand and w·range encloses the integral. Rigorous enclosure at 120 bits. ✓
- **Order of magnitude (hand check, T = 0.12):** c₀ ≈ 0.2403; tail/c₀ ≈ log coth 0.06 + 2arctan e^{−0.12} ≈ 2.815 + 1.451;
  the piece [0, 0.24] contributes ≈ 1 (nearly triangular autocorrelation against K ≈ 1/u); total ≈ −5.372 + 5.27 ≈ −0.1,
  compatible with the certified [−0.047 ± 3.5·10⁻⁴]. ✓ (As T → 0 the value is ≈ C₀ + log(1/T) + O(1) > 0: the threshold is
  near 0.1; T₀ = 0.12 is the certified lower bound, nothing is claimed for T < 0.12.)

## (4) Passage to n₋(𝔄_ev(T)) ≥ 1 for T ≥ T₀ — CORRECT
χ_{ev,T} ≠ Eχ_{ev,T₀}, but that is not needed: E (zero extension) maps 𝒟^ev_{T₀} into 𝒟^ev_T, preserves parity, norm,
autocorrelation, and the new contacts (log n ≥ 2T₀) do not see c_{Eχ} (proof of lem:monoT). Then
𝔞_T(Eχ_{ev,T₀}) = 𝔞_{T₀}(χ_{ev,T₀}) < 0 and, by min-max over the semibounded operator with compact resolvent,
n₋(𝔄_ev(T)) ≥ 1. ✓

## Scope and consequence
For every T ≥ 0.12 where the hypotheses of prop:WT hold (0 ∉ spec 𝔄_ev, q_ev ≠ 0), the branch "n₋(𝔄) = 0, q > −½" is
excluded, and λ^W_{T,ev} > 0 ⟺ n₋(𝔄_ev) = 1 ∧ q_ev < −½. What is proved is n₋ ≥ 1, not n₋ = 1; equality is part of the
condition. The values T₀ = 0.5 and ½log3 are redundant (implied by 0.12) but serve as controls. Label: **PROVED**
(computer-assisted, intervals).
Note: the numbers from CALIB_R4 §1 (q_ev + ½, M = 30 inertias) remain NUMERICAL and are not part of H1⁻.

## Text for P47 (corollary of prop:WT)
> **Corollary.** For $\zeta$ and every $T\ge0.12$, $n_-(\mathfrak A_{\mathrm{ev}})\ge1$: interval arithmetic gives $\mathfrak a_{0.12}(\chi_{\mathrm{ev}})/\|\chi_{\mathrm{ev}}\|^2\in[-0.047\pm3.5\cdot10^{-4}]$ via (eq:Aform), $c_\chi(u)=\sinh(T-\frac u2)+(T-\frac u2)\cosh\frac u2$ and Theorem S(iii), and extension by zero (Lemma monoT) carries this negative vector to every larger window. Hence, under the hypotheses of Proposition WT, the even sector has positive bottom if and only if $n_-(\mathfrak A_{\mathrm{ev}})=1$ and $q_{\mathrm{ev}}<-\frac12$.

## Index entry
- **AUDIT_204_H1MINUS_001:** H1⁻ PROVED (intervals, arb 120 bits): 𝔞_{T₀}(χ_ev) < 0 at T₀ = 0.12 ⇒ n₋(𝔄_ev(T)) ≥ 1 ∀T ≥ 0.12
  by zero extension. Formula for c_χ, constants (C₀, K, tail thm:S(iii)) and the [0,10⁻¹²] bound verified. Excludes the
  n₋ = 0 branch of prop:WT for ζ. Does not give n₋ = 1 nor the sign of q_ev + ½ (which remains NUMERICAL).
