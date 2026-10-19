# Off-machine computation package — the two-prime window at `T = 0.58` (R154_030 §3, decision (b))

**Purpose.** Decide, by computation on a workstation (not the local machine), whether the lattice/hybrid
certificate class reaches `c > 0` at the first two-prime window `T = 0.58` (Galerkin upper bound
`λ_min ≈ 2.16·10⁻⁴`; best certified value so far `−3.1802·10⁻³`, R154_015/028). Nothing here is
mathematics; it is the value problem of R154_030 §2. All results are DIAGNOSTIC until the final
step (exhaustive second-order cover + interval enclosures) has run with `0` unresolved cells.

**Requirements.** Python 3.10+, `numpy`, `scipy ≥ 1.11` (HiGHS), `mpmath 1.3`. One run of step 3 needs
~20 cores for ~30 min; steps 1–2 are single-process LPs of 1–6 h each. RAM ≤ 16 GB. Copy the whole
directory `03-research/phase-154-row-d-law-of-the-body/scripts/` (rounds 4, 5, 6, 9, 10 are imported
by relative path).

## The three experiments (run in this order; stop as soon as one gives `c > 0` after step 3)

### E1 — the `M`-sweep with row+column generation (the lever named in R154_015 §5.1, R154_017 §4)
```
cd ../round6
for M in 32 44 64 96 128; do
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 timeout 21600 \
  python3 r6cg.py --T 0.58 --M $M --U 20 --tau1 30 --N 3 --iters 400 --patience 40 --maxsec 21000 \
     --out OFF058M$M > sw_OFF058M$M.log 2>&1
done
```
Report per `M`: final LP value, true refined minimum (`sep_min` in the log), `Σ|a_j|`, `β₀`, `β₁`, wall.
The question is whether `c(M)` crosses zero at an attainable `M` (at `½log3` it crossed between
`M = 16` and `19`; at `0.58` `M = 24` gives `−3.18·10⁻³`). `N = 3` is used because R154_016 measured
that the `k = N` worst-case row is binding at `N = 2` (moves to `+0.19` at `N = 3`).

### E2 — the hybrid LP at `N = 6` (R154_028 §4.5, Prop. X; R154_029 says UNRESOLVED at `N = 2`)
```
cd offmachine
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 timeout 36000 python3 hybrid_N.py --N 6 --iters 60 --tag H6 > H6.log 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 timeout 36000 python3 hybrid_N.py --N 6 --iters 60 --tag C6 --nocols > C6.log 2>&1
```
`hybrid_N.py` runs `round10/r10lp.run` with the worst-case block pushed to `τ₁ + NP ≈ 810` and, per
R154_029 L-b, with the four solver diagnostics the round-10 run lacked: interior-point method
(`highs-ipm`) instead of dual simplex (rows still scaled by `S = 1e4` as in round 10; to test `S = 1` edit `round10/r10lp.py` line 154), solver status printed for every solve, and a
feasibility check of the round-5 control point against every row set (a maximisation LP whose value
falls below a feasible point is VOID — R154_029 §3). Compare `H6` (two canonical columns `ν_{½,0}`,
`ν_{½,1}`) with the matched control `C6` (columns fixed to 0). The question is whether the column
buys anything once its tail price `|c₀|/√(¼+810²) ≈ 1.2·10⁻³|c₀|` is below the deficit.

### E3 — polish and certify whatever E1/E2 produce (the round-5 pipeline, R154_011 accepted)
```
cd ../round5
python3 r5polish.py ../round6/lp_OFF058M64.pkl --G 128 --scale 1e4 --hp --out P058M64      # ≈ 1 h
python3 r5bb.py drive lp_P058M64.pkl --target <half of the fine-grid infimum printed by r5polish> --wmin 1e-9 --nproc 19 --dir bb_P058M64
python3 r5final.py lp_P058M64.pkl bb_P058M64/_all.json --tag CERT_T058_OFF
```
A certificate exists iff `r5final.py` reports `checks_failed: []`, `0` unresolved cells and a strictly
positive interval enclosure at every argmin. Archive the JSON next to `round5/certificate/`.

## What to report back (one table)
| experiment | class size | LP value | true min | after polish | certified `c` (0 unresolved?) | wall |

## What the result means (both outcomes are useful)
* `c > 0` at some `M` or at `N = 6`: the staircase climbs one step; steps `0.62 … log 2` then reuse the
  shape within the contact set `{2,3}` (R154_015 §6; note R154_017 refuted the cheap lattice
  rescaling — re-solve each step with warm start instead).
* `c(M)` saturates below `0` up to `M = 128`: a theorem-shaped negative — the lattice class at these
  resolutions does not reach the two-prime window; feeds Problem A of Paper 47 §8 (phase 155).

Nothing in this package touches the FATAL rule: `T = 0.58 < log 2` is Paper-42-certified; the run
produces an independent dual certificate or fails to.
