# Phase 147 — Row D: the Galois group ring `Z[Gal(L/F)]` as the missing `+`

*Row D = the sign. Question: does the group ring of a Galois group, acting on the arithmetic square by
the graphs `Γ_σ`, supply the ring of effective correspondences (the `+`) that `Spec Z` lacks — and does
it enlarge the frame's effective cone toward bigness?*

**Answer after three rounds: it supplies the `+`, and the `+` is inert at `ζ`.** One mechanism, seen at
two levels:

* **Radial realization (round 1).** Every `σ ∈ Gal(K/Q)` preserves the idele modulus, `|σx| = |x|`, so
  the radial realization map `R : Corr(C_{K,S}) → End(D^W)` sends every Galois correspondence to the
  identity: `R(Γ_σ) = id`. `Z[G]` acts through its augmentation; cone, support function (`≤ s₁`) and
  `dim H⁰` do not move, and everything is `Ξ_a`-uniform. *(Upstairs nothing collapses — the theorem is
  about `R`, not about "the carrier".)*
* **χ-graded carrier (rounds 2–3).** On `𝒟_L = ⊕_χ (D^W ⊗ C)` with phase 139 Theorem D.20.2's form,
  graded by **conjugate packets** (the `χ`-slot paired with the `χ̄`-slot), `Z[G]` acts by `χ(σ)` and the
  blueprint's formula is **true and proved, with no adjoint smuggled in**:
  `I(Γ_σE, Γ_τF) = Σ_χ χ(στ⁻¹) I^{[χ]}(E_χ, F_χ̄)`. The cone is the isotypic image of nonnegative
  `C_c^∞(R×G)` tests; the Galois action is by **norm-one translations**; and there are effective classes
  with negative character coordinates — **the `+` exists**, the analogue of `[Γ_i]` in the model.

> **Theorem D.55.9′ — the phase's result, and the sole basis for closing** (numbered statement and
> proof in `R147_003b` §R3.3). The `χ = 1` slot of the cone `𝓒` is **exactly** `𝓔^∞ = 𝓔 ∩ C_c^∞(R)`,
> because `f_1 = Σ_{g∈G} f(·,g) ≥ 0` and every nonnegative `C_c^∞` test arises this way. Hence the
> support function **at the `χ = 1` slot** is `S(γ,θ,1) = s(γ,θ)` — **unchanged**, for every abelian
> `L/F`, every tower and every order `m`. Why: `f_1 = h·t(E')` is the coset average, and norm-one
> translations fix `u = log|x|`, so the coset average cannot see them — the round-1 lemma one level up.
> *(Not via the `G`-invariant **sector** — that is a compatible but different statement — and not via a
> "unique `χ_ρ`": a zero of `ζ_F` may also lie in `Z(Λ(·,χ))`, and nothing needs to exclude it. Both
> routes are withdrawn in `R147_003b` §R3.3.)*

**Function-field control.** On `E/F₅ : y² = x³+x` (`π = 1+2i`, `End = Z[i]`, `Aut = μ₄`) the
automorphism graph `Γ_i = ½Γ_π − ½Δ − F₁ + F₂` is an irreducible curve, and the cone constant rises
`2/3 → 1/√2 → 2/√5`, all now **proved**, against `1` for `Eff`. That gain comes from the discreteness of
`(log q)Z`; the arithmetic carrier is `R` and the same mechanism buys far less (`MISMATCH 12`).

## Files

| file | contents |
|---|---|
| `R147_000_BLUEPRINT.md` | blueprint: D.50–D.54; warnings W-a (no trace-form positivity), W-c (falsifiers by structure) |
| `CORPUS_CHECK_R147b.md` | pre-phase corpus check |
| [`single-prime-tower-corpus-check/`](single-prime-tower-corpus-check/) | second thread of the phase: corpus check for single-prime Frobenius towers and `Frob ⋆ Δ^rad` (no construction; own README) |
| `R147_001_ROUND1.md` | round 1 (D.50–D.54). **Ends with `Corrections of record` C1–C19 — read that first**; body not rewritten |
| `R147_002_AUDIT.md` | audit 1: ACCEPT WITH REPAIRS (0 FATAL, 6 MAJOR, 11 MINOR) |
| `R147_003_ROUND2.md` | round 2. Part A: all of audit 1 discharged. Part B (§D.55): the χ-graded carrier. **Ends with `Corrections of record` D1–D20 — read that first**; body not rewritten |
| `R147_004_AUDIT_R2.md` | audit 2: **ACCEPT PART A; PART B REQUIRES MAJOR REPAIRS** (0 FATAL, 7 MAJOR, 9 MINOR, 4 NOTE) |
| `R147_003b_ROUND3.md` | **document of record for Part B.** Repairs only: packet grading + real symmetric (not sesquilinear) form (MAJOR 1–2), `C_c^∞` cone with a two-halves support proof (MAJOR 3), the `S = 1` framing withdrawn (MAJOR 4), the `θ`-freedom clearing argument withdrawn → O-47.7 (MAJOR 5), the false `t`-clause deleted (MAJOR 6), `dim H⁰ ≤ 1` downgraded to a remark (MAJOR 7), all 9 MINORs and 4 NOTEs, `s_Frob = 2/3` now proved. **Ends with `Final corrections` C1–C9** from the confirmation round: Theorem D.55.9′ now a numbered theorem with a proof in the `f_1` form (C1), the base-dependent degree normalisation (C2), `θ*(6) = π/6` (C3), `ι(𝓔^∞)` not `ι(𝓔)` (C4), `K_H ∉ closure(𝓒)` proved (C5), script docstring (C6), `+9%` (C7), absolute convergence (C8) |
| `R147_004b_CONFIRMATION.md` | confirmation: **ACCEPT** with C1–C7 (0 FATAL); all of audit 2 confirmed discharged; numbers re-run and reproduced |
| `scripts/graded_support.py` | `L(m)` for `m = 1..12` (margins `≤ 1.1e−16`); `S(γ,θ,m)` at `θ = π/2` and minimised over `θ`; `σ` and `d₀` **as lower bounds**, exact argmin `d/2`. Docstring rewritten to the packet pairing; the per-χ form and the "may choose theta" clause are gone (C6). **Theorem D.55.9′ is exact and is not computed here** |
| `scripts/model_intersections.py` | `E/F₅`: point counts, `Γ_α·Γ_β = N(α−β)`, fixed points + Riemann–Hurwitz, the NS identity for `Γ_i` (integer-exact), the three cone constants, cross-check against R145's `√(7/11)` |
| `scripts/epstein_cone_test.py` | `deg K = 1` normalization check; the `K_Q` membership table (eleven discriminants); `Ξ_Q` on the real axis; quadrature margins |

## Reproducing the numbers

```
python3 scripts/graded_support.py --fast       # ~2 min
python3 scripts/model_intersections.py         # ~4 min   (--fast: ~20 s)
python3 scripts/epstein_cone_test.py --fast    # ~3 min
```

Of record (round 3 framing):

```
L(m) = min_th max_k |cos(th + 2 pi k/m)| = cos(pi/m) (m even >=4), cos(pi/2m) (m odd >=3), 0 (m<=2)
       argmin d/2;  numerics agree to <= 1.1e-16       [round 1's "cos(pi/m) throughout" was wrong for odd m]

S(gamma_1, pi/2, m) = 1  exactly when 4 | m
       -- NOT a new value: s(gamma,0) = 1 for every gamma, and max_th s = 1 is Paper 47 (19.2).
          For 4|m the mu_m-orbit of pi/2 meets pi Z.  Nothing ever binding is lifted.
chi = 1 SLOT of the cone = E^inf exactly (f_1 = sum_g f >= 0)  ->  S(gamma,theta,1) = s(gamma,theta)
       -- Theorem D.55.9', exact, not computed: the phase's result.

sigma(gamma_1,m) = min_th S  <  1  for every finite m   (analytic, via Prop 19.18)
       LOWER bounds:  s_1 = 0.99846016 (corpus, certified) at m=1 -> d_0 = 324.9598266
                      0.999613 (m=4) -> d_0 >~ 1294 ;  0.999956 (m=12) -> d_0 >~ 11313 (+9%)
       and these are thresholds of a theorem NOT stated for L(s,chi)  -- O-47.7

model:  s_Frob = 2/3,  s_AutFrob = cos(pi/4) = 1/sqrt2,  s_End = 2/sqrt5   (all PROVED)
        R145 record-curve cross-check: 0.7977281 vs sqrt(7/11) = 0.7977240 (margin 4.1e-06)
```

## Warnings honoured

* **W-a** — no positivity of any trace form on `Z[G]`, of `I^{[χ]}`, or of `𝓒` is claimed anywhere.
  `I^{[χ]} ≤ 0` on a χ-effective cone **is GRH for `L(s,χ)`** and is never asserted; the bigness clause
  for `𝓒` **would be** GRH by an analogue of `R145` Prop. D.42.5 that is **not built**.
* **FATAL rule** — raised in round 2, and **cleared in round 3 on the correct ground**: the value `1` at
  `θ = π/2` for `4 ∣ m` is Paper 47 (19.2)'s value, carries no new inferential power, produces no `h⁰`,
  and makes no transfer theorem run. Round 2's "first support function in row D to reach `1`" is
  **withdrawn**.
* **No label anywhere else in the corpus is changed.** One repair issued to R145 Prop. D.41.12′
  (F-147-1, the `n = −1` exclusion clause; confirmed on re-checking, R145's record curve unaffected).

## What is closed, and what is not

**Closed, on the negative, by Theorem D.55.9′ alone** — now a numbered theorem with a complete proof
(`R147_003b` §R3.3). Not by `dim H⁰ ≤ 1` (withdrawn as load-bearing), not by the `d₀` table, not by any
`S = 1` claim, and not by the `G`-invariant-sector inference (withdrawn as a non sequitur).

**Explicitly open:**
* **O-47.7** — the `χ ≠ 1` sectors. A `ζ_F`-frame theorem consumes **all** zeros of `ξ_L = ∏_χ Λ(s,χ)`,
  so the enlarged constants at `L`-zeros **would** matter to it; rounds 2–3 show only that they are
  irrelevant at the zeros of `ζ_F`. Includes: build the direction-`θ` witness family `F_θ` (Paper 47's
  `F_0` is **odd** and tied to `θ = π/2`), and state an analogue of Def. 19.19 / Thm 19.23 for
  `Λ(·,χ)` — **no such theorem exists**.
* **O-47.8** — non-abelian `L/F`: isotypic components of dimension `χ(1) > 1`, `Γ_σ` acting by a matrix
  `ρ_χ(σ)`, and D.20.2 only `PROVED-CONDITIONAL` on Artin holomorphy there.
* **O-47.1′** — `𝒟_L` is a **model**, not a realization (the `(u,g)` coordinates are a projection; `S`
  is an equality for the model, at most `≤` for a realizable cone).
* **O-47.3′** — (4a) of (P145′) on `𝒟_L`, restated as a mathematical question; round 2 tested a
  different object and says nothing about it.
* **O-47.4–O-47.6** carried. **O-47.2 withdrawn** (closed at `R139_004` H4).

## Next

`R147_005`. The confirmation round's condition for closing — *"with C1 written as a numbered
theorem in the `f_1 = Σ_gf` form, phase 147 may close"* — is met.
