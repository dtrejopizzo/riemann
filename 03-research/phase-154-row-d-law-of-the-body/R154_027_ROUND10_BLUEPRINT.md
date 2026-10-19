# R154.027 — Blueprint, round 10: the hybrid certificate (lattice + canonical Lévy column) and the repair of Lemma V.

## 0. State after R154_026
Lemma T PROVED but its tail cost is linear in `Σ|a_j|` for atoms (full mass) and in `A = Σ|c_k|p_k!` for columns; Theorem O forces `A → ∞`,
so the tail is reduced, not removed. On atomic classes Lemma T is hopeless (`τ₁ ~ 10⁴¹`); Lemma F1 (periodic block rows, `τ₁ = 30`) stays the
tool for the lattice part. Lemma V(i) PROVED; V(ii)/(iii) proved only for the moment-free relaxation (Fejér witness violates both primitivity
constraints: `∫cosh(u/2)μ̌₀ = 1.19289`, `∫u·sinh(u/2)μ̌₀ = 0.13302`). Theorem E complete. Identity M correct; `ν_K = 2e^{−T}ν_{½,0}`.

## 1. Tasks
(H1) **Repair Lemma V** (PROVED or withdrawn): construct the corrected witness — mix `μ_{ε,R}` with two feasible measures whose moment
images span a neighbourhood of 0 in the moment map `(∫cosh(u/2)μ̌, ∫u·sinh(u/2)μ̌)`, correcting the `O(ε/R)` defect at cost `o(ε)`; prove
feasibility and the value bound `≤ V₀ + ε(log R + C)`; conclude the logarithmic exchange is sharp ON the primitive relaxation. If the
correction fails, say exactly why and downgrade (P154.8) back to OPEN.
(H2) **Hybrid Lemma (PROVED):** `ν = ν_lat + c·ν_{½,0}` (lattice atoms with period `P` + the canonical Lévy column, `s = ½`, `k = 0`, and
optionally `ν_{½,1}`). Tail certification: Lemma F1's periodic block rows for `ν_lat` (worst case `−ρ` per block, prime term exact on the
first `N` periods), PLUS in each block row the column term `−|c|·1/√(¼ + τ_left²)` evaluated at the block's left endpoint (legitimate: the
bound is additive over parts of `ν`, and the column bound is decreasing in `τ`). State and prove; check the pairing (columns are densities
on `|u| ≥ 2T`: `∫ν̂|F̂|² = 0` for `F ∈ P_T`).
(H3) **ONE LP** (single process, `timeout 900`): `T = 0.58`, the round-5 lattice class `M = 24` (414 atoms on `[2T, 2T+20]`), plus the two
column variables `c₀ (ν_{½,0}), c₁ (ν_{½,1})`, plus `β₀, β₁`; rows: cutting planes on `[0, τ₁ + N·P]` with `τ₁ = 30, N = 2` (reuse
`scripts/round6/r6lp.py` machinery) and the hybrid block rows of (H2). Matched control: the same LP with `c₀ = c₁ = 0` (this is round 5's
`−3.1802·10⁻³` — confirm it reproduces). Report LP value, fine-grid true minimum on `[0, τ₁+NP]`, `β₀, β₁, c₀, c₁`, `Σ|a_j|`, the F1 slack,
wall time. Decision: if the hybrid true min `> 0` on the fine grid, STOP (exhaustive F3 verification is a separate authorised step; it is
affordable since the B&B range is unchanged); if `> −3.18·10⁻³` by a factor `≥ 2` in deficit, CORROBORATED (the column buys the tail); else
REFUTED. Also record whether `c₀` comes out near `2e^{−T} = 1.1198` (Identity M's canonical value) — DIAGNOSTIC.
(H4) **Repairs to R154_025** (from R154_026, seven items): headline "tail solved / wall gone" → "tail cost reduced from exponential to
linear in ℓ¹; not removed"; "residual penalty reducible to 0" → extrapolation caveat; conditioning caveat (`l1_cols = 1.9·10⁵` vs cap);
"missing constant m" remark → tautology; Lemma V scope; the phase-55/58 [PROP 176.9] distinction kept.

## 2. Rules
Labels; FATAL rule (T = 0.58 < log 2, Paper-42-certified; new-method proof is the point); corpus-check lines ("hybrid certificate",
"canonical column", "columna canónica"); one LP only; deliverable `R154_028_ROUND10.md` (≤ 4000 words) + `scripts/round10/`.
