# `scripts/r8a` — round 8a of phase 155: the negative index `n₋(A_∞|P_T)`

Memo: `03-research/phase-155-row-d-flat-kernel-criterion/R155_052_ROUND8A_INDEX_MULTIBAND.md`.

| file | role |
|---|---|
| `r8a_lib.py` | interval (mpmath `iv`, `dps = 40`) primitives: closed-form `C₀`; enclosure of `m(τ)` from the `Σ s/(a_k(a_k²+s))` series with an integral tail; `sup m''` on a band; exact rational `β_k` and the Bessel moments `I_p^{(ij)}(c) = ∫₀^c xᵖ j_i j_j dx`; `g_l = ⟨cosh(t/2) or sinh(t/2), e_l⟩`; interval Cholesky (`cholesky_pd`) and congruence. No quadrature, no special-function library call enters a certified number. |
| `r8a_01_upper.py` | certified **upper** bound on `n₋(A_∞\|P_T^par)`: multi-band (piecewise-linear) minorant of `m`, bordered form, Haynsworth split at Legendre level `K`, multi-band Ky Fan ceiling `Λ_K(c_*)` for the tail, interval Cholesky certification. |
| `r8a_02_lower.py` | certified **lower** bound `n₋(A_∞\|P_T^par) ≥ 1`: explicit 2-dimensional negative-definite subspace of the bordered form, entries enclosed with `scripts/r4a/r4a_lib.py` (Paper 47 `thm:w11` machinery) with the prime atoms switched off and the pole term unused. |
| `r8a_03_recheck_lower.py` | independent re-check (0.1 s) of every `r8a_02` certificate from its archived JSON: rebuilds the 3×3 bordered matrix, inflates every entry by `±10⁻⁹` (covers double rounding of the stored ends and the float rounding of `F±h` in the polarisation, R155_052 Lemma 3.3), certifies by interval Cholesky, returns a certified margin, and re-imposes `T < 0.88137`. Output `r8a_03_recheck.json`. |
| `r8a_01_<T>_par<p>.json` | outputs of the upper-bound runs. `result.certified_upper_bound_sector = r` means `n₋(A_∞\|P_T^par) ≤ r` is certified. |
| `r8a_02_<T>_par<p>.json` | outputs of the lower-bound runs. `certified_lower_bound_sector = 1` means `n₋(A_∞\|P_T^par) ≥ 1` is certified. |

## Usage

```
python3 r8a_01_upper.py <T | log2 | halflog3> <par 0|1> [K=22 K2=36 c*=16.0 [grid=default|fine]]
python3 r8a_03_recheck_lower.py [inflate=1e-9]
python3 r8a_02_lower.py <T | log2 | halflog3> <par 0|1> [N=18 panels=3000]
```

## Measured runtimes (2026-09-22, from the `runtime_s` field of each JSON)

| run | runtime |
|---|---|
| `r8a_01` `0.58` par0 / par1 | 88.7 s / 87.6 s |
| `r8a_01` `0.80` par0 | 86.9 s |
| `r8a_01` `0.90` par0 / par1 | 87.5 s / 89.7 s |
| `r8a_01` `log2` par0 / par1 | 106.2 s / 21.5 s |
| `r8a_02` `0.60` par0 | 27.3 s |
| `r8a_02` `0.80` par0 | 27.4 s |
| `r8a_02` `0.81` par1 / `0.82` par1 | 27.8 s / 26.4 s |
| `r8a_02` `0.90` par1 | 27.4 s |
| `r8a_02` `log2` par0 | 55.4 s |

**Deviation from the phase's ≤ 60 s guideline.** Every `r8a_01` run except `log2 par1`
exceeds 60 s; the worst is `log2 par0` at 106 s. The `r8a_01` runs were launched
concurrently (file timestamps 15:32–15:35), so the ~87 s figures are contended wall
clock; the single uncontended run (`log2 par1`, 21.5 s) is the honest cost of the
linear-algebra stage. The dominant cost is `BesselMoments.moments(i,l)` over the
~198 same-parity pairs `(i<K, l<K2)` at the 28 band edges. Two cheap splits, neither
applied here: (i) cache the moment table to disk keyed by `(T, band grid, K2)` — it is
parity-independent only in its `(i,l)` recursion but the `par 0` and `par 1` tables are
disjoint, so the real saving is (ii) split the pair loop into two processes by `i`-block
and combine, which halves each run to ≈ 45 s. Nothing in the certified output depends on
the split.

## Note on the range of validity

`r8a_02` inherits from `r4a_lib` the affine sandwich of the kernel `K`, which needs
`1/(2cosh(u/2))` concave on `u ∈ [0,2T]`, i.e. `T < arccosh√2 = 0.88137`
(Paper 47 `thm:w11` proof (c)). **The run `r8a_02_0p90_par1.json` is outside that range
and is therefore NOT certified** — it is recorded as diagnostic only. `r8a_01` does not
use `r4a_lib` and has no such restriction (its only range condition is `T/2 < 1/2`,
asserted in `g_coeffs`).

## Changes of 2026-09-22 (evening, memo R155_052)

1. **Sign of the border coupling in the Schur bound (`r8a_01`).** The `Y`-column of `e_i` in the bordered
   form is `−P^⊥Me_i` and that of the border is `+P^⊥g`, so the Schur bound's `(e_i, ξ)` entry is
   `g_i + ⟨P^⊥Me_i, P^⊥g⟩/γ`. The archived runs computed `g_i − ⟨…⟩/γ`. Fixed in the script. The archived
   JSON are **not** regenerated: the difference is `≤ 2W‖P_K^⊥g‖/γ ≤ 1.4·10⁻³⁴` per entry for `T ≤ 0.9`
   (`‖P_{22}^⊥g‖ ≤ 9.3·10⁻³⁶`), against certified margins `≥ 0.0159`; R155_052 Lemma 2.4 turns this into a
   proof that every archived certificate stands.
2. **`m''` bound.** `r8a_lib.m2sup_band` sums `a(a²/2 − s)/(a²+s)³`, which is **not** the summand of `m''`
   (that is `a(a² − 3s)/(2(a²+s)³)`) but dominates it termwise for `s ≥ 0` and is itself
   decreasing-then-increasing in `s`, so the archived offsets are valid (conservative). Kept unchanged for the
   default grid; the new `m2sup_band_exact` uses the exact summand and is used only with `grid=fine`.
3. **Option `grid=fine`** (6th argument of `r8a_01_upper.py`): adaptive edges on `(0, 8]` with chord error
   `≈ 2·10⁻³` (step `min(0.2, √(8·2·10⁻³/|m''|))`, float, data only) plus 16 geometric edges on `[8.2, τ_N]`,
   77 bands in all; writes `r8a_01_<T>_par<p>_fine.json`. Non-default `K, K2, c*` add the suffix
   `_K<K>_K2<K2>_c<c*>`; a default run whose output already exists writes `_rerun.json`. No archived file is
   overwritten.

## New runs (2026-09-22 evening, one at a time, uncontended)

| run | runtime | result |
|---|---|---|
| `r8a_01 0.80 1 22 36 16.0 fine` → `r8a_01_0p80_par1_fine.json` | 47.3 s | `≤ 1` only; 2nd midpoint eigenvalue `−0.00433` (default grid `−0.00469`) |
| `r8a_01 0.80 1 30 44 24.0` → `r8a_01_0p80_par1_K30_K244_c24.json` | 18.1 s | `≤ 1` only; 2nd midpoint eigenvalue `−0.00189` (`τ_N = 30`) |
| `r8a_03` (all nine `r8a_02` JSON) → `r8a_03_recheck.json` | 0.1 s | certified `≥ 1` at `0.60/0.80/log2` par0, `0.81/0.82` par1; `0.90` par1 out of range; `0.75/0.78/0.80` par1 not certified |

The residual at `0.80` odd is insensitive to the band grid below `τ_N` and moves with `τ_N` (the constant
minorant `c_N` beyond `τ_N`): see R155_052 §5. Certifying `n₋ = 0` there needs `τ_N ≳ 60`
(`c* ≈ 48`, `K ≈ 60`, `K2 ≈ 75`, `IVDPS ≥ 70` because the alternating Bessel series loses `≈ 2c·log₁₀e`
digits), which is over the 60 s budget on this machine — **not attempted**.

## Measured runtimes: honest reading

The archived `r8a_01` figures of 87–106 s are **contended** wall clock (the runs were launched concurrently).
Uncontended: `17.8 s` (`0.80` par1, rerun), `21.5 s` (`log2` par1), `18.1 s` (`τ_N = 30`), `47.3 s` (`fine`).
Every run made uncontended is within 60 s.

## Audit re-runs (R155_061, 2026-09-22 23:03–23:05)

The corrected `r8a_01_upper.py` (border sign `+`) was re-run in the independent audit on the eight archived default
cases, strictly one at a time on an idle machine. Outputs `r8a_01_{0p58,log2,0p80,0p90}_par{0,1}_rerun.json`
(the script never overwrites an existing default output). Result: the same certified `r` and the same margins
`μ` as the archived JSON to every printed digit; runtimes 13.2–14.0 s each. **These `_rerun.json` files are the
certificates of record for the upper bounds.** `r8a_03_recheck_lower.py` was re-run (0.1 s); `r8a_03_recheck.json`
is identical to the previous one and is the certificate of record for the lower bounds — `r8a_02`'s own flag is not,
because under `r8a_02`'s import order (`r4a_lib`, then `r8a_lib`, which resets `mp.dps = 50`) the `C₀` guard in
`r4a_lib._constants` (`±1e-55` around a 60-digit print of a 169-bit `mp.euler`) can miss the true value by
`≈ 1e-51`; `r8a_03`'s `±1e-9` inflation absorbs it. See R155_061 (vi)–(viii).
