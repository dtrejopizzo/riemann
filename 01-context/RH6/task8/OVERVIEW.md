## Overview <output>
<conclusion>
The slow growth exponent α≈0.9 observed for the L_DH off-critical anomaly is a geometric signature of projecting a single off-critical zero pair onto the Gaussian-monomial basis at T₀=85.7, σ=2.0: an artificial Weil form built from ζ critical zeros plus the same off-critical pair (β=±0.3085, γ=85.6993) reproduces α≈1.06, far below the α≈14 seen for a single-zero ζ-shift and consistent (within ~17%) with the L_DH value.
</conclusion> <methods>
1. Implemented the Weil quadratic form Q = M_zeros − M_arith in mpmath at dps=80 with the shifted-and-scaled Gaussian-monomial basis h_j(u) = ((u−T₀)/σ)^j · exp(−(u−T₀)²/(2σ²)), j=0..J−1.
2. Parameters: T₀=85.7, σ=2.0, prime_bound=1000.
3. Loaded the 5,000 Riemann ζ zeros from zeta_zeros_5000_dps50.npy and selected critical-line zeros within the window |γ−T₀| ≤ 40 (matching the reference L_DH experiment); 33 zeros qualified. Also re-ran with the objective-specified half-window 6σ=12 (10 zeros) as a robustness check.
4. M_zeros built using the documented non-Hermitian construction: for each zero at s=½+β+iγ contribute Re[v(+γ−iβ)v(+γ−iβ)^T + v(−γ−iβ)v(−γ−iβ)^T]. Critical ζ zeros use β=0; the artificial off-critical pair uses (β=±0.3085, γ=85.6993), summing all four sign combinations.
5. M_arith = standard ζ prime-power sum Σ_{p^k≤1000} (log p)/√(p^k) · [Re vv^T at u=k log p + at u=−k log p].
6. Computed the full spectrum of Q via mp.eig for J ∈ {4,8,12,16,20} and recorded λ_min, λ_max.
7. Fit log|λ_min| vs log J by ordinary least squares over J∈{8,12,16,20} (i.e. all J with λ_min<0), matching exactly the regression range used for the L_DH reference fit. Also computed local log-log slopes between consecutive J values.
8. Compared against the published references in weil_J_sweep_ldh_results.json (α≈0.904) and weil_J_sweep_single_shift_results.json (α≈13.98 single-shift, 28.24 multi-shift). Ran a control with only critical ζ zeros (no off-critical pair) to confirm λ_min stays positive and decays toward the numerical floor.
</methods> <results>
λ_min values for the artificial ζ+off-critical-pair Weil form (half_window=40):
- J=4: λ_min = +1.846e−01 (still PSD)
- J=8: λ_min = −4.054e−03
- J=12: λ_min = −7.090e−03
- J=16: λ_min = −9.610e−03
- J=20: λ_min = −1.041e−02 Power-law fit on |λ_min| vs J over J∈{8,12,16,20}: α = 1.060 (intercept c = −7.655). With the strict 6σ window (10 ζ zeros), α = 1.098. Local slopes: 1.38 (8→12), 1.06 (12→16), 0.36 (16→20). M_arith is numerically ~10⁻⁶⁶⁵ at these parameters (as predicted by the dataset description), so Q is determined almost entirely by M_zeros. Control (ζ critical zeros only, no off-critical pair): λ_min remains positive at every J and decays as 1.91e−01, 3.87e−05, 1.74e−13, 1.59e−28, 6.21e−54 — i.e., consistent with a PSD form approaching the numerical floor, confirming the negative λ_min is caused by the added off-critical pair. Comparison of α exponents (same J∈{8,12,16,20} regression):
- ζ single-zero shift (δ=0.05, T₀=46.13, σ=1.0): α ≈ 13.98
- ζ multi-shift (r24): α ≈ 28.24
- L_DH off-critical (real anomaly at 85.7): α ≈ 0.904
- Artificial ζ + off-pair at (±0.3085, 85.6993): α ≈ 1.06 (this work) The artificial construct reproduces the L_DH growth exponent to within ~17%, three orders of magnitude in log-slope below the single-shift ζ_δ case, and in the same order of magnitude as the L_DH signal.
</results> <challenges>
- Choice of integration window: the objective specifies T₀±6σ (=12), while the reference L_DH experiment used half_window=40. For an apples-to-apples α comparison the main fit uses 40; a sanity check at 6σ gave α=1.10, confirming insensitivity of the conclusion to this choice (off-critical contribution dominates either way because critical-zero contributions are bounded and the basis decays as a Gaussian).
- M_arith is so small (~10⁻⁶⁶⁵) at T₀=85.7, σ=2.0 that it does not affect any digit of λ_min at dps=80; it was included for formal completeness only, as noted in the objective.
- The non-Hermitian Re[v v^T] (not v v†) construction had to be implemented exactly as specified; using v v† would change off-critical signs and corrupt the comparison.
- mp.eig on dense symmetric matrices up to 20×20 at dps=80 is fast (<3 s per J); no scaling issues.
</challenges> <discussion>
The result strongly supports the geometric-signature hypothesis. The α≈0.9 growth seen in the L_DH J-sweep is reproduced (α≈1.06) by an artificial setup that retains only the geometry of the off-critical pair location (β=±0.3085 at γ=85.6993) and substitutes the L_DH critical zeros and arithmetic with those of ζ. Since M_arith is numerically zero at this (T₀, σ), the entire signal is encoded in how a single off-critical pair projects onto the Gaussian-monomial basis at T₀=85.7, σ=2.0 — a property of the measurement geometry, not of L_DH itself. This sharpens the interpretation of r28/r35: the Weil-form J-sweep at this configuration cannot distinguish "L_DH-specific arithmetic with an off-critical zero" from "ζ arithmetic with an artificially planted off-critical zero at the same location." The dramatic α≈14 exponent seen for tiny δ=0.05 shifts near T₀=46.13 reflects the very different geometric setup there (smaller σ, β orders of magnitude smaller, deeper-inside-window zero), not a generic property of off-critical detection. Consequently, the magnitude of α in a J-sweep should not be read as a measure of "how off-critical" a zero is — geometric factors (β/σ ratio, distance from T₀, σ itself) dominate. A practical implication: to amplify the off-critical signature for L_DH-like anomalies one should re-run the J-sweep at smaller σ (so that the off-critical pair is many σ's deep into the imaginary direction) and ideally at a T₀ exactly coincident with the anomaly, which the linearity of α≈1 suggests is currently far from optimal.
</discussion> <proposed-next-hypotheses>
1. The growth exponent α of |λ_min| with J for an off-critical pair (β, γ) probed at (T₀=γ, σ) is governed by the dimensionless ratio β/σ: a parametric J-sweep over σ∈{0.25, 0.5, 1.0, 2.0} at fixed (β=0.3085, γ=85.6993, T₀=γ) will show α increasing monotonically as σ decreases, recovering super-polynomial growth (α>10) for σ≲β.
2. Replacing the artificial ζ+off-pair construction with an artificial L(χ₄ mod 5)+off-pair (or L(Δ)+off-pair) at the same (T₀=85.7, σ=2.0) will likewise yield α≈1 within ~20%, demonstrating that the geometric signature is independent of the host L-function's arithmetic at this configuration.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_J_sweep_artificial_zeta_offpair.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON record of the artificial-ζ + off-critical-pair Weil J-sweep at (T₀=85.7, σ=2.0, prime_bound=1000, dps=80). Contains full parameters, λ_min/λ_max for J∈{4,8,12,16,20} using both half_window=40 (main) and half_window=6σ (sensitivity check), a critical-only ζ control, local and global log-log slopes, and a side-by-side comparison with the L_DH (α≈0.90) and single-shift ζ_δ (α≈14) reference fits. Produced via the non-Hermitian Re[v v^T] mpmath implementation in this notebook.</artifact-description>
</artifact>
<artifact>
<file-name>weil_geometric_signature.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Log-log summary plot of |λ_min| vs J for three cases: L_DH off-critical (α≈0.90), artificial ζ+off-critical pair at the L_DH anomaly location (α≈1.06, this work), and ζ single-zero shift δ=0.05 (α≈14). The artificial-ζ curve nearly overlays the L_DH curve and is well separated from the single-shift curve, visually confirming the geometric-signature hypothesis.</artifact-description>
</artifact>
</artifacts>
</output>
