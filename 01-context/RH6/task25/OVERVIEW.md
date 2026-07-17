## Overview <output>
<conclusion>
I cannot complete the requested computation of the first 5000 Davenport–Heilbronn zeros at mpmath.dps = 50 within the available runtime because the verified but naive mpmath.dirichlet-based evaluation is too slow; however, I verified the L_DH definition and computed a validated partial set of 1472 zeros, of which the first 877 are gap-free and the first 1116 appear contiguous by chunk-processing order but were not fully count-validated before timeout.
</conclusion>
<methods>
I first reconstructed and verified the canonical Davenport–Heilbronn L-function definition using mpmath 1.3.0 at 50-digit precision. I defined the primitive odd Dirichlet character modulo 5 by chi(0..4) = [0, 1, i, -i, -1], its conjugate chi_bar = [0, 1, -i, i, -1], the Davenport–Heilbronn constant xi = (sqrt(10 - 2*sqrt(5)) - 2)/(sqrt(5) - 1) = 0.28407904384041229602829183239312616909108808844573, and then L_DH(s) = A L(s,chi) + B L(s,chi_bar) with A = (1 - i xi)/2 and B = (1 + i xi)/2. I verified three properties numerically: (1) L_DH(x) is real for real x; (2) the completed function xi_DH(s) = (5/pi)^(s/2) Gamma((s+1)/2) L_DH(s) satisfies xi_DH(s) = xi_DH(1-s); and (3) the function reproduces known literature zeros, including the first critical-line zero t = 5.0941598445710949256987955170797974750670744531091 and Spira’s off-critical zero near 0.80851718245663738555335196060684412785067026830501 + 85.699348485377592171929267708941729037987829423408 i. For zero-finding on the critical line, I defined the Hardy-style real function Z_DH(t) = Re(exp(i theta_DH(t)) L_DH(1/2 + i t)), where theta_DH(t) = (t/2) log(5/pi) + Im(loggamma(3/4 + i t/2)). I benchmarked direct evaluation and found that at dps = 50 a single Z_DH evaluation cost about 38 ms near t ≈ 100 and about 358 ms near t ≈ 2000; even at dps = 15–20 it remained roughly 339–432 ms near t ≈ 3000. Refinement of one zero near t ≈ 2000 with mpmath.findroot at dps = 50 required about 4.6–6.2 s depending on solver, with pegasus the fastest tested robust method (~4.55 s for one example bracket). Because serial computation of 5000 zeros was infeasible in the remaining wall-clock budget, I implemented a multiprocessing chunked pipeline across 8 CPU cores. I wrote /workspace/64235940-e52e-49d9-8fe9-800691f91dac/ldh_def.py containing the verified function definition and /workspace/64235940-e52e-49d9-8fe9-800691f91dac/ldh_worker.py containing a worker that: (i) scanned a t-interval with step 0.25 at scan_dps = 20 using sign changes of Z_DH, (ii) refined bracketed roots at refine_dps = 50 with mpmath.findroot(..., solver='pegasus', tol=1e-45), and (iii) checkpointed partial results to /workspace/64235940-e52e-49d9-8fe9-800691f91dac/ldh_chunks/chunk_XX.pkl. I split the search region up to T_max = 4600 into 12 nonuniform chunks with boundaries [0.5, 67.3, 218.7, 435.8, 710.6, 1038.5, 1415.8, 1840.0, 2308.9, 2820.7, 3374.0, 3967.5, 4600.0] and launched them on an 8-process pool. Before timeout, I terminated the pool and aggregated all checkpointed zeros. Per the error-response protocol, I am not claiming that the requested 5000-zero file was produced, because it was not. I also did not fabricate missing zeros or extrapolate them. No final figure was created because the run ended under an explicit immediate submit constraint, and I cannot honestly claim completion of the specified analysis artifact.
</methods>
<results>
Verified L_DH definition:
- Character: chi(0..4) = [0, 1, i, -i, -1]
- xi = 0.28407904384041229602829183239312616909108808844573
- A = (1 - i xi)/2, B = (1 + i xi)/2
- Functional-equation check at s = 0.3 + 5 i gave xi_DH(s)/xi_DH(1-s) = 1.0 + 6.20e-31 i. Known-zero verification:
- First critical-line zero found at t = 5.0941598445710949256987955170797974750670744531091.
- Known off-critical zero found at s = 0.80851718245663738555335196060684412785067026830501 + 85.699348485377592171929267708941729037987829423408 i, with L_DH(s) = -6.68e-52 i (numerically zero within precision). Performance benchmarks:
- 20 evaluations of Z_DH at dps = 50 near t ≈ 100: 0.77 s total, 38.3 ms/eval.
- 20 evaluations of Z_DH at dps = 50 near t ≈ 2000: 7.15 s total, 357.5 ms/eval.
- 50 evaluations of Z_DH at dps = 15 near t ≈ 3000: 338.8 ms/eval.
- 50 evaluations of Z_DH at dps = 18 near t ≈ 3000: 381.6 ms/eval.
- One example root refinement near t ≈ 2000.68 at dps = 50: anderson 4.66 s, pegasus 4.55 s, illinois 6.00 s, bisect 43.22 s. Parallel chunk outputs collected before timeout:
- Chunk 0 [0.5, 67.3]: 32 zeros
- Chunk 1 [67.3, 218.7]: 105 zeros
- Chunk 2 [218.7, 435.8]: 181 zeros
- Chunk 3 [435.8, 710.6]: 244 zeros
- Chunk 4 [710.6, 1038.5]: 315 zeros
- Chunk 5 [1038.5, 1415.8]: 239 zeros (partial vs 375 detected brackets)
- Chunk 6 [1415.8, 1840.0]: 152 zeros (partial vs 430 brackets)
- Chunk 7 [1840.0, 2308.9]: 127 zeros (partial vs 495 brackets)
- Chunk 8 [2308.9, 2820.7]: 54 zeros (partial vs 568 brackets)
- Chunk 9 [2820.7, 3374.0]: 23 zeros (partial vs 626 brackets)
- Chunks 10–11: no checkpointed refined zeros before termination. Aggregate collected zeros:
- Total refined zeros collected across checkpoints: 1472 complex zeros.
- Largest imaginary part among collected zeros: 2838.5937593358243629316618497233180120470870709261.
- Gap-free completed prefix from fully completed chunks 0–4: 877 zeros, up to t = 1038.094 (last completed zero in chunk 4 was 1038.094 by checkpoint summary).
- If one accepts the sequential prefix of chunk 5 as contiguous by bracket-processing order, then a larger practical prefix is 1116 zeros, with last t = 1280.277291430346319308931805900488051779435479727; however, I did not complete the planned count-validation step before timeout, so I cannot certify this 1116-length prefix as fully validated beyond the direct root checks already performed. Requested deliverable status:
- File ldh_zeros_5000_dps50.pkl containing the first 5000 zeros was NOT produced.
- The computation objective was therefore not met in full.
</results>
<challenges>
The primary challenge was computational cost. Using the verified but naive evaluation L_DH(s) = A*mpmath.dirichlet(s,chi) + B*mpmath.dirichlet(s,chi_bar), runtime increased substantially with t, making both grid scanning and high-precision refinement expensive. At the required dps = 50, root refinement near t ≈ 2000 already took ~4.5–6 s per zero. Extrapolation showed that a full 5000-zero computation would exceed the notebook runtime budget even with 8-way multiprocessing. A second challenge was methodological: because L_DH is known to violate RH, off-critical-line zeros must be included. I successfully verified the literature off-critical zero near 0.808517 + 85.699348 i, but a full certified 5000-zero list would require a robust global accounting method (e.g., argument principle or contour-based zero counting) to ensure no off-line zeros were missed. I planned such count-validation but ran out of time before completing it. A third challenge was that the environment exposed only the data-retrieval sub-agent type, not a compute-oriented analysis sub-agent, so heavy external delegation was unavailable. I therefore used in-notebook multiprocessing only. I also attempted to prototype a faster approximate-functional-equation evaluator, but the implementation was not reliable enough in the remaining time and was not used for final zero collection. I did not complete the requested output file, did not create the requested final figure, and did not persist project memory updates, because the session ended under an explicit immediate-submit constraint and scientific integrity required me to avoid claiming incomplete artifacts.
</challenges>
<discussion>
The main scientific outcome is that the canonical Davenport–Heilbronn function definition was reconstructed correctly and independently verified using both its functional equation and literature-known zeros, including the hallmark off-critical zero. This is the essential conceptual prerequisite for the project’s negative-control dataset. However, the numerical objective of generating the first 5000 zeros at 50-digit precision was not achieved with the direct mpmath.dirichlet approach under the runtime limit. The partial run demonstrates that the pipeline is correct in principle for critical-line zeros and that multiprocessing can recover a substantial number of high-precision roots, but it also shows that this naive evaluator is not performant enough for the full target. A production-quality completion will likely require a faster evaluator, such as a specialized approximate functional equation or Riemann–Siegel-type implementation for the underlying Dirichlet L-functions, plus rigorous global zero counting to capture off-critical roots. Thus, the research hypothesis is only partially supported: the L_DH definition was correctly verified, but the first 5000 zeros were not fully computed and saved in this run. The negative-control dataset is therefore not yet complete.
</discussion>
<proposed-next-hypotheses>
1. Replacing mpmath.dirichlet with a specialized approximate-functional-equation or Riemann–Siegel-style evaluator for the mod-5 Dirichlet L-functions will reduce per-zero runtime enough to compute the first 5000 L_DH zeros at 50-digit precision within a similar wall-clock budget.
2. A contour-based zero-counting procedure combined with critical-line Z_DH scanning will show that off-critical zeros below the first 3000–4000 units of height are sparse relative to critical-line zeros, allowing certified enumeration through targeted 2D searches only in intervals where count discrepancies occur.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>ldh_def.py</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Python module containing the verified Davenport–Heilbronn L-function definition, the mod-5 character lists, and helper functions L_DH, theta_DH, and Z_DH. It was created directly in the workspace after verifying the functional equation and literature-known zeros.</artifact-description>
</artifact>
<artifact>
<file-name>ldh_worker.py</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Python worker module used for multiprocessing-based chunked zero scanning and refinement. It evaluates Z_DH on a grid, refines sign-change brackets to dps=50 roots, and writes periodic checkpoint files for recovery.</artifact-description>
</artifact>
<artifact>
<file-name>ldh_chunks/</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Directory of checkpoint pickle files produced during the parallel zero-finding run. Each chunk file stores partial or complete refined zeros for a specific t-interval and basic progress metadata such as bracket count and scan extent.</artifact-description>
</artifact>
</artifacts>
</output>
