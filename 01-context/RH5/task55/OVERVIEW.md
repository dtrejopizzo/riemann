## Overview <output>
<conclusion>
Using direct numerical integration of central-line values up to T=4000, the Riemann zeta function is broadly consistent with the Keating–Snaith moment predictions at this finite height, while the Davenport–Heilbronn function L_DH shows a large upward deviation in both second and fourth moments; I could not complete a valid Ramanujan Δ or corrected Dirichlet-character panel within the time and data available.
</conclusion>
<methods>
I first validated the available zero-list inputs locally in /workspace/ea35b3fb-1b6a-4c62-bcf8-209857918dcc. The files present were zeta_zeros_N5000_dps50.npy, ldh_zeros_N5000_dps50.npy, lchi5_zeros_N5000_dps80.npy, and ldh_off_line_zeros.csv; no L(Delta,s) N=5000 file and no zeta_delta file were present in the workspace. I checked the zeta R2 gate by confirming the first three ordinates matched the documented values. For L_DH, I defined the classical Davenport–Heilbronn function via Hurwitz zeta combinations with kappa = (sqrt(10-2*sqrt(5)) - 2)/(sqrt(5)-1), and verified that a documented off-line zero gave |L_DH(rho)| ≈ 2.39e-6 and a documented critical-line zero gave |L_DH(rho)| ≈ 3.95e-31. Because the requested explicit-formula moment computation from zeros alone was not completed in the allotted runtime, I estimated the moments by direct numerical quadrature of |L(1/2+it)| on a uniform grid. Specifically, I sampled t on 0.2-spaced points from 0.2 to 4000.0 (20,000 points) and evaluated: (i) |zeta(1/2+it)| using mpmath.siegelz, (ii) |L_DH(1/2+it)| using the Hurwitz-zeta definition above, and (iii) an initial Dirichlet-L function using mpmath.dirichlet. I then computed cumulative trapezoidal integrals to form both the research-objective moments I_k(T) = (1/T)∫_0^T |L(1/2+it)|^k dt for k=1,2 and the standard Keating–Snaith-compatible even moments M_2(T) = (1/T)∫_0^T |L|^2 dt and M_4(T) = (1/T)∫_0^T |L|^4 dt. For the Keating–Snaith comparison, I used the standard unitary predictions M_2(T) ~ c_1 log T and M_4(T) ~ c_2 (log T)^4, with zeta constants c_1 = 1 and c_2 = 1/(2π^2) ≈ 0.05066. I also examined effective exponents by linear regression of log M_{2k}(T) against log log T over T in [100,4000]. A critical limitation emerged late in the analysis: the local file lchi5_zeros_N5000_dps80.npy did not match the initially assumed quartic character modulo 5. Testing showed its first zero annihilated the real quadratic character [0,1,-1,-1,1], not the order-4 complex character [0,1,i,-i,-1]. I therefore could not trust the initially computed Dirichlet-L moment panel and did not use it as a primary conclusion.
</methods>
<results>
Quantitative results at T = 4000 were: 1) For the research-objective convention I_k(T) = (1/T)∫ |L|^k dt:
- zeta: I_1 = 1.7765, I_2 = 6.6285
- L_DH: I_1 = 3.6089, I_2 = 21.4883
- Initial Dirichlet-L run (later found to use the wrong character): I_1 = 1.8095, I_2 = 7.2222 2) For the standard Keating–Snaith-compatible moments:
- zeta: M_2 = 6.6285, M_4 = 272.3637
- L_DH: M_2 = 21.4883, M_4 = 1707.6821
- Initial Dirichlet-L run with wrong character: M_2 = 7.2222, M_4 = 379.9919 3) Ratios to the zeta Keating–Snaith scaling at T = 4000, with log T = 8.2940:
- zeta: M_2/log T = 0.7992 versus asymptotic prediction 1.0000
- zeta: M_4/(log T)^4 = 0.05755 versus asymptotic prediction 0.05066
- L_DH: M_2/log T = 2.5908
- L_DH: M_4/(log T)^4 = 0.36086 4) Percentage differences from the zeta asymptotic constants at T = 4000:
- zeta second moment ratio: -20.1% relative to c_1 = 1.0
- zeta fourth moment ratio: +13.6% relative to c_2 = 1/(2π^2)
- L_DH second moment ratio relative to zeta c_1: +159.1%
- L_DH fourth moment ratio relative to zeta c_2: about +612.3% 5) Effective scaling exponents from fits of log M_{2k}(T) versus log log T on T in [100,4000]:
- zeta M_2: slope 1.3328
- zeta M_4: slope 4.0553
- L_DH M_2: slope 0.8033
- L_DH M_4: slope 2.5335
- Initial Dirichlet-L run with wrong character: M_2 slope 0.9001, M_4 slope 2.8705 6) Character-identification check for the local Dirichlet-L zero file:
- Using the initially assumed complex quartic character [0,1, i, -i, -1], |L(1/2 + i*gamma_1)| at the file’s first zero gamma_1 = 6.6484533447... was about 0.5020, not 0.
- Using the real quadratic character [0,1,-1,-1,1], |L(1/2 + i*gamma_1)| was about 4.36e-26, confirming the local zero file corresponds to the real quadratic character instead.
</results>
<challenges>
I cannot complete the full five-function requested analysis because two required zero lists were not available in the workspace: the Ramanujan Delta L-function N=5000 list was absent/incomplete, and no zeta_delta control file was present locally. I also cannot claim a completed explicit-formula-from-zeros calculation because the implemented workflow estimated moments by direct central-line quadrature rather than a finished Guinand–Weil zero-sum derivation. Additional technical and methodological issues occurred. First, the initial Dirichlet-L analysis used the wrong modulo-5 character; this was detected only after comparing the supplied zero list against direct function evaluations. Because time expired before recomputing that panel with the corrected character, those Dirichlet-L moment values should be treated as invalid for inference. Second, numerical quadrature on a fixed 0.2 grid up to T=4000 introduces deterministic discretization error that I did not fully quantify by grid-refinement analysis. Third, the Keating–Snaith predictions are asymptotic and convergence is known to be slow, especially for the second moment because lower-order terms are substantial at modest T. Fourth, no formal statistical test of “significance” was completed; the deviations reported are quantitative effect-size comparisons to asymptotic constants, not p-value-based hypothesis tests.
</challenges>
<discussion>
Within the subset I could validate, the zeta results are qualitatively consistent with the standard unitary Keating–Snaith framework: the normalized fourth moment was close to the expected constant and the fitted fourth-moment log-log-log slope was very close to 4. The second-moment normalized ratio for zeta was below 1, but this is not surprising at T=4000 because the classical lower-order terms in the zeta second moment are large relative to log T at this height. In contrast, L_DH showed much larger normalized moments than zeta and substantially different effective growth, especially for the fourth moment. This supports the stated hypothesis at least qualitatively: the non-Euler-product, off-line-zero control does not behave like the GRH-satisfying zeta benchmark under these moment diagnostics. However, the evidence is incomplete. I did not finish a correct quadratic-character Dirichlet panel, and I did not analyze Ramanujan Delta. Therefore I cannot make the stronger panel-wide claim that all GRH-satisfying controls closely follow their symmetry-specific RMT constants while L_DH alone deviates. The strongest defensible statement is narrower: among the functions I validated numerically, zeta appears broadly compatible with the expected asymptotic moment scaling at finite T, while L_DH exhibits a markedly inflated moment profile.
</discussion>
<proposed-next-hypotheses>
1. After recomputing the correct real quadratic L-function modulo 5, its normalized second and fourth moments M_2/log T and M_4/(log T)^4 will stay much closer to the zeta/RMT constants than the corresponding L_DH ratios over the same T range.
2. The inflated L_DH moments are driven disproportionately by neighborhoods of off-line zeros, so removing or separately windowing intervals near those ordinates will reduce the gap between L_DH and zeta in the normalized moment ratios.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>abs_zeta_grid.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy array of sampled values |zeta(1/2+it)| on the uniform grid t = 0.2, 0.4, ..., 4000.0. Created with mpmath.siegelz at low working precision for numerical quadrature of central-line moments.</artifact-description>
</artifact>
<artifact>
<file-name>abs_lchi5_grid.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy array of sampled values from the initial Dirichlet-L run on t = 0.2, 0.4, ..., 4000.0. This artifact was generated using an incorrect modulo-5 character and should be treated as invalid for scientific conclusions.</artifact-description>
</artifact>
<artifact>
<file-name>abs_ldh_grid.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy array of sampled values |L_DH(1/2+it)| on the uniform grid t = 0.2, 0.4, ..., 4000.0. Created from the Hurwitz-zeta representation of the Davenport–Heilbronn function for numerical quadrature of central-line moments.</artifact-description>
</artifact>
<artifact>
<file-name>lf_helpers.py</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Python helper module used to batch-evaluate zeta, the initial Dirichlet L-function, and L_DH on grid points for multiprocessing-based sampling. It includes the initial incorrect Dirichlet-character specification and is retained only for reproducibility of the partial run.</artifact-description>
</artifact>
<artifact>
<file-name>lf_helpers2.py</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Partial helper module created to recompute the modulo-5 Dirichlet L-function using the corrected real quadratic character [0,1,-1,-1,1]. The corrected recomputation did not complete before runtime expiration.</artifact-description>
</artifact>
</artifacts>
</output>
