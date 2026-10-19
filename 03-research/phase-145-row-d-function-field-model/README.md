# Phase 145 — Row D: the function-field model of the frame

**Option (β) of `ROW-D-SYNTHESIS-PHASES-135-144.md` §3 (α follows in phase 146).**
Build the whole row-D frame — carrier, canonical class, degree, effective cone, `I_∞`, `Frob_n`, the
trace cone — for a curve `C/F_q`, where RH is a **theorem** (Weil), and see what the comparison says.

**[ROUND 2.** Audit `R145_002` — **ACCEPT WITH MAJOR REPAIRS, no FATAL**. All
twelve findings accepted and discharged; ledger in `R145_003_ROUND2.md`; `R145_001` repaired in
place with bracketed notes. The two headline claims are **unchanged**. Three numbers and one target
moved: `s_C` is `θ`-dependent, so the model's sharp constant is `s_C^* = √(7/11)` (not `√7/3`) and the
deficit is `131.4×`, not `76.7×`; the witness is at `d = 3`, not `d = 6`; Theorem D.41.17(ii)–(iv) is a
`g = 1` theorem; and **(P145) is withdrawn for (P145′)**, because its bigness clause was **RH
restated**.**]**

*The falsifier protocol is inverted here: the model is a solved case, so every transcribed statement
must come out **true**, and every break or change of truth value is a finding (`MISMATCH 1–10`).*

## Outcome in three lines

1. **The prediction of record is refuted.** The frame defect theorem (no `h⁰` with (a),(b′),(c))
   **holds** in the model, with `s_C^* = √(7/11) = 0.7977 < 1` — a deficit **`131.4×`** the arithmetic
   one — and a witness at `d = 3` instead of `d = 325`, **in a case where RH is true**. So `s < 1` is a
   property of the **cone**, not a signature of a missing `h⁰` and not evidence about zeros.
2. **The frame's effective cone, identified exactly.** In the model,
   `𝓔_C = Cone{ q^{−|n|/2}·Γ_{q^n}, q^{−|n|/2}·Γ_{q^n}^t }` — the graphs of the Frobenius powers and
   their transposes, and nothing else — with Gram `q^{−|a−b|/2}N_{|a−b|}` (the Euler product). The
   geometric effective cone `Eff(C×C)` is strictly larger; the ratio of support functions in the
   direction `θ` is `s_C(γ_1,θ)`, minimised at `s_C^* = √(7/11)`. (`σ(Eff‾) = ½` is proved for `g = 1`
   via the abelian-surface nef argument; **open for `g ≥ 2`**, O-37.)
3. **The named ingredient** is the **divisor group of the surface**: the rulings `e_∓` as *effective*
   classes (they are the radical of the boundary form arithmetically), plus **bigness**
   `D² > 0, D·H > 0 ⟹ D` effective. Adjoining the rulings alone is **proved insufficient**.
4. **[round 2]** Bigness as a *clause* is **RH restated** (Proposition D.42.5, frame-internal, with
   converse). So phase 146 is handed the **mechanism** — **(P145′)**: (4a) a sections functor with a
   *rational* bigness conclusion `D ∈ 𝔈⊗Q`, (4b) the degree gate, (4c) bounded density over the
   enlarged cone — with the RH-equivalence **printed in the blueprint** so that no round can mistake
   assuming it for proving it.

Also: `O-23` ("the absence of a function-field model of `D^W`") is **closed affirmatively**.

## Files

| file | what it is |
|---|---|
| `R145_000_BLUEPRINT.md` | blueprint: D.41 items 1–6, D.42, D.43, the acceptance test ("names the ingredient"), the inverted falsifier protocol, and the binding corpus consequences |
| `CORPUS_CHECK_R145.md` | prior-art audit, read first; six items with `NEW` / `TRIED–PROVED` / `TRIED–PARTIAL` / `TRIED–NO-GO` verdicts and a per-item reuse instruction |
| **`R145_001_ROUND1.md`** | **the round-1 document, repaired in place in round 2** (bracketed `[REPAIRED, round 2, Fn]` notes). §D.41 (the model, complete: carrier and Weil class with all discreteness/periodicity changes recorded; the explicit formula (145.4); the dictionary `E ↦ D_E` with the sign decided; `K_C`; Lemma D.31.4 in the model with `s_C` exact and the witness; the geometric `h⁰_C`; section cone vs pointwise cone; the trace cone `B4_C`), §D.42 (`[X]`,`[Y]`,`[Z]`, the separating feature, **(P145′)**), §D.43 (synthesis input), §D.44 (corpus check per idea), §D.45 (paper-facing), §D.46 (open list O-30′–O-39), §Label. Round 2 adds **Prop. D.41.12′** (the sharp `s_C^*`), **MISMATCH 11**, the `g = 1` restriction of D.41.17 with its abelian-surface proof, and **Prop. D.42.5 + (P145′)** in place of (P145) |
| `R145_002_AUDIT.md` | audit of round 1: ACCEPT WITH MAJOR REPAIRS, no FATAL; F1–F6 MAJOR, m1–m6 minor; both headline claims verified independently |
| **`R145_003_ROUND2.md`** | **round 2.** Per-finding ledger (all twelve accepted), the independent re-derivations of F1 (sharpened: an **exact triple tie** at `n = −2,0,+1`, proved in closed form) and F3 (Prop. D.42.5 with converse), the **final text of (P145′)** with its model/arithmetic supply table, and the hand-over to phase 146 |
| `scripts/sC_and_points.py` | the round's only script. Brute-force point counts for every isogeny class of elliptic curves over `F_2` and `F_3`; `s_C(γ,θ)`; the threshold `d_0` and a certified witness with margin; the coefficients of `K_C` and the sign test; the Gram check `I_∞^C(δ_a,δ_b) = q^{−|a−b|/2}N_{|a−b|}`; the two support functions; explicit preimages of `F_1`, `F_2`, `F_0`, `κ_C` in `D^W_C`; and **§[8], new in round 2**: the `θ`-optimised constant `s_C^*`, its closed form, the exact tie pattern, `d_0^*`, and the minimal witness degree at both `θ = π/2` and `θ = θ^*`. `--fast` supported; every constant is also given in exact closed form in the text, so nothing depends on the script. |

## The curve of record

`C = E/F_2 : y² + xy = x³ + 1`, `g = 1`, ordinary. Brute force: `N_1 = 4`, so `a = q+1−N_1 = −1`,
`h = P(1) = 4`, `α = (−1 ± i√7)/2`, `|α| = √2`. Then **exactly**

    s_C(γ_1, π/2)² = (4q − a²)/(q+1)²                         = 7/9  ,   d_0  = 9/2   (witness d = 5)
    (s_C^*)²        = (4q − a²)/((4q − a²) + (q+1+a)²)         = 7/11 ,   d_0^* = 11/4  (witness d = 3)
    at  tan θ* = (q+1+a)/√(4q − a²) = 2/√7 ,  θ* = 0.647284848…

Arithmetic comparison, imported verbatim (`R142_001` Prop. D.31.5, not re-derived):
`s_1 = 0.99846016271880910923…`, `d_0^arith = 324.9598266…`, witness `d = 325`. **On the line
`θ = π/2` is the optimum; on the lattice it is not** (MISMATCH 11), so the apples-to-apples comparison
is `s_1` against `s_C^* = √(7/11)`: deficit `131.4×`.

**Two limitations of the certified model, on the record.** (i) `g = 1`, so it sits on the side
`𝓔_C ⊆ B4_C` — **opposite** to the arithmetic `𝓔 ⊄ B4` (`R143_001` Rem. D.34.2): no inference about the
trace cone may be drawn from it (O-38). (ii) The upper bound `σ(Eff‾) ≤ ½` is proved only for `g = 1`
(O-37).

## Reproduction

```
python3 scripts/sC_and_points.py          # full
python3 scripts/sC_and_points.py --fast   # short n-range; same conclusions, same margins
```

## Labels

Everything classical is labelled **`CLASSICAL`**, not `PROVED`: Weil's theorem, Hartshorne V.1.6 /
V.1.8 / V.1.9 and Exercises V.1.9–V.1.10, Serre's *Zeta and L-functions*, Hindry–Silverman A.4,
Lazarsfeld §2.2. The row-D label is **unchanged**; no label is claimed. Full table in
`R145_001_ROUND1.md` §Label.

## Next

Confirmation round, then `R145_005`. Phase 146 proceeds on **option α**, receiving
**(P145′) as target-of-record** together with the sign-corrected pairing statement (`J ≥ I_∞` on `P^W`,
`J ≤ 0` provable there — a *dominating non-positive* form), which is **not** opened here. The model's
translation of α goes across too: `J` is the intersection form of a **larger** `NS` in which `P^W`
acquires more negative directions, and those come from correspondences that are *not* Frobenius powers.
**Proposition D.42.5 must be printed in the phase-146 blueprint**: it is the statement of what α may
not assume.
