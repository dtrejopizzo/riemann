# `scripts/r3c/` — Schur reduction at the archimedean ground state (phase 155, round 3c, `R155_026`)

Splits `W_T = A_∞ + Π_T` on the primitive subspace `P_T` at the ground state `F*` of the
**archimedean** form `A_∞|P_T` (so `F*` is prime-independent), and encloses `w₁₁ = W_T(F*)`
rigorously at `T = log 2`. Reuses `scripts/r3a/arch_core.py` **unmodified** (imported by path);
no file in `scripts/r3a` or `scripts/r3b` is touched.

| file | what it does | runtime |
|---|---|---|
| `r3c_01_schur.py` | `N = 18` and `N = 36`, `T ∈ {0.58, 0.62, 0.65, log 2}`: `λ₁, λ₂` of `A_∞\|P_T`, `w₁₁`, cross term `c = ‖P_V W F*‖`, `‖Π_T\|_V‖`, the crude sufficient condition, `λ_min(S)` vs `λ_min(W_T\|P_T)` (sign-consistency test), overlaps of the `S` ground state with the archimedean eigenvectors → `r3c_01.json` | **99 s** (`N = 18` half: 15 s; `N = 36` half: 84 s — the only run above the 60 s guideline) |
| `r3c_02_enclosure.py` | **rigorous** two-sided enclosure of `w₁₁` at `T = log 2` for the explicit `N = 18` Galerkin `F*` (coefficients archived in `r3c_02.json`): exact polynomial autocorrelation `c(u)` (Chebyshev, residual `2.5e−15`), `sup\|g'\| ≤ Σ\|cheb coeffs\|`, `K` decreasing, `K ≤ 1/u + 1/2` at the singular end, `3·10⁶` geometric panels, exact prime atoms, pole defect paid for → `r3c_02.json` | **9.5 s** |
| `r3c_03_parity.py` | parity of `F*` and of the archimedean eigenvectors at `log 2`; decoupling of the odd sector (`\|W(F*, odd)\| ≤ 1.3e−15`); parity of the `S` ground state → `r3c_03.json` | 7 s |
| `r3c_04_even_ladder.py` | the coupled (same-parity) archimedean level `λ₃`, `c²/w₁₁`, `‖Π_T\|_even‖` and the even-sector crude condition at the four windows → `r3c_04.json` | 23 s |

`r3c_01`, `r3c_03`, `r3c_04` are `DIAGNOSTIC` (double precision, Galerkin; Galerkin eigenvalues are
**upper** bounds on the true infima). `r3c_02` is the only rigorous computation: two-sided bounds at
every step, with a uniform rounding slack `ε = 1e−9` (four orders above the observed interpolation
residual) subtracted from the lower and added to the upper bound. Result:
`w₁₁ ∈ [0.0341712660, 0.0342537492]`. It certifies **one direction**, not the form.

Reproduce: `python3 r3c_01_schur.py` (or comment out the `N = 36` row to stay under 60 s);
`python3 r3c_02_enclosure.py`; `python3 r3c_03_parity.py`; `python3 r3c_04_even_ladder.py`.
Total ≈ 2 min 20 s in a single process.

## `r3c_04_enclosure_iv.py`  **[2026-09-22, per `R155_028 §2`]**

The **hardened** enclosure that now supports Theorem 3c.3 of `R155_026 §4`. It supersedes
`r3c_02_enclosure.py`, which is kept only as an archived cross-check.

* It **loads** the coefficient vector of `F*` from `r3c_02.json` (`arch_core` is not imported and
  nothing is recomputed); the decimals are read exactly.
* Every step is `mpmath` interval arithmetic (`mp.iv`, `dps = 60`) or a closed-form inequality:
  the autocorrelation `c` is built as an **exact** polynomial of degree `≤ 35` by rational/interval
  algebra (Legendre recurrence with `Fraction`s, binomial expansions, term-by-term integration);
  `sup|G'| ≤ 4.7518` from the exact Chebyshev expansion; the body integral from an **affine
  sandwich** of `K` (convexity of `1/(2 sinh)`, concavity of `1/(2 cosh)` on `u < 1.7627`) against
  `g ≥ 0`, with `∫G` and `∫sG` exact on each panel; the singular end by `G(s) ≤ G₁ s`,
  `K ≤ 1/u + 1/2`, `δ = 10⁻⁶`; `C₀`, the tail `∫_{2T}^∞K`, the atoms `v_2 c(log2)`, `v_3 c(log3)`
  and the pole defect `2|A||B|` all in intervals.
* **The `EPS = 1e−9` budget is gone.**

Output (`M = 8000` panels, `18.2 s`): `W_{log2}[F*] ∈ [0.0342113430, 0.0342182500]`, width
`6.91·10⁻⁶`, contained in and `12×` narrower than the archived float interval
`[0.0341712660, 0.0342537492]`. Panel count is settable with `R3C_PANELS` (`M = 2000` gives width
`3.9·10⁻⁵` in `6.1 s`). Result archived in `r3c_04_enclosure_iv.json`.
