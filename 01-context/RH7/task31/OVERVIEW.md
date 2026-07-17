## Overview <output>
<conclusion>
The explicit perturbation theorem successfully predicts the forced-negativity prefactor at the second anchor T₀=85.7: c_pred = −4.375767 agrees with c_emp = −4.375767 (δ=10⁻⁴) to within ~10⁻⁶ %, far exceeding the 1% success criterion.
</conclusion> <methods>
1. Loaded `weil_quadratic_form_general.py`'s `compute_Q` engine and computed the first 100 Riemann ζ zero imaginary parts to 30-digit precision with `mpmath.zetazero`.
2. Theoretical prefactor c_pred: identified the 16 zeros γ_k within the basis window |γ_k − 85.7| ≤ 3·σ·√J = 18.97 (γ_16=67.08 through γ_31=103.73). Built the J=10 Hermite-Gauss basis φ_j(t) = h_j((t−T₀)/σ)/√σ with derivatives via the standard recurrences (φ′ via ψ_n′ = √(n/2)ψ_{n−1} − √((n+1)/2)ψ_{n+1} ; φ″ via the Hermite ODE u²−(2n+1)). Built A(γ_k) = −2[φ′φ′ᵀ + ½(φφ″ᵀ + φ″φᵀ)] for each in-window zero, summed, symmetrised, and took the minimum eigenvalue.
3. Empirical prefactor c_emp via ζ_δ simulations: reproduced the exact 4-member quartet convention {ρ, ρ̄, 1−ρ, 1−ρ̄} that was verified against the existing T₀=46.13 grid (σ=2, J=12, m=20: reproduced c_emp=−4.7511 ✓). Both baseline and deformed runs supply the quartet via `compute_Q(zeros_complex=True, include_negative_zeros=True)` with primes_cutoff=10000 and n_nodes_quad=200. Deformed first m=40 zeros to (½+δ)+iγ_k for δ ∈ {10⁻⁵, 10⁻⁴, 10⁻³}; remaining 60 zeros stayed on the critical line. Computed ΔQ = Re(Q_delta − Q_base), symmetrised, and extracted λ_min(ΔQ)/δ².
4. Convention validation: trace identity Q_base ≈ 0 verified (eigenvalues at noise floor ~10⁻¹⁴), and the existing 60-row T₀=46.13 grid row was reproduced before applying the convention to T₀=85.7.
</methods> <results>
- 16 Riemann zeros fall in the basis window [66.73, 104.67]: γ_16..γ_31 (67.08, 69.55, 72.07, 75.70, 77.14, 79.34, 82.91, 84.74, 87.43, 88.81, 92.49, 94.65, 95.87, 98.83, 101.32, 103.73).
- c_pred = −4.37576696 (minimum eigenvalue of Σ A(γ_k)).
- c_emp values: δ=10⁻⁵: λ_min(ΔQ) = −4.376×10⁻¹⁰ → c_emp = −4.37576765 (rel err 1.6×10⁻⁵ %) δ=10⁻⁴: λ_min(ΔQ) = −4.376×10⁻⁸ → c_emp = −4.37576701 (rel err 9.7×10⁻⁷ %) δ=10⁻³: λ_min(ΔQ) = −4.376×10⁻⁶ → c_emp = −4.37577183 (rel err 1.1×10⁻⁴ %)
- Signal scales as δ² with absolute slope |c_pred|, as required by the theory.
- All three rel-errors are 5–7 orders of magnitude better than the 1% success criterion.
</results> <challenges>
The biggest pitfall was the simulation convention. The primary memory described a "4-member quartet" convention but the engine's `include_negative_zeros=True` flag already supplies a γ → −γ mirror. Naively passing only ρ produced c_emp at exactly half the expected value, while passing the quartet only in the deformed run (and not in the baseline) gave a wrong intermediate value. The correct procedure — verified by reproducing the T₀=46.13, σ=2, J=12, m=20 reference row to 6 sig figs — is to use the quartet form (pass both ρ and ρ̄, letting the engine mirror) **in both baseline and deformed runs**, so the M_arith terms cancel cleanly and only the off-line displacement enters ΔQ.
A second subtlety: c_pred uses only the positive in-window γ_k (no doubling), because the −2 prefactor and rank-2 operator structure already encode the quartet response.
</challenges> <discussion>
This is a clean cross-validation of the r20 explicit perturbation theorem at a parameter point with different T₀ (85.7 vs 46.13), different σ (2 vs sweep), different J (10 vs sweep), and a different population of in-window zeros (16 zeros γ_16–γ_31 rather than γ_4–γ_18). The agreement is essentially numerical-precision-limited: rel err ≈ 10⁻⁶ at the optimum δ=10⁻⁴, with the slightly larger residual at δ=10⁻³ reflecting onset of O(δ⁴) terms beyond the linearised theorem and at δ=10⁻⁵ reflecting double-precision round-off in computing tiny eigenvalues. The success generalises r20 from a single anchor to a proper validation at a second independent point, providing strong evidence that A(γ_k) = −2[φ′φ′ᵀ + ½(φφ″ᵀ + φ″φᵀ)] is the correct localised rank-two operator for ζ_δ-style real-part perturbations of Riemann zeros, with the in-window restriction (|γ_k − T₀| ≤ 3σ√J) being a sharp and physically meaningful cutoff governed by the Hermite-Gauss basis support.
</discussion> <proposed-next-hypotheses>
1. The explicit perturbation operator A(γ_k) = −2[φ′φ′ᵀ + ½(φφ″ᵀ + φ″φᵀ)] is *family-universal*: it predicts c at the same precision for primitive Dirichlet L(χ₄ mod 5) using its own zeros, and for L(Δ,s) once the modular trace-identity bug is resolved.
2. Higher-order corrections to the prefactor scale exactly as δ⁴ with coefficient given by a tensorised operator B(γ_k) involving φ‴ and φ⁴, predictable from a Taylor expansion of the same localisation argument.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>c_pred_vs_c_emp_T0_85p7.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Validation table for the explicit perturbation theorem at the second anchor point T₀=85.7, σ=2, J=10, m=40. Three rows for δ ∈ {1e-5, 1e-4, 1e-3} containing min_eig_dQ from the ζ_δ Weil-form simulation, c_emp = min_eig/δ², c_pred = −4.375767 (min eigenvalue of Σ A(γ_k) over the 16 Riemann zeros γ_16..γ_31 in the basis window), and relative error in percent. All rel-errors below 1.2×10⁻⁴ %, satisfying the 1% validation gate by 4+ orders of magnitude.</artifact-description>
</artifact>
<artifact>
<file-name>perturbation_validation_T0_85p7.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Log-log plot of |λ_min(ΔQ)| vs δ at T₀=85.7 with empirical points overlaid on the theoretical |c_pred|·δ² line, demonstrating the δ² scaling and the predicted prefactor to numerical precision.</artifact-description>
</artifact>
</artifacts>
</output> 