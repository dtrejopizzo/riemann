## Overview <output>
<conclusion>
The hypothesis is refuted: centering the Weil basis on the displaced ζ zero γ₂₃ does NOT modestly increase the growth exponent α — instead it collapses |λ_min| super-exponentially (fitted α ≈ −97 over J=8..20), demonstrating that off-center placement is not a minor confounder but rather the dominant geometric ingredient that produces the positive growth signal seen in r55 (α ≈ 3.76).
</conclusion> <methods>
1. Loaded the validated ζ zero list `zeta_zeros_5000_dps50.npy` and selected the 33 zeros in the window [T₀−40, T₀+40] around T₀ = γ₂₃ = 84.735492980517050105735311206827741417106627934241.
2. Built the Gaussian-modulated monomial basis h_i(z) = exp(−(z−T₀)²/(2σ²))·(z−T₀)^i with σ=2.0 at mpmath dps=80.
3. Constructed M_zeros via the asymmetric single-zero displacement protocol: for each γ in the window, formed Re[v(+)v(+)ᵀ + v(−)v(−)ᵀ] with v(±) = h(±γ − iβ_g) where β_g = β = 0.3085 only for γ₂₃ and 0 for all other zeros (matching r55's formula).
4. Constructed M_arith as Σ_{p^k ≤ 10⁵} (log p)/√(p^k) · [h(k log p)h(k log p)ᵀ + h(−k log p)h(−k log p)ᵀ] using all 9,700 prime-power terms (9,592 primes ≤ 10⁵).
5. Formed Q = M_zeros − M_arith for J ∈ {4, 8, 12, 16, 20}, verified bit-exact symmetry, and computed eigenvalues with mp.eig.
6. Performed log-log power-law fits of |λ_min| vs J over J=8..20 for both the shifted system and a critical-only control (β=0 for all zeros) using the identical basis and identical M_arith.
7. Compared with r55 (T₀=85.6993, off-center by 0.964 from γ₂₃; α=3.76).
</methods> <results>
On-center (T₀ = γ₂₃) |λ_min| sequence (shift): J=4 → 5.57×10⁻¹; J=8 → 9.43×10⁻²; J=12 → 3.84×10⁻⁸; J=16 → 6.58×10⁻²²; J=20 → 3.50×10⁻⁴².
On-center critical-only control |λ_min|: J=4 → 6.52×10⁻¹; J=8 → 2.73×10⁻⁵; J=12 → 1.05×10⁻¹⁴; J=16 → 1.07×10⁻²⁹; J=20 → 6.13×10⁻⁴⁸. Power-law fits (J=8..20):
• On-center shift α = −97.45 (super-exponential collapse, not a positive growth signal).
• On-center critical-only control α = −104.43.
• |λ_max| α = +51.02 (same magnitude as r55, indicating geometric growth is intrinsic to the basis, not the perturbation). Comparison with r55 (off-center, T₀=85.6993, otherwise identical parameters):
• r55 α = +3.76 (positive growth) vs. on-center α = −97.45 → Δα = −101.2.
• Shift/control ratio of |λ_min| grows by ~13 orders of magnitude with J for r55 (off-center), but only ~7 orders for on-center, and that growth is non-monotonic (peaking at J=16 and reversing at J=20). The on-center shift behaves qualitatively like the r55 critical-only control: it collapses with J. The displacement signal therefore vanishes when the basis is centered on the perturbed zero.
</results> <challenges>
At J=20 the on-center |λ_min| reaches 10⁻⁴² while |λ_max| ≈ 8×10²⁷, a ratio of ~10⁷⁰ that approaches the limits of dps=80 arithmetic. Fits restricted to J=8..16 give similar conclusions (α_shift ≈ −64.9, α_ctrl ≈ −79.3), confirming the qualitative result is not a precision artifact. The mpmath eigensolver scales steeply: J=20 required ~44 s per matrix; total wall time for the sweep was under 5 minutes. No other issues were encountered.
</challenges> <discussion>
This experiment cleanly isolates the role of basis placement in the Weil-form spectral diagnostic. The r55 result (α ≈ 3.76 for ζ vs. α ≈ 0.90 for L_DH at the same off-center geometry) had been interpreted as a possible signature of an intrinsic structural difference between ζ and L_DH. The present finding shows that the off-center geometry is not a minor confounder — it is the actual generator of the positive growth exponent in |λ_min|. When the basis is centered exactly on the displaced zero, the Gaussian envelope makes the asymmetric perturbation a near-symmetric, well-resolved local feature; the zero-side and arithmetic-side contributions effectively cancel inside the basis's effective support, returning the system to critical-line-like behavior with super-exponentially collapsing |λ_min|. Consequently, the previously observed r28/r55 "L_DH α≈0.90 vs ζ α≈3.76" gap cannot be attributed straightforwardly to intrinsic structural differences without controlling for the basis offset to the perturbed zero. The Weil-form spectral signal observed in these experiments is strongly geometric in origin: it requires the perturbation to lie at a non-trivial offset from the Gaussian basis center. This has direct methodological implications for any future use of Q-eigenvalue growth as a structural diagnostic for L-functions: the offset must be matched across functions (or systematically swept) before structural interpretations are justified.
</discussion> <proposed-next-hypotheses>
1. The growth exponent α of |λ_min| as a function of basis offset δ = |T₀ − γ_shift| (with σ, β, J held fixed) follows a smooth curve that increases from a strongly negative value at δ=0, crosses zero, and saturates near δ ≈ σ; if this curve is the same shape for ζ and L_DH after rescaling by their local zero density, the apparent "intrinsic structural" α gap will disappear.
2. The collapse of |λ_min| at the on-center configuration is driven by a near-Gaussian quadrature identity between the shifted-zero contribution and the leading low-order prime-power terms; replacing the Gaussian envelope by an off-center compactly supported window will restore α > 0 even when T₀ is centered on γ_shift.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_J_sweep_zeta_oncenter_gamma23_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Full record of the on-center Weil J-sweep experiment: parameters (T₀=γ₂₃, σ=2.0, β=0.3085, half-window=40, prime_bound=10⁵, dps=80, 33 zeros in window), λ_min/λ_max for J ∈ {4,8,12,16,20} for both the shifted ζ and the critical-only control, power-law fits over J=8..20 and J=8..16, local log-log slopes, and a direct numerical comparison against r55. Produced by reconstructing the M_zeros − M_arith Weil form with the validated r55 Gaussian-monomial basis recipe at mpmath dps=80.</artifact-description>
</artifact>
<artifact>
<file-name>weil_oncenter_vs_offcenter.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: |λ_min| vs J on log scale, comparing r55 (T₀=85.6993, off-center, blue solid) with on-center (T₀=γ₂₃, red solid) for both the shifted system and the critical-only control (dashed). Panel B: ratio |λ_min|(shift) / |λ_min|(crit-only) vs J, showing the displacement signal grows ~13 orders of magnitude in r55 but only ~7 orders (and non-monotonically) in the on-center case.</artifact-description>
</artifact>
</artifacts>
</output> 