## Overview <output>
<conclusion>
Detection is theoretically possible at both common parameter points: at the optimal point (T₀=46.13, σ=1, J=10, m=20) a δ=10⁻³ off-critical zero rises above the truncation noise floor once the prime cutoff exceeds X≈1.35×10⁵, while at the L_DH point (T₀=85.7, σ=2, J=10, m=20) the noise floor sits at η≈4.6×10⁻¹⁰ so the signal already exceeds the noise for every δ tested (δ∈{10⁻⁴,10⁻³,10⁻²}) even at X=10³.
</conclusion> <methods>
1. Loaded `forced_negativity_surface.csv` (300 rows, T₀=46.13) and `eta_residual_law.json` (η(X,H) at the two control points).
2. Extracted the quadratic forced‑negativity prefactor c(σ,J,m)=|λ_min(ΔQ)|/δ² from the surface. Only the m=20 mode produced a measurable, δ²‑scaling signal at small δ; m=1 and m=5 returned zero (machine precision) at δ≤10⁻³ — consistent with the off‑critical zero coupling primarily to the high‑m Hermite‑Gauss modes. The c values were verified to be δ‑independent (ratio c_max/c_min within ~5 % for σ=1, m=20 across δ=10⁻⁵…10⁻³, validating the c·δ² model).
3. Because the surface CSV covers J∈{4,8,12,16,20} but the target points specify J=10, c was obtained by linear interpolation of c(J) between J=8 and J=12 at m=20: - optimal (σ=1): c ≈ 16.87 - L_DH (σ=2): c ≈ 3.63
4. Pulled η(X) at H=2500 from the `fine_X_scan_H2500` block (X ∈ {10³,3×10³,10⁴,3×10⁴,10⁵,3×10⁵,10⁶}). η was confirmed essentially H‑independent for H ≥ 1000 in the main grid.
5. For each δ ∈ {10⁻⁴,10⁻³,10⁻²}, defined signal s = c·δ² and located the crossover X_min where η(X) = s by log‑log interpolation between consecutive X grid points.
6. Produced a 2‑panel detectability phase diagram: panel A (optimal), panel B (L_DH), each showing η(X) vs three horizontal signal levels.
</methods> <results>
Prefactors (from forced_negativity_surface.csv, m=20, J=10 by interpolation):
- c(optimal, σ=1) ≈ 16.87
- c(L_DH, σ=2) ≈ 3.63 Optimal point (T₀=46.13, σ=1, J=10, m=20) — η(X) at H=2500: X=10³ → η ≈ 1.56×10⁻¹ X=10⁴ → η ≈ 2.56×10⁻² X=10⁵ → η ≈ 6.10×10⁻⁵ X=3×10⁵→ η ≈ 5.35×10⁻⁷ X=10⁶ → η ≈ 5.80×10⁻⁹
Minimum X for signal > noise: δ=10⁻² → signal 1.69×10⁻³, X_min ≈ 2.65×10⁴ δ=10⁻³ → signal 1.69×10⁻⁵, X_min ≈ 1.35×10⁵ ← spec‑sized δ δ=10⁻⁴ → signal 1.69×10⁻⁷, X_min ≈ 4.08×10⁵
Thus the originally specified X=10⁵ is just below threshold for δ=10⁻³ at this point; X ≳ 1.35×10⁵ is required. L_DH point (T₀=85.7, σ=2, J=10, m=20) — η(X) ≈ 4.6×10⁻¹⁰ across all tested X (1000–10⁶): δ=10⁻² → signal 3.63×10⁻⁴ ≫ η (factor ≈ 8×10⁵) δ=10⁻³ → signal 3.63×10⁻⁶ ≫ η (factor ≈ 8×10³) δ=10⁻⁴ → signal 3.63×10⁻⁸ > η (factor ≈ 80)
At this point the noise floor is already at the machine‑precision floor at the smallest cutoff tested, so any δ ≥ 10⁻⁴ is, in principle, detectable without increasing X. Saved `detectability_summary.csv` and figure `detectability_phase_diagram.png`.
</results> <challenges>
- The forced_negativity_surface.csv does not contain the exact J=10 specified in the research objective; J=10 had to be obtained by linear interpolation between J=8 and J=12 (slope is mild for both σ=1 and σ=2, so the interpolation is well‑behaved, but the values carry interpolation uncertainty of order 10–20 %).
- Only the m=20 mode produced a non‑zero ΔQ signal at small δ; m=1 and m=5 returned exact zeros (likely below numerical precision after baseline subtraction). The reported detectability conditions are therefore specific to m=20; lower‑m modes are not detectable at any X within this data.
- η(X) is sampled only at 7 X‑values per point; X_min crossovers are log‑log interpolated and not measured directly.
- At the L_DH point the noise floor (~5×10⁻¹⁰) is at the level of a δ‑independent numerical floor, so it represents an effective floor rather than an X‑limited truncation error — pushing X further will not improve detectability there.
</challenges> <discussion>
The two control points sit in very different regimes. The optimal point has a steeply X‑sensitive truncation noise floor that falls roughly four orders of magnitude per decade of X over the tested range; here the prime cutoff is the dominant detectability lever and X=10⁵ (the original spec value) is marginal — a modest factor of ~1.35 increase suffices to detect a δ=10⁻³ off‑critical zero. The L_DH point, by contrast, already sits at an essentially X‑independent floor of ~5×10⁻¹⁰ and gives a very favourable signal‑to‑noise ratio (≥80 even at δ=10⁻⁴), suggesting it is intrinsically the more sensitive detector for off‑critical zeros despite its smaller prefactor c. This pattern indicates that the forced‑negativity test is, in principle, viable for the Riemann‑ζ Front C question, but with two practical caveats: (i) the high‑m basis modes carry the signal, so the basis must include at least m≈20, and (ii) at lower σ/T₀ regimes, the prime sum must be aggressively extended (X ≳ 10⁵–10⁶) before any sub‑per‑mille off‑critical excursion can be resolved.
</discussion> <proposed-next-hypotheses>
1. The detectability gain at the L_DH point (T₀=85.7, σ=2) relative to the optimal point arises because the Hermite–Gauss basis localizes near T₀, sampling a higher‑density region of ζ‑zeros and saturating the prime sum at much smaller X; therefore the noise floor η(T₀,σ,J,X) at fixed (σ,J,X) should decrease monotonically with T₀ up to where high‑precision zero data run out.
2. The forced‑negativity prefactor c(σ,J,m) grows super‑linearly with m at fixed (σ,J): specifically, c(σ=1, J=10, m) ∝ m^α with α > 1 in the m ∈ [1,20] range, implying that increasing the maximum Hermite index is a more efficient detectability lever than increasing the prime cutoff X for the optimal point.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>detectability_summary.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Tabulated detectability conditions for the two common parameter points. Columns: point, T₀, σ, J, m, δ, c_prefactor, signal=c·δ², X_min (log‑log‑interpolated crossover where η(X)=signal), and η at X=10⁶. Built by combining the m=20 prefactor from forced_negativity_surface.csv (J=10 by linear interpolation between J=8 and J=12) with the η(X) fine scan at H=2500 from eta_residual_law.json.</artifact-description>
</artifact>
<artifact>
<file-name>detectability_phase_diagram.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two‑panel detectability phase diagram. Panel A (optimal, T₀=46.13, σ=1, J=10, m=20): log‑log plot of noise floor η(X) with three horizontal signal levels c·δ² for δ∈{10⁻⁴,10⁻³,10⁻²} and an annotated X_min≈1.35×10⁵ for δ=10⁻³. Panel B (L_DH, T₀=85.7, σ=2, J=10, m=20): same overlay showing that η≈5×10⁻¹⁰ is below all three signal levels for every X tested.</artifact-description>
</artifact>
</artifacts>
</output>
