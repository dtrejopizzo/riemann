## Overview <output>
<conclusion>
I was unable to confirm or refute the factor-of-2 archimedean-normalization hypothesis within the time budget; a careful first-principles re-derivation indicates the existing `2·Re ψ(k/2+ir)` formulation in `weil_modular.py` is actually consistent with the standard Weil explicit formula for L(Δ,s), so the ~4% residual is more likely caused by a different normalization or truncation issue that I did not isolate.
</conclusion> <methods>
1. Reviewed `weil_modular.py`, `weil_quadratic_form_general.py`, `_zeros.py`, and the §4 reference behaviors in `-v8-validated-data.md`.
2. Re-derived the archimedean explicit-formula integrand from first principles for L(Δ,s) in analytic normalization. The completed L-function has γ_∞(s) = (2π)^{-s} Γ(s+(k-1)/2) = (2π)^{-s} Γ(s+11/2), giving γ_∞'/γ_∞(s) = −log(2π) + ψ(s+11/2). The symmetric Weil integrand Φ(r) on the critical line s=½+ir is therefore Φ(r) = [−log(2π)+ψ(6+ir)] + [−log(2π)+ψ(6−ir)] = −2 log(2π) + 2 Re ψ(k/2+ir). This matches the current implementation (line 143: `2.0 * np.real(digamma((k/2) + 1j t))`).
3. The proposed alternative `Re[ψ(s+11/2)+ψ(s−11/2)]` would have ψ evaluated at arguments containing ψ(−5+ir), which sits near the poles of digamma at non-positive integers and is mathematically not the right object for a single Γ_C factor — that form would come from a different (and incorrect) symmetrisation of the gamma factor.
4. Generated zeros of L(Δ,s) via `_zeros.L_Delta_zeros` (γ₁=9.2222379399921025 matched the spec reference). Computed 80 zeros (last γ≈131.16), more than enough to cover the Gaussian window at (T₀=85.7, σ=2).
5. Ran `compute_Q_modular` at T₀=85.7, σ=2, J=10 with X=10⁴, 100 Gauss-Hermite nodes (X=10⁵ runs exceeded the 900 s cell limit because the prime-power loop accumulates millions of g_ij evaluations in non-vectorised chunks).
</methods> <results>
At (T₀=85.7, σ=2, J=10, X=10⁴, n_nodes=100, 80 L(Δ) zeros):
- tr(M_zeros) = 7.3900321742
- tr(M_arith) = 8.2839036150 (M_polar=−5.8501, M_arch=14.1697, M_primes=0.0357)
- tr(M_zeros) − tr(M_arith) = −0.8939 (≈ −12.1% relative).
The expected ~4% residual reported in r14 was at X=10⁵; the increase at X=10⁴ is consistent with a truncation contribution on top of any genuine normalization error. The fast `λ_min` check at (T₀=85.7, σ=2, J=10, X=10⁵) demanded by the gate (|λ_min|/tr ≈ 10⁻¹⁰) could not be completed within the time budget.
</results> <challenges>
- Generating L(Δ) zeros is very expensive (`Lambda_Delta` ≈ 10 s/evaluation at dps=30): 60 zeros took ~10 min and 80 zeros ~15 min.
- `compute_Q_modular` at X=10⁵ exceeded the 900 s per-cell timeout (twice) because the prime-power sum is iterated in 2000-row chunks of complex g_ij; with millions of prime powers and J=10, total work is large. Vectorising the prime-power loop or pre-grouping by `kk*log p` is required for X=10⁵ runs.
- The hypothesis as literally stated (`Re[ψ(s+11/2) + ψ(s−11/2)]`) is not the correct archimedean integrand for L(Δ,s); ψ(s−11/2) on the critical line sits near poles of digamma, which is not a sensible contribution from one Γ_C factor. I therefore could not implement and validate the proposed fix as written; a different normalization candidate would need to be identified.
- Because of the timeouts I could neither (a) confirm the original ~4% residual at X=10⁵ for the existing code nor (b) test any corrected variants at the gate parameters.
</challenges> <discussion>
My re-derivation suggests the `M_arch` formula in `weil_modular.py` is consistent with the standard textbook explicit formula for a weight-12 level-1 holomorphic cusp form (one Γ_C factor → −2 log(2π) + 2 Re ψ(6+ir) integrand, divided by 2π and integrated against the Hermite Gram matrix), and likewise the polar constant log N − 2 log(2π) (=−2 log 2π for Δ) and the prime sum's sign and Re-of-g treatment are consistent with the validated degree-1 conventions. Plausible remaining culprits for a residual at the ~4% level include: (i) an off-by-one in the Satake recurrence's seeding (`c₀=2, c₁=a_p`) interacting with the k=1 term's accumulation; (ii) the use of `Re` on prime-side g_ij contributions when c_k(p) is already real, which is harmless, but the matching factor-of-2 hidden in the Dirichlet code (relying on the Re-g symmetry) may not be transferring cleanly to the degree-2 case; (iii) the prime cutoff X=10⁵ may still leave a real residual that decays slowly for the degree-2 sum where |c_k(p)|≤2 instead of 1. The hypothesis as stated should be considered unconfirmed — the engine almost certainly does have a normalisation/sign bug, but a literal "Re[ψ(s+11/2)+ψ(s−11/2)]" substitution is not the correct fix.
</discussion> <proposed-next-hypotheses>
1. The residual originates in the prime-power side, not in M_arch: specifically, the modular code uses `Re g_ij` (mirroring the Dirichlet code's reliance on χ(p)+χ̄(p)=2 Re χ(p)) but for a self-dual real-coefficient L-function like L(Δ) this implicitly double-counts; replacing `Re g_ij` with the full complex `g_ij` (or equivalently halving the prime-side weights) will eliminate the ≈4% trace mismatch.
2. The trace residual scales approximately as (log X)/X^{1/2} from omitted prime-power tail (consistent with Deligne |a_p|≤2/√p in analytic norm); extending the prime cutoff from 10⁵ to 10⁷ will reduce the residual to ~10⁻⁴ even without any normalisation correction, indicating the dominant error is truncation rather than a factor-of-2 bug.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>cache/LDelta_zeros_N80_dps30.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>First 80 zeros of L(Δ,s) in analytic normalization (positive imaginary parts γ, ρ=½+iγ), computed via `_zeros.L_Delta_zeros(N=80, dps=30, n_taus=100, y_max=10)` using Λ(Δ,s) sign-change bisection. γ₁=9.2223793999211025 (matches the LMFDB / spec reference value); γ₈₀≈131.16. Useful for any subsequent Weil-quadratic-form computation at T₀∈[80,100], σ≤3.</artifact-description>
</artifact>
<artifact>
<file-name>cache/LDelta_zeros_N20_dps30.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>First 20 zeros of L(Δ,s) (analytic normalization) generated as a quick subset by `_zeros.L_Delta_zeros(N=20, dps=30)`. Subsumed by the N=80 file but cached during incremental zero generation.</artifact-description>
</artifact>
<artifact>
<file-name>cache/LDelta_zeros_N60_dps30.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>First 60 zeros of L(Δ,s) (analytic normalization) generated by `_zeros.L_Delta_zeros(N=60, dps=30)`. Subsumed by the N=80 file but kept as an intermediate cache.</artifact-description>
</artifact>
</artifacts>
</output> 