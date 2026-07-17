## Overview <output>
<conclusion>
The empirical peak-conditioned matrix difference Δ_empirical = M_jk(F12) − M_jk(ζ) is NOT well-modelled by the r13-style explicit-formula sensitivity Δ_predicted obtained by injecting the constructed F12 off-line zero ρ₀ = 0.7 + 7i: the canonical cosine similarity is only −0.136 (range −0.28 to +0.28 across cutoff choices), far below the 0.5 threshold, refuting the hypothesis.
</conclusion> <methods>
1. Loaded the regenerated zeta peak-conditioned artifacts from the workspace (`t_peaks.npy` (200 peaks in t∈[10⁴,10⁵]), `absZ_peaks.npy`, `Sre.npy`, `Sim.npy`, `M.npy`); confirmed the matrix convention is M_jk = (1/200)·Σᵢ Re(S_j(tᵢ)* S_k(tᵢ)) by reconstruction from S (max abs deviation 0).
2. Constructed one F12 (DH-style) function from scratch: L_F12(s) = L(s, χ₃) + c·L(s, χ₅), where χ₃ is the real primitive Dirichlet character mod 3 (values [0,1,−1]) and χ₅ is the real primitive Legendre symbol mod 5 (values [0,1,−1,−1,1]). Targeting an off-line zero at ρ₀ = 0.7 + 7i, set c = −L(ρ₀, χ₃)/L(ρ₀, χ₅) using `mpmath.dirichlet` at 30 dps, giving c ≈ −0.16567 + 1.90093 i. Verified |L_F12(ρ₀)| = 0 exactly by construction.
3. Generated coefficients a_n^F12 = χ₃(n) + c·χ₅(n) for n ≤ N = 10⁶ and the Erdős–Kac function ω(n) (small-prime sieve; ω_max = 7 at N=10⁶, with k=7 stratum vanishing because every small-prime product of seven distinct primes ≤10⁶ contains both 3 and 5).
4. Computed S_k(t; N=10⁶) for k=0..7 at the 200 zeta peak t-values using a Numba parallelised, Kahan compensated-summation kernel (per-thread per-k accumulators). Formed M_F12 with the same convention, giving Δ_empirical = M_F12 − M(ζ).
5. Implemented the r13-style forward explicit-formula sensitivity by injecting the off-line zero pair ρ₀, ρ̄₀ as a coefficient perturbation: δa_n = −(n^{ρ₀−1/2} + n^{ρ̄₀−1/2})·w(n), with smooth quartic cutoff w(n) = exp(−4·(log n/log N)⁴). δa_n is real (conjugate pair).
6. Propagated δa_n to δS_k(t) using a second Numba Kahan kernel. Linearised M_jk perturbation: Δ_predicted_{jk} = (1/200) Σᵢ Re(S_j(ζ)* δS_k + δS_j* S_k(ζ)) (Hermitian symmetrisation).
7. Compared via Frobenius norms and cosine similarity of vectorised matrices. Robustness sweep over six alternative cutoff/sign choices.
8. Saved heatmap figure and full numerical artifact.
</methods> <results>
- Constructed F12: L_F12(s) = L(s, χ₃) + c·L(s, χ₅) with c = −0.16567330 + 1.90092523 i and verified zero ρ₀ = 0.7 + 7 i (mpmath, 30 dps).
- M_jk(F12) diagonal: [4.310, 11.870, 11.880, 4.855, 0.861, 0.0570, 9.0e-4, 0]; M_jk(ζ) diagonal: [1.000, 19.246, 50.877, 29.279, 10.340, 2.295, 0.0591, 1.5e-5].
- ‖Δ_empirical‖_F = 111.42, ‖Δ_predicted‖_F = 40.55, ‖Δ_empirical − Δ_predicted‖_F = 123.66, cosine similarity = −0.1362 (canonical quartic cutoff).
- Robustness across cutoffs/signs: cosine ∈ {−0.282, −0.136, +0.053, +0.081, +0.117, +0.136, +0.282}; |cos| max = 0.28, well below the 0.5 threshold.
- Δ_empirical is dominated by large negative off-diagonals in the (j,k) ∈ [1..5]² block (e.g. M[2,3] difference ≈ −43.7), while Δ_predicted is much smaller in magnitude and has substantial positive entries at the same positions (e.g. (1,1)=+13.6, (1,3)=+11.4) — mostly opposite-signed structure.
- Hypothesis threshold cos > 0.5 is REFUTED.
</results> <challenges>
- Sub-leading numerical hygiene: the explicit-formula injection grows like n^{β₀−1/2} = n^{0.2}, so a smooth cutoff is mandatory. The cosine similarity does shift across cutoffs but never reaches 0.5; the result is robust but cutoff-dependent in detail.
- F12 ω=7 stratum is identically zero at N=10⁶ because every product of seven smallest distinct primes ≤10⁶ contains 3 or 5; this introduces a hard zero column/row in M_F12 that cannot exist in M_ζ.
- Without the LMFDB-validated full F12 family, only one DH-style construction was tested (one γ₀=7, β₀=0.7); a small ensemble of ρ₀ choices would strengthen the refutation.
- The forward sensitivity model assumes ζ is a small-perturbation reference for F12, but a_n^F12 differs from a_n^ζ ≡ 1 at O(1), violating the linearisation premise — this is an intrinsic limitation of the r13-style bridge for DH-style sums (not a numerical issue).
</challenges> <discussion>
This is the critical control experiment proposed in r13. The result strongly supports the r13 conclusion: the peak-conditioned M_jk signature is dominated by class-specific coefficient algebra (here the Euler factors at primes 3 and 5 in χ₃ and χ₅, the absence of a true Euler product, and the Selberg-class structural mismatch between F12 and ζ) rather than by the off-line zero injected into the explicit formula. The forward-injection model captures only the sub-leading single-zero perturbation, while the empirical Δ_empirical reflects the much larger structural Dirichlet-series gap between a non-multiplicative linear combo and ζ. Per the rationale stated in the research objective, this provides strong evidence that the explicit-formula bridge is fundamentally disconnected from the M_jk signature mechanism in the F12-vs-ζ comparison, and supports abandoning that line of inquiry in favour of the fallback objective.
</discussion> <proposed-next-hypotheses>
1. The dominant component of Δ_empirical = M(F12) − M(ζ) can be quantitatively attributed to differences in local Euler factors at the conductor primes (here p=3, 5) of the constituent χ₃, χ₅ characters: a "ramified-prime ablation" model that removes the n divisible by 3 or 5 from M(ζ) will reproduce most of Δ_empirical (predicted cosine similarity > 0.7).
2. Within a same-degree, same-conductor pair of GRH-true L-functions (e.g. two Dirichlet L(s,χ) with different primitive χ of equal modulus), the explicit-formula sensitivity bridge will achieve cosine similarity > 0.5 between the empirical M_jk perturbation and the predicted one, isolating any residual zero-driven signal from the Selberg-class confound.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>Delta_F12_vs_zeta_results.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Numpy .npz archive containing the F12-vs-zeta control experiment: 200 zeta peak t-values and |Z|, M(zeta), M(F12), Δ_empirical, Δ_predicted, the F12 ω-stratified S_k arrays, the predicted δS_k arrays, the perturbation δa_n (n=0..10^6), the F12 construction parameters (ρ₀, c), and the summary scalars (cosine similarity, Frobenius norms). Generated by the Numba Kahan-summation engine described in the methods.</artifact-description>
</artifact>
<artifact>
<file-name>Delta_emp_vs_pred_F12_vs_zeta.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final summary figure with two stacked heatmaps: (A) Δ_empirical = M_jk(F12) − M_jk(ζ); (B) Δ_predicted from explicit-formula injection of ρ₀ = 0.7 + 7i with smooth quartic cutoff, annotated with Frobenius norms and the canonical cosine similarity (−0.136), showing the structural mismatch that refutes the hypothesis.</artifact-description>
</artifact>
</artifacts>
</output> 