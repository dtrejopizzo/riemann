## Overview <output>
<conclusion>
For the constructed five-function violator family F(γ)=L(s,χ₃)+c(γ)L(s,χ₅) with forced zero at 0.7+iγ, the demodulated observable P_23(γ′)=E[S₂(t)conj(S₃(t))e^{-iγ′t}] did not show a reliable resonance at γ′=γ for any of γ∈{7,20,50,80,100}, so the tested inverse-bridge hypothesis is refuted in this protocol.
</conclusion>
<methods>
I implemented the experiment from scratch in Python in the notebook using numpy, mpmath, scipy, matplotlib, numba, and finufft. First, I defined the real primitive Dirichlet characters χ₃ mod 3 and χ₅ mod 5 explicitly by residue class. For each target ordinate γ∈{7,20,50,80,100}, I solved for the complex coefficient c(γ) by enforcing L(0.7+iγ,χ₃)+c(γ)L(0.7+iγ,χ₅)=0, i.e. c(γ)=-L(0.7+iγ,χ₃)/L(0.7+iγ,χ₅), with mpmath at 50-digit precision. I validated each construction by checking |L_F(0.7+iγ)|, which was numerically ≈10^-51 or smaller. I then generated the Dirichlet coefficients a_n=χ₃(n)+c(γ)χ₅(n) for n≤10^6. As a consistency check, the γ=7 coefficients exactly matched the provided F12 coefficient array over the tested prefix. I computed the ω(n) stratification (number of distinct prime factors) for n≤10^6 by sieve, confirming the observed support ω(n)∈{0,…,7} for this truncation. For each function, I evaluated the truncated Dirichlet polynomial L_N(1/2+it)=Σ_{n≤10^6} a_n n^{-1/2-it} over t∈[10^4,2·10^4] on a coarse grid with spacing 0.05 using a 1D type-3 NUFFT (finufft), with x_n=-log n and coefficients a_n/√n. I identified candidate local maxima of |L_N(1/2+it)| using scipy.signal.find_peaks with minimum separation 0.6 in t, then refined each of the top 200 peaks by reevaluating on a local ±0.06 window with step 0.001 and taking the local maximum. At those 200 refined peaks, I computed the complex ω-stratified sums S_k(t)=Σ_{n≤10^6, ω(n)=k} a_n n^{-1/2-it} for k=0,…,7, again with NUFFT. I verified numerical consistency by checking that Σ_{k=0}^7 S_k(t) reconstructed L_N(1/2+it) with maximum absolute discrepancy 4.19×10^-6 in the tested case. For the target cross-term (j,k)=(2,3), I computed the demodulated average P_23(γ′)=mean_t[S₂(t)conj(S₃(t))e^{-iγ′t}] over the 200 peaks for a dense γ′ grid around each true γ. I examined both Re(P_23(γ′)) and |P_23(γ′)|, located global maxima, measured the value at γ′=γ, and compared that value to a background defined from grid points separated from both 0 and γ by more than 5 units. I summarized the result both visually and with quantitative diagnostics including |P(0)|, |P(γ)|, the 99th percentile of the background, and argmax_{γ′}|P(γ′)|.
</methods>
<results>
The solved coefficients were:
γ=7: c=-0.16567330026345564+1.9009252335917202i;
γ=20: c=-0.22574335464094544+0.6584718402748783i;
γ=50: c=-0.39671620865557156+0.09128321836769292i;
γ=80: c=-1.908989146611492-1.8403352051658193i;
γ=100: c=-1.554834413283402-0.20104443380860113i.
For all five constructions, the forcing condition was satisfied to numerical precision: |L_F(0.7+iγ)| ranged from 0 to about 1.67×10^-52. Peak finding over t∈[10^4,2·10^4] at N=10^6 produced 200 refined peaks per function. The largest peak amplitudes of |L_N(1/2+it)| were 44.417 (γ=7), 20.311 (γ=20), 17.122 (γ=50), 57.379 (γ=80), and 34.592 (γ=100). The smallest amplitudes among the top 200 peaks were 24.455, 12.105, 9.951, 31.316, and 18.002, respectively. For the demodulated cross-spectrum P_23(γ′), the global maxima of |P_23(γ′)| occurred near γ′=0 or a small offset from 0, not near the true ordinate γ:
γ=7: argmax|P| at γ′=0.000;
γ=20: argmax|P| at γ′=-0.470;
γ=50: argmax|P| at γ′=-5.075;
γ=80: argmax|P| at γ′=-3.620;
γ=100: argmax|P| at γ′=0.000.
The maxima of Re(P_23) were likewise near 0: 0.000, -0.470, -5.338, -1.993, and 0.000. The key diagnostic table was:
γ=7: |P(0)|=67.955, |P(γ)|=12.617, background 99th pct=11.401, |P(γ)|/bg99=1.107, argmax|P|=0.000.
γ=20: |P(0)|=0.227, |P(γ)|=0.943, background 99th pct=3.003, |P(γ)|/bg99=0.314, argmax|P|=-0.470.
γ=50: |P(0)|=0.855, |P(γ)|=0.229, background 99th pct=2.191, |P(γ)|/bg99=0.104, argmax|P|=-5.075.
γ=80: |P(0)|=1.883, |P(γ)|=13.953, background 99th pct=21.070, |P(γ)|/bg99=0.662, argmax|P|=-3.620.
γ=100: |P(0)|=48.810, |P(γ)|=4.111, background 99th pct=8.927, |P(γ)|/bg99=0.461, argmax|P|=0.000. Thus, for 4/5 ordinates, |P(γ)| was below the 99th-percentile background; for γ=7 it was only marginally above background but still far below the dominant peak at γ′=0. In no case did the principal resonance align with γ′=γ. A supplementary scan over all (j,k)∈{0,…,7}² for γ=50 also failed to reveal a strong resonance near γ, with the best local-to-background ratio only about 1.40, indicating no convincing hidden channel among other ω-stratified cross-terms under the same criterion.
</results>
<challenges>
The primary challenge was computational rather than statistical: the experiment requires evaluating a length-10^6 Dirichlet polynomial across a large t-grid and then recomputing ω-stratified sums at many peak locations. Direct summation would have been infeasible, so I used finufft for type-3 nonuniform FFT evaluation. This required installing finufft during the session. Another limitation is that, although the PDF specification discusses Kahan-summed engines and prior archives, the comprehensive peak archives were not present in the workspace, so I regenerated the required quantities directly from the mathematical definitions instead of reusing prior stored results. A methodological limitation is that this study tested the user-specified observable P_23 for one peak-selection/range protocol only: top 200 peaks in t∈[10^4,2·10^4] at N=10^6. I did not perform bootstrap confidence intervals on resonance locations because the central claim was not close: the observed maxima were plainly displaced away from γ and concentrated near γ′≈0. I also did not test alternative demodulation observables beyond limited pairwise checks, so the negative conclusion is specific to this proposed phase-demodulated cross-spectrum protocol and not a proof that no inverse bridge exists.
</challenges>
<discussion>
The result is a clean negative test of the proposed inverse-bridge mechanism. The ordinary time-averaged cross-term E[S_jconj(S_k)] contributes a strong DC component at γ′=0, and the attempted phase demodulation by e^{-iγ′t} did not isolate the imposed off-line zero ordinate γ. Empirically, the demodulated spectra are dominated by near-zero-frequency structure and background fluctuations rather than by a sharp resonance at the planted γ. This indicates that, in this family and under high-peak conditioning, the phase information retained by S₂(t)conj(S₃(t)) is not organized in a way that linearly encodes the zero height through this simple Fourier demodulation. This fits the broader pattern in the project description: several previous features were highly sensitive to how the function was constructed but not to the actual off-line zero location. Here too, although the construction parameter c(γ) changes substantially with γ, the chosen observable does not recover γ as a stable spectral line. The failure across five well-separated ordinates {7,20,50,80,100} is especially informative because it rules out an obvious and computationally natural candidate inverse bridge. A different observable may still succeed, but it will need to suppress the DC contribution more effectively and likely condition on a more explicit model of the explicit-formula phase contribution from the off-line zero.
</discussion>
<proposed-next-hypotheses>
1. After removing the DC component and peak-specific phase trends, a centered demodulated observable of the form E[(S_jconj(S_k)-E[S_jconj(S_k)])e^{-iγ′t}] still will not show a resonance at γ′=γ for the χ₃+cχ₅ violator family.
2. A demodulated observable based directly on the full peak value or on explicit-formula-informed residuals, rather than on the single cross-term S₂conj(S₃), will show stronger alignment between its dominant spectral peak and the planted zero ordinate γ.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>peaks_Sk_F_gamma_family.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing the constructed five-function family F(γ)=L(s,χ₃)+c(γ)L(s,χ₅), the solved coefficients c(γ), the 200 refined peak locations in t∈[10^4,2·10^4], the corresponding peak amplitudes, and the complex ω-stratified sums S_k(t) for k=0..7 at N=10^6. It was generated directly from the definitions using mpmath for coefficient solving, a sieve for ω(n), and finufft for Dirichlet polynomial evaluation.</artifact-description>
</artifact>
<artifact>
<file-name>demod_spectrum_P23.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing dense γ′ grids and the demodulated cross-spectrum P_23(γ′)=E[S₂(t)conj(S₃(t))e^{-iγ′t}] for each constructed function with γ∈{7,20,50,80,100}. It was produced from the peak-level S_k data stored in the companion archive and used for the quantitative resonance tests reported here.</artifact-description>
</artifact>
</artifacts>
</output>
