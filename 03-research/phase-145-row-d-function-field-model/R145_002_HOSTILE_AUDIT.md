# R145.002 — Hostile audit, round 1, phase 145 (row D: the function-field model of the frame)

*Auditor: Opus 5, hostile. Date 2026-09-14. Target: `R145_001_BUILDER_ROUND1.md` (813 lines), `README.md`,
`scripts/sC_and_points.py`. Method: every claim assumed wrong until verified; all classical facts
re-derived or checked against the cited statement; every number recomputed independently (including
the script rerun in FULL mode); every corpus quotation opened at the cited line. No builder file edited.*

**Overall verdict: ACCEPT WITH MAJOR REPAIRS. No FATAL finding.** The mathematics of §D.41 is, with the
exceptions listed below, correct, and the phase's two headline claims — (1) the frame defect theorem
**holds** in a case where RH is a theorem, so `s < 1` is a property of the cone and not of the zeros;
(2) the frame's `𝓔` is exactly the Frobenius-graph sub-cone of `Eff(C×C)` — survive the audit intact
and are the most useful things row D has produced since phase 142. Six MAJOR findings and six MINOR
ones are listed. One of them (**F3**) changes what phase 146 should be told to do.

---

## 1. Verdict table

| item | verdict |
|---|---|
| D.41.1–2: carrier, explicit formula, dictionary, **the sign `+`** | **CORRECT.** Independently re-derived. No finding. |
| Gram `γ_a·γ_b = q^{−|a−b|/2}N_{|a−b|}`, `D_E·F_1 = Φ_E(0)`, `D_E·F_2 = Φ_E(1)` | **CORRECT**, certification reproduced (`3.553×10^{−15}`). |
| D.41.7 radical / dimension / isometry | **CORRECT BUT UNDER-HYPOTHESISED** — **F5** |
| `s_C` and the defect in the model (D.41.11–D.41.14) | **MECHANISM CORRECT; THE CONSTANT IS MIS-NAMED** — **F1** (and MINOR m3) |
| D.41.17 (the deliverable: two cones) | **HALF-PROVED**: `σ(𝓔_C) = ½s_C` correct; `σ(Eff) = ½` proved only as `≥` — **F2** |
| `K_C`, `deg K_C`, `κ_C ≡ ½(F_1+F_2)`, "the frame's `K` is the ample class" | **CORRECT**; one notation collision — **F6**; MISMATCH 7 over-general — m4 |
| `B4_C = 𝓔_C^∨`, `𝓔_C ⊆ B4_C ⟺ g ≤ 1` | **CORRECT** (caveat m5) |
| MISMATCH 1–10 and the three withdrawals | **JUSTIFIED**; all three quotations verified verbatim; one mismatch missing — **F1(c)**; one statement false — **F4** |
| D.42 naming of the ingredient | **CORRECT AS A NAME** |
| D.42.4 **(P145)** as the phase-146 target | **NOT SOUND AS WRITTEN — (P145) clause 4 is RH, not a construction problem** — **F3** |
| Labels, corpus check, README, paper-facing | **CORRECT** (two README numbers must move with F1/F2) |
| **Acceptance test ("names the ingredient")** | **MET, with the qualification of F3** |

---

## 2. What was verified and stands (no finding)

Recorded so that the repairs are not mistaken for a general doubt.

1. **The curve of record.** `y²+xy = x³+1 /F_2`: discriminant `−433`, odd, so smooth; affine points
   `(0,1),(1,0),(1,1)` plus `∞`, so `N_1 = 4` **by hand**; `a = q+1−N_1 = −1`; `2 ∤ a`, so **ordinary**;
   `h = P(1) = q+1−a = 4`; `α = (−1±i√7)/2`, `|α| = √2`. `N_m` for `m = 0..6` recomputed from
   `s_m = a s_{m−1} − q s_{m−2}`: `0, 4, 8, 4, 16, 44, 56` — matches.
2. **(W3)/(W4) are internally consistent and correctly used.** `Γ_f² = f^*`-adjunction:
   `2g−2 = Γ² + Γ·K_S = Γ² + (2g−2)(1+d)` gives `Γ_f² = d(2−2g)`, so `Γ_{q^n}² = q^n(2−2g)` and, after
   the half-density weight, `γ_n·γ_n = 2−2g = N_0` — the `N_0 := 2−2g` convention is **forced**, not
   chosen. `Γ_{q^m}·Γ_{q^n} = q^nN_{m−n}` (`m ≥ n ≥ 0`) is right: `F^m x = F^n x ⟺ F^n x ∈ Fix(F^{m−n})`,
   `N_{m−n}` set-theoretic solutions each of inseparable multiplicity `q^n`. `Γ^t_{q^m}·Γ_{q^n} = N_{m+n}`.
   Hence the Toeplitz Gram `κ(a−b)` for **all** signs of `a,b`, as claimed.
3. **The sign is `+` and the blueprint's `−` is genuinely refuted.** `(145.4)` re-derived from
   `N_m = q^m+1−S_m`; `Φ_{E⋆F^∨}(0) = Φ_E(0)Φ_F(1)` etc. check; so
   `I_∞^C(E,F) = Σ_m(E⋆F^∨)(m)κ(m) = +(D_E·D_F)`. **Consistency with the Hodge index verified in the
   direction the brief asks:** for real primitive `E`, `1−ρ = \barρ` on the line, so
   `I_∞^C(E,E) = −Σ_ρ|Φ_E(ρ)|² ≤ 0`, i.e. RH for `C` **is** `D² ≤ 0` on `{F_1,F_2}^⊥`, Hartshorne V.1.9
   with `H = F_1+F_2`, `H² = 2`. The `+` convention and the frame's "primitive `⟹` `I_∞ ≤ 0`" target
   agree. No sign error anywhere in §D.41.
4. **The fibre pairings.** `γ_n·F_1 = q^{−n/2}`, `γ_n·F_2 = q^{n/2}` uniformly in `n ∈ Z`; these are
   exactly the coefficients of `Φ_E(0)` and `Φ_E(1)`. So `D_E·F_1 = Φ_E(0)` (**not** `Φ_E(1)`) — the
   brief's "which is which" is answered correctly in the document.
5. **Script rerun, FULL mode.** Every printed constant reproduced: `θ_u = 1.932163450702`,
   `s_C(π/2) = 0.881917103688`, `d_0 = 4.5`, `d = 6` window `(2.645751311065, 2.738612787526)`,
   `R(E) = 0.252155813453`, margin `4.643×10^{−2}`, Gram deviation `3.553×10^{−15}` (the README's
   "certified to `3.6e−15`" is accurate), `deg K_C = 2hq^{−g/2}` for all listed isogeny classes.
6. **`s_C(γ_1,π/2)² = 7/9` exactly.** `cos θ_u = a/(2√q) = −1/(2√2)`, `sin²θ_u = 7/8`,
   `cosh²(log2/2) = 9/8`, ratio `7/9`; the `|n| ≥ 2` entries are `≤ 1/cosh(log 2) = 4/5 < √7/3`, as the
   document says. `d_0 = (q+1)²/((q−1)²+a²) = 9/2` re-derived. The closed forms are right.
7. **`K_C`, `κ_C`.** `k_0 = −(u+\bar u) = −a/√q`; `deg K_C = ξ_C(0)+ξ_C(1) = 2hq^{−g/2}` (Lemma D.41.1
   re-proved: `∏(q−α_i) = q^gP(1)`); `κ_C = (½,½,0,0)`, `I_∞^C(κ_C,κ_C) = ½`, and `½(F_1+F_2)` has the
   same pairings — so **`κ_C ≡ ½(F_1+F_2)`**, while `K_{C×C} = (2g−2)(F_1+F_2) = 0` for `g = 1`. The
   naming consequence the brief asks about is **upheld and is a real finding of the round**: the frame's
   `K` is a **polarization/ample class**, not a canonical class; the frame has no `h²`/Serre duality,
   only "vanishing in degree `≤ 0`" (the builder's MISMATCH 8, correctly assessed as not biting for the
   defect theorem).
8. **The central paradox is correctly resolved.** `h⁰_C` is defined on `Div(C×C)`, the frame's `(b′)`
   demands a representative in `𝓔_C` = nonnegative combinations of Frobenius graphs, and
   `𝓔_C ⊊ Eff(C×C)`. The separating class is right: every `E ≥ 0`, `E ≢ 0` has `Φ_E(0) = ΣE(n)q^{−n/2} > 0`,
   while `F_1·F_1 = 0`, so `F_1 ∉ 𝓔_C`; and `F_1` **is** in the image of the dictionary for this curve
   (script §[7]; see F5 for the one-line justification the document owes). **"Adding `F_1,F_2` does not
   change `σ`" is correct**: `σ` of a cone is the max over its generators (`|Σλ_iy_i|/Σλ_i\deg_i ≤ max`),
   and `F_1,F_2` have `y = 0`.
9. **`B4_C = 𝓔_C^∨`** is immediate from `t_n^C(E) = D_E·γ_n`; `𝓔_C ⊆ B4_C ⟺ κ(m) ≥ 0 ∀m ⟺ 2−2g ≥ 0
   ⟺ g ≤ 1` is correct (`N_m ≥ 0` always; only `m = 0` can fail).
10. **The three withdrawals are justified.** All three quotations opened and verified verbatim:
    `R144_004:93–98` ("`s₁ < 1` being the exact numerical signature of its absence"),
    `ROW-D-SYNTHESIS` §3(β) lines 48–52 ("the frame defect theorem will **fail** there"),
    `R142_003:111–115` ("One cannot 'run the refutation for a curve over `F_q`…'; the **absence of a
    function-field model of `D^W`** … O-23"). All three are genuinely falsified **as diagnoses** by
    D.41.13/D.41.14, whose mechanism I re-ran independently. O-23 is correctly **closed affirmatively**.
11. **Classical citations are accurate.** Hartshorne V.1.6 (RR for surfaces), V.1.8 (`D² > 0`, `D·H > 0`
    `⟹` `nD` effective for `n ≫ 0`), V.1.9 (Hodge index), Ex. V.1.9–V.1.10 (`C×C` and Weil's RH); Serre;
    Hindry–Silverman A.4. Labels `CLASSICAL` vs `PROVED` are used correctly throughout, and **no row-D
    label is claimed** — correct.
12. **Paper 46 Theorem 12.3 was transcribed faithfully.** I read the source (main.md:2701–2760). Clauses
    (a),(b′),(c), the `E' ≢ 0` requirement, Step 2's ampleness, Step 3's `(c)` at `E = nF`, and Step 4's
    degree gate are all reproduced correctly in D.41.14's three steps. Every step is valid on the
    lattice; the two properties Step 4 needs (`deg > 0` on the cone, `deg` constant on `𝓝`-cosets) are
    proved in D.41.9bis(i)/D.41.7.

---

## 3. MAJOR findings

### F1 (MAJOR) — `√7/3` is **not** "the" model constant; the optimal one is `√(7/11)`, and the witness is at `d = 3`

`s_C` is a function of **two** arguments `(γ,θ)`, and the defect theorem is free to choose `θ`: Lemma
D.31.4 / D.41.11 holds for every `θ`, and D.41.13 builds the witness in whatever direction it likes
(`F_0` with `(x,y) = (\cos φ, \sin φ)` for any `φ` exists, because `D^W_C → R^{2+2g}` is onto). The
round transcribed the arithmetic choice `θ = π/2` and then called the resulting number **the** model
constant, in the README ("`s_C = √7/3` exactly"), in the D.41.12 table, in D.41.17(iv) ("the ratio of
support functions is `s_C`") and in D.43. Recomputed independently:

    min_{θ} s_C(γ_1,θ) = √(7/11) = 0.797724562032…   at  tan θ* = 2/√7,  θ* = 0.647285896…  (and π−θ*),
    the sup being TIED at n = 0 and n = 1;
    d_0^* = 1/(1 − 7/11) = 11/4 = 2.75  EXACTLY;   minimal integer witness degree d = 3
    (window t ∈ (1.196586843, 1.224744871), non-empty — checked).

Closed form of the optimum (derivation: the tie `|\cos θ| = |\cos(θ_u+θ)|/\cosh(\tfrac12\log q)` gives
`\tan θ^* = (\cosh(\tfrac12\log q)+\cos θ_u)/\sin θ_u = (q+1+a)/\sqrt{4q−a^2}`):

    (s_C^*)^2 = \frac{4q − a^2}{(4q − a^2) + (q+1+a)^2}      [= 7/11 at q=2, a=−1 — verified numerically]

Three consequences, all of which must be repaired in the text:

* **(a)** The deficit of record is `1 − √(7/11) = 0.2023` (**131×** the arithmetic `1.5398×10^{−3}`), not
  `0.1181` / `76.7×`. The conclusion is *strengthened*, which is why this is MAJOR and not FATAL.
* **(b)** The comparison `s_C` vs `s_1` is apples-to-apples **only because** arithmetically the θ-optimum
  *is* `π/2`: on the line the nearest peak of `|\cos(γu+θ)|` sits at `|u| ≤ π/(2γ_1)`, maximised at
  `θ = π/2`, so `min_θ s(γ_1,θ) = s_1`. On the **lattice** the optimum moves off `π/2` because `n = 0`
  is a sample point. The document never says this, and it must, or the table is comparing an optimum
  with a non-optimum.
* **(c)** This is a genuine, unrecorded discreteness effect and should be **MISMATCH 11**: *the optimal
  direction `θ` of the sharp bound is `π/2` on the line and is not `π/2` on the lattice.*
* **(d)** Even at `θ = π/2` the witness degree `d = 6` is not minimal: `d_0 = 9/2` and `d = 5` already
  gives a non-empty window `(2.204792759, 2.236067977)`. "Witness at `d = 6`" is true but should be
  "`d = 5`" (or `d = 3` after the θ-optimisation).

**Required repair:** define `s_C(γ,θ)` everywhere with its `θ`; state `s_C(γ_1,π/2) = √7/3` as the
*transcription of the arithmetic choice*, `s_C^* = √(7/11)` as the *model's sharp constant*, give
`d_0^* = 11/4`, `d = 3`; correct the README's three lines and the D.41.12 table; add MISMATCH 11.

### F2 (MAJOR) — Theorem D.41.17(iii) `σ(\mathrm{Eff}) = ½` is proved only as `≥ ½`

The proof given is "`\overline{\mathrm{Eff}} ⊇ \overline{\mathrm{Pos}}` by Hartshorne V.1.8, hence
`σ(\mathrm{Eff}) = ½`". That yields `σ(\mathrm{Eff}) ≥ σ(\mathrm{Pos}) = ½` and nothing more. The
**upper** bound requires *every* effective class to satisfy `|y_D| ≤ ½\deg D`, which is **false in
general for classes with `D² < 0`** (the Hodge-index argument
`|y_D| ≤ \sqrt{(\tfrac12(\deg D)^2 − D^2)/2}` only gives `½\deg D` when `D² ≥ 0`), and `C×C` has plenty
of negative curves as soon as `g ≥ 2` (`Δ² = 2−2g`, `Γ_{q^n}² = q^n(2−2g)`). For the curve of record the
statement is true, but for a reason the document never gives: `E×E` is an **abelian surface**, where
every irreducible curve has `D² ≥ 0` and `\overline{\mathrm{Eff}} = \mathrm{Nef} = \overline{\mathrm{Pos}}`.
As written, the headline of the phase ("the analogue of `s₁` is `1`") is established only in the `g = 1`
case and by an uncited fact.

**Required repair:** either restrict D.41.17(ii)–(iv) to `g = 1` with the abelian-surface citation, or
prove `|y_D| ≤ ½\deg D` for effective `D` in general (I do not believe this is free). Related MINOR m2:
the script's §[6] comment "on the nef boundary, hence pseudo-effective …, hence in the SECTION cone" is
wrong twice — pseudo-effective is not "has a section", and V.1.8 needs `D² > 0`, not `D² = 0`. The
correct statement is that `σ(\mathrm{Eff})` is a **supremum over big classes, not attained**.

### F3 (MAJOR, and the finding that governs phase 146) — **(P145) clause 4 is RH restated, not a construction problem**

This is the brief's item 7, and the answer is negative. Paper 46 Theorem 12.3's proof (main.md:2724–2758)
uses the effective cone in exactly three places: Step 1–2 need `H' = F+2mK` to be **ample against the
cone** (`I_∞(E,H') > 0` for all `E` in it, via the bounded-density constant `C_F` of Theorem 11.14(ii)),
and Step 4 needs the **degree gate** `E' ∈ 𝔈, E' ≢ 0 ⟹ \deg E' > 0` (Theorem 11.13(i)). (P145) states
neither the degree gate nor the ampleness requirement, and once the degree gate is added:

> **Claim (proved here, frame-internal, no model input).** Clause 4 (`⟨D,D⟩ > 0, \deg D > 0 ⟹ D ∈ \bar𝔈`)
> together with the degree gate is **equivalent to RH**.
>
> *Proof.* (⟸) Under RH, `I_∞ ≤ 0` on primitives, so for `D ∈ \overline{\mathrm{Pos}}` with `\deg D = 0`
> one has `D` primitive and `D² ≥ 0`, hence `D² = 0` and `D ∈ 𝓝_∞`: the gate holds on `\overline{\mathrm{Pos}}`.
> (⟹) Suppose RH fails: some primitive `P ≢ 0` has `q := I_∞(P,P) > 0`. By Paper 46 Theorem 11.8,
> `I_∞(P,K) = ½\deg P = 0` and `I_∞(K,K) = ½`. Then for every `ε > 0`,
> `\deg(P+εK) = ε > 0` and `I_∞(P+εK,P+εK) = q + ε²/2 > 0`, so `P+εK ∈ \mathrm{Pos} ⊆ \bar𝔈` by clause 4;
> letting `ε ↓ 0` and using closedness, `P ∈ \bar𝔈` with `P ≢ 0` and `\deg P = 0` — the gate fails. ∎

So the enlarged-cone route is not an independent target: **(P145) as written is either trivially
satisfiable (take `𝔈` = everything: clauses 1–4 all hold, and only clause 5's falsifier requirement
blocks it) or equivalent to RH.** Two further defects of the statement:

* clause 4 concludes `D ∈ \overline{𝔈}` (closure), while `(b′)` needs an **actual** element of `𝔈`;
  Hartshorne V.1.8 gives `nD` effective, i.e. `D ∈ 𝔈⊗Q`, which is the correct form;
* enlarging `𝓔` to contain `\mathrm{Pos}` also puts Theorem 11.14(ii)'s `C_F < ∞` (Step 1's ampleness)
  in doubt — over `\mathrm{Pos}` that bound is itself a signature statement. (P145) must carry it as a
  clause.

**This does not retire the phase's naming result** — in geometry bigness is a *theorem* (RR + Serre
duality + ampleness), not an assumption, and Weil's proof is not circular. But it fixes what phase 146
may be asked to do. **Recommended restatement:**

> **(P145′).** Construct the *mechanism* that **proves** clause 4 — an arithmetic Riemann–Roch:
> a module with sheaf-like `H⁰`/`H²`, an `h²`-vanishing, and a `χ → ∞` argument — and state up front
> that clause 4 itself is **RH-equivalent** (proof above), so that the content of phase 146 is the
> mechanism and never the hypothesis. Add: (4a) `D²>0, \deg D>0 ⟹ D ∈ 𝔈⊗Q`; (4b) the degree gate
> `E ∈ 𝔈∖0 ⟹ \deg E > 0`; (4c) bounded density `C_F < ∞` over `𝔈`.

Accordingly: **(P145) as written is NOT the right target for phase 146; (P145′) is, and it is a strictly
harder-to-fake statement.** The builder's own negative — "clause 2 alone is insufficient" — is
**correct and I confirm it** (`F_1,F_2` have `y = 0`, so `\mathrm{Cone}(𝓔_C ∪ \{F_1,F_2\})` has the same
`σ`); it retires the obvious first attempt and is worth keeping verbatim.

### F4 (MAJOR, local) — D.41.9bis(ii)'s justification is false

"`C_F := \sup_n|w_F(n)|/(2\cosh(n\log q/2)) < ∞` (a sup of a sequence tending to `0`, hence attained)".
The sequence does **not** tend to `0`: `w_F(n)/(2\cosh(n\log q/2)) → Φ_F(0)` as `n → +∞` and `→ Φ_F(1)`
as `n → −∞` (the polar terms dominate; for `F = κ_C` the ratio is identically `½`). Finiteness — the
only thing used downstream — survives, but the parenthetical proof and the word "attained" are wrong and
the bracketed argument that follows it ("the difference of the two leading exponentials decays") is
incoherent. **Repair:** replace by `C_F ≤ |Φ_F(0)|+|Φ_F(1)|+Σ_i|Φ_F(1−ρ_i)| < ∞`, drop "attained".

### F5 (MAJOR, hypotheses) — D.41.7 needs "the `α_i` are pairwise distinct", and `F_1 ∈ V_C` needs a Tate rank count

* The proof of `\dim_R D^W_C/𝓝^C_∞ = 2+2g` runs "the characters `q^{±m/2}` and `\bar u_i^m` are pairwise
  distinct, hence independent". **That fails when `ξ_C` has a repeated zero** (supersingular curves and
  many `g ≥ 2` curves have repeated Weil numbers); then the dimension drops. The theorem is stated with
  no hypothesis. Add "`α_1,…,α_{2g}` pairwise distinct" (true for the curve of record: ordinary, `g=1`).
* D.41.17(v) and MISMATCH 6 assert `F_1, F_2 ∈ V_C`. What the script establishes is weaker: a class of
  `V_C` with the same pairings against every `γ_n` as `F_1`. `F_1 ∈ V_C` itself needs
  `\mathrm{rk}\,NS(C×C) = 2+2g`, i.e. (Tate) `\mathrm{rk\,End}(\mathrm{Jac}) = 2g`; for the ordinary
  `E/F_2` of record `NS(E×E)` has rank `2 + \mathrm{rk\,End}(E) = 4` — true, but it must be said, and the
  builder's own O-36 (supersingular: `\mathrm{rk}\,NS = 6 > 4`) shows they knew the issue and did not
  propagate it back into D.41.7/D.41.17(v). One sentence fixes both.

### F6 (MAJOR, notation) — MISMATCH 5 collides two different `K_C`'s

MISMATCH 5 writes `κ(0) = N_0 = 2−2g = χ_{\mathrm{top}}(C) = −\deg K_C`. In this very document
`\deg K_C = 2hq^{−g/2}` (Theorem D.41.8(ii)) — the *frame's* degree of the *frame's* `K_C`. The intended
reading is `\deg` of the curve's canonical divisor (`= 2g−2`), a different object with the same symbol.
As printed the identity is simply false in the document's own notation. Rename (e.g. `K_C^{\mathrm{geo}}`
or `ω_C`) in MISMATCH 5 and wherever `K_{C×C}` and `K_C` appear in the same paragraph.

---

## 4. MINOR findings

* **m1.** MISMATCH 7 says "all `11` isogeny classes of elliptic curves over `F_2` and `F_3`". The script
  prints **12** (`a = −2..2` over `F_2`: 5; `a = −3..3` over `F_3`: 7). Miscount.
* **m2.** Script §[6]'s comment (see F2): "nef boundary ⟹ pseudo-effective ⟹ in the SECTION cone" —
  two errors in one line. The printed *numbers* are unaffected.
* **m3.** "Witness at `d = 6`" is non-minimal (see F1(d)): `d = 5` at `θ = π/2`, `d = 3` at `θ = θ^*`.
* **m4.** MISMATCH 7's headline "`K_C ≥ 0` ⟺ `N_1 ≥ q+1`" is a **`g = 1`** statement (it is the sign of
  the single coefficient `k_0`). For `g ≥ 2` the `k_n` are elementary symmetric functions and no such
  equivalence is proved. Qualify.
* **m5.** The certified instance is `g = 1`, i.e. **the side of D.41.19(iii) on which `𝓔_C ⊆ B4_C` holds**,
  whereas arithmetically `𝓔 ⊄ B4` (`R143_001` Remark D.34.2). The model of record is therefore *not*
  faithful to the arithmetic trace-cone geometry; the document says so for `g ≥ 2` but the reader of the
  README will not see it. Add one line, or certify a `g = 2` instance.
* **m6.** The "`76.7×`" figure of the README and D.43 inherits F1; after repair it is `131×`, and it must
  carry the `θ`-qualifier either way.

---

## 5. Item-by-item answers to the audit brief

1. **The model (D.41.1–2).** Discrete carrier, Weil class, Laurent-series `Φ_E`, periodicity: correct and
   all consequences recorded (MISMATCH 2–4). Explicit formula: re-derived, correct. `I_∞^C`: correct.
   Dictionary: `Γ_{q^n}` for `n < 0` **is** the transpose and `Γ_0 = Δ`, as the brief supposed; the Gram
   `q^{−|a−b|/2}N_{|a−b|}` is forced, including the self-intersection convention `N_0 = 2−2g` (which is
   *derived* from `Γ_{q^n}² = q^n(2−2g)` and the half-density weight, not assumed).
   `D_E·F_1 = Φ_E(0)`, `D_E·F_2 = Φ_E(1)`. **The sign is `+`**, and it is consistent with the Hodge index
   in the right way: primitive `⟹ D² ≤ 0 ⟺ I_∞^C ≤ 0 ⟺` RH for `C`. Certification `3.6×10^{−15}`
   reproduced in FULL mode.
2. **`s_C`.** The curve, `a = −1`, `N_1 = 4`, ordinarity, `h = 4`, the formula `s_C² = (4q−a²)/(q+1)²`,
   the threshold `d_0 = (q+1)²/((q−1)²+a²) = 9/2`, and every step of D.31.4 → D.31.10 → D.31.12 on the
   lattice: **all valid**. `n = 0` is in the sample set and gives `s_C(γ,0) = 1`, as the brief expects;
   the `θ` actually used by the witness is `π/2` and it is used consistently. **But** `√7/3` is the
   `π/2` value, not the model's optimum — **F1**.
3. **The central claim and the paradox.** Correct, and correctly diagnosed. `σ(𝓔_C) = ½s_C` is right;
   `σ(\mathrm{Eff}) = ½` is only half-proved — **F2**. The separating class `F_1`, its non-membership in
   `𝓔_C`, its preimage, and the "rulings do not close the gap" negative: all confirmed.
4. **`K_C`.** `Φ_{K_C} = ξ_C`, `k_0 = −a/√q`, `K_C ≥ 0 ⟺ N_1 ≥ q+1` (`g = 1`), `\deg K_C = 2hq^{−g/2}`
   with `h = P(1) = \#\mathrm{Pic}^0(C)(F_q)`, `κ_C ≡ ½(F_1+F_2)`: all verified. The naming consequence —
   **the frame's `K` is the polarization, not the canonical class** — is correct and is one of the
   round's better findings; notation collision at MISMATCH 5 — **F6**.
5. **`B4_C = 𝓔_C^∨`, `𝓔_C ⊆ B4_C ⟺ g ≤ 1`.** Verified.
6. **Axioms and withdrawals.** The A1–A9 pass with the A4 edit is fair; MISMATCH 1 (elementary factors)
   and MISMATCH 5 (no archimedean place) are correctly identified as the two that bite, and MISMATCH 5 is
   correctly flagged as **the boundary of the model's authority** (Paper 46 open item (21) gets no
   guidance). The three withdrawals are justified and accurately quoted.
7. **D.42 / (P145).** The *name* is right: "the divisor group of the surface — rulings as effective
   generators, plus bigness (Hartshorne V.1.8)" is exactly what separates `𝓔_C` from `Eff(C×C)`, and the
   proof that clause 2 alone is insufficient is **correct**. Clause 4 is **not** well-posed as a
   construction problem — **F3**: it is RH restated once the degree gate that Theorem 12.3 Step 4 needs is
   supplied, it is trivially satisfiable without it, and it omits the ampleness/`C_F` requirement. A
   "12.3-`𝔈`" transfer therefore *can* exist only in the sense `RH ⟹ RH`. T1/T2 and the falsifiers are
   respected by the statement as written (clause 5 does the work), but clause 5 is also the only thing
   preventing the trivial solution, which is a sign the problem is mis-scoped.
8. **Labels / corpus / README / paper-facing.** `CLASSICAL` vs `PROVED` correct; no label claimed; the
   corpus-check table is honest and every reuse instruction was honoured (phase-125 gap closed,
   phase-113 doc 11 read and correctly summarised, CC not over-attributed, the stale phase-41 citation
   not leaned on, option α not opened). README must move with F1/F2/m1.

---

## 6. Acceptance test and the phase-146 recommendation

**Did the phase meet its acceptance test ("names the ingredient, precisely enough to scope phase 146")?
YES, with one qualification.** `[X]`, `[Y]`, `[Z]` are named concretely, the separating feature is
identified (prime divisors exist because the Frobenius correspondence is a genuine morphism of a genuine
surface; hence rulings, hence bigness), the placement against `113_11`'s Target T1 is exact and honest,
and the refutation of the prediction of record is a real and useful negative that no other route
produced. The phase also delivered something the blueprint did not ask for and that is worth more than
the prediction: **`s < 1` is a property of the cone and carries no information about zeros** — this
retires a diagnosis that three corpus documents were resting on.

**The qualification, and the recommendation for phase 146.** The named ingredient's operative half —
bigness — is, on the arithmetic side, *equivalent to RH* (F3). Phase 146 must therefore **not** be given
(P145) as written. Two defensible options:

* **(β′)** take **(P145′)** above — build the *mechanism* (an arithmetic Riemann–Roch with `h²`-vanishing
  and a `χ → ∞` argument), with the RH-equivalence of clause 4 stated in the blueprint so that no round
  can mistake assuming it for proving it, and with clauses (4a),(4b),(4c) added; or
* **(α)** proceed to option α as the owner originally scheduled, now informed by the model's translation
  (`J` = the intersection form of a **larger** `NS` in which `P^W` acquires more negative directions),
  and keep (P145′) as the standing statement of what α's positivity must deliver.

My recommendation, hostilely: **α (as scheduled), with (P145′) recorded as the target-of-record and the
RH-equivalence of clause 4 printed in the phase-146 blueprint.** Handing 146 a problem that is RH in
disguise, unlabelled, is the one way this phase's real result could do harm.

**Repairs required before confirmation:** F1 (with new MISMATCH 11), F2, F3 (restate (P145) as (P145′)
and add the equivalence proof), F4, F5, F6, and m1–m6. None of them touches the two headline claims.
