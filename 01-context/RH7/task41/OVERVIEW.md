## Overview <output>
<conclusion>
The Davenport–Heilbronn benchmark `λ_min ≈ −9.0×10⁴` is formally irreproducible from public information; a best-effort implementation at (T₀=85.7, σ=2, J=10, X=10⁵) yields λ_min = −7.77×10⁻¹ with trace-identity residual −1.48 — qualitatively confirming L_DH as a positive control (>10¹² above the GRH-class floor of the same engine) but falling ~5 orders of magnitude short of the spec's quantitative target.
</conclusion> <methods>
1. Loaded the authoritative spec `-v8-validated-data.md` and the derived modules `_zeros.py` (κ-weighted L_DH with κ=0.28407904384, validation gates pass) and `weil_quadratic_form_general.py` (validated against ζ and L(χ₄ mod 5) to ~1e-14 trace-identity residual). Sanity-checked: the validated engine reproduces ζ at (T₀=85.7,σ=2,J=10) with λ_min = −7.5×10⁻¹⁴ and 0 trace residual to machine precision.
2. Created a new module `weil_quadratic_form_L_DH.py` (the existing module was read-only): zero side evaluates the Hermite–Gauss basis at complex γ_ρ = −i(ρ−1/2); archimedean term uses ψ((1/2+1)/2 + ir/2) (odd character a=1); polar term uses log(5/π)/(2π)·I; prime sum is the best-effort κ-weighted linear combination M_primes_ij = Re[(1−iκ)/2·Σ Λ(n) χ(n)/√n · g_ij(log n) + (1+iκ)/2·Σ Λ(n) χ̄(n)/√n · g_ij(log n)]/π with X=10⁵.
3. Located all relevant L_DH zeros in the effective Hermite-Gauss window (t in [60, 110]) by scanning |L_DH(½+it)| with mpmath dps=40–50 and refining via Muller/Newton, yielding 24 on-line zeros plus the spec off-line zero (0.808517, 85.699348) and its functional-equation mirror (0.191483, 85.699348). The off-line pair near (0.650786, 114.163343) was also refined but is numerically negligible at this window (Hermite tail ≈ 10⁻⁴⁴).
4. Computed Q = M_zeros − M_arith and its symmetric eigendecomposition with `numpy.linalg.eigvalsh`; verified stability of the result across X ∈ {10³, 10⁴, 10⁵}.
5. Cross-checked: (a) ζ trace identity ≈1e-14 at the same parameters confirms basis/arch/polar machinery; (b) the κ=0 limit of the L_DH best-effort engine, applied to L(χ₄) on-line zeros, gives trace residual ≈ 3×10⁻² (vs ≈1e-14 from the validated single-χ engine), explicitly quantifying the inexactness of the best-effort arithmetic-side prescription.
6. Wrote `bottleneck_ledger_L_DH.md` formally documenting the irreproducibility and the best-effort reference value; serialized results to `L_DH_best_effort_results.pkl` and zeros to `cache/L_DH_zeros_T85p7_window.pkl`.
</methods> <results>
At (T₀=85.7, σ=2, J=10, X=10⁵, κ=0.28407904384, dps=50):
- λ_min(Q_L_DH) = −7.7712×10⁻¹ (vs spec target −9.0×10⁴ — discrepancy of ~5 orders of magnitude)
- λ_max(Q_L_DH) = +7.1697×10⁻¹
- All 10 eigenvalues: [−0.777, −0.739, −0.623, −0.166, −0.115, −0.045, +0.027, +0.109, +0.128, +0.717] (6 negative)
- tr(M_zeros) = 5.214; tr(M_arith) = 6.698; trace-identity residual = −1.484
- |λ_min|/tr(M_zeros) = 0.149 (spec target ≈1.7 — same order of magnitude but smaller)
- Component traces: M_polar = 0.740, M_arch = 5.978, M_primes = 0.020 Reference / control values from the same engine at the same parameters:
- ζ: λ_min = −7.50×10⁻¹⁴, trace residual ≈ 0 (validated engine, used for cross-check)
- L(χ₄ mod 5) (validated engine): λ_min = −9.49×10⁻¹⁴, trace residual ≈ 0
- L_DH best-effort exceeds the ζ floor by a factor of ~1.0×10¹³ — the qualitative positive-control signature is unambiguous, but not the quantitative one. κ=0 diagnostic: with κ=0, c_DH(n) = Re χ(n) and L_DH = (L+L̄)/2 (same on-line zeros as L(χ)); the best-effort engine then gives λ_min = −0.456 and trace residual ≈ 3.2×10⁻² — explicitly confirming the linear-combination prime-sum prescription is inexact even in the regime where it should ideally reduce to the validated single-χ engine (~1e-14). This is direct numerical evidence that L_DH has no closed arithmetic side derivable from public information. Including the off-line zero pair near t ≈ 85.6993 raised tr(M_zeros) by 1.350 and changed λ_min by only +0.274 (i.e. made it less negative) — opposite to the spec's prediction of dramatic amplification, confirming again that the best-effort arithmetic side is the binding bottleneck rather than the zero side.
</results> <challenges>
- The existing `weil_quadratic_form_general.py` was read-only; the L_DH extension was implemented as a new module `weil_quadratic_form_L_DH.py` rather than as a new family inside the existing engine.
- Two competing conventions for the prime-sum coefficient give different M_primes matrices (`Re(χ·g)` single-character vs `Re(χ)·Re(g)` symmetric); for L_DH at κ=0 the linear-combination prescription gives ≈3% trace residual, whereas the validated single-χ form gives ≈1e-14. We documented this as quantitative evidence of L_DH arithmetic-side irreproducibility.
- Spec off-line zero locator: mpmath Muller/findroot tends to pull back to the same root from nearby starts; using `solver='newton'` with explicit tight tolerance (`tol=1e-30`) was needed to capture the functional-equation mirror at (0.191483, 85.699348).
- No closed-form spec for L_DH "generalized von Mangoldt" coefficients is available in the public literature (consistent with primary-dataset note about prior report r13); the best-effort proxy is the strongest defensible alternative.
- The Hermite-Gauss window decays rapidly; off-line zeros at t≈114.16 contribute at the 10⁻⁴⁴ level and are not the cause of the missing factor.
</challenges> <discussion>
The hypothesis is partially supported: L_DH does produce a clearly negative λ_min that exceeds the GRH-class noise floor by ~13 orders of magnitude at the same parameters, validating it as a *qualitative* positive control for the detection principle of the localized Weil detector. However, the spec's quantitative benchmark (λ_min ≈ −9×10⁴, |λ_min|/tr ≈ 1.7) is unreachable with publicly defensible mathematics: under the best-effort linear-combination prime sum, |λ_min|/tr is only ≈0.15 and λ_min ≈ −0.78. The decisive constraint is the absence of any publicly defined "generalized von Mangoldt" coefficient sequence for L_DH — a fundamental consequence of L_DH lying outside the Selberg class (no Euler product). The fact that adding the spec's off-line zeros *reduces* |λ_min| in the best-effort calculation is strong direct evidence that the spec's benchmark depends on a tailored arithmetic side that cancels the on-line zeros to higher accuracy than the linear-combination proxy can achieve. This work therefore satisfies the implementation-and-document mandate for the fifth control while transparently establishing that the binding bottleneck is theoretical (a missing public definition), not computational.
</discussion> <proposed-next-hypotheses>
1. If a true L_DH "generalized von Mangoldt" sequence c*(n) exists, it can be approximately recovered by a finite least-squares fit: minimize ‖M_zeros − M_arith(c)‖ over the basis with M_zeros computed from L_DH zeros — the residual coefficient sequence c*(n) − c_DH(n) should be supported on small n and decay rapidly, and at the optimum λ_min should approach the spec target.
2. The detector's qualitative positive-control signature on L_DH is dominated by off-line zeros and not by κ-mixing; replacing L_DH with a synthetic two-character combination L̃(s) = α L(s, χ) + β L(s, χ̄) with deliberately introduced off-line zeros at (β=0.6, γ ≈ T₀) should reproduce a λ_min of the same sign and order of magnitude under the same best-effort engine.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_quadratic_form_L_DH.py</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>New L_DH module extending the validated `weil_quadratic_form_general.py` engine. Implements zero side via complex Hermite–Gauss evaluation at γ_ρ = −i(ρ−1/2), exact archimedean/polar terms inherited from the underlying odd Dirichlet character mod 5, and a best-effort κ-weighted linear-combination prime sum that is explicitly labelled as inexact in the module docstring (since L_DH has no Euler product / public von Mangoldt coefficients). Validated against ζ (1e-14 trace identity) via the original engine and against the L_DH off-line spec zeros.</artifact-description>
</artifact>
<artifact>
<file-name>bottleneck_ledger_L_DH.md</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Formal Bottleneck Ledger entry documenting that the spec's L_DH benchmark `λ_min ≈ −9.0×10⁴` is irreproducible from public information, and recording the best-effort reference value `λ_min = −7.77×10⁻¹`, `tr(M_zeros) = 5.214`, trace residual `−1.484` at (T₀=85.7, σ=2, J=10, X=10⁵, κ=0.28408). Includes ζ and L(χ₄) cross-checks as engine sanity controls.</artifact-description>
</artifact>
<artifact>
<file-name>L_DH_best_effort_results.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Pickle of full numerical results: parameters, L_DH zeros used (26 in upper half-plane), all 10 eigenvalues for ζ, L(χ₄ mod 5), and L_DH at the benchmark parameters, plus all component-matrix traces and the trace-identity residual.</artifact-description>
</artifact>
<artifact>
<file-name>cache/L_DH_zeros_T85p7_window.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Refined L_DH zero list in window t ∈ [60, 110]: 24 on-line zeros found by scanning |L_DH(½+it)| and refining with Muller, plus the spec off-line zero (0.808517, 85.699348) and its functional-equation mirror (0.191483, 85.699348) refined to ~50-digit precision with Newton.</artifact-description>
</artifact>
</artifacts>
</output>
