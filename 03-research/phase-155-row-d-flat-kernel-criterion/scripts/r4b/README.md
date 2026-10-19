# `scripts/r4b/` — phase 155, round 4b (Problem A on the archimedean form; the negative index)

Support for `03-research/phase-155-row-d-flat-kernel-criterion/R155_033_ROUND4B_PROBLEM_A_ARCH.md`.
**Everything here is double precision and therefore `DIAGNOSTIC`.** No interval arithmetic, no LP, no
sweep. Total runtime `< 3 min` on one core. Nothing in `scripts/r4a/` is touched.

| file | what it computes | runtime |
|---|---|---|
| `r4b_01_ceil_inf.py` | `Ceil_∞(M,T) = sup_β inf_{τ₀} λ_min(C_M(τ₀,β))` for the **archimedean** symbol `S_β = m + β₀ĝ₀ + β₁ĝ₁` (Paper 47 `prop:TK` with the prime comb deleted), `M = 8,12,16,24,32,48,64` at `T = ½log3, log2`. Simpson on one period (`n = 2¹⁵`) → one FFT per `(τ₀, family)`; `τ₀`-grid of 33 points on `[−P,0]`; coarse grid + Nelder–Mead on the concave `β`-objective. Writes `r4b_01.json`. | ≈ 4 min (measured by the audit R155_037; the earlier 60 s figure was wrong) |
| `r4b_02_negcount.py` | the explicit negative-index bound of Proposition NC: `θ(τ₁) = m(τ₁)/(m(τ₁)−C₀)`, the `PROVED` trace/Markov bound `⌊2Tτ₁/(πθ)⌋` minimised over `τ₁ > τ₀`, and the sharper `DIAGNOSTIC` count `#{n : λ_n(S_{T,τ₁}) > θ(τ₁)}` from a Gauss–Legendre Nyström discretisation (`N = 500`) of the sinc kernel, at `T = ½log3, log2, 0.80`. | ≈ 90 s |

Both reuse `03-research/phase-155-row-d-flat-kernel-criterion/scripts/tk_common.py`
(`m_arch`, `make_S_parts`) via a `sys.path` insert; `tk_common.py` itself is unmodified.

Headline outputs (see `R155_033 §2.5`, `§3.3`):
`λ^{∞,P}_min − Ceil_∞(M,T) ≈ 0.28·M^{−1.17}`, essentially independent of `T` for `M ≥ 24`;
`n₋(A_∞|P_T) ≤ 37/47/54` (`PROVED`, trace) and `≤ 4/5/5` (`DIAGNOSTIC`, prolate) at
`T = ½log3, log2, 0.80`, against a computed `n₋ = 0/1/1`.
