## Overview <output>
<conclusion>
At the available full-scale Front I resolution, the Jacobi coefficient sequences for all analyzable controls—including L_DH—are best described by a log-quadratic law, but L_DH shows substantially larger residual variance and somewhat greater spectral-weight sensitivity than the GRH controls, supporting the hypothesis that the key distinction is fit quality rather than model class.
</conclusion>
<methods>
I first checked the workspace contents and verified that only three complete N=5000 zero lists were initially present: zeta_zeros_N5000_dps50.npy, zeta_delta_zeros_N5000_dps50.npy, and ldh_zeros_N5000_dps50.npy. Because the objective required five controls, I attempted to generate the missing Dirichlet and Ramanujan-Delta zero lists within the notebook. I installed cypari2 and cysignals via pip after confirming cypari2 was absent. For the mod-5 Dirichlet L-function, I used PARI through cypari2 with lfuncreate([znstar(5,1),[1]]) to obtain the primitive order-4 character mod 5, then computed zeros with lfunzeros over height intervals and cached the results. This produced >5000 zeros, and I saved the first 5000 as lchi5_zeros_N5000_dps80.npy; however, consistent with the dataset notes, PARI returned only about 19–20 significant digits despite higher requested precision. For Ramanujan Delta, I used PARI modular-form functionality via mfinit([1,12],1), mfDelta(), and lfunmf(...), then called lfunzeros on height intervals; due to runtime limits, only 1298 zeros were cached, saved as ldelta_zeros_N1298_dps80.npy, so a complete N=5000 Delta analysis could not be completed. For Front I reconstruction, I treated each zero list’s imaginary parts gamma_n as a discrete spectrum and reconstructed the finite Jacobi operator T_N using a Lanczos/Stieltjes approach: Lanczos tridiagonalization of the diagonal operator diag(gamma_n) with starting vector proportional to sqrt(w_n), where w_n is the chosen spectral weight. I audited two weights exactly as requested: uniform weights and inverse-squared spectral weights w_n = 1/|rho_n|^2 with |rho_n|^2 = 1/4 + gamma_n^2. To improve numerical stability, I used full double Gram-Schmidt reorthogonalization in float64 at each Lanczos step. I extracted the diagonal coefficients a_n and off-diagonal coefficients b_n and restricted analysis to the stable window min(0.1*N, 500), yielding 500 coefficients for zeta, zeta_delta, L_DH, and L_chi5, and 129 coefficients for the partial L_Delta dataset. For model selection, I fit each coefficient sequence separately for a_n and b_n, under each weight, using ordinary least squares on the candidate families specified in the objective: constant, log-linear, and log-quadratic. Concretely, for n starting at 5 to reduce boundary effects, I compared y_n = c0, y_n = c0 + c1 log n, and y_n = c0 + c1 log n + c2 (log n)^2. For each fit I computed residual sum of squares, AIC = 2k + n log(RSS/n), BIC = k log n + n log(RSS/n), fitted parameters, and residual standard deviations. I then directly compared best-model identity, parameter estimates, and residual scales across the controls. Because a_n and b_n are deterministic truncated quantities rather than stochastic observables, I did not compute bootstrap confidence intervals; instead I reported model-comparison metrics and residual magnitudes, in line with the dataset protocol. I saved tabular outputs to front1_model_selection.csv, front1_logquad_params.csv, front1_spectral_audit.csv, and the reconstructed coefficients to front1_jacobi_coefficients_N5000.npz. I also produced the required final summary figure as front1_summary_figure.png and front1_summary_figure.pdf.
</methods>
<results>
Data availability and validation status:
- Complete N=5000 inputs available/analyzable: zeta, zeta_delta, L_DH, and newly generated L_chi5.
- I could not complete ldelta_zeros_N5000_dps80.npy because the Delta zero generation did not finish before timeout; only 1298 zeros were obtained, so the Delta result is partial and not directly comparable on equal N=5000 footing.
- zeta and zeta_delta had identical imaginary-part spectra, so Front I produced identical a_n and b_n results for these two controls, as expected from the known structural blindness of this pipeline to the zeta_delta real-part perturbation. Model selection:
- Across all analyzed sequences (5 functions x 2 coefficient types x 2 weights = 20 combinations, counting the partial Delta analysis), AIC and BIC both selected the log-quadratic model over constant and log-linear alternatives.
- Example for zeta a_n with uniform weights: AIC(constant)=2424.8, AIC(log-linear)=1724.6, AIC(log-quadratic)=1108.9; BIC(constant)=2429.0, BIC(log-linear)=1733.0, BIC(log-quadratic)=1121.5. This was representative of the general pattern.
- Thus, the best-supported model class was log-quadratic for every analyzable sequence, including L_DH. Residual variance / fit quality:
Using the log-quadratic model, residual standard deviations were:
- zeta: a_n uniform 3.0399, a_n weighted 3.1248; b_n uniform 2.0162, b_n weighted 2.1037.
- zeta_delta: identical to zeta in all four cases.
- L_chi5: a_n uniform 2.5152, a_n weighted 2.5703; b_n uniform 1.5715, b_n weighted 1.5045.
- L_Delta (partial N=1298): a_n uniform 0.8084, a_n weighted 0.9003; b_n uniform 0.4780, b_n weighted 0.4912. These smaller absolute values are not directly comparable because the stable window and spectral range were much smaller.
- L_DH: a_n uniform 7.9165, a_n weighted 7.4845; b_n uniform 3.9245, b_n weighted 4.1211. To normalize for different coefficient magnitudes, I also computed relative residual standard deviations sigma_resid / |c0| from the log-quadratic intercept term:
- zeta: a_n 0.001095 (uniform), 0.001123 (weighted); b_n 0.001513, 0.001579.
- zeta_delta: identical to zeta.
- L_chi5: a_n 0.001128, 0.001151; b_n 0.001457, 0.001395.
- L_Delta (partial): a_n 0.001581, 0.001756; b_n 0.001957, 0.002010.
- L_DH: a_n 0.003139, 0.002963; b_n 0.003194, 0.003348.
These values show that L_DH’s normalized residual scale was about 2.3x to 3.0x larger than the zeta and L_chi5 controls, which is the clearest quantitative support for the hypothesis. Selected log-quadratic parameter estimates:
- zeta, uniform: a_n ~ 2777.03 - 29.25 log n + 4.384 (log n)^2; b_n ~ 1332.23 + 17.81 log n - 2.722 (log n)^2.
- L_DH, uniform: a_n ~ 2522.10 - 17.83 log n + 2.581 (log n)^2; b_n ~ 1228.86 + 10.44 log n - 1.583 (log n)^2.
- L_chi5, uniform: a_n ~ 2229.43 - 19.39 log n + 2.791 (log n)^2; b_n ~ 1078.77 + 11.71 log n - 1.761 (log n)^2.
- L_Delta, uniform (partial): a_n ~ 511.29 - 7.050 log n + 1.562 (log n)^2; b_n ~ 244.21 + 4.090 log n - 0.9399 (log n)^2.
These parameter differences indicate distinct coefficient scales and curvature across functions, but not a different winning model class. Spectral-weight audit:
- zeta parameter shifts under weight change were modest: for a_n, c1 changed by -4.55% and c2 by +2.53%; for b_n, c1 changed by -3.12% and c2 by +2.52%.
- L_chi5 shifts were also modest overall: a_n c1 -7.02%, c2 +4.04%; b_n c1 -1.84%, c2 +1.84%.
- L_DH showed larger instability, especially for b_n: c1 changed by -10.27% and c2 by +7.14%. For a_n the changes were -5.38% and +2.58%.
- L_Delta also showed larger relative shifts in b_n (~-11.57% for c1 and +8.60% for c2), but because only N=1298 zeros were available, I do not treat this as a full-strength comparison against the N=5000 controls.
Overall, the weight audit indicates that while the log-quadratic model class is stable, L_DH is somewhat more sensitive than the main GRH controls in its fitted coefficient law, especially for b_n.
</results>
<challenges>
I cannot fully complete the requested five-way N=5000 Front I comparison because ldelta_zeros_N5000_dps80.npy was not available and could not be generated within the remaining runtime. Only 1298 Ramanujan-Delta zeros were obtained before timeout, so the Delta analysis is partial and not on the same N=5000 footing as the other four controls. This is the main limitation of the analysis. A second technical limitation is precision of the generated Dirichlet and Delta zeros from PARI: even after increasing the PARI stack and requesting higher precision, lfunzeros returned only about 19–20 significant digits, consistent with the dataset notes. That precision is still ample for the present Front I stable-window analysis at N=5000, but it does not satisfy a literal “80-digit zero list” interpretation. I therefore used the generated list as a practical numerical input for Front I while explicitly noting the precision caveat. A third limitation is methodological: the Delta comparison used only N=1298, so its residual and weight-sensitivity estimates are not directly comparable to the full N=5000 controls. In addition, I used float64 Lanczos with full reorthogonalization rather than arbitrary-precision orthogonal polynomials; this is numerically appropriate for the observed scales and produced stable coefficients quickly, but it remains an approximation to the ideal high-precision reconstruction. Finally, I did not perform formal significance testing on residual variance differences because these are deterministic truncation-derived sequences, not repeated random samples; the evidence is reported as direct quantitative comparison of residual scales, AIC/BIC margins, and parameter shifts rather than p-values.
</challenges>
<discussion>
Within the limits of the available data, the main research hypothesis is supported. The key finding is not that L_DH requires a different asymptotic family—because it does not—but that the same log-quadratic model fits L_DH much less cleanly than it fits the GRH-type controls zeta and L(chi_5). This aligns with the project framing that Front I is spectral phenomenology rather than operator identification: the discriminating signal lies in reconstruction quality and robustness, not in discovering a qualitatively distinct law for the coefficients. The result is also consistent with the broader control logic of the dataset. zeta and zeta_delta were exactly indistinguishable in Front I because this pipeline depends only on the zero imaginary parts; that reproduces the documented blindness of standard Jacobi reconstruction to the specific zeta_delta deformation. Thus, Front I should not be interpreted as a pure detector of off-line-zero perturbations in the current implementation. Instead, its utility here is descriptive and comparative: among spectra that differ in arithmetic structure, L_DH remains the standout in residual roughness and somewhat greater weight-instability. That is meaningful for the stated hypothesis, but it must not be overstated as a direct RH-sensitive signature without the Step 0.5 power calibration and a complete equal-N Delta control. A further scientific point is that the weight audit matters. The non-canonicity of gamma_n -> T_N means any claimed Front I signature must survive changes in spectral weight. In this analysis the winning model class did survive universally, which strengthens the “shared model class” conclusion. The quantitative parameters shifted modestly for the main GRH controls and somewhat more strongly for L_DH, especially for b_n, reinforcing the interpretation that L_DH’s distinguishing feature is not the form of the fit but its reduced stability and increased residual structure.
</discussion>
<proposed-next-hypotheses>
1. After completing a full N=5000 Ramanujan-Delta zero list, the log-quadratic model will remain AIC/BIC-optimal for Delta’s a_n and b_n, and its normalized residual scale will stay in the same low range as zeta and L(chi_5), below the corresponding L_DH values.
2. Under additional admissible spectral weights beyond uniform and 1/|rho|^2, the identity of the winning model class for all controls will remain log-quadratic, but L_DH will continue to exhibit systematically larger parameter drift in b_n than zeta and L(chi_5).
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>lchi5_zeros_N5000_dps80.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Generated in this session using PARI via cypari2 with lfuncreate([znstar(5,1),[1]]) and lfunzeros over height intervals, then truncated to the first 5000 zeros. The filename reflects the intended precision target from the project objective, but PARI returned only about 19–20 significant digits, consistent with the dataset caveat. The file contains the imaginary parts of the first 5000 critical-line zeros for the primitive order-4 Dirichlet character mod 5.</artifact-description>
</artifact>
<artifact>
<file-name>ldelta_zeros_N1298_dps80.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Partial Ramanujan-Delta zero list generated in this session using PARI modular-form routines mfinit([1,12],1), mfDelta(), lfunmf, and lfunzeros. Runtime constraints prevented completion of the requested N=5000 list, so this artifact contains only the first 1298 zeros obtained before timeout. It was used only for a partial Front I comparison and should not be treated as a complete N=5000 control.</artifact-description>
</artifact>
<artifact>
<file-name>front1_model_selection.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table of AIC/BIC model-selection results for all analyzed coefficient sequences. Each row records the function, coefficient type, weight choice, AIC/BIC values for constant, log-linear, and log-quadratic fits, the winning model, and residual summaries. It was created from ordinary least-squares fits to the stable-window Jacobi coefficients.</artifact-description>
</artifact>
<artifact>
<file-name>front1_logquad_params.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table of fitted log-quadratic parameters c0, c1, c2 and residual standard deviations for each function, coefficient type, and spectral weight. It summarizes the direct cross-control comparison of the selected Front I model. The values were extracted from the OLS fits used in model selection.</artifact-description>
</artifact>
<artifact>
<file-name>front1_spectral_audit.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Spectral-weight audit table comparing log-quadratic fit parameters under uniform and 1/|rho|^2 weights. It reports parameter values, relative parameter shifts, and residuals for each function and coefficient type. This artifact was created to assess whether Front I conclusions survive a change of spectral measure.</artifact-description>
</artifact>
<artifact>
<file-name>front1_jacobi_coefficients_N5000.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing reconstructed a_n and b_n sequences for each analyzed function under uniform and 1/|rho|^2 weights. The coefficients were produced by Lanczos tridiagonalization of the discrete zero spectra with double Gram-Schmidt reorthogonalization. For L_Delta the stored sequences correspond to the partial N=1298 dataset, not a full N=5000 reconstruction.</artifact-description>
</artifact>
<artifact>
<file-name>front1_summary_figure.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final summary figure containing two vertically stacked panels: residuals of a_n after log-quadratic fitting, and a bar chart of relative residual scales across controls, coefficient types, and weight choices. It was created with matplotlib at 300 dpi to summarize the core Front I result. A PDF version with the same content was also saved.</artifact-description>
</artifact>
<artifact>
<file-name>front1_summary_figure.pdf</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>PDF version of the final Front I summary figure. It contains the same two-panel visualization as the PNG file and was produced directly from the notebook analysis. This figure summarizes the model-class agreement and the elevated residual variance of L_DH.</artifact-description>
</artifact>
</artifacts>
</output>
