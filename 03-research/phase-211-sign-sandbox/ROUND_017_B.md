# Round 017 B — Full-range band margins at T = 2.5–4 by a matrix-free closed form, and direct W_T on the extremal packets

Notation of ROUND_016_A: N = e^{2T}, v_n = 2Λ(n)/√n, ℓ_n = log n < 2T, m(t) = Re ψ(¼ + it/2) − log π,
Ω_lo = 2πN·1.1, a_k = kπ/2T, e_k = sin(a_k(x + T))/√T, K = ⌊2Tητ/π⌋, A_τ^{(η)} the compression of A_τ to span{e_1..e_K};
margin μ_η(τ) = m(τ) − λ_max(A_τ^{(η)}). By Theorem 1.1 of ROUND_016_A, for β the top eigenvector and f = β cos τx,
Q_T(f)/‖f‖² = μ_η(τ) + (D + X − R)/‖β‖² up to ‖f‖² = ½‖β‖²(1 + O(τ^{−1})) (ROUND_016_A §2.3 normalisation).

## 0. Corpus check

Index rows read: P211-15C, P211-16A. Same object (A_τ^{(η)}, the packet identity), no new route: this memo is the
numerical completion requested in P211-16A "Next concrete step (ii)" (full τ-ranges, T ≥ 3, direct W_T). No index row is
retried.

## 1. A closed form for A_τ^{(η)} that makes it matrix-free (PROVED)

**Proposition 1.1.** Let σ_k(ℓ) = sin(a_kℓ), ε_k = (−1)^k, 0 < ℓ < 2T. In the basis e_1, e_2, …,
  2T⟨e_j, Sh(ℓ)e_k⟩ = (σ_k − ε_jε_kσ_j)/(a_j − a_k)·[j ≠ k] + (σ_k + ε_jε_kσ_j)/(a_j + a_k) + δ_jk(2T − ℓ)cos(a_kℓ).
Consequently, with c_n = v_n cos(τℓ_n), s_k = Σ_n c_n sin(a_kℓ_n), d_k = Σ_n c_n(2T − ℓ_n)cos(a_kℓ_n),
C_jk = (a_j − a_k)^{−1}[j ≠ k] (Toeplitz), H_jk = (a_j + a_k)^{−1} (Hankel), S = diag(s), E = diag(ε), Dd = diag(d):
  A_τ^{(η)} = ½(𝔈 + 𝔈ᵀ),  2T·𝔈 = C S − E S C E + E S H E + H S + Dd   (all restricted to k ≤ K).
*Proof.* In the closed form of tools/A_tau_lmax.py, for s = ℓ > 0 one has L = −T, U = T − ℓ, and with c₁ = a_j − a_k,
d₁ = c₁T − a_kℓ: c₁U + d₁ = (j − k)π − a_jℓ, c₁L + d₁ = −a_kℓ, so I₁ = (−(−1)^{j−k}σ_j + σ_k)/c₁ (j ≠ k) and
I₁ = (2T − ℓ)cos(a_kℓ) (j = k); with c₂ = a_j + a_k, d₂ = c₂T + a_kℓ: c₂U + d₂ = (j + k)π − a_jℓ, c₂L + d₂ = a_kℓ, so
−I₂ = ((−1)^{j+k}σ_j + σ_k)/c₂ (sin(pπ − y) = −(−1)^p sin y). Sh(−ℓ) = Sh(ℓ)*, hence Sh(ℓ) + Sh(−ℓ) has matrix 𝔈_ℓ + 𝔈_ℓᵀ.
Summing over n, the n-dependence enters only through the vectors s, d (the matrices C, H, E do not depend on n). ∎
The comb therefore acts on the band only through the two Dirichlet-polynomial vectors s_k, d_k (frequencies τ ± a_k);
C and H are applied by FFT, so one matvec costs O(K log K) after O(K·#{n}) for s, d. Checked against the dense
matrix of tools/A_tau_lmax.py: max entry difference 4·10⁻¹⁵ (T = 1.5, K = 16); top eigenvalues agree to 10⁻¹⁵ and
reproduce ROUND_016_A (0.91541 at (1.5, 140.42, ⅛), 0.27488 at (2, 416.86, ¼), 0.11408/0.11390 at (3, Ω_lo + 30.94, ⅛/¼)).
Tools: tools/band_lanczos.py (operator + Lanczos, `eigsh`, tol 10⁻¹⁰, residual ‖Aβ − λβ‖ recorded at every point),
tools/band_scan.py (parallel scan, warm starts), tools/band_direct.py (direct a_T, W_T; §3).

**Lanczos reliability (a failure found and repaired).** With a pure warm start (previous τ's eigenvector as v0),
`eigsh` locked onto a non-top eigenvector at 2 629 of 44 295 points of the T = 2.5 scan (detected because a dense
96 × 96 leading block gave a *larger* eigenvalue, impossible by Rayleigh–Ritz nesting; dense eigvalsh of the full
K × K matrix confirmed the cold-start value, e.g. τ = 1977.12: warm 1.3194, true 0.9647). The defect only *raised*
margins, so it could hide a minimum. Repair: v0 = previous vector + equal-norm random vector. Rerun: 0 violations of
nesting (min of screen − full = +6·10⁻⁶), Lanczos residual ‖Aβ − λβ‖ ≤ 6·10⁻⁹ at every point of every scan below.

## 2. Full-range band margins (NUMERICAL)

Range: [Ω_lo, 3·2πN] = [1.1, 3]·2πN (ROUND_016_A used [Ω_lo, 3Ω_lo] for T ≤ 2 and partial windows at T ≥ 2.5).
Step: 0.04 at T = 2.5; the T = 2.5 data subsampled at step 0.08 reproduce the minimum exactly, at step 0.2 miss it by
0.013, at step 0.4 by 0.037 (dips have width ≈ 0.1–0.2 in τ); hence step 0.08 at T ≥ 3, followed by a fine rescan
(step 0.005) around the ten lowest local minima.

### 2.1 T = 2.5, η = ⅛ (44 295 points, step 0.04, full range)
min μ = **0.256614** at τ = 1268.798 (τ − Ω_lo = 243.04, K = 252) — the ROUND_016_A partial-range value was the true
minimum. Next local minima: 0.256913 (τ = 1223.60), 0.267991 (τ = 2633.48, far end), 0.281307 (2447.72),
0.285197 (1178.36). The far-end dips (τ ≈ 2.6Ω_lo) are within 0.012 of the minimum: the margin does not grow
appreciably across [1.1, 3]·2πN (m grows by log(3/1.1) = 1.0 there, the peaks of λ_max grow with K).

### 2.2 T = 3, η = ⅛, first part [1.1, 1.8]·2πN (22 181 points, step 0.08)
min μ = **0.116502** at τ = 2819.260 (τ − Ω_lo = 30.96, K = 673); next 0.135053 (τ = 3825.74), 0.168483 (3517.50),
0.175181 (2959.58).

### 2.3 T = 3, η = ⅛, full range [1.1, 3]·2πN (60 203 points, step 0.08)
Second part [1.8, 3]·2πN: min 0.260744 (τ = 5266.75). Whole range: min on the grid 0.116502 at τ = 2819.26; Brent polish
(rescan step 0.01 on ±0.08 around each of the 40 lowest grid minima, then bounded Brent, xatol 10⁻⁶; largest
polish gain 0.011, the 40 cells cover all grid minima up to 0.285): **min μ_⅛ = 0.114017 at τ = 2819.23599** (K = 673, residual 6·10⁻¹³); η = ¼ at the same τ:
**0.113840** (K = 1346). Second-deepest cell: 0.133560 (τ = 3825.72481), η = ¼: 0.133391. Ten lowest grid minima:
0.1165, 0.1351, 0.1685, 0.1752, 0.1882, 0.1988, 0.2038, 0.2101, 0.2108, 0.2113 — all in [1.1, 1.6]·2πN. The
ROUND_016_A partial-range value at T = 3 was the true full-range minimum.

**Shape of the extremal envelopes.** At the three deepest cells (T = 2.5: τ = 1268.80; T = 3: τ = 2819.24, 3825.72)
the top eigenvector carries 91%, 98%, 96% of its mass on e_1 (half-sine envelope), the rest on e_3, e_5, …
(odd modes only: an even, flattened envelope). The single mode e_1 is *not* enough: m − ⟨A e_1, e_1⟩ = 0.939 at
(2.5, 1268.80) against μ = 0.256 — the small odd tail (amplitudes 0.21, 0.12 on e_3, e_5) lowers the margin by 0.68.
Other cells (e.g. T = 2.5, τ = 2633.48, μ = 0.268) have envelopes concentrated on a cluster of adjacent modes
k ≈ 294–296 (a modulated envelope, frequency a_k ≈ 186).

**Screens that were tried and do not locate the minima** (recorded so that they are not reused as a shortcut):
(i) flat-window tone function g_T(ω) = m(ω) − Σ v_n(1 − ℓ_n/2T)cos(ωℓ_n) (tools/tone_scan.py): min g = 0.439, 0.471,
0.345, 0.379, 0.399 at T = 2.5, 3, 3.25, 3.5, 4 — it lies 0.18–0.52 *above* the band margin at the same τ and its minima
do not predict the band minima (at T = 3 the band minimum τ = 2819.24 has g = 0.633; the candidate set needed to cover all
band minima within 0.1 grows to 2 820 τ-cells, more than the full scan); (ii) the dense leading block k ≤ 96: within
0.005 of μ at the k ≈ 1 cells, but 0.3–0.9 above it at the modulated-envelope cells; (iii) the diagonal max_k A_kk
(tools/diag_scan.py, exact via Proposition 1.1): 0.3–0.7 above μ everywhere. All three are Rayleigh upper bounds for μ
(valid, but not tight); none replaces the full scan. Consequence: at T ≥ 3.25 the full Lanczos scan is the only reliable
locator, and its cost limits the τ-range covered (§2.4).

### 2.4 T = 3.25, η = ⅛, partial range [1.1, 1.6]·2πN (26 121 points, step 0.08, then 40 cells polished)
Grid min 0.159717 (τ = 4618.65). After polishing the 40 lowest cells (all grid minima ≤ 0.251): **min μ_⅛ = 0.134339 at
τ = 5228.68250** (K = 1352, residual 8.5·10⁻¹¹; η = ¼: **0.134214**, K = 2704), a cell the step-0.08 grid had at 0.1731
(polish gain 0.0388: at T = 3.25 the dips are narrower than at T = 3; largest gain at T = 3 was 0.011). Next cells:
0.156949 (τ = 4618.62976; η = ¼ 0.156941), 0.167526 (5266.76), 0.168479 (4872.46; η = ¼ 0.168438), 0.174700 (4759.10).
Envelope at the minimiser: 98% on e_3 (odd tail on e_1, e_5); at τ = 4618.63: e_291, e_289 (87%, 12%: modulated).
Not covered: [1.6, 3]·2πN. Status: upper bound for the full-range minimum; positive on the covered range.

### 2.5 T = 3.5, η = ⅛, partial range [1.1, 1.2]·2πN (8 614 points, step 0.08, then 40 cells polished)
Grid min 0.082089 (τ = 7713.86). After polishing the 40 lowest cells (grid minima ≤ 0.257; largest gain 0.023):
**min μ_⅛ = 0.078201 at τ = 7713.88056** (K = 2148, residual 2.5·10⁻⁹); **η = ¼: 0.078088** (K = 4296, residual
6.8·10⁻¹¹). Envelope: 93% on e_1 (odd tail e_3, e_7). Next cells: 0.132791 (τ = 8180.49), 0.138820 (7786.31), 0.151023
(7854.60). The minimiser is isolated: the next cell is 0.055 higher. Not covered: [1.2, 3]·2πN.
Remark (NUMERICAL): τ = 7713.86 is also the second-lowest local minimum of the flat-tone function g at T = 3.25
(g = 0.4043 at ω = 7713.862) — an arithmetic alignment point of the small-prime phases (τ log p mod 2π) that is not
tied to T; at T = 3.5 it lies inside the high range and gives the deepest cell found.

### 2.6 T = 4, η = ⅛, partial range [1.1, 1.1126]·2πN (2 947 points, step 0.08, then 20 cells polished)
(The scan was stopped by the 20-minute limit; incremental saving kept the contiguous first 236 units of τ.)
**min μ_⅛ = 0.134069 at τ = 20812.04990** (K = 6624, residual 2.7·10⁻¹⁰); **η = ¼: 0.134038** (K = 13249, residual
9.9·10⁻¹⁰). Next cells 0.139178 (20608.87), 0.139675 (20640.37), 0.139681 (20763.11). Not covered: [1.1126, 3]·2πN.

### 2.7 Summary and trend

| T | range covered (×2πN) | points | min μ_⅛ (τ) | μ_¼ at the same τ | status |
|---|---|---|---|---|---|
| 2.5 | [1.1, 3] full | 44 295 | 0.256614 (1268.80; polished 0.25634) | 0.255029 | full range |
| 3.0 | [1.1, 3] full | 60 203 | 0.114017 (2819.23601) | 0.113840 | full range |
| 3.25 | [1.1, 1.6] | 26 121 | 0.134339 (5228.68250) | 0.134214 | upper bound |
| 3.5 | [1.1, 1.2] | 8 614 | **0.078201** (7713.88056) | **0.078088** | upper bound |
| 4.0 | [1.1, 1.1126] | 2 947 | 0.134069 (20812.04990) | 0.134038 | upper bound |

(i) **No negative band margin was found**, at any T, τ or η. The smallest value is 0.0781 (T = 3.5, η = ¼).
(ii) The trend is not linear in T: 0.257, 0.114, ≤ 0.134, ≤ 0.078, ≤ 0.134. The extrapolated zero near T ≈ 3.3
(ROUND_016_A) does not occur: at T = 3.25 the covered minimum is 0.134 and at T = 3.5 it is 0.078. The minimum
at each T is set by an isolated cell (the next cell is 0.02–0.055 higher), so the sequence reflects where good phase
alignments of the small primes fall inside the high range, not a smooth decline in T.
(iii) η-dependence at the minimisers: |μ_¼ − μ_⅛| ≤ 1.3·10⁻³ for T ≥ 2.5 (≤ 1.6·10⁻⁴ for T ≥ 3).
(iv) Convergence: Lanczos residual ≤ 7.6·10⁻⁹ at every scanned point; the operator is exact (Proposition 1.1;
no basis truncation inside V_η); grid → polish gains ≤ 0.039 (largest at T = 3.25), and every cell polished down to
grid value ≥ 0.22; the T = 2.5 grid at step 0.04 and its 0.08 subsample give the same minimum.
(v) The "trivial cap" (margin automatically positive once m(τ) ≥ Σ v_n) is useless as a range bound: Σ v_n = 75.2
at T = 3 would need log(τ/2π) ≳ 75. The ranges above are the high range [Ω_lo, 3·2πN] used in all earlier rounds;
beyond 3·2πN nothing was scanned. The margin does *not* grow appreciably across [1.1, 3]·2πN (T = 2.5: the 3rd
deepest cell sits at 2.8·2πN; T = 3: second part min 0.261), so the restriction to 3·2πN is a real gap in coverage.

## 3. Direct evaluation at the T = 3 minimiser (NUMERICAL)

tools/band_direct.py: β evaluated exactly on the grid (DST-I/DCT-I of the coefficients; ‖β‖² by trapezoid = 1 to 10⁻¹⁶),
comb by exact shifted samples (no interpolation in ℓ), archimedean part by FFT and, independently, by the Lévy form
a(f) = m(0)‖f‖² + ∫_0^∞ 2e^{−u/2}(‖f‖² − c_f(u))/(1 − e^{−2u}) du (c_f by exact discrete correlation, trapezoid in u,
analytic tail beyond 2T). (T, τ, η) = (3, 2819.23599, ⅛), K = 673:

| M (grid) | Q_T(f)/‖f‖² FFT | Lévy | W_T(P_Tf)/‖·‖² FFT | Lévy | D + X | −R | ‖P_Tf − f‖²/‖f‖² |
|---|---|---|---|---|---|---|---|
| 2^17 | 0.1140164 | 0.1133224 | 0.1140164 | 0.1133224 | −1.1·10⁻⁶ | +8.5·10⁻⁷ | 4.9·10⁻¹¹ |
| 2^18 | 0.1140164 | 0.1138429 | 0.1140164 | 0.1138429 | −1.1·10⁻⁶ | +8.4·10⁻⁷ | 4.9·10⁻¹¹ |
| 2^19 | 0.1140164 | 0.1139730 | 0.1140164 | 0.1139730 | −1.1·10⁻⁶ | +8.4·10⁻⁷ | 4.9·10⁻¹¹ |

The Lévy value converges at rate h² (differences to FFT 6.9·10⁻⁴, 1.7·10⁻⁴, 4.3·10⁻⁵); Richardson extrapolation gives
0.1140164 ± 10⁻⁶, equal to the FFT value, which is M-stable to 7 digits. μ_⅛ = 0.1140167. So **W_T = 0.11402 > 0**
with D + X − R = −2·10⁻⁶: the packet identity is exact to 10⁻⁶ here (ROUND_016_A's −R = −0.0018 at this cell was the
interpolation error of the comb quadrature, not a property of the packet).
(T, τ, η) = (3.25, 5228.68250, ⅛), K = 1352: W_T FFT 0.1343392 (M = 2^18 and 2^19 identical), Lévy 0.1336387 / 0.1341641,
Richardson 0.1343392; D + X = −5·10⁻⁷, −R = +5·10⁻⁷, projection loss 1.6·10⁻¹¹; μ_⅛ = 0.1343392.
(T, τ, η) = (3.5, 7713.88056, ⅛), K = 2148: W_T FFT 0.07820184 / 0.07820182 (2^18 / 2^19), Lévy 0.07643334 / 0.07775981,
Richardson 0.0782020; D + X = −4·10⁻⁷, −R = +1.2·10⁻⁶, projection loss 9.3·10⁻¹²; μ_⅛ = 0.078201.
In every case the two archimedean quadratures agree after extrapolation to ≤ 2·10⁻⁶, the packet identity holds to
≤ 2·10⁻⁶ (|D + X − R|), and the direct value W_T(P_Tf)/‖P_Tf‖² equals the band margin to 10⁻⁶. **No negative value.**
(T, τ, η) = (4, 20812.04990, ⅛), K = 6624: W_T FFT 0.1315097 (2^18 and 2^19 identical), Lévy 0.1145572 / 0.1272826,
Richardson 0.131524 (agreement 1.5·10⁻⁵; Lévy still in its h² regime); D + X = −2.56·10⁻³, −R = −2.7·10⁻⁷,
projection loss 8·10⁻¹³; μ_⅛ = 0.134069, so W_T = μ + (D + X − R) = 0.13151 > 0. Here the curvature term D is the
visible error (the envelope carries higher modes), as Proposition 1.4 of ROUND_016_A predicts; it lowers the true
value below the band margin by 0.0026.

**True margins (direct W_T(P_Tf)/‖P_Tf‖² on the extremal packets).** 0.11402 (T = 3), 0.13434 (T = 3.25),
0.07820 (T = 3.5), 0.13151 (T = 4). No cell with margin < 0.05 was found, so step (2)'s threshold was never reached;
the four minimisers were checked directly anyway. Nothing was certified: these are floating-point values with the
quadrature-error estimates stated, not interval enclosures.

## Falsifier note

No sign step is made; this is a measurement of (HB_η)'s left side. Proposition 1.1 is a structural identity valid for
any real weights v_n (hence for (a) cΛ, (b) a_P, (c) Beurling systems, (d) finite modifications) and it must be,
being an identity. The measured margins are what distinguishes the true comb: with λ_max(A_τ^{(η)}) = 7.0347 and
m = 7.1129 at the T = 3.5 minimiser, c·Λ fails (HB_η) at that single cell for c > m/λ_max = 1.0111 — the cΛ budget
c*(T) keeps shrinking (1.07 at T = 2, ≤ 1.022 at T = 3, ≤ 1.011 at T = 3.5). (b)–(d) not run.

## Result

NUMERICAL (no candidate). PROVED piece: the closed form of A_τ^{(η)} (Proposition 1.1) — the comb enters the band only
through two Dirichlet-polynomial vectors s_k, d_k, and A_τ^{(η)} = ½(𝔈 + 𝔈ᵀ) with Toeplitz/Hankel Cauchy kernels.
NUMERICAL: full-range band margin at T = 2.5 (0.2566) and T = 3 (0.1140); partial ranges at T = 3.25 (≤ 0.1343),
3.5 (≤ 0.0782), 4 (≤ 0.1341); all positive, η-insensitive; direct W_T on the four extremal packets equals the margin up
to |D + X − R| ≤ 2.6·10⁻³ (≤ 2·10⁻⁶ for T ≤ 3.5) with two independent archimedean quadratures; no negative value.

## What was proved

Proposition 1.1 (closed form of the shift matrix in the sine basis and of A_τ^{(η)} as a structured Toeplitz/Hankel
operator; checked against the dense matrix to 4·10⁻¹⁵).

## What failed and why

(1) Warm-started Lanczos misconverged at 6% of points (fixed; detected by Rayleigh–Ritz nesting). (2) Three cheap
screens (flat-tone g_T, leading dense block, diagonal) are valid upper bounds but are 0.2–0.9 above the margin at many
cells; none locates the minima, so T ≥ 3.25 could only be scanned on partial ranges within the time limit.
(3) The zero crossing predicted by linear extrapolation (T ≈ 3.3) did not appear; the minimum is governed by isolated
alignment cells and is not monotone in T.

## Next concrete step

(i) Cover [1.2, 3]·2πN at T = 3.5 and [1.11, 3]·2πN at T = 4 (≈ 2·10⁵ and 4·10⁵ Lanczos points at step 0.08:
off-machine or a block-Lanczos batch over τ); (ii) a locator for alignment cells from the phases (τ log p mod 2π,
p ≤ 13) to replace the scan; (iii) certify the T = 3.5 cell (τ = 7713.88056, μ = 0.0782) with interval arithmetic
only if a smaller cell is found — at 0.078 it is a positive value with error ≤ 10⁻⁵, not a candidate.

Reproducibility: tools/band_lanczos.py, band_scan.py (T η τ_lo τ_hi step out.npz [nproc]), band_direct.py (T τ η M),
tone_scan.py, band_screen.py, diag_scan.py; Ω_lo = 2π e^{2T}·1.1, v_n = 2Λ(n)/√n over prime powers n < e^{2T}.

