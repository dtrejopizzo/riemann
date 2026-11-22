## Conclusion

The script could not complete generation of 5,000 L_DH zeros within the phase's 3,600-second budget because the previously generated `ldh_ckpt_02500.npy` checkpoint was not available in this workspace, forcing a from-scratch run whose per-zero cost grows steeply with t and exceeds the available wall time.

## Methods

1. Inspected the working directory and discovered only `generate_ldh_zeros.py`; no checkpoints, no prior NPY artifacts.
2. Searched the entire filesystem (`find the working directory …`, `find / …`) for any `ldh_ckpt_*` or `ldh_zeros_*` files; none existed. The script's hard-coded `WORK_DIR` points to a previous phase that is no longer accessible, and no `data_entry:` URIs to the prior checkpoint were found in memory.
3. Installed `cypari2 2.2.4` (and `cysignals 1.12.6`) via pip; verified PARI/GP `lfun` works at 50–80 dps.
4. Copied the script locally to obtain write permissions and updated `WORK_DIR` to the current workspace.
5. Benchmarked Z(t) evaluation cost: ~5 ms at t=50, ~7 ms at t=500, ~22 ms at t=1500, ~137 ms at t=3000, ~138 ms at t=5000 (with `lfuninit([5200])`, dps_pari=80).
6. Launched the script as a background subprocess starting from t=1.0 (no checkpoint to resume from), polling progress from `script_stdout.log` and `checkpoints_ldh/` every 5–10 minutes.
7. The script performs a grid scan with step `h=0.1`, sign-change detection, root refinement with `mpmath.findroot` (Anderson → Illinois → bisect fallback), strict-monotonicity guard, checkpointing every 250 zeros, and writes `ldh_zeros_5000_dps50.npy` only on completion.

## Results

- Setup: `lfuninit` at T_max=5200, dps_pari=80 completed in 6.9 s.
- Generation progress (from `run_log.txt` / `script_stdout.log`, wall-time relative to script start at 07:36:38): - 00:36 → 250 zeros, t≈356.3, cumulative rate 6.73 z/s - 01:24 → 500 zeros, t≈638.3, 5.97 z/s - 02:26 → 750 zeros, t≈903.0, 5.12 z/s - 03:50 → 1000 zeros, t≈1152.1, 4.34 z/s - 05:43 → 1250 zeros, t≈1402.5, 3.65 z/s - 08:13 → 1500 zeros, t≈1646.8, 3.04 z/s - 12:01 → 1750 zeros, t≈1893.1, 2.43 z/s - 16:27 → 2000 zeros, t≈2129.8, 2.03 z/s - 21:33 → 2250 zeros, t≈2359.7, 1.74 z/s - 29:49 → 2500 zeros, t≈2585.0, 1.40 z/s - 37:23 (last log captured) → ~2644 zeros, t≈2718.5
- Cumulative rate dropped monotonically from ~6.7 z/s to ~1.4 z/s, consistent with the measured ~28× growth in per-evaluation Z-function cost from t≈50 to t≈3000.
- All saved checkpoints passed the script's built-in strict-monotonicity guard (no "WARNING: non-monotonic root" entries were logged).
- Checkpoint NPY files written: `ldh_ckpt_00250.npy`, `…_00500.npy`, `…_00750.npy`, `…_01000.npy`, `…_01250.npy`, `…_01500.npy`, `…_01750.npy`, `…_02000.npy`, `…_02250.npy`, `…_02500.npy` (plus matching `_meta.json` files), in `./checkpoints_ldh/`.
- Final NPY `ldh_zeros_5000_dps50.npy` was NOT produced — the run was forcibly terminated by the phase time budget before reaching N_TARGET = 5000.
- Naive linear extrapolation at the phase-rate of ~0.5–0.7 z/s in the t∈[2500, 5000] regime suggests an additional ~70–80 minutes of compute would be required from the 2500-zero checkpoint to reach 5000 zeros.

## Challenges

- The hypothesis was predicated on resuming from `checkpoints_ldh/ldh_ckpt_02500.npy`, but that file lived only in an earlier run's working directory which is not mounted in this phase and was not uploaded to data storage. No `data_entry:` URI exists. The script therefore had to start from t=1.0, doubling the required work.
- The script file in the workspace was read-only; I copied it locally and edited `WORK_DIR` to the current phase directory.
- `cypari2` was not pre-installed; installation via pip succeeded.
- Per-zero cost is dominated by PARI's `lfun` evaluation of the χ and χ̄ Dirichlet L-functions at high t; cost grows roughly with the conductor-dependent functional-equation work and rises by ≳25× between t=50 and t=3000. As a result, the cumulative rate fell from 6.7 z/s to 1.4 z/s by zero #2500 and was projected to fall to ~0.3–0.5 z/s by zero #5000.
- The 3,600 s task wall-time budget is insufficient for a from-scratch run of 5,000 zeros at the present accuracy settings (dps=50, dps_pari=80, T_max=5200) on this hardware (single-process, no GPU).
- I was unable to upload the 2,500 produced zeros via the shared data store before time expired.

## Discussion

The hypothesis as stated — "Executing the script will successfully complete the generation of the first 5,000 critical-line zeros … at 50-decimal precision" — is **not confirmed** under the conditions of this phase. The script itself is correctly implemented (it ran without errors, checkpointed reliably every 250 zeros, and never flagged a non-monotonicity violation), but the necessary precondition — the prior 2,500-zero checkpoint — was not present, so the run had to start from scratch and the per-evaluation cost growth at large t makes the 5,000-zero target infeasible in 3,600 s wall-clock. To complete the phase in a future run one should either (i) upload `ldh_ckpt_02500.npy` to data storage so it can be restored to `checkpoints_ldh/` before launching, or (ii) launch the script with a longer wall budget (≈90 minutes from scratch, or ≈45 minutes from the 2500-zero checkpoint, on the same hardware), or (iii) parallelize the grid scan over disjoint t-intervals — the only sequential dependency is the boundary sign at each chunk's start.

## Next hypotheses

1. Resuming from `ldh_ckpt_02500.npy` and partitioning the residual range t ∈ [≈2585, ≈5200] into four equal sub-intervals processed in parallel separate long-running computation (with sign-overlap stitching at boundaries) will allow the remaining 2,500 zeros to be computed within a single 3,600 s wall budget.
2. Reducing PARI's working precision from `realprecision=80` to `realprecision=60` while retaining `mpmath.mp.dps=50` for the final refinement step will reduce the asymptotic per-Z cost at t≈3000 by ≳40% without degrading the precision of the saved 50-dp zeros.

## Files

- `checkpoints_ldh/ldh_ckpt_02500.npy` (computed) — Numpy object-array of the first 2,500 critical-line zeros of the Davenport-Heilbronn L-function, computed at 50-decimal precision and stored as decimal strings. Generated from scratch (t=1.0) by running `generate_ldh_zeros_local.py` (a writeable copy of `generate_ldh_zeros.py` with `WORK_DIR` redirected to the current phase) in this run. All 2,500 zeros passed the script's strict-monotonicity guard during generation. The final 5,000-zero file `ldh_zeros_5000_dps50.npy` was NOT produced; intermediate checkpoints at every 250 zeros (00250, 00500, … 02500) and their `_meta.json` files reside in `./checkpoints_ldh/`.
- `generate_ldh_zeros_local.py` (computed) — Local writeable copy of `generate_ldh_zeros.py` with one edit: `WORK_DIR` updated from the inaccessible path of an earlier run to the current phase's working directory. All other logic (cypari2 lfuninit at T_max=5200, dps_pari=80, grid step h=0.1, anderson/illinois/bisect refinement, every-250 checkpointing, strict-monotonicity guard) is preserved. This is the script that was executed in this phase.
- `run_log.txt` (computed) — Plain-text log emitted by `generate_ldh_zeros_local.py` recording startup, lfuninit timing, each 250-zero checkpoint (count, t, elapsed, cumulative rate, total Z-evaluations), and minute-level progress entries up to the phase's wall-time termination. Useful for benchmarking the t-dependence of L_DH zero-finding throughput.
