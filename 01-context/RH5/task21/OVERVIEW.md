## Overview <output>
<conclusion>
A synthesis of all v6.6 analytical fronts establishes a strict inverse correlation between sensitivity and relevance to Riemann Hypothesis (RH) proofs: topological methods (TDA) perfectly detect off-line zero perturbations but lack any proof route, whereas theoretically rigorous positivity certificates (Li coefficients) are virtually blind to those same perturbations at feasible finite scales.
</conclusion>
<methods>
The capstone synthesis leveraged previously computed datasets including high-precision zero lists for five controls (ζ, ζ_δ, L(χ₄ mod 5), L_DH, L(Δ,s)) at sizes up to $N=5000$, and reconstructed Jacobi spectral coefficients ($a_n, b_n$). 1. **Front I (Spectral operator):** Computed AIC-selected asymptotic models for Jacobi $b_n$ across controls, confirming a stable shallow power-law decay but establishing that the mapping is structurally insensitive to real-part shifts at current precision (ζ and ζ_δ yield identical float64 coefficients).
2. **Front II.5 & II.6 (Positivities):** Synthesized prior L_DH Li coefficient calculations ($λ_n > 0$ for $n \le 200$) demonstrating insensitivity to 110 known off-line zeros. Computed a finite-$N$ spectral Gram quadratic form ($\lambda_{min}(Q_{10})$) using Hermite test functions to verify condition floors for numerical positive-definiteness on all test spectra.
3. **Front III (TDA):** Re-computed H0 bottleneck distances ($d_B$) and executed a Wasserstein-1 permutation test (500 permutations) on $Re(\rho)$ spectra.
4. **Front II.7 (Moments):** Computed numerical integration estimates for the leading ratios $I_1/(T \log T)$ and $I_2/[T(\log T)^4/(2\pi^2)]$ for ζ up to $T \approx 5447.86$ to confirm classical leading asymptotics prior to a full ω-class decomposition.
5. All findings were formalized in the strict "Bottleneck Ledger" (R10) defining the precise mathematical or computational obstruction for each observable.
</methods>
<results>
- **Front III (TDA)** precisely matched the theoretical calibration: $\zeta_\delta$ perturbed by $\delta=1.0$ and $\delta=0.001$ yielded $d_B = 0.5000$ and $d_B = 0.0005$ respectively (a strict $\delta/2$ scaling). Comparing $\zeta$ against $L_{DH}$ with 110 off-line zeros yielded $d_B = 0.0141$. The Wasserstein-1 permutation test yielded $p \le 0.002$ for any off-line perturbation versus $\zeta$, and exactly $p=1.000$ for all pure critical-line spectra combinations.
- **Front I (Jacobi)** showed identical $b_n$ sequences for $\zeta$ and $\zeta_\delta$ under both uniform and weighted reconstructions to full `float64` precision ($\Delta b_n / b_n = 0.0$). AIC favored a power law $b_n \approx c \cdot n^\delta$ with $\delta \approx -0.01$ over logarithmic models ($\Delta AIC \approx 698$ for $\zeta$).
- **Front II.5 (Li)** confirmed that for $L_{DH}$, all $λ_n > 0$ for $n \le 200$; the off-line zero orbit contributes positively (e.g. $+0.00039$ for $\lambda_1$).
- **Front II.6 (Weil)** yielded $\lambda_{min}(Q_{10}) \approx 4.57 \times 10^{-9}$ for $\zeta$, which is positive strictly by structural construction, driven by the $\sim 2 \times 10^{16}$ condition number of the test matrix.
- **Front II.7 (Moments)** computed $I_1$ ratio $= 0.799$ and $I_2$ ratio $= 1.089$ at $T=5447.86$ for $\zeta$.
</results>
<challenges>
- **Front II.6 (Weil form):** True explicit-formula Weil forms (requiring boundary term subtraction) could not be rapidly constructed without the explicit Bombieri-Hejhal or de Branges formulations ready; the structural Hermite-Gram form computed is positive by construction, which serves to establish the numerical condition floor but not a genuine RH discriminator.
- **Front II.7 (Moments):** Full ω-class decompositions matching Keating-Snaith $C_{k,r}$ values are explicitly not completed in this pass due to missing Dirichlet sum infrastructure, leaving this priority deliverable as the primary open bottleneck.
- **Front I & III (L(Δ,s)):** High-precision ($dps=80$) zero tables for Ramanujan Δ ($T^{2.85}$ cypari2 cost scaling) are critically incomplete, leaving its TDA and Weil evaluations missing.
</challenges>
<discussion>
The completed Bottleneck Ledger strictly bounds what numeric simulations can deliver for the RH. Observables structurally tied to RH proofs (Li $λ_n$, Weil explicit forms) require impossibly deep computations ($n \approx 86,000$ for Li) to register known critical-line deviations, while phenomenologically sensitive detectors (TDA $H_0$ bottleneck, $p=0.002$) completely lack an associated pure-mathematical lemma connecting them to the required analytic properties. Thus, computational evidence for the RH derived from finite $N \le 20,000$ data must be classified strictly as phenomenological rather than theorem-adjacent unless accompanied by novel uniform-in-$N$ lower bounds.
</discussion>
<proposed-next-hypotheses>
1. The Keating-Snaith cross-class moment fractions for the $L_{DH}$ function will fail to stabilize as $T \to \infty$ due to its missing Euler product structure.
2. An explicit-formula Weil form $Q_N(\phi)$ incorporating boundary term corrections will yield $\lambda_{min} < 0$ at $N \le 5000$ for the $L_{DH}$ off-line spectrum.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>bottleneck_ledger.md</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>The canonical Markdown table (R10) documenting the strongest proven statement, missing lemma, and plausible theoretical route for every analytical front across the control panel.</artifact-description>
</artifact>
<artifact>
<file-name>_final_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>A 300-dpi two-panel summary figure overlaying Jacobi $b_n$ fits and a heatmap of the Front III H0 bottleneck distances.</artifact-description>
</artifact>
<artifact>
<file-name>_final_summary.pdf</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>A vector-graphics (PDF) version of the two-panel summary figure overlaying Jacobi $b_n$ fits and the Front III H0 bottleneck distances.</artifact-description>
</artifact>
<artifact>
<file-name>_supplementary_4panel.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>A 300-dpi four-panel supplementary figure detailing Front I (Jacobi), Front II.5 (Li), Front II.6 (Gram $\lambda_{min}$), and Front III (Wasserstein-1 permutation test $p$-values).</artifact-description>
</artifact>
<artifact>
<file-name>_supplementary_4panel.pdf</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>A vector-graphics (PDF) version of the four-panel supplementary figure detailing Front I (Jacobi), Front II.5 (Li), Front II.6 (Gram $\lambda_{min}$), and Front III (Wasserstein-1 permutation test $p$-values).</artifact-description>
</artifact>
<artifact>
<file-name>front3_bottleneck_distance_matrix.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>A CSV matrix recording the exact pairwise H0 bottleneck distances between the $Re(\rho)$ distributions of the five main functions.</artifact-description>
</artifact>
<artifact>
<file-name>front3_perm_pvalues.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>A CSV matrix of exact $p$-values derived from a 500-iteration Wasserstein-1 permutation test on the $Re(\rho)$ values.</artifact-description>
</artifact>
</artifacts>
</output>
