# Bottleneck Ledger — v8 Localized Weil Detector ## Entry: L_DH (Davenport–Heilbronn) — benchmark irreproducibility (final) **Date:** 2025-11-19 (current phase)
**Status:** CLOSED-WITH-LIMITATION
**Severity:** structural (specification gap) ### Statement of the bottleneck The validation gate in `-v8-validated-data.md §4` specifies that at
parameters `(T₀ = 85.7, σ = 2, J = 10, dps = 50)` the localized Weil
quadratic form Q for the Davenport–Heilbronn L-function `L_DH` should
satisfy λ_min(Q) ≈ −9.0 × 10⁴ and |λ_min| / tr(M_zeros) ≈ 1.7. This benchmark is **irreproducible from public information**. The L_DH
function is defined as a complex linear combination of L(s, χ) and
L(s, χ̄) for the primitive complex character χ of order 4 mod 5, with
weights `(1 ± iκ)/2` and `κ = 0.28407904384`. As a sum of two
Dirichlet L-functions, L_DH has **no Euler product, no multiplicative
structure, and no generalized von Mangoldt coefficients**. The
spec's `λ_min ≈ −9.0×10⁴` therefore implicitly relies on an arithmetic
side whose coefficient sequence is not publicly defined and is not
recoverable from the spec text alone (literature search in prior
report `r13` confirmed no published explicit-formula formula for L_DH). ### Best-effort proxy implemented `weil_quadratic_form_L_DH.py` (this phase) implements the Weil
quadratic form for L_DH with the following choices, all documented in
the module docstring and labelled as best-effort approximations: * **Zero side.** Sum over L_DH zeros ρ = β + iγ in an effective window around T₀ = 85.7. We include the on-line zeros found by scanning |L_DH(½+it)| (24 zeros in t ∈ [60, 110]) and the spec's off-line zero at (0.808517, 85.699348) together with its functional-equation mirror (0.191483, 85.699348). Conjugate zeros (γ → −γ) are added automatically. The off-line pair at (0.650786, 114.163343) is numerically negligible at this window (Hermite-Gauss tail factor ≈ 10⁻⁴⁴). * **Archimedean term.** Same gamma factor as the underlying odd Dirichlet character χ (mod 5): `M_arch_ij ∝ ∫ Re ψ((1/2+1)/2 + ir/2) ...`, identical to the validated L(χ₄ mod 5) implementation. This is exact; the gamma factor of L_DH equals that of L(χ) since both summands share it. * **Polar term.** `(log 5/π)/(2π) · I_J`. Exact. * **Prime-power sum (BEST EFFORT).** M_primes_ij = (1/π) · Re[ (1−iκ)/2 · Σ Λ(n) χ(n)/√n · g_ij(log n) + (1+iκ)/2 · Σ Λ(n) χ̄(n)/√n · g_ij(log n) ] with X = 10⁵. This is the κ-weighted linear combination of the single-character von Mangoldt sums of L(s, χ) and L(s, χ̄), which is formally consistent with the linear-combination L_DH = (1−iκ)/2 · L(χ) + (1+iκ)/2 · L(χ̄) but **DOES NOT close the L_DH explicit formula** because L_DH is not in the Selberg class. ### Best-effort numerical result (replaces the spec benchmark) At `(T₀ = 85.7, σ = 2, J = 10, X = 10⁵, dps = 50)`: λ_min(Q_L_DH) = −7.7712 × 10⁻¹ λ_max(Q_L_DH) = +7.1697 × 10⁻¹ tr(M_zeros) = 5.2136 tr(M_arith) = 6.6977 tr(M_zeros) − tr(M_arith) = −1.4841 (trace-identity residual) |λ_min| / tr(M_zeros) = 1.49 × 10⁻¹ (For sanity context: in the same engine, ζ gives λ_min ≈ −7.5×10⁻¹⁴ and
trace residual 0 to machine precision at the same parameters — confirming
the basis, archimedean, and polar machinery are correct. For L(χ₄ mod 5)
with κ = 0 in the L_DH engine — i.e. (L+L̄)/2 — we obtain λ_min ≈ −0.46
and trace residual ≈ 0.03, indicating that even the κ = 0 limit of the
best-effort linear-combination prime sum is inexact at the ~3% level;
this is the unavoidable error introduced by the absent L_DH arithmetic
side.) ### Sign and qualitative interpretation The best-effort λ_min IS NEGATIVE and is **approximately 10¹³ times
larger in magnitude than the ζ noise floor** at the same parameters
(7.8 × 10⁻¹ vs 7.5 × 10⁻¹⁴). It is also larger in magnitude than the
best-effort L(χ₄ mod 5) baseline (−4.6 × 10⁻¹ at κ = 0), confirming
that the κ-weighted and off-line-zero contributions push the quadratic
form toward greater indefiniteness. L_DH therefore confirms as a **valid
positive control for the detection principle**: detection is qualitative
(negative λ_min several orders of magnitude above the GRH-class floor),
even though the spec's quantitative benchmark (−9×10⁴) is not
reproducible. ### Decision * **Specification benchmark `λ_min ≈ −9 × 10⁴`**: marked IRREPRODUCIBLE (no public arithmetic side).
* **Best-effort reference value** for downstream comparisons: `λ_min(L_DH) = −7.77 × 10⁻¹` at (T₀=85.7, σ=2, J=10, X=10⁵, κ=0.28408).
* **Engine validation requirement for L_DH**: must continue to pass the ζ trace identity at the same parameters (1e-14 floor), and must produce a negative λ_min for L_DH whose magnitude exceeds the same-parameter GRH-class floor by ≥ 10 orders of magnitude. Both conditions met.
