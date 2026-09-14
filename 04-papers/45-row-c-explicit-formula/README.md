# Paper 45 — Row C: the explicit formula on row A's declared carrier

> **Status, 2026-09-12 — rebuilt in phase 132, round 2, label not claimed.**  The paper
> is rebuilt from the banner down onto the carrier that Papers 43 and 44
> actually declare (Paper 43 §14.0a).  The previous version was written against
> the **old** row A — a Fell completion, the zero-count filtration `Z_J` with
> corner strata, `χ_A` assembled term by term, and a §11 discharging an `n−1`
> obligation that Paper 44 §9bis W1 has since proved never existed.  None of
> those objects is the declared carrier.  The paper does not claim a label; it
> states clause by clause what it proves and on which carrier (§14.2) and hands
> the grading to the audit of record.  Withdrawal ledger: §13.
> Round 2 repairs the four `MAJOR` findings of the hostile audit of record
> ([R132.002](../../03-research/phase-132-row-c-closure/R132_002_AUDIT_ROUND1.md),
> which graded the round-1 paper `EARNED WITH REPAIRS`) and the five findings
> of the lead audit
> ([R132.003](../../03-research/phase-132-row-c-closure/R132_003_LEAD_AUDIT_ROUND1.md)).
> Two of the repairs make the paper **stronger** than round 1 claimed:
> Corollary 9.6a (`c = 0` is *derived*, not declared) and Theorem 9bis.2′ (a
> one-sided residue computation in place of a vanishing).  Builder records:
> [R132.001](../../03-research/phase-132-row-c-closure/R132_001_BUILDER_ROUND1.md),
> [R132.004](../../03-research/phase-132-row-c-closure/R132_004_BUILDER_ROUND2.md).
> Previous audit of record:
> [D128.003](../../03-research/phase-128-adversarial-audit/D128_003_AUDIT_C.md).

[main.md](main.md) — the complete construction and proofs.

## What row C is, now

Row C is the **comparison theorem** between row A's declared trace on row B's
radial classes and the spectral side of the Weil explicit formula — with the
explicit formula **proved in the repository** and no analytic black box.

The test class is not constructed here: it *is* Paper 44's
`Γ_h ∈ D_A^{rad} ⊂ D_A = C_c^∞(C_S)` (Def. 3bis.6, Lem. 3bis.6a).  The trace
identity is not assembled here: it *is* Paper 43 Theorem 8.8 evaluated on
radial classes by Paper 44 Theorem 3bis.7.  The corner-strata problem has no
referent: `C_S ≅ R^× × ∏_p Z_p^×` is a **group**.  What is genuinely row C's
is four theorems.

### 1. The explicit formula, proved (Theorem 9.4)

The phase-128 audit (`C4`) broke the old sketch, which shifted a contour
across the zeros it was computing.  The correct argument does not need that
shift and is written out in full: the argument principle on rectangles whose
horizontal sides avoid the zeros (using the **local** Riemann–von Mangoldt
count `N(T+1) − N(T) = O(log T)`, import (E3b), and the strip estimate (E3c) —
**not**, as round 1 wrongly said, `N(T) = O(T log T)`; round-2 finding `M2`),
the exact
partial-fraction expansion of `ξ'/ξ`, the reflection `ξ'/ξ(1−s) = −ξ'/ξ(s)`,
and then the shift of **each prime term separately**, whose integrand is
entire because `ζ'/ζ` has already been expanded.  Clause C.8 is therefore met
in the **strong** form the closure plan wrote it, not in the weakened form the
audit had to fall back on.  Every classical input is named in §11 with the
clause it serves.

### 2. The comparison theorem (Theorem 9.6)

For real `F ∈ C_c^∞(R)`, on the colimit `D_A^∞` with `T_∞` (Paper 44's
convention (C1)):

    I_∞(Γ_F,Γ_F) = T_∞(Γ_{F⋆F^†}) = β_T(M(Γ_F),M(Γ_F)) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ),

and on the primitive sector `I_∞ = −Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = −q(F) = B_nuc(F,F)`.
At a finite chart it holds inside the window `R(Γ_h) < log ℓ_next(S)` and is
**false** outside it — the quantifier is carried explicitly, as Paper 44
requires.  Theorem 9.6′ states the distributional reading: at a chart `T̂_S` is
a real-analytic function; in the colimit it is **not a function**
(`Ŵ_fin^∞(0) = +∞`), and the explicit formula is exactly what it is as a
functional on `|F̂|²`.

### 3. The Tate residues: `|S_f|+1` at a chart, exactly `1` in the
continuation (Theorem 9bis.2′)

Write `s = ½ + iτ`.  Paper 43's local symbols are `Ŵ_p(τ) = f_p(s)+f_p(1−s)`
with `f_p(s) = (log p)p^{−s}/(1−p^{−s})`, and `Ŵ_∞(τ) = a(s)+a(1−s)` with
`a(s) = ½log π − ½ψ(s/2)`.  Each of `f_p`, `a` has a simple pole at `s = 0` of
residue exactly `1` — the universal Tate residue of Paper 43 Thm 9.7b and
Paper 44 Thm 8bis.8 — so the chart total is `|S_f|+1`.  Let `A(s)` be the
**continued Euler-product symbol** `½log π − ½ψ(s/2) − ζ'/ζ(s)` (convergent for
`Re s > 1`, then continued; **not** the symbol of `T_∞`, which is not a
function at all).  Then `A(s) = −ξ'/ξ(s) + 1/s + 1/(s−1)`, and since `ξ` is
entire and nonzero at `0` and `1`:

    Res_{s=0} A   = 1            Res_{s=1} A   = 1        (chart-independent)
    Res_{s=0} A_S = |S_f| + 1    Res_{s=1} A_S = 0        (every finite chart)

**The two poles of `A` are the poles of the trivial factor `½s(s−1)` of `ξ`;
their residues against `g` are `g(0)` and `g(1)`; and that pair *is* the polar
packet `2Φ_F(0)Φ_F(1) = β_T(M,M)` of Theorem 8.1, with coefficient exactly `1`
each.**  The passage from chart to continuation is asymmetric: at `s = 0` the
`|S_f|` finite residues **evaporate** — summation over primes and analytic
continuation do not commute there (Corollary 9bis.3) — leaving the archimedean
`1`; at `s = 1` the chart has **no pole at all** and the pole is **created in
the limit** by the pole of `ζ`, at the Mertens rate
`Σ_{p≤x} log p/(p−1) ∼ log x` — the one thing Mertens is for here
(Theorem 9bis.4(iii), `CLASSICAL`, quarantined, with a deletion test covering
**both** its uses); **clause C.4's discharge does not use it**.  The
identity `A(s)+A(1−s) ≡ 0` — round 1's headline, under the misnomer
`T̂_∞^{mer}` — is demoted to Remark 9bis.2b: it is the functional equation in
one line, and **no clause rests on it** (round-2 finding `M3`).

### 4. `𝓝_∩ = 0` on the radial sector (Theorem 12.2)

Clause A.6 for the intersection form, on `D_A^{rad}` rather than on the
withdrawn `G_rad`.  This is **not** a corollary of Paper 43 Theorem 9.8: a
smaller test space can only make a radical larger.  What makes it true is that
the radial sector's Fourier transforms fill the Schwartz space on the single
component `𝔠_0`, where the symbol is real-analytic and nonzero
(`T̂_S(𝔠_0,0) ≥ 5.372`).  Fixed-chart statement; no colimit claim is made.

### 5. `c = 0` is derived, not declared (Corollary 9.6a)

D128 finding `C9` said `I_A` is well defined only modulo `R·‖·‖²` and that
"for a **sign** statement that is not harmless".  It was right, and round 1
understated it.  By Corollary 9.6a,

    I_∞^{(c)}(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ) + c‖F‖²_{L²},

and the correction does **not** vanish on the primitive sector — `M(Γ_F) = 0`
kills the *polar* packet, not the `L²` norm.  Hence **`c = 0` is the unique
real constant for which the comparison *identity* (9.9)–(9.10) holds**, and
therefore the only one for which §14.4 item 4's route from row D's target to RH
— which goes through that identity — is available.  *No claim is made about
whether the **sign condition** `I_∞^{(c)} ≤ 0` remains equivalent to RH for
`c ≠ 0`: that biconditional is unproved and is probably false for `c < 0`.
Round-3 finding `R1` deleted it.*  Paper 43 Definition 8A.7d *declares*
`c := 0` and says "none of [the four reasons] is a derivation"; row C now
**characterizes** it, and Paper 43's reason (iv) — which cited
the `χ_A` that this paper withdraws — has been replaced accordingly
(§14.5(d)).  This is the closure of D128 `C9` in the only form available: not
by computing a cutoff constant, but by proving that the Weil comparison itself
pins the normalization.  Paper 43's *separate* comparison constant `c_cut`
(Theorem 8.10) is unrelated and stays open in row A; §14.4 keeps the two apart.

### Kept from the previous version

**Theorem 8.1** (the polar packet *is* the hyperbolic ruling form) — phase 128
verified it clean; re-proved here, with a correction of record: the two rulings
were labelled the wrong way round.  `M(Γ_F) = (Φ_F(1),Φ_F(0))` is the **swap**
of the old `z(F) = (Φ_F(0),Φ_F(1))`.  Harmless, because `β_T` is
swap-invariant, but it is a real error and Remark 8.2 records it.

**Theorem 10.4** (primitive tests suffice for Weil's criterion) — phase 128
called it "the strongest and most defensible result in the paper" and found
one wrong step.  §10.3 carries out the fix: `(a,b) ↦ a + b s_0²` is an
`R²→C` isomorphism whenever `s_0² ∉ R`, so the **real** coefficients of
`106_11`'s construction realise any complex target; the previous "rescale
`a_N,b_N` by `ρ(1−ρ)`" was wrong because those coefficients must stay real.

## What this paper does not claim

No sign.  No positivity.  No statement that the colimit numerical radical
vanishes.  No statement about the location of a zero of `ζ` outside the
comparison theorem (§9.5), the contrapositive sufficiency argument of §10, and
the clauses labelled `CLASSICAL`.  Row D's target is
stated honestly in §14.4: `I_∂ ≤ 0` on primitive radial classes of `D_A^∞`, in
the colimit, and nothing else — with Paper 43 Theorem 14.1 (no Hodge-index
shape on `N_A`) and Paper 44 Theorem 8bis.4a (positivity fails on the pure
Frobenius form at every chart) carried beside it.

## Numerical record

[`verify_132_explicit_formula.py`](../../03-research/phase-132-row-c-closure/scripts/verify_132_explicit_formula.py)
— **26/26 checks pass**.  The explicit formula is verified for three real
compactly supported `F` against the first 100 zeros of `ζ` to `4·10^{−16}`
(illustration; the truncation error is reported, not hidden);
`A(s)+A(1−s) = 0` to `4·10^{−31}`; the universal Tate residue `1` per place
and the chart total `|S_f|+1 = 6`; the local symbols in the `s`-variable
against Paper 43 (9.11) and P123.035 (4.1); the chart/continuation residue table of Theorem 9bis.2′
(`Res_{s=0}A_S = 6.000`, `Res_{s=1}A_S = −2·10^{−37}`,
`Res_{s=0}A = Res_{s=1}A = 1.000`); all five convention tables of §§1.3–1.7,
including the ruling swap of Remark 8.2 and the agreement of the three sign
conventions; and Corollary 9.6a — for a primitive `F` with
`Φ_F(0) = Φ_F(1) = −3·10^{−15}` the `c`-term is still `c·11.047…`, so it does
not vanish there.

## Clause ledger

§14.2.  Dependencies by theorem number, in both directions, with each item
row A and row B hand to row C **used or explicitly declined with a reason**:
§14.3.  Withdrawal ledger (sixteen items): §13.  Cross-paper edits made in
round 2 to Papers 43 and 44, each one sentence marked `[phase 132]`: §14.5 —
in particular Paper 44 Theorem 8bis.4(ii)'s explicit-formula import is
relabelled `CLASSICAL` → `PROVED-IN-REPOSITORY (Paper 45 Thm 9.4)`, while
Weil's *criterion* (iii) stays `CLASSICAL`.
