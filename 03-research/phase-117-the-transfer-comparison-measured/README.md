# Phase 117 — the transfer comparison, measured

Date: 2026-08-17.

Phase 116 left row (d) resting on two inputs, of which the second —
the comparison carrying the Gamma–Tate *source model* to the *exact* threshold
condition — had never been addressed anywhere in the corpus. Two external
audits of `main.tex` flagged that gap; phase 116 established that the
machinery around it (balanced factorization, exact step, output-defect
reduction) was already proved in phase 114 and merely untransferred, leaving
the comparison itself as the one genuinely open item.

**This phase measures it. The answer is negative.**

## Result

| quantity | measured | meaning |
|---|---|---|
| **`c_N`** (transfer comparison) | **`< 1` at every threshold `3 ≤ N ≤ 37`**; `0.58` at `N=4` down to `0.09` at `N=29`; decays like `(log N)^-0.6`; decreases monotonically under refinement | The source route **does not reach** the exact target. `Corollary (conditional completion of row d)` does not apply. |
| unit source estimate `ℰ_{ΓT,N} ≥ ‖L_N‖²` | holds, `λ_min ≈ 3.6–4.9` (i.e. a ~4× margin, not 1×) | The conjecture's own content is fine. |
| physical Schur target `S_E − Z_E*Z_E − b_E*A_0†b_E` | `λ_min ∈ [0.012, 0.075] > 0` at every threshold tested | **The exact condition itself appears true.** |
| `ρ_N ≤ 1/(20 log N)` | **FALSE** — violated at `N = 20, 40, 80, 120` | See below. |

**The directions are what make these conclusive, not merely indicative:**

- `c_N` is a **minimum** over the corona, so a Galerkin restriction returns an
  **upper** bound. Measured `c_N < 1` ⟹ true `c_N < 1`.
- `ρ_N` is a **supremum** over cell profiles, so Galerkin returns a **lower**
  bound. Measured `ρ_N > 1/(20 log N)` ⟹ the bound is genuinely false.

Both findings therefore survive refinement by construction.

## The falsified bound

`1/(20 log N)` was recorded in `CANDIDATE_LOG_SCHUR_THEOREM.md` and carried
into the paper. It is contradicted **by the paper's own audit table**:

| N | paper's ρ_N | 1/(20 ln N) | |
|---|---|---|---|
| 10 | 0.0156 | 0.02171 | ok |
| 20 | 0.0175 | 0.01669 | **violates** |
| 40 | 0.0150 | 0.01355 | **violates** |
| 80 | 0.0116 | 0.01141 | **violates** |
| 120 | 0.0118 | 0.01044 | **violates** |

Four of five tabulated points. The companion claim "ρ_N log N < 0.047 in every
recorded sample" also fails — the tabulated values reach 0.0565.

Independent recomputation reproduces the table at 12 bins (N=10: 5.1509 /
8.2879 / 0.01600 against the paper's 5.1436 / 8.2823 / 0.0156) and then
increases monotonically with refinement, so this is not a discretization
artifact. The paper now states `ρ_N ≤ 1−ε` — the strength the argument
actually consumes — and records `1/(20 log N)` as falsified.

## What this redirects

The source model is a *model*, and the loss in passing to it is real and grows
with `N`. But the exact target is satisfied on every threshold tested. So:

> **Work the exact target directly**, in the output-defect metric of
> `thm:newdOutputDefect` where it carries constant one
> (`y_N ∈ Ran D_out^{1/2}`, `‖D_out^{†/2} y_N‖ ≤ 1`).
> Further effort on the Gamma–Tate source estimate does not close row (d),
> however sharp it becomes.

## Verification performed

Independent of the phase-114 verifiers, this phase's assembly was checked:

- **Gamma kernel in closed form.** `Ψ(Δ) = Σ_j e^{-a_jΔ}/a_j²`, `a_j = 2j+½`,
  equals `(1/π)∫₀^∞ g_Γ(τ)cos(τΔ)/τ² dτ`. Validated against direct quadrature;
  `Ψ(0) = ¼ψ′(¼)` exactly. Vectorized with an Euler–Maclaurin / `E₁` tail,
  machine precision.
- **Mesh-independence.** Every form (`L²`, Gamma, shifts, `A_T`) is *exactly*
  invariant to 9 digits across refine 4→64 on a fixed function.
- **`thm:exactstep`(4)**: `E*A_{τ_{j+1}}E = A_{τ_j}` — old-core spectra agree
  to `0.000e+00` at 9 consecutive prime-power steps.
- **`thm:exactstep`(5)**: corona minus annulus-primitives `= 2` exactly, at
  every step tested.
- **Balanced factorization**: `A = R − L` to `0.000e+00`, both halves PSD.
- **Source model** validated against `phase-116/.../urg_negative_test.py`; the
  FFT reference converges monotonically to this phase's closed form.
- **Range conditions** `r ∈ Ran R_0`, `b_E ∈ Ran A_0^{1/2}`: residuals `1e-15`
  to `1e-14` — consistent with `thm:newdRegularizedStep` deriving them.

## Contents

`scripts/`
- `rowd_assembly.py` — mesh, Gram, compressed shifts, closed-form Gamma, Tate
- `rowd_threshold.py` — old/new split, blocks, the exact Schur target
- `rowd_source.py` — the Gamma–Tate source defect `𝔇_N`
- `measure_cN.py` — the comparison, with three natural `Ξ_N`
- `sweep.py`, `rho_only.py` — drivers; `cN_results.csv`, `sweep.out`, `rho.out`

Needs `numpy`/`scipy` only (float64 diagnostic). `python-flint` is *not*
required here; it is needed only for the certified Arb tier in
`04-papers/42-arithmetic-lefschetz-programme/certificates/row_d_log2/`.

## Scope

Floating-point Galerkin computation, not interval-certified. The two headline
conclusions are one-sided-robust as argued above, but the underlying matrix
entries are float64 and the claim "`c_N < 1`" would need interval arithmetic
to be a theorem. Nothing here bears on RH; row (d) is not closed, and this
phase makes it *less* likely that the source route closes it.
