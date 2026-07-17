## Overview <output>
<conclusion>
Using the final N=5000, dps=50 ζ and ζ_δ datasets, the Step 0.5 calibration does not support the hypothesis that Front II is highly sensitive and Front I moderately sensitive to the imposed off-line perturbation; instead, all primary observables tested were effectively blind or uninformative for the provided deformation (20 zeros shifted from Re=0.5 to 0.6).
</conclusion>
<methods>
I first loaded the two provided NumPy artifacts: `zeta_zeros_N5000_dps50.npy` (5000 imaginary parts as fixed-width strings) and `zeta_delta_zeros_N5000_dps50.npy` (structured array with `re` and `im` fields). I verified that the imaginary parts were identical across datasets and that exactly 20 entries (indices 1000–1019) had real part shifted from 0.5 to 0.6 in the ζ_δ control. For Front II, I computed truncated Li coefficients for n=1,…,200 using the canonical zero-sum formula
λ_n = Σ_ρ [1 − (1 − 1/ρ)^n],
implemented with `mpmath` at 50 decimal digits and symmetric complex-conjugate pairing, so each upper-half-plane zero contributed `2*Re(1-u^n)` with `u = 1 - 1/ρ`. I used all 5000 provided upper-half zeros for both ζ and ζ_δ, then calculated absolute and relative differences between the two λ_n sequences. For Front I, I used the specified Lanczos/Stieltjes inverse-spectral reconstruction on the discrete γ-spectrum to produce Jacobi coefficients in the stable window n < 0.1·N = 500. Because the specification requires a spectral-weight audit, I evaluated two admissible weights: (W1) uniform weights `w_k = 1/N`, and (W2) `w_k ∝ 1/|ρ_k|^2`. The Lanczos algorithm was applied to the diagonal operator with spectrum γ_k and starting vector proportional to sqrt(weights), yielding diagonal coefficients a_n and off-diagonal coefficients b_n. Relative differences between ζ and ζ_δ were then computed. For Front III, I unfolded the zeros using the standard smooth Riemann-von-Mangoldt/Riemann–Siegel theta approximation, then computed Vietoris–Rips persistence with `ripser` and comparison metrics with `persim`. I tested H1 persistence on 3D embeddings in windows around the perturbed region, including a real-part-aware embedding `(scaled σ, unfolded γ, lagged unfolded γ)`. I also checked an imag-only Takens-style embedding as a baseline. Because H1 was empty, I report this as the primary TDA result; I additionally recorded the H0 bottleneck distance as an ancillary quantity. I saved quantitative outputs to `front2_li_calibration.csv`, `front1_jacobi_a.csv`, `front1_jacobi_b.csv`, `step0p5_sensitivity_summary.csv`, and generated the required final summary figure `step0p5_sensitivity_summary.png`. I also updated `./.prompts/MEMORY.md` with provenance and findings.
</methods>
<results>
Dataset validation showed: (1) the ζ and ζ_δ imaginary parts were identical at sampled and full-array checks, and (2) exactly 20 zeros were perturbed in ζ_δ, all at indices 1000–1019 with real part 0.6. Front II (Li coefficients):
- λ_n was computed for n=1 to 200.
- For ζ, selected values were λ_1 = 0.02286887, λ_2 = 0.09143839, λ_5 = 0.56987183, λ_50 = 42.96400916, λ_100 = 116.33544063, λ_200 = 297.58265871.
- For ζ_δ, corresponding values were λ_1 = 0.02287083, λ_2 = 0.09144230, λ_5 = 0.56988159, λ_50 = 42.96410669, λ_100 = 116.33563532, λ_200 = 297.58304523.
- The maximum relative change over n≤200 was 8.53×10^-5 at n=1.
- Mean absolute relative change over n≤200 was 3.19×10^-6.
- Under a linear-response extrapolation, the δ needed to induce a 5% relative change in λ_1 at fixed m=20 is about 58.6, which is non-physical for a real-part shift from the critical line.
- Equivalently, at fixed δ=0.1, about 1.17×10^4 displaced zeros would be needed for a 5% effect in λ_1 by the same extrapolation. Front I (Jacobi coefficients):
- With W1 = uniform spectral weights, the reconstructed γ-spectrum is identical for ζ and ζ_δ, so a_n and b_n were exactly unchanged across the full computed window n<500.
- With W2 = 1/|ρ|^2 weights, low-index relative differences were at numerical-noise scale: for example, a_n relative changes at n = 0,1,2,10,50,100,200 were approximately -1.84×10^-10, 1.20×10^-10, -1.13×10^-10, 1.02×10^-10, 1.77×10^-11, 3.23×10^-11, and -1.31×10^-11.
- Larger apparent relative changes near n≈362–363 reached about 1.86×10^-2, but these occurred in a regime dominated by Lanczos loss of orthogonality and are not interpretable as signal; the perturbed weights themselves changed by only about 5.45×10^-8 at most.
- Therefore, in the reliable low-n region, Front I was effectively insensitive to the imposed perturbation. Front III (TDA):
- In the tested 3D embeddings around the perturbed region (indices 900–1100 and 800–1200), H1 persistence was empty for both ζ and ζ_δ.
- The H1 bottleneck distance between ζ and ζ_δ was therefore 0 in these runs.
- In the imag-only Takens embedding, H1 was also empty, confirming no H1 signal after unfolding in this setting.
- Ancillary H0 analysis in the 900–1100 window gave a finite-diagram bottleneck distance of 3.656×10^-2, indicating only a small shift in connected-component scale structure. Sensitivity classification table:
- Front I, W1 uniform: exact relative change 0; classified UNINFORMATIVE (blind).
- Front I, W2 = 1/|ρ|^2: reliable-window changes ~10^-10; classified UNINFORMATIVE.
- Front II, λ_n (n≤200): max relative change 8.53×10^-5; classified UNINFORMATIVE for m=20, δ=0.1.
- Front III, H1 persistence: no H1 features in either dataset; classified UNINFORMATIVE.
- Front III, H0 persistence: small nonzero ancillary shift only; classified MARGINAL, not primary.
</results>
<challenges>
The main methodological challenge was that the supplied ζ_δ deformation changes only the real parts of 20 zeros while leaving all imaginary parts unchanged. Under the exact Front I and Front III constructions that depend only on the γ-spectrum or unfolded γ-values, this makes those observables structurally blind to the perturbation. This is not a computational failure but a limitation of the observable-definition/data combination. A second challenge was numerical stability in the Lanczos/Stieltjes reconstruction for Front I. Although coefficients were computed up to n=499, apparent relative differences at high n under the `1/|ρ|^2` weighting were inconsistent with the tiny underlying weight perturbation (~10^-8 scale) and were therefore attributed to Lanczos loss of orthogonality rather than true signal. I accordingly relied on the low-index stable region for interpretation. A third challenge was software availability: `ripser` and `persim` were not initially installed in the environment, so I installed them via pip after the import error occurred. After installation, all TDA cells executed successfully. Finally, the objective requested “minimum detectable δ” values, but only one nonzero deformation artifact (δ=0.1, m=20) was actually provided. I therefore did not fabricate a full sensitivity curve. Where appropriate, I gave only a clearly labeled local linear extrapolation from the observed δ=0.1 effect, and I explicitly note that this extrapolation is not a substitute for running the full mandated δ-grid.
</challenges>
<discussion>
These results indicate that, for the actual provided ζ_δ artifact, the principal observables from Fronts I–III do not show practically meaningful sensitivity. This directly weakens the stated hypothesis: Front II did not exhibit high sensitivity, Front I did not show robust moderate localized sensitivity, and Front III H1 remained non-informative, consistent with the specification’s warning that some metrics may be blind to small numbers of off-line zeros. Scientifically, this means null comparisons involving these observables cannot be interpreted as support for RH-like behavior unless their detection power is demonstrated on a broader injected-deformation grid. In particular, for the supplied control with only 20 displaced zeros among 5000, any failure of λ_n, Jacobi coefficients, or H1 persistence to distinguish ζ from a deformed control should be reported as lack of discriminating power, not evidence that the perturbation is irrelevant. The only nonzero topological signal I observed was a modest H0 bottleneck shift in a local real-part-aware embedding, but that was ancillary rather than the primary Front III H1 target. Thus, the current Step 0.5 calibration supports a conservative conclusion: with this exact final N=5000, dps=50 ζ_δ artifact, the tested observables are mostly blind, so downstream negative results from these fronts should be labeled uninformative unless stronger calibration data are generated.
</discussion>
<proposed-next-hypotheses>
1. For the same N=5000 zero list, Li coefficients λ_n remain effectively insensitive for n≤200 unless either the number of displaced zeros m or the deformation magnitude δ is increased substantially beyond the provided m=20, δ=0.1 setting.
2. TDA observables based on H0 persistence in real-part-aware embeddings are more sensitive to sparse off-line perturbations than H1 persistence after unfolding, and may provide a more useful Step 0.5 calibration target than H1 for this control family.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>front2_li_calibration.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table of Li coefficients λ_n for ζ and ζ_δ for n=1..200, including absolute and relative differences. Created from the provided zero lists using mpmath-based evaluation of the truncated Li zero sum with conjugate pairing.</artifact-description>
</artifact>
<artifact>
<file-name>front1_jacobi_a.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table of Front I Jacobi diagonal coefficients a_n for n=0..499 under two spectral weights: uniform and 1/|ρ|^2, for both ζ and ζ_δ. Generated via Lanczos/Stieltjes reconstruction on the discrete γ-spectrum.</artifact-description>
</artifact>
<artifact>
<file-name>front1_jacobi_b.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table of Front I Jacobi off-diagonal coefficients b_n for n=0..498 under two spectral weights: uniform and 1/|ρ|^2, for both ζ and ζ_δ. Generated via the same Lanczos/Stieltjes reconstruction used for the a_n table.</artifact-description>
</artifact>
<artifact>
<file-name>step0p5_sensitivity_summary.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compact summary table classifying each tested observable by its measured sensitivity to the provided ζ_δ perturbation. Includes the maximum observed relative change, qualitative detectability, and sensitivity interpretation.</artifact-description>
</artifact>
</artifacts>
</output>
