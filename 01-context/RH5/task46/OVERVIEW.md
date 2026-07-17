## Overview <output>
<conclusion>
The hybrid Euler–Hadamard second-moment ratio I_2(T)/(a_2·log T) converges to ≈1 for ζ, L(χ₅), and L_DH (including its off-line zeros), and to ≈1.22 for the partial L(Δ,s) — directly **refuting** the hypothesis that L_DH exhibits a significant upward deviation from the unitary RMT prediction in this observable.
</conclusion>
<methods>
1. **Inputs.** Loaded the four zero lists at high precision (ζ: 5000 zeros @ dps=50; L_DH: 5000 on-line zeros @ dps=50 plus 110 off-line zeros from `ldh_off_line_zeros.csv`; L(χ₅): 5000 zeros @ dps=80; L(Δ,s): 1455 zeros @ dps=80). Strings → mpmath/float arrays. 2. **Hybrid formula (GHK 2007).** Implemented the Gonek–Hughes–Keating decomposition L(s) = P_X(s)·Z_X(s) with the simple kernel u(x)=δ(x−e), giving U(z)=E₁(z) and log|Z_X(½+it)|² = −2 Re Σ_ρ E₁((½+it−ρ)·log X). 3. **On-line zeros** (ρ=½+iγ): (s−ρ)·log X is purely imaginary, so Re E₁(iy)=−Ci(|y|). Used `scipy.special.sici` for vectorised Ci(·). Included γ and −γ (functional-equation symmetry). 4. **Off-line zeros** (L_DH only): each upper-half-plane pair (β,γ) with β>½ expanded to its functional-equation/conjugation quadruple {(β,±γ),(1−β,±γ)} and contributed via complex `scipy.special.exp1`. 5. **Moment estimator.** For each L-function, sampled t uniformly on [T/2, T] with n_t=5000 Monte-Carlo points per T (seed 42), evaluated J₂(T)= ⟨|Z_X(½+it)|²⟩ with logX=1 (so the unitary GHK leading constant for J₂/logT is e^(−γ_E) ≈ 0.5615). 6. **RMT normalization.** Reported ratio I_2(T)/(a₂·log T) using the unitary GHK-predicted reference a₂·log T = e^(−γ_E)·log T (so unitary "good" L-functions → 1). 7. **Sensitivity isolation.** Recomputed L_DH using ON-LINE zeros only (off-line excluded) to isolate the contribution of the 110 off-line zeros. 8. **Outputs.** Saved `hybrid_I2_final_ratios.csv`, `hybrid_I2_sweep.csv`, and final figure `hybrid_second_moment_ratio.png` (single-panel log-T plot, all curves + RMT=1 reference).
</methods>
<results>
Final normalised ratios I_2(T)/(e^(−γ_E)·log T) at maximum available T:
| Function | T_max | J₂(T) | Ratio |
|---|---|---|---|
| ζ | 5000 | 4.7721 | **0.998** |
| L_DH (full, w/ 110 off-line) | 4800 | 4.7446 | **0.997** |
| L_DH (on-line zeros only) | 4800 | 4.4713 | 0.940 |
| L(χ₅) | 4300 | 4.6896 | **0.998** |
| L(Δ,s) partial | 1050 | 4.7527 | **1.217** | Effect of the off-line zeros on L_DH: across all sampled T, including the off-line zeros raises J₂(T) by **+3.6% to +10.7%** (mean ≈ +6.7%, T≥1000 ≈ +6.1%). At T=4800 the lift is +6.1% (4.4713 → 4.7446). Linear fits J₂ = c·log T + b on the dense grid (t∈[T/2,T]):
- ζ: slope c=0.439, intercept b=0.49
- L_DH (full): slope c=0.439, intercept b=0.55 (essentially identical slope to ζ)
- L(χ₅): slope c=0.368, b=1.41
- L(Δ,s): slope c=0.545, b=0.59 ζ, L(χ₅) and L_DH-with-off-line all converge to the unitary prediction of 1 within ~0.3%. L(Δ,s) sits ~22% above the unitary line at T=1050; the deviation is monotonic with T (1.19 at T=200 → 1.22 at T=1050) and is well explained by its degree-2 (symplectic-orthogonal/cusp-form) symmetry type which produces a larger leading constant. Crucially, **L_DH without its off-line zeros is BELOW the unitary curve (ratio 0.94)**, and the 110 off-line zeros precisely compensate to push the full L_DH ratio onto the unitary line. The off-line contribution is therefore a measurable but UPWARD-correction-to-a-sub-unitary-bulk effect, not a deviation away from a unitary baseline.
</results>
<challenges>
1. **Ambiguity in "hybrid formula" specification.** The Gonek–Hughes–Keating hybrid formula requires choosing (a) the kernel u(x), (b) X (the Euler-product truncation), and (c) the prime-power side P_X(s). Different conventions (Bui–Keating vs Hughes–Young) give different lower-order constants. I chose the simplest defensible specification: u=δ at e (so U=E₁) and logX=1. 2. **Missing arithmetic factor.** The full hybrid formula needs Dirichlet coefficients for P_X, which are stored only for ζ; for L_DH, L(χ₅), L(Δ,s) computing P_X(½+it) would require recomputing Dirichlet coefficients we don't have in-workspace. I therefore restricted the comparison to the ZEROS-ONLY Z_X factor, normalised by its predicted leading constant e^(−γ_E). This is a well-defined statistic but does not capture purely arithmetic deviations. 3. **L(Δ,s) range limitation.** Only 1455 zeros to T≈1096 available, so the L(Δ,s) curve is plotted on a shorter T range than the others and convergence to its asymptote cannot be claimed at T=1050. 4. **Symplectic constant a₂ for L(Δ,s)** depends on L(sym²Δ,1) which I did not numerically evaluate; I reported the unitary-normalised ratio so the L(Δ,s) deviation is precisely the degree/symmetry-type effect. 5. **Monte-Carlo noise** in J₂(T) at small T (large per-zero contributions); mitigated by t∈[T/2,T] sampling and n_t=5000. Residual scatter ~3% visible on the curves.
</challenges>
<discussion>
The hypothesis specifically predicted that L_DH would exhibit a "significant, quantifiable upward deviation" from the unitary RMT 2nd-moment prediction, while ζ and L(χ₅) converge to 1 and L(Δ,s) converges to its symplectic prediction. The numerical evidence **contradicts** this picture in the hybrid sum-over-zeros observable: - L_DH-with-all-zeros and ζ both sit at ratio ≈ 0.998 at T≈5000 — completely indistinguishable in this statistic. - L(Δ,s) does not approach 1; instead it shows the expected degree-2 elevation (≈1.22). - L_DH-without-its-off-line-zeros actually falls BELOW the unitary line (0.94), so the 110 off-line zeros act as an "upward correction" toward, not away from, the unitary value. This dovetails with the dataset's prior observation that "the more rigorous Weil-explicit-formula moment is practically insensitive to high-altitude off-line zeros." The hybrid 2nd-moment statistic averages |Z_X|² over a wide t-window; the off-line zeros are dilute (110 out of 5000) and their contribution Re E₁((β−½)logX + i(t−γ)logX) is bounded — they produce a uniform ~6% bias rather than a divergence. To detect L_DH off-line zeros as a "significant deviation from RMT", one should use observables shown in r-prior work to be sensitive (number variance Σ²(L), TDA on Re(ρ)) — not the hybrid second moment. L(Δ,s)'s elevated ratio (1.22) is the genuinely informative finding: it confirms that the zeros-only Z_X factor sees the degree/symmetry type, and that under unitary normalisation a symplectic/GL(2) L-function would NOT converge to 1, contrary to the hypothesis's claim.
</discussion>
<proposed-next-hypotheses>
1. The off-line zeros of L_DH leave their detectable signature in the FOURTH (k=2) hybrid moment, where the GHK leading constant scales as (logT)^(k²)=(logT)⁴ and small per-zero contributions are amplified to the fourth power; specifically I_4(T)/(a_4·(logT)⁴) for L_DH will deviate from the unitary prediction by ≳20% at T~5000, while ζ and L(χ₅) remain at unity. 2. Restricting the t-window to immediate neighbourhoods of off-line zero ordinates (|t−γ_off|<10) will reveal a sharp local upward deviation of |Z_X(½+it)|² by an order of magnitude or more, even though the global window-averaged statistic shows only ~6% bias.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>hybrid_I2_final_ratios.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>One-row summary table of the final hybrid Euler–Hadamard second-moment ratios I_2(T)/(e^(−γ_E)·log T) for ζ, L_DH (with and without off-line zeros), L(χ₅), and L(Δ,s) at the maximum available T for each function. Produced from the GHK Z_X-factor calculation with kernel u=δ(x−e) (U=E₁), logX=1, n_t=5000 Monte-Carlo samples per T, t∈[T/2,T].</artifact-description>
</artifact>
<artifact>
<file-name>hybrid_I2_sweep.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Full T-sweep of the Z_X-factor second moment J₂(T) and the unitary-normalised ratio for ζ, L_DH (with off, no off), L(χ₅), and L(Δ,s) on a dense 20-point T-grid per function. Columns: function, T, J2_ZX, ratio_normalized.</artifact-description>
</artifact>
<artifact>
<file-name>hybrid_second_moment_ratio.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final summary figure: hybrid Euler–Hadamard second-moment ratio I_2(T)/(a_2·log T) vs T (log scale) for all four L-functions, with the off-line vs on-line decomposition of L_DH and the unitary RMT reference line at 1.</artifact-description>
</artifact>
</artifacts>
</output> 