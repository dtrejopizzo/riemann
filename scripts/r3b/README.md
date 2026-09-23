# `scripts/r3b` — round 3B: rigorous enclosures of the test-kernel ceiling at the two-prime windows

Phase 155, round 3B (`03-research/phase-155-row-d-flat-kernel-criterion/R155_024_BUILDER_ROUND3B_TWOPRIME_ENCLOSURES.md`).
Orders: `R155_010 §5` and `R155_018 §4(iii),(iv)`.  Windows `T = 0.68` and `T = log 2`
(contact set `{2,3}`, `A_T = 2.24882634`).  **Nothing here touches Paper 47 or `scripts/r3a`.**

| file | what it is |
|---|---|
| `r3b_enclosure.py` | the enclosure: double-precision search for a test pair `(τ₀,q)`, then a rigorous `mpmath` interval bound `Ceil(M,T;β) ≤ a + b·β ≤ a + (\|b₀\|+\|b₁\|)·B` |
| `betabox.py` | Theorem B constants `r₀, V⋆, B = V⋆/r₀` at `T = 0.68` and `log 2` (calls `r2_c_beta_bound.run`) |
| `run_all.sh` | one separate single-process run per `(T,M)`; `./run_all.sh 7 9 11 …` |
| `explore.py`, `dbg.py` | double-precision exploration and the cross-check used to find the Gauss–Legendre weight bug (kept for the record) |
| `r3b_beta_box.json` | output of `betabox.py` |
| `r3b_enclosure_<T>_M<M>.json` | one enclosure: `τ₀`, `q`, the three interval integrals, the quadrature error bounds, the final `ceiling_upper_bound`, runtimes |
| `r3b_summary.json`, `r3b_summary.md` | the collected table of §2 of `R155_024` |

## Method (differences from `03-research/phase-155-.../scripts/r2_a_enclosure.py`)

Same mathematics: Theorem TK at a **single** pair `(τ₀,q)`, so that `c ≤ a + b₀β₀ + b₁β₁` for every
certificate of the lattice class of step `d = 2T/M`, every range, every atom count and every `β`;
then Theorem B's a priori box `‖β‖_∞ ≤ B` closes it `β`-uniformly.  Same interval ingredients:
`C₀ = ψ(1/4) − log π` from `iv.euler/iv.pi/iv.log`; `m` by `K = 100` terms of the `ψ`-series plus the
convex midpoint bracket of `R155_004` Lemma 2.2; `σ_T = m − v₂cos(τ log2) − v₃cos(τ log3)` (two
contacts, not one); `ĝ₀, ĝ₁` in closed form; `∫_W φ = P‖q‖²` exactly.

**Two changes.**

1. **Quadrature.** Composite Simpson with the crude fourth-derivative bound would need `~10⁵` nodes
   here (`|a| ~ 10⁻⁵…10⁻⁶` instead of `6·10⁻³`, and `P = πM/T ≈ 111` instead of `45.75`).  We use
   composite **Gauss–Legendre** of order `p` on `N = ⌈P/H⌉ panels`, with the classical remainder
   `|E_panel| ≤ H^{2p+1}(p!)⁴/((2p+1)((2p)!)³)·sup|f^{(2p)}|`, and `sup|f^{(2p)}|` from the same
   Leibniz/Bernstein bounds as `R155_004 §2.3(iii)` extended to order `2p`
   (`|m^{(j)}| ≤ 2^{-j}j!ζ(j+1,1/4)`, `|ĝ₀^{(j)}| ≤ 2cosh T(2T)^{j+1}/(j+1)`,
   `|ĝ₁^{(j)}| ≤ 2 sinh T(2T)^{j+2}/(j+2)`, `|φ^{(j)}| ≤ (d(M−1))^j(Σ|q_k|)²`), and with
   `|m| ≤ max(|C₀|, m(τ_max))` for `j = 0` (`m` even and increasing in `|τ|`), the second entry itself
   enclosed by the interval `m`.  Defaults `p = 6`, `H = 0.2`: `≈ 3300` nodes, `err ≈ 10⁻⁸` on the
   `σ`-integral and `≈ 10⁻¹⁶` on the two `ĝ`-integrals.
   Nodes/weights are Newton-refined at `mp.dps = 60` from the double-precision `leggauss` seeds and
   widened by `10⁻⁴⁵` before entering interval arithmetic; the JSON field `gl_residual` is
   `max(max_i|P_p(x_i)|, |Σ_i w_i − 2|)` and is `< 10⁻⁶⁰` in every run.
   *(A first version computed the nodes with `mpmath.findroot` from Chebyshev seeds; two seeds
   converged to the same root, `Σw_i = 2.189`, and the rule was silently wrong by `~6·10⁻⁶` in the
   integral.  The `Σw_i = 2` check now guards it; `dbg.py` is the cross-check that caught it.)*
2. **Choice of `q`.** `r2_a_enclosure.py` used the bottom eigenvector of `C(β⋆)`.  Here `|a|` is
   `10²–10³` times smaller while `B ≈ 1.9·10⁴`, so the term `(|b₀|+|b₁|)B` must be pushed below
   `|a|`.  We minimise `a + B(|b₀|+|b₁|)` over the span of the three lowest eigenvectors of `C(β⋆)`
   (10 Nelder–Mead starts).  When the minimax over `(τ₀,β)` has a single active `τ₀`, strong duality
   makes `b = 0` attainable, and the optimiser reaches `|b| ~ 10⁻¹⁶`; when two `τ₀` are active it does
   not, and the run fails (the enclosure is then positive and is reported as **not closed**).
   The three Toeplitz families are recomputed at the selected `τ₀` with `n = 2²⁰` Simpson nodes,
   because the `n = 2¹⁶` families of `tk_common` carry `~10⁻⁸` error in the `ĝ` coefficients — larger
   than the `|b|` we are trying to reach.

Provenance of `(τ₀,q)` is irrelevant to the proof: **any** pair gives a valid upper bound.

## Reproduce

```
python3 betabox.py                                  # Theorem B constants, ~40 s
python3 r3b_enclosure.py 0.68 24 121 6 0.2          # one enclosure, ~50 s
./run_all.sh 24 20 16                               # a batch, one process each
```

Runtimes are in each JSON (`sec_double`, `sec_quad`, `sec_total`); every single run is `< 60 s`
single-process with `OMP_NUM_THREADS=1`.
