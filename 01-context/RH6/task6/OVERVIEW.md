## Overview <output>
<conclusion>
The Weil form does detect the real Davenport–Heilbronn anomaly near t≈85.7, but in this implementation its minimum eigenvalue does not show the super-polynomial negative growth seen previously for ζ_δ; instead, λ_min becomes negative only for J≥8 and its magnitude grows slowly.
</conclusion>
<methods>
I followed a three-step analysis plan. (1) I loaded the provided zero lists `ldh_zeros_partial_dps50.npy` and `lchi_zeros_5000_dps50.npy`, verified their shapes and contents, and used `mpmath` high-precision arithmetic with `mp.dps=80` throughout matrix construction and eigensolution. I also inspected the prior artifact `weil_J_sweep_results.json` to recover the validated r24 Weil-form convention. (2) I re-implemented the Weil quadratic form as Q = M_zeros − M_arith using the non-Hermitian zero-side construction `Re[v v^T]`, not `v v^H`, with basis functions `h_i(t) = ((t−T0)/sigma)^i * exp(-((t−T0)/sigma)^2/2)` for i=0,…,J−1, centered at `T0=85.7` and `sigma=2.0`, over J ∈ {4, 8, 12, 16, 20}. For each zero `rho = 1/2 + beta + i*gamma`, I added the functional-equation pair contributions `Re[h(+gamma − i beta) h(+gamma − i beta)^T] + Re[h(−gamma − i beta) h(−gamma − i beta)^T]`. I used a zero window of `|gamma−T0| ≤ 40`, which included 49 listed critical-line L_DH zeros and 53 control L(χ₄ mod 5) zeros. Because the provided L_DH zero file contains only critical-line zeros, I numerically refined the known off-critical pair from `ldh_def.py` using `mpmath.findroot` on `L_DH`, obtaining a positive-height pair at `gamma = 85.699348485377592...` with real-part offsets `beta = ±0.308517182456637...`. (3) For the arithmetic side, I used prime powers up to `prime_bound=1000`. For the control Dirichlet L-function, I used `Lambda_chi(p^k) = chi(p)^k log p` and inserted `Re[Lambda_chi(p^k)] / sqrt(p^k)` into `M_arith`. For L_DH, since it has no Euler product, I derived logarithmic-derivative coefficients recursively from its Dirichlet coefficients `c_n = A chi(n) + B chi_bar(n)`, using the recurrence `c_{p^k} * k log p = sum_{j=1}^k Lambda_DH(p^j) c_{p^{k-j}}`, and then formed `M_arith` with `Re[Lambda_DH(p^k)] / sqrt(p^k)`. I computed eigenvalues with `mpmath.eig`, extracted `lambda_min` and `lambda_max`, compared the L_DH growth pattern to the prior `ζ_δ` sweep from `weil_J_sweep_results.json`, saved the numeric results to `weil_J_sweep_ldh_results.json`, and created the final summary figure `weil_J_sweep_ldh_summary.png`.
</methods>
<results>
Data inclusion: the analysis window `[45.7, 125.7]` contained 49 listed L_DH critical-line zeros and 53 control L(χ₄ mod 5) zeros. The refined positive-height off-critical L_DH zeros were at `1/2 ± 0.308517182456637... + i*85.699348485377592...`. Control L(χ₄ mod 5): `lambda_min(Q)` remained positive for all tested J, with values
- J=4: 2.2896e-01
- J=8: 2.9943e-02
- J=12: 3.4375e-03
- J=16: 1.1951e-06
- J=20: 3.3363e-13
This is consistent with decay toward a numerical floor rather than emergence of a negative mode. L_DH using only the listed critical-line zeros: `lambda_min(Q)` also remained positive,
- J=4: 6.5459e-02
- J=8: 7.1248e-04
- J=12: 2.2841e-07
- J=16: 7.0898e-13
- J=20: 2.4008e-21
showing no negative instability from the critical-line zeros alone. L_DH with the refined off-critical pair included: `lambda_min(Q)` was
- J=4: 1.7293e-01
- J=8: -1.5690e-02
- J=12: -1.8983e-02
- J=16: -2.8436e-02
- J=20: -3.4950e-02
Thus negativity appears from J=8 onward, confirming that the Weil form detects the anomaly when the off-critical pair is included. The corresponding `lambda_max(Q)` values for L_DH with off-critical pair were 5.2565e+00, 2.5708e+03, 1.5512e+07, 4.4427e+11, and 3.9046e+16 for J=4,8,12,16,20 respectively, indicating rapidly increasing matrix scale/conditioning with J. Growth-rate comparison with prior `ζ_δ` result from `weil_J_sweep_results.json`: for L_DH with off-critical pair, local log-log slopes of `|lambda_min|` across successive J intervals were
- 4→8: -3.462
- 8→12: 0.470
- 12→16: 1.405
- 16→20: 0.924
The negative first slope reflects the fact that J=4 had not yet entered the detecting regime (`lambda_min>0`). Restricting attention to J≥8, the growth was mild. A power-law fit on J={8,12,16,20} gave exponent `alpha = 0.904`; an exponential fit gave rate `a = 0.0702`; and a `J log J` fit gave coefficient `a = 0.0194`. By contrast, the prior `ζ_δ` sweep had local log-log slopes about 5.97, 16.75, 29.93, and 50.58, with `|lambda_min|` growing from 1.81e-04 at J=4 to 4.43e+09 at J=20. Therefore the L_DH growth is quantitatively and qualitatively much weaker than the prior ζ_δ benchmark.
</results>
<challenges>
The main methodological challenge is that the Davenport–Heilbronn function does not have an Euler product, so there is no standard prime-sum arithmetic side identical to the zeta/Dirichlet-L explicit formula case. I therefore had to construct a nonstandard but well-defined arithmetic side from the Dirichlet-series logarithmic derivative of L_DH itself via a prime-power recurrence. This choice is principled, but it is also a limitation: a different normalization or explicit-formula convention for non-Euler-product functions could change the absolute scale of Q. A second challenge is that the provided `ldh_zeros_partial_dps50.npy` contains only critical-line zeros, so the known off-critical anomaly was not present directly in the file and had to be added by numerically refining the root with `ldh_def.py`; if that off-critical pair were omitted, no negative λ_min would appear. A third challenge is numerical conditioning: `lambda_max` grows to ~3.9e16 by J=20, confirming the need for high precision. Finally, the comparison with prior `ζ_δ` is not perfectly apples-to-apples because the earlier experiment used a different center (`T0≈46.13`), width (`sigma=1.0`), and an artificial deformation affecting multiple zeros in the window, whereas the L_DH case involves a real anomaly localized to one off-critical pair.
</challenges>
<discussion>
The analysis supports the practical utility of the Weil form as a detector of a real off-critical anomaly: once the actual L_DH off-critical zero pair is included, the minimum eigenvalue becomes negative for moderate basis size (J≥8), while both the control L(χ₄ mod 5) and the L_DH critical-line-only calculation remain nonnegative up to numerical floor. That qualitative separation is exactly the detection behavior desired from the method. However, the stronger research hypothesis—that the negative mode would grow super-polynomially with J in a way analogous to or distinct-from-but-comparable-to `ζ_δ`—is not supported by these results. In this implementation, the L_DH anomaly produces only a modest increase in `|lambda_min|` over J=8→20. Scientifically, this suggests that the dramatic r24 growth for `ζ_δ` was not a universal signature of every off-critical configuration, but rather a property of that specific artificial deformation and parameter regime. The result also highlights that “detectability” and “growth rate” are separate questions: the L_DH anomaly is detectable, but not with the same amplification pattern as the earlier synthetic benchmark. Because the arithmetic side for L_DH is necessarily nonstandard here, this conclusion should be interpreted as conditional on the adopted explicit-formula generalization.
</discussion>
<proposed-next-hypotheses>
1. For the Davenport–Heilbronn function, the sign change in `lambda_min(Q)` is robust to reasonable changes in `sigma` and half-window around `T0≈85.7`, but the growth rate of `|lambda_min|` with J remains sub-super-polynomial over J≤20.
2. If an artificial deformation is applied to the control L(χ₄ mod 5) that shifts only one zero pair by a real-part offset comparable to the L_DH anomaly, then the resulting `|lambda_min|` growth with J will resemble the mild L_DH pattern more closely than the dramatic multi-zero `ζ_δ` benchmark.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>weil_J_sweep_ldh_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON file containing the full L_DH and control J-sweep results, including parameters, refined off-critical zero location, and eigenvalue tables for J in {4,8,12,16,20}. It was created from a high-precision mpmath implementation of the Weil form using the provided zero lists and the L_DH definition in `ldh_def.py`.</artifact-description>
</artifact>
</artifacts>
</output>
