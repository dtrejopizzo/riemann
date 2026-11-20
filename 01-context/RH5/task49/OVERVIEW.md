## Overview <output>
<conclusion>
The Odlyzko-seed + mpmath refinement strategy successfully produced high-precision (dps=50) ζ zeros at ~18 ms/zero for low-index zeros but became significantly slower (~0.7–0.85 s/zero) for higher-index zeros, and the full N=5000 refinement could not be completed within the runtime budget, leaving the hypothesis only partially supported and the ζ_δ control list unable to be cached.
</conclusion> <methods>
1. Loaded the pre-validated `zeta_zeros_N100000_dps9.npy` (Odlyzko `zeros1`-derived) NumPy array and re-confirmed the R2 gate: max absolute difference vs. the three spec zeros = 1.00e-9 (consistent with ~9-digit source precision).
2. Took the first N=5000 imaginary parts as seeds.
3. Set `mpmath` working precision to `dps=50` and refined each seed by Newton/secant root-finding via `mpmath.findroot(mpmath.siegelz, seed)`, where `Z(t) = e^{iθ(t)} ζ(1/2+it)` is real-valued on the critical line. Each seed (stringified for full-precision construction) was passed as the initial guess.
4. Periodic checkpointing: refined zeros saved as strings (full 50-digit precision) to `zeta_refined_partial.npy`.
5. Step 4 (perturbation to build ζ_δ) was planned as: copy of refined ζ zeros, then for `m=20` chosen indices, replace `γ` with `γ + i·0` and add a horizontal displacement δ=0.1 to the real part (i.e. zeros moved from σ=1/2 to σ=1/2+0.1) — consistent with the one-sided perturbation used in r3/r10. This step could not be executed because Step 3 did not complete in time.
Libraries: `numpy`, `mpmath` (v1.x).
</methods> <results>
- R2 gate verification on Odlyzko table: max |γ_spec − γ_table| = 1.00e-9 across the first three zeros. PASS at the table's ~9-digit precision.
- Refinement of seed γ₁ from 14.134725142 to dps=50: γ₁ = 14.134725141734693790457251983562470270784257115699.
- Throughput scaling (empirical): • First ~20 zeros: ~18 ms/zero. • Indices ~2000: ~0.16 s/zero (cumulative wall time 900 s for 2176 zeros). • Indices ~2700: ~0.71 s/zero (next 500 zeros in 354 s). • Indices ~3500: ~0.72 s/zero (next 800 zeros in 577 s). • Indices ~4700: ~0.85 s/zero. This is consistent with the known growth of `siegelz` evaluation cost with t at fixed precision.
- Progress: 4705 of 5000 ζ zeros (94.1%) refined to dps=50 and saved to `zeta_refined_partial.npy` as string representations.
- Estimated total wall time to finish all 5000 refinements at dps=50: ≈ 2700–3000 s on this single-core kernel, which exceeds the available runtime budget given prior cell consumption.
- ζ_δ control list: NOT generated (depends on completed ζ list).
</results> <challenges>
1. The dominant computational cost in `mpmath.findroot(siegelz, ...)` is the per-call evaluation of the Riemann–Siegel Z-function at high precision (dps=50). This cost grows substantially with t — empirically a ~40–50× slowdown between γ₁ and γ₅₀₀₀ — which made the naive "uniform throughput" estimate from the first 20 zeros (~1.5 minutes total) far too optimistic.
2. The notebook kernel imposed 900-second wall-time limits per cell, requiring the refinement loop to be split into chunks. Two cells were killed mid-chunk; partial results were preserved only because checkpointing was added after the first timeout.
3. mpmath.siegelz at dps=50 is not parallelized internally, and the kernel is single-process, so no easy CPU parallelism was available within the cell budget.
4. The hypothesis (Odlyzko seeds + refinement is the most computationally efficient route) is only weakly supported: the technique works correctly, but at dps=50 the per-call cost of Z(t) dominates, and refinement does not provide the dramatic speedup one might naively assume — consistent with the dataset note that "a hybrid refinement approach gives only a modest 1.1–1.3× speedup over de novo generation."
5. The ζ_δ generation step could not be executed; only its specification (m=20 zeros, δ=0.1 horizontal one-sided displacement) is documented.
</challenges> <discussion>
The Odlyzko-seed refinement strategy is methodologically clean: seeds are within 1e-9 of the truth, Newton-like iteration on Z(t) converges in 1–2 iterations regardless of t, and the seeds remove the need for any scanning/bracketing. However, the absolute cost is governed by Z(t) evaluation at dps=50, which scales with t (the Riemann–Siegel formula sums O(√(t/2π)) terms and `mpmath` further pays a precision-related constant). This explains why prior `r5` analysis found only a ~1.1–1.3× speedup over de novo `mp.zetazero`: both share the same Z-evaluation bottleneck, and the seed merely saves iteration count, not per-iteration cost. For producing an N=5000, dps=50 list in a single-core, time-budgeted environment, a parallel (multi-process) refinement scheme is essentially required; the algorithm itself is correct and the partial 4705-zero output is genuine and reusable.
</discussion> <proposed-next-hypotheses>
1. Parallelizing the Odlyzko-seed refinement across N CPU cores (each running `mpmath.findroot(siegelz,…)` on disjoint index ranges) will yield near-linear speedup, allowing the full N=5000 dps=50 ζ zero list to be produced in <10 minutes on an 8-core machine, because each refinement is independent and CPU-bound in `mpmath`.
2. The per-zero refinement cost at dps=50 grows as O(√t) (the Riemann–Siegel main-sum length), so a fitted model `t_refine(γ) = a + b·√γ` will predict total wall time for arbitrary N to within ~10% accuracy across the range N ∈ {2k, 5k, 10k, 20k} from the project's parameter grid.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>zeta_refined_partial.npy</file-name>
<artifact-type>computed</artifact-type>
<artifact-description>NumPy array of 4705 string-encoded imaginary parts of the first 4705 nontrivial Riemann ζ zeros, refined to dps=50 precision via `mpmath.findroot(mpmath.siegelz, seed)` starting from Odlyzko `zeros1` table seeds. Strings preserve the full 50-digit precision; reload with `np.load(...)` then `mpmath.mpf(s)` per element. This is a partial cache of the N=5000 target (94.1% complete); the remaining 295 zeros and the ζ_δ perturbation list were not produced due to runtime exhaustion.</artifact-description>
</artifact>
</artifacts>
</output> 