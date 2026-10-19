# R132.002 — audit of record, row C, phase 132 round 1

Target:
[Paper 45](../../04-papers/45-row-c-explicit-formula/main.md) as rebuilt in
round 1 (1763 lines, every `[REBUILT, phase 132, round 1]` passage read), the
round-1 record [R132.001](R132_001_ROUND1.md), the blueprint
[R132.000](R132_000_BLUEPRINT.md) and its supplement, and the audit that
withdrew the old label, [D128.003](../phase-128-adversarial-audit/D128_003_AUDIT_C.md).

Method: every load-bearing statement was **re-derived**, not re-read.  Every
citation to Paper 43 and Paper 44 named in the brief was opened and checked
against the cited theorem's own text and hypotheses.
`scripts/verify_132_explicit_formula.py` was run: **22/22 pass**, reproduced
here (explicit formula to `3·10^{-15}` at 100 zeros; `A(s)+A(1-s)` to
`3.9·10^{-31}`; chart residue `6.000` at `|S_f| = 5`; `Res_{s=0}A = 1.000`;
`(5j)` to `1.4·10^{-9}` at 200 zeros).

**Headline.** The mathematics is right.  Theorem 9.4 is a correct, complete,
repository proof of the Weil explicit formula — I re-derived every line of it
independently and the signs, the factor 2, the reflection-first order and the
per-prime shift all check.  Theorem 9.6, Theorem 10.4 (with the `C10` fix) and
Theorem 12.2 are correct as stated.  Eight of D128's ten findings are
genuinely disposed of.  But **the label is not grantable as the paper
stands**: four `MAJOR` findings, none of them requiring new mathematics.  The
gravest is that **D128 `C9` is not disposed of — it is relocated and
understated**: the comparison theorem (9.9)–(9.10), and therefore §14.4's
"row D's target implies RH", are true *only* for the declared constant
`c := 0`, and §14.4 says in terms that "nothing in row C depends on"
`c_cut`.  That sentence is false, and the repair is available and is in fact
a strengthening (§3, `M1`).

Grade: **`WEIL-STRENGTH-COMPLETE` — EARNED WITH REPAIRS** (M1–M4), not
granted in this round.  §8 states what must be recorded beside the label.

---

## 1. What survives, re-derived

I re-derived the following from scratch; these are the load-bearing facts and
they hold.

**(a) Theorem 9.4 (the explicit formula).**  With `g(s) = Φ_F(s)Φ_F(1-s)`,
`F` real `C_c^∞`:

* `g` entire, `g(1-s) = g(s)`, `g(½+iτ) = |\hat F(τ)|²`, `Φ_h = g` for
  `h = F⋆F^†` — verified, including `Φ_{F^†}(s) = Φ_F(1-s)` for real `F`.
* (9.1): integrating by parts `N` times gives
  `Φ_F(s) = (-1)^N(s-½)^{-N}∫F^{(N)}(t)e^{(s-½)t}dt`, hence the bound with
  `C_N = ‖F^{(N)}‖_{L^1}`.  Correct.
* Lemma 9.2: `ξ'/ξ` is regular at `s = 0` and `s = 1` (`ξ(0) = ξ(1) ≠ 0`), so
  the only poles of `g·ξ'/ξ` in the rectangle are the zeros; horizontal sides
  are `O(X_j^{-4}\log^2X_j)`; the verticals converge absolutely.  Correct.
  **Except for the derivation of (E3) — see `M2`.**
* Lemma 9.3: the substitution `s = 1-u` and `g(1-u) = g(u)` give (9.4); with
  `(ξ'/ξ)(1-s) = -(ξ'/ξ)(s)` this gives (9.5), hence (9.7),
  `Σ_ρ g(ρ) = (1/πi)∫_{L_c}g\,ξ'/ξ`.  Correct.
* (9.8): `ξ'/ξ = 1/s + 1/(s-1) - ½\log π + ½ψ(s/2) + ζ'/ζ`.  I checked the
  pole bookkeeping: `A_0`'s `1/s` is cancelled by `½ψ(s/2) ∼ -1/s` and
  `A_0`'s `1/(s-1)` by `ζ'/ζ ∼ -1/(s-1)`, consistent with `ξ'/ξ` being
  regular at `0,1`.  Each summand is integrable against `g` on `L_c`.
* (a) polar: `A_0(1-s) = -A_0(s)`, so `(1/πi)∫_{L_c}gA_0 =
  (1/2πi)[∫_{L_c}-∫_{L_{1-c}}]gA_0 = g(0)+g(1) = 2Φ_F(0)Φ_F(1)`.  Correct.
* (b) Gamma: shift to `L_{1/2}` (no pole of `ψ(s/2)` in `½ ≤ Re s ≤ c`),
  `(1/πi)∫_{L_{1/2}} = 2·(1/2π)∫_R g(½+iτ)[-½\log π+½ψ(¼+iτ/2)]dτ`, and the
  odd imaginary part drops by evenness of `|\hat F|²`, giving
  `(1/2π)∫|\hat F|²[Re ψ(¼+iτ/2) - \log π]dτ`.  Correct.
* (c) primes: Fubini on `L_c`, then `g(s)n^{-s}` **entire** (this is the
  point D128 `C4` broke and it is now genuinely legitimate — `ζ'/ζ` has been
  expanded away before the shift), shift to `L_{1/2}`, giving
  `(1/πi)∫g n^{-s}ds = 2n^{-1/2}h(-\log n)`, and `h` even (because `F` is
  real) turns `2h(-\log n)` into `h(\log n)+h(-\log n)`.  Correct, and the
  R132.001's "factor of 2" refutation of the blueprint is right: the single
  line gives exactly half, and the other half is the `L_{1-c}` line.
* Sum: (9.6).  This is the classical Weil explicit formula with the standard
  signs.  **`PROVED`, and the proof is in the repository.**  Clause C.8 is met
  in its strong form.

**(b) The imports, checked one by one.**  Functional equation and Hadamard
order (E2, E3) — used only through `ξ`'s zero set and the `O(\log^2)` bound;
Euler product (E1) — only on `Re s > 1`, only for Fubini; Stirling/digamma
(E4); Fourier inversion (E5).  No spectral realization, no Meyer, no cutoff
theorem.  I confirm §11's "not used anywhere" list by grep.

**(c) Theorem 9.6.**  Adding `2Φ_F(0)Φ_F(1)` to (9.6) and using
`T_∞(Γ_h) = ΣΛ(n)n^{-1/2}[h(\log n)+h(-\log n)] + (1/2π)∫|\hat F|²[\log π -
Re ψ(¼+iτ/2)]dτ` gives `T_∞(Γ_h) = 2Φ_F(0)Φ_F(1) - Σ_ρ g(ρ)` — arithmetically
exact, and the script confirms it to `1.4·10^{-9}` at 200 zeros.  The chart
clause and the window `R(Γ_h) < \log ℓ_{next}(S)` are Paper 43 Theorem
8A.7c(a),(b),(e) verbatim; I opened 8A.7c and it says exactly that.  **True.**
Its citation of the trace evaluation is defective — `M4`.

**(d) Signs, all three conventions.**  `q = -B_nuc` (P123.036), Paper 43
(14.1) with `c := 0`, Paper 44 (8bis.14a),(8bis.14e) `I_∂ = -Q`.  I checked
(8bis.14a) `Q(g) = Σ_ρ\hat g(ρ)\overline{\hat g(1-\barρ)}` with
`\hat g = Φ_g`, and the reality reduction `Q(F) = Σ_ρΦ_F(ρ)Φ_F(1-ρ)`.
Lemma 1.3 is correct, and its three legs agree with the script's (5i),(5j).
**No sign error anywhere in the paper.**

**(e) Theorem 10.4 and the `C10` fix.**  Verified against `106_11` directly.
Lemma 10.1: `Φ_{ΠG} = (¼-(s-½)²)Φ_G = s(1-s)Φ_G`, `= ¼+τ² > 0` on the line.
Corollary 10.2: primitivity, support, parity, injectivity by analyticity.
The quartet bookkeeping matches `106_11` (8),(11): with `z = (ρ-½)/i`,
`Φ_F(ρ)Φ_F(1-ρ) = F(z)F(-z) = ±F(z)² = \overline{F(\bar z)}F(z)`.
`ρ(1-ρ) = ¼+z² ≠ 0` at a nontrivial zero.  **Flag `P3` is disposed**
— see `n2`.

**(f) Theorem 12.2.**  `\widehat{Γ_h}` is carried by `𝔠_0` and equals
`\hat h(-τ)` there; `\hat T_S` is even on `𝔠_0` (`θ_p = 0`); `m = \hat h\hat
T_S` is tempered (Schwartz × logarithmic growth, Paper 43 Thm 9.7(a),(b));
`\{\hat g\}` dense in `𝒮`; `\hat T_S(𝔠_0,·)` real-analytic and not identically
zero.  Hence `\hat h ≡ 0`.  **Correct.**  Surjectivity of `M` on the radial
sector is genuinely available: Paper 43 Theorem 9.1's own surjectivity proof
runs through "the radial push-forward of `F` at the two points `s = ∓½`", so
it is a statement about exactly this sector.

**(g) The refutations of the blueprint.**  All five checked, all right.
(i) `M(Γ_F) = (λ_-,λ_+) = (Φ_F(1),Φ_F(0))` by Paper 44 Lemma 3bis.6a
`λ_∓(Γ_h) = ∫h(s)e^{±s/2}ds` — the blueprint's `z(F) = M(Γ_F)` is false, the
swap is right, `β_T` is swap-invariant, and the ruling relabelling is
consistent with Paper 44 Thm 3ter.14's `M(Frob_n) = (n^{1/2},n^{-1/2})` (which
I checked is `(λ_-,λ_+)` in that order, and agrees with a profile atom at
`t = \log n`).  (ii) factor 2: right (§1(a)).  (iii) `\log π`: right — applied
to the entire symmetric summand `-½\log π`, the bracket
`[∫_{L_c}-∫_{L_{1-c}}]` annihilates it by (9.4), so the reflection must be
applied **first**; the paper does so.  (iv) composite vanishing: right —
Paper 44 Thm 3bis.7 carries `Λ(n) = 0` for composite `n` ("no single place has
a shell of modulus `1/n`") for the **radial** family, while Thm 3ter.12 is a
**support** statement about `Frob_n`; the paper's Cor. 5.2 keeps them apart and
says so.  (v) the profile sign `\widehat{Γ_h}(τ) = \hat h(-τ)`: right, and
harmless by evenness, which the paper proves rather than assumes.

**(h) The five consistency tables.**  Checked entry by entry against the
cited sources: `\hat W_∞(0,τ) = \log π - Reψ(¼+iτ/2)` = Paper 43 Thm 9.7(b) =
P123.035 (4.1) ✔; `\log π - ψ(¼) ≈ 5.372` = Paper 43 (14.2) ✔ (and (14.2) is
indeed the value **at** `𝔠_0, τ = 0`, bounding `m` from below, which is the
direction Thm 12.2 needs — flag `P4` is moot, see `n3`);
`γ+\log4π+ψ(½) = \log π` ✔; `K(t) = ¼[1/\sinh(t/2)+1/\cosh(t/2)]` = Paper 43
(8.5∞) ✔; `K(\log n) = n^{3/2}/(n²-1)` = Paper 44 (3bis.11) ✔;
`d^*x_∞ = dx/(2|x|)` = Paper 43 (8.5b) ✔; `vol(Z_p^×) = \log p` = Paper 44
Thm 8bis.8 (a genuine uniqueness theorem, not a stipulation) ✔;
`dχ|_{𝔠_0} = dτ/2π` = Paper 43 Thm 9.7b(d) ✔; `Φ_F(½+iτ) = \hat F(-τ)` ✔;
Paper 44 (8bis.14a)'s `\hat g(s) = Φ_g(s)` ✔.  The archimedean Tate residue
(Thm 7.5) is correct: `a(s) = 1/s+O(1)` at `0`, residue transport `r ↦ -ir`
gives `-i` at `τ = i/2`, matching Paper 43 Thm 9.7b(b); and
`ζ_∞(s) = ∫_{|x|≤1}|x|^s dx/(2|x|) = 1/s` ✔.  Lemma 9bis.1(i) checks against
Paper 43 (9.11): `ζ_p = p^{-(1-s)}` on `𝔠_0` and
`(\log p)ζ_p/(1-ζ_p) = f_p(1-s)`, `2Re(\cdot) = f_p(s)+f_p(1-s)` ✔, and
`Res_{s=0}T̂_S = |S_f|+1 ↔ Res_{τ=i/2} = -i(|S_f|+1)` = Paper 43 (9.7b.3) ✔.

---

## 2. Disposition of D128 `C1`–`C10`

| # | D128 finding | disposition in round 1 | my verdict |
|---|---|---|---|
| `C1` | Thm 5.4 argues from a contradiction | withdrawn a second time **with its referent**: `C_S` is a group, no `Z_J`, no corner strata (W45.1); replaced by Thm 5.1/Cor 5.2 | **DISPOSED.**  Not a relabelling: the object is gone and the replacement is a theorem of Paper 44 |
| `C2` | no localization of `χ_A` along the filtration | moot — `χ_A` and the filtration do not exist on the declared carrier; §5.1 says row C claims no localization | **DISPOSED** as a claim.  The underlying question is not answered, it is **declined**, and the paper says so in those words.  Acceptable, because no clause of C asserts it |
| `C3` | additivity over places inherited from a definition | §5.1 + W45.3: `T := Σ_vW_v` is row A's **declared** trace; row C proves statements about it and claims nothing more | **ACKNOWLEDGED, not refuted** — correctly.  Place-additivity is still definitional.  §14.2's C.3 row does say "as a theorem about row A's declared trace, and stated as such".  This is the honest disposal and it passes the renaming test (§6) |
| `C4` | the contour step is invalid | **Theorem 9.4**, proved here, with the illegitimate shift removed | **DISPOSED, and upgraded.**  This is the paper's real achievement |
| `C5` | `det_ζ` overclaim | honesty clause carried verbatim into §7.1; `N_Γ` "defined by its spectrum"; the slogan struck and not restated (grep confirms) | **DISPOSED** |
| `C6` | half-density archimedean only in a gauge | W45.4 + Thm 4.1: both factors are local data of the same finite place | **DISPOSED, and the old claim refuted** |
| `C7` | Thm 6.1 a normalization-compatibility lemma | replaced by Paper 44 Thm 8bis.8 (uniqueness given a universal Tate residue); Cor. 6.2 states the negative half as strongly as the positive | **DISPOSED, and strengthened** |
| `C8` | "compact section" citation wrong | object gone; `Γ_h ∈ D_A^{rad}` is literal membership | **DISPOSED** |
| `C9` | the `f(1)` counterterm; `I_A` defined modulo `R·‖·‖²`; "for a sign statement that is not harmless" | `c := 0` declared (Paper 43 Def 8A.7d) and carried as a hypothesis; `c_cut` recorded in §14.4 as "an open comparison item this paper does not inherit and does not close ... nothing in row C depends on it" | **NOT DISPOSED — `M1`.**  Relocated and understated |
| `C10` | six minor items | all six carried out: Def. 9.2 (W45.13), `F` real as standing hypothesis, symmetric order, (10.1) replaces the `a_N,b_N` rescaling, injectivity by analyticity, imports listed | **DISPOSED**, item by item, verified by grep |

---

## 3. `MAJOR` findings

### `M1` — D128 `C9` is not disposed of; §14.4's disclaimer is false as written

**Location.** §14.4, final paragraph ("nothing in row C depends on it");
§14.2 rows C.3, C.6; Theorem 9.6; §1.2 (1.2).

**Error.** By Paper 43 (9.13)/(14.1), `I_A(F,F) = ∫_{Ĉ_S}|\hat F|²(\hat T+c)dχ`,
so a nonzero constant `c` adds `c·‖Γ_F‖_{L²}²` to `I_A(Γ_F,Γ_F)` — and this
term does **not** vanish on the primitive sector (`M(Γ_F) = 0` kills the
*polar* packet, not the `L²` norm).  Hence (9.9), (9.10),
`I_∞ = -Q = B_{nuc}` and §14.4 item 4 ("row D's target therefore implies RH,
unconditionally") are all statements about the trace **with `c := 0`**, and
they are false for any other admissible normalization.  Paper 43 Def. 8A.7d
is explicit that `c := 0` is a **declaration**, that "none of [the four
reasons] is a derivation", and Remark 8A.7e records that the attempt to
compute the comparison constant `c_cut` "does not close".  D128 `C9` said
precisely this and said why it matters.  The paper carries `c := 0` as a
hypothesis everywhere — which is correct and is the main part of the repair —
but then tells row D that the open item is irrelevant.  It is not irrelevant:
it is the single normalization on which the whole chain to RH rests.

**Repair (and it is a strengthening, not a retreat).**  Two sentences and one
corollary.

1. Replace "nothing in row C depends on it" by: *every theorem of §§9, 9bis,
   10, 12 is a theorem about the trace with `c := 0`; for any other constant
   `c`, (9.9) reads `I_∞(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) - Σ_ρΦ_F(ρ)Φ_F(1-ρ) +
   c‖Γ_F‖²`, and the equivalence with Weil's criterion fails.  The declaration
   `c := 0` is therefore load-bearing for row D's target.*
2. Add **Corollary 9.6a**: *`c = 0` is the **unique** real constant for which
   `I_∞(Γ_F,Γ_F) = B_{nuc}(F,F)` for all real `F ∈ C_c^∞(R)`* — immediate from
   Theorem 9.6 and `‖Γ_F‖² > 0`.  This converts Paper 43's declaration into a
   **determination relative to the Weil comparison**, and closes D128 `C9` in
   the only form in which it can be closed: not by computing `c_cut`, but by
   proving that the comparison itself pins the constant.  The script's checks
   (1) and (5j) already verify it numerically to `10^{-9}`.

With that corollary the finding is fully answered and row C becomes *stronger*
than it now claims.

### `M2` — the import (E3) is mislabelled as a derivation

**Location.** §9.1 bullet (E3) ("consequently, for each `j` there is `X_j` …";
"`(ξ'/ξ)(σ±iX_j) = O(\log^2X_j)`"); §11 table row E3; Lemma 9.2's proof.

**Error.** Neither consequence follows from `N(T) = O(T\log T)`.  A bound on
`N(T)` says nothing about `N(j+1) - N(j)`; the gap statement requires the
**local** density `N(T+1) - N(T) = O(\log T)`, and the `O(\log^2 X)` bound on
`ξ'/ξ` requires in addition the Hadamard partial fraction
`ξ'/ξ(s) = Σ_ρ 1/(s-ρ) + B` together with that local density (Titchmarsh
§9.6).  Under clause C.8 in its strong form — "every analytic input is either
proved here or named" — presenting a strictly stronger classical input as a
"consequence" of a weaker one is exactly the failure mode the clause exists to
prevent.  The statement is of course true; the ledger is wrong.

**Repair.** Split (E3) into (E3a) `ξ` of order 1 with the Hadamard partial
fraction; (E3b) `N(T+1) - N(T) = O(\log T)` (Riemann–von Mangoldt, local
form); (E3c) the resulting `ξ'/ξ(σ±iX_j) = O(\log^2 X_j)` on ordinate-avoiding
heights, labelled `CLASSICAL` and cited, not derived.  Keep
`N(T) = O(T\log T)` as the separate input used by Thm 10.4(iii).  Update the
§11 table and §9.6 row 7.

### `M3` — Theorem 9bis.2 is a misnomer, and it is the weakest form of the true statement; clause C.4's polar half is discharged by a renaming plus a negative

**Location.** §0.1 item (3); §9bis title; Theorem 9bis.2(ii); Cor. 9bis.3;
Thm 9bis.4(i); §14.2 row C.4.

**Error, in three parts.**

1. *The name.*  `T̂_∞^{mer}(s) := A(s)+A(1-s)` is **not** the symbol of the
   colimit trace `T_∞`.  `T_∞` is defined by a finite sum at each test
   (Paper 43 Thm 8A.7c(b)) and its Fourier side is not a function (Thm 9.6′).
   `A(s)` is the analytic continuation from `Re s > 1` of the *formal* prime
   sum, and `A_S(½+iτ) → ∞` on the critical line, so `A` is not any limit of
   the chart symbols where the symbols live.  Calling it "the meromorphic
   symbol of the colimit trace" and headlining it as item (3) of §0.1 invites
   exactly the reading that Cor. 9bis.3 then has to forbid.  R132.001
   flagged this himself (`P1`); I confirm the flag and I do not accept his own
   answer that "the rhetoric is the weakest point": §14.2's clause C.4 row
   cites **Theorem 9bis.2** as the discharge of "poles in the same
   comparison", so the rhetoric is load-bearing.
2. *The content.*  `A(s)+A(1-s) ≡ 0` is a one-line restatement of the
   functional equation: `A = -ξ'/ξ + 1/s + 1/(s-1)` and
   `(ξ'/ξ)(1-s) = -(ξ'/ξ)(s)` make the cancellation formal.  It says nothing
   about any trace, and as a "reconciliation" of the chart residue it says
   only that both sides of a cancelling pair vanish.
3. *What the paper missed, and its own script found.*  The informative
   statement is **one-sided**: since `ζ'/ζ` is regular at `s = 0`,

       Res_{s=0} A_S(s) = |S_f| + 1     but     Res_{s=0} A(s) = 1 ,

   and that residual `1` is exactly the `1/s` of the trivial factor `½s(s-1)`
   of `ξ` — i.e. exactly the term whose rectangle residue is `g(0)`, half the
   polar packet `2Φ_F(0)Φ_F(1) = β_T(M,M)`.  *In the colimit the `|S_f|` finite
   Tate residues disappear and the single archimedean residue survives as the
   polar packet.*  That **is** "the poles in the same comparison", it is a
   theorem, and the paper's own script prints it (check (3d):
   `Res_{s=0}A(s) = 1.000`) without the paper stating it.  Instead
   Thm 9bis.4(i) declares that the two numbers "are not to be reconciled".

**Repair.** (i) Rename `T̂_∞^{mer}` to something that does not say "symbol of
the colimit trace" — e.g. `Ξ(s) := A(s)+A(1-s)`, "the reflected continuation
of the formal Euler symbol" — and demote Theorem 9bis.2(ii) to a corollary of
the functional equation.  (ii) Promote to the headline of §9bis the one-sided
statement **Theorem 9bis.2′**: `Res_{s=0}A_S = |S_f|+1`, `Res_{s=0}A = 1 =
Res_{s=0}(1/s)`, and this residue is the polar packet of Theorem 9.4(a) via
Theorem 8.1(i).  (iii) Rewrite §0.1 item (3) and the §14.2 C.4 row around
Theorem 7.5 + Lemma 9bis.1 + 9bis.2′, which are the three statements with
content.  After that repair clause C.4 is discharged by theorems; before it,
it is discharged by a definition (`T̂_∞^{mer} :=`) plus a negative, which is
D128 `C3`'s failure mode in a new place.

### `M4` — the central theorem cites its main input outside that input's hypotheses

**Location.** Theorem 9.6's proof, line "By Paper 44 Theorem 3bis.7 …
together with (1.2)'s regularized `W_∞` when `0 ∈ supp h`"; identically in
Lemma 1.3's proof (S1) and implicitly in Theorem 9.6′.

**Error.** Paper 44 Theorem 3bis.7 is stated **for `h ∈ C_c^∞(R)` with
`0 ∉ supp h`**, and its proof begins "By Lemma 3bis.6a, `Γ_h ∈ D_A^0`, so
Paper 43 Theorem 8.8 applies".  In Theorem 9.6 the test is `h = F⋆F^†`, for
which `h(0) = ‖F‖_{L²}² > 0` **always**, so `0 ∈ supp h` in every application
of the theorem.  Paper 45's own Theorem 5.1 restates the hypothesis
`0 ∉ supp h` correctly and is then used in a case it excludes.  The
parenthesis "use (1.2)'s regularized `W_∞`" is a gesture, not a citation:
neither Paper 44 nor Paper 45 states the `0 ∈ supp h` version anywhere, and
the naive archimedean integral `∫K(|t|)h(t)dt` **diverges** at `t = 0`
(`K(t) ∼ 1/(2t)`), so the displayed identity is not obtained from (5.1) by
continuity either.

**The statement is nevertheless true**, and the repair is two citations:

* the **finite** places: `W_p(Γ_h)` is the shell sum for every
  `h ∈ C_c^∞(R)` without support restriction, because on a radial class the
  regularized unit packet of (8.5) is `(\log p)∫_{Z_p^×}(a(u)-a(1))/|1-u|_p du`
  with `a ≡ h(0)` constant, hence **identically zero** — which is exactly the
  step the paper's own §9.6 row 2 asserts ("vanishes identically on radial
  classes, pointwise, with no smallness hypothesis", Paper 44 Thm 3bis.7 proof
  step (1));
* the **archimedean** place: `W_∞(Γ_h) = (1/2π)∫\hat h(-τ)\hat W_∞(0,τ)dτ` by
  Paper 43 Theorem 9.7(d)/(9.13), which holds **for every `H ∈ D_A`**, with no
  support hypothesis at all.

**Repair.** Insert **Lemma 5.1a** ("the radial trace, without a support
hypothesis"): *for every `h ∈ C_c^∞(R)` and `c := 0`,
`T(Γ_h) = Σ_{p∈S_f}Σ_{k≥1}(\log p)p^{-k/2}[h(k\log p)+h(-k\log p)] +
(1/2π)∫\hat h(-τ)\hat W_∞(0,τ)dτ`*, proved by the two citations above, and
route Lemma 1.3, Theorem 9.6 and Theorem 9.6′ through it.  Until that lemma
exists, the paper's central theorem rests on a citation its source forbids.

---

## 4. `MINOR`

* **`m1` (Thm 9.6′).**  "the linear functional `|\hat F|² ↦ …`" — the domain
  is the **cone** `\{|\hat F|² : F ∈ C_c^∞ \text{ real}\}`, not a vector
  space, so linearity is not established; and no continuity in any topology is
  proved, so the word "distribution" (blueprint §2.1) is not earned.  *Repair:*
  state Theorem 9.4 for arbitrary **real even** `h ∈ C_c^∞(R)` with
  `g := Φ_h` — the proof is verbatim, since `g(1-s) = g(s)` is exactly
  evenness of `h` and `g(½+iτ) = \hat h(τ)` is real but no longer `≥ 0`, which
  no step uses except the cosmetic `|\hat F|²`.  Then (9.11) is a genuine
  linear functional on `C_c^∞(R)^{even}`.  Say explicitly that continuity is
  **not** claimed.
* **`m2` (Thm 10.4(iii)).**  The tail mechanism is misdescribed.  Paper 45
  says `Φ^N` must "beat `(1+|Im ρ|)^{-4}` … once `N` is enlarged by a fixed
  amount".  `106_11`'s tail bound (27)–(30) carries a **fixed degree `D`
  larger than the degrees of the polynomial factors** and a global factor
  `4^{-(N-N_0)}`; the extra factor `|ρ(1-ρ)|²` is absorbed by taking
  `D ↦ D+2`, and (29) still converges by the rapid strip decay (15) and (28).
  Enlarging `N` is not what does the work.  Conclusion unaffected.
* **`m3` (banner vs §0.2 vs §10).**  The banner claims no statement about the
  location of a zero "outside the comparison theorem (section 9.5)"; §0.2 says
  "outside §9.5 **and §10**"; and §10's Theorem 10.4 does reason from a
  hypothetical off-line zero `ρ_0`.  Align the banner with §0.2.
* **`m4` (Lemma 9.2).**  "on `L_c`, `ξ'/ξ` is bounded" — it is `O(\log|s|)`,
  as the same sentence's parenthesis says.  Harmless; fix the word.
* **`m5` (§14.3).**  "*The three items Paper 43 §14.1a hands to row C*" is
  followed by **five** bullets, and Paper 43 §14.1a does not contain that list
  (the three-item handoff is §14's item 5 plus §14.0a).  Fix the pointer and
  the count.
* **`m6` (ordering).**  Lemma 1.3's leg (S3) uses Theorem 9.4, and Theorem
  9.6's proof uses Lemma 1.3.  There is **no circularity** (Thm 9.4 uses only
  (E1)–(E5); the leg of Lemma 1.3 that 9.6 uses is (S1), which uses Paper 43
  Thm 9.7(b),(d) only), but a reader cannot see that.  State the dependency at
  Lemma 1.3.
* **`m7` (notation inherited).**  Paper 43 (8.5∞) writes the counterterm as
  `(γ+\log4π)b(1)` with `b` "in the logarithmic coordinate", where the
  identity is `t = 0`; §9.6 row 6 of Paper 45 repeats `2b(1)e^{-t/2}`.  The
  bracket is `O(t)` as claimed (I checked: `[b(t)-b(0)]+[b(-t)-b(0)] +
  2b(0)(1-e^{-t/2}) = O(t)`), but the argument of `b` should be `0`.

---

## 5. `NOTE`

* **`n1`.**  For `F ∈ C_c^∞` the zero sum is **absolutely** convergent:
  `|g(ρ)| ≤ C_N|γ_ρ|^{-2N}` on the strip by (9.2), and `N(T) = O(T\log T)`
  makes `Σ_ρ|γ_ρ|^{-4} < ∞`.  D128 `C10`'s symmetric-order requirement is
  therefore harmless but unnecessary for this test class; saying so is
  stronger and removes an apparent fragility from (9.9), (9.11) and §14.4.
* **`n2` (flag `P3`, resolved against R132.001's worry).**  I
  traced `106_11` myself.  Its (9) fixes `s_0 = x_0+iy_0` with
  **`x_0y_0 ≠ 0`**, glossing `y_0 ≠ 0` as "exactly the failure of the
  critical-line condition" and `x_0 ≠ 0` as "the classical absence of real
  nontrivial zeros `ρ∈(0,1)`" — i.e. the variable is `z = (ρ-½)/i`, the
  critical line is `Im z = 0` and a real zero is `Re z = 0`, exactly as
  Paper 45 (10.1) reads it.  Its (20) states `Im w_0 = 2x_0y_0 ≠ 0` for
  `w_0 = s_0²` and (21) concludes the `R²→C` isomorphism.  **`s_0² ∉ R` is
  established by `106_11` itself; no degenerate case needs excluding by hand,
  and Paper 45's (10.1) is a faithful rendering.**  The `C10` fix is complete.
* **`n3` (flag `P4`, moot).**  Theorem 12.2 does not need Paper 43
  (14.2) at all: Theorem 9.7(c) states outright that `T̂+c` "vanishes
  identically on **no** component" and has discrete zero set on each.  (14.2)
  is indeed a lower bound for `m := \sup_{Ĉ_S}T̂` **by the value at `𝔠_0,
  τ = 0`**, so the direction is right, and the extra remark that every
  finite-place term at `τ = 0` on `𝔠_0` is positive is correct (`ζ = p^{-1/2}`
  real positive).  No confusion of the two `m`'s occurs.
* **`n4` (cross-paper, for the closing review; does not touch row A's label).**  Paper 43
  §14.1a — the section Paper 45 §14.3 cites as the handoff — is **stale**: it
  still offers row C "`c` the open constant of Remark 8.6b" (superseded by
  Def. 8A.7d), "the realization `Γ_n = E_{a_S(n)}` inside `G`" (a withdrawn-
  carrier object), and endorses Paper 45's `G_rad` §12 as "unaffected by this
  rebuild" — which phase 132 withdraws (W45.8).  Housekeeping item for row A.
* **`n5` (cross-paper, mild circularity of justification).**  Paper 43
  Def. 8A.7d's reason **(iv)** for `c := 0` is "it agrees with the convention
  of Paper 45, `χ_A = Σ_pW_p + W_∞`" — and `χ_A` is precisely the assembly
  Paper 45 W45.3 withdraws.  Reasons (i)–(iii) are independent and stand;
  reason (iv) should be struck.  Combined with `M1` this matters: the
  declaration's fourth leg points at a withdrawn object, which is one more
  reason to replace the declaration by Corollary 9.6a.
* **`n6`.**  The script is honest: it labels the zero-sum checks
  "illustration only" and reports truncation error.  I reproduced 22/22.  No
  check is circular (each compares an independently computed geometric side
  with an independently computed spectral side).

---

## 6. The renaming / definition test (D128 `C3`'s failure mode)

*Is any clause of C.1–C.9 satisfied by a definition rather than a theorem?*

| clause | satisfied by | verdict |
|---|---|---|
| C.1 | Paper 44 Lemma 3bis.6a (`Γ_h⋆Γ_g = Γ_{h*g}`, `λ_∓` formula) and Def–Thm 3bis.8 (the typing of the point classes) — **theorems** | pass |
| C.2 | Paper 43 Thm 9.1, 9.13(a), 9.14a–c′ and Paper 45 Thm 8.1 — **theorems**; Rem. 8.2's swap is a computation with a counterexample | pass |
| C.3 | Paper 44 Thm 3bis.7 on Paper 43 Thm 8.8 — **theorems** — applied to a trace that is **declared**.  Place-additivity is definitional and the paper says so | pass **with the disclosure**; the disclosure is explicit and correct |
| C.4 | primes: theorem; Gamma: theorems (7.2–7.5); **poles: `T̂_∞^{mer} :=` is a definition and its `≡ 0` is a restatement of the functional equation** | **fail as written** — `M3`.  Passes after the `9bis.2′` repair |
| C.5 | a nine-row table each of whose rows is an exact identity or an absolute-convergence certificate | pass |
| C.6 | Lemma 1.3 + Thm 9.6; Thm 10.4 | pass — but the first half is a theorem **about the `c = 0` trace** (`M1`) |
| C.7 | Rem. 9.7 + Paper 43 Thm 14.1 + Paper 44 Thm 8bis.4a | pass |
| C.8 | Theorem 9.4, proved | pass — with the import ledger corrected (`M2`) |
| C.9 | §13 ledger + §14.3, by theorem number, each handed item used or declined | pass |

*Is anything still resting on the old carrier?*  I grepped `Fell`, `E_u`,
`E_{a_S`, `Z_J`, `χ_A`, `G_rad`, `K_h`, `zero-count`, `corner`.  **Every hit
is inside a withdrawal, a historical clause text, or the banner's description
of what was withdrawn.**  No statement of §§3–12, §14 rests on any of them.
Clean.

*Independence.*  Zeros of `ζ` occur in: (E2)/(E3) as a set and a density;
Lemma 9.2, Thm 9.4, Thm 9.6, Thm 9.6′ (the comparison); Thm 10.4 (a
hypothetical off-line zero, in a contrapositive sufficiency argument).  **No
sign is proved anywhere**, and no statement of the paper uses the position of
a zero to obtain one.  Clause C.7 holds.  Only the banner's wording lags
(`m3`).

*The `(C1)` quantifier.*  Carried explicitly in Thm 9.6 (hypothesis block and
chart clause), Thm 9.6′, Thm 9bis.4(ii)–(iv), §14.4's target box, and §9.6
row 3.  **One exception, and it is `M3`'s:** Theorem 9bis.2 concerns all
primes and is **not** a colimit statement — `A(s)` is an analytic
continuation, not `\lim_S A_S(s)` — so it stands outside the convention §1.2
declares to be carried into "§9bis".  Cor. 9bis.3 knows this; §1.2 and §0.1
do not say it.  Fold this into `M3`'s repair.

---

## 7. Per-clause verdict

| clause | verdict |
|---|---|
| **C.1** | `PROVED` on the declared carrier, by citation to row B theorems.  No construction, no completion, no delta.  **Clean** |
| **C.2** | `PROVED` at the chart, rulings in the completion; the ruling labels corrected with a counterexample.  **Clean** |
| **C.3** | `PROVED` as a theorem about row A's **declared** trace, with place-additivity disclosed as definitional.  **Conditional on `M4`** (the input is cited outside its hypotheses; true, repairable in two citations) |
| **C.4** | primes and Gamma term `PROVED`; **poles `NOT EARNED as written`** (`M3`): discharged by a definition plus a negative.  `EARNED-WITH-REPAIR` available and stated |
| **C.5** | `PROVED`.  The table is exact and I found no interchange.  Row 7's certificate depends on `M2`'s import being correctly named |
| **C.6** | first half `PROVED` **for `c := 0`** — the normalization dependence must be recorded (`M1`); second half `PROVED`, the `C10` fix complete and `106_11` traced (`n2`) |
| **C.7** | `PROVED`.  No sign is proved anywhere in the paper.  Banner wording `m3` |
| **C.8** | `PROVED` in the strong form.  This is the paper's real achievement.  **Conditional on `M2`** (the ledger must name the import it actually uses) |
| **C.9** | `PROVED`.  The handoffs are by theorem number in both directions, each used or declined with a reason; the `n-1` obligation is deleted, not discharged.  `m5` is cosmetic |
| **A.6 (radial)** | `PROVED` at every finite chart, not claimed in the colimit.  **Clean**; Thm 12.2 is correct and does not need (14.2) (`n3`) |

---

## 8. Grade, and what must be recorded beside the label

**Grade.**  On Paper 43's declared carrier (a fixed finite chart `S` with the
chart system and its colimit as additional structure), for row C:

    WEIL-STRENGTH-COMPLETE: EARNED WITH REPAIRS -- NOT GRANTED in round 1.

Conditions: `M1`, `M2`, `M3`, `M4` repaired as specified.  None of the four
requires new mathematics; all four are one-paragraph or one-lemma edits, and
two of them (`M1`'s Corollary 9.6a, `M3`'s Theorem 9bis.2′) make the paper
**stronger** than it now claims.  `m1`–`m7` should be swept in the same round.
I record that the round-1 paper is, mathematically, the best of the three row
papers I have audited: its central theorem is proved rather than imported, its
refutations of its own blueprint are all correct, and its withdrawal ledger is
complete.

**What must be recorded beside the label, if it is granted.**

1. *The normalization is load-bearing.*  Every theorem of §§9, 9bis, 10, 12 —
   and therefore §14.4's "row D's target implies RH" — is a statement about
   row A's declared trace **with `c := 0`** (Paper 43 Def. 8A.7d, a
   declaration and not a derivation; Rem. 8A.7e's computation of `c_cut` does
   not close).  With Corollary 9.6a this becomes: `c = 0` is the unique
   constant compatible with the Weil comparison — which is the closure of
   D128 `C9` and must travel with the label.
2. *What is declined, not proved.*  Row C does **not** prove that `Σ_vW_v` is
   the relative character of a localization (D128 `C2`,`C3`); it proves
   statements about a declared trace and says so.  Place-additivity remains
   definitional.
3. *Quantifiers.*  The comparison theorem is a **colimit** statement
   ((C1)); at a finite chart it holds exactly inside the window
   `R(Γ_h) < \log ℓ_{next}(S)` (Paper 43 Thm 8A.7c(e)) and is **false**
   outside it.  `𝓝_∩ = 0` (Thm 12.2) is a **fixed-chart** statement; no
   colimit radical statement is made.
4. *The poles.*  The chart residue `|S_f|+1` and the polar packet `2` measure
   different things; what connects them is the one-sided collapse
   `Res_{s=0}A_S = |S_f|+1 ⟶ Res_{s=0}A = 1 = ` the `1/s` of `ξ`'s trivial
   factor `= ` half the polar packet (`M3`'s repair).  Mertens enters **once**
   (Thm 9bis.4(ii), via Paper 43 Thm 10.8b, `CLASSICAL`, quarantined, with a
   deletion test), and its subject is `s = 1`, not the residue count at
   `s = 0`.  The blueprint's §2.2 mechanism does not exist and R132.001's
   refutation of it is correct.
5. *Imports.*  (E1)–(E8), (R1) of §11, with (E3) split as in `M2`.  No
   spectral realization, no Meyer, no cutoff theorem.  Nothing else is used —
   verified by grep.
6. *No sign.*  Row C proves no sign, no positivity, no `𝓝_∞ = 0`, and nothing
   about the location of any zero outside the comparison theorem and the
   contrapositive sufficiency argument of §10.
7. *Row D inherits* `I_∂ ≤ 0` on primitive radial classes of `D_A^∞` in the
   colimit, on the trace with `c := 0`, and nothing else; and it inherits
   Paper 43 Thm 14.1 and Paper 44 Thm 8bis.4a as the two standing negatives.
8. *Housekeeping for row A* (`n4`, `n5`): Paper 43 §14.1a is stale and
   Def. 8A.7d reason (iv) points at the withdrawn `χ_A`.  Neither affects
   row A's label; both should be corrected when row A is next touched.
