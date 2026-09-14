# R145.004 — Hostile confirmation, phase 145

*Auditor: Opus 5, hostile. Date 2026-09-14. Targets: `R145_003_BUILDER_ROUND2.md`, the 13 in-place
`[REPAIRED, round 2, …]` notes in `R145_001_BUILDER_ROUND1.md`, `README.md`, `scripts/sC_and_points.py`
§[8]. Every repair was checked **at its site of use**, not only in the ledger; F1's and F3's
re-derivations were re-run from scratch; the script was re-executed.*

**Verdict: CONFIRMED. All twelve findings discharged. No new MAJOR finding. Phase 145 closes.**

---

## 1. Per-finding status

| # | status at the site | note |
|---|---|---|
| **F1** | **DISCHARGED and CORRECTED IN MY FAVOUR** | see §2 |
| **F2** | **DISCHARGED by restriction** | D.41.17(iii) now proves both bounds for `g = 1`; `g ≥ 2` declared OPEN (O-37). Correct. |
| **F3** | **DISCHARGED** | Prop. D.42.5 with converse; (P145) withdrawn; (P145′) in place. See §3. |
| **F4** | **DISCHARGED** | D.41.9bis(ii) now bounds `C_F` by the (11.17)-type sum; "attained" withdrawn. |
| **F5** | **DISCHARGED** | D.41.7 carries "`α_i` pairwise distinct" (verified for the record curve by `a²−4q = −7 < 0`); MISMATCH 6 carries the Tate rank count and the supersingular caveat. |
| **F6** | **DISCHARGED** | `ω_C` introduced; `ω_C`, `K_C`, `K_{C×C}` now three distinct symbols. |
| m1–m6 | **all DISCHARGED** | 12 isogeny classes; script §[6] comment rewritten and the correction also printed in D.41.17(iii); `d = 5` / `d = 3`; MISMATCH 7 scoped to `g = 1`; O-38 opened for the `g = 1`/`B4` asymmetry; `131.4×` with the θ-qualifier throughout. |

## 2. F1 — recomputed; the builder is right and **my own value was the approximation**

Recomputed at 30 digits, independently of both documents:

    θ^* = atan((q+1+a)/√(4q−a²)) = atan(2/√7) = 0.647284848015652521794515587806
    s_C^* = √(7/11) = 0.797724035217465641855126209765 ,   d_0^* = 11/4 exactly
    entries at θ^*:  n=−2, 0, +1 all equal 0.797724035217466  → EXACT TRIPLE TIE, confirmed;
    largest remaining entry: n=+3 → 0.620452027391 ;  |n| ≥ 5 ⟹ ≤ 1/cosh(5log2/2) = 0.1754.

The closed-form proof of the `n = −2` entry is correct as written (`\cos2θ_u = −3/4`,
`\sin2θ_u = −√7/4`, `\cosh\log2 = 5/4`, giving `(5√7/4√11)(4/5) = √(7/11)`). **My audit's
`0.7977245620 at θ ≈ 0.6472859` was a grid artefact** (a kink minimum; linear error in the mesh); the
exact value is `√(7/11)`, and the lead's `0.79779 at θ ≈ 2.4944` is the mirror optimum `π−θ^*`. The
builder's side condition (`no |n| ≥ 2 entry exceeds`) is a genuine gap in my derivation and is correctly
**printed as a hypothesis** of Prop. D.41.12′ and verified. `d_min = 5` at `π/2` and `d_min = 3` at
`θ^*` reproduced from the script, windows and margins matching. MISMATCH 11 is correctly stated and its
arithmetic half ("on the line `π/2` **is** the optimum, because the nearest peak is pushed furthest from
`u = 0` there") is correct. **F1 discharged; the sharpening is a genuine improvement over my finding.**

## 3. F2, F3 — re-derived

**F2.** The upper bound now runs: `E×E` abelian ⟹ every effective divisor is nef (translate off a given
curve) ⟹ `\overline{\mathrm{Eff}} ⊆ \mathrm{Nef} ⊆ \overline{\mathrm{Pos}}`, and on `\overline{\mathrm{Pos}}`,
`D² ≥ 0` reads `x²+y² ≤ ab`, so `|y_D| ≤ √(ab) ≤ ½(a+b) = ½\deg D` (AM–GM, legitimate since `a,b ≥ 0`
for nef `D`). **Both steps verified.** One residue: *the fact* (effective ⟹ nef on an abelian variety)
is standard and correctly argued in the text, but **"Mumford, `Abelian Varieties`, Ch. II §6" should be
checked against the book** before it reaches a paper — the statement actually used is the
translation/theorem-of-the-square corollary, and the section number is the weakest link in an otherwise
exact citation list. Non-blocking. The "supremum, not attained" correction is right.

**F3.** Proposition D.42.5 re-derived in both directions, independently:
(⟹) with `\deg K = 1`, `I_∞(P,K) = ½\deg P = 0`, `I_∞(K,K) = ½`: `P+εK` has degree `ε > 0` and square
`q+ε²/2 > 0`, so clause (4) puts it in `𝔈`; closedness gives `P ∈ 𝔈`, `\deg P = 0`, `P ∉ 𝓝_∞` — gate
fails. (⟸) under RH a positive-cone class of degree `0` lies in `𝓝_∞`. **Both correct.** Two residues,
both presentational: (a) "(⟸) … `\deg D = 0`, then `D` is primitive" needs its half-line —
`Φ_D(0)+Φ_D(1) = 0` together with `I_∞(D,D) ≥ 0` forces `Φ_D(0)Φ_D(1) ≥ 0`, hence both vanish; (b)
`\overline{\mathrm{Pos}}+𝓔` is asserted closed, and a sum of closed cones need not be closed (take the
closure; under RH the gate survives it, by the same estimate). Neither affects the statement.

**Verdict on (P145′): SOUND, WELL-POSED, AND NON-TRIVIAL.** The trivial solution is excluded twice over
(`𝔈 = D^W` fails (4b), and supplies no `H⁰` for (4a)) rather than only by the falsifier clause — which
was my objection to (P145). Clause (4a) now demands the *construction* (a finite-dimensional `H⁰`, a
**scaling-invariant** divisor map — the point of `113_11` Cor. 3.2 — and a **rational** bigness
conclusion `D ∈ 𝔈⊗Q`), (4b) and (4c) name the two properties Theorem 12.3 Steps 1–2 and 4 consume, and
**the RH-equivalence is printed in the problem statement itself** with the explicit instruction that a
round assuming (4a)'s conclusion has proved nothing. The supply table is accurate: I checked the model
column (V.1.6 + Serre duality + `χ(mD) → ∞`) and the arithmetic column (`113_11` Thm 3.3 / Concl. 4.1;
`R(E)` as the `χ`-side; D.27.4 as the surrogate `h²`). O-37/O-38/O-39 are the right three residues, and
the warning that **(4c) may bind before (4a)** is well taken.

## 4. The hand-over sentence (rank statement) — CORRECT, and it can be made sharper

`\mathrm{rk\,End}_{F_q}(E) = 2 = 2g` for the ordinary curve of record (`π` generates an order in
`Q(\sqrt{−7})`), so by Tate `\mathrm{rk}\,NS(E×E) = 2 + \mathrm{rk\,Hom}(E,E) = 4 = 2+2g`: **`V_C` is
all of `NS(E×E)_R`**, the enlargement of O-36 is *not* proper here, and the frame's carrier loses no
class. The sentence is therefore right but weak, and the model says something much more precise:

> **What is actually missing is not classes but the *additive* structure of the endomorphism ring.**
> `NS(E×E)_R` is spanned by `F_1, F_2` and the graph classes `Γ_α`, `α ∈ \mathrm{End}(E) = Z[π]`, with
> `Γ_α·F_1 = 1`, `Γ_α·F_2 = \deg α`, `Γ_α·Γ_β = \deg(α−β)` — the Gram `q^{−|a−b|/2}N_{|a−b|}` is the
> special case `α = π^a`, `β = π^b`, since `N_m = \deg(1−π^m)`. The frame's `𝓔_C` is the cone on the
> **multiplicative semigroup** `\{π^n\}` and its transposes `\{\barπ^n\}` only. The missing effective
> classes are exactly the graphs `Γ_{m+nπ}` of the **sums** — which are *not* nonnegative combinations
> of the `Γ_{π^k}` — together with the fibres. Equivalently: the frame keeps
> `\mathrm{Frob}_m⋆\mathrm{Frob}_n = \mathrm{Frob}_{mn}` (Paper 44 Thm 3ter.4(i)) and has **no `+`**.

This is the same gap as `F_1 ∉ 𝓔_C`, stated in the form phase 146 can use, and I recommend it replace
the O-36 sentence in the hand-over.

## 5. Overall and residue

**Phase 145 is confirmed and closes.** The two headline claims are untouched and were verified twice:
the frame defect theorem **holds** in a case where RH is a theorem (so `s < 1` is a property of the
cone), and `𝓔` is exactly the Frobenius-graph cone. The acceptance test (**name the ingredient**) is
**MET**, and round 2 added the thing that makes the name usable: the ingredient's operative half is
RH-equivalent, so phase 146 is handed a *mechanism* problem with the trap printed on it.

**Residue carried:** O-36 (the `NS` enlargement, now better stated as "no `+`"), **O-37** (`σ(\overline{\mathrm{Eff}}) ≤ ½`
for `g ≥ 2`), **O-38** (certify a `g ≥ 2` instance — the `g = 1` curve sits on the wrong side of
`𝓔 ⊆ B4`), **O-39** (bounded density over an enlarged cone; may bind first), the Mumford §6 citation
check, and the two presentational residues in D.42.5 (§3(a),(b)). None blocks the label position, and
**no label is claimed or changed** — correct.

---

## 6. Assessment of the lead's intended redefinition of phase 146's option α

*(Requested separately; this section is an assessment, not a finding against round 2.)*

**"The degree form on `Z[\mathrm{Frob}]` with a count interpretation — `\deg(m+nπ) = \#\ker(m+nπ) ≥ 0`,
with the infinite genus `Δ·Δ = −∞` as the named obstruction and the elliptic curve as control" is the
right reading of what the model taught, and it is sharper than "bigness".** Three reasons, and two
warnings.

*Why it is right.* (i) In the `g = 1` model, the entire content of F2's repair —
`\overline{\mathrm{Eff}} = \overline{\mathrm{Pos}}`, i.e. "the analogue of `s₁` is `1`" — **is** the
positive-semidefiniteness of the norm form `\deg(m+nπ) = m^2+amn+qn^2` on the rank-`2` module `Z[π]`,
whose discriminant condition `a^2−4q ≤ 0` is RH for `C`. So the ingredient named in D.42 has, in the
certified case, an elementary avatar. (ii) That avatar is a **counting functional, not a sheaf**: it
discharges (P145′)(4a) without any `H^0`, `𝒪(D)`, or cohomology — which is the only route I know that
is not blocked by `113_11` Theorem 3.3 (no `h^0` inside `D`) and Conclusion 4.1 (the CC import is
rank-one and signatureless). A mechanism that is a *count* rather than a *dimension* sidesteps both
no-gos instead of fighting them. (iii) The obstruction is correctly named and it is already on the
corpus's books in two independent places: `Δ·Δ = N_0 = 2−2g → −∞` is exactly Paper 44 Remark 8bis.1c
(`I_A(\mathrm{Frob}_n,\mathrm{Frob}_n)` **does not exist**) and Paper 46 Prop. 14.2
(`τ_{\log n}(ΠK) ∈ 𝓝_∞`). The model supplies the missing interpretation of that divergence: it is the
genus, and nothing else.

*Warning 1 — the F3 trap transfers verbatim.* `\deg ≥ 0` is a theorem on an elliptic curve **because it
counts a kernel**; the arithmetic statement "the degree form on `Z[\mathrm{Frob}]` is positive
semidefinite" is Weil positivity, i.e. RH. Proposition D.42.5's caution must be restated for α in its
own terms: **α must deliver the count, never the positivity.** A round that posits a positive form on
`Z[\mathrm{Frob}]` has assumed RH exactly as a round positing bigness would.

*Warning 2 — `g = 1` is the degenerate case, twice.* As `g → ∞` not only does `Δ·Δ = 2−2g` diverge, but
the rank of the endomorphism module grows, and the elementary norm form is replaced by **Rosati
positivity** `\mathrm{Tr}(f\,f^\dagger) > 0` on `\mathrm{End}(\mathrm{Jac})⊗Q`. The elliptic control is
therefore a control on the *shape* of the argument, not on its difficulty, and any round that only
reproduces `g = 1` has reproduced the one case where the mechanism is free. (This is O-38 again, from a
second direction.)

*The first decidable question.* Not "does the degree form exist" — too large. In order:

> **Q0 (free, one line, model-side, do it first).** Is the frame's own data enough to *reconstruct* the
> degree form? Yes: `\deg(m+nπ) = m^2+amn+qn^2` and `a = q+1−N_1` is read off the Gram
> `κ(1) = q^{−1/2}N_1`. **So the Euler product already contains the form; only its positivity —
> the count — is missing.** Recording this converts the programme's question from "find more data" to
> "find the interpretation", which is the useful narrowing.
>
> **Q1 (the first decidable question proper).** Does the **additive** module
> `M := Z⟨\mathrm{Frob}_n : n ≥ 1⟩` exist arithmetically with a *finite* diagonal? Paper 44 Rem. 8bis.1c
> says `I_A(\mathrm{Frob}_n,\mathrm{Frob}_n)` does not exist; the model says the value it is trying to
> take is `2−2g`. **Decide: is there a renormalization of the diagonal (a `2−2g` counterterm; a relative
> degree `\deg(α−β)` taken as primitive, with the diagonal defined only through differences) under which
> the Gram of `M` is finite, symmetric, and extends Paper 44 Thm 3ter.10's off-diagonal weights
> `Λ(n)n^{−1/2}`?** This is decidable, finite, and falsifiable: the model supplies the exact target
> (`Γ_α·Γ_β = \deg(α−β)`, a **difference-only** form, which is precisely how one builds a quadratic form
> whose diagonal has been subtracted), and the elliptic curve is the control in which the answer must
> come out "yes, and the form is the norm form".

If Q1 fails, α is dead in the same way the trace cone was, and the failure is diagnostic. If Q1
succeeds, the *next* question — and only then — is whether the resulting form's positivity admits a
count interpretation, which is (P145′)(4a) in its `Z[\mathrm{Frob}]` form. I recommend phase 146 be
scoped to **Q0 + Q1 only**, with Proposition D.42.5 and both warnings printed in its blueprint.
