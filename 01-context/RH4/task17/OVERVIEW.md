## Overview <output>
<conclusion>
The tested additive perturbation F16 = F15 + 0.1·χ_3 did not measurably shift the spectral signature toward the known violator region: its pc1_complex remained 0.9412 (vs 0.9413 for F15), far above the violator threshold of 0.92.
</conclusion>
<methods>
I rebuilt the spectral pipeline from scratch in Python (numpy, pandas, scipy, matplotlib, numba, mpmath, cypari2). I loaded the reference feature table `peaks_features_F1_F12_normalized_full_with_spectral_complex.csv` and summarized class-level spectral coordinates. Using PARI/GP via cypari2 (`mfDelta()`/`mfcoefs`) I generated Ramanujan tau coefficients up to N=10^6 and analytically normalized them as a_n = τ(n)/n^(11/2). I defined the quartic primitive character mod 5 by χ_5(1)=1, χ_5(2)=i, χ_5(3)=-i, χ_5(4)=-1 and built F15 coefficients b_n = a_n·χ_5(n). I defined the real primitive character mod 3 (Legendre symbol mod 3) and built F16 coefficients c_n = b_n + 0.1·χ_3(n). I computed ω(n) for all n ≤ 10^6 by sieve and stratified the sum into k = ω(n) ∈ {0,…,7}. Peaks of |S(t)| = |Σ_n a_n n^(-1/2-it)| in t ∈ [10^4, 2×10^4] were located using a Numba-jitted complex evaluator: a coarse N_short=10^5 scan with grid spacing 0.05 was peak-detected with `scipy.signal.find_peaks`, all coarse maxima were rescored at full N=10^6, and the top 300 candidates were refined in two stages (±0.05/21 pts, then ±0.005/41 pts). At the resulting 200 best peaks per function I evaluated the complex stratified sums S_k(t), formed the 8×8 real symmetric matrix M_jk = E[Re(S_j·conj(S_k))], computed its eigenvalues with `numpy.linalg.eigvalsh`, and defined pc1_complex = λ_1/Σλ_i and H_complex = -Σ p_i log p_i with p_i = λ_i/Σ λ_j. A 500-resample peak bootstrap quantified uncertainty. Outputs were saved (CSV/NPZ/PNG).
</methods>
<results>
Reference violator centroid (F4, F5p, F5m, F12) was (pc1_complex, H_complex) = (0.90396, 0.20130); GRH-true reference centroid was (0.94863, 0.11432). For the recomputed F15 in the requested t-range I obtained pc1_complex = 0.94127, H_complex = 0.25767, with eigenvalues [34.001, 1.783, 0.207, 0.103, 0.0255, 0.00311, 9.0×10^-6, 0]. For F16 I obtained pc1_complex = 0.94122, H_complex = 0.26190, with eigenvalues [34.139, 1.730, 0.254, 0.112, 0.0317, 0.00378, 1.18×10^-5, 0]. The shift from F15 to F16 was Δpc1_complex = -0.00005 and ΔH_complex = +0.00424. Bootstrap SDs were: F15 σ_pc1 = 0.00455, σ_H = 0.01459; F16 σ_pc1 = 0.00440, σ_H = 0.01422; thus Δpc1/σ ≈ -0.01 and ΔH/σ ≈ 0.29 — both within noise. F15 and F16 each remained about 0.037 above the violator pc1 centroid and both stayed well above the violator threshold pc1_complex < 0.92. Top peak magnitudes: max|S| = 18.3143 (F15) and 18.3097 (F16). Files saved: peaks_F15_F16_complex.csv, F15_F16_spectral.npz, F15_F16_spectral_position.png.
</results>
<challenges>
The workspace lacked precomputed F15/F16 coefficient and S_k arrays, so the full coefficient generation, peak finding, and spectral pipeline had to be rebuilt from scratch, including installing cypari2 and increasing the PARI stack. The reference feature table mainly aggregates peaks at much higher t (up to 10^5) than the requested [10^4, 2×10^4] range; per project notes, spectral features are sensitive to the t-range, so absolute cross-comparison to historical points has to be treated as approximate while the within-experiment F15-vs-F16 contrast is the reliable comparison. The exact entropy scale used in the reference table could not be cross-validated from stored complex reference S_k arrays, so the entropy axis comparison is qualitative; the pc1_complex axis comparison remains directly comparable. The χ_5 convention (quartic primitive character mod 5) was chosen consistently with the project's "F2 = L(chi5_quartic)" convention, but I could not directly inspect the r62 source.
</challenges>
<discussion>
Under a fully range-matched protocol, adding a 0.1·L(s, χ_3) component to the GRH-true twisted L-function F15 produced no meaningful movement of the spectral signature toward the established violator cluster. This is a controlled negative control for the hypothesis that the violator signature is sensitive to small additive non-automorphic admixtures. Combined with the prior r62 finding that a multiplicative twist L(s, Δ⊗χ) clusters with GRH-true functions, this strengthens the picture that the known violator signature is specific to the Davenport–Heilbronn-style construction and not easily induced by mild additive non-automorphic contamination. The result is also compatible with prior r63 findings that the difference matrix Δ_jk in parametric Davenport–Heilbronn families tracks the construction parameter κ (how the function is built) rather than the off-line zero location β (where the zero is). Together these observations suggest that the spectral feature space is more sensitive to structural construction class than to small additive perturbations.
</discussion>
<proposed-next-hypotheses>
A larger additive perturbation c·L(s, χ_3) with c ∈ {0.3, 0.5, 1.0} will produce a monotonic, statistically significant decrease in pc1_complex of F15+c·L(s, χ_3) under the same range-matched protocol. Additive perturbations using a Davenport–Heilbronn-style component (rather than the primitive χ_3) will move F15 toward the violator cluster at substantially smaller perturbation strengths than χ_3 does.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>peaks_F15_F16_complex.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>CSV with the 200 refined peaks for F15 and F16 in t ∈ [10^4, 2×10^4], including total peak magnitudes and complex ω-stratified sums S_k (Re/Im for k=0..7). Generated by the reconstructed N=10^6 Numba-accelerated main-sum pipeline.</artifact-description>
</artifact>
<artifact>
<file-name>F15_F16_spectral.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy archive with the 8×8 M_jk matrices, eigenvalues, scalar spectral features (pc1_complex, H_complex), and peak locations for F15 and F16, computed from the 200-peak stratified S_k data.</artifact-description>
</artifact>
<artifact>
<file-name>peaks_features_F1_F12_normalized_full_with_spectral_complex.csv</file-name>
<artifact-type>external_source</artifact-type>
<artifact-description>Reference feature table already present in the workspace (2200 rows, F1–F12) that provides the historical spectral coordinates pc1_complex, H_complex, pc1_mag, H_mag used as the comparison feature space for positioning F15 and F16.</artifact-description>
</artifact>
</artifacts>
</output>
