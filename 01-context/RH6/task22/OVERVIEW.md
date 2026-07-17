## Overview <output>
<conclusion>
The hypothesis is rejected: increasing N from 10⁴ to 5·10⁴ does NOT drive the L(Δ) and L_DH off-diagonal residuals toward zero in a way that approaches zeta's diagonal-dominant structure — L(Δ)'s residual is essentially unchanged (+37.4% → +39.8%), L_DH's residual shrinks but stays positive (+22.6% → +5.2%), while zeta's own residual moves further from zero (−8.6% → −32.2%), showing that all three are in a non-asymptotic, finite-N regime rather than converging to a common diagonal-dominant decomposition.
</conclusion> <methods>
1. Reconstructed the ω-class fourth-moment engine from the r16 specification (no source file was retained in the workspace). D_L(t)=Σ_{n=1}^{N} a_L(n) n^{−(1/2+it)} on the critical line; S_k(t) is the restriction to n with ω(n)=k for k=0..5; quantities computed: total = ∫|D|⁴ dt, pure = Σ_k∫|S_k|⁴ dt, diag×4 = 4·Σ_{j<k}∫|S_j|²|S_k|² dt, off-diag = total − pure − diag×4.
2. Coefficients: a_ζ(n)=1; a_LΔ(n)=τ(n)/n^{11/2} (analytic normalization; τ(n) from PARI/GP `ramanujantau` at primes via cypari2, extended multiplicatively with Hecke recursion τ(p^{a+1})=τ(p)τ(p^a)−p^{11}τ(p^{a−1})); a_LDH(n)=A·χ(n)+B·χ̄(n) with χ the primitive mod-5 quartic character, A=(1−iξ)/2, B=(1+iξ)/2, ξ=(√(10−2√5)−2)/(√5−1) (matches ldh_def.py).
3. ω(n) and smallest-prime-factor computed by linear sieve to n=5·10⁴.
4. Integration: uniform grid t∈[500,1000), Δt=0.01 (50 000 samples), left Riemann sum (matches r16; validated below). Computed S_k(t) and D(t) by batched matrix–vector products of size 200×N over complex128 (memory ≈160 MB).
5. Validation: re-ran zeta at N=10⁴ on the same grid; total = 85 022.94 vs. r16 value 85 022.93 (relative error <2·10⁻⁵), per-class pure integrals match to 4 significant figures — engine reproduces r16.
6. Saved comparison JSON (`fourth_moment_omega_decomposition_T500_1000_N50000.json`), CSV (`comparison_N1e4_vs_N5e4.csv`), and a single summary figure with two stacked panels.
</methods> <results>
Numerical decomposition on t∈[500,1000]: | L-function | ∫|D|⁴ N=10⁴ | ∫|D|⁴ N=5·10⁴ | pure% 10⁴ → 5·10⁴ | diag×4% 10⁴ → 5·10⁴ | off-diag% 10⁴ → 5·10⁴ | Δ off-diag (pp) |
|---|---|---|---|---|---|---|
| ζ | 85 023 | 85 933 | 23.31 → 27.03 | 85.32 → 105.14 | −8.63 → −32.17 | **−23.5** |
| L(Δ) | 45 406 | 64 002 | 15.57 → 13.53 | 46.99 → 46.63 | +37.45 → +39.84 | **+2.4** |
| L_DH | 26 507 | 26 509 | 18.80 → 22.29 | 58.64 → 72.56 | +22.56 → +5.15 | **−17.4** | Key observations:
• L(Δ) off-diagonal residual fraction is essentially flat (+37.4% → +39.8%): the absolute total grows ~41% but the diagonal cross-class terms grow in proportion, leaving the residual share unchanged.
• L_DH off-diagonal residual drops sharply (+22.6 pp → +5.2 pp), driven entirely by an increase of the diagonal cross-class share (+58.6 pp → +72.6 pp); the absolute total is nearly unchanged (∫|D|⁴ moves only +0.005%), meaning the new high-ω terms (k=3..5) reshuffle existing |D|⁴ rather than adding mass.
• ζ's off-diagonal residual becomes more negative (−8.6 pp → −32.2 pp): diag×4 exceeds 100% of total (105.1%), so the cross-term over-count grows. Zeta is NOT becoming diagonal-dominant in the (pure + diag×4) sense in this window; instead the negative residual deepens, signalling stronger destructive interference between unequal-ω blocks.
• Total integrals: L(Δ) grows substantially with N (+41%) — Deligne-bounded normalized coefficients can still accumulate fourth-moment slowly; ζ grows weakly (+1.1%); L_DH is essentially saturated (+0.005%) on this window.
</results> <challenges>
• Engine source from report r16 was absent — had to rebuild from the dataset description plus the existing JSON config. Validated by reproducing zeta at N=10⁴ against the stored numbers (<2·10⁻⁵ relative error).
• Computing τ(n) for n≤5·10⁴ required PARI/GP via cypari2 (installed at runtime) for τ(p) at the 5 133 primes; multiplicative extension done with Python big-int arithmetic to avoid overflow before dividing by n^{11/2}.
• Memory/runtime: a single dense (50 000 t)×(50 000 n) phase matrix is ~40 GB; used batched matrix products (200 t per batch) to keep peak memory ≈160 MB. Each L-function took ~100 s.
• Convention choice: r16's "left Riemann sum, 50 000 points" had to be inferred from dt and the validation residual; an inclusive-endpoint grid (50 001 points) gives a slightly worse match to the stored numbers.
• Sign of the off-diagonal residual is not constrained — it can legitimately be negative (cross-terms with j≠k that aren't in the (j,j,k,k) pattern, e.g. (j,j,j,k), can sum to a negative real). This makes the residual a bookkeeping quantity rather than a strictly non-negative "error".
</challenges> <discussion>
The asymptotic random-matrix / Conrey–Ghosh prediction for the fourth moment of ζ is dominated by the diagonal n₁n₂=n₃n₄ pairings, so one expects that at very large N the (pure + diag×4) block captures essentially all of ∫|D|⁴. The data here say we are nowhere near that regime even at N=5·10⁴ on a window of length 500: zeta's residual is moving away from zero (more negative), and L(Δ)'s residual is flat. Only L_DH shows the qualitative behaviour predicted by the hypothesis — and only because its total has saturated while internal cross terms grow. The fact that the three functions behave in three different directions rules out a simple "all converge to diagonal dominance with N" picture, at least for these (N, t-window) parameters. The ω-class decomposition is therefore better interpreted as a finite-N structural fingerprint than as an asymptotic signature: it reflects how heavily the Dirichlet polynomial concentrates on high-ω integers (which depends on the coefficient size distribution, e.g. Deligne-bounded τ(n)/n^{5.5} vs. unit coefficients), more than it reflects properties of the underlying L-function on the critical line. For zeta, the deepening negative residual at N=5·10⁴ is a known finite-truncation artefact: as N grows, more n with ω(n)=3..5 enter and create (j,j,j,k)-type terms whose phases cancel the (j,j,k,k) over-count built into the "diag×4" definition. This is consistent with the dataset description's warning that the decomposition is sensitive to N and to the integration window.
</discussion> <proposed-next-hypotheses>
1. For zeta, the off-diagonal residual fraction on t∈[T₀, T₀+500] is, at fixed N, a monotone-decreasing function of T₀ — i.e. the diagonal-dominant asymptotic regime is reached by moving the window up rather than by enlarging N: testable by recomputing the decomposition at N=10⁴ on t∈[5·10³, 5·10³+500] and t∈[5·10⁴, 5·10⁴+500].
2. For L(Δ), the off-diagonal residual fraction stabilises near a non-zero limit ≈ 40% as N→∞ at fixed window [500,1000], because the slow growth of partial sums of |τ(n)/n^{5.5}|² keeps multiple ω-classes simultaneously active; testable by adding an intermediate N=2·10⁴ point and an extrapolated N=10⁵ point and fitting f(N) = c + a·N^{−α}.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>fourth_moment_omega_decomposition_T500_1000_N50000.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Full ω-class fourth-moment decomposition for ζ, L(Δ), and L_DH at N_terms=5·10⁴ on the high-t window t∈[500,1000] (Δt=0.01, left Riemann sum). Contains total ∫|D|⁴, per-class pure integrals (k=0..5), all C(6,2)=15 pairwise |S_j|²|S_k|² integrals, and derived percentages (pure, diag×4, off-diag). Direct N-extension of `fourth_moment_omega_decomposition_T500_1000.json`. Engine reconstructed from r16 spec; validated against the N=10⁴ JSON to <2·10⁻⁵ relative error on the zeta total.</artifact-description>
</artifact>
<artifact>
<file-name>comparison_N1e4_vs_N5e4.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Side-by-side comparison table (3 rows × 10 columns) of total ∫|D|⁴, pure%, diag×4%, off-diag%, and the off-diagonal percentage-point change between N=10⁴ and N=5·10⁴, for ζ, L(Δ), and L_DH on t∈[500,1000].</artifact-description>
</artifact>
<artifact>
<file-name>fourth_moment_N_dependence.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: grouped bar chart of pure / diag×4 / off-diag fractions at N=10⁴ (light) vs. N=5·10⁴ (solid) for the three L-functions. Panel B: off-diagonal residual % vs. N (log-x) showing zeta diverging more negative, L(Δ) essentially flat, and L_DH shrinking toward zero.</artifact-description>
</artifact>
</artifacts>
</output> 