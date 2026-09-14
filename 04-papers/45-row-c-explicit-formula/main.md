# Paper 45 — Row C: the explicit formula on row A's declared carrier

David Alejandro Trejo Pizzo, with Claude (Opus 5).
Repository: `research/riemann`.  Date: 2026-09-12.

Third of the series.  [Paper 43](../43-row-a-torsion-theory/main.md) closes
row A (the carrier `C_S`, the declared trace `T`, its symbol `T̂`, the
numerical object `N_A = D_A` and its completion `N_A^{dist}`);
[Paper 44](../44-row-b-arithmetic-family/main.md) closes row B (the norm class
`Γ_n^{rad}`, the Frobenius family `Frob_n`, the two Gram forms, the interface
with Weil's criterion).  This paper is row C: the comparison theorem between
row A's declared trace on row B's radial classes and the spectral side of the
Weil explicit formula, **with the explicit formula proved here** and no
analytic black box.

> **Lead decision of record (R132.007, 2026-09-12).** `ROW C: WEIL-STRENGTH-COMPLETE`
> on Paper 43's declared carrier, as a theorem about row A's declared trace with
> `c = 0` (unique by Cor 9.6a), the explicit formula **proved here** (Thm 9.4).
> Granted after three builder rounds and two hostile audits (R132.002, R132.005,
> the latter grading the label GRANTED conditional on items verified by grep in
> R132.007 §1). Recorded beside the label: normalization load-bearing and pinned;
> place-additivity definitional and declined as a localization; colimit
> quantifier (C1); the poles by Thm 9bis.2′; imports (E1)–(E8), (R1) only; no
> sign; what row D inherits. Full text: §14.1a and
> [R132.007](../../03-research/phase-132-row-c-closure/R132_007_LEAD_FINAL_AUDIT_AND_LABEL.md).

**[REBUILT, phase 132, round 1.]**  The whole paper is rebuilt.  The previous
version (label `ASSEMBLED AND NORMALIZATION-COMPATIBLE, NOT LOCALIZED`, after
`D128.003`) was written against the **old** row A — a Fell completion with
sections `K_h` supported on "external classes `E_u`", the zero-count
filtration `Z_J` with corner strata, `χ_A` assembled term by term from the
phase-123 notes, Theorem 5.4 withdrawn, and a §11 discharging an `n−1`
obligation that Paper 44 has since proved never existed.  **None of those
objects is the declared carrier any more.**  Since phases 129–131 the carrier
is named once in Paper 43 §14.0a, and row C must be a theorem about *it*.
That is what follows.  Every rewritten passage is marked
`[REBUILT, phase 132, round 1]`; the withdrawal ledger is §13.

**Status banner.**

```text
ROW C: LABEL NOT CLAIMED HERE.
       This paper states what it proves and on which carrier, clause by
       clause (section 14.2), and hands the grading to the audit of record.
       It claims NO sign, NO positivity, NO statement that N_infinity = 0,
       and NO statement about the location of any zero of zeta outside
       the comparison theorem (section 9.5), the contrapositive
       sufficiency argument of section 10, and the clauses explicitly
       labelled CLASSICAL.  [aligned with section 0.2 in round 2,
       minor m3 of R132.002.]
```

---

## 0. Summary

### 0.1 What changed, and what row C actually is now

**[REBUILT, phase 132, round 1.]**

On the true carrier most of what was hard in the old Paper 45 is either a
theorem of row A or row B, cited by number, or a non-problem.

* The test class is not constructed here.  It **is** Paper 44's
  `Γ_h ∈ D_A^{rad} ⊂ D_A = C_c^∞(C_S)` (Definition 3bis.6, Lemma 3bis.6a), a
  genuine element of row A's declared test algebra.  There is no completion,
  no "compact section" argument, and D128 finding `C8` dissolves with the
  object it was about (§3).
* The corner-strata problem disappears with the carrier.  `C_S` is a *group*
  (Paper 43 Lemma 3.3); there is no zero-count filtration on it; the only
  loci are the valuation shells `j_p(p^kZ_p^×)`.  Composite labels carry no
  finite contact because no single place has a shell of modulus `1/n`
  (Paper 44 Theorem 3bis.7), and at the object level because
  `supp Frob_n` meets no shell (Paper 44 Theorem 3ter.12).  Theorem 5.4 of the
  old paper stays withdrawn and is now **unnecessary** (§5, §13).
* The trace identity is not assembled here.  It **is** Paper 43 Theorem 8.8
  (absolute convergence off the identity, `T = Σ_v W_v`, no counterterm, no
  regularization) evaluated on radial classes by Paper 44 Theorem 3bis.7.
  D128 findings `C2`, `C3` are answered by *row A's construction* — `T` is
  Paper 43's **declared** trace (Definition 8.6, Definition 8A.7d, `c := 0`),
  not a localization claim of this paper — and this paper says so in those
  words (§5.1).

What is genuinely row C's, and is proved here, is four theorems.

**(1) The explicit formula, proved in the repository (§9.1–9.4).**  D128 `C4`
broke the old sketch: it shifted a contour across the zeros it was computing.
The correct argument does not need that shift, and it is written here in full —
the argument principle on rectangles whose horizontal sides avoid the zeros,
the exact partial-fraction expansion of `ξ'/ξ`, and then the shift of **each
prime term separately**, whose integrand is entire.  Theorem 9.4.

**(2) The comparison theorem: the spectral side is the symbol of the colimit
trace (§9.5).**  For real `F ∈ C_c^∞(R)`,

    T_∞(Γ_{F⋆F^†}) = 2Φ_F(0)Φ_F(1) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ),

the zero sum in symmetric order.  At a finite chart the symbol `T̂_S` is a
real-analytic function on `𝔠_0` (Paper 43 Theorem 9.7); in the colimit it is
**not a function** — `Ŵ_fin^∞(0) = +∞` (Paper 44 Remark 8bis.4b(1)) — but the
displayed identity says exactly what it is as a linear functional on `|F̂|²`.
Theorem 9.6.

**(3) The Tate residues, at a chart and in the continuation (§9bis).**
**[REBUILT, phase 132, round 2, finding `M3` of `R132.002`: round 1 headlined
a *vanishing* under a name — "the meromorphic symbol of the colimit trace" —
that the object does not deserve.  Both are corrected; the statement below is
one-sided, positive, and is what discharges clause C.4's polar half.]**  Write
`s = ½ + iτ`.  Paper 43's local symbols are, on the principal component,

    Ŵ_p(τ) = f_p(s) + f_p(1−s),   f_p(s) = (log p)p^{−s}/(1−p^{−s}),
    Ŵ_∞(τ) = a(s) + a(1−s),       a(s)   = ½log π − ½ψ(s/2),

each of `f_p, a` having a simple pole at `s = 0` of residue exactly `1` — the
universal Tate residue of Paper 43 Theorem 9.7b and Paper 44 Theorem 8bis.8 —
so that at a chart the total is `|S_f| + 1`, as Paper 43 Theorem 9.7b(c) says.
Now let `A(s) := a(s) + Σ_p f_p(s) = ½log π − ½ψ(s/2) − ζ'/ζ(s)` be the
**continued Euler-product symbol** — convergent for `Re s > 1`, then continued;
it is *not* the symbol of `T_∞`, which is not a function at all, and §9bis says
so in a box.  Then `A(s) = −ξ'/ξ(s) + 1/s + 1/(s−1)`, and since `ξ` is entire
and nonzero at `0` and `1`:

    Res_{s=0} A = 1 = Res_{s=1} A ,   against
    Res_{s=0} A_S = |S_f|+1 ,  Res_{s=1} A_S = 0  at every finite chart.

Theorem 9bis.2′.  **The two poles of `A` are the poles of the trivial factor
`½s(s−1)` of `ξ`, their residues against `g` are `g(0)` and `g(1)`, and that
pair is the polar packet `2Φ_F(0)Φ_F(1) = β_T(M,M)` of Theorem 8.1 — with
coefficient exactly `1` each.**  The passage from the chart to the
continuation is asymmetric and is tabulated in Remark 9bis.2a: at `s = 0` the
`|S_f|` finite residues **evaporate** (summation over primes and analytic
continuation do not commute there — Corollary 9bis.3), leaving the archimedean
`1`; at `s = 1` the chart has **no pole at all** and the pole is **created in
the limit** by the pole of `ζ`.  (The *rate* of that creation is Mertens,
Theorem 9bis.4(iii), `CLASSICAL` and quarantined; **clause C.4's discharge does
not use it** — **[REBUILT, phase 132, round 3, finding `r6` of `R132.005`:
round 2 folded a quarantined import into the sentence that discharges a clause
it does not serve]**.)  This settles clause C.4's "poles in the same
comparison" as a residue computation; the
identity `A(s)+A(1−s) ≡ 0` — round 1's headline — is demoted to Remark 9bis.2b,
where it belongs: it is the functional equation in one line, and no clause
rests on it.

**(4) `𝓝_∩ = 0` on the radial sector, at every chart (§12).**  On `D_A^{rad}`,
`I_A(Γ_F,Γ_G) = (1/2π)∫ \hatΓ_F \overline{\hatΓ_G} T̂_S dτ` on the principal
component, and `T̂_S` is real-analytic and not identically zero there
(Paper 43 Theorem 9.7(c), (14.2)); so the scalar radical of `I_A` **within the
radial sector** is `0`.  Theorem 12.2.  The rulings are not lost: they live in
the completion (Paper 43 Theorems 9.14a–c′).

Kept from the old paper, re-proved on the true carrier: Theorem 8.1 (the polar
packet *is* the hyperbolic ruling form; D128 confirmed it) and Theorem 10.4
(sufficiency of primitive tests for Weil's criterion; D128 called it "the
strongest and most defensible result in the paper"), the latter with D128
`C10`'s fix carried out in full (§10.3).

### 0.2 What this paper does not claim

No sign.  No positivity.  No statement that the colimit numerical radical
vanishes (Paper 43 §13.8 forbids it and this paper does not need it).  No
statement about the location of a zero of `ζ` outside §9.5 and §10, where the
zeros enter the comparison theorem itself, which is what the closure plan §7
explicitly permits.  The label is not claimed; §14.2 states clause by clause
what is proved and on which carrier.

---

## 1. Conventions, the carrier, and five dictionaries

### 1.1 Status labels

`PROVED` (here), `PROVED-IN-REPOSITORY` (proved in a note or in Paper 43/44,
cited by number), `CLASSICAL` (a standard theorem about `ζ` or about analysis,
named in §11 with the clause it serves, proof recalled here when the paper
uses its internals), `IMPORTED`, `OPEN`.  No arrow is used without a label.

### 1.2 The carrier, named once

**[REBUILT, phase 132, round 1.  This replaces §§1.2–1.4 of the previous
version, which described the withdrawn carrier.]**

The carrier is Paper 43 §14.0a, verbatim: a fixed finite chart
`S = {∞} ∪ S_f`, `S_f` finite nonempty, with the chart system `{C_S, π_{TS}}`
and its colimit as additional structure on that carrier.  Concretely:

    C_S ≅ R^× × ∏_{p∈S_f} Z_p^×,        |x|_S = |x_∞|_∞ on C_S,      (1.1)

by Paper 43 Lemma 3.3 (the valuation splitting `A_S^× = Γ_S × ker φ`, with
`C_S := Γ_S\A_S^× ≅ ker φ`), and

    D_A := C_c^∞(C_S),   F^†(u) = conj(F(u^{−1})),   (Paper 43 (3.6), (8.2))

a commutative nuclear LF `†`-algebra (Paper 43 Corollary 3.4).  The declared
trace is Paper 43 Definition 8.6 with the constant declared by Definition
8A.7d:

    T(F) = Σ_{v∈S} W_v(F),   c := 0,                                  (1.2)

with `W_p` given by (8.5) (shell integral plus regularized unit packet, with
`vol_{d^*x}(p^kZ_p^×) = log p`) and `W_∞` by (8.5∞) (the `(γ+log4π)b(1)`
counterterm plus the regularized heat integral of `K(t) = e^{−t/2}/(1−e^{−2t})`,
with the archimedean measure `d^*x_∞ = dx/(2|x|)` of Remark 8.6a).  The
intersection form is Paper 43 Definition 9.2,

    I_A(F,G) := T(F ⋆ G^†),                                           (1.3)

Hermitian and jointly continuous (Theorem 9.3), with `𝓝 = 0`, `N_A = D_A`
(Theorem 9.8).  The Tate boundary is `M = (λ_−,λ_+)`,
`λ_∓(F) = ∫_{C_S}F(u)|u|_S^{∓1/2}d^*u`, continuous and surjective onto
`B_T = C²` with the hyperbolic form `β_T(z,w) = z_−\overline{w_+} +
z_+\overline{w_−}` (Theorem 9.1).  The completion is
`N_A^{dist} = \overline{J(N_A)} ⊆ D_A' ⊕ B_T`, `J(F) = (I_A(F,·),M(F))`
(Theorem 9.14); the rulings `e_±^{dist}` live there and only there
(Theorems 9.14a–c′).

**Colimit convention, inherited verbatim from Paper 44 (C1).**  *Every
statement about all primes is a colimit statement.*  `T_∞` is the chart-
invariant trace on `D_A^∞ = colim_S D_A(S)` (Paper 43 Theorem 8A.7c); for a
test of radius `R(F) < log ℓ_next(S)` the chart form equals the colimit form
exactly (Theorem 8A.7c(e)); outside that window they differ by the finite sum
(8A.21).  Where this paper writes `T` with the prime sum running over **all**
primes, it means `T_∞`, and it says so.  *This convention is carried
explicitly into the hypotheses of every theorem below that uses it* — §9.5,
§9bis, §10 — as the hypothesis-carrying rule requires.  **[REBUILT, phase 132,
round 3, finding `r1` of `R132.005`.]**  In §9bis it is carried into the
statements about `T_∞` — Theorem 9bis.4(ii),(iv) — and **not** into
Definition 9bis.1a or Theorem 9bis.2′, which are about the **continued
Euler-product symbol** `A`: `A` is an analytic continuation, not a colimit of
the chart symbols where those live (Corollary 9bis.3 is precisely the failure
of that exchange), so (C1) does not govern it and Definition 9bis.1a's box says
so.  Every §9bis theorem carries its own quantifier at its point of use.

**Normalization convention, inherited from Paper 44 (C2).**  This paper works
only with radial classes `Γ_h` of Definition 3bis.6, for which no level-`N`
normalization arises; §§8, 9bis cite Paper 44's Frobenius statements in the
**bare** convention and say so at the point of use.

### 1.3 Dictionary 1 — coordinates: `𝒯`, `C_c^∞(R)`, and the half-density

**[REBUILT, phase 132, round 1.  Blueprint §3(a).  Fixed once, here, and used
in every later section.]**

Three coordinate systems occur in the corpus.  They are related as follows.

| object | coordinate | relation |
|---|---|---|
| Paper 42's `𝒯 = C_c^∞(R_{>0}^×)` | multiplicative `x ∈ R_{>0}` | `F(t) = e^{t/2}f(e^t)` |
| P124.013 / P123.036's test `F` | additive `t = log x` | `Φ_F(s) = ∫F(t)e^{(s−½)t}dt` |
| Paper 44's radial profile `h` | additive `t = log\|w\|_S` | `Γ_h(w) = h(−log\|w\|_S)` |
| Paper 43's chart coordinate | `t = log\|w\|_S` on `C_S` | `d^*w = dt ⊗ μ`, `μ` a probability measure |

The factor `e^{t/2}` in the first row **is** the half-density: Paper 43 §5.2
and §8.2's normalization dictionary record that P123.007's unnormalized
involution `f^†(x) = x^{−1}\overline{f(x^{−1})}` is carried to Paper 43's
`F^†(u) = \overline{F(u^{−1})}` by `F ↦ |·|_S^{1/2}F`, which in the
multiplicative coordinate is exactly `f ↦ e^{t/2}f(e^t)`.  So `𝒯` and
`C_c^∞(R)` are the same test class in two gauges, and **the half-density is
the change of gauge, not a weight inserted by hand**.

**Lemma 1.1 (the sign of the profile).**  For `h ∈ C_c^∞(R)` the profile of
`Γ_h` in the coordinate `t = log|w|_S` is `t ↦ h(−t)`.  Consequently, with
`\hat u(τ) := ∫u(t)e^{−iτt}dt`,

    \widehat{Γ_h}(𝔠_0,τ) = \hat h(−τ) ,                               (1.4)

and `\widehat{Γ_h}` vanishes on every non-principal component of `Ĉ_S`.

*Proof.*  Definition 3bis.6 of Paper 44 is `Γ_h(w) = h(−log|w|_S)`, whence the
profile.  `Γ_h` is constant on the compact coordinates and even in the sign of
`w_∞`, so by orthogonality its Fourier transform is carried by the component
`𝔠_0 = (ε = 0, κ_q = 1 ∀q)` (the computation is Paper 43 Theorem 9.14a(b)).
Then `\widehat{Γ_h}(τ) = ∫h(−t)e^{−iτt}dt = \hat h(−τ)`.  ∎  `PROVED`

**Remark 1.2 (why the sign is harmless, and where it is not).**  Every symbol
occurring in this paper is **even** in `τ` on `𝔠_0` (Paper 43 Theorem 9.7(a)
with `θ_p = 0` there, and 9.7(b)), so (1.4) never changes a value of `I_A`.
It does change the *labelling of the two rulings*: see Remark 8.2, which is a
correction of record to this paper's own previous convention.

### 1.4 Dictionary 2 — the three sign conventions, in one table

**[REBUILT, phase 132, round 1.  Blueprint §3(b).]**

Let `F ∈ C_c^∞(R)` be **real**, `h := F ⋆ F^†` with `F^†(t) = \overline{F(−t)}`,
so `h` is real and **even** and `\hat h = |\hat F|²`.  Put
`Φ_F(s) = ∫F(t)e^{(s−½)t}dt` (P124.013 (1.1)).

| convention | statement | source |
|---|---|---|
| (S1) | `q(F) = ⟨𝒜F,F⟩`, `𝒜 = g_Γ(D) − m_0 − Σ_nΛ(n)n^{−1/2}(S_{\log n}+S_{−\log n})`, `g_Γ(τ)−m_0 = Re ψ(¼+iτ/2) − \log π`; and `q = −B_nuc` | P123.036 (1.1); paper 42 `eq:Bnuc` |
| (S2) | `I_A(F,F) = ∫_{Ĉ_S}\|\hat F\|²(T̂ + c)dχ`, `c := 0` | Paper 43 (14.1), Def. 8A.7d |
| (S3) | `I_∂(Γ_u,Γ_u) = −Q(u)` on primitive `u`, `Q(g) = Σ_ρ\hat g(ρ)\overline{\hat g(1−\bar ρ)}` | Paper 44 (8bis.14a), (8bis.14e) |

**Lemma 1.3 (the three agree).**  **[REBUILT, phase 132, round 2, minor `m6`
of `R132.002` — the dependency, stated so a reader can see there is no
circularity.  Leg (S1) uses only Lemma 5.1a and Paper 43 Theorem 9.7(b),(d),
and it is the **only** leg used by Theorem 9.6.  Leg (S3) uses Theorem 9.4,
which in turn uses only the imports (E1)–(E5) and **nothing** from §1 — so the
chain Lemma 1.3(S3) → Thm 9.4 → (E1)–(E5) terminates and Theorem 9.6 does not
depend on (S3).  **[Round 3, note `n2′` of `R132.005`: after the phase-132
cross-paper edit to Paper 44 Thm 8bis.4(ii), leg (S3)'s chain passes through
Paper 44 — `Lem 1.3(S3) → P44 (8bis.14e) → P44 Thm 8bis.4(ii) → P45 Thm 9.4 →
(E1)–(E5)`.  It still **terminates**: Theorem 9.4 uses nothing from Paper 44
and nothing from §1.]**  **[REBUILT, phase 132, round 3, finding `r7` of
`R132.005`: the (C1) quantifier is now carried here.  §1.2 requires that where
this paper writes `T` with the prime sum over **all** primes it means `T_∞` and
says so; (1.5) and the proof's display do sum over all prime powers, and
round 2 did not say so.  This was the one place in the paper where the
hypothesis-carrying rule was violated.]**  For real `F ∈ C_c^∞(R)`, with
`T_∞` the **colimit** trace on `D_A^∞` (convention (C1); at a fixed finite
chart every display below holds verbatim inside the window
`R(Γ_{F⋆F^†}) < \log ℓ_{next}(S)` of Paper 43 Theorem 8A.7c(e)),

    I_∞(Γ_F, Γ_F) = T_∞(Γ_{F⋆F^†}) = −q(F) = B_nuc(F,F),              (1.5)

and, when `F` is primitive, `= −Q(F)`, where `Q(F) = Σ_ρΦ_F(ρ)Φ_F(1−ρ)`.

*Proof.*  Three steps, each a computation.

*(S1) versus the trace.*  **[REBUILT, phase 132, round 2, `M4`: `h(0) =
‖F‖²_{L²} > 0`, so `0 ∈ supp h` always and Theorem 5.1 is out of its
hypotheses here; the citation is Lemma 5.1a, which has none.]**  By
**Lemma 5.1a** (with `c := 0`),

    T(Γ_{F⋆F^†}) = Σ_n Λ(n)n^{−1/2}[h(\log n)+h(−\log n)] + W_∞(Γ_h),

and `h(a) = ⟨S_aF,F⟩` with `S_aF(t) = F(t+a)` (P123.036 §1; direct
substitution).  So the first summand is **minus** the prime part of
`⟨𝒜F,F⟩`.  By Paper 43 Theorem 9.7(d) and Theorem 9.7(b),
`W_∞(Γ_h) = (1/2π)∫\hat h(τ)\hat W_∞(0,τ)dτ =
(1/2π)∫|\hat F|²[\log π − Re ψ(¼+iτ/2)]dτ`, which is **minus** the first two
terms of `⟨𝒜F,F⟩`.  (The step uses Lemma 1.1 and the evenness of `\hat W_∞` in
`τ`.)  Adding, `T(Γ_{F⋆F^†}) = −⟨𝒜F,F⟩ = −q(F) = B_nuc(F,F)`.

*(S2).*  `I_A(Γ_F,Γ_F) = T(Γ_F⋆Γ_F^†) = T(Γ_{F⋆F^†})` by Lemma 3bis.6a, and
(S2) is the Plancherel form (9.13) of the same number, with
`\widehat{Γ_F⋆Γ_F^†} = |\widehat{Γ_F}|² = |\hat F(−τ)|²` and `T̂` even.

*(S3).*  For real `F`, `Φ_F(\bar s) = \overline{Φ_F(s)}`, so
`\overline{Φ_F(1−\bar ρ)} = Φ_F(1−ρ)` and `Q(F) = Σ_ρΦ_F(ρ)Φ_F(1−ρ)`.  By
Theorem 9.4 below with `Φ_F(0) = Φ_F(1) = 0`, `Q(F) = ⟨𝒜F,F⟩ = q(F)`, so
`I_A(Γ_F,Γ_F) = −Q(F)`, which is (8bis.14e).  ∎  `PROVED`

### 1.5 Dictionary 3 — the archimedean constants

**[REBUILT, phase 132, round 1.  Blueprint §3(c).]**

| quantity | value | source |
|---|---|---|
| `\hat W_∞(0,τ)` | `\log π − Re ψ(¼+iτ/2)` | P123.035 (4.1); Paper 43 Thm 9.7(b) |
| `\hat W_∞(0,0)` | `\log π − ψ(¼) = \log π + γ + 3\log 2 + π/2` | Paper 43 **(9.12b)**.  **[Round 3, note `n7′` of `R132.005`: round 2 cited (14.2), which is a lower bound for `m := \sup_{Ĉ_S}\hat T` **including** the finite places; the exact *archimedean* value is (9.12b).  This is the typing distinction Theorem 12.2 draws.]** |
| numerically | `1.144730 + 0.577216 + 2.079442 + 1.570796 = 5.372184` | §15 script |
| `m_0` | `\log π − ψ(¼)`, the same number | P123.036 §2; Paper 45 (1.7) |
| counterterm in (8.5∞) | `γ + \log 4π` | P123.035 (3.1); Paper 43 (8.5∞) |
| reconciliation | `γ + \log 4π + ψ(½) = \log π`, via `ψ(½) = −γ − 2\log 2` | Thm 7.4 below |
| kernel | `K(t) = e^{−t/2}/(1−e^{−2t}) = ¼[1/\sinh(t/2) + 1/\cosh(t/2)]` | Paper 43 (8.5∞) |
| `K(\log n)` | `n^{3/2}/(n²−1) = ½[τ_∞(1/n)+τ_∞(−1/n)]` | Paper 44 (3bis.11) |
| archimedean measure | `d^*x_∞ = dx/(2\|x\|)`, declared | Paper 43 (8.5b) |

All four sources are consistent; the `½` in the last two rows is the declared
folding factor of Remark 8.6a, and it is the same `½` throughout.  The
numerical identities are re-verified in §15.

### 1.6 Dictionary 4 — `vol(Z_p^×) = \log p`

**[REBUILT, phase 132, round 1.  Blueprint §3(d).  The old Lemma 6.1 becomes a
corollary; see §6.]**  The normalization `vol_{d^*x}(p^kZ_p^×) = \log p` is
**not** a stipulation of this paper and is no longer defended by an Arakelov
analogy.  It is Paper 44 Theorem 8bis.8: it is the **unique** local
normalization, up to one global scale, for which the local Tate residue
`Res_{s=0}∫_{|x|_v≤1}|x|_v^s d^*x_v` is the same at every place.  §6 records
the three coincidences that the old Lemma 6.1 listed, with their true status.

### 1.7 Dictionary 5 — Fourier and Mellin

**[REBUILT, phase 132, round 1.  Blueprint §3(e).]**

    \hat u(τ) = ∫_R u(t)e^{−iτt}dt ,      u(t) = (1/2π)∫\hat u(τ)e^{iτt}dτ,
    Φ_F(s)    = ∫_R F(t)e^{(s−½)t}dt ,    s = ½ + iτ  ⟹  Φ_F(½+iτ) = \hat F(−τ),
    Φ_F(0) = M_−(F) = λ_+(Γ_F),           Φ_F(1) = M_+(F) = λ_−(Γ_F),   (1.6)
    dχ|_{𝔠_0} = dτ/2π    (Paper 43 Thm 9.7b(d); P123.035 (4.1)),
    λ_+(F) = \hat F(i/2)  for a profile f = \hat{}-transformed test (Paper 43 (9.7b.6)).

Paper 44's `\hat g(s) := ∫g(t)e^{(s−½)t}dt` of (8bis.14a) is `Φ_g(s)`; the two
notations are identified once here and `Φ` is used below.  **The last line of
(1.6) is a correction of record to this paper's previous convention**; see
Remark 8.2.

---

## 2. The acceptance contract for row C, re-expressed on the true carrier

**[REBUILT, phase 132, round 1.  The clause texts are PLAN §7 verbatim in
column 2; column 3 says what each clause *is* on the declared carrier, with
citations by theorem number.]**

| clause | requirement (PLAN §7) | what it is on the declared carrier |
|---|---|---|
| **C.1** | fix the test class; construct `K_h` inside row A; a sum of deltas needs justification as a multiplier/distribution | `Γ_h ∈ D_A^{rad} ⊂ D_A` (Paper 44 Def. 3bis.6, Lem. 3bis.6a).  Point classes are **not** in `D_A`: `Γ_n^{rad}, Frob_n ∈ N_A^{dist}` only (Paper 44 Thms. 8.3, 3ter.14).  §3 |
| **C.2** | realize the complex; identify action, coboundaries, duality and the **two Tate terms** | `M = (λ_−,λ_+)` onto `B_T` with `β_T` (Paper 43 Thm. 9.1, 9.12); rulings `e_±^{dist}` in the completion (Thm. 9.14a–c′); the polar packet is `β_T(M,M)` (Thm. 8.1 here).  §8 |
| **C.3** | trace identity over a common kernel; finite, archimedean and identity contact | Paper 43 Thm. 8.8 (`D_A^{off}`, absolutely convergent, no counterterm), evaluated on radial classes by Paper 44 Thm. 3bis.7 (= Thm. 5.1); the **identity case `0 ∈ supp h`** by **Lemma 5.1a**, which carries no support hypothesis.  Place-additivity is **definitional**, §5.1.  §5 |
<!-- [REBUILT, phase 132, round 3, note `n3′` of `R132.005`: rows C.3 and C.4 of this summary table lagged §14.2, which is the authoritative clause table; they now agree.  No statement in §2 was false, but the two tables must not disagree.] -->
| **C.4** | prime term, Gamma term and the **poles in the same comparison** | primes and Gamma off **one object**, the symbol (Paper 43 Thms. 9.7, 9.7b); the **poles by Theorem 9bis.2′**, a residue computation at both Tate points, with Thm. 7.5 and Lem. 9bis.1.  §§5–7, §9bis |
| **C.5** | record the order of limits | §9.6.  Convention (C1); `Γ_h` compactly supported ⇒ finite prime sum; absolutely convergent archimedean integral; zero sum in symmetric order.  No interchange |
| **C.6** | prove `I_A = B_nuc`, and sufficiency for Weil's criterion | first half: Lemma 1.3 + Theorem 9.6.  Second half: Theorem 10.4.  §§9, 10 |
| **C.7** | no zero position assumed in proving any sign; zeros may be used in the comparison theorem | §9.5 Remark 9.7, Paper 43 Thm. 14.1, Paper 44 Thm. 8bis.4a.  §§9, 14 |
| **C.8** | no analytic black box | **strong form**: the explicit formula is **proved here**, Theorem 9.4.  Every classical import is named in §11 with the clause it serves |
| **C.9** | compatibility with A and B; handoffs | §14.3, by theorem number, both directions.  The old §11 is deleted: the `n−1` obligation never existed (Paper 44 §9bis W1–W3).  §13 |

---

## 3. The test class (clause C.1)

**[REBUILT, phase 132, round 1.  This replaces Definition 3.1, Proposition 3.2
and Remark 3.3 of the previous version, all of which referred to the withdrawn
Fell completion.  D128 finding `C8` is about an object that no longer
exists.]**

**Definition 3.1 (the test class, imported by number).**  For `h ∈ C_c^∞(R)`,
`Γ_h(w) := h(−\log|w|_S)` (Paper 44 Definition 3bis.6), and

    D_A^{rad} := { Γ_h : h ∈ C_c^∞(R) } ⊂ D_A = C_c^∞(C_S).            (3.1)

**Proposition 3.2 (C.1 is a theorem of row B).**  `D_A^{rad}` is a `†`-stable
subalgebra of `D_A` and `h ↦ Γ_h` is an isomorphism of `†`-algebras from
`(C_c^∞(R), ∗)` onto it:

    Γ_h ⋆ Γ_g = Γ_{h∗g},   Γ_h^† = Γ_{h^∨},  h^∨(t) = \overline{h(−t)},
    λ_∓(Γ_h) = ∫_R h(s)e^{±s/2}ds,   and  0 ∉ supp h ⟹ Γ_h ∈ D_A^{off} .   (3.2)

*Proof.*  This is Paper 44 Lemma 3bis.6a, verbatim.  Injectivity of `h ↦ Γ_h`
is immediate from (1.1) (`|·|_S` is surjective onto `R_{>0}`).  ∎
`PROVED-IN-REPOSITORY` (Paper 44 Lemma 3bis.6a).

**Remark 3.3 (what the closure plan warned about, and where it lands).**  PLAN
§7.1 warns that "a sum of deltas needs justification as a multiplier or
distribution; one does not declare a Schwartz function".  On this carrier the
warning is met by *typing*, and the type is enforced by row B:

* `Γ_h ∈ D_A` is a genuine `C_c^∞` function of the carrier.  No delta appears.
* the point classes `Γ_n^{rad}` (the Haar measure of a level set of `|·|_S`)
  and `Frob_n` (the Haar measure of a fixed-point stratum) are **not** in
  `D_A`.  Paper 44 Definition–Theorem 3bis.8 states in terms: `T(Γ_n^{rad})`
  is **undefined**, and the naive place-wise extension returns `0`, not
  `Λ(n)n^{−1/2}`.  What is defined is `J(Γ_n^{rad}) ∈ N_A^{dist}` (Paper 44
  Theorem 8.3) and `J(Frob_n) ∈ N_A^{dist}` (Theorem 3ter.14), by convergence
  **in the strong dual**, and the number `Λ(n)n^{−1/2}` is the atom mass of
  the unique representing measure `ω_fin` (Definition–Theorem 3bis.8).
* every statement of this paper is therefore made either **on `D_A^{rad}`**
  (§§5, 7, 9, 10, 12) or **on `N_A^{dist}`** (§8's rulings, §8.3's point
  classes), and each theorem says which.  This is the requirement of clause
  C.1's second sentence, discharged by type rather than by argument.

`PROVED` (by citation; nothing new is constructed here).

---

## 4. The anatomy of the Weil weight, on the true carrier

**[REBUILT, phase 132, round 1.  The previous §4 (Lemma 4.1, Theorem 4.2,
Remark 4.3) was about the external group `H_S = R_{>0}×∏Z_ℓ^×` acting on
`X^+ = R_{>0}×∏Q_ℓ` with gauge labels `Γ_S`.  That is the withdrawn carrier.
The true statement is shorter, and it is a corollary of Paper 43 Lemma 3.3 and
Paper 44 Theorem 3bis.7.]**

**Theorem 4.1 (the two halves of the weight, restated correctly).**  Let
`n = p^k` with `p ∈ S_f`.  In the atom mass `Λ(n)n^{−1/2}` of Paper 44's
representing measure `ω_fin` (Definition–Theorem 3bis.8):

  (i) the factor `n^{−1/2} = p^{−k/2}` is the value of the local density
      `τ_p(x) = |x|_p^{1/2}/|1−x|_p` on the shell `p^kZ_p^×`, where it is the
      **constant** `p^{−|k|/2}` (Paper 43 Lemma 8.2(i));
  (ii) the factor `Λ(p^k) = \log p` is the multiplicative Haar volume
      `vol_{d^*x}(p^kZ_p^×)` of that shell (Paper 44 (3bis.8));
  (iii) both factors are therefore **finite-place** data of the single place
      `p`, and the archimedean place contributes to `ω_fin` nothing at all:
      its contribution to `T(Γ_h)` is the continuous density
      `ω_∞ = K(|t|)dt` (Paper 44 Definition–Theorem 3bis.8).

*Proof.*  (i) and (ii) are the two displayed inputs to the proof of Paper 44
Theorem 3bis.7, read off it.  (iii) is that theorem's statement: the finite
part is a sum of atoms, the archimedean part an absolutely continuous density,
and the two are proved to be the unique representing measures.  ∎  `PROVED`

**Remark 4.2 (a claim of the previous version, withdrawn).**  The previous
Theorem 4.2 asserted that "`n^{−1/2}` is **archimedean** and `\log p` is
**finite**", so that "`Λ(n)n^{−1/2}` is not one object".  On the declared
carrier that is **false**: by Theorem 4.1 both factors are local data of the
same finite place `p`, and the half-density `p^{−k/2}` is the value of `τ_p`,
not a real coordinate.  The old statement was an artefact of the withdrawn
carrier's normalized representative `h_S(n) = (1/n; 1,1,…)` and of D128
finding `C6`, which already recorded that the gauge choice was doing the work.
Withdrawn; see §13, item W45.4.

---

## 5. The finite places (clauses C.3, C.4)

### 5.1 The trace identity is row A's construction, and this paper says so

**[REBUILT, phase 132, round 1.  This is the honest answer to D128 findings
`C2` and `C3`, and it is the answer row A's rebuild makes available.]**

D128 `C2` found that the old paper never proved that a character `χ_A`
decomposes along the zero-count filtration; `C3` found that additivity over
places was *inherited from a definition* `B_P(f) = Σ_p C_pλ_G(f)C_p`.  Both
findings are accepted and both are now moot, for the following reason, which
must be stated plainly and not softened:

> **`T` is row A's declared trace.**  Paper 43 Definition 8.6 *defines*
> `T := Σ_{v∈S}W_v + c·F(1)`, with `c := 0` by Definition 8A.7d.  Paper 43
> §8.2 states why the order was reversed in its round 4 — so that nothing
> downstream rests on an imported cutoff theorem whose constants P123.035 §6
> forbids citing — and Theorem 8.10 records the comparison with the analytic
> regularization as a **comparison theorem** with one undetermined constant
> `c_cut`, on which nothing depends.  Row C therefore does **not** claim that
> `Σ_v W_v` is *the* relative character of a localization; it claims, and
> proves, statements about row A's declared trace.  Row A's own clause A.5 is
> discharged on that declared object (Paper 43 §8A: Thms 8A.3–8A.4 cyclicity,
> 8A.7b nuclearity of `𝓐_tr`, 8A.9's Euler characteristic of the shadow at
> unit shells with a **declared** half-density–Lefschetz normalization at
> non-unit shells, and obstacle O-A5-5's "no stronger statement is claimed").

Everything in §§5–12 is a statement about that declared `T`, and no sentence
of this paper asserts more.

### 5.2 The prime packet, on radial classes

**Theorem 5.1 (the prime packet; `PROVED-IN-REPOSITORY`, Paper 44
Theorem 3bis.7).**  Let `h ∈ C_c^∞(R)` with `0 ∉ supp h`, and let `c := 0`.
Then `T(Γ_h)` is an absolutely convergent **finite** sum plus a convergent
integral, with **no regularization and no counterterm**, and

    T(Γ_h) = Σ_{p∈S_f}Σ_{k≥1}(\log p)p^{−k/2}[h(k\log p)+h(−k\log p)]
             + ∫_R K(|t|)h(t)dt                                        (5.1)
           = Σ_{n=p^k, p∈S_f} Λ(n)n^{−1/2}[h(\log n)+h(−\log n)]
             + ∫_R K(|t|)h(t)dt .                                      (5.2)

On the colimit `D_A^∞` with `T_∞` (Paper 43 Theorem 8A.7c) the restriction
`p ∈ S_f` disappears and the sum runs over all prime powers `n` with
`|\log n| ≤ R(Γ_h)`, still a finite sum.

This is exactly the prime term the contract's clause C.4 asks for, in the
convention of (1.5)–(1.7), and it is a **theorem about row A's declared trace
evaluated on row B's arithmetic family** (Paper 44 §9.1), not an analogy.

**Corollary 5.2 (`Λ(n) = 0` for composite `n`, on the carrier;
unconditionally).**  In (5.2) no composite label occurs, for the reason given
in the proof of Paper 44 Theorem 3bis.7: the finite-place part of `T(Γ_h)` is
a sum over the valuation shells `p^kZ_p^×`, whose moduli are exactly the prime
powers, and no single place has a shell of modulus `1/n` for composite `n`.

At the level of **objects** the corresponding statement is Paper 44
Theorem 3ter.12: for composite `n`, `supp Frob_n` meets `Im j_q` for no `q`
at all, while for `n = p^k` it **is** the whole shell `j_p(p^kZ_p^×)`.  The
two statements are different and must not be conflated: (5.2) is about the
radial family and is an evaluation of `T`; 3ter.12 is about the Frobenius
objects and is a support computation, prior to any trace.

*Proof.*  Both citations, verbatim.  ∎  `PROVED-IN-REPOSITORY`.

**Lemma 5.1a (the radial trace, with **no** support hypothesis).**  **[REBUILT,
phase 132, round 2, finding `M4` of `R132.002`.  Theorem 5.1 — Paper 44
Theorem 3bis.7 — is stated for `0 ∉ supp h`, and its proof opens "By Lemma
3bis.6a, `Γ_h ∈ D_A^{off}`, so Paper 43 Theorem 8.8 applies".  But every
application in §§1.4, 9.5, 12 has `h = F⋆F^†` with `h(0) = ‖F‖_{L²}² > 0`, so
`0 ∈ supp h` **always**.  Round 1 wrote "together with (1.2)'s regularized
`W_∞` when `0 ∈ supp h`", which is a gesture and not a citation: the naive
archimedean integral `∫K(|t|)h(t)dt` **diverges** at `t = 0`, since
`K(t) ∼ 1/(2t)`, so the identity is not obtained from (5.1) by continuity
either.  The statement is nevertheless true, and here it is, with the two
citations that prove it.]**  Let `h ∈ C_c^∞(R)` be **arbitrary** — no support
restriction — and let `c := 0` (Paper 43 Definition 8A.7d).  Then `Γ_h ∈ D_A`,
`T(Γ_h)` is defined, and

    T(Γ_h) = Σ_{p∈S_f}Σ_{k≥1}(\log p)\,p^{−k/2}[h(k\log p)+h(−k\log p)]
             + \frac1{2π}∫_R \hat h(−τ)\,\hat W_∞(0,τ)\,dτ ,            (5.1a)

the finite part a **finite** sum, the archimedean part an absolutely
convergent integral.  When `0 ∉ supp h`, the second term equals
`∫_R K(|t|)h(t)dt` and (5.1a) is (5.1).  On the colimit `D_A^∞` with `T_∞` the
restriction `p ∈ S_f` disappears (Paper 43 Theorem 8A.7c).

*Proof.*  Two citations, one per place type; neither carries a support
hypothesis.

*The finite places.*  `T(Γ_h) = Σ_v W_v(Γ_h)` is Paper 43 Definition 8.6 with
`c := 0`, valid on all of `D_A`.  At a finite place, `W_p` is (8.5): a shell
integral plus the **regularized unit packet**
`(\log p)∫_{Z_p^×}(a(u) − a(1))/|1−u|_p\,du` with `a := Γ_h ∘ j_p`.  For a
radial class `a` is **constant** on `Z_p^×`: by (9.5b), `j_p(u) = (1` at `∞`,
`u` at `p`, `1` elsewhere`)` for a unit `u`, so `|j_p(u)|_S = 1` and
`a(u) = h(0) = a(1)` for every `u`.  Hence the unit packet vanishes
**identically and pointwise, with no smallness and no support hypothesis** —
this is step (1) of the proof of Paper 44 Theorem 3bis.7, which is where that
proof uses radiality and **not** where it uses `0 ∉ supp h`.  What remains is
the shell part, computed in step (2) of the same proof by Paper 43
Lemma 8.2(i) (`τ_p = p^{−|k|/2}`, constant on the shell) and
`vol_{d^*x}(p^kZ_p^×) = \log p`, giving the displayed finite sum; it is finite
because `supp h` is compact.

*The archimedean place.*  Do **not** use (8.5∞) directly.  Use Paper 43
Theorem 9.7(d), the Plancherel form (9.13),

    T(H) = ∫_{Ĉ_S}\hat H(χ)\,(\hat T(χ)+c)\,dχ ,   absolutely convergent,

which is stated and proved there **for every `H ∈ D_A`**, with no support
hypothesis whatever; `\hat T = \hat W_∞ + Σ_{p∈S_f}\hat W_p` by (8A.23).
Apply it to `H = Γ_h`, which by Lemma 1.1 is carried by `𝔠_0` with
`\widehat{Γ_h}(τ) = \hat h(−τ)`, and with `dχ|_{𝔠_0} = dτ/2π`.  Subtracting
the finite-place terms just computed leaves the archimedean term of (5.1a) —
legitimately, because the Plancherel form holds **place by place**: Paper 43
**(9.13′)**, `W_v(H) = ∫\hat H\,\hat W_v\,dχ` for every `v ∈ S` and every
`H ∈ D_A`, each integral absolutely convergent.  **[phase 133, PANEL_1 finding
C1: the subtraction step needs the place-wise identity, which was proved
inside Paper 43 Theorem 9.7(d)'s termwise interchange but was not a numbered
assertion; it is now Paper 43 Theorem 9.7(d′).  The lemma is unchanged.]**
(Equivalently: (8.5∞)'s regularization — the `(γ+\log4π)b(0)` counterterm and
the `−2b(0)e^{−t/2}` subtraction — is exactly what makes `W_∞` a continuous
functional on all of `D_A` with symbol `\hat W_∞`; Paper 43 Theorem 9.7(b),(d).
The divergence of the naive `∫K(|t|)h(t)dt` at `t = 0` is what the
counterterm removes, and (5.1a) is the regularized value.)

*Consistency.*  For `0 ∉ supp h` the counterterm and the subtraction both
vanish (Paper 43 Theorem 8.8), so the archimedean term is
`∫_0^∞K(t)[h(−t)+h(t)]dt = ∫_R K(|t|)h(t)dt`, and (5.1a) reduces to (5.1).  ∎
`PROVED` (Paper 44 Thm 3bis.7 proof step (1); Paper 43 Def. 8.6, Thm 9.7(b),(d)).

**Remark 5.3 (the corner-strata problem has no referent).**  The old §5.3–5.6
computed a "naive stratum count" `n^{−1/2}∏_{p|n}\log p` over the corner strata
`Z_J` of a filtration of `X^+ = R_{>0}×∏Q_ℓ`, and Theorem 5.4 tried to kill
the corners by an irrational-rotation argument.  On the declared carrier
**there are no corner strata**: `C_S ≅ R^× × ∏_{p∈S_f}Z_p^×` is a locally
compact abelian **group** (Paper 43 Lemma 3.3), every coordinate is a unit,
nothing vanishes, and `T` is an integral of `F∘j_v` against `τ_v` over
`Q_v^×`, one place at a time (Paper 43 (8.6)).  Theorem 5.4 stays withdrawn
(D128 `C1`, verified and accepted) and is now **unnecessary**; §13 records the
whole of §§5.3–5.6, Cor. 5.5 and Cor. 5.7 as withdrawn with their referent.

---

## 6. `vol(Z_p^×) = \log p`, as a corollary

**[REBUILT, phase 132, round 1.  The previous Lemma 6.1 claimed three
independent fixings agreeing "with the Arakelov length"; D128 `C7` accepted
that two of them were stipulations and struck Remark 6.3.  The true theorem is
Paper 44's.]**

**Theorem 6.1 (`PROVED-IN-REPOSITORY`, Paper 44 Theorem 8bis.8 and
Corollary 8bis.8a).**  Declare the local multiplicative measures by
`vol_{d^*x_p}(Z_p^×) = c_p > 0` and `d^*x_∞ = dx/(2|x|)`, all other
conventions of Paper 43 §8.2 unchanged, and define the **local Tate residue**
of a place `v` as `Res_{s=0}ζ_v(s)`, `ζ_v(s) = ∫_{|x|_v ≤ 1}|x|_v^s d^*x_v`.
Then `ζ_p(s) = c_p/(1−p^{−s})` with residue `c_p/\log p` at `s = 0`, and
`ζ_∞(s) = 1/s` with residue `1`; so the local Tate residues agree at all
places **iff** `c_p = \log p` for every finite `p`.  The only remaining
freedom is one global positive scale, which rescales `I_A` and changes no
sign, no vanishing and no ratio.

**Corollary 6.2 (what the old Lemma 6.1 was really saying).**  Under
`c_p = \log p`, the following three numbers are equal to `\log p`:
(i) `vol_{d^*x}(p^kZ_p^×)`, by Theorem 6.1;
(ii) `Λ(p^k)`, by Paper 44 (3bis.8) — the atom mass identification;
(iii) `\deg_{det}\mathrm{Prim}_{p^k} = \log\#(Z/p)`, by Paper 44's degree law.
**No map, functor or pairing relating (iii) to (i) is exhibited**, here or in
Paper 44; the equality of (i) and (iii) is a numerical coincidence in the
declared normalization, and Remark 6.3 of the previous version — "the same
Arakelov degree" — stays **withdrawn** (D128 `C7`).  What (i) and (ii) share
is a theorem (Paper 44 Theorem 3bis.7); what (iii) shares with them is a
number.  ∎  `PROVED` as stated, with the negative half stated as strongly as
the positive half.

---

## 7. The archimedean place (clause C.4)

### 7.1 What is kept, and with which reading

**[REBUILT, phase 132, round 1.  Theorems 7.2–7.4 of the previous version are
**correct computations**; D128 `C5` struck their interpretive claims and this
version does not restate them.  The connection to Paper 43 is new.]**

The archimedean term of `T` is not a fixed-point index.  On the declared
carrier `C_S ≅ R^× × ∏Z_p^×` the real coordinate is the modulus direction, a
group; `W_∞` is Paper 43 (8.5∞), the regularized integral of `τ_∞` against the
profile, and its symbol is `\hat W_∞(0,τ)` of Theorem 9.7(b).  The following
three statements identify it spectrally.  **None of them is used in §9, §9bis,
§10 or §12**; they are the answer to clause C.4's "Gamma term", and they are
labelled as computations.

**Definition 7.1.**  `N_Γ` is the operator with simple spectrum
`{2m + ½ : m ≥ 0}`.  (`N_Γ` is **defined by its spectrum**; D128 `C5`.)

**Theorem 7.2 (the kernel is a heat trace).**  For `t > 0`,
`K(t) = e^{−t/2}/(1−e^{−2t}) = Σ_{m≥0}e^{−(2m+½)t} = \mathrm{Tr}\,e^{−tN_Γ}`.
*Proof.*  Geometric series.  ∎  `PROVED` — a **consistency check**, since
`N_Γ` is defined by its spectrum, not a discovery.

**Theorem 7.3 (the zeta determinant).**  For `Re s > 0`,

    \det_ζ(N_Γ + s − ½) = \sqrt{2π}\,2^{½−s/2}/Γ(s/2).                 (7.1)

*Proof.*  `N_Γ+s−½` has simple spectrum `{2m+s}`, so
`ζ_{N_Γ,s}(w) = 2^{−w}ζ_H(w,s/2)`, regular at `w = 0`;
`ζ'_{N_Γ,s}(0) = −(\log 2)ζ_H(0,a) + ζ_H'(0,a)` with `a = s/2`.  Insert
`ζ_H(0,a) = ½ − a` and Lerch's `ζ_H'(0,a) = \log Γ(a) − ½\log 2π` and
exponentiate.  ∎  `PROVED`, using `CLASSICAL` import (E7) of §11.

**Honesty clause (D128 `C5`, carried into every use of Theorem 7.3).**  (7.1)
delivers `Γ(s/2)` **up to the scalar `\sqrt{2π}\,2^{½−s/2}`**, and the factor
`π^{−s/2}` of the completed zeta is **not** produced by `N_Γ`: to reach
`A_∞(s) = π^{−s/2}Γ(s/2)` one needs the extra scalar `\sqrt{π}(2π)^{−s/2}`.
The `\log π` of (7.2) below comes from P123.035's independently computed
finite part.  The slogan "one operator produces both" is withdrawn and is not
restated anywhere in this paper.

**Theorem 7.4 (the archimedean symbol, and its constant).**  With `W_∞` as in
Paper 43 (8.5∞),

    \hat W_∞(0,τ) = \log π − Re ψ(¼+iτ/2),                             (7.2)

and the constant of (8.5∞) reconciles as `γ + \log 4π + ψ(½) = \log π`, using
`ψ(½) = −γ − 2\log 2`.
*Proof.*  (7.2) is P123.035 (4.1) = Paper 43 Theorem 9.7(b); the constant is
the displayed identity, `\log 4π − \log 4 = \log π`.  ∎
`PROVED-IN-REPOSITORY`, constant re-verified here and numerically in §15.

### 7.2 The archimedean Tate residue, and the dictionary that makes it a
comparison

**[REBUILT, phase 132, round 1.  This is the archimedean half of "poles in the
same comparison", and it is new.]**

**Theorem 7.5 (the archimedean Tate residue is the local Tate residue).**  Put
`s = ½ + iτ`, so that `τ = i/2 ⟺ s = 0` and `τ = −i/2 ⟺ s = 1`, and
`ds = i\,dτ`.  Then, with `a(s) := ½\log π − ½ψ(s/2)`:

  (i) `\hat W_∞(0,τ) = a(s) + a(1−s)` as meromorphic functions;
  (ii) `a` has a simple pole at `s = 0` with residue exactly `1`, and no other
       pole in `Re s > −2`; hence `\hat W_∞(0,·)` has a simple pole at
       `τ = i/2` with residue `−i` and at `τ = −i/2` with residue `+i`,
       which is Paper 43 Theorem 9.7b(b) for `n = 0`;
  (iii) `Res_{s=0}\,a(s) = 1 = Res_{s=0}ζ_∞(s)`, `ζ_∞(s) = ∫_{|x|≤1}|x|^s
       dx/(2|x|) = 1/s` — the archimedean local Tate zeta of Paper 44
       Theorem 8bis.8(ii).  The same holds at every finite place with
       `f_p(s) := (\log p)p^{−s}/(1−p^{−s})`: `Res_{s=0}f_p = 1 =
       Res_{s=0}ζ_p(s)` **precisely when `c_p = \log p`** (Theorem 6.1).

*Proof.*  (i)  On `s = ½+iτ` with `τ` real, `a(s)+a(1−s) =
\log π − ½[ψ(¼+iτ/2) + ψ(¼−iτ/2)] = \log π − Re ψ(¼+iτ/2)` since
`ψ(\bar z) = \overline{ψ(z)}`; this is (7.2).  Both sides are meromorphic in
`s`, and they agree on a line, hence everywhere.
(ii)  `ψ(z) = −1/z + O(1)` at `z = 0`, so `a(s) = −½·(−2/s) + O(1) = 1/s +
O(1)`; the next pole of `ψ(s/2)` is at `s = −2`.  Transporting to `τ`:
if `G(s)` has residue `r` at `s = s_0` then, as a function of `τ` with
`s = ½+iτ`, its residue at `τ_0 = (s_0−½)/i` is `r·ds/dτ|^{-1}`, i.e.
`r/i = −ir`.  With `r = 1` at `s = 0` this is `−i` at `τ = i/2`; the pole at
`s = 1` comes from `a(1−s)` with residue `−1` in `s`, hence `+i` in `τ` at
`τ = −i/2`.
(iii)  `∫_{|x|≤1}|x|^s\,dx/(2|x|) = 2·½∫_0^1 x^{s−1}dx = 1/s`, residue `1`;
the finite-place statement is Theorem 6.1's computation `ζ_p(s) =
c_p/(1−p^{−s})`, residue `c_p/\log p`, together with `1−p^{−s} = s\log p +
O(s²)` giving `Res_{s=0}f_p = 1`.  ∎  `PROVED`

**Remark 7.6 (this is what "poles in the same comparison" means at one
place).**  Theorem 7.5 says that the Tate pole of the *symbol* of `W_v` at
`τ = ∓i/2` is, place by place and under the dictionary `s = ½+iτ`, the pole at
`s = 0, 1` of the *local Tate zeta integral*, with the same residue at every
place — and that "the same at every place" is exactly Paper 44
Theorem 8bis.8's requirement, which forces `vol(Z_p^×) = \log p`.  The
**global** statement — what those poles do when summed over all places — is
§9bis, and its answer is not what a chart suggests.

---

## 8. The rulings and the polar packet (clause C.2)

### 8.1 The polar packet is the hyperbolic ruling form

**Theorem 8.1 (kept from the previous version; D128 confirmed it "clean";
re-proved here on the declared carrier).**  Let `B_T = C ⊕ C` with the
involution `(z_−,z_+)^♯ = (\bar z_+, \bar z_−)` and the Hermitian form
`β_T(z,w) = z_−\overline{w_+} + z_+\overline{w_−}`, matrix `[[0,1],[1,0]]` in
the basis `e_∓` — this is Paper 43 Theorem 9.1, and `M = (λ_−,λ_+) : D_A → B_T`
is a surjective continuous algebra map with `M(F^†) = M(F)^♯`.  For real
`F ∈ C_c^∞(R)`:

  (i) `M(Γ_F) = (Φ_F(1), Φ_F(0))`, and
      `β_T(M(Γ_F),M(Γ_F)) = 2Φ_F(0)Φ_F(1)`, which is **exactly** the polar
      packet `g(0)+g(1)` of the explicit formula (Theorem 9.4 below) and
      exactly `Φ_h(0) + Φ_h(1)` for `h = F⋆F^†`;
  (ii) `M(Γ_F) = 0` **iff** `Φ_F(0) = Φ_F(1) = 0`, i.e. iff `F` is primitive
       — the two linear Tate conditions of Paper 44 (8bis.9);
  (iii) `†` acts on `B_T` by `♯`, exchanging the two rulings.

*Proof.*  (i)  By Proposition 3.2, `λ_∓(Γ_F) = ∫F(s)e^{±s/2}ds`, so
`λ_−(Γ_F) = Φ_F(1)` and `λ_+(Γ_F) = Φ_F(0)`; this is (1.6).  For real `F`
these are real, so
`β_T(M,M) = λ_−\overline{λ_+} + λ_+\overline{λ_−} = 2Φ_F(0)Φ_F(1)`.  The
identification with the corpus's polar packet is P123.036 §1, which states it
as `M_+(F)\overline{M_-(F)} + M_-(F)\overline{M_+(F)}` and says explicitly it
is **not** `|M_+|²+|M_-|²`; with `M_+ = Φ_F(1)`, `M_- = Φ_F(0)` (P124.013
(1.2)) the two displays are the same expression.  Finally
`Φ_h(s) = Φ_F(s)Φ_{F^†}(s) = Φ_F(s)Φ_F(1−s)` for real `F`, so
`Φ_h(0) = Φ_F(0)Φ_F(1) = Φ_h(1)`.
(ii) is (1.6) and P124.013 (1.3).  (iii) is Paper 43 Theorem 9.1's
`λ_∓(F^†) = \overline{λ_±(F)}`.  ∎  `PROVED`

**Remark 8.2 (a correction of record: the two rulings were labelled the wrong
way round).**  **[REBUILT, phase 132, round 1.  This refutes the lead
blueprint's clause C.2 as literally stated, and corrects the previous version
of this paper.]**  The previous version set `z(F) := (M_−(F),M_+(F)) =
(Φ_F(0),Φ_F(1))`, and the blueprint's clause C.2 asserts `z(F) = M(Γ_F)`.
**That identity is false.**  By (i), `M(Γ_F) = (λ_−,λ_+) = (Φ_F(1),Φ_F(0))`,
which is the **swap** of `z(F)`.  Counterexample: take real `F ∈ C_c^∞` with
`Φ_F(0) = 1`, `Φ_F(1) = 2` (possible, since a compactly supported smooth
function may have prescribed Mellin values at two distinct points — Paper 43
Theorem 9.1's surjectivity argument).  Then `z(F) = (1,2)` and
`M(Γ_F) = (2,1) ≠ (1,2)`.

The correct statement is `M(Γ_F) = σ(z(F))`, `σ` the swap.  **Every
consequence used in this paper survives**, because `β_T` is invariant under
`σ`: `β_T(σz,σw) = (σz)_-\overline{(σw)_+} + (σz)_+\overline{(σw)_-} =
z_+\overline{w_-} + z_-\overline{w_+} = β_T(z,w)`.  So Theorem 8.1(i),(ii),
(iii) are unaffected, as is every later use.  What *is* affected is any
sentence naming *which* ruling a given class approximates: with Paper 43's
convention, `λ_+(F_n) = 1` and `λ_-(F_n) → 0` for the spread family (9.21), so
`F_n → e_+`; and `λ_+(Γ_F) = Φ_F(0) = M_-(F)`, so `e_+` pairs with the
`s = 0` pole, not the `s = 1` pole.  The old Corollary 8.2's phrase "the two
rulings span a hyperbolic plane" is unaffected; its identification of `e_±`
with `M_±` is corrected here.

### 8.2 Where the rulings live

**Proposition 8.3 (typed, per Remark 3.3).**  The rulings are **not** classes
of `D_A`: by Paper 43 Theorem 9.13(a) there is no `D_A`-module splitting of
the Tate boundary inside `D_A`, so "the ruling component of a test class" must
be phrased through `M`.  They exist in the completion: by Paper 43
Theorem 9.14a the spread Tate families `F_n, G_n` of (9.21) satisfy
`J(F_n) → e_+^{dist} = (0,e_+)` and `J(G_n) → e_-^{dist} = (0,e_-)` in
`D_A' ⊕ B_T`, both limits in `N_A^{dist}`, and `D_A` acts on them by the two
Tate characters.  By Theorem 9.14c the plane `σ(B_T)` they span is exactly the
**scalar** radical `R_∂` of the completion, and by Theorem 9.14c′ it is
`I_A`-null along **every** admissible approximation — not merely along the
family (9.21).

*Proof.*  Citations, verbatim.  ∎  `PROVED-IN-REPOSITORY` (Paper 43
Thms. 9.13, 9.14a–c′).

**Corollary 8.4 (primitivity, geometrically).**  `Γ_F` is primitive
(`M(Γ_F) = 0`) iff the class `J(Γ_F) ∈ N_A^{dist}` has zero component in the
canonical splitting `N_A^{dist} = primitive ⊕ σ(B_T)` of Paper 43
Theorem 9.14b.  ∎  `PROVED`

**Warning 8.5 (no Hodge-index reading is available, and this paper does not
offer one).**  **[REBUILT, phase 132, round 1.  The previous Corollary 8.2
concluded "row D's target is, verbatim, the Hodge index statement for `N_A`".
Paper 43 Theorem 14.1 forbids that reading and this paper deletes it.]**  By
Paper 43 Theorem 14.1(a)–(d) with `c := 0`: `I_A` is **indefinite with
infinite index on both sides** on `N_A = D_A`, and `(D_A^{prim})^{⊥I_A} = 0`,
so there is no decomposition "hyperbolic plane ⊕ definite complement" to run
a Hodge index argument on.  By Paper 44 Theorem 8bis.4a the pure Frobenius
form fails positivity on the primitive sector at **every** finite chart.  The
only positivity statement equivalent to RH is Weil's criterion on the
primitive radial sector **in the colimit** (Paper 44 (8bis.10), `CLASSICAL`),
and what §9 adds is that row C now **proves** the identity underlying it
rather than citing it.  §14.4 states what row D inherits, and it is not a
Hodge index.

---

## 9. The explicit formula, proved; and the comparison theorem

### 9.1 What must be imported, and nothing else

**[REBUILT, phase 132, round 1.  This section replaces Theorem 9.2 of the
previous version, which was cited as `CLASSICAL` after D128 `C4` broke its
sketch.  Clause C.8 in its strong form requires the proof to be in the
repository, and it is written out here.  The imports are listed in §11 and
each is used only where named.]**

Facts about `ζ` used below, each named, each `CLASSICAL`:

* **(E1)** `ζ'/ζ(s) = −Σ_{n≥2}Λ(n)n^{−s}`, absolutely convergent for
  `Re s > 1` (Euler product).
* **(E2)** `ξ(s) := ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)` is entire, `ξ(s) = ξ(1−s)`,
  and the zeros of `ξ` are exactly the nontrivial zeros of `ζ` with the same
  multiplicities; `ζ` has a simple pole at `s = 1`, `ζ(0) = −½`, and `ξ` is
  regular and nonzero at `s = 0` and `s = 1`.  **[REBUILT, phase 132, round 2,
  finding `LF1` of `R132.003`.]**  Also: **no nontrivial zero of `ζ` is real**
  — `ζ(σ) ≠ 0` for `σ ∈ (0,1)` — used **only** at (10.1).
* **(E3a)** `ξ` has order `1`, with the Hadamard product and the resulting
  partial-fraction expansion `ξ'/ξ(s) = Σ_ρ\big(\frac1{s−ρ}+\frac1ρ\big) + B`,
  locally uniformly off the zeros.
* **(E3b)** *Local* Riemann–von Mangoldt: `N(T+1) − N(T) = O(\log T)`.  Hence
  for each `j` there is `X_j ∈ [j,j+1]` whose distance to every ordinate of a
  zero is `≥ c/\log j` (the `O(\log j)` ordinates in `[j,j+1]` cannot block
  every subinterval of length `≍ 1/\log j`).
* **(E3c)** Consequently `ξ'/ξ(σ ± iX_j) = O(\log^2 X_j)` uniformly for `σ` in
  a fixed vertical strip, by (E3a) together with (E3b): the `O(\log X_j)`
  nearby terms each contribute `O(\log X_j)` and the rest is `O(\log X_j)`.
* **(E3d)** *Global* Riemann–von Mangoldt: `N(T) = O(T\log T)`.  Used **only**
  in Theorem 10.4(iii) and Remark 9.8.

  **[REBUILT, phase 132, round 2, finding `M2` of `R132.002` = `LF2` of
  `R132.003`.  Round 1 presented (E3b) and (E3c) as *consequences* of
  `N(T) = O(T\log T)`.  They are not: a bound on `N(T)` says nothing about
  `N(T+1)−N(T)`, and the `O(\log^2)` bound needs the Hadamard partial fraction
  in addition.  Under clause C.8 in its strong form — every analytic input
  either proved here or **named** — presenting a strictly stronger classical
  input as a consequence of a weaker one is exactly the failure mode the clause
  exists to prevent.  The statements are true; the round-1 ledger was wrong.
  Sources: Davenport, *Multiplicative Number Theory*, ch. 15–17 (Hadamard
  product and `ξ'/ξ`; the zero-counting lemma; the strip estimate); equivalently
  Titchmarsh, *The Theory of the Riemann Zeta-Function*, §§9.6, 3.1.]**
* **(E4)** `ψ(z) = O(\log|z|)` for `|z| → ∞` away from the poles (Stirling),
  and `ψ(z) = −1/z + O(1)` at `z = 0`.
* **(E5)** Fourier inversion and Plancherel on `R`.

### 9.2 The test function and its transform

**Lemma 9.1.**  Let `F ∈ C_c^∞(R)` be real with `supp F ⊆ [−T,T]`, and
`Φ_F(s) = ∫F(t)e^{(s−½)t}dt`.  Then `Φ_F` is entire; `Φ_F(\bar s) =
\overline{Φ_F(s)}`; and for every `N ≥ 0` there is `C_N = ‖F^{(N)}‖_{L^1}`
with

    |Φ_F(σ+iτ)| ≤ C_N\,e^{T|σ−½|}\,|s−½|^{−N}    (s = σ+iτ, s ≠ ½).     (9.1)

Put `g(s) := Φ_F(s)Φ_F(1−s)`.  Then `g` is entire, `g(1−s) = g(s)`,
`g(\bar s) = \overline{g(s)}`, `g(½+iτ) = |\hat F(τ)|² ≥ 0`, and for every `N`

    |g(σ+iτ)| ≤ C_N^2\,e^{2T|σ−½|}\,|s−½|^{−2N}.                       (9.2)

Moreover, with `h := F ⋆ F^†`, `h` is real, **even**, supported in `[−2T,2T]`,
`\hat h = |\hat F|²`, `h(a) = ⟨S_aF,F⟩` and `Φ_h(s) = g(s)`.

*Proof.*  Entirety and the reflection identity are immediate from the integral.
(9.1): integrate by parts `N` times, the boundary terms vanishing by compact
support, giving `Φ_F(s) = (½−s)^{−N}∫F^{(N)}(t)e^{(s−½)t}dt` up to sign, and
bound the integral by `‖F^{(N)}‖_{L^1}e^{T|σ−½|}`.  `g(1−s) = g(s)` is the
definition.  `g(\bar s) = \overline{g(s)}` uses `F` real.  On `s = ½+iτ`,
`Φ_F(½+iτ) = ∫F(t)e^{iτt}dt = \hat F(−τ)` and `Φ_F(½−iτ) =
\overline{Φ_F(½+iτ)}` by reality, so `g = |\hat F(−τ)|²`; and `|\hat F|` is
even because `F` is real.  For `h`: `h(a) = ∫F(s)\overline{F(s−a)}ds =
⟨S_aF,F⟩`; reality of `F` gives `h` real and `h(−a) = h(a)`; the support and
`\hat h = |\hat F|²` are standard; and
`Φ_h(s) = Φ_F(s)Φ_{F^†}(s) = Φ_F(s)Φ_F(1−s)`, since
`Φ_{F^†}(s) = ∫\overline{F(−t)}e^{(s−½)t}dt = \overline{∫F(u)e^{(\bar s−½)(−u)}du}
= \overline{Φ_F(1−\bar s)} = Φ_F(1−s)` for real `F`.  ∎  `PROVED`

### 9.3 The contour, and the argument principle

**Lemma 9.2 (the zero sum as a contour integral).**  Fix `c > 1` and let
`(X_j)` be as in (E3b).  Let `R_j` be the rectangle with vertices
`1−c ∓ iX_j`, `c ∓ iX_j`, traversed counterclockwise.  Then

    Σ_{|Im ρ| < X_j} g(ρ)
      = (1/2πi)\oint_{R_j} g(s)(ξ'/ξ)(s)ds
      \xrightarrow[j→∞]{} (1/2πi)\Big[∫_{L_c} − ∫_{L_{1−c}}\Big]g(s)(ξ'/ξ)(s)ds,
                                                                       (9.3)

`L_a` the line `Re s = a` oriented upward, both line integrals absolutely
convergent, and the left-hand side converges to `Σ_ρ g(ρ)` **in the symmetric
order `|Im ρ| ≤ X`**, the zeros counted with multiplicity.

*Proof.*  All zeros of `ξ` lie in `0 ≤ Re s ≤ 1 ⊂ (1−c, c)` (E2, and the
Euler product for `Re s > 1` with the functional equation), and `g` is entire
(Lemma 9.1), so the only poles of `g·ξ'/ξ` inside `R_j` are the zeros of `ξ`
there, each simple as a pole of `ξ'/ξ` with residue the multiplicity.  The
argument principle gives the first equality; no zero lies on `∂R_j` because
`X_j` avoids all ordinates (E3b), and the vertical sides at `Re s = 1−c, c`
carry no zero.  Horizontal sides: by (E3c) `|ξ'/ξ| = O(\log^2 X_j)` there — an
import, **not** a consequence of (E3d) — and
by (9.2) with `N = 2`, `|g(σ ± iX_j)| ≤ C_2^2e^{2T(c−½)}X_j^{−4}`, so each
horizontal integral is `O(X_j^{−4}\log^2X_j) → 0`.  Absolute convergence of
the two line integrals: on `L_c`, `ξ'/ξ` is `O(\log|s|)` (it equals
`1/s + 1/(s−1) − ½\log π + ½ψ(s/2) + ζ'/ζ(s)`, each summand being
`O(\log|s|)` by (E1) and (E4)), and `g` decays faster than any power by (9.2);
same on `L_{1−c}` by the functional equation `ξ'/ξ(1−s) = −ξ'/ξ(s)` (E2).  ∎
`PROVED` using (E2), (E3a), (E3b), (E3c).

**Lemma 9.3 (the reflection).**  For any function `A` meromorphic and
integrable against `g` on both lines,

    \Big[∫_{L_c} − ∫_{L_{1−c}}\Big]g(s)A(s)ds = ∫_{L_c}g(s)[A(s) − A(1−s)]ds.
                                                                       (9.4)

In particular, since `(ξ'/ξ)(1−s) = −(ξ'/ξ)(s)` (differentiate `ξ(s)=ξ(1−s)`),

    \Big[∫_{L_c} − ∫_{L_{1−c}}\Big]g\,\frac{ξ'}{ξ}\,ds
       = 2∫_{L_c}g(s)\frac{ξ'}{ξ}(s)\,ds.                              (9.5)

*Proof.*  Substitute `s = 1−u` in the second integral: as `s` runs upward
along `L_{1−c}`, `u` runs **downward** along `L_c` and `ds = −du`, so
`∫_{L_{1−c}}gA\,ds = ∫_{L_c}g(1−u)A(1−u)du = ∫_{L_c}g(u)A(1−u)du`, using
`g(1−u) = g(u)` (Lemma 9.1).  ∎  `PROVED`

### 9.4 The explicit formula

**Theorem 9.4 (Weil's explicit formula, `PROVED` here).**  Let
`F ∈ C_c^∞(R)` be real with `supp F ⊆ [−T,T]`, `h = F⋆F^†`, and let the zero
sum be taken in the symmetric order `|Im ρ| ≤ X`.  Then

    Σ_ρ Φ_F(ρ)Φ_F(1−ρ)
      = 2Φ_F(0)Φ_F(1)
        + (1/2π)∫_R |\hat F(τ)|²\big[Re ψ(¼+iτ/2) − \log π\big]dτ
        − Σ_{2≤n<e^{2T}} Λ(n)n^{−1/2}\big[h(\log n) + h(−\log n)\big],  (9.6)

i.e. `Σ_ρ g(ρ) = 2Φ_F(0)Φ_F(1) + ⟨𝒜F,F⟩` in the notation (1.5)–(1.7), the
prime sum being **finite**.

*Proof.*  By Lemma 9.2 and (9.5),

    Σ_ρ g(ρ) = \frac{1}{πi}∫_{L_c}g(s)\frac{ξ'}{ξ}(s)\,ds .            (9.7)

On `L_c` (`c > 1`) expand, from `\log ξ(s) = \log½ + \log s + \log(s−1)
− \tfrac s2\log π + \log Γ(s/2) + \log ζ(s)`,

    \frac{ξ'}{ξ}(s) = A_0(s) + A_Γ(s) + \frac{ζ'}{ζ}(s),
    A_0(s) := \frac1s + \frac1{s−1},   A_Γ(s) := −\tfrac12\log π + \tfrac12ψ(s/2),
                                                                       (9.8)

an identity of meromorphic functions, valid at every `s` where no term has a
pole; in particular on `L_c`.  Each of the three terms is integrable against
`g` on `L_c` (Lemma 9.2's estimate, with (E1) and (E4)), so (9.7) splits into
three.

**(a) The polar terms.**  `A_0(1−s) = \frac1{1−s} + \frac1{−s} = −A_0(s)`, so
by (9.4), `\frac1{πi}∫_{L_c}gA_0 = \frac{1}{2πi}\big[∫_{L_c}−∫_{L_{1−c}}\big]
gA_0\,ds`.  The function `gA_0` is meromorphic in the closed strip
`1−c ≤ Re s ≤ c` with exactly two poles, both simple, at `s = 0` and `s = 1`
(recall `1−c < 0` since `c > 1`), with residues `g(0)` and `g(1)`; the
rectangle `R_j` of Lemma 9.2 has vanishing horizontal contributions by (9.2),
so the bracket equals `2πi(g(0)+g(1))`.  Hence

    \frac1{πi}∫_{L_c}gA_0\,ds = g(0)+g(1) = 2Φ_F(0)Φ_F(1),

by `g(0) = Φ_F(0)Φ_F(1) = g(1)` (Lemma 9.1).

**(b) The Gamma term.**  `A_Γ` is holomorphic in `Re s > 0`, and by (E4)
`A_Γ(s) = O(\log|s|)` there, away from `s=0`.  Together with (9.2) this lets
the line `L_c` be shifted to `L_{1/2}`: apply Cauchy's theorem on the
rectangle `[½,c]×[−X_j,X_j]`, whose horizontal sides contribute
`O(X_j^{−4}\log X_j) → 0`, and whose interior contains no pole of `gA_Γ`.
Hence

    \frac1{πi}∫_{L_c}gA_Γ\,ds = \frac1{πi}∫_{L_{1/2}}gA_Γ\,ds
      = 2·\frac1{2π}∫_R g(½+iτ)\big[−\tfrac12\log π + \tfrac12ψ(¼+iτ/2)\big]dτ,

using `s = ½+iτ`, `ds = i\,dτ` and `\frac1{2πi}(i\,dτ) = \frac{dτ}{2π}`.  Now
`g(½+iτ) = |\hat F(τ)|²` is **even** in `τ` (Lemma 9.1) and
`ψ(¼−iτ/2) = \overline{ψ(¼+iτ/2)}`, so the odd imaginary part integrates to
zero and

    \frac1{πi}∫_{L_c}gA_Γ\,ds
      = \frac1{2π}∫_R|\hat F(τ)|²\big[Re ψ(¼+iτ/2) − \log π\big]dτ ,

which is the second line of (9.6), i.e. `⟨(g_Γ(D)−m_0)F,F⟩` of (1.7).

**(c) The prime terms.**  On `L_c`, (E1) gives
`ζ'/ζ(s) = −Σ_{n≥2}Λ(n)n^{−s}` with `Σ_nΛ(n)n^{−c} < ∞`; since
`∫_{L_c}|g| < ∞` (Lemma 9.2), Fubini permits term-by-term integration:

    \frac1{πi}∫_{L_c}g\frac{ζ'}{ζ}ds
      = −Σ_{n≥2}Λ(n)\cdot\frac1{πi}∫_{L_c}g(s)n^{−s}ds .

**This is the step D128 `C4` broke, and here is why it is now legitimate.**
The integrand `g(s)n^{−s}` is **entire** — `g` is entire (Lemma 9.1) and
`n^{−s}` is entire — so the line may be shifted from `L_c` to `L_{1/2}` with
no residue whatever: `ζ'/ζ` has already been expanded and is no longer
present, so no zero of `ζ` is crossed.  (Cauchy on `[½,c]×[−X_j,X_j]`;
horizontals `O(X_j^{−4}) → 0` by (9.2), uniformly in `n ≥ 2` since
`|n^{−s}| ≤ n^{−1/2}` on the strip.)  Hence, with `s = ½+iτ`,

    \frac1{πi}∫_{L_c}g(s)n^{−s}ds = 2n^{−1/2}\cdot\frac1{2π}∫_R\hat h(τ)e^{−iτ\log n}dτ
      = 2n^{−1/2}h(−\log n) ,

by `\hat h = |\hat F|² = g(½+i·)` and Fourier inversion (E5).  Since `h` is
**even** (Lemma 9.1 — this uses `F` real), `2h(−\log n) = h(\log n) +
h(−\log n)`, and the sum is finite because `supp h ⊆ [−2T,2T]`, so only
`n < e^{2T}` contributes.  Collecting,

    \frac1{πi}∫_{L_c}g\frac{ζ'}{ζ}ds
      = −Σ_{2≤n<e^{2T}}Λ(n)n^{−1/2}[h(\log n)+h(−\log n)] .

Adding (a), (b), (c) gives (9.6).  ∎  `PROVED`, using the `CLASSICAL` imports
(E1)–(E5) and nothing else.

**Corollary 9.4a (the same formula for an arbitrary real even test).**
**[REBUILT, phase 132, round 2, minor `m1` of `R132.002`: `\{|\hat F|² : F
\text{ real}\}` is a **cone**, not a vector space, so (9.11) was not a linear
functional on anything.  The proof of Theorem 9.4 never uses positivity.]**
Let `h ∈ C_c^∞(R)` be **real and even**, `supp h ⊆ [−2T,2T]`, and put
`g := Φ_h`.  Then `g` is entire, `g(1−s) = g(s)`, `g(½+iτ) = \hat h(τ)` is real
(not necessarily `≥ 0`), and

    Σ_ρ Φ_h(ρ) = Φ_h(0) + Φ_h(1)
        + \frac1{2π}∫_R \hat h(τ)\big[Re ψ(¼+iτ/2) − \log π\big]dτ
        − Σ_{2≤n<e^{2T}} Λ(n)n^{−1/2}\big[h(\log n)+h(−\log n)\big] .   (9.6a)

Theorem 9.4 is the case `h = F⋆F^†`, where `g(s) = Φ_F(s)Φ_F(1−s)` and
`\hat h = |\hat F|²`.

*Proof.*  Verbatim the proof of Theorem 9.4, with Lemma 9.1 replaced by: `Φ_h`
is entire and satisfies (9.1) with `C_N = ‖h^{(N)}‖_{L^1}` and `T ↦ 2T` (same
integration by parts); `g(1−s) = g(s)` **is** the evenness of `h`, since
`Φ_h(1−s) = ∫h(t)e^{(½−s)t}dt = ∫h(−u)e^{(s−½)u}du`; and
`g(½+iτ) = ∫h(t)e^{iτt}dt = \hat h(−τ) = \hat h(τ)`, real because `h` is real
and even.  Step (a) uses only `g(0) = Φ_h(0)`, `g(1) = Φ_h(1)`; step (b) uses
only that `g(½+i·)` is **even and real**, which is where `|\hat F|²`'s
positivity was never needed; step (c) uses only Fourier inversion and the
evenness of `h`.  ∎  `PROVED`

**Remark 9.8 (the zero sum is absolutely convergent for this test class).**
**[REBUILT, phase 132, round 2, note `n1` of `R132.002`.]**  For
`h ∈ C_c^∞(R)` real and even, (9.1) applied to `Φ_h` with `N = 2` gives
`|Φ_h(ρ)| ≤ C_2 e^{2T|β−½|}|ρ−½|^{−2} = O(|γ_ρ|^{−2})` uniformly for `ρ` in
the critical strip; by (E3d), `Σ_ρ|γ_ρ|^{−2} < ∞` (partial summation against
`N(T) = O(T\log T)`).  So `Σ_ρ Φ_h(ρ)` converges **absolutely**, and D128
`C10`'s symmetric-order requirement — which is genuinely needed for the
argument-principle step of Lemma 9.2, and is stated there — imposes no
restriction on the *value*.  This removes an apparent fragility from (9.9),
(9.11) and §14.4: none of them depends on an order of summation.

**Remark 9.5 (three corrections to the route, recorded).**  **[REBUILT,
phase 132, round 1.]**
(1) The blueprint's step 3 says the single integral `∫_{(c)}g(s)n^{−s}ds`,
shifted to `Re s = ½`, "gives `Λ(n)n^{−1/2}⟨(S_{\log n}+S_{−\log n})F,F⟩`".
It does **not**: it gives `n^{−1/2}h(−\log n) = n^{−1/2}⟨S_{−\log n}F,F⟩`,
**half** of that.  The other half comes from the `L_{1−c}` line via (9.5), and
the two halves coincide only because `h` is even, i.e. only because `F` is
real.  Both facts are used explicitly above.
(2) The termwise split of (9.7) must be made **on `L_c` only**; one may not
split `[∫_{L_c}−∫_{L_{1−c}}]` termwise, because `−½\log π` is entire and
symmetric, so that combination would annihilate the `\log π` the formula needs.
This is why (9.5) is applied first and the expansion second.
(3) The horizontal-side estimate needs `N ≥ 2` in (9.1), i.e. two derivatives
of `F`; `F ∈ C_c^∞` is ample, but a merely continuous compactly supported `F`
would not do, and the theorem is stated for `C_c^∞`.

### 9.5 The comparison theorem: the spectral side is the symbol of the colimit
trace

**Theorem 9.6 (row C's comparison theorem).**  **[REBUILT, phase 132,
round 1.  Hypotheses carried explicitly: `F` real and `C_c^∞`; `c := 0`
(Paper 43 Def. 8A.7d); the trace is the **colimit** trace `T_∞` on `D_A^∞`,
convention (C1) of Paper 44; the zero sum is symmetric.]**  Let
`F ∈ C_c^∞(R)` be real, `h = F⋆F^†`, and let `Γ_F, Γ_h ∈ D_A^{rad}` be the
radial classes of Definition 3.1.  Then

    I_∞(Γ_F,Γ_F) = T_∞(Γ_{F⋆F^†})
      = 2Φ_F(0)Φ_F(1) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ)
      = β_T\big(M(Γ_F),M(Γ_F)\big) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ) ,              (9.9)

and consequently, **on the primitive radial sector** `M(Γ_F) = 0`,

    I_∞(Γ_F,Γ_F) = −Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = −Q(F) = −q(F) = B_nuc(F,F).    (9.10)

At a fixed finite chart `S`, (9.9)–(9.10) hold verbatim provided
`R(Γ_h) < \log ℓ_{next}(S)` (Paper 43 Theorem 8A.7c(e)); outside that window
the left-hand side omits the atoms at the primes `ℓ ∉ S_f` and the identity is
**false** at a chart.

*Proof.*  **[REBUILT, phase 132, round 2, finding `M4`: the trace evaluation is
now Lemma 5.1a, which carries **no** support hypothesis.  Note `h(0) =
‖F‖_{L²}² > 0`, so `0 ∈ supp h` in **every** application of this theorem, and
Theorem 5.1 (= Paper 44 Thm 3bis.7) may **not** be cited here.]**  By
Proposition 3.2, `Γ_F ⋆ Γ_F^† = Γ_{F⋆F^†} = Γ_h`, and `h` is real and even
(Lemma 9.1).  By **Lemma 5.1a** in the colimit form (Paper 43 Theorem 8A.7c,
convention (C1)), with `\hat h(−τ) = \hat h(τ) = |\hat F(τ)|²` (Lemma 9.1) and
`\hat W_∞(0,τ) = \log π − Re ψ(¼+iτ/2)` (Theorem 7.4),

    T_∞(Γ_h) = Σ_{n≥2}Λ(n)n^{−1/2}[h(\log n)+h(−\log n)]
               + \frac1{2π}∫_R|\hat F(τ)|²\big[\log π − Re ψ(¼+iτ/2)\big]dτ,

both terms absolutely convergent, the first finite.  This is **minus** the
second and third groups of (9.6).  Adding
`2Φ_F(0)Φ_F(1)` to both sides of (9.6) and rearranging gives (9.9); the
identification of the polar packet with `β_T(M,M)` is Theorem 8.1(i).  For
(9.10), `M(Γ_F) = 0` is primitivity (Theorem 8.1(ii)), and the three
right-hand equalities are Lemma 1.3.  The chart clause is Theorem 8A.7c(a),(e)
of Paper 43 and Paper 44 (C1), stated there in exactly these words.  ∎
`PROVED`

**Corollary 9.6a (`c = 0` is the unique constant compatible with the Weil
comparison; D128 `C9` closed).**  **[REBUILT, phase 132, round 2, finding `M1`
of `R132.002`.  This is a **strengthening**: Paper 43 Definition 8A.7d
*declares* `c := 0` and gave, at the time this corollary was written, four
reasons of which **none** was a derivation.  Row C now derives it — and the
phase-132 edit this paper authorized has since rewritten Paper 43
Definition 8A.7d to read that reasons (i)–(iii) are normalization choices and
are **not** derivations, while reason (iv) — which cites this corollary — **is**
one.  **[phase 133, PANEL_2 MINOR-5: the preamble quoted "none of [its four
reasons] is a derivation" as current text of Paper 43; that quotation became
stale with the phase-132 edit.  Non-circularity is unaffected: this
corollary's proof uses only Paper 43's family (8.4) and this paper's
Theorem 9.4.]**]**  Let `c ∈ R` be arbitrary and let
`T^{(c)} := Σ_v W_v + c·F(1)` be the corresponding member of Paper 43's family
(8.4), with `I^{(c)}(F,G) := T^{(c)}(F⋆G^†)` and `I_∞^{(c)}` its colimit.  Then
for every real `F ∈ C_c^∞(R)`:

  (i) `I_∞^{(c)}(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)
      + c\,‖Γ_F‖_{L²(C_S)}²`, and `‖Γ_F‖_{L²(C_S)}² = ‖F‖_{L²(R)}²`;
  (ii) the correction `c‖F‖²_{L²}` is **strictly positive for `c > 0` and
      strictly negative for `c < 0`, for every `F ≠ 0`**, and in particular it
      does **not** vanish on the primitive sector: `M(Γ_F) = 0` kills the
      *polar* packet, not the `L²` norm;
  (iii) consequently `c = 0` is the **unique** real constant for which
      `I_∞^{(c)}(Γ_F,Γ_F) = B_nuc(F,F)` for all real `F ∈ C_c^∞(R)`,
      equivalently for which (9.9) and (9.10) hold.

**[REBUILT, phase 132, round 3, finding `R1` of `R132.005`.  Round 2 appended a
third "equivalently" here — *"equivalently for which `I_∂ ≤ 0` on the primitive
radial sector is Weil's criterion"* — and it is **deleted**.  It asserted that
for every `c ≠ 0` the **sign condition** `I_∞^{(c)} ≤ 0` on primitive radial
classes ceases to be equivalent to RH.  Nothing in this paper proves that, and
for `c < 0` it is very likely **false**: the condition becomes
`Σ_ρΦ_F(ρ)Φ_F(1−ρ) ≥ c‖F‖²`, which is pointwise weaker than Weil positivity but
is plausibly still equivalent to RH, because under `¬RH` the negative tests of
`106_11` (Theorem 10.4) have no fixed lower bound in units of `‖F‖²` — the
ratio is not scale-limited, since `F ↦ λF` scales both sides by `λ²` and the
target quartet's contribution can be made to dominate `‖F‖²` by concentration.
A `PROVED` corollary may not carry an unproved biconditional, least of all the
sentence the label travels with.  **What is proved is uniqueness at the level
of the identity**, which is all D128 `C9` asks and all §14.4 uses.  The
statement of Paper 43 Definition 8A.7d's new reason (iv) is already phrased at
the identity level and needs no change.]**

*Proof.*  (i)  `T^{(c)} = T + c·(\cdot)(1)` by (8.4), so
`I^{(c)}(Γ_F,Γ_F) = I_A(Γ_F,Γ_F) + c·(Γ_F⋆Γ_F^†)(1)`.  Now
`(Γ_F⋆Γ_F^†)(1) = ∫_{C_S}Γ_F(u)\overline{Γ_F(u)}d^*u = ‖Γ_F‖_{L²}²` (the
computation in the proof of Paper 43 Theorem 9.8), and by Lemma 1.1 and the
disintegration `d^*w = dt⊗μ` with `μ` a **probability** measure (Paper 43
Theorem 9.14a's proof), `‖Γ_F‖_{L²(C_S)}² = ∫_R|F(−t)|²dt = ‖F‖_{L²(R)}²`.
The displayed identity is then Theorem 9.6 plus that term.  The same
conclusion is (14.1) of Paper 43 read on `𝔠_0`:
`I^{(c)}(Γ_F,Γ_F) = (1/2π)∫|\hat F|²(\hat T_S+c)dτ`, whose `c`-part is
`(c/2π)∫|\hat F|²dτ = c‖F‖²` by Plancherel (E5).
(ii)  `‖F‖_{L²}² > 0` for `F ≠ 0`, and nothing in `M(Γ_F) = (Φ_F(1),Φ_F(0))`
constrains it: e.g. `F = ΠG` of Corollary 10.2 is primitive and nonzero, so
`‖F‖² > 0` while `M(Γ_F) = 0`.
(iii)  Immediate from (i),(ii) and Theorem 9.6: two values of `c` give values
of `I_∞^{(c)}(Γ_F,Γ_F)` differing by `(c−c')‖F‖² ≠ 0`, so at most one `c`
satisfies (9.9), and `c = 0` does.  ∎  `PROVED`

**Remark 9.6b (what this does to Paper 43 Definition 8A.7d, and to D128 `C9`).**
**[REBUILT, phase 132, round 2.]**  Three statements, in order.

1. *The normalization is load-bearing, and round 1 said the opposite.*  Every
   theorem of §§9, 9bis, 10, 12 — and therefore §14.4's "row D's target implies
   RH" — is a statement about row A's declared trace **with `c := 0`**.  For any
   other `c`, (9.9) reads `I_∞^{(c)}(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) −
   Σ_ρΦ_F(ρ)Φ_F(1−ρ) + c‖F‖²`, so the **identity** (9.9)–(9.10) — and with it
   §14.4 item 4's route from row D's target to RH — is available only for
   `c = 0`.  **[REBUILT, phase 132, round 3, `R1`: no claim is made about
   whether the *sign condition* `I_∞^{(c)} ≤ 0` remains equivalent to RH for
   `c ≠ 0`; that biconditional is unproved and is probably false for `c < 0`.]**
   Round 1's §14.4 sentence "nothing in row C depends on it" was **false** and
   is withdrawn (§13, W45.14).
2. *But the constant is no longer a declaration.*  Paper 43 Definition 8A.7d
   offers four reasons for `c := 0` and states that "none of them is a
   derivation"; its reason (iv) is "it agrees with the convention of Paper 45,
   `χ_A = Σ_pW_p + W_∞`" — and `χ_A` is exactly the assembly this paper
   withdraws (§13, W45.3), so reason (iv) points at a withdrawn object
   (`R132.002` note `n5`).  Corollary 9.6a replaces it: **`c = 0` is derived as
   the unique constant compatible with the explicit formula.**  Reasons (i)–(iii)
   of 8A.7d are independent and stand; reason (iv) is struck and replaced by
   "derived: Paper 45 Corollary 9.6a".  That one-sentence edit has been made in
   Paper 43 and is recorded in §14.5 below.
3. *D128 `C9` is thereby closed, in the only form in which it can be closed.*
   `C9` said `I_A` is well defined modulo `R·‖·‖²` and that "for a **sign**
   statement that is not harmless".  It is exactly right, and Corollary 9.6a is
   the answer: not a computation of the cutoff constant, but a proof that **the
   Weil comparison itself pins the normalization**.  What remains open is a
   different and unrelated quantity — Paper 43 Theorem 8.10 / Remark 8A.7e's
   comparison constant `c_cut`, which measures the declared trace against an
   *imported* analytic regularization whose own coefficient P123.035 §6 forbids
   citing.  `c_cut` is undetermined in Paper 43 and is **not** the `c` of
   Corollary 9.6a; §14.4 states both, separately.

**Theorem 9.6′ ("the spectral side is the limit of the chart symbols").**
**[REBUILT, phase 132, round 2: the title says *limit of the chart symbols*,
not "symbol of the colimit trace".  The two are different objects and the
difference is the whole of §9bis: `T̂_S` is a genuine function on `𝔠_0` and
this theorem is about the limit of the numbers `L_S(h)`; the **continued
Euler-product symbol** `A` of Definition 9bis.1a is a different object again,
and is not a limit of the `T̂_S` where those live (Corollary 9bis.3).]**  Fix a
chart `S` and let `T̂_S` be Paper 43's symbol on the principal component `𝔠_0`,
a real-analytic function (Theorem 9.7).
**[REBUILT, phase 132, round 2, findings `LF3` of `R132.003` and `m1` of
`R132.002`: the domain is now a **vector space**, the mode of convergence is
named, and continuity is explicitly **not** claimed.]**  Let
`𝓔 := C_c^∞(R)^{even,\,real}` and for `h ∈ 𝓔` let
`L_S(h) := (1/2π)∫_R\hat h(τ)\,\hat T_S(𝔠_0,τ)\,dτ = T_S(Γ_h)`.  Then, as `S ↑`
along any exhaustion of the primes, the sequence `L_S(h)` is **eventually
constant for every `h ∈ 𝓔`** — constant for every `S` containing all primes
`ℓ ≤ e^{R(Γ_h)}` — with common value `L_∞(h) = T_∞(Γ_h)`, and

    L_∞(h) = Φ_h(0) + Φ_h(1) − Σ_ρ Φ_h(ρ),   h ∈ 𝓔 ,                  (9.11)

a **linear** functional on `𝓔`.  Theorem 9.6 is the case `h = F⋆F^†`, where
(9.11) is `2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)`.  This is the explicit formula
and nothing more.  *Two things are **not** claimed*: no continuity of `L_∞` in
any topology on `𝓔` is asserted (so the word "distribution" is used here only
informally, and clause C.4 does not rest on it), and the convergence is
pointwise-in-`h` eventual constancy — which is **stronger** than convergence in
any topology pointwise, and **weaker** than uniform convergence on bounded
sets, neither of which is claimed.  The limit is **not** given
by integration against a function: at `τ = 0`,
`\hat W_{fin}^∞(0) = Σ_p(\log p)\frac{2p^{−1/2}}{1−p^{−1/2}} = +∞`
(Paper 44 Remark 8bis.4b(1)).  Under RH one may write (9.11) as
`−Σ_ρ δ_{γ_ρ}` tested against `|\hat F|²` plus the polar functional, but
**that rewriting is a statement about zeros and this paper does not assert
it**; (9.11) is asserted, and it is unconditional.

*Proof.*  `L_S(h) = T_S(Γ_h)` is Lemma 5.1a together with Paper 43
Theorem 9.7(d); linearity of `h ↦ L_∞(h)` is linearity of `T_∞` and of
`h ↦ Γ_h` (Proposition 3.2).  Eventual constancy: by Paper 43
Theorem 8A.7c(a), `W_ℓ(J_{ST}Γ_h) = 0` for every prime `ℓ` with
`\log ℓ > R(Γ_h)`, so the sequence is constant for all `S` containing every
prime `ℓ ≤ e^{R(Γ_h)}`, with common value `T_∞(Γ_h)` — the convergence is
eventually **exact**, not merely convergent.  The value (9.11) is
Corollary 9.4a rearranged (add `Φ_h(0)+Φ_h(1)` to (9.6a) and use Lemma 5.1a).
The divergence statement is the cited remark of Paper 44, and it is what
forbids calling the limit an integration against a function.  ∎  `PROVED`

**Remark 9.7 (clause C.7 checked line by line).**  No step of §§9.1–9.5 uses
the location of any zero.  (E2) uses only that the zeros of `ξ` are the
nontrivial zeros of `ζ` (and, at (10.1) only, that none of them is real);
(E3a)–(E3d) use only their density and the Hadamard product; Lemma 9.2 chooses
`X_j` to avoid ordinates, which requires no knowledge of where they are;
§9.4(c) shifts contours only for **entire** integrands.  The zeros appear in
the conclusion, which is the comparison theorem itself — precisely what PLAN
§7 permits: *"Se pueden usar los ceros en el teorema de comparación de la
fórmula explícita; lo prohibido es asumir su posición para demostrar el
signo."*  No sign is proved anywhere in this paper.

### 9.6 Order of limits (clause C.5)

**[REBUILT, phase 132, round 1, on the true carrier.]**

| # | limit | status on the declared carrier |
|---|---|---|
| 1 | the local cutoff `L_p → ∞` | **no limit occurs.**  On `D_A^{off}` Paper 43 Theorem 8.8 gives `T` as an absolutely convergent integral with **no** counterterm and **no** limiting operation; for radial `Γ_h` with `0 ∉ supp h`, Paper 44 Theorem 3bis.7 makes the finite part a finite sum outright |
| 2 | the unit packet | **vanishes identically** on radial classes, pointwise, with no smallness hypothesis (Paper 44 Thm. 3bis.7, proof, step (1)) |
| 3 | the chart `S ⊆ T` | **stabilizes exactly**: Paper 43 Thm. 8A.7c(a),(b) — the correction terms are identically zero for `\log ℓ > R(Γ_h)`, and `T_∞` is the common value.  Convention (C1) |
| 4 | the sum over primes | **finite** for each test, by 3 and by `supp h` compact |
| 5 | the window `T` | **exact cutoff**: `h(±\log n) = 0` for `\log n > 2T` (Lemma 9.1); no tail estimate |
| 6 | the archimedean integral `∫_0^∞K(t)[\cdots]dt` | absolutely convergent: the bracket of (8.5∞) is `O(t)` at `t↓0` by the `2b(0)e^{−t/2}` subtraction (Paper 43 writes `b(1)`, the value at the **identity class**, which is `t = 0` in the logarithmic coordinate; **[REBUILT, phase 132, round 2, minor `m7`]**) and `K(t) = O(1/t)`, and vanishes for large `t` by compact support (Paper 43 (8.5∞); for `0∉supp h` there is no subtraction at all) |
| 7 | the zero sum `Σ_ρ` and the contour | Lemma 9.2: symmetric order, horizontal sides `→ 0` along `(X_j)` by (E3b), (E3c) and (9.2), verticals absolutely convergent.  **[REBUILT, phase 132, round 2, `M2`: the certificate is (E3c), a named import, not a consequence of (E3d).]**  By Remark 9.8 the sum is in fact **absolutely** convergent for this test class, so the symmetric order is harmless |
| 8 | the shift `L_c → L_{1/2}` | Theorem 9.4(b),(c): **no residue is crossed**, the integrands being holomorphic in `Re s ≥ ½` (b) resp. entire (c) |
| 9 | the interchange `Σ_n ↔ ∫_{L_c}` | Fubini, justified by `Σ_nΛ(n)n^{−c} < ∞` and `∫_{L_c}|g| < ∞` |

**No two limits are interchanged anywhere.**  Items 1–5 are exact identities or
eventually-constant sequences; 6, 7, 8, 9 are single limits with an
absolute-convergence certificate each, and none of them is nested inside
another.  `PROVED`

---

## 9bis. The poles, in the same comparison: the Tate residues of the continued
Euler-product symbol

**[REBUILT, phase 132, round 1.  This section is new, and it is what clause
C.4 was asking for when it said "the poles in the same comparison".  It
replaces the blueprint's §2.2 route, which I refute in Remark 9bis.5.]**

### 9bis.1 The local symbols in the `s`-variable

**Lemma 9bis.1 (the local symbols are `A(s) + A(1−s)`).**  Put `s = ½ + iτ`
and, for a prime `p` and the real place,

    f_p(s) := \frac{(\log p)p^{−s}}{1−p^{−s}} = Σ_{k≥1}(\log p)p^{−ks}
              \quad (Re s > 0),
    a(s)   := \tfrac12\log π − \tfrac12ψ(s/2).                        (9bis.1)

Then, as meromorphic functions of `s`, on the principal component `𝔠_0` of
`Ĉ_S`:

  (i) `\hat W_p(𝔠_0,τ) = f_p(s) + f_p(1−s)`;
  (ii) `\hat W_∞(0,τ) = a(s) + a(1−s)`;
  (iii) `Res_{s=0}f_p = Res_{s=0}a = 1`, and `Res_{s=1}f_p(1−s) =
       Res_{s=1}a(1−s) = −1`; `f_p` has no pole at `s=1` and `a` none at
       `s=0` other than the one named, in `Re s > −2`.  Under `τ = (s−½)/i`
       these are the residues `−i` at `τ = i/2` and `+i` at `τ = −i/2` of
       Paper 43 Theorem 9.7b(a),(b).
  (iv) Consequently, at the chart `S`,
       `T̂_S(𝔠_0,·) = A_S(s) + A_S(1−s)` with
       `A_S(s) := a(s) + Σ_{p∈S_f}f_p(s)`, and
       `Res_{s=0}T̂_S = |S_f| + 1`, i.e. `Res_{τ=i/2}T̂_S = −i(|S_f|+1)`,
       which is Paper 43 Theorem 9.7b(c).

*Proof.*  (i)  Paper 43 (9.11) on `𝔠_0` reads
`\hat W_p = (\log p)\,2\,Re\big(ζ_p/(1−ζ_p)\big)` with
`ζ_p = p^{−1/2}\overline{η_p}`, and on `𝔠_0` the phase `θ_p = 0`, so
`\overline{η_p} = p^{iτ}` and `ζ_p = p^{−1/2+iτ} = p^{−(1−s)}`.  Hence
`(\log p)ζ_p/(1−ζ_p) = f_p(1−s)`, and for real `τ`,
`\overline{f_p(1−s)} = f_p(\overline{1−s}) = f_p(s)`, so
`2Re(\cdot) = f_p(s)+f_p(1−s)`.  Both sides are meromorphic, agreeing on a
line, hence everywhere.
(ii) is Theorem 7.5(i).
(iii) `1−p^{−s} = s\log p + O(s²)` gives `f_p(s) = 1/s + O(1)`; the poles of
`f_p` are at `s ∈ (2πi/\log p)Z`, so `s = 1` is not one.  For `a`, Theorem
7.5(ii).  The residue transport is the computation in Theorem 7.5(ii).
(iv) Sum (i) over `p ∈ S_f` and add (ii); the residue at `s=0` receives `1`
from `a` and `1` from each `f_p`, and `f_p(1−s)`, `a(1−s)` are regular there
(they equal `f_p(1), a(1)`, finite).  ∎  `PROVED`

### 9bis.2 The Tate residues of the continued Euler-product symbol

**[REBUILT, phase 132, round 2, finding `M3` of `R132.002`.  Round 1 headlined
the identity `A(s)+A(1−s) ≡ 0` under the name "the meromorphic symbol of the
colimit trace".  Three things were wrong with that, and the auditor is right
about all three.  (1) *The name.*  `A` is **not** the symbol of `T_∞`: `T_∞` is
defined by a finite sum at each test (Paper 43 Theorem 8A.7c(b)) and its
Fourier side is not a function at all (Theorem 9.6′); `A` is the analytic
continuation from `Re s > 1` of a *formal* prime sum, and `A_S(½+iτ)` does not
converge on the critical line, where the chart symbols live.  The name is
withdrawn and occurs nowhere in this paper.  (2) *The content.*
`A(s)+A(1−s) ≡ 0` is a one-line restatement of the functional equation; it is
now a **remark**, not the theorem.  (3) *What was missed.*  The informative
statement is **one-sided**, it is a positive residue computation rather than a
vanishing, and the round-1 script printed it (check (3d),
`Res_{s=0}A = 1.000`) without the paper stating it.  Clause C.4's polar half
now rests on Theorem 9bis.2′ below, and not on a definition plus a negative —
which was D128 `C3`'s failure mode in a new place.]**

**Definition 9bis.1a (the continued Euler-product symbol).**  Put

    A(s) := a(s) + Σ_{p}f_p(s)
          = \tfrac12\log π − \tfrac12ψ(s/2) − \frac{ζ'}{ζ}(s),        (9bis.2)

the sum over **all** primes, absolutely convergent for `Re s > 1` by (E1) and
**continued meromorphically** to `C` by the right-hand display; and, at a
finite chart `S`, `A_S(s) := a(s) + Σ_{p∈S_f}f_p(s)`, so that
`T̂_S(𝔠_0,·) = A_S(s) + A_S(1−s)` by Lemma 9bis.1(iv).

> **`A` is the continued Euler-product symbol.  It is *not* the symbol of
> `T_∞`, and this paper nowhere says it is.**  `T_∞` is a finite sum at each
> test and has no Fourier-side function (Theorem 9.6′).  Convention (C1) of
> §1.2 governs statements about `T_∞`; it does **not** govern `A`, which is not
> a limit of the chart symbols where those live — Corollary 9bis.3 is precisely
> the failure of that exchange.  Every statement of §9bis about `A` is a
> statement about this continued function and about nothing else.

**Theorem 9bis.2′ (the Tate residues: `|S_f|+1` at every chart, exactly `1`
in the continuation, at each of `s = 0` and `s = 1`).**

  (i) *(the identity)*  `A(s) = −\dfrac{ξ'}{ξ}(s) + \dfrac1s + \dfrac1{s−1}`.
  (ii) *(the two poles, and their residues)*  `ξ` is entire and **nonzero** at
      `s = 0` and `s = 1` (E2), so `−ξ'/ξ` is regular there, and `A` has
      **exactly two** poles in `\{0,1\}`, both simple, with

        Res_{s=0} A = 1 ,        Res_{s=1} A = 1 ,                     (9bis.3)

      **chart-independently**.  They are the poles of the **trivial factor**
      `½s(s−1)` of `ξ` and of nothing else.
  (iii) *(the chart, for comparison)*  At every finite chart,

        Res_{s=0} A_S = |S_f| + 1 ,      Res_{s=1} A_S = 0 ,           (9bis.4)

      the first by Lemma 9bis.1(iii),(iv) — one residue `1` per place of `S` —
      and the second because `a(1)` and `f_p(1) = (\log p)/(p−1)` are
      **finite**: a finite chart has no pole at `s = 1` at all.
  (iv) *(this is the polar packet)*  In Theorem 9.4(a) the two summands
      `A_0(s) = 1/s + 1/(s−1)` of `ξ'/ξ` contribute, against `g`, exactly the
      rectangle residues `g(0)` and `g(1)`; by (i) these are the **same two
      poles** as in (ii), with the same residues `1` each.  Hence, with
      Theorem 8.1(i) and Remark 8.2,

        polar packet = g(0) + g(1) = 2Φ_F(0)Φ_F(1) = β_T(M(Γ_F),M(Γ_F)) ,

      i.e. **the polar packet is the pair of Tate poles of `A`, with
      coefficient exactly `1` each** — one at `s = 0`, one at `s = 1`,
      corresponding under Theorem 8.1 to the two rulings `e_+` and `e_−`
      respectively (Remark 8.2 fixes which is which).

*Proof.*  (i)  Logarithmically differentiating
`ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)` (E2) gives (9.8),
`ξ'/ξ = 1/s + 1/(s−1) − ½\log π + ½ψ(s/2) + ζ'/ζ`, hence
`½\log π − ½ψ(s/2) − ζ'/ζ(s) = −ξ'/ξ(s) + 1/s + 1/(s−1)`, which is (i) by
(9bis.2).
(ii)  `ξ` is entire (E2) and `ξ(0) = ξ(1) = ½ ≠ 0` (the zero of `s−1` cancels
the pole of `ζ` at `s = 1` and the zero of `s` cancels the pole of `Γ(s/2)` at
`s = 0`; the functional equation then gives `ξ(0) = ξ(1)`).  So `ξ'/ξ` is
regular at `0` and `1`, and by (i) the only poles of `A` there are `1/s` and
`1/(s−1)`, simple, residue `1` each.  The same two residues read off (9bis.2)
directly, which is the useful cross-check: at `s = 0`, `ζ'/ζ` is regular
(`ζ(0) = −½ ≠ 0`) and `−½ψ(s/2) = 1/s + O(1)` by (E4), so the residue is the
**archimedean** one; at `s = 1`, `ψ(½) = −γ−2\log2` is finite and
`−ζ'/ζ(s) = 1/(s−1) + O(1)` by the simple pole of `ζ` (E2), so the residue is
the **finite-place** one, created by the whole Euler product at once.
(iii)  The first is Lemma 9bis.1(iii),(iv).  For the second, `a` is regular at
`s = 1` and each `f_p(s) = (\log p)p^{−s}/(1−p^{−s})` has poles only at
`s ∈ (2πi/\log p)Z`, so `f_p(1) = (\log p)/(p−1) < ∞` and the finite sum is
finite.
(iv)  Theorem 9.4(a) computed `\frac1{πi}∫_{L_c}gA_0\,ds = g(0)+g(1)` by the
rectangle, `A_0` being exactly the two-pole part isolated in (i)–(ii), and
`g(0) = g(1) = Φ_F(0)Φ_F(1)` by Lemma 9.1.  Theorem 8.1(i) identifies the sum
with `β_T(M(Γ_F),M(Γ_F))`.  ∎  `PROVED`, using (E1), (E2), (E4).

**Remark 9bis.2a (the two collapses, stated side by side).**  **[REBUILT,
phase 132, round 2.]**  (9bis.3) against (9bis.4) is the whole of "the poles
in the same comparison", and it is **asymmetric**:

| point | at every finite chart `S` | in the continuation `A` | what the passage is |
|---|---|---|---|
| `s = 0` | `Res = \|S_f\|+1`, **divergent** as `S ↑` | `Res = 1` | the `\|S_f\|` finite residues **disappear**; the surviving `1` is the archimedean one, and it is the `1/s` of `ξ`'s trivial factor.  Corollary 9bis.3: summation and continuation do not commute here |
| `s = 1` | `Res = 0` for **every** `S` | `Res = 1` | the pole is **created in the limit**, by the pole of `ζ` at `s = 1`.  Theorem 9bis.4(iii): the rate is Mertens, `A_S(1) = Σ_{p≤x}\frac{\log p}{p−1} + a(1) \sim \log x` |

So at `s = 0` the chart overcounts and the excess evaporates; at `s = 1` the
chart undercounts and the pole appears only at the end.  In both cases the
continuation has residue exactly `1`, and the pair of them **is** the polar
packet (Theorem 9bis.2′(iv)).  *This is the statement clause C.4 asks for, and
it is a computation of two residues, not a renaming.*

**Remark 9bis.2b (the reflected sum vanishes — the functional equation, in one
line).**  **[REBUILT, phase 132, round 2: this was Theorem 9bis.2(ii) of
round 1 and is demoted, per `M3`.  It is true, it is pretty, and it carries no
information beyond `ξ(s) = ξ(1−s)`.]**  Write `Ξ(s) := A(s) + A(1−s)`.  Then
`Ξ ≡ 0` on `C`: by (i) and `(ξ'/ξ)(1−s) = −(ξ'/ξ)(s)` (E2),

    A(1−s) = +\frac{ξ'}{ξ}(s) + \frac1{1−s} + \frac1{−s}
           = \frac{ξ'}{ξ}(s) − \frac1{s−1} − \frac1s = −A(s).

In particular the residue `+1` of `A` at `s = 0` is cancelled inside `Ξ` by the
residue `−1` of `A(1−s)` there, the latter coming from the pole of `ζ` at
`s = 1`.  **`Ξ` is not the symbol of `T_∞`** (Definition 9bis.1a's box), and
**no clause of this paper rests on `Ξ ≡ 0`**: clause C.4's polar half is
Theorem 9bis.2′(ii),(iv).  `PROVED`

**Corollary 9bis.3 (the chart residue `|S_f|+1` is an artefact of the partial
Euler product).**  The map `S ↦ Res_{s=0}A_S = |S_f|+1` diverges as `S ↑`,
while `Res_{s=0}A = 1` (Theorem 9bis.2′).  There is no contradiction: the two
numbers are computed by operations that **do not commute**.  Precisely,
`Σ_{p∈S_f}f_p(s) → −ζ'/ζ(s)` **only on `Re s > 1`**; at `s = 0` each `f_p` has
a pole of residue `1` while `−ζ'/ζ` — the analytic continuation of the sum — is
**regular** there (`ζ(0) = −½ ≠ 0`), so the tail `Σ_{p∉S_f}f_p` supplies
exactly one `1/s` per omitted prime near `s = 0` and the sequence of residues
is unbounded, while the continuation contributes none.  Summation over primes
and analytic continuation **do not commute at `s = 0`**, and that — not a
cancellation — is the whole content of the chart dependence recorded in Paper 43 §14.0a ("WHY the chart dependence is
real and not formal") and in Paper 44 Remark 8bis.8b.

*Proof.*  Lemma 9bis.1(iv) and Theorem 9bis.2′(ii),(iii); the divergence of
the tail residues is the count of omitted primes.  ∎  `PROVED`

**Theorem 9bis.4 (where the polar packet actually comes from, and what Mertens
is for).**  With the notation above:

  (i) *(the polar packet, restated from Theorem 9bis.2′.)*  The polar packet
      is the pair of Tate poles of `A` at `s = 0` and `s = 1`, each of residue
      exactly `1` (9bis.3), evaluated against `g`: `g(0) + g(1) =
      2Φ_F(0)Φ_F(1) = β_T(M(Γ_F),M(Γ_F))`.  It is **chart-independent**.  The
      chart residues (9bis.4) are `|S_f|+1` at `s = 0` and `0` at `s = 1`;
      Remark 9bis.2a tabulates the two collapses that carry them to `1` and
      `1`.  **[REBUILT, phase 132, round 2, `M3`: round 1 said here that the
      two numbers "are not to be reconciled".  That was the weak form.  They
      *are* reconciled, one-sidedly and in both directions, by Theorem 9bis.2′
      and Remark 9bis.2a.]**
  (ii) *(the hyperbolic structure constant is Mertens; `CLASSICAL`,
      quarantined.)*  Paper 43 Theorem 10.8b, labelled `CLASSICAL` there and
      counting toward no clause of row A, proves that in the **colimit** chart
      the scalar form reproduces the hyperbolic pairing on the rulings:
      `\lim_{n,m}I_∞(F_n,G_m) = 1 = β_T(e_+,e_−)` and
      `\lim_n I_∞(F_n,F_n) = 0 = β_T(e_+,e_+)`, the value `1` being Mertens'
      `Σ_{N≤x}Λ(N)/N = \log x + O(1)`.  Row C **uses** this statement, with
      its label, for exactly one purpose: to say that the hyperbolic form
      `β_T` appearing in (9.9) is not an external decoration but the
      restriction of the colimit form `I_∞` to the ruling plane.  It is
      **not** used to identify the polar packet, which is (i) and needs no
      Mertens.
  (iii) *(what Mertens is measuring.)*  The value `1` of (ii) is the
      statement that the partial Euler products mimic the **pole of
      `−ζ'/ζ` at `s = 1`**: `A_S(1) = a(1) + Σ_{p∈S_f}\frac{\log p}{p−1}
      \sim \log x` for `S_f = \{p ≤ x\}` by Mertens, while `−ζ'/ζ(σ) \sim
      1/(σ−1)` as `σ ↓ 1`.  So Mertens governs the behaviour of the chart
      symbols at `s = 1`, i.e. at `τ = −i/2`; it has nothing to do with the
      residue count at `s = 0` of Corollary 9bis.3, which is a statement about
      non-commuting limits.
  (iv) *(the chart/colimit discontinuity is genuine, and this is where it
      sits.)*  At a **fixed chart**, Paper 43 Theorem 9.14c′ proves
      `I_A(F_α,G_β) → 0` along every admissible pair of ruling
      approximations — value `0`.  In the **colimit**, Theorem 10.8b gives
      value `1`.  There is no contradiction: 9.14c′'s proof uses the uniform
      seminorm `N` of Lemma 9.14a0, which is finite only because
      `|T̂_S| ≤ A_S + B_S\log(2+|τ|)` at a fixed chart, and the colimit symbol
      is unbounded (Paper 44 Remark 8bis.4b(1)).  Row C records this
      discontinuity as a fact of the theory and claims nothing beyond it.

*Proof.*  (i) is Theorem 9.4(a) together with Theorem 9bis.2′(i),(ii),(iv) and
Theorem 8.1(i); no new argument.  (ii) is the citation, with its label.
(iii): Mertens' theorem in the form used by Paper 43 Theorem 10.8b Step 2,
`A(x) = Σ_{N≤x}Λ(N)/N = \log x + O(1)`, gives
`Σ_{p ≤ x}\frac{\log p}{p−1} = Σ_{p≤x}Σ_{k≥1}\frac{\log p}{p^k} =
Σ_{N≤x}\frac{Λ(N)}{N} + O(1) = \log x + O(1)`, while
`f_p(1) = \frac{\log p}{p−1}`; and `−ζ'/ζ(σ) = 1/(σ−1) + O(1)` as `σ↓1` is the
simple pole of `ζ` (E2).  (iv) is the two cited theorems and the cited reason
for the failure of the transfer.  ∎  `PROVED` in (i),(iii),(iv); `CLASSICAL`
(Mertens) in (ii), quarantined exactly as in Paper 43 Theorem 10.8b.

**Remark 9bis.5 (the blueprint's route to §2.2, refuted).**  **[REBUILT,
phase 132, round 1.]**  The lead blueprint §2.2 proposed: *"the finite-place
residues sum to a divergence that is exactly the archimedean growth, leaving
coefficient 1"*.  That mechanism does not exist, for two independent reasons.

1. *There is no archimedean divergence to cancel against.*  In Paper 43
   Theorem 10.8b, Step 3, the archimedean contribution to `I_∞(F_n,F_m)` is
   bounded by `(1−e^{−2a})^{−1}e^{−(n+m)a}` and tends to `0` **exponentially**.
   The value `1` comes entirely from the finite places, via the **main term**
   `\log x` of Mertens integrated against `−φ'`.  So the archimedean place is
   negligible there, not a compensating divergence.
2. *The residue count at `s = 0` needs no absorption.*  **[REBUILT, phase 132,
   round 2, per `M3`: restated one-sidedly.]**  By Theorem 9bis.2′(ii),(iii)
   the chart residue at `s = 0` is `|S_f|+1` and the continuation's is `1`; by
   Corollary 9bis.3 the difference is the failure of summation over primes and
   analytic continuation to commute there, the tail supplying one `1/s` per
   omitted prime while `−ζ'/ζ` is regular at `0`.  Nothing is "absorbed" by
   archimedean growth, and Mertens is not needed for this step at all.  Mertens
   governs the **other** Tate point, `s = 1`, where the chart residue is `0`
   for every `S` and the pole is created only in the limit (Remark 9bis.2a,
   Theorem 9bis.4(iii)).

What survives of the blueprint's intention is Theorem 9bis.4(ii): Mertens is
used, once, with its label, to identify the structure constant of `β_T` with a
value of the colimit form.  Its true subject is the pole at `s = 1`, not the
residue count at `s = 0` (Theorem 9bis.4(iii)).

---

## 10. Sufficiency for Weil's criterion (clause C.6, second half)

### 10.1 The gap, stated exactly

The arrow "`q_T ≥ 0` on the primitive class `P_T` for every `T` ⟹ RH" is
asserted throughout the corpus as classical but proved nowhere in it:
`113_07` Proposition 4.1 records its (⇐) leg as resting on "a Paley–Wiener
style statement about `D` … **not proved here**"; `106_11` Theorem 1 proves
unconditionally that if RH fails there are nonzero real
`f_+ ∈ C_c^∞(R)^{even}`, `f_- ∈ C_c^∞(R)^{odd}` with the Weil form negative,
but **for unconstrained tests**, never upgraded to the two-moment primitive
class.  §10 closes the joint.  D128 confirmed this section line by line and
called Theorem 10.4 "the strongest and most defensible result in the paper";
it also found one wrong step, fixed in §10.3.

### 10.2 The primitivization operator

**Lemma 10.1.**  Let `Π := −∂_t² + ¼`.  For `G ∈ C_c^∞(R)`,
`Φ_{ΠG}(s) = s(1−s)Φ_G(s)`, and on `s = ½+iτ` the factor is `τ² + ¼ > 0`.
*Proof.*  Two integrations by parts, boundary terms vanishing by compact
support, give `∫G''(t)e^{(s−½)t}dt = (s−½)²Φ_G(s)`; hence
`Φ_{ΠG} = (¼−(s−½)²)Φ_G = s(1−s)Φ_G`.  At `s = ½+iτ`, `s(1−s) = ¼+τ²`.  ∎
`PROVED`

**Corollary 10.2.**  `Π` maps `C_c^∞(I_T)` into the primitive class `P_T`,
preserves support, reality and parity, and is injective; for every nontrivial
zero `ρ` the factor `ρ(1−ρ)` is nonzero, so prescribing `Φ_{ΠG}(ρ)` is
equivalent to prescribing `Φ_G(ρ)`.
*Proof.*  `Φ_{ΠG}(0) = 0`, `Φ_{ΠG}(1) = 0` by Lemma 10.1, which is primitivity
(Theorem 8.1(ii)).  `Π` is a real, even-order, constant-coefficient local
operator, so it does not enlarge support and commutes with `t ↦ −t`.
Injectivity: `Φ_{ΠG} ≡ 0` forces `Φ_G ≡ 0` off `{0,1}`, hence everywhere by
analyticity (`Φ_G` entire), hence `G = 0` — **this is analyticity, not
continuity** (D128 `C10`).  Finally `ρ ∉ {0,1}` for a nontrivial zero.  ∎
`PROVED`

**Remark 10.3 (`Π` is the same operator row B uses).**  Paper 44
Theorem 8bis.4a Step 2 constructs its primitive test as `g_T = Π g_{0,T}` and
verifies `λ_∓(Γ_{g_T}) = 0` by exactly this computation, citing this theorem;
and Paper 44 (8bis.9) is the pair of conditions `Φ_g(0) = Φ_g(1) = 0` that `Π`
enforces.  The two papers use one operator, and this is the statement of that
fact.  `PROVED` (by inspection of the cited proof).

**Lemma 10.3a.**  For `F = ΠG`,
`Σ_ρΦ_F(ρ)Φ_F(1−ρ) = Σ_ρ[ρ(1−ρ)]²Φ_G(ρ)Φ_G(1−ρ)`.
*Proof.*  `Φ_F(ρ)Φ_F(1−ρ) = ρ(1−ρ)Φ_G(ρ)·(1−ρ)ρΦ_G(1−ρ)`.  ∎  `PROVED`

### 10.3 The upgrade, with the D128 `C10` fix carried out

**Theorem 10.4 (sufficiency).**  If RH is false, there exist nonzero
compactly supported **primitive** real tests `F_+` (even) and `F_-` (odd) with
`Σ_ρΦ_{F_±}(ρ)Φ_{F_±}(1−ρ) < 0`.  Consequently `q_T ≥ 0` on `P_T` for every
`T` implies RH.

*Proof.*  Suppose RH fails; fix an off-line zero `ρ_0 = β_0+iγ_0`, `β_0 ≠ ½`,
with quartet `ρ_0, 1−ρ_0, \barρ_0, 1−\barρ_0`, all zeros.  Run the
construction of `106_11` Theorem 1 with one change: impose the target values
on `Φ_F` rather than on `\hat f`, where `F = ΠG`.  By Corollary 10.2,
`Φ_F(ρ) = ρ(1−ρ)Φ_G(ρ)` with `ρ(1−ρ) ≠ 0` at every nontrivial zero, so the
prescribed values at the finitely many target zeros are attainable **iff** they
are attainable for `Φ_G`, which is `106_11`'s own statement.

**The `C10` fix.**  The previous version said the prescribed values "are
attained by rescaling the coefficients `a_N,b_N` … by the fixed nonzero
factors `ρ(1−ρ)`".  **That is wrong, because `a_N,b_N` must stay real** while
`ρ(1−ρ)` is not.  The correct argument is `106_11` (20)–(21) itself, and it
is this.  `106_11` realizes the target value at the quartet by the family

    z ↦ Z_R(z)\,(a + b z²)\,Φ(z)^N ,     a,b ∈ R,

with `Z_R` a fixed real even polynomial annihilating the finite non-target
divisor and `Φ = \hatφ` a fixed even damping with `Φ(s_0) ≠ 0`.  Prescribing
the value at the single quartet representative `z = s_0` is the **real-linear**
map

    R² → C,    (a,b) \mapsto Z_R(s_0)Φ(s_0)^N\,(a + b\,s_0²),          (10.1)

which is an `R`-linear isomorphism **iff** `1` and `s_0²` are `R`-linearly
independent in `C`, i.e. iff `s_0² ∉ R`, i.e. iff `s_0` is neither real nor
purely imaginary.  **[REBUILT, phase 132, round 2, finding `LF1` of `R132.003`,
with note `n2` of `R132.002`, which traced `106_11` independently and closed
the builder's round-1 flag `P3`.]**  In `106_11` the variable is
`z = (ρ−½)/i`, so the critical line is `Im z = 0` and a real zero would be
`Re z = 0`; its (9) fixes `s_0 = x_0 + iy_0` with `x_0y_0 ≠ 0`, glossing
`y_0 ≠ 0` as the failure of the critical-line condition and **`x_0 ≠ 0` as the
classical absence of real nontrivial zeros** — which is the last clause of
import **(E2)**, `ζ(σ) ≠ 0` for `σ ∈ (0,1)`, and this is the **only** place in
this paper where that import is used.  Its own (20) then states
`Im(s_0²) = 2x_0y_0 ≠ 0`, i.e. `s_0² ∉ R`, and (21) concludes the isomorphism.
So no degenerate case needs excluding by hand.  Finally
`Z_R(s_0)Φ(s_0)^N ≠ 0` by construction.  So (10.1) is
surjective and the real coefficients realize **any** complex target, including
the one rescaled by `ρ(1−ρ)`.  The odd-parity family
`z ↦ i z Z_R(z)(c+dz²)Φ(z)^N` is handled identically.  **This is the whole of
the fix, and no other step of `106_11` changes.**

The three quantitative ingredients survive verbatim, with one change of
constants:

  (i) *Paley–Wiener* (import (E6)).  `\hat F = (τ²+¼)\hat G` is entire of the
      same exponential type, since multiplication by a polynomial does not
      change the type; so `F` is compactly supported in the same interval.
  (ii) *Parity.*  `τ²+¼` is even, so `Π` preserves the even/odd split and both
      `F_+` and `F_-` are produced.
  (iii) *Tail domination.*  **[REBUILT, phase 132, round 2, minor `m2` of
      `R132.002`: round 1 said the extra decay is bought by "enlarging `N` by a
      fixed amount".  That misdescribes `106_11`'s mechanism and is corrected
      here.]**  By Lemma 10.3a the tail acquires the factor
      `|ρ(1−ρ)|² = O((1+|Im ρ|)^4)`.  `106_11`'s tail bound (27)–(30) is
      organised around a **fixed degree `D`**, chosen larger than the degrees
      of the polynomial factors in play, together with the global geometric
      factor `4^{−(N−N_0)}`; the extra `|ρ(1−ρ)|²` is absorbed by taking
      `D ↦ D+2`, after which (29) still converges by the strip decay (15) and
      the estimate (28).  **It is the degree `D`, not the exponent `N`, that
      absorbs the new factor**; `N` continues to do only what it does in
      `106_11`, namely supply `4^{−(N−N_0)}`.  With `N(T) = O(T\log T)` (E3d)
      the tail is then dominated by the target quartet's contribution for `N`
      large, exactly as there.

Hence the target quartet dominates, its contribution is negative, both tests
are primitive (Corollary 10.2) and nonzero (injectivity).  Contrapositively,
`q_T ≥ 0` on `P_T` for every `T` — equivalently for `T` large enough to
contain the fixed supports — forces RH.  ∎  `PROVED`, using imports (E2)'s
last clause, (E3d), (E6) and the repository construction `106_11` Theorem 1.

**Remark 10.5 (why the upgrade is available only now).**  It is (9.10) —
Theorem 9.6 on the primitive sector — that makes `q` and `Σ_ρ` the same object
there.  Before it, `106_11` could be run only for the unconstrained Weil form.
The two halves of the missing arrow belong to row C and to `106_11`
respectively, and neither alone suffices.

**Remark 10.6 (what this does and does not say about row D).**  Theorem 10.4
is a **sufficiency** statement: the primitive radial class is rich enough for
Weil's criterion.  It is not a positivity statement and it does not make one
available.  Read together with Warning 8.5 — Paper 43 Theorem 14.1 (no
Hodge-index shape on `N_A`) and Paper 44 Theorem 8bis.4a (positivity fails on
the pure Frobenius form at every chart) — what it says is: row D's target is
`I_∂ ≤ 0` on primitive radial classes of `D_A^∞`, in the **colimit**
(convention (C1)), and nothing else.  `§14.4`.

---

## 11. External inputs, each with the clause it serves

**[REBUILT, phase 132, round 1.  This section **replaces** the previous §11
entirely; see §13, item W45.7.  The previous §11 discharged an obligation
(`w_unit(Γ_n) = n−1`) that Paper 44 §9bis W1–W3 has proved never existed.]**

Clause C.8 in its strong form requires every analytic input to be either
proved here or named.  This is the complete list.  Nothing else is used.

| id | import | label | used in | clause served |
|---|---|---|---|---|
| **E1** | Euler product: `ζ'/ζ(s) = −Σ_{n≥2}Λ(n)n^{−s}`, `Re s > 1` | `CLASSICAL` | Thm 9.4(c), Def 9bis.1a, Thm 9bis.2′ | C.4, C.8 |
| **E2** | `ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)` entire, `ξ(s)=ξ(1−s)`, zeros of `ξ` = nontrivial zeros of `ζ` with multiplicity; `ζ` has a simple pole at `s=1`, `ζ(0) = −½`, `ξ(0) = ξ(1) = ½ ≠ 0`; **and no nontrivial zero is real** (`ζ(σ) ≠ 0` on `(0,1)`) | `CLASSICAL` | Lem 9.2, Thm 9.4, Thm 9bis.2′; the last clause **only** at (10.1) | C.4, C.6, C.7, C.8 |
| **E3a** | `ξ` of order 1; Hadamard product and `ξ'/ξ(s) = Σ_ρ(\frac1{s−ρ}+\frac1ρ) + B` | `CLASSICAL` (Davenport ch. 15–17; Titchmarsh §3.1) | (E3c) | C.5, C.8 |
| **E3b** | *local* Riemann–von Mangoldt `N(T+1) − N(T) = O(\log T)`; hence ordinate-avoiding heights `X_j ∈ [j,j+1]` at distance `≥ c/\log j` | `CLASSICAL` (Davenport ch. 15) | Lem 9.2 | C.5, C.8 |
| **E3c** | `ξ'/ξ(σ ± iX_j) = O(\log^2X_j)` uniformly in a fixed strip, from (E3a)+(E3b) | `CLASSICAL` (Davenport ch. 17; Titchmarsh §9.6) | Lem 9.2 | C.5, C.8 |
| **E3d** | *global* Riemann–von Mangoldt `N(T) = O(T\log T)` | `CLASSICAL` | Thm 10.4(iii), Rem 9.8 | C.5, C.6 |
| **E4** | Stirling/digamma: `ψ(z) = O(\log\|z\|)`, `ψ(z) = −1/z+O(1)` at `0`, `ψ(½) = −γ−2\log2`, `ψ(¼) = −γ−3\log2−π/2` | `CLASSICAL` | Thm 7.4, 7.5, 9.4(b), 9bis.1 | C.4 |
| **E5** | Fourier inversion and Plancherel on `R` | `CLASSICAL` | Thm 9.4(c), Lem 1.3, Thm 12.2 | C.3, C.4, A.6 |
| **E6** | Paley–Wiener (compact support ⟺ exponential type) | `CLASSICAL` | Thm 10.4(i) | C.6 |
| **E7** | Lerch: `ζ_H'(0,a) = \log Γ(a) − ½\log 2π`; `ζ_H(0,a) = ½−a` | `CLASSICAL` | Thm 7.3 | C.4 |
| **E8** | Mertens: `Σ_{N≤x}Λ(N)/N = \log x + O(1)` | `CLASSICAL`, **quarantined** | Thm 9bis.4(ii),(iii) **only**, via Paper 43 Thm 10.8b | C.4 (structure constant of `β_T` only) |
| **R1** | `106_11` Theorem 1 (negative Weil tests in both parities, unconditional) | `PROVED-IN-REPOSITORY` | Thm 10.4 | C.6 |

**Not used anywhere:** Meyer's trace theorem or any imported spectral
realization (this is what clause C.8 buys, and it is the one sense in which
D128's restatement of C.8 is *weaker* than what is now delivered); the
imported semilocal cutoff theorem `C` of Paper 43 §12 (Paper 43 Remark 8.10a
confines it to Theorem 8.10, on which nothing here depends); any statement
about the location of a zero.

**[REBUILT, phase 132, round 2, finding `M2` of `R132.002` = `LF2` of
`R132.003`: (E3) was one row and is now four.  Round 1 presented (E3b) and
(E3c) as *consequences* of (E3d); they are strictly stronger classical inputs,
and clause C.8 in its strong form exists precisely to stop that.  The
mathematics of Lemma 9.2 is unchanged.]**

**Quarantine of E8.**  **[REBUILT, phase 132, round 3, finding `r5` of
`R132.005`: round 2 added a **second** use of Mertens — the rate at `s = 1` in
Theorem 9bis.4(iii) — and left the quarantine paragraph saying "once".  Both
uses are now recorded, and the deletion test covers both.]**  Mertens is used
**twice**, and nowhere else:

* in **Theorem 9bis.4(ii)**, through Paper 43 Theorem 10.8b, which carries the
  label `CLASSICAL` there and counts toward no clause of row A — to say that
  the hyperbolic `β_T` is the restriction of the colimit form `I_∞` to the
  ruling plane;
* in **Theorem 9bis.4(iii)**, as the *rate* `Σ_{p≤x}(\log p)/(p−1) = \log x +
  O(1)` at which the chart symbols manufacture the `s = 1` pole they do not
  have (Theorem 9bis.2′(iii)).

*Deletion test, for both.*  Deleting Theorem 9bis.4(ii) and (iii) deletes no
other statement of this paper.  The explicit formula (Theorem 9.4,
Corollary 9.4a), the comparison theorem (9.9)–(9.10) and Corollary 9.6a, the
polar-packet identification (Theorem 8.1, **Theorem 9bis.2′(ii),(iv)**),
Corollary 9bis.3 and Theorem 12.2 are all independent of both.  **In
particular clause C.4's discharge uses no Mertens at all**: its polar half is
Theorem 9bis.2′, a residue computation.  What would be lost is exactly two
sentences: "the hyperbolic form `β_T` is the restriction of `I_∞` to the ruling
plane" (which would revert to "the hyperbolic form `β_T` of Paper 43
Theorem 9.1"), and the *rate* in Remark 9bis.2a's `s = 1` row (the row's
qualitative content — chart residue `0`, continuation residue `1` — is
Theorem 9bis.2′ and survives).

---

## 12. Clause A.6 for the intersection form on the radial sector

**[REBUILT, phase 132, round 1.  This replaces §12.1's `G_rad`, Theorem 12.3,
Theorem 12.4, Theorem 12.5 and Corollary 12.6 of the previous version.  The
sector is now `D_A^{rad}`, an honest subalgebra of the declared test algebra,
and the theorem is a Fourier computation, not a topological argument.]**

**Definition 12.1.**  `𝓝_∩ := \{Γ_h ∈ D_A^{rad} : I_A(Γ_h,Γ_g) = 0` for all
`Γ_g ∈ D_A^{rad}\}`, the scalar radical **within the radial sector**.

**Theorem 12.2 (`𝓝_∩ = 0` at every finite chart).**  Fix a finite chart `S`
with `S_f ≠ ∅` and `c := 0`.  **[REBUILT, phase 132, round 2, finding `M4`:
`h ∗ g^∨` has `0` in its support whenever `h` and `g` overlap, so this theorem
too must avoid Theorem 5.1 and use Lemma 5.1a / Paper 43 Theorem 9.7(d), both
of which hold on **all** of `D_A`.  No support hypothesis is imposed on `h` or
`g`.]**  Then for **arbitrary** `h,g ∈ C_c^∞(R)`,

    I_A(Γ_h,Γ_g) = \frac1{2π}∫_R \hat h(−τ)\overline{\hat g(−τ)}\,
                    \hat T_S(𝔠_0,τ)\,dτ
                 = \frac1{2π}∫_R \hat h(τ)\overline{\hat g(τ)}\,
                    \hat T_S(𝔠_0,τ)\,dτ ,                             (12.1)

and `𝓝_∩ = \{0\}`.  Consequently `N_A^{rad} := D_A^{rad}/𝓝_∩ = D_A^{rad}`, on
which `I_A` is nondegenerate, `⋆` and `†` are its own operations, and
`M = (λ_−,λ_+)` is defined and surjective onto `B_T`.

*Proof.*  *(12.1).*  By Lemma 1.1, `\widehat{Γ_h}` is carried by `𝔠_0` and
equals `\hat h(−τ)` there; by Proposition 3.2, `Γ_h ⋆ Γ_g^† = Γ_{h∗g^∨}`; by
Paper 43 Theorem 9.7(d), `T(H) = ∫_{Ĉ_S}\hat H(χ)(\hat T(χ)+c)dχ` absolutely —
which holds **for every `H ∈ D_A`**, with no support hypothesis, and is the
same citation Lemma 5.1a rests on — with `dχ|_{𝔠_0} = dτ/2π` and `c = 0`; and
`\widehat{Γ_h⋆Γ_g^†} = \widehat{Γ_h}\overline{\widehat{Γ_g}}` (Paper 43
Theorem 9.8's computation).  The second equality of (12.1) is the substitution
`τ ↦ −τ` together with the **evenness** of `\hat T_S` on `𝔠_0`, which holds
because on that component `θ_p = 0`, so `\hat W_p(𝔠_0,τ) = f_p(s)+f_p(1−s)` is
invariant under `τ ↦ −τ` (Lemma 9bis.1(i), conjugation), and `\hat W_∞(0,τ) =
\log π − Re ψ(¼+iτ/2)` is even.

*(`c`-dependence).*  The conclusion `𝓝_∩ = 0` holds for **every** `c`, since
Paper 43 Theorem 9.7(c) states that `T̂ + c` vanishes identically on no
component and has discrete zero set on each, **for every `c ∈ R`**; so unlike
(9.9) this theorem is not tied to `c = 0` (contrast Corollary 9.6a).  The
display (12.1) is written with `c := 0` because that is the declared value.

*(the radical).*  Let `Γ_h ∈ 𝓝_∩`.  By (12.1),
`∫_R \hat h(τ)\overline{\hat g(τ)}\hat T_S(𝔠_0,τ)dτ = 0` for every
`g ∈ C_c^∞(R)`.  The function `m(τ) := \hat h(τ)\hat T_S(𝔠_0,τ)` is locally
integrable and of at most logarithmic growth times Schwartz decay (Paper 43
Theorem 9.7(a),(b)), hence tempered; `\{\hat g : g ∈ C_c^∞\}` is dense in the
Schwartz space (E5); so `m = 0` a.e.  By Paper 43 Theorem 9.7(c),
`\hat T_S(𝔠_0,·)` is **real-analytic** and **not identically zero**, with
discrete zero set.  **[REBUILT, phase 132, round 2, note `n3` of `R132.002`:
this needs only Theorem 9.7(c), which states outright that `T̂+c` "vanishes
identically on **no** component" and has discrete zero set on each.  Paper 43
(14.2) is a **lower bound for `m := \sup_{Ĉ_S}T̂` by the value at `𝔠_0, τ = 0`**,
so it is a stronger and differently-typed statement; it is quoted below only
as a concrete witness, and the proof does not rest on it.]**  Concretely,
`\hat T_S(𝔠_0,0) ≥ \log π − ψ(¼) ≈ 5.372 > 0` by Paper 43 (14.2), every
finite-place term at `τ=0` on `𝔠_0` being positive (`ζ_p = p^{−1/2}` real and
positive there).  Hence `\hat h = 0` off a discrete set, and `\hat h` is continuous,
so `\hat h ≡ 0` and `h = 0`, i.e. `Γ_h = 0`.  The remaining assertions are
Proposition 3.2 and Paper 43 Theorem 9.1.  ∎  `PROVED`

**Remark 12.3 (relation to Paper 43 Theorems 9.8 and 9.14c).**  Theorem 12.2
is **not** a corollary of `𝓝 = 0` (Paper 43 Theorem 9.8): that theorem pairs
against all of `D_A`, whereas 𝓝_∩ pairs only against radial tests, and a
smaller test space can only make a radical **larger**.  What makes the
restricted statement true is that `D_A^{rad}` is exactly the sector whose
Fourier transforms fill the Schwartz space on the single component `𝔠_0`,
where the symbol is already nonzero.  Conversely, Paper 43 Theorem 9.14c
computes the radical of the **scalar** component of `I_vec` on the completion
and finds it two-dimensional — the ruling plane `σ(B_T)`.  The three
statements are consistent and describe three different pairings: `𝓝 = 0` on
`D_A`, `𝓝_∩ = 0` on `D_A^{rad}`, `R_∂ = σ(B_T)` on `N_A^{dist}`.  The rulings
are **not** in `D_A^{rad}`: they are limits of spread Tate families whose
`L¹`-mass escapes to `|w|_S → ∞` (Paper 43 Definition 9.14c0), and they live
in the completion (Proposition 8.3).

**Remark 12.4 (no colimit claim).**  Theorem 12.2 is a **fixed-chart**
statement.  Nothing is claimed about `𝓝_∩^∞` on `D_A^∞`: Paper 43 §13.8
withdraws every colimit-radical claim and Paper 44 Remark 8bis.4b(1) explains
why the Plancherel step does not transfer (the colimit symbol is unbounded).
This paper asserts no colimit vanishing.

**Remark 12.4a (`[phase 135]`: the colimit statement Remark 12.4 declines is
now available, by a different mechanism).**  Paper 46 **Theorem 11.12** proves
`\mathrm{rad}(I_∞|_{D_A^{rad}}) = 0` — and more, that no nonzero compactly
supported radial class is `I_∞`-orthogonal to the primitive sector — for the
**colimit** form `I_∞`, by **zero counting**: a nonzero `N ∈ C_c^∞(R)` has
`Φ_N` entire of exponential type, hence `O(r)` zeros in `|s−½| ≤ r` (Jensen),
whereas `ξ` has at least `\tfrac{2}{5π}r\log r(1+o(1))` **distinct** zeros
there, so `Φ_N` cannot vanish at every zero of `ξ`.  **[CORRECTED, phase 135
round 2, finding M3 of `R135_002`: round 1 of that phase wrote "whereas `ξ` has
`\sim(r/π)\log r` there (Riemann–von Mangoldt)", and this remark reproduced it.
Riemann–von Mangoldt counts **with multiplicity**, whereas the hypothesis in
force (Paper 46 Theorem 11.10(c)) gives vanishing of `Φ_N` to order one at each
**distinct** zero; the comparison therefore needs a lower bound for the
distinct count.  Paper 46 now imports one — (X18), Conrey (1989): at least
`\tfrac25` of the zeros are simple, hence distinct — which gives the displayed
bound and closes the argument.  The conclusion is unchanged.]**  **This is not a second proof of Theorem
12.2**, which is a fixed-chart Plancherel statement about `I_A` and the chart
symbol `\hat T_S(𝔠_0,·)`; the two theorems concern different forms and use
disjoint inputs.  It is the colimit companion this remark says is not claimed
here, and it is claimed there and nowhere else.  Nothing in this paper changes.

**Remark 12.5 (the old §12's two theorems, disposed of).**  The previous
Theorem 12.3 argued that comparing `I_A` with Paper 43's `T` is "ill-posed"
because they live on different domains, and Theorem 12.5/Corollary 12.6 read
Paper 44's weight `n^{−1/2}(n−1)` as a "deepest-stratum index".  On the
declared carrier: (a) `T` and `I_A` have the **same** domain, `D_A`, and
`I_A(F,G) = T(F⋆G^†)` is Paper 43 Definition 9.2 — there is no comparison to
make and no ill-posedness; (b) there is no deepest stratum, and Paper 44
§9bis W1 proves that `n−1` is a product of local factors of a **lift**, which
the class does not see.  Both are withdrawn; §13, items W45.8–W45.9.

---

## 13. The withdrawal ledger

**[REBUILT, phase 132, round 1.  Written in the style of Paper 44 §9bis.
Nothing is deleted from the record: each item says what was claimed, why it
falls, and what replaces it.]**

**W45.1.  Theorem 5.4 ("no corner terms, because `\log p/\log q` is
irrational"), and §§5.3–5.6, Corollary 5.5, Corollary 5.7.**  *Withdrawn in
phase 128 (D128 `C1`, verified: the family `\{τ_J^{p_0}\}` is mutually
inconsistent, so step (d) argues from a contradiction); now withdrawn a second
time, **with its referent**.*  The declared carrier `C_S ≅ R^××∏Z_p^×` is a
group with no zero-count filtration and no corner strata (Paper 43 Lemma 3.3).
*Replaced by:* Theorem 5.1 and Corollary 5.2 — the prime packet is
Paper 44 Theorem 3bis.7, an evaluation of `T`, and the vanishing at composite
labels is the shell structure (radial family) and Paper 44 Theorem 3ter.12
(object level).

**W45.2.  Definition 3.1 and Proposition 3.2 (`K_h` in the compact-section
Fell completion), and Remark 3.3.**  *Withdrawn.*  The completion is not the
declared test algebra; D128 `C8` found the "compact section" citation wrong
(P123.032–033 stabilize **places**, not classes) and the Haar normalization on
`∏Z_ℓ^×` unstated.  *Replaced by:* Definition 3.1 and Proposition 3.2 of this
version — `Γ_h ∈ D_A^{rad} ⊂ D_A = C_c^∞(C_S)`, with the convolution identity
a theorem of Paper 44 (Lemma 3bis.6a) and the probability normalization on the
compact part fixed by Paper 43 Theorem 9.14a's proof.

**W45.3.  Theorem 5.2 (the semilocal assembly `B_P(f) = Σ_pC_pλ_G(f)C_p` as
"the relative character").**  *Withdrawn as an identification.*  D128 `C3`
accepted that additivity over places was inherited from a definition.
*Replaced by:* §5.1 — `T` is row A's **declared** trace (Paper 43 Def. 8.6,
Def. 8A.7d), and this paper claims nothing about a localization.

**W45.4.  Theorem 4.2 ("the two halves of the Weil weight live at different
places"), Lemma 4.1 and Remark 4.3.**  *Withdrawn as false on the declared
carrier.*  Both factors of `Λ(p^k)p^{−k/2}` are local data of the single
finite place `p` (Theorem 4.1): `p^{−k/2}` is the value of `τ_p` on the shell,
`\log p` is the shell's `d^*x`-volume.  The old statement depended on the
normalized representative `h_S(n)` of the withdrawn carrier, which D128 `C6`
had already identified as a gauge choice.  *Replaced by:* Theorem 4.1,
Remark 4.2.

**W45.5.  Lemma 6.1's Arakelov reading, and Remark 6.3.**  *Remark 6.3 was
withdrawn in phase 128 (`C7`); Lemma 6.1 is now demoted.*  `vol(Z_p^×)=\log p`
is Paper 44 Theorem 8bis.8 — the unique normalization with a universal Tate
residue, up to one global scale.  *Replaced by:* Theorem 6.1, Corollary 6.2,
with the negative half (no map relating (i) and (iii)) stated as strongly as
the positive half.

**W45.6.  Corollary 6.2's conditionality, and the phrase "two independent
proofs" of Corollary 5.7.**  *The conditionality is removed* — the prime
packet is unconditional (Theorem 5.1) — *and the "two independent proofs"
claim stays withdrawn*: only Paper 44's statements are established, and
Corollary 5.2 above distinguishes the radial statement (Thm 3bis.7) from the
object statement (Thm 3ter.12), which the blueprint conflates (see §15.2 of
the builder report).

**W45.7.  §11 in its entirety (Theorem 11.1, Remark 11.2: "row B's `n−1`
obligation is discharged").**  *Withdrawn: there was no obligation.*  Paper 44
§9bis **W1** proves it: the class `δ_S(1/n)` is in the image of no slice map
`j_q` for `|S_f| ≥ 2` (Proposition 3bis.2), the radial norm class annihilates
the unit packet identically (Theorem 3bis.7), and on the minimal chart the
product defining `w_unit` is **empty**.  `n−1` is a product of local factors
of a **lift**.  Paper 44 §9.4(a) records that the old Theorem 11.1's
*computation* is correct as a computation about the lift; it is that, and not
a discharge.  *Replaced by:* §11 of this version (external inputs) and §14.3
(the true handoffs).  See also §9bis W2, W3 of Paper 44.

**W45.8.  §12.1's `G_rad`, Proposition 12.2, Theorem 12.3.**  *Withdrawn.*
`G_rad` was a closed span inside the withdrawn completion, and Theorem 12.3's
"the comparison of `I_A` with `T` is ill-posed" is false on the declared
carrier, where `I_A(F,G) := T(F⋆G^†)` **is** Paper 43 Definition 9.2 on one
domain.  *Replaced by:* Definition 12.1, Theorem 12.2, Remarks 12.3–12.5.

**W45.9.  Theorem 12.5 and Corollary 12.6 (the deepest-stratum index
`n^{−1/2}(n−1)`, and "`χ_A` is the shadow's character on the single-zero
layer").**  *Withdrawn as referring to a lift artefact and to a withdrawn
filtration.*  Paper 44 §9bis W1 and Lemma 3bis.1.  *Replaced by:* nothing —
the question does not arise on the declared carrier.

**W45.10.  Corollary 8.2's Hodge-index reading ("row D's target is, verbatim,
the Hodge index statement for `N_A`").**  *Withdrawn.*  Paper 43 Theorem 14.1
proves there is **no** Hodge-index shape on `N_A`: the form is indefinite with
infinite index on both sides and the primitive sector has no orthogonal
complement.  *Replaced by:* Warning 8.5 and §14.4.

**W45.11.  §0.2's "four new theorems" and §0.3–§0.5.**  *Rewritten.*  Items
(1) (no corner terms) and (2) (the two halves at different places) are false
on the declared carrier (W45.1, W45.4); item (3)'s slogan "one operator
produces both" was withdrawn in phase 128 (`C5`) and is not restated; item (4)
survives and is Theorem 8.1, with the ruling labels corrected (Remark 8.2).
*Replaced by:* §0.1's four items, which are Theorem 9.4, Theorem 9.6,
Theorem 9bis.2′ and Theorem 12.2.

**W45.12.  Theorem 9.2 as `CLASSICAL`.**  *Superseded, not withdrawn.*  D128
`C4` correctly broke the old sketch and correctly disposed of it by labelling
the explicit formula `CLASSICAL`, and it restated clause C.8 to mean "no
black-boxed spectral realization".  This version restores the **strong** form
of C.8: Theorem 9.4 proves the explicit formula here, from the imports (E1)–(E5)
named in §11.  D128's restatement of C.8 is therefore no longer needed, and
the clause is met in the form the closure plan wrote it.

**W45.14.  §14.4's sentence "nothing in row C depends on it" (the constant).**
*Withdrawn as **false**.*  **[REBUILT, phase 132, round 2, finding `M1` of
`R132.002`; this is the disposal of D128 `C9`, which round 1 relocated and
understated.]**  By Corollary 9.6a(i) a nonzero constant `c` adds
`c‖F‖²_{L²}` to `I_∞(Γ_F,Γ_F)`, and that term does **not** vanish on the
primitive sector — `M(Γ_F) = 0` kills the *polar* packet, not the `L²` norm.
So (9.9), (9.10) and §14.4 item 4 ("row D's target implies RH") are statements
about the trace **with `c := 0`** and are false for any other constant.  D128
`C9` said exactly this ("`I_A` is well defined modulo `R·‖·‖²`, and for a
**sign** statement that is not harmless") and it was right.  *Replaced by:*
**Corollary 9.6a** — `c = 0` is the **unique** constant compatible with the
Weil comparison — plus Remark 9.6b and the rewritten final paragraph of §14.4,
which separates that `c` from Paper 43's unrelated comparison constant
`c_cut`.  The replacement is a strengthening: Paper 43 Definition 8A.7d
*declares* `c := 0` and, in its phase-130 text, gave four reasons none of
which was a derivation; row C now derives it.  **[phase 133, PANEL_2 MINOR-5:
the phase-132 edit rewrote Paper 43 Definition 8A.7d so that reason (iv) **is**
a derivation, citing Corollary 9.6a; the quotation is dated accordingly.]**  A one-sentence `[phase 132]` note has been added at
Paper 43 Definition 8A.7d (§14.5).

**W45.15.  Theorem 9bis.2 of round 1, and the name `T̂_∞^{mer}`.**
*Withdrawn as a misnomer and demoted as a theorem.*  **[REBUILT, phase 132,
round 2, finding `M3` of `R132.002`.]**  `A(s)+A(1−s)` is **not** the symbol of
the colimit trace — `T_∞` is a finite sum at each test and has no Fourier-side
function (Theorem 9.6′) — and its vanishing is a one-line restatement of the
functional equation, so clause C.4's polar half was being discharged by a
definition plus a negative, which is D128 `C3`'s failure mode in a new place.
The name occurs nowhere in this version.  *Replaced by:* Definition 9bis.1a
(the **continued Euler-product symbol**, with an explicit box saying it is not
the symbol of `T_∞` and that (C1) does not govern it), **Theorem 9bis.2′** (the
one-sided residue computation `Res_{s=0}A = Res_{s=1}A = 1` against
`Res_{s=0}A_S = |S_f|+1`, `Res_{s=1}A_S = 0`), Remark 9bis.2a (the two
collapses, tabulated) and Remark 9bis.2b (the reflected sum, demoted).

**W45.16.  The citation of Theorem 5.1 inside its excluded case.**
*Withdrawn as a defective citation; the statement stands.*  **[REBUILT,
phase 132, round 2, finding `M4` of `R132.002`.]**  Round 1's Theorem 9.6 and
Lemma 1.3(S1) cited Paper 44 Theorem 3bis.7, which is stated **for
`0 ∉ supp h`**, in a case where `h = F⋆F^†` has `h(0) = ‖F‖²_{L²} > 0` always;
the parenthesis "use (1.2)'s regularized `W_∞`" was a gesture, and the naive
`∫K(|t|)h(t)dt` **diverges** at `t = 0`, so the identity does not follow by
continuity either.  *Replaced by:* **Lemma 5.1a**, proved from two citations
that carry no support hypothesis — the unit packets vanish identically and
pointwise on radial classes (Paper 44 Thm 3bis.7 proof step (1)) and the
Plancherel form (9.13) holds on all of `D_A` (Paper 43 Thm 9.7(d)) — through
which Lemma 1.3, Theorem 9.6, Theorem 9.6′ and Theorem 12.2 are now routed.

**[Round 3, note `n4′` of `R132.005`: W45.14–W45.16 were inserted above
W45.13, so the numbering runs 1–12, 14, 15, 16, 13.  Sixteen items; the order
is odd and is left as it is, since renumbering a withdrawal ledger destroys the
cross-references that cite it.]**

**W45.13.  "External inputs: none", and the residual `C10` items.**
*Corrected in phase 128 and again here.*  §11 is the complete list.  `I_A` is
Paper 43 **Definition 9.2** (the old text said "9.1" in one place and "9.2" in
another); `F` must be **real** for `g(½+iτ) = |\hat F(τ)|²` (Lemma 9.1, and it
is now a standing hypothesis of every theorem that uses it); `Σ_ρ` is in the
**symmetric order** (Lemma 9.2, carried into Theorems 9.4, 9.6, 10.4); the
rescaling of `a_N,b_N` is replaced by (10.1); `Π`'s injectivity is by
**analyticity** (Corollary 10.2).

---

## 14. Verdict, clause table, dependencies, handoffs

### 14.1 The label

**[REBUILT, phase 132, round 1.]**  This paper does **not** claim a label, and
does not grant one.  The grading is the audit of record's.  What it asserts is
the clause table of §14.2 and nothing beyond it.

### 14.1a Lead decision of record (R132.007, 2026-09-12)

**[Inserted by the session lead as audit of record.]**

    ROW C: WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier (a fixed
           finite chart with its chart system and colimit as declared
           structure), as a theorem about row A's declared trace with c = 0,
           the explicit formula PROVED in the repository (Thm 9.4).
           Granted 2026-09-12 after builder rounds 1–3 and hostile audits
           R132.002 (EARNED WITH REPAIRS) and R132.005 (GRANTED conditional
           on R1 + r1–r10, all verified by grep in R132.007 §1).

Recorded beside the label (R132.005 §8.3, adopted): (1) the normalization
`c := 0` is load-bearing and is now pinned by Cor 9.6a as the unique constant
with `I_∞^{(c)} = B_nuc` — an identity-level uniqueness, not a statement about
the sign condition; `c_cut` is a different, open quantity; (2) row C does not
prove that `Σ_vW_v` is the character of a localization — place-additivity is
definitional (row A's declared trace) and is said so; `𝓝_∞^W = 0` and Paper 43
Thm 8A.7b are declined; (3) the comparison theorem is a colimit statement
((C1)), exact at a chart inside the window of Paper 43 Thm 8A.7c(e) and false
outside it; `𝓝_∩ = 0` is fixed-chart; (C1) does not govern the continued
Euler-product symbol `A`; (4) clause C.4's polar half is Thm 9bis.2′ (residues
`|S_f|+1`, `0` at a chart; `1`, `1` in the continuation; the pair is the polar
packet `β_T(M,M)`); Mertens is quarantined in Thm 9bis.4(ii),(iii) and serves
no discharge; `Ξ ≡ 0` is a remark; (5) imports (E1)–(E8), (R1) only — no
Meyer, no spectral realization, no cutoff theorem; (6) no sign, nothing about
zero locations outside §9.5 and §10; (7) row D inherits `I_∂ ≤ 0` on primitive
radial classes of `D_A^∞` with `c = 0`, plus Paper 43 Thm 14.1 and Paper 44
Thm 8bis.4a as standing negatives; (8) the `[phase 132]` cross-paper records in
Papers 43 and 44 change no theorem, proof or row label; (9) as for rows A and
B: the section theory with nonnegative dimension that turns Riemann–Roch into
an inequality is the content of RH and belongs to row D.

### 14.2 The contract table, re-issued

| clause | status | where, by theorem number |
|---|---|---|
| **C.1** test class inside row A | `PROVED` (by citation; nothing constructed) | Def. 3.1, Prop. 3.2 = Paper 44 Def. 3bis.6, Lem. 3bis.6a; typing of the point classes in Rem. 3.3 = Paper 44 Def–Thm 3bis.8, Thm 8.3, Thm 3ter.14 |
| **C.2** realization; the two Tate terms | `PROVED` at the chart, with the rulings in the completion | Thm 8.1, Rem 8.2 (ruling labels corrected), Prop. 8.3 = Paper 43 Thms 9.1, 9.13(a), 9.14a–c′, Cor. 8.4 = Paper 43 Thm 9.14b |
| **C.3** trace identity; finite, archimedean, identity | `PROVED` as a theorem about row A's **declared** trace, and stated as such; place-additivity is **definitional** and §5.1 discloses it | §5.1; Thm 5.1 = Paper 44 Thm 3bis.7 on Paper 43 Thm 8.8; **Lemma 5.1a** for the identity case `0 ∈ supp h`, with no support hypothesis (round 2, `M4`); constant `c := 0` now **derived**, Cor. 9.6a |
| **C.4** prime term, Gamma term, poles in one comparison | `PROVED`, all three off one object (the symbol); the polar half by a **residue computation**, not by a definition | primes: Thm 5.1, Lem. 5.1a; Gamma: Thms 7.2–7.5 (with D128 `C5` honesty carried); poles: Thm 7.5, Lem. 9bis.1, **Thm 9bis.2′** (`Res_{s=0}A = Res_{s=1}A = 1` vs `|S_f|+1` and `0` at a chart), Rem. 9bis.2a, Cor. 9bis.3, Thm 9bis.4.  Rem. 9bis.2b (`Ξ ≡ 0`) is used by **no** clause.  `CLASSICAL` (E8) is used **twice** (Thm 9bis.4(ii),(iii)), quarantined, with a deletion test for both — and **clause C.4's discharge uses neither** (round 3, `r5`, `r6`) |
| **C.5** order of limits | `PROVED`; no two limits are interchanged | §9.6, nine rows, each with its certificate; row 7's certificate is the **named** import (E3c), not a consequence of (E3d) (round 2, `M2`); and by Rem. 9.8 the zero sum is **absolutely** convergent for this test class |
| **C.6** `I_A = B_nuc`; sufficiency | first half `PROVED` **for the trace with `c := 0`, and `c = 0` is the unique such constant** (Lem. 1.3, **Thm 9.6**, **Cor. 9.6a**); second half `PROVED` (**Thm 10.4**, with the `C10` fix at (10.1), using (E2)'s no-real-zeros clause) | §§1.4, 9.5 (Thm 9.6, Cor. 9.6a), 10.3 |
| **C.7** no zero position assumed for any sign | `PROVED`; and **no sign is proved anywhere** | Rem. 9.7; Warning 8.5 = Paper 43 Thm 14.1, Paper 44 Thm 8bis.4a |
| **C.8** no analytic black box | `PROVED` in the **strong** form: the explicit formula is proved here | **Thm 9.4**, and **Cor. 9.4a** for an arbitrary real even test; §11 names every import — (E1),(E2),(E3a)–(E3d),(E4)–(E8),(R1) — with the clause it serves and the theorem that uses it; no spectral realization is imported |
| **C.9** compatibility with A and B; handoffs | `PROVED`; the old §11 obligation is deleted, not discharged | §13 W45.7, §14.3 |
| — | **A.6 for the radial sector** (Paper 43's clause, re-proved here on `D_A^{rad}`) | `PROVED` at every finite chart; **not claimed in the colimit** | **Thm 12.2**, Rems 12.3–12.5 |

### 14.3 Dependencies, by theorem number, both directions

**Used from Paper 43 (row A).**  Lemma 3.3 (the carrier, §1.2); Corollary 3.4
(`D_A` is an algebra); Definition 8.5, 8.6 and (8.5), (8.5∞), Remark 8.6a,
(8.5b) (the declared trace and its measures, §§1.2, 5.1); Theorem 8.8
(absolute convergence off the identity, §§5, 9.6); Definition 8A.7d (`c := 0`,
carried into every theorem, §§1.2, 5.1, 9.5, 12); Theorem 8A.7b (`𝓐_tr`
Banach `†`-algebra — **declined**, see below); Theorem 8A.7c (the colimit
trace and the window statement, §§1.2, 9.5, 9.6); Theorem 9.1 (the external
Tate characters, `M`, `β_T`, §8); Definition 9.2 (`I_A`, §§1.2, 12); Theorem
9.3 (Hermitian, continuous); Theorem 9.7 (the symbol: reality, analyticity,
boundedness, Plancherel form (9.13), §§9bis, 12); Theorem 9.7b (Mittag–Leffler
form, universal Tate residue, the contour identities, §§7.5, 9bis);
Theorem 9.8 (`𝓝 = 0`, §12, and as the model for Theorem 12.2's argument);
Theorem 9.13(a) (no module splitting, §8.2); Theorem 9.14, 9.14a, 9.14b,
9.14c, 9.14c′ and Definition 9.14c0 (the completion and the rulings, §§8.2,
9bis.4(iv), 12.3); Theorem 10.8b (Mertens, `CLASSICAL`, §9bis.4(ii));
Theorem 14.1 (no Hodge-index shape, Warning 8.5, §14.4); §14.0a (the carrier,
§1.2); §14.1a (what row C may use).

*The five bullets below: the three items Paper 43 §14.1 actually hands to row C
— Thm 10.8b (item 5), Thm 14.1 (item 1) and the window statement 8A.7c(e)
(item 4) — each **used**; plus two items row C **declines**, recorded here so
the decline is deliberate.  **[Round 3, note `n5′` of `R132.005`: round 2's
"the five items Paper 43 hands to row C" conflated the handoffs with the
declines.  The count of bullets is five; the count of handoffs is three.]***
**[REBUILT, phase 132, round 2, minor `m5` of `R132.002`: round 1 wrote "the
three items Paper 43 §14.1a hands to row C" above **five** bullets, and
§14.1a is not where that list lives.  The pointer and the count are fixed;
§14.1a itself was stale and has been corrected in Paper 43 — see §14.5(c).]**

* **Theorem 10.8b (Mertens).**  **Used**, once, in Theorem 9bis.4(ii), with
  its `CLASSICAL` label, quarantined in §11 as (E8).
* **Theorem 14.1 (the negative).**  **Used**, in Warning 8.5 and §14.4, to
  delete the previous version's Hodge-index reading (§13 W45.10) and to state
  row D's target honestly.
* **The window statement Theorem 8A.7c(e).**  **Used**, in Theorem 9.6's chart
  clause, in Theorem 9.6′'s proof (where it makes the convergence *exact*),
  and in §9.6 row 3.
* **Theorem 8A.7b (`𝓐_tr` nuclear Banach `†`-algebra, and `Det_S^{rel}`).**
  **Declined**, with the reason: row C's statements are about the bilinear
  form `I_A` on `D_A^{rad}` and about the symbol, and no determinant of the
  theory is used.  Nothing in §§3–12 invokes it, and nothing would change if
  it were deleted.
* **Theorem 8.10 / Remark 8A.7e (the comparison constant `c_cut`).**
  **Declined**, with the reason: this paper works with `c := 0` throughout
  (Definition 8A.7d) and never compares with an imported cutoff
  regularization; `c_cut` is undetermined in Paper 43 and nothing here needs
  it.  Recorded as an open comparison item that row C does not inherit.

**Used from Paper 44 (row B).**  Definition 3bis.6 and Lemma 3bis.6a (the test
class, §3); Theorem 3bis.7 (the prime packet, §§5, 9.5); Definition–Theorem
3bis.8 (the representing measures `ω_fin`, `ω_∞`, and the type warning about
`Γ_n^{rad}`, §§3.3, 4, 7); Theorem 8.3 and Theorem 3ter.14 (the point classes
lie in `N_A^{dist}`, §3.3); Theorem 3ter.10 and Corollary 3ter.10b (the
Frobenius has no archimedean contact; the complementary-slice dichotomy —
**used** in §5.2's distinction and in §14.4); Theorem 3ter.12 (composite
labels: the support meets no stratum, §5.2); Theorem 8bis.1e (the Weil kernel
is the Gram form of `Frob ⋆ Δ^{rad}` — **used** in §14.4 to name the object
whose sign is row D's); Theorem 8bis.4 (the interface, (i) `PROVED`,
(ii) **`PROVED-IN-REPOSITORY`** — it is this paper's Theorem 9.4 —
(iii) `CLASSICAL` (Weil's criterion), §§8.3, 14.4)
**[phase 133, PANEL_2 MAJOR-2: this read "(ii)–(iii) `CLASSICAL`", i.e. this
paper recorded as `CLASSICAL` the very statement it proves in its own
Theorem 9.4 and relabelled in §14.5(a).]**; Theorem 8bis.4a and Remark 8bis.4b
(positivity fails on the pure Frobenius form at every chart; the colimit
version `OPEN`, Warning 8.5); Theorem 8bis.8 and Corollary 8bis.8a
(`vol(Z_p^×) = \log p` unique given a universal Tate residue, §§1.6, 6, 7.5);
Remark 8bis.8b (chart-invariance does **not** force it — used verbatim in
Corollary 9bis.3); conventions **(C1)** and **(C2)** (§1.2, carried into
Theorems 9.6, 9.6′, 9bis.4(ii),(iv) and §14.4 — **and deliberately not into
Definition 9bis.1a or Theorem 9bis.2′**, which are statements about the
continued Euler-product symbol `A` and are chart-independent by construction;
**[REBUILT, phase 132, round 3, finding `r1` of `R132.005`: round 2 listed the
**withdrawn** theorem number `9bis.2` here and asserted that (C1) is carried
into it, the exact opposite of Definition 9bis.1a's box]**); (8bis.9) (the two Tate
conditions, §§8.1, 10.2); (8bis.14a), (8bis.14e) (the sign convention,
Lemma 1.3); §9, §9bis W1–W3 (the `n−1` obligation never existed, §13 W45.7);
§10.4's lead decision of record (the label and what travels beside it).

*The four items Paper 44 §9 hands to row C, each used or declined:*

* **§9.1, the prime packet.**  **Used**: Theorem 5.1, and it is the finite side
  of Theorem 9.6.
* **§9.2, the archimedean density `ω_∞(\log n) = K(\log n) = n^{3/2}/(n²−1)`.**
  **Used** in §1.5's constants table and in §7; note it is a **density**, not a
  contact, and this paper never calls it one.
* **§9.3, `Λ` = shell volume.**  **Used**: Theorem 4.1(ii), Corollary 6.2(ii).
* **§9.3a, the contact locus (Theorem 3bis.7′).**  **Used** in Corollary 5.2's
  reading and in Remark 5.3; it is what lets §5 say the geometric side is a
  contact locus on the carrier rather than a quotation of `Λ`.
* **Theorem 8bis.1e and the two-slice theorem (Theorem 8bis.1′).**  **Used**
  in §14.4 only, to name row D's object.  Declined elsewhere: this paper's
  comparison runs on the radial family, where 8bis.1e's content — that the
  full kernel is the Gram form of `Frob ⋆ Δ^{rad}` — is an identification of
  the *source* of the kernel and is not needed for (9.9).

**What row C hands back.**  To row A: nothing is asked of it; Theorem 12.2 is
a strengthening of Paper 43 Theorem 9.8 to a smaller test space and may be
cited there.  To row B: Theorem 9.4 discharges, with a proof in the
repository, the `CLASSICAL` import carried in Paper 44 Theorem 8bis.4(ii) —
"the Weil explicit formula converts `T(Γ_{g⋆g^†})` into `Σ_ρ\hat h(ρ)` minus
the Tate/polar terms".  Paper 44 may replace that citation by Theorem 9.4 of
this paper, and the label of 8bis.4(ii) may be changed from `CLASSICAL` to
`PROVED-IN-REPOSITORY (Paper 45 Thm 9.4)`.  **Weil's criterion itself —
8bis.4(iii)'s biconditional — stays `CLASSICAL`**, and this paper does not
touch it.

### 14.4 What row D inherits

**[REBUILT, phase 132, round 1.]**  Stated with every hypothesis carried.

> **ROW D'S TARGET (boxed identically in Paper 43 §14.1, Paper 44 §8bis.4(vi)
> and §10.4, and Paper 45 §14.4).**  **[phase 133, PANEL_2 §5 / PANEL_3
> recommendation.]**
>
> **ROW D'S TARGET: I_∂ ≤ 0 on every primitive radial class Γ_g, g ∈ C_c^∞(R), on the colimit D_A^∞ with T_∞ and c = 0 (Paper 45 Cor 9.6a); this implies RH by Paper 45 Thm 9.6 (9.10) and Thm 10.4. Standing negatives: Paper 43 Thm 14.1, Paper 44 Thm 8bis.4a; Paper 44 Thm 8bis.7 is conditional under (H_L), OPEN.**


    ROW D'S TARGET, and nothing else:

      I_partial <= 0 on every primitive radial class Gamma_g,
      g in C_c^infty(R), on the COLIMIT D_A^infty with T_infty
      (convention (C1) of Paper 44; Paper 43 Thm 8A.7c).

Beside it, four facts that row D may not ignore:

1. *It is a colimit statement and it is false at a finite chart.*  Paper 44
   Theorem 8bis.4(iii) and its round-5 quantifier note; at a fixed chart the
   kernel carries only the primes of `S_f` and, by Paper 43 Theorem 14.1, both
   forms are indefinite there.
2. *There is no Hodge-index shape to argue with.*  Paper 43 Theorem 14.1
   (indefinite, infinite index both sides, `(D_A^{prim})^{⊥I_A} = 0`); Paper 44
   Theorem 8bis.4a (positivity fails on the pure Frobenius form at every
   chart, unconditionally; the colimit version `OPEN`).  Warning 8.5.
3. *The object whose sign is at issue is named.*  It is the Gram form of
   `Frob ⋆ Δ^{rad}` — the **full** Weil kernel `W_fin + ω_∞` — and not the
   Frobenius Gram form (Paper 44 Theorem 8bis.1e, 8bis.1′, 8bis.4(vi)).
4. *The chain to RH is now complete at this joint.*  By Theorem 9.6 (9.10),
   `I_∞(Γ_F,Γ_F) = −Σ_ρΦ_F(ρ)Φ_F(1−ρ)` on primitive radial classes, proved
   here and not cited; by Theorem 10.4 the primitive class is sufficient for
   Weil's criterion.  Row D's target therefore implies RH, unconditionally,
   with the explicit formula proved in the repository.

**The normalization is load-bearing, and it is now derived.**  **[REBUILT,
phase 132, round 2, finding `M1` of `R132.002`.  Round 1's paragraph here said
"nothing in row C depends on it".  That sentence was **false** and is withdrawn
(§13, W45.14).]**  Two different constants must be kept apart, and row D
inherits them differently.

1. *The identity-class normalization `c` of Paper 43 (8.4).*  **Every** theorem
   of §§9, 9bis, 10, 12 — and therefore item 4 above — is a statement about the
   trace with `c := 0`.  For any other `c`, Corollary 9.6a(i) gives
   `I_∞^{(c)}(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ) + c‖F‖²_{L²}`,
   the correction does **not** vanish on the primitive sector, and **the
   identification of row D's target with Weil's criterion made in item 4 above
   — which goes through the identity (9.10) — is available only for `c = 0`.**
   **[REBUILT, phase 132, round 3, `R1`: round 2 wrote "the equivalence with
   Weil's criterion fails", which asserts an unproved biconditional about the
   sign condition for `c ≠ 0`.  What is available is the identity, and that is
   what item 4 uses.]**  And `c` is no longer a free declaration: by
   **Corollary 9.6a(iii)** it is the **unique** real constant for which the
   **identity** holds.  Row D inherits `c = 0` as a **theorem of
   row C**, not as a convention — and that is the closure of D128 `C9`, which
   asked exactly this question and is otherwise open.
2. *Paper 43's comparison constant `c_cut` (Theorem 8.10, Remark 8A.7e).*  This
   is a **different** quantity: it measures the declared trace against an
   **imported** analytic regularization whose own real coefficient P123.004 §4
   and P123.035 §6 forbid citing, and Paper 43 states in terms that the
   computation "does not close" and claims no value.  `c_cut` is **not** the
   `c` of Corollary 9.6a, it is unrelated to the Weil comparison, and nothing
   in rows C or D needs it.  It stays open in row A, and it is recorded here so
   that row D neither inherits it silently nor confuses it with item 1.

---

### 14.5 Cross-paper edits made in round 2

**[REBUILT, phase 132, round 2.  Authorized by the lead (`R132.003` `LF5`) and
by the hostile auditor's cross-paper notes `n4`, `n5` (`R132.002`).  Each is
one sentence or one block, marked `[phase 132]` in the target paper, and each
names the theorem it concerns.  Grep evidence is in `R132.004` §3.]**

| # | target | edit | why |
|---|---|---|---|
| (a) | Paper 44 Thm 8bis.4(ii) | the explicit formula relabelled `CLASSICAL` → **`PROVED-IN-REPOSITORY` (Paper 45 Thm 9.4)**; **Weil's criterion, 8bis.4(iii), stays `CLASSICAL`** | row C now proves what row B imported |
| (b) | Paper 43 §14.0 obstacle list, row `𝓝_∞^W = 0` | "`CLASSICAL`, row C" replaced by "**declined by row C** (Paper 45 §0.2, §14.3); not claimed by any row" | row C declines it; the row said it was row C's |
| (c) | Paper 43 §14.1a | a new `[phase 132]` block stating what row C **actually** used and declined, and marking the round-129 paragraph superseded (`c` is no longer "the open constant of Rem 8.6b"; `Γ_n = E_{a_S(n)}` is a withdrawn-carrier object; `G_rad` is withdrawn) | auditor's note `n4`: §14.1a was stale |
| (d) | Paper 43 Def 8A.7d, reason (iv) | the citation of the withdrawn `χ_A` replaced by "**derived**: Paper 45 Cor. 9.6a"; reasons (i)–(iii) stand.  **[Round 3, `r10`: round 2 wrote "(i)–(ii)" here and in Paper 43's own edit, disagreeing with Rem. 9.6b(2)'s "(i)–(iii)".  Reason (iii) — the intrinsic Mittag–Leffler constants — **is** independent and does stand; Rem. 9.6b was right and both other places are corrected.]** | auditor's note `n5` + `M1`: the fourth leg pointed at an object Paper 45 withdraws (§13 W45.3) |
| (d′) | Paper 43 §14.0 obstacle list, row `c_{cut}` | a `[phase 132]` clause separating `c_{cut}` from the identity-class constant `c`, the latter now derived | so that the two constants are never conflated again (§14.4) |
| (e) | Paper 44 §9 (new §9.1a) and §10.4 (new item 4a) | "row C received **§9.1** (Paper 44 has no Thm 9.1 — **[phase 133, PANEL_2 MINOR-4]**) as Paper 45 Thm 5.1 — and Lem. 5.1a for the case `0 ∈ supp h` that §9.1 excludes — and (C1) as its standing convention; the explicit-formula import of 8bis.4(ii) is now Paper 45 Thm 9.4" | closes the handoff in both directions |

**Nothing else in Papers 43 or 44 was touched**, and no label of either paper
is affected: (a) and (e) *remove* an import from row B, (b)–(d′) correct
bookkeeping in row A that no clause of A used.

---

## 15. Numerical verification

The script
[`verify_132_explicit_formula.py`](../../03-research/phase-132-row-c-closure/scripts/verify_132_explicit_formula.py)
checks, with `mpmath` at 30 digits:

1. **The explicit formula (Theorem 9.4)** for two or three real compactly
   supported `F`, against the first `~100` nontrivial zeros of `ζ`
   (`mpmath.zetazero`) in symmetric order.  *Illustration only*: the zero sum
   is conditionally convergent and the truncation error is visible and
   reported.
2. **Theorem 9bis.2′**, the Tate residues: `Res_{s=0}A = Res_{s=1}A = 1`
   against `Res_{s=0}A_S = |S_f|+1` and `Res_{s=1}A_S = 0`; and
   Remark 9bis.2b, `A(s) + A(1−s) ≡ 0`, at several off-real points.
3. **Lemma 9bis.1(iii)** and **Theorem 7.5**: the residue of `Σ_{p∈S}f_p + a`
   at `s = 0` is `|S_f| + 1`; the archimedean residue is `1`.
4. **Lemma 9bis.1(i),(ii)**: `\hat W_p(τ) = f_p(s)+f_p(1−s)` and
   `\hat W_∞(τ) = a(s)+a(1−s)` against Paper 43 (9.11) and (7.2).
5. **The five dictionaries** of §§1.3–1.7, numerically: the archimedean
   constants (`\log π − ψ(¼) = 5.372…`, `γ+\log4π+ψ(½) = \log π`,
   `K(\log n) = n^{3/2}/(n²−1)`), the three sign conventions of Lemma 1.3, the
   Fourier/Mellin dictionary `Φ_F(½+iτ) = \hat F(−τ)` and
   `(λ_−,λ_+)(Γ_F) = (Φ_F(1),Φ_F(0))` (Remark 8.2's swap).
6. **Corollary 9.6a**: the `c`-term of `I_∞^{(c)}` equals `c‖F‖²_{L²}` and does
   **not** vanish for a primitive `F ≠ 0`, so `c = 0` is the unique constant
   compatible with the Weil comparison.

Run it from the repository root; it prints a `PASS`/`FAIL` line per check.
