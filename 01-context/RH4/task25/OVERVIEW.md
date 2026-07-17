## Overview <output>
<conclusion>
The hypothesis is refuted: the empirical change Δ_empirical = M_jk(L_DH) − M_jk(ζ) is not quantitatively reproduced by injecting one (or even the canonical 4) off-line DH zero(s) into the Riemann–Weil explicit-formula sensitivity model — Frobenius residuals exceed the magnitude of Δ_empirical itself and the cosine similarity is essentially zero (≈ −0.08), with opposite signs on the dominant ω-strata.
</conclusion> <methods>
1. Validated the Davenport–Heilbronn constant κ ≈ 0.28408 by solving |L_DH(s; κ)| = 0 with mpmath (50-digit precision) starting near the documented canonical zero, recovering ρ₀ = 0.808517652 + 85.69934869 i with |L_DH(ρ₀)| < 10⁻⁴⁹ (R2 / R11 validation gates passed). Two additional non-trivial off-line zeros were also reproduced.
2. Built L_DH coefficients c_n periodic mod 5: (1, κ, −κ, −1, 0). Computed ω(n) for n ≤ N = 10⁶ by linear sieve (max ω = 7).
3. Reused the 200 zeta-peak t-values from M_jk_peaks_zeta_N1e6.json and recomputed S_k(t) = Σ_{ω(n)=k} c_n n^{−1/2−it} for L_DH using a Numba-parallel Kahan-compensated routine (rule R6). Saved as Sk_at_peaks_F4.npz.
4. Formed the empirical M_jk(L_DH) = mean over peaks of Re(S_j conj S_k) and the difference Δ_empirical = M_jk(L_DH) − M_jk(ζ).
5. Implemented the Riemann–Weil one-zero sensitivity injection: δa_n = −(n^{ρ₀−1/2} + n^{1/2−ρ₀}) (functional-equation symmetric pair). Propagated to δS_k(t) at each peak with the same Numba+Kahan engine. Built Δ_predicted(j,k) = mean over peaks of Re(δS_j conj S_k + S_j conj δS_k + δS_j conj δS_k).
6. Repeated with (a) a smooth log-Gaussian cutoff w(n)=exp(−ln²n/(2 ln² N_eff)), N_eff scanned over {10, 50, 200, 1000, 10⁴}, and (b) the full canonical quartet of zeros {ρ₀, 1−ρ₀, conj ρ₀, 1−conj ρ₀}.
7. Compared via Frobenius norm, sign-pattern agreement, and cosine similarity. Visualized side-by-side heatmaps.
</methods> <results>
- Empirical: ||M_jk(L_DH) − M_jk(ζ)||_F = 37.01. Δ_empirical is uniformly negative on the diagonal, with the strongest entries at (j=k=3) ≈ −16.1 and (j=k=2) ≈ −11.4, mirroring loss of the constructive ω≈2,3 block that dominates ζ at peaks.
- Diagonal comparison E[|S_k|²] (peaks): ζ has [1, 6.49, 12.79, 16.58, 5.88, 0.34, 3.5e-3, 8.6e-6]; L_DH has [1, 1.21, 1.40, 0.49, 0.11, 9.9e-3, 2.4e-4, 0]. Ratios L_DH/ζ for k=1..6 are 0.19, 0.11, 0.030, 0.019, 0.029, 0.069.
- Naive single-zero prediction (no cutoff) yields ||Δ_pred||_F ≈ 4.8×10⁷ — six orders of magnitude larger than empirical (the unsmoothed Σ n^{ρ₀−1−it} is asymptotically O(N^{β₀}) which overshoots wildly at N=10⁶).
- With smooth log-Gaussian regularization the magnitude can be matched at N_eff ≈ 10 (||Δ_pred||_F ≈ 11.9), but the residual ||Δ_emp − Δ_pred||_F = 39.8 actually exceeds ||Δ_emp||_F = 37 (relative residual 1.075). Cosine similarity = −0.079.
- Using the full canonical quartet of zeros (ρ₀, 1−ρ₀ and complex conjugates, smooth cutoff): ||Δ_pred₄||_F = 28.7, ||Δ_emp − Δ_pred₄||_F = 48.5, cosine similarity = −0.076. Sign agreement only 20/36 (≈ chance) and FAILS on every entry of the dominant (j,k)∈{(2,2),(2,3),(3,3),(3,4)} block where empirical is strongly negative but prediction is positive.
- Heatmap comparison shows the structural mismatch: Δ_empirical is a broad uniformly-negative block centered on (2,3); Δ_predicted has a hot positive lobe at (1,1)–(3,3) and a negative cross-band, fundamentally different geometry.
</results> <challenges>
- The Davenport–Heilbronn coefficients are not multiplicative and are periodic mod 5 with mean zero, so M_jk(L_DH) is governed by an entirely different arithmetic structure than M_jk(ζ) (a_n = 1). A "single zero injection" perturbation of the explicit formula formally modifies Λ_L on primes; it cannot transform the all-positive coefficient vector of ζ into the periodic-with-mean-zero coefficient vector of L_DH.
- The unsmoothed sensitivity integral diverges in the partial-sum sense (n^{β₀−1/2} grows), forcing introduction of an arbitrary smoothing scale N_eff. Results depend sensitively on this choice with no first-principles fixing.
- The predicted Sk_at_peaks_F4.npz file from a previous task was not present in /workspace; I generated it from scratch following Step 1 (R1) and saved it.
- t_peaks were grid-discretized (Δt = 0.1 from the prior detection step). Using the same peak set as for ζ ensures fair (peak-conditioned) comparison even though those t-locations are not L_DH peaks.
</challenges> <discussion>
A close match between Δ_empirical and the explicit-formula sensitivity Δ_predicted was the necessary "bridge" linking the candidate ω-stratified peak signature M_jk to off-line zeros. The attempt fails decisively, both in magnitude (mismatch by orders of magnitude unless an ad-hoc cutoff is tuned) and in structure (sign of the dominant ω≈2,3 block is wrong, cosine similarity ~0). The most honest interpretation, consistent with rule R5 (MVT kills unconditional cross-class structure) and R8 (honest reporting), is that the difference between M_jk(L_DH) and M_jk(ζ) is dominated by the difference in their *coefficient algebras* (a_n=1 vs. a periodic mean-zero vector that destroys the ω-stratified constructive interference at peaks), and is not a small perturbation that can be modeled by injecting individual off-line zeros into a common explicit formula. This refutes the claim that M_jk constitutes a "candidate signature" reading out off-line zeros: the bulk of the empirical signal is class-of-coefficient effect, exactly the pitfall flagged in the dataset description (r10 SVM held-out failure where features capture class-specific properties rather than a universal GRH-vs-non-GRH signal). Any future GRH-vs-non-GRH classifier based on M_jk will need to control for coefficient normalization/structure (e.g., contrasting against a multiplicative GRH-violator like F12 linear combinations rather than the non-multiplicative L_DH).
</discussion> <proposed-next-hypotheses>
1. Within a *family of multiplicative L-functions* with arithmetically matched Euler product structure (e.g., F1 ζ vs. F12 multiplicative DH-style linear combinations vs. F2 χ_4 mod 5), Δ M_jk = M_jk(non-GRH) − M_jk(GRH) becomes small and IS dominated by the explicit-formula sensitivity vector S(j,k; β₀) of the off-line zero, with cosine similarity > 0.5.
2. The L_DH peak structure can be matched by a "renormalized" sensitivity model that simultaneously injects all low-lying off-line zeros AND replaces ζ-Λ_L by L_DH-Λ_L (i.e., a coefficient-substitution model), with the residual after this substitution scaling as ε^β₀ in the perturbation parameter ε of F5 = L_DH(ε).
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>Sk_at_peaks_F4.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Davenport–Heilbronn (F4) ω-stratified partial sums S_k at the 200 ζ-peak t-values used in M_jk_peaks_zeta_N1e6.json. Computed at N=10⁶, K=8, with κ=0.28408 (operationally validated against ρ₀ = 0.80852 + 85.69935 i to |L_DH|<10⁻⁴⁹) using Numba-parallel Kahan-compensated summation. Stored as t_peaks, Sk_re, Sk_im, kappa, N, K. Enables future re-analyses of the L_DH peak-conditioned cross-term matrix without recomputing.</artifact-description>
</artifact>
<artifact>
<file-name>Mjk_DH_vs_zeta_prediction.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel heatmap (A: Δ_empirical = M_jk(L_DH)−M_jk(ζ); B: Δ_predicted from injecting the canonical 4-zero DH quartet through the Riemann–Weil sensitivity model with log-Gaussian cutoff). Annotated with Frobenius norms and cosine similarity. Visually demonstrates the structural mismatch (uniform negative block in A vs. mixed-sign pattern in B).</artifact-description>
</artifact>
</artifacts>
</output>
