# Round 22-B: full Lanczos scan of the low-end strip r ∈ [1.1, 1.3] at T ≥ 4

Object: the band margin μ_η(τ) = m(τ) − λ_max(A_τ^{(η)}), η = 1/8, of ROUND_017_B / ROUND_021_B (definitions in
tools/band_lanczos.py), with r = τ/(2π e^{2T}). Every value below is NUMERICAL.

## 1. Tool

tools/strip_scan.py (new). Scan grid τ ∈ w₀ + δℤ with δ = h/m, h = π/2T (m = 5 for T ≤ 4.5, m = 4 for T = 5, so
δ ≤ 0.0785). Then every frequency τ ± a_k (a_k = kh) lies on the same grid, and the vectors of the closed form are
s1_k = ½[S(τ+a_k) − S(τ−a_k)], d_k = ½[D(τ+a_k) + D(τ−a_k)], S(w) = Σ v_n sin(w l_n), D(w) = Σ v_n (2T − l_n) cos(w l_n),
tabulated once per T. The operator is the one of tools/band_lanczos.py; check against LBand (tools/align_band.py) at
T = 4, τ = 1.15·2πe⁸: μ = 0.77009589922 vs 0.77009589921 (difference 1.3·10⁻¹¹). Resumable: finished chunks are
stored in tools/strip22/<prefix>_chunks/; usage `OMP_NUM_THREADS=1 TLIM=sec python3 strip_scan.py T m r_lo r_hi prefix nproc`.

**Cost (measured).** The scan is Lanczos-bound: one top eigenpair costs ≈ 2–4 s at T = 4 (K ≈ 6.6–7.8·10³), ≈ 30–45 s
per process at T = 4.5 (K ≈ 2.0–2.4·10⁴) and ≈ 60–185 s at T = 5 (K ≈ 6·10⁴) on the shared machine. The strip has
47 697 grid points at T = 4.0, 145 857 at T = 4.5 and ≈ 3.5·10⁵ at T = 5.0. A pure warm start was retested and again
locks onto non-top eigenvectors (T = 4, τ ≈ 21 542.7: 7.31598 vs 7.31633), so the warm-plus-random start of ROUND_017_B is
kept. Consequence: within the run budget the full strip is covered only at its low end (§2); T = 4.5 and T = 5 are
reached through cell tracking (§3) and short contiguous strip segments.

## 2. Strip scans (task 1)

Grid step δ = 0.0785 (T = 4.0, 5.0), 0.0698 (T = 4.5); polish of the lowest grid minima with tools/strip22/polish22.py
(tools/align_band.cell, ALIGN_WIN = 0.2: scan ± 0.2 step 0.02, bounded Brent xatol 2·10⁻⁵; η = ¼ at the minimiser).
Lanczos residual ≤ 9.5·10⁻⁹ at every scanned point. Data: tools/strip22/s40.npz, s45.npz, s50.npz (+ *_chunks/,
resumable), p40.npy, p45.npy.

### 2.1 T = 4.0: r ∈ [1.100, 1.158] covered contiguously (14 247 points; 29% of the strip), 63 cells polished
(all grid local minima ≤ 0.214 in the covered range). Strip minimum on the covered part:
**μ_⅛ = 0.079788 at τ = 20948.73412** (r = 1.1185, K = 6668, residual 1.9·10⁻¹⁰; η = ¼: 0.079775); grid value 0.0847.
Next cells: 0.087195 (τ = 21623.87387, r = 1.1545; η = ¼ 0.087171; grid 0.0979), 0.122970 (21075.32797, r = 1.1252),
0.129300 (20989.88415), 0.132184 (21456.35211), 0.134069 (20812.04990), 0.137680 (20934.75963), 0.139178
(20608.86580, r = 1.1003). Largest polish gain 0.022 (21456.35: grid 0.154 → 0.132). Not covered: r ∈ (1.158, 1.3].
The covered-strip minimum 0.0798 lies below the ROUND_021_B value for T = 4.0 (0.0839 at r = 1.64), consistent with
the low-end law, and above the overall smallest value 0.0631 (T = 4.2).

### 2.2 T = 4.5: r ∈ [1.1000, 1.1008] only (607 points, τ ∈ [56004.50, 56046.80]); 5 cells polished
Segment minimum **0.137703 at τ = 56042.82204** (η = ¼: 0.137675; K = 20068, residual 8.6·10⁻⁹); next 0.138186 (56042.8127, same
dip), 0.140015 (56038.15659), 0.179162 (56016.56743). Coverage 0.4% of the strip: not a strip minimum.

### 2.3 T = 5.0: r ∈ [1.10000, 1.10005] only (90 points, τ ∈ [152236.00, 152243.39], K ≈ 6.06·10⁴)
Grid minimum 0.12255 (τ = 152241.972), next 0.13735 (152237.495); not polished (one polish ≈ 36 eigensolves ≈ 1–2 h of
one process at this K). Coverage 0.03%: not a strip minimum.

Per-T summary (all upper bounds for the strip minimum except where coverage is stated):

| T | coverage of r ∈ [1.1,1.3] | strip value found | τ | r |
|---|---|---|---|---|
| 4.0 | [1.100, 1.158] | 0.07979 | 20948.73412 | 1.1185 |
| 4.25 | none | (ROUND_021_B: 0.0836 at r = 1.33, outside strip) | | |
| 4.5 | [1.1000, 1.1008] | 0.13770 | 56042.82204 | 1.1008 |
| 4.75 | none | — | | |
| 5.0 | [1.10000, 1.10005] | 0.12255 (grid) | 152241.972 | 1.1000 |

## 3. Tracking of the three deepest known cells continuously in T (task 2)

Cells: the three deepest values of ROUND_021_B §5 (τ₀ = 30775.056, 41081.584, 63751.812). At each T (grid step 0.05,
plus the three T at which r = 1.1, 1.05, 1.01 exactly) the cell is re-polished (scan τ₀ ± 0.2 step 0.02, bounded Brent,
xatol 2·10⁻⁵); tools/strip22/track22.py, data tools/strip22/trk1.npy. Lanczos residual ≤ 9·10⁻⁹ everywhere; the
minimiser moves by ≤ 0.005 in τ over the whole T-range (the cell is a fixed arithmetic feature).

| cell τ* | r | T | μ_⅛ |
|---|---|---|---|
| 30775.05 | 1.643 / 1.487 / 1.345 / 1.217 / 1.101 | 4.00 / 4.05 / 4.10 / 4.15 / 4.20 | 0.08388 / 0.07649 / 0.07118 / 0.06728 / 0.06312 |
|  | **1.100 / 1.050 / 1.010** / 0.997 | 4.2006 / 4.2239 / 4.2433 / 4.25 | **0.06306 / 0.06114 / 0.05953** / 0.05887 |
| 41081.58 | 1.625 / 1.470 / 1.330 / 1.204 / 1.089 | 4.15 / 4.20 / 4.25 / 4.30 / 4.35 | 0.10288 / 0.09239 / 0.08360 / 0.07678 / 0.07082 |
|  | **1.100 / 1.050 / 1.010** / 0.986 | 4.3451 / 4.3683 / 4.3877 / 4.40 | **0.07134 / 0.06932 / 0.06803** / 0.06728 |
| 63751.81 | 1.690 / 1.529 / 1.384 / 1.252 / 1.133 / 1.025 / 0.928 | 4.35 / 4.40 / 4.45 / 4.50 / 4.55 / 4.60 / 4.65 | 0.10432 / 0.09567 / 0.08841 / 0.08318 / 0.07864 / 0.07388 / 0.06650 |
|  | **1.100 / 1.050 / 1.010** | 4.5648 / 4.5880 / 4.6075 | **0.07731 / 0.07506 / 0.07321** |

Rate. At each fixed cell μ decreases monotonically as T grows (r falls), smoothly and nearly linearly in log r:
least-squares slope dμ/d log r = 0.047, 0.070, 0.058 (max deviation from the line 0.0018, 0.0030, 0.0022), with the
local slope on r ∈ [~0.99, 1.1] equal to 0.042, 0.037, 0.063. Along the admissible part (r ≥ 1.1) the drop from
r = 1.64 to r = 1.1 is 0.021, 0.032, 0.027. Between r = 1.1 and r = 1.0 (outside the admissible window; recorded
because the task asks for r = 1.0 + δ) the further drop is only 0.004, 0.004, 0.005. Linear extrapolation in log r
places the zero of each cell at r ≈ 0.29, 0.39, 0.29, i.e. far below the window; no tracked cell approaches 0.02.
Per-cell values at the low end r = 1.1 do not decrease with the cell's T: 0.0631 (T = 4.20), 0.0713 (T = 4.35),
0.0773 (T = 4.56).

Two further cells (the deepest of the T = 4.0 strip, §2.1) tracked the same way (data tools/strip22/trk2.npy):

| cell τ* | r | T | μ_⅛ |
|---|---|---|---|
| 20948.73 | 1.669 / 1.510 / 1.366 / 1.236 / 1.118 | 3.80 / 3.85 / 3.90 / 3.95 / 4.00 | 0.11957 / 0.10550 / 0.09519 / 0.08640 / 0.07979 |
|  | **1.100 / 1.050 / 1.010** | 4.0083 / 4.0316 / 4.0510 | **0.07889 / 0.07639 / 0.07457** |
| 21623.87 | 1.558 / 1.410 / 1.276 / 1.155 | 3.85 / 3.90 / 3.95 / 4.00 | 0.10810 / 0.09901 / 0.09230 / 0.08720 |
|  | **1.100 / 1.050 / 1.010** | 4.0242 / 4.0474 / 4.0669 | **0.08489 / 0.08279 / 0.08099** |

Same behaviour: monotone decrease in T, average slope dμ/d log r = 0.090 and 0.062, local slope on [1.01, 1.1] 0.051
and 0.046, so the curve is convex in log r (it flattens toward the low end). Values at r = 1.1: 0.0789, 0.0849.

## 4. Stop rule (task 3)

Not triggered: the smallest margin met anywhere in this round is 0.0589 (cell τ = 30775.06 at r = 0.997, outside the
admissible window); inside r ≥ 1.1 the smallest is 0.0631 (τ = 30775.06, T = 4.2006, r = 1.100), already known.
No margin < 0.02, so tools/band_direct.py was not run. **No negative value; no candidate.**

## Result

PIVOT (counterexample watch, NUMERICAL): no band margin below 0.02. Low-end strip at T = 4.0 (r ≤ 1.158): minimum
0.0798. Five deepest known cells, tracked continuously in T, decrease smoothly and monotonically as r falls, by
0.02–0.045 between r ≈ 1.65 and r = 1.1 and only 0.004–0.005 more between r = 1.1 and r = 1.01, with the curve
flattening (convex in log r); their values at r = 1.1 are 0.0631, 0.0713, 0.0773, 0.0789, 0.0849, with no decrease
in the cell's T. The full strip at T ≥ 4.5 is out of reach of the present eigensolver (Lanczos cost × 1.5–3.5·10⁵ points).

## What was proved

Nothing (computational memo). All values NUMERICAL; residuals ≤ 10⁻⁸. Reproducibility: tools/strip_scan.py
(`OMP_NUM_THREADS=1 TLIM=1380 [CHUNK=50] python3 strip_scan.py T m 1.1 1.3 prefix nproc`, m = 5 at T = 4, 4.5, m = 4 at
T = 5), tools/strip22/polish22.py (`python3 polish22.py prefix.npz T 40 out.npy nproc`), tools/strip22/track22.py
(`python3 track22.py out.npy nproc tau0:Tlo:Thi:1.1,1.05,1.01 …`); logs tools/strip22/*.log.

## What failed and why

The full scan of r ∈ [1.1, 1.3] was completed for no T: each point needs a cold-mixed Lanczos top eigenpair of size
K = 2Tητ/π (6.6·10³ at T = 4, 2·10⁴ at T = 4.5, 6·10⁴ at T = 5); measured throughput was ≈ 2 000–6 500 points per 25-minute
run at T = 4 and ≈ 400 at T = 4.5 on the shared machine, against 4.8·10⁴ / 1.5·10⁵ / 3.5·10⁵ points needed. The grid
tabulation (§1) removed the trigonometric cost but not the eigensolver cost; a pure warm start is unreliable (§1).

## Next concrete step

Either (a) finish T = 4.0 on r ∈ (1.158, 1.3] (≈ 3 more runs, resumable as is) and stop scanning, accepting the
tracked-cell law as the T ≥ 4.5 evidence; or (b) a cheaper certified locator: a Lipschitz bound for λ_max(A_τ) in τ
(dλ/dτ = ⟨∂_τA x, x⟩, ∂_τA explicit from the closed form) to replace the 0.08 grid by a certified coarser grid with
a lower bound for the margin between grid points.
