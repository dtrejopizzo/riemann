## Overview <output>
<conclusion>
Shifting the integration window from [0,500] to [500,1000] dramatically removes the t=0 dominance of the Dirichlet polynomial and reveals very different ω-class decomposition fingerprints; for ζ the off-diagonal residual fraction collapses from +82.3% to −8.6% (~91 percentage-point drop in magnitude), in qualitative agreement with the hypothesis, but for L(Δ) and L_DH the off-diagonal residual actually grows (+11.6 and +25.6 pp), so the hypothesis is supported only for ζ and is not universal across the L-functions tested.
</conclusion> <methods>
1. Recovered prior artifacts from the e14c data_storage tag `heron_output`: zero lists (zeta_zeros_5000_dps50.npy, lchi_zeros_5000_dps50.npy, ldelta_zeros_2000_dps50.npy, checkpoints_ldh/ldh_ckpt_02500.npy), and the r13 summary outputs (fourth_moment_omega_decomposition.json, fourth_moment_omega_decomposition_summary.csv) plus the r13 notebook (8c50938a-…ipynb), which contains the canonical ω-class fourth-moment decomposition engine.
2. Re-implemented the r13 engine verbatim: Dirichlet polynomial D_L(t)=Σ_{n=1..N} a_n n^{-1/2-it} split into ω-class pieces S_k(t)=Σ_{ω(n)=k} a_n n^{-1/2-it}. Decomposition: • Pure-class = Σ_k ∫ |S_k|^4 dt • Diagonal cross-class = 4 · Σ_{j<k} ∫ |S_j|^2 |S_k|^2 dt (combinatorial factor 4 from the 4-tuple expansion) • Off-diagonal residual = ∫|D|^4 dt − pure − diagonal cross.
3. Coefficients (N_terms=10^4): a_n=1 (ζ); a_n=τ(n)/n^{11/2} (L(Δ), via cypari2 ramanujantau); a_n=A χ(n)+B χ̄(n) with χ a primitive character mod 5 of order 4 and (A,B)=((1∓iξ)/2) with ξ=(√(10−2√5)−2)/(√5−1) (L_DH, per the canonical ldh_def.py construction; coefficients are real, as expected).
4. ω(n) computed via sympy.factorint; classes 0…5 present, with counts [1, 1280, 4097, 3695, 894, 33].
5. Time sampling at dt=0.01 over t∈[500,1000] (50,001 points); chunked outer-product evaluation of phases for memory efficiency; integration via scipy.integrate.simpson. Output saved as JSON, comparative CSV, and a single summary figure.
</methods> <results>
N_terms=10^4, dt=0.01. Total fourth moment ∫|D_L|^4 dt:
| L | [0,500] (r13) | [500,1000] (new) | ratio new/old |
|---|---|---|---|
| ζ | 6.278246e8 | 8.5023e4 | 1.35e-4 |
| L(Δ) | 3.30367e4 | 4.5406e4 | 1.374 |
| L_DH | 1.60939e4 | 2.6507e4 | 1.647 | For ζ the t=0 peak alone supplies ~99.99% of the [0,500] integral; removing it makes the windowed total ~4 orders of magnitude smaller. For L(Δ) and L_DH the densities on [500,1000] are actually higher than the averaged [0,500] density. Fractional decomposition (pure / diag-cross×4 / off-diag), in %:
| L | window | pure | diag×4 | off-diag |
|---|---|---|---|---|
| ζ | [0,500] | 5.10 | 12.64 | +82.26 |
| ζ | [500,1000] | 23.31 | 85.32 | −8.63 |
| L(Δ) | [0,500] | 17.66 | 56.53 | +25.80 |
| L(Δ) | [500,1000] | 15.57 | 46.99 | +37.45 |
| L_DH | [0,500] | 26.65 | 76.41 | −3.06 |
| L_DH | [500,1000] | 18.80 | 58.64 | +22.56 | Change in off-diagonal residual (Δ = new − old):
• ζ: 82.26% → −8.63% (Δ = −90.89 pp; |off-diag| drops from 82.26% to 8.63%, a 9.5× reduction in magnitude).
• L(Δ): 25.80% → 37.45% (Δ = +11.65 pp).
• L_DH: −3.06% → 22.56% (Δ = +25.62 pp; magnitude grows from 3.06% to 22.56%). For ζ on the high-t window the off-diagonal residual is now small AND negative, while the pure + 4·diag-cross terms over-explain the total (≈108.6%). For L(Δ) and L_DH the off-diagonal residual moves toward larger positive values, with the diagonal pieces summing to <100% (62.6% for L(Δ), 77.4% for L_DH).
</results> <challenges>
1. The current workspace was empty: zero lists, the r13 notebook/summary, and ldh_def.py–related code were located via `e14c.data_storage.list_entries_by_tag("heron_output")` and pulled with `download(entry_id, …)`; provenance was traced through the file_path metadata pointing back to prior task IDs.
2. The r13 cross-class definition uses a combinatorial factor of 4 (4·Σ_{j<k} ∫|S_j|^2|S_k|^2 dt); this must be reused verbatim or fractions are not comparable. The factor follows from the (j₁,k₁,j₂,k₂) ordered expansion of |Σ_k S_k|^4 — there are 4 ordered 4-tuples per unordered pair {j,k} (j≠k) whose positive multiset equals the negative multiset.
3. r13 reported a negative off-diagonal residual for L_DH on [0,500] (-3.06%), and we obtain a negative value for ζ on [500,1000] (-8.63%). This is a legitimate algebraic outcome: the off-diagonal residual is the signed remainder (Σ over 4-tuples whose positive multiset ≠ negative multiset) and can be negative when destructive interference dominates over constructive interference; it is not a sign error.
4. The hypothesis as stated ("off-diagonal residual for ζ becoming smaller relative to diagonal components, moving closer to expected asymptotic behaviour") is operationally ambiguous; we report both the signed value and its magnitude. The magnitude interpretation supports the hypothesis for ζ very strongly; the signed value does too (smaller magnitude).
5. No assessment of higher-T convergence is provided: a single high-t window cannot establish asymptotic behaviour, only contrast with [0,500].
</challenges> <discussion>
The r13 observation that >99% of ∫|D_L|^4 dt on [0,500] is concentrated near t=0 is most extreme for ζ, whose coefficients a_n=1 produce a polynomial that is maximally large at t=0 (D_ζ(0)=Σ 1/√n ≈ 198 for N=10^4). The diagonal terms there are positive and bounded, while the off-diagonal cross-terms inherit the same enormous magnitude and dominate, explaining the +82% off-diagonal share on [0,500]. Moving to [500,1000] eliminates this non-asymptotic peak and the off-diagonal residual collapses to small magnitude (−8.6%), with the diagonal pieces accounting for ≈108.6% of the total — a configuration consistent with what one would expect in the asymptotic mean-value regime for ζ, where the fourth-moment is dominated by diagonal/divisor contributions of the form T·Σ d(n)^2/n. For L(Δ) and L_DH the situation is opposite: their Dirichlet coefficients are not monotone (τ(n)/n^{11/2} decays rapidly; a_n for L_DH is bounded periodic), so the t=0 peak is far less dominant, and the [0,500] window already contains substantial high-t content. Shifting to [500,1000] simply samples a regime with stronger cross-class interference; the off-diagonal residual grows in magnitude, and the diagonal pieces now under-explain the total. This is consistent with the heuristic that small-N truncations of automorphic / character L-functions have richer phase structure than ζ at the same N, and asymptotic divisor-style diagonal dominance only sets in at much larger t (or larger N). Net: removing the t=0 peak is a clean structural test, but the cleaner asymptotic structure it reveals is L-function-dependent. For ζ it markedly suppresses off-diagonal residual (supporting the hypothesis); for L(Δ) and L_DH it does the opposite, indicating these higher-rank L-functions need either much larger N or higher-t windows before their off-diagonal residual contracts.
</discussion> <proposed-next-hypotheses>
1. For ζ, the off-diagonal residual fraction is well-modelled by a function of T₀·log N that decays to zero in the limit T₀→∞ with N fixed, so increasing the window centre (e.g. windows [10^k, 10^k+500] for k=3,4) will further shrink |off-diag| while pure + diag-cross approach their asymptotic divisor-sum prediction T·Σ d(n)^2/n.
2. For L(Δ) and L_DH at N=10^4 the off-diagonal residual on high-t windows grows because the polynomial length is too short relative to t; doubling N to 2·10^4 (or 5·10^4) on the same [500,1000] window will reduce their off-diagonal residual fraction (testable: predict |off-diag| ∝ (log t / log N) or similar).
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>fourth_moment_omega_decomposition_T500_1000.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Full ω-class fourth-moment decomposition for ζ, L(Δ), L_DH at N_terms=10^4, dt=0.01, on the high-t window t∈[500,1000]. Contains per-class pure integrals ∫|S_k|^4 dt for k=0..5, per-pair diagonal cross-class integrals ∫|S_j|^2|S_k|^2 dt for j<k, total ∫|D_L|^4 dt, and the pure/diagonal-cross-×4/off-diagonal fractions. Produced by re-running the r13 time-sampling engine with the integration window shifted.</artifact-description>
</artifact>
<artifact>
<file-name>fourth_moment_decomposition_500_1000_vs_0_500.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Side-by-side comparative table of total ∫|D_L|^4 dt and the three fractional contributions (pure-class, diagonal cross-class ×4, off-diagonal residual) for ζ, L(Δ), L_DH between the original r13 window [0,500] and the new high-t window [500,1000].</artifact-description>
</artifact>
<artifact>
<file-name>fourth_moment_high_t_window_comparison.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Summary figure: grouped bar chart of the three fractional decomposition components for ζ, L(Δ), L_DH in [0,500] (solid) vs [500,1000] (hatched), with annotated change in off-diagonal residual per L-function.</artifact-description>
</artifact>
</artifacts>
</output>
