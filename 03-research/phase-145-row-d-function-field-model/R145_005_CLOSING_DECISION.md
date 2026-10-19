# R145.005 — Closing decision, phase 145 (the function-field model of the frame)

R145_001 (rounds 1–2 in place), R145_002 (audit: accept with major repairs), R145_003 (ledger), R145_004
(confirmation: CONFIRMED). Independent checks: `s_C` θ-infimum recomputed independently (0.7977 at the mirror
optimum `π − θ*`), which exposed the mis-named constant (F1); `s_C² = 7/9` reproduced as the `θ = π/2` value.*

## 1. Results of record (all CLASSICAL inputs cited; new statements PROVED unless marked)
| item | statement |
|---|---|
| Model | discrete carrier `t ∈ (log q)Z`; Weil class; `Φ_E` Laurent in `q^{−s}`, periodic; explicit formula over `2g` zeros; **`I_∞^C(E,F) = +(D_E·D_F)`** with `D_E = Σ E(n)q^{−|n|/2}Γ_{q^n}`, Gram `q^{−|a−b|/2}N_{|a−b|}` (`N_0 = 2−2g` forced), `D_E·F_1 = Φ_E(0)`, `D_E·F_2 = Φ_E(1)`; closes phase-125 A125.009's gap |
| Defect | **the frame defect theorem holds on the curve**: for `E/F_2: y²+xy = x³+1`, sharp constant `s_C* = √(7/11) = 0.7977` (`tan θ* = 2/√7`, exact triple tie `n = −2,0,1`), threshold `d₀* = 11/4`, witness at `d = 3`; no `h⁰` on `D^W_C` satisfies (a),(b′),(c) — while RH for `C` is a theorem. So `s < 1` is a property of the **cone**, not of the zeros. Prior prediction refuted |
| Cones | `𝓔_C` = cone of Frobenius graphs (and transposes) exactly; `σ(𝓔_C) = ½s_C*` vs `σ(Eff‾) = ½` (both bounds for `g = 1`: `E×E` abelian ⟹ effective ⟹ nef; `g ≥ 2` OPEN O-37); `F_1 ∈ Eff ∖ 𝓔_C`; adding `F_1, F_2` to the cone does not raise `σ`; `B4_C` = Frobenius-nef cone; `𝓔_C ⊆ B4_C ⟺ g ≤ 1` |
| `K` | `Φ_{K_C} = ξ_C`; `K_C ≥ 0 ⟺ N_1 ≥ q+1`; `deg K_C = 2h q^{−g/2}`; **the frame's `K` is the ample class `½(F_1+F_2)`, not the canonical class `K_{C×C} = (2g−2)(F_1+F_2)`** — naming corrected for the arithmetic frame |
| Mismatches | eleven recorded, incl. no archimedean place (MISMATCH 5) and the lattice moving the optimal `θ` off `π/2` (MISMATCH 11); axioms A1–A9 do not separate the model from `ξ` |
| Withdrawn | three corpus sentences (R144_004 "signature of a missing sections functor"; synthesis §3(β) prediction; R142_003 D.32.1 consistency remark); **O-23 closed affirmatively** |
| (P145) | clause 4 (bigness) **⟺ RH** for closed `𝓝_∞`-saturated cones with the degree gate (Prop. D.42.5, both directions) — withdrawn as a target |
| **(P145′)** | build the **mechanism**: `(𝔐, 𝔈, H⁰, H²)` with (1) `I_∞`-extension, (2) rulings effective, (3) `Frob_n ∈ 𝔈` with Paper 44's Gram, (4a) a functor `H⁰` with divisor map into `𝔈 ⊗ Q`, (4b) degree gate, (4c) bounded density, (5) falsifier/field-uniformity; RH-equivalence printed; `𝔈 = D^W` excluded |

## 2. What the model taught (the named ingredient, sharpened by the auditor)
`NS(E×E)_R` is spanned by `F_1, F_2` and the graphs `Γ_α`, `α ∈ Z[π]`, with `Γ_α·Γ_β = deg(α−β)`; the
frame's Gram is the case `α = π^a` (`N_m = deg(1−π^m)`). **The frame keeps only the multiplicative semigroup
`{π^n}`; the missing effective classes are the graphs of the sums `Γ_{m+nπ}`.** The frame has
`Frob_m ⋆ Frob_n = Frob_{mn}` and no `+`. For `g = 1` the whole of "bigness" is the positive-semidefiniteness
of the norm form `deg(m+nπ) = m² + amn + qn²` on `Z[π]` — a **count** (`#ker`), not a sheaf — which is the
classical proof of RH for elliptic curves and the only route that sidesteps the sections-functor no-go
(113_11) rather than fighting it. Named obstruction to transport: `Δ·Δ = 2−2g → −∞` (Paper 44 Rem 8bis.1c,
Paper 46 Prop 14.2): the arithmetic curve has infinite genus.

## 3. Decision
Phase 145 closed; acceptance test met; no label change. Phase 146 (α, redefined): **the degree form on
`Z[Frob]` with a count interpretation** — Q0 (the Euler product already contains the form; the problem is
interpretation) and Q1 (does the additive module `Z⟨Frob_n⟩` admit a finite, symmetric Gram extending the
`Λ(n)n^{−½}` off-diagonal weights — a `2−2g` counterterm or a difference-only form `deg(α−β)`?), with the
elliptic model as control, Prop. D.42.5 printed, and the two warnings: **deliver the count, never the
positivity** (positivity of the form is Weil positivity = RH); `g = 1` is degenerate (rank of End grows with
`g`; the norm form becomes Rosati positivity). Residue: Mumford AV II §6 page-check; two presentational
half-lines in D.42.5; O-36…O-39 carried.
