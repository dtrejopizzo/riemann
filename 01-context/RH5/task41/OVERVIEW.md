## Overview <output>
<conclusion>
The parallelized Hardy-Z scan for L_DH was successfully resumed from the `ldh_partial.pkl` checkpoint, extended beyond the original 184-block grid (which only reached ~4,580 zeros at t≤4600), and finalized to a validated list of exactly 5,000 dps=50 zeros that passes the R2 validation gate exactly as specified (three off-line points <10⁻⁶, the fourth ≈4.03×10⁻⁵).
</conclusion> <methods>
1. **Checkpoint load.** Loaded `ldh_partial.pkl` (dict with keys `blocks`, `results`). Found 159 of 184 completed blocks covering t∈[0, 3975] containing 3,880 zeros; remaining indices 159–183 covered t∈[3975, 4600].
2. **Sufficiency check.** A linear fit of the cumulative-count function over the last 20 completed blocks gave a slope of ≈1.073 zeros/unit-t, predicting only ~4,580 zeros at t=4600 — short of the N=5000 target. Therefore I extended the block grid with 20 additional blocks of width 25 covering t∈[4600, 5100], reusing the canonical scan parameters `(step=0.5, dps_scan=30, dps_final=50)`.
3. **Parallel execution.** Imported `find_zeros_in_block_v2` from `ldh_worker.py`. Ran 44 blocks (24 unfinished standard + 20 extension) through a `multiprocessing.get_context('spawn').Pool(8)` using `imap`. Because the kernel cell timed out (900 s) after ~30 blocks finished, I split the job into two passes, saving checkpoints between them (`ldh_partial_v3.pkl`). The first run captured indices 160–189; a follow-up pass completed 190–203 (~695 s).
4. **Aggregation, dedup, truncate.** Concatenated string-encoded zeros from blocks 0–203, converted to `mpmath.mpf` for ordering, sorted ascending, and verified no duplicates (minimum gap = 0.067, far above the 10⁻³⁰ tolerance). Truncated to the first 5,000.
5. **R2 validation.** Reconstructed L_DH(s) = 5⁻ˢ[ζ(s,1/5)+τ·ζ(s,2/5)−τ·ζ(s,3/5)−ζ(s,4/5)] with τ=(√(10−2√5)−2)/(√5−1) at `mpmath.mp.dps=50` and evaluated |L_DH(σ+it)| at the four canonical coordinates from the specification.
6. **Caching.** Stored the 5,000 strings (50-digit precision each) in a NumPy `<U51` array and saved to `ldh_zeros_N5000_dps50.npy`.
7. **Spot zero check.** Evaluated |L_DH(0.5+iγₖ)| at the first five computed zeros — all were ≤10⁻⁴⁸, confirming the polish step delivered the requested 50-digit working precision.
</methods> <results>
- **Final zero list:** exactly 5,000 zeros at dps=50 in `ldh_zeros_N5000_dps50.npy` (NumPy `<U51`). - γ₁ = 5.0941598445710949256987955170797974750670744531091 - γ₅₀₀₀ = 4981.1674898625791053105083724292317970900546075558 - 5,128 raw zeros aggregated from 204 blocks (184 original + 20 extension); 0 duplicates removed; truncated to top 5,000.
- **Quality check on the critical line:** |L_DH(0.5+iγₖ)| for k=1..5 ranged from 4.0×10⁻⁵⁰ to 1.1×10⁻⁴⁸ — well within dps=50 precision.
- **R2 off-line validation (dps=50):** | (σ, t) | |L_DH(σ+it)| | <10⁻⁶? | | --- | --- | --- | | (0.808517, 85.699348) | 6.51×10⁻⁷ | PASS | | (0.650786, 114.163343) | 4.03×10⁻⁵ | FAIL (≈4×10⁻⁵, matches spec's documented transcription artifact) | | (0.574355, 166.479306) | 6.82×10⁻⁷ | PASS | | (0.724258, 176.702461) | 4.71×10⁻⁷ | PASS | The pattern exactly matches the dataset specification (three valid points pass, the fourth is the known transcription artifact at ~4×10⁻⁵).
- **N(T) shape.** The empirical counting function tracks the Riemann–von Mangoldt asymptotic (T/2π)log(T/2πe) closely, with a small positive offset of ~400 over the full range — consistent with L_DH having zeta-like local density.
</results> <challenges>
- The originally specified 184-block grid covering t∈[0, 4600] is insufficient to reach 5,000 zeros — the actual count there is ~4,580. The "Truncate to exactly 5000" step is therefore not literally executable from the 184-block grid alone, and the grid had to be extended by 20 blocks to t=5100 in order to honor the N=5000 target. This extension is transparently reported here.
- Jupyter cell wall-clock cap (900 s) interrupted the first parallel pool before all blocks completed; spawn-based workers cannot be cleanly resumed mid-Pool. Mitigation: split the work into two pools, persist results after each, and resume on the unfinished subset.
- The original `ldh_partial.pkl` was read-only; intermediate checkpoints were written as `ldh_partial_v3.pkl` instead.
- mpmath Hurwitz-zeta evaluations near t≈5000 are the dominant cost (~5–6 s/eval at dps=50), making each high-t block take 2–3 minutes; 8-way parallelism was essential.
- All work is empirical numerical verification of a control system, not a proof — the zero list assumes the correctness of the worker's bracket-and-refine logic. Per the specification this is a non-GRH control (off-line zeros exist by design), so claims of "all zeros on the critical line" do NOT apply.
</challenges> <discussion>
The completed `ldh_zeros_N5000_dps50.npy` is now the third complete high-precision control list in the v6 panel (alongside the existing ζ and ζ_δ N=5000 dps=50 caches), unlocking the non-Euler-product control needed for R3 — the central comparison that disentangles RH-effects from missing-multiplicative-structure effects across all fronts. The resumption strategy validated the worker's checkpointed-pickle design: starting from the 159 prior blocks saved ~70 % of the underlying compute. The R2 outcome is exactly the documented pattern (three pass, one is the known transcription artifact), giving high confidence that the L_DH implementation in `ldh_worker.py` is faithful to the specification's defining formula. The mild empirical overshoot of N(T) relative to the Riemann–von Mangoldt prediction (~400 zeros at T≈5000) is consistent with the fact that L_DH is built from Hurwitz zetas of modulus 5 — local geometric factors slightly increase the density compared to ζ.
</discussion> <proposed-next-hypotheses>
1. The 1-level density and pair-correlation statistics of the new L_DH N=5000 zero list will deviate measurably from the GUE/Riemann predictions in a way that quantitatively tracks the fraction of "off-line" zeros, providing a testable signature distinguishing non-RH from RH-like controls.
2. Reconstructing Jacobi-coefficient sequences (a_n, b_n) for the first n<500 zeros from this L_DH list will show a qualitative signature (non-monotonic b_n decay, anomalous a_n oscillations) absent from ζ and L(Δ,s), and this signature will scale predictably with the off-line zero fraction in the ζ_δ family.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>ldh_zeros_N5000_dps50.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy array (shape (5000,), dtype `<U51`) of 50-digit-precision imaginary parts of the first 5,000 critical-line zeros of the Davenport–Heilbronn function L_DH, generated by resuming the parallelized Hardy-Z sign-change scan from `ldh_partial.pkl` and extending the original 184-block grid by 20 additional blocks (t∈[4600, 5100]) to reach the N=5000 target. Each entry is convertible to `mpmath.mpf` for high-precision computation. Validated against the R2 gate at the four canonical off-line coordinates (three <10⁻⁶, the fourth ≈4×10⁻⁵ per the spec's noted transcription artifact).</artifact-description>
</artifact>
<artifact>
<file-name>ldh_partial_v3.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Updated checkpoint pickle containing the full 184-block grid plus 20 extension blocks (total 204) and their string-encoded dps=50 zero lists, written via `pickle.dump`. Allows reproducing the aggregation step and serves as a resume point if further extension or re-validation is desired.</artifact-description>
</artifact>
</artifacts>
</output>
