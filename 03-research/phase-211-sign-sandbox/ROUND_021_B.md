# Round 021 B — Band margins at the small-prime alignment cells, T = 3.5–4.5

Notation of ROUND_016_A and ROUND_017_B: N = e^{2T}, v_n = 2Λ(n)/√n (n < N), ℓ_n = log n, m(t) = Re ψ(¼ + it/2) − log π,
A_τ^{(η)} the band compression (closed form, ROUND_017_B Proposition 1.1), μ_η(τ) = m(τ) − λ_max(A_τ^{(η)}),
g_T(ω) = m(ω) − Σ_n v_n(1 − ℓ_n/2T)cos(ωℓ_n) (flat-tone function), range [1.1, 3]·2πN.
All statements in this memo are NUMERICAL unless labelled otherwise.

## 0. Corpus check

Index rows read: P211-16A, P211-17B. Same object (A_τ^{(η)}, the packet identity of ROUND_016_A Theorem 1.1); no route
is retried. What differs from ROUND_017_B: the τ-cells are chosen arithmetically (simultaneous approximation of
τ log p/2π, p ≤ 7, to integers) instead of by a uniform τ-scan, which makes the whole range [1.1, 3]·2πN reachable at
T ≥ 3.5, where ROUND_017_B covered only [1.1, 1.2]·2πN (T = 3.5). This is a counterexample watch, not a sign argument;
the falsifier test of the brief does not apply to it.

## 1. Method

Tool: tools/align_band.py (output in tools/align21/). Two candidate families in [1.1, 3]·2πN:
(a) the 4-prime alignment function h₄(τ) = Σ_{p ∈ {2,3,5,7}} (1 − cos(τ log p)), local minima on an exhaustive grid of
step 0.004 (the fastest phase, τ log 7, moves by 0.0078 per step), Brent-polished; quality of the simultaneous
approximation recorded as δ(τ) = max_p ‖τ log p/2π‖ (distance to the nearest integer);
(b) the lowest local minima of g_T (grid step 0.02, Brent-polished).
At each candidate τ₀: μ_⅛ on τ₀ ± 0.1 (step 0.02, warm-started Lanczos with the random admixture of ROUND_017_B, tol
10⁻⁹), then bounded Brent (xatol 2·10⁻⁵) around the best scan point; μ_¼ at the minimiser. The matrix-free operator is
that of tools/band_lanczos.py with s, d computed in chunks (no K × #n storage). Check: μ_⅛(3.5, 7713.88056) = 0.078201
(ROUND_017_B: 0.078201).

## 2. Results

### 2.1 T = 3.5, full range [1.1, 3]·2πN = [7579.4, 20671.0] (15 h₄-cells + 15 g-cells)

Columns: τ* (polished minimiser of μ_⅛), h₄(τ*), δ(τ*), g_T(τ*), μ_⅛, μ_¼, K_⅛. Lanczos residual ≤ 5·10⁻⁹ at every
point. Lowest eight of 30 cells:

| family | τ* | h₄ | δ | g_T | μ_⅛ | μ_¼ | K_⅛ |
|---|---|---|---|---|---|---|---|
| h₄ | 14303.97045 | 0.107 | 0.043 | 1.355 | **0.154061** | 0.154022 | 3983 |
| h₄ | 11204.19745 | 0.139 | 0.049 | 0.794 | 0.155337 | 0.155315 | 3120 |
| h₄ | 15853.96282 | 0.083 | 0.059 | 1.102 | 0.166366 | 0.166269 | 4415 |
| g | 13651.85567 | 0.160 | 0.077 | 0.526 | 0.177931 | 0.177844 | 3802 |
| h₄ | 17403.94152 | 0.142 | 0.072 | 1.252 | 0.181026 | 0.180982 | 4847 |
| h₄ | 10923.45216 | 0.117 | 0.051 | 1.046 | 0.210470 | 0.210378 | 3042 |
| h₄ | 12754.06400 | 0.129 | 0.051 | 0.802 | 0.223943 | 0.223727 | 3552 |
| h₄ | 19851.46819 | 0.079 | 0.046 | 1.084 | 0.234448 | 0.232454 | 5529 |

The best simultaneous approximation in range (h₄ = 0.0707 at τ = 18301.59, δ = 0.050) gives μ_⅛ = 0.397. All 30 cells
have μ_⅛ ≥ 0.154, i.e. *above* the non-aligned cell of ROUND_017_B (0.078201 at τ = 7713.88056).

**Correction to the ROUND_017_B remark.** At τ = 7713.88056 the fractional phases τ log p/2π (nearest-integer
residues) are −0.022, −0.231, −0.089, −0.002, −0.099, −0.006 for p = 2, 3, 5, 7, 11, 13 (h₄ = 1.046): p = 3 is a quarter
cycle off, so this is not a simultaneous small-prime alignment. At the T = 3.25 minimiser τ = 5228.68250 (μ_⅛ = 0.1343)
the residues are −0.18, 0.23, 0.33, 0.33, 0.46, 0.48 (h₄ = 4.43): anti-aligned, if anything. At the T = 3 minimiser
τ = 2819.23599: 0.012, −0.058, 0.147, 0.121 (h₄ = 0.74). The deepest band cells are therefore not located by
small-prime alignment, and the alignment cells are not the deepest cells: over the whole range at T = 3.5, the
correlation between h₄ (or δ) and μ_⅛ across the 15 h₄-cells is weak (h₄ ∈ [0.071, 0.138], μ_⅛ ∈ [0.154, 0.472]).

### 2.2 T = 3.75 (10 h₄ + 5 g cells) and T = 4.0 (8 h₄ + 4 g cells), full range [1.1, 3]·2πN

T = 3.75, range [12496.3, 34080.8]; best h₄ in range 0.01795 (τ = 28327.24, δ = 0.023). Lowest cells:

| family | τ* | h₄ | δ | μ_⅛ | μ_¼ (same τ*) | K_⅛ |
|---|---|---|---|---|---|---|
| h₄ | 30774.98295 | 0.068 | 0.050 | **0.171083** | 0.171057 | 9183 |
| g | 16751.52857 | 0.197 | 0.096 | 0.187998 | 0.187965 | 4998 |
| g | 12582.38927 | 0.900 | 0.219 | 0.201966 | 0.201897 | 3754 |
| h₄ | 18301.63417 | 0.077 | 0.038 | 0.225382 | 0.225151 | 5461 |
| h₄ | 32324.87583 | 0.065 | 0.053 | 0.252072 | 0.252029 | 9646 |
| h₄ | 28327.24376 | 0.018 | 0.023 | 0.333886 | 0.246518 | 8453 |

T = 4.0, range [20602.9, 56189.7]; best h₄ 0.01795 (τ = 28327.24). Lowest cells:

| family | τ* | h₄ | δ | μ_⅛ | μ_¼ (same τ*) | K_⅛ |
|---|---|---|---|---|---|---|
| h₄ | 30774.98286 | 0.068 | 0.050 | **0.116024** | 0.116007 | 9795 |
| h₄ | 32324.87605 | 0.065 | 0.054 | 0.156458 | 0.156431 | 10289 |
| h₄ | 45079.03773 | 0.080 | 0.051 | 0.168602 | 0.168586 | 14349 |
| h₄ | 28327.25504 | 0.019 | 0.026 | 0.191887 | 0.159441 | 9016 |
| g | 25227.28907 | 0.149 | 0.078 | 0.202156 | 0.188324 | 8030 |
| h₄ | 33874.76852 | 0.078 | 0.057 | 0.229812 | 0.159470 | 10782 |

Residuals ≤ 7·10⁻⁹ everywhere. Where μ_¼ < μ_⅛ by more than 0.01 the η = ¼ margin was polished separately
(tools/align21/pol4.py, minimising μ_¼ over τ): min μ_¼ = 0.15036 (T = 4, τ = 33874.79607), 0.15552 (T = 4,
τ = 28327.27651), 0.17682 (T = 4, τ = 25227.25976), 0.23268 (T = 3.75, 28327.28045), 0.30865 (T = 3.75, 26777.31272),
0.24924 (T = 3.5, 18301.48041). None goes below the μ_⅛ minimum at the same T. At these cells the η = ¼ envelope
uses modes with a_k > τ/8 (the η = ⅛ band misses them); the best simultaneous approximation (h₄ = 0.018, δ = 0.023)
is exactly such a cell.

The same arithmetic cell τ ≈ 30774.98 is the deepest one found at both T = 3.75 and T = 4.0, its margin decreasing
from 0.171 to 0.116 as T grows (§3).

**Caveat on §2.1–2.2 (a defect found).** The polish window τ₀ ± 0.1 is too narrow at some cells: at τ₀ = 30774.88 the
μ_⅛-minimum sits at τ = 30775.05, outside the window, so the tabulated values there are upper bounds. The tracking of
§3 (window re-centred) supersedes them: at T = 3.75 the cell gives 0.13787 (not 0.171), at T = 4.0 0.08388 (not 0.116).
The T = 4.5 runs below use half-width 0.2.

## 3. Fixed arithmetic cells tracked across T (tools/align21/track.py)

Three cells: τ ≈ 7713.88 (the ROUND_017_B minimiser), τ ≈ 14303.97 (best cell of §2.1), τ ≈ 30775.05 (best cell at
T = 3.75, 4.0). Residues of τ log p/2π for p = 2, 3, 5, 7, 11, 13:
7713.8806: −0.022, −0.231, −0.089, −0.002, −0.099, −0.006; 14303.967: −0.018, 0.043, −0.039, −0.044, −0.079, 0.228;
30775.056: 0.036, 0.005, 0.030, 0.072, −0.104, 0.128. The last two are simultaneous 4-prime alignments (δ ≤ 0.072),
the first is a partial one (2, 7, 13 aligned; 3 a quarter cycle off).
At each T: μ_⅛ minimised over τ₀ ± 0.1 (re-centred), r = τ*/2πN.

| τ cell | T | τ* | r | μ_⅛ |
|---|---|---|---|---|
| 7713.88 | 3.0 | 7713.90394 | 3.04 | 0.49463 |
| | 3.25 | 7713.88650 | 1.85 | 0.19601 |
| | 3.375 | 7713.88510 | 1.44 | 0.12589 |
| | 3.5 | 7713.88056 | 1.12 | 0.07820 |
| 14303.97 | 3.25 | 14303.97514 | 3.42 | 0.21869 |
| | 3.5 | 14303.97045 | 2.08 | 0.15406 |
| | 3.6 | 14303.96924 | 1.70 | 0.12956 |
| | 3.75 | 14303.96707 | 1.26 | 0.10610 |
| 30775.05 | 3.75 | 30775.04472 | 2.71 | 0.13787 |
| | 3.875 | 30775.04858 | 2.11 | 0.11224 |
| | 4.0 | 30775.05123 | 1.64 | 0.08388 |
| | 4.1 | 30775.05432 | 1.35 | 0.07118 |
| | 4.2 | 30775.05574 | 1.10 | 0.06312 |

Observations (NUMERICAL). (i) At a fixed τ the margin decreases monotonically as T grows (r decreases toward the
lower end 1.1 of the range): adding primes and widening the window deepens the same arithmetic cell. (ii) Hence for
each cell the deepest admissible value is at r ≈ 1.1, i.e. at T ≈ ½ log(τ/2.2π). (iii) Edge values: 0.0782 (τ = 7714,
T = 3.5), 0.0631 (τ = 30775, T = 4.2). (iv) T = 3.75 has at least the value 0.10610 (τ = 14303.967), below every value of
§2.2: the true per-T minimum at T ≥ 3.75 is attained near r = 1.1, where the 4-prime alignment cells of §2.2 were not
the best ones (they were spread over the range).

## 4. Low-end windows r ∈ [1.1, 1.35] at T = 4.25 and T = 4.5 (half-width 0.2)

T = 4.25, range [33968.4, 41688.5], 6 of 8 h₄-cells finished (best h₄ in this window only 0.068):
μ_⅛ = **0.083603** (τ = 41081.58414, K = 13893, h₄ = 0.250), 0.094928 (40800.72353), 0.174814 (36974.53696),
0.185484 (35424.65030), 0.188410 (39531.35759), 0.191726 (39250.60356).
T = 4.5, range [56004.5, 68732.8], 10 of 12 h₄-cells finished, plus 2 cells of the full-range run (window 0.1):
μ_⅛ = **0.083178** (τ = 63751.81179, K = 22829, h₄ = 0.060, δ = 0.040), 0.086556 (60651.81934; h₄ = 0.162 at τ*,
the h₄-minimum 0.0126 at 60652.013 is 0.19 away), 0.096494 (58204.42048), 0.098087 (59102.16262, full-range run),
0.102032 (56654.61428), 0.105520 (61549.57052), 0.121910 (59754.25489), 0.126027 (63099.70834), 0.140287
(57552.11479), 0.157608 (60651.93548, full-range run, window 0.1), 0.178976 (65301.68139), 0.182776 (64649.50149).
μ_¼ at every minimiser within 2·10⁻⁵ of μ_⅛. Lanczos residuals ≤ 10⁻⁸.

## 5. Margin at the best cells vs T (step 2 of the task)

Values are minima over the cells examined, hence upper bounds for the true per-T minimum (not certified minima).

| T | best μ_⅛ found | τ* | r = τ*/2πN | source |
|---|---|---|---|---|
| 3.0 | 0.114017 | 2819.23599 | 1.11 | ROUND_017_B full scan |
| 3.25 | ≤ 0.134339 | 5228.68250 | 1.85 | ROUND_017_B partial |
| 3.5 | ≤ 0.078201 | 7713.88056 | 1.12 | ROUND_017_B partial; §2.1 alignment cells ≥ 0.154 |
| 3.75 | ≤ 0.106097 | 14303.96707 | 1.26 | §3 |
| 4.0 | ≤ 0.083881 | 30775.05123 | 1.64 | §3 |
| 4.1 | ≤ 0.071181 | 30775.05432 | 1.35 | §3 |
| 4.2 | ≤ 0.063116 | 30775.05574 | 1.10 | §3 |
| 4.25 | ≤ 0.083603 | 41081.58414 | 1.33 | §4 |
| 4.5 | ≤ 0.083178 | 63751.81179 | 1.25 | §4 |

No cell has margin < 0.02, so step (3) (direct W_T with tools/band_direct.py) was not triggered; ROUND_017_B already
showed W_T = μ to 10⁻⁶ at three such cells. **No negative value; no candidate.**

## 6. Depth law of alignment cells (step 4)

(i) Dependence on T at a fixed cell: μ_⅛(τ, T) decreases monotonically in T over the whole admissible window
r ∈ [1.1, 3] (13 tracked points, §3), roughly linearly in log r with cell-dependent slope: Δμ/Δlog r ≈ 0.24
(τ = 7714), 0.10 (τ = 14304), 0.08 (τ = 30775). The deepest value of a cell is at the low end r ≈ 1.1.
(ii) Dependence on the approximation quality: weak. Across all 51 alignment cells, the best simultaneous
approximations do not give the deepest margins: h₄ = 0.0071 → μ = 0.397 (T = 3.5, r = 2.4); h₄ = 0.018, δ = 0.023 →
μ_⅛ = 0.192, μ_¼ = 0.156 (T = 4.0, r = 1.39); h₄ = 0.0126 → 0.087 (T = 4.5); the deepest cells have δ ≈ 0.04–0.07
and r ≤ 1.35. Position in the range (r) dominates alignment quality as a predictor. The ROUND_017_B minimiser at
T = 3.5 is not a 4-prime alignment (p = 3 residue −0.23) and the T = 3.25 minimiser is anti-aligned; alignment is
neither necessary nor sufficient for depth.
(iii) Dependence of the per-T low-end minimum on T: values 0.114, 0.078, 0.106, 0.084, 0.063, 0.084, 0.083 over
T = 3 … 4.5 (upper bounds): a slow, non-monotone drift with no trend that can be extrapolated to a zero crossing from
these data; the smallest value found is 0.0631 (T = 4.2, τ = 30775.05574, r = 1.10).
(iv) η-dependence: μ_¼ ≤ μ_⅛ − 0.01 only at cells away from the low end (e.g. 0.150 vs 0.230 at T = 4, τ = 33874.8);
never below the per-T minimum.

## Result

PIVOT (counterexample watch, NUMERICAL): no negative and no sub-0.02 band margin at the small-prime alignment
cells for T = 3.5, 3.75, 4.0, 4.25, 4.5; smallest found 0.0631 (T = 4.2). Alignment of (τ log p) mod 2π, p ≤ 7, does not
locate the deepest cells; position r = τ/2πN near the low end 1.1 does.

## What was proved

Nothing new (computational memo). All values NUMERICAL, Lanczos residual ≤ 10⁻⁸; reproducibility: tools/align_band.py
(`OMP_NUM_THREADS=1 [ALIGN_WIN=0.2] python3 align_band.py T n_h4 n_g out.npy nproc [lo hi]`), tools/align21/track.py,
tools/align21/pol4.py; logs in tools/align21/*.log. Cross-check: μ_⅛(3.5, 7713.88056) = 0.078201 reproduced.

## What failed and why

The 4-prime alignment locator (h₄) and the flat-tone locator (g_T) both fail to locate the minima: at T = 3.5 all 30
cells of the full range are ≥ 0.154 while the non-aligned cell at r = 1.12 gives 0.078. The ±0.1 polish window was
too narrow at some cells (minimum 0.19 away from the h₄-point); §3–§4 use re-centred or 0.2 windows. Search coverage at
T ≥ 4 is a few dozen cells, so per-T values are upper bounds only.

## Next concrete step

Locator by position instead of alignment: full Lanczos scan of the low-end strip r ∈ [1.1, 1.3] (step 0.04, the
dips have width 0.1–0.2) at T = 4.0, 4.25, 4.5, plus tracking of each strip minimum across T, to decide whether the
low-end minimum drifts below 0.06.
