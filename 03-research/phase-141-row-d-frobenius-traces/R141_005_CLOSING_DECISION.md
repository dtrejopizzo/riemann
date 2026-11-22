# R141.005 — Closing decision, phase 141 (an `h⁰` that reads the Frobenius traces → the Riemann–Roch-defined `h⁰`)

in round 2 on R141_002's construction), R141_002 (audit: 0 FATAL, 7 MAJOR, 7 MINOR; REVISE),
R141_003 (ledger), R141_004 (confirmation: CONFIRMED with C4–C6 inside §D.30). Checks: Serre
symmetry `R(K−E) = R(E)` (symbolic); the `χ > 0` witness `αK + βτ_cK` with rulings `(−ε, 2ε)`; the reading
of the dichotomy as Thm 12.3's own proof shape (agreed with the auditor before round 2); C5 applied in place.*

## 1. Results of record

| item | statement | label |
|---|---|---|
| D.26.1–6 | Frobenius traces `t_n(E) = I_∞(E, τ_{log n}g)` determine `E` mod `𝓝_∞` (`ker T = 𝓝_∞`), separation of `n^{½−ρ}` by the ζ-transform argument; moment cone `𝔐` convex, pointed, in the positive-degree half-space; (b′) for trace functionals = containment `{Ψ > 0} ⊆ 𝔐` | PROVED (D.26.7–10 RESTATEMENT) |
| D.27 | 2-homogeneous ray-continuous `Ψ` of the traces is the wrong ansatz (`¼m²` growth needs a non-homogeneous part); for `C^deg`, (c) ⟺ RH with `χ = 3/16`; case (B): (c) alone ⟹ RH (a weakening of Thm 12.3's hypotheses) | PROVED / RESTATEMENT |
| D.28 | **O-17 closed**: `Ξ_Q`-primitive `C_c^∞` test with `Ŵ^{(Ξ_Q)} > 0` (Prop. 12.4B transposed, `P = {0,1}`, non-real DH zero, Lemma 3.1 for the compactly supported inverse of `Π`); (AT-1)(ii) is a refutation again | PROVED |
| **D.30.1** | Serre symmetry `R(K−E) = R(E)`, `R(E) := ½I_∞(E,E) − ¼deg E + χ`, from bilinearity alone | PROVED |
| **D.30.4–5** | `h⁰_RR⁺(E) := max(R(E),0)·1_{deg E>0}` satisfies **(a) and (c) unconditionally for every `χ`** (gate argument: `deg E + deg(K−E) = 1`), growth `¼m² − ¼m + χ`, vanishes in degree `≤ 0`, non-homogeneous, non-bidegree, defeats D.24.7's witness; plain `max(R,0)` fails (b′) for every `χ` | PROVED |
| **D.30.7–8** | `χ > 0` refuted unconditionally (witness with rulings `(−ε,2ε)`, `Z = 0`); `χ = 0` calibrated exactly to the necessary bound `R > 0 ⟹ |Φ_E(ρ)| < √(ab)` | PROVED |
| **D.30.9–10** | **the clause (b′)⁺**: `deg E > 0 ∧ R(E) > 0 ⟹ ∃E' ≥ 0, E' ≢ 0, E − E' ∈ 𝓝_∞`; (b′)⁺ ⟹ RH (two proofs; the direct one via Thm 11.14(ii) needs no ampleness) | PROVED |
| D.30.11–12 | stable weakening (b′)⁺_st ("`D² > 0, D·H > 0 ⟹ D` big" form); Thm 12.3 survives it; (b′)⁺_st ⟹ RH without A7 (C10) | PROVED |
| D.30.13 | zero-free locus: every `(a,b)`, `a,b > 0`, with `Z(E) = 0` is realized effectively by `2√(ab)·τ_{log(a/b)}K` | PROVED |
| D.30.14 | `S_0` convex under RH (as a set, not a cone — C5 corrected); containment `T(S_0) ⊆ 𝔐` | PROVED (i), SKETCH (ii) |
| D.30.15–16 | (a),(c) model-uniform (gate needs only `deg_Z K_Z > 0`; polar rank irrelevant); **(b′)⁺ is false for `Ξ_a`** (witness `rF₊ + K_a`); for `Ξ_Q` Thm 11.14's constant is infinite (A7 fails) so Thm 12.3's frame does not transport | PROVED |
| **O-18** | RH ⟹ (b′)⁺ ? proved on the zero-free locus; general case needs a sufficiency criterion for the exponential moment problem; perturbative route blocked (R138 D.15.2b(ii)) | OPEN |

## 2. What the phase established
Row D is reduced **unconditionally** to one clause defined without zeros:

> **(b′)⁺ at `χ = 0`.** If `deg E > 0` and `½I_∞(E,E) > ¼deg E`, then `E` is equivalent modulo `𝓝_∞`
> to a nonzero nonnegative class.

(a) and (c) are free for every admissible `Z`; the clause implies RH; it is false for `Ξ_a` (so any proof
must use A3 at a named line); for `Ξ_Q` the frame breaks earlier (A7). A8 has not yet been needed —
this is the sharpest form T2's demand has taken, and the place where the Euler product must enter is now
a single existence statement. Whether the clause is *equivalent* to RH or strictly stronger is O-18.

## 3. Residues carried
R12: decide (C4.1) `C_F ≥ √(−I_∞(F,F)/2)` under RH — the cheap necessary condition that could refute
O-18. R13 applied in R141_005 (C5, C6). R14 wording items C1–C3, C7–C10 for Part III. R15 carried.

## 4. Decision
Phase 141 closed; no label change for row D. Phase 142 targets (b′)⁺_st at `χ = 0`, in the order the
auditor fixed: (Q-A) consistency with all known necessary conditions, starting with (C4.1) — cheap and
refutation-capable; then (Q-B) the sufficiency side of the exponential moment problem. FATAL rule from
line one: the clause implies RH and is false for `Ξ_a` while the entire frame holds there.
Paper-facing: P47-18…P47-25 (P47-25 = §D.30 entire).
