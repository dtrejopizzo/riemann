# R143.005 — Closing decision, phase 143 (`s_*`, the trace-positive cone, the repaired transfer theorem)

(audit: no FATAL, 4 MAJOR), R143_003 (ledger), R143_004 (confirmation: accepted; residue H12–H14 applied
in place). Checks: Lemma D.33.2's factor `π/(4γ)`; the proof of Thm D.34.10 (AM–GM +
Cauchy–Schwarz + `R > 0`); the compact-support question for `g = K + λh` (raised in R143_000, settled by the
auditor: class widened to `D^W` with rapid decay, nothing breaks).*

## 1. Results of record

| item | statement | label |
|---|---|---|
| D.33 | `s_* = m(γ₁) ∈ [0.99845824, 0.99846016]`, attained at `ρ₁`, `θ = ±π/2`; elementary bound `m(γ) ≥ 1/cosh(π/(4γ))`; every other zero has `m > s_1` by margin `8.4·10⁻⁴`. The **cone** constant `s_*^cone` (D.31.13) stays OPEN | PROVED / CERTIFIED |
| D.34.1 | trace-positive cone `B4^{g,0} := {E : t_0 ≥ 0, t_n(E) ≥ 0 ∀n}` for every admissible `g` (real even, `≥ 0`, rapid decay, Baire condition `Φ_g(ρ) ≠ 0`); contains `𝓝_∞`; `K` itself inadmissible (with `g = K` (T1′) fails) | PROVED |
| **D.34.5** | **(T1′): `B4^{g,0} ∩ P^W ⊆ 𝓝_∞`, unconditionally** — Landau on the Dirichlet series `Σ t_n n^{−w} = Φ_g(1)bζ(w−½) + Φ_g(0)aζ(w+½) − Σ_ρ c_ρζ(w+ρ−½)`, whose only real poles are the two polar ones (`ξ` has no real zero) | PROVED |
| D.34.7 | (T2) false for B4 (`C'_X = +∞`), so Thm D.32.4 does not apply to B4 | PROVED (case split, R143_005) |
| **D.34.8** | **transfer theorem 12.3-B4**: `h⁰` with (a), (b′)_{B4} (`h⁰(E) > 0 ⟹ E ∈ B4 + 𝓝_∞`, `deg E > 0`), (c) ⟹ `I_∞(F,F) ≤ 0` on primitive `C_c^∞` ⟹ RH. Uses only (T1′); no ample class, no Thm 11.14, no (T2) | PROVED (unconditional) |
| D.34.9′ | `(G⁺)`: `I_∞(g,g) ≥ 0` holds **unconditionally** for `g_λ = K + λh`, `λ ≤ (2W^abs(h))^{−1/2}` (O-25 closed) | PROVED |
| **D.34.10** | `(b′)_{B4}` for `h⁰_RR⁺` (`χ = 0`) is **true under RH**: `R > 0, deg > 0 ⟹ a,b > 0` and `t_n(E) ≥ 2√(abΦ_g(0)Φ_g(1)) − √(W(E)W(g)) ≥ 0` uniformly in `n` | PROVED under RH |
| D.34.12 | **`∃g: (b′)_{B4^g}` for `h⁰_RR⁺` ⟺ RH**; hence RH ⟺ ∃`h⁰` with (a),(b′)_{B4},(c) | PROVED + RESTATEMENT |
| D.34.13 | for `Ξ_a`: 12.3-B4 transports, its conclusion is false, hence `(b′)_{B4_a}` is false (FATAL rule invoked and resolved) | PROVED |
| D.34.14 | `ξ_K`: transport conditional on no real zero of `ζ_K` (Siegel); (ii) CLAIM (O-28) | PROVED (i) |
| **D.34.16** | unconditionally, for `b > 0`, `t_n(E) > 0` for all `n ≥ N(E)` (finite; effective iff `β_min(E) > 0`); under RH `N(E) ≤ 4W(E)W(g)/(b²Φ_g(1)²)` and `N ≤ 64d²` uniformly on `{R > 0, 0 < deg ≤ d}`; witness `N ≤ 15.96`; for `Ξ_a` the tail also holds and the violation sits at a **fixed finite index** — the A3-line is in the head, not the tail | PROVED |

## 2. What the phase established
Row D is now: **RH ⟺ trace positivity on the Riemann–Roch-positive set** — for every `E` with `deg E > 0`
and `½I_∞(E,E) > ¼deg E`, all Frobenius traces `t_n(E) = I_∞(E, τ_{log n}g)` are `≥ 0`. Labelled honestly:
a RESTATEMENT, because the `⟸` direction uses RH three times (now two: `W ≥ 0`, `|n^{½−ρ}| = 1`; `(G⁺)` is
unconditional). Its value: the `⟹` direction is an unconditional transfer theorem needing only (T1′); the
clause is incomparable with phase 142's refuted effective clause; and the RH-content is **index-local** —
automatic for `n ≥ N(E)`, concentrated in the head `n < N(E)`, uniform per degree slice under RH — with
`Ξ_a` failing at a fixed finite index because four polar exponents give no AM–GM floor where `ξ`'s two do.
Residue warning (auditor): unconditional uniformity of `N` on a slice is a quasi-RH zero-free-strip
statement (`inf Re ρ > 0` is not given by any classical zero-free region) — not a target.

## 3. Decision
Phase 143 closed; no label change. Phase 144 target (auditor's, adopted): **the fixed-index inequality**.
Identify the smallest index `m` at which `(b′)_{B4_a}` fails for `Ξ_a` (Remark D.34.16c), write the
`ξ`-inequality `t_m(E) ≥ 0` for `R(E) > 0, deg E > 0`, and decide whether it is unconditional for `ξ`
while false for `Ξ_a` — at fixed `n`, `ξ`'s two polar exponents give the floor `2√(abΦ_g(0)Φ_g(1))`.
Secondary: O-29 (sparse cone `{t_{2^k} ≥ 0}`), O-26; Horn A gated on O-19′/O-18′. Rejected: uniformity
of `N` on slices; attacking O-24 whole. Paper-facing P46-34…P46-42 (P46-41 corrected).
