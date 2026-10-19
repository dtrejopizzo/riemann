# R157_001 — O-150.1, importing (H-DMV) from the open secondary literature

* Task: blueprint `R157_000` round 1, row 1. Pure mathematics; no numerics; **no sign is
claimed anywhere in this document**; row D keeps no label. Paper 46 is not edited; replacement wording is in §5.*

**Primary source still not read.** H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, *Beurling primes with large
oscillation*, Math. Ann. **334** (2006) 1–36, doi:10.1007/s00208-005-0638-2. Springer redirects to an
authentication page; the Deep Blue (U. Michigan) record `hdl 2027.42/46253` returned HTTP 403. No attempt was made
to get around either. A web-search summary of the Springer abstract came back garbled ("1/2 < θ < 4/e(1−θ)") and
**is not used anywhere below**.

Label conventions: `QUOTED [file:line]` means verbatim from a secondary source in `00-references/beurling-dmv/`
(the PDF-to-text extraction mangles formulas, so formulas are re-typeset by me and the typesetting is checked
against the surrounding words); `CITED (secondary source)` is a statement about DMV that rests on such a quote;
`PROVED` means proved here from the quoted items by elementary steps; `CLASSICAL` means a standard theorem that is
not specific to DMV.

---

## 0. The finding in one paragraph

Phase 150 wrote the DMV integer law as `N(x) = ax + O(x·exp(−c√log x))` (R150_001 l.~175, "(DMV-a)"). **That was a
misquotation.** Every secondary source gives it as `N(x) = ρx + O(x^θ)` with a **fixed `θ ∈ (1/2, 1)`**. The
`x·exp(−c√log x)` term belongs to the **primes**: it is the size of the Ω± oscillation of `π(x) − Li(x)`. The audit
`R150_002` §1.1 was right that no continuation follows from the misquoted hypothesis. It was right *about that
hypothesis*. **[amended per R157_003, A1: (DMV-a) is at R150_001 l.167–171, not "l.~175". R150_001's own (DMV-b),
l.173–177, already put the `x e^{−c√log x}` term on the prime side.]** With the correct power saving `O(x^θ)`, analytic continuation of `ζ − ρ/(s−1)` to the half-plane
`Re s > θ` is immediate. It is stated as immediate in two of the sources, and BE3 and BE7 follow in one line
each (§2). The zeros are stated explicitly in the sources: infinitely many lie **on the curve**
`σ = 1 − a/log(|t|+2)`. Result: every clause of (H-DMV) is either quoted or proved from quoted items. The
verdict (§3) is that **(H-DMV) becomes `CITED (secondary source)` in full**, through a reduced statement (H-DMV′)
of two quoted clauses.

---

## 1. Deliverable (1): the DMV theorem as the secondary sources state it

### 1.1 Verbatim quotations

**S1** — Broucke–Debruyne–Vindas, arXiv 2004.11501 (Adv. Math. 370 (2020)), `2004.11501.txt` l.15–53:

> "In [10], H. G. Diamond, H. L. Montgomery, and U. M. A. Vorhauer constructed a Beurling generalized number system
> with very regularly distributed integers, but whose distribution of prime numbers has large oscillation. In fact,
> given 1/2 < θ < 1, they showed the existence of Beurling numbers with integer counting function N satisfying the
> asymptotic estimate N(x) = ρx + O(x^θ), (1.1) for some ρ > 0, and whose primes realize the de la Vallée Poussin
> error term in the Prime Number Theorem (PNT), namely, with prime counting function satisfying the oscillation
> estimate π(x) = Li(x) + Ω±(x exp(−c√log x)) for some c > 0 […]. Their Beurling number system has the additional
> feature that its associated zeta function, defined as (1.2) ζ(s) = ∫_{1^−}^∞ x^{−s} dN(x) = exp(∫_1^∞ x^{−s} dΠ(x))
> with Π(x) = Σ_{j≥1} j^{−1} π(x^{1/j}), also realizes the classical de la Vallée Poussin zero-free region; in
> particular, the Riemann hypothesis (RH) fails for it."

The same source, l.70–76: "The existence of such a number system proves the optimality of E. Landau's classical PNT
[15], which, recasted in the language of Beurling numbers, states that (1.1) always implies the validity of the PNT
in the form π(x) = Li(x) + O(x exp(−c√log x))". l.80–83: "a zeta function might not have a wider zero-free region
than that of de la Vallée Poussin if we only require that Beurling's property that the integers have multiplicative
structure and (1.1) hold." l.89–95 gives the definition: generalized primes are an unbounded sequence
`1 < p_1 ≤ p_2 ≤ …`, and the integers are the multiplicative semigroup they generate, counted with multiplicity.

**S2** — Broucke, arXiv 2409.10051, `2409.10051.txt` l.2687–2692:

> "Diamond, Montgomery, and Vorhauer [4] […] constructed for every θ ∈ (1/2, 1) a Beurling number system
> (P_DMV, N_DMV) with N_DMV(x) = Ax + O(x^θ) for some A > 0 and for which ζ_DMV(s) has infinitely many zeros on the
> contour σ = 1 − a/log(|t|+2), for some constant a > 0. They showed that, as a result, no better remainder than the
> de la Vallée-Poussin remainder O(x exp(−2√(a log x))) can be obtained in the prime number theorem".

The same source, l.2713–2718: "ζ_DMV(s) = ζ_c(s)e^{Z(s)}, where ζ_c(s) is the Mellin–Stieltjes transform of an
absolutely continuous measure dN_c (and Z(s) satisfies Z(σ+it) ≪_σ √log(|t|+2) for σ > 1/2)". l.2695–2708 gives the
zero-count lower bound `N(ζ_DMV; α, T) = Ω(T^{2λ(1−α)})`, with `λ < 1/(2(1−θ))`, and the remark that λ at the endpoint
costs `O_ε(x^{θ+ε})`. l.2733–2742: `ζ_DMV(σ+it) = Ω_ε(|t|^{(1−σ)/(1−θ)−ε})`, and the convexity bound
`ζ_P(σ+it) ≪_σ |t|^{(1−σ)/(1−θ)}` for `θ < σ < 1`, which holds for every θ-well-behaved system. l.44–47:
"[N_P(x) = Ax + O(x^θ)] readily yields the analytic continuation of ζ_P(s) − A/(s−1) to the half-plane Re s > θ."

**S3** — Broucke–Debruyne, arXiv 2211.08716, `2211.08716.txt` l.94–95: "The condition (1.2) [N(x) = Ax + O(x^θ)]
implies that ζ(s) − A/(s−1) has analytic continuation to the half-plane σ > θ." l.100–111: the zero-free region
`σ ≥ 1 − d/log(|t|+2)` holds for every well-behaved system (Landau), and "for θ ∈ (1/2, 1) this zero-free region was
shown to be optimal, apart from the precise value of d, in the seminal work of Diamond, Montgomery, and Vorhauer [3]
who constructed a Beurling system whose zeta function has infinitely many zeros on a curve of the form
σ = 1 − d/log|t|." l.113–118 (Lemma 1.1): for `α > θ` there are `O_α(log T)` zeros with `β ∈ [α, 1]` and
`|γ| ∈ [T, T+1]`, "a similar estimate was already obtained by Diamond, Montgomery, and Vorhauer as part of their
'clustering of zeros' result, [3, Theorem 2]". l.1413–1458 is the construction, "in the notations from the book of
Diamond and Zhang [4, Sections 17.4–17.9], where a slightly more streamlined version of the construction from [3]
is presented". Its data are `ℓ_k = 4^k`, `γ_k = e^{ℓ_k}`, `β_k = 1 − 1/ℓ_k` and `ρ_k = β_k + iγ_k`, with
`ζ_C(s) = s/(s−1) · Π_k G(ℓ_k(s−ρ_k)) G(ℓ_k(s−ρ̄_k))`, `G(z) = 1 − (e^{−z} − e^{−2z})/z`. The text continues: "This
defines a function holomorphic for σ > 1/2 except for a simple pole at s = 1, and admitting zeros at s = ρ_k and
s = ρ̄_k, situated on the curve σ = 1 − 1/log|t|." l.1431: "The actual discrete example (P, N) is a suitable
'approximation' of this continuous system, whose existence is guaranteed by an ingenious probabilistic method."

**S4** — Révész, arXiv 2207.00665, `2207.00665.txt` l.189–210: "They basically showed that under Axiom A the
Riemann hypothesis may still fail; moreover, nothing better than the most classical zero-free region and error term
of (9) ζ(s) ≠ 0 whenever σ > 1 − c/log t and (10) ψ(x) = x + O(x exp(−c√log x)) follows from (2) at least if
θ > 1/2." Here "Axiom A" is `N(x) = κx + O(x^θ)`, the "(2)" of that paper. Footnote l.763–766: "already Diamond,
Montgomery and Vorhauer argued [14] that anything essentially better does not hold in general (i.e. assuming only
Axiom A)".

**S5** — Broucke, arXiv 2012.06220, `2012.06220.txt` l.43–50: "Landau's PNT was shown to be optimal by Diamond,
Montgomery, and Vorhauer [6] in the case θ > 1/2. Namely, they showed the existence of a system of Beurling
generalized primes satisfying N(x) = ax + O(x^θ) and π(x) = Li(x) + Ω(x exp(−c√log x))." l.164 (Lemma 2.1) is the
DMV–Zhang discretisation lemma.

### 1.2 The statement, assembled

> **Theorem DMV (as reported; `CITED (secondary source)`, S1–S5).** For every `θ ∈ (1/2, 1)` there is a **discrete**
> Beurling generalized number system `𝒫 = (p_j)`, `1 < p_1 ≤ p_2 ≤ …`, with integer counting function `N` and zeta
> function `ζ_𝒫(s) = ∫_{1^−}^∞ x^{−s}dN(x) = Π_j(1 − p_j^{−s})^{−1}`, such that
> (a) `N(x) = ρx + O(x^θ)` for some `ρ > 0` [S1 l.17–21, S2 l.2689, S5 l.49];
> (b) `π(x) = Li(x) + Ω±(x exp(−c√log x))` for some `c > 0` [S1 l.23–28; S5 l.49 has Ω];
> (c) `ζ_𝒫` has infinitely many zeros on a curve `σ = 1 − a/log(|t|+2)`, `a > 0` [S2 l.2691; S3 l.111]. Consistently [amended per R157_003, A2: was "Equivalently"]
> it "realizes the classical de la Vallée Poussin zero-free region" [S1 l.52], and in particular RH fails for
> `ζ_𝒫` [S1 l.53; S4 l.190].

Item by item, against the four questions of the brief:

| asked | what the sources say | label |
|---|---|---|
| continuation left of `Re s = 1` | `ζ − ρ/(s−1)` is analytic on `Re s > θ` (**a half-plane**, not a thin region), for every θ-well-behaved system [S2 l.44–47, S3 l.94–95]; this is also proved in §2.1 below. The streamlined continuous model is holomorphic on `σ > 1/2` except for the pole [S3 l.1454], and `ζ_DMV = ζ_c·e^{Z}` with `Z` analytic on `σ > 1/2` [S2 l.2714–2718] **[amended per R157_003, A2: S2 states only the bound `Z(σ+it) ≪_σ √log(\|t\|+2)`, not holomorphy. Zeros and growth still transfer (R157_003 D2, also via S3 l.1431–1436), and T3 does not use the transfer]** | `CITED (secondary)` + `PROVED` |
| infinitely many zeros with `β ≥ 1 − c/log γ` | "infinitely many zeros on the contour σ = 1 − a/log(\|t\|+2)" [S2 l.2691]; "on a curve of the form σ = 1 − d/log\|t\|" [S3 l.111]; in the book model the zeros are `ρ_k = 1 − 1/ℓ_k + ie^{ℓ_k}`, so `β_k = 1 − 1/log γ_k` exactly [S3 l.1443, 1456] | `CITED (secondary)` |
| `N(x) = ρx + O(x^θ)` | yes, for each prescribed `θ ∈ (1/2,1)` [S1, S2, S5] | `CITED (secondary)` |
| RH fails | yes [S1 l.53, S4 l.190]; also immediate from (c) | `CITED (secondary)`; `PROVED` from (c) |

**What the sources do not give me** (`NOT SUPPORTED`, and not needed; see §3): the theorem numbering inside DMV
(only "[3, Theorem 2]", the clustering result, is named; S3 l.115); the value of `a` as a function of `θ`; whether
DMV's own paper uses exactly the ζ_C written in S3 or an earlier version (S3 l.1440–1441 says the book's version is
"slightly more streamlined"); and the exact growth of `ζ_𝒫` in `θ < σ < 1` beyond the general convexity bound. The
Ω-lower bound in S2 l.2734 is stated there to rest on "routine calculations which we omit".

---

## 2. Deliverable (2): item-by-item against (H-DMV) and BE1–BE8

Fix `θ ∈ (1/2,1)` and let `𝒫` be the system of Theorem DMV. BE1–BE8 are verbatim from R150_001 l.195–212. Their
region is `Re s > 1 − η(|t|)`, and I take **`η ≡ 1 − θ`** (a constant), which is allowed. **[amended per R157_003, A5:
take `η ≡ (1−θ)/2`. BE3's region is then `Re s > (1+θ)/2`, where Lemma 2.1 gives `≪_θ |t|` uniformly, as P46's (H-DMV)
wording "polynomial growth … in that region" requires. Read `η ≡ (1−θ)/2` wherever `η ≡ 1−θ` appears below.]**

### 2.1 Two elementary lemmas

**Lemma 2.1 (continuation; `PROVED`, and `CITED (secondary)` as S2 l.44–47, S3 l.94–95).** Let `dN ≥ 0` on
`[1,∞)`, `N(1^−) = 0`, and `N(x) = ρx + R(x)` with `|R(x)| ≤ Cx^θ`, `θ < 1`. Then for `σ > 1`,
`ζ(s) = ρ s/(s−1) + s∫_1^∞ R(x)x^{−s−1}dx` (with the normalisation `N(1^−) = 0`, so that the boundary term at
`x = 1^−` vanishes and `R(x) = N(x) − ρx` is bounded on compacts). The integral converges absolutely and locally uniformly on `σ > θ`. So `ζ` continues
meromorphically to `σ > θ` and its only pole is a simple one at `s = 1`, with residue `ρ > 0`. Its growth is
`|ζ(σ+it)| ≤ ρ|s|/|s−1| + C|s|/(σ−θ) + O(1) ≪_ε |t|` uniformly for `σ ≥ θ + ε`, `|t| ≥ 2`.

*Proof.* Integrate by parts, `∫x^{−s}dN = [x^{−s}N]_{1^−}^∞ + s∫N x^{−s−1}dx`, and insert `N = ρx + R` (with
`ρ∫_1^∞ x^{−s}dx = ρ/(s−1)` and `s/(s−1) = 1 + 1/(s−1)`). Then `|∫R x^{−s−1}| ≤ C∫_1^∞ x^{θ−σ−1}dx = C/(σ−θ)`. ∎

**[amended per R157_003, A3: the bound `C|s|/(σ−θ)` grows with `σ`. For uniformity on `σ ≥ θ+ε`, use it on
`θ+ε ≤ σ ≤ 2` (where `|s| ≤ 2+|t|`) and use `|ζ(s)| ≤ ζ(2)` (from `dN ≥ 0`) on `σ ≥ 2`.]**

This is exactly the step that R150_002 §1.1 correctly found **false** for `R = O(x·exp(−c√log x))`. It is true for
`R = O(x^θ)`. Only the quotation of the hypothesis was wrong.

**[amended per R157_003, A4: the proof below has a gap. "Not all in `θ < σ < θ+ε`" does not give infinitely many in
`σ ≥ θ+ε`, and zeros on `C_a` could accumulate at bounded height at `σ = θ` when `a/log 2 > 1−θ`. The lemma is `PROVED`
only if `a/log 2 < 1−θ` or `|γ_n| → ∞` is assumed. It is **not used**. The zero clause of (H-DMV′) rests instead on
Z1 (S2 l.2694–2696: `N(ζ_DMV;α,T) = Ω(T^{2λ(1−α)})` for each fixed `α > θ`), Z2 (Theorem DMV(b) + Révész, S4
l.375–377, Theorem 5) and Z3 (Zhang 2007, zbMATH `zbMATH-records.txt` l.19–23, + Révész Theorem 5). See
R157_003 D3. The "independent route" in the caveat is now Z2, with Révész Theorem 5 in place of the sketched contour
shift.]**

**Lemma 2.2 (zeros tend to the line; `PROVED` from S2 l.2691 and S3 l.116–118).** Suppose `ζ_𝒫` has infinitely many
zeros on `C_a = {σ = 1 − a/log(|t|+2)}` inside `σ > θ`. Then for every `δ > 0` it has a zero with `β > 1 − δ`.

*Proof.* On `C_a`, `σ` is an increasing function of `|t|` tending to `1`. Fix `ε > 0` with the infinitely many
zeros not all in `θ < σ < θ + ε` (see caveat). Then infinitely many lie on `C_a ∩ {σ ≥ θ+ε}`. For each `T` the arc
`C_a ∩ {σ ≥ θ+ε, |t| ≤ T}` is compact in the domain of meromorphy, and `ζ_𝒫 ≢ 0`, so it carries finitely many
zeros. The same finiteness is S3 Lemma 1.1 (l.116–118), which is a theorem for every θ-well-behaved system. Hence
`|γ_n| → ∞` along `C_a`, and `β_n = 1 − a/log(|γ_n|+2) → 1`. ∎

*Caveat for the auditor.* If `C_a ∩ {σ > θ}` is not closed near `σ = θ`, i.e. if `a/log 2 > 1 − θ`, the compactness
step is applied to `C_a ∩ {σ ≥ θ+ε}`. Zeros on `C_a` accumulating at `σ = θ` with bounded `|t|` are not excluded by
this argument. They are excluded by S3's explicit model (`γ_k = e^{4^k} → ∞`, l.1443) and by the natural reading
of "infinitely many zeros on the contour". **Independent route (`PROVED` modulo `CLASSICAL`).** Suppose some
`δ > 0` gave `ζ_𝒫 ≠ 0` on `σ > 1 − δ`. Lemma 2.1 gives polynomial growth on `σ ≥ θ + ε`, and the zero count of S3
Lemma 1.1 holds. The truncated explicit formula for θ-well-behaved systems is quoted as a Riemann–von Mangoldt
formula in S3 l.1180, 1203–1209 (Révész). With these, the standard contour shift gives
`ψ_𝒫(x) = x + O(x^{1−δ'})`, and by partial summation `π(x) = Li(x) + O(x^{1−δ''})`, `δ'' > 0`. That contradicts
Theorem DMV(b). So (b) alone also implies the conclusion of Lemma 2.2.

### 2.2 The table

| item | (H-DMV)/BE clause (R150_003 l.~101–106; R150_001 l.195–212) | status for the DMV system | label |
|---|---|---|---|
| BE1 | `Z = Σ n_k^{−s}`, `n_k ≥ 1`, abs. conv. on `σ > 1` | discrete system [S1 l.89–95, S3 l.1431]; `N(x) ≪ x` by (a) gives abs. convergence on `σ > 1` | `CITED (secondary)` (discreteness) + `PROVED` |
| BE2 | Euler product, `dΛ ≥ 0`, `log Z` with coefficients ≥ 0 | holds for every discrete Beurling system on `σ > 1`: `π(x) ≤ N(x) ≪ x` gives `Σ p_j^{−σ} < ∞`, and the identity is in S1 l.38–52, S5 l.125–140 | `PROVED` |
| BE3 | meromorphic to `Re s > 1 − η(\|t\|)`, single simple pole at 1, residue `a > 0` | holds with `η ≡ 1−θ`, residue `ρ > 0` (Lemma 2.1); **stronger than required: a half-plane** | `PROVED` from (a); also `CITED (secondary)` S2 l.44–47, S3 l.94–95 |
| BE4 | reality | `p_j ∈ R` | `PROVED` |
| BE5 | `ψ(x) ≍ x` | (a) gives Landau's PNT `π = Li + O(x e^{−c√log x})` [S1 l.70–76], hence `ψ(x) ∼ x`, hence `ψ ≍ x` for `x ≥ x_0` (and `ψ = 0` for `x < p_1`, as for `ζ`). [amended per R157_003, A6: the verbatim statement for every `θ < 1` is S5 l.32–35] | `CITED (secondary)` (Landau's theorem as restated in S1) / `CLASSICAL` |
| BE6 | no zeros on `σ > 1` | from BE2 | `PROVED` |
| BE7 | `Z ≪ \|t\|^A`, uniformly for `σ ≥ 1 − η/2`, `\|t\| ≥ 2` | with `η/2 = (1−θ)/2`, the range `σ ≥ (1+θ)/2` lies in `σ ≥ θ+ε`; `A = 1` by Lemma 2.1. The sharper convexity bound `≪_σ \|t\|^{(1−σ)/(1−θ)}` is quoted in S2 l.2742 | `PROVED` from (a) |
| BE8 | Landau: the abscissa of a nonnegative Dirichlet integral is a singularity | holds for every `∫x^{−s}dμ`, `dμ ≥ 0`; nothing DMV-specific | `CLASSICAL` |
| zeros | for every `δ > 0` a zero with `β > 1 − δ` | Theorem DMV(c) + Lemma 2.2; alternatively Theorem DMV(b) + the independent route | `CITED (secondary)` + `PROVED` (caveat in §2.1) |
| (extra) | RH fails | from (c) | `PROVED` from a cited item |

**Nothing needed by (H-DMV) or BE1–BE8 is `NOT SUPPORTED`.** The items in §1.2 that are not supported by the sources
(value of `a`, DMV's own theorem numbering, the exact ζ_C of the paper against the book's) are not used.

**Implicit items** (said by the sources in words, made explicit here): that the system is **discrete** rather than
continuous. S1 l.15 calls it a "Beurling generalized number system" with "primes", S3 l.1431 says "the actual
discrete example", and S1 l.216–218, S5 l.161–164 describe the DMV probabilistic discretisation. BE2 as written
(`Π_j(1 − p_j^{−s})^{−1}`) needs discreteness; the continuous `ζ_C` alone would satisfy BE1 only in its integral
form, and BE2 not at all. Also implicit: that `|γ_n| → ∞` for the zeros on the curve (§2.1 caveat).

---

## 3. Deliverable (3): verdict

> **Hypothesis (H-DMV′) (the reduced form; `CITED (secondary source)`).** *There exist `θ < 1` and a discrete
> Beurling generalized prime system `𝒫` with `N_𝒫(x) = ρx + O(x^θ)`, `ρ > 0`, whose zeta function has zeros
> `β_n + iγ_n` with `β_n → 1`.*
> Support: Theorem DMV(a),(c) [S1 l.15–53; S2 l.2687–2692; S3 l.108–111; S5 l.43–50]; `β_n → 1` by Lemma 2.2.
> **[amended per R157_003, A4/A7: `β_n → 1` by Z1, Z2 or Z3, not by Lemma 2.2. Independent second model: Zhang,
> Math. Ann. 337 (2007), author's abstract in zbMATH Open, Zbl 1121.11061, with Révész Theorem 5.]**

**Proposition 3.1 (`PROVED`).** (H-DMV′) ⟹ (H-DMV). *Proof.* Take `η ≡ 1 − θ` [amended per R157_003, A5: `η ≡ (1−θ)/2`; the zeros with `β_n > (1+θ)/2` lie in the BE3 region]. Then BE1, BE2, BE4 and BE6 hold
because `𝒫` is a discrete Beurling system, BE3 and BE7 by Lemma 2.1, BE5 by Landau's PNT (`CLASSICAL`; restated in
S1 l.70–76), BE8 is `CLASSICAL`, and the zero clause is part of (H-DMV′). ∎

**Verdict.** **(H-DMV) → `CITED (secondary source)` in full**, via (H-DMV′) and Proposition 3.1. Beyond the two
quoted clauses of (H-DMV′), T3's proof uses only material that is `PROVED` here (Lemma 2.1, Lemma 2.2) or
`CLASSICAL` (Landau's PNT for BE5, Landau's theorem for BE8, and in Lemma 2.2 the finiteness of the zeros of a
nonzero meromorphic function on a compact set, or the zero count of S3 Lemma 1.1). T3's proof (R150_003 Thm 2.8′)
is the soundness argument, "a derivation from BE1–BE8 is valid in every model; here is a model violating
`(ZFS_δ)` for every δ". So it needs **exactly one model**, and it does not care whether that model is DMV's own
paper version, the streamlined system of Diamond–Zhang §17.4–17.9 (S3 l.1440), or Broucke's β = 1 case (S5).
Any system reported with (a) and (c) will do. This redundancy is the strongest point in favour of the import.

It does **not** become `IMPORTED` or `PROVED`, because the primary text is unread (README rule).

---

## 4. Deliverable (4): resulting labels

| item | old label | new label |
|---|---|---|
| (H-DMV) (R150_003 §2.1; P46 §27.4) | `HYPOTHESIS` | **`CITED (secondary source)`**, via (H-DMV′) + Prop. 3.1 (`PROVED`) |
| T3 = R150_003 Thm 2.8′ = P46 Remark 27.16 | `META-THEOREM / METHOD-CONSTRAINT, conditional on (H-DMV)` | **`METHOD-CONSTRAINT (meta-theorem); PROVED modulo one CITED (secondary source) import, (H-DMV′)`** [amended per R157_003, A8: content = RESTATEMENT of DMV/Zhang + axiom list (R150_002 l.64–69, R150_003 l.671); stays a Remark in P46 (R150_005 l.43)] |
| Cor. 2.9′ | `PROVED` from 2.8′, conditional on (H-DMV) | **`PROVED` from T3; inherits the `CITED (secondary source)` import (H-DMV′)** |
| P46 Prop. 27.17 item 3 | conditional on (H-DMV) | **`PROVED` modulo `CITED (secondary source)` (H-DMV′)** |
| O-150.1 / P46 open item (41) | `OPEN`, blocking | **`CLOSED at the secondary-source level`**; residual non-blocking item: primary read [amended per R157_003, A8: "discharged at the `CITED (secondary source)` level; no longer blocking; residual `OPEN`: primary read". O-150.1 as written asks for the primary read, so "CLOSED" overstates] |
| Observation 2.7, Prop. 2.6, 2.6′ | unchanged | unchanged |

**[amended per R157_003, A8: not cleared. T3 stays a Remark until the primary text is read (R150_005 l.43).]**
**Recommendation on the form of T3 in Paper 46.** Remark 27.16 can be promoted to a **theorem
modulo a cited import**, in the same way the paper treats other imports. If the convention adopted requires a
primary-read source before promotion, it stays a Remark with the new label. The fact that it now rests on a quoted
statement rather than a belief does not depend on that choice.

**Correction for the record** (`PROVED`, bookkeeping). R150_001 l.~175 [amended per R157_003, A1: l.167–171] "(DMV-a)" misquotes DMV's integer error term
as `O(x·exp(−c(log x)^{1/2}))`. The correct term is `O(x^θ)`, `θ ∈ (1/2,1)`. The withdrawn row of P46's §27.4 table
("the inference … is false — the Mellin integral diverges for every σ < 1") remains **correct as a statement about
the misquoted hypothesis** and should gain the clause "that hypothesis misquoted DMV; with the correct `O(x^θ)` the
continuation to `Re s > θ` holds".

### 5. Replacement wording for Paper 46 (not applied)

**[amended per R157_003, A8: the texts of this section are superseded by R157_003 §5. The (41) text below attributes the
full theorem to all five sources, which S4 and S5 do not state, and it uses `η ≡ 1−θ`.]**

Paper 46 locations: the brief's line numbers (~11652–11735, 11897) are out of date. In the current `main.md`, the
Hypothesis is at **l.11842–11861**, Remark 27.16 at **l.11863–11881**, the withdrawn-table row at **l.11925**, the
§-summary at **l.12016–12017**, and open item (41) at **l.12087–12090**.

**Open item (41), replacement:**

> * **(41)** *Closed at the secondary-source level (phase 157, `R157_001`).* The open literature — Broucke–Debruyne–
>   Vindas, Adv. Math. 370 (2020) §1; Broucke–Debruyne (arXiv 2211.08716) §1 and §5; Broucke (arXiv 2409.10051)
>   §6.2; Broucke (arXiv 2012.06220) §1; Révész (arXiv 2207.00665) §1 — states the theorem of
>   Diamond–Montgomery–Vorhauer, Math. Ann. **334** (2006), as follows. For every `θ ∈ (1/2,1)` there is a discrete
>   Beurling system with `N(x) = ρx + O(x^θ)`, `ρ > 0`, and `π(x) = Li(x) + Ω_±(x\exp(−c\sqrt{\log x}))`, whose
>   zeta function has infinitely many zeros on a curve `σ = 1 − a/\log(|t|+2)`. From `N(x) = ρx + O(x^θ)` alone
>   follow meromorphic continuation to `\mathrm{Re}\,s > θ` with a single simple pole at `s = 1` of residue `ρ`, and
>   `ζ_𝒫(σ+it) ≪ |t|` on `σ ≥ θ+ε`. Hence all of BE1–BE8 hold with `η ≡ 1−θ`, and (H-DMV) holds.
>   **(H-DMV) is `CITED (secondary source)`**; Remark 27.16 is `PROVED` modulo that import. *Residual, not
>   blocking:* confirm the statement against the primary text. `CITED (secondary source)`.

**Hypothesis paragraph (l.11842–11861), replacement of the label sentence onward:**

> **Label: `CITED (secondary source)`.** Diamond–Montgomery–Vorhauer construct, for each `θ ∈ (1/2,1)`, a discrete
> Beurling system with `N_𝒫(x) = ρx + O(x^θ)` whose zeta function has infinitely many zeros on
> `σ = 1 − a/\log(|t|+2)` (as stated in Broucke–Debruyne–Vindas, Adv. Math. 370 (2020), §1, and Broucke, arXiv
> 2409.10051, §6.2; primary text not read). The power saving `O(x^θ)` gives continuation of
> `ζ_𝒫 − ρ/(s−1)` to `\mathrm{Re}\,s > θ` and `ζ_𝒫 ≪ |t|` there, hence BE3 and BE7 with `η ≡ 1−θ`. BE5 is Landau's
> prime number theorem; the rest hold for every Beurling system; and the zeros tend to `\mathrm{Re}\,s = 1`.

**Remark 27.16, label sentence (l.11876–11878), replacement:**

> **Label of the remark: `METHOD-CONSTRAINT`, proved modulo the `CITED (secondary source)` import (H-DMV);** open
> item (41) is closed at that level.

---

## 6. Doubts for the audit

1. **[amended per R157_003, A7: resolved. Zhang, Math. Ann. 337 (2007), author's abstract via zbMATH Open
   (`zbMATH-records.txt` l.19–23), is an independent open statement of a second model of (H-DMV′). Révész's
   Theorem 5 (S4 l.375–377) and three further Révész papers are also independent of Broucke.]** **Primary unread.**
   Everything rests on five secondary texts. **Four of the five have F. Broucke as an author**
   (S1, S2, S3, S5; the Ghent school). Only Révész (S4) is independent, and S4 states the result in words only
   ("RH may still fail; nothing better than (9), (10)") without the `O(x^θ)` detail. S4's "(2)" is Axiom A, which is
   `O(x^θ)`, so it corroborates (a) indirectly. S1 l.268 thanks H. G. Diamond for comments. That is weak evidence
   that §1 of S1 was seen by an author of the primary paper.
2. **Discreteness.** BE2 needs a *discrete* system. The sources say so (S3 l.1431, S1 l.216–218), but the
   explicit formula in S3 is for the **continuous** ζ_C of the Diamond–Zhang book. The zeros of the discrete
   ζ_DMV equal those of ζ_c on σ > 1/2 only through S2 l.2714–2718 (`ζ_DMV = ζ_c e^{Z}`, `Z` analytic there). If
   the auditor does not accept that quotation, clause (c) still rests on S2 l.2691 and S3 l.111 directly, and
   Lemma 2.2's independent route rests on clause (b).
3. **Lemma 2.2 caveat.** Zeros on the curve accumulating at `σ = θ` with bounded height are not excluded by the
   compactness argument alone (§2.1). They are excluded by the explicit model and by clause (b) plus the classical
   contour argument. That argument is `CLASSICAL` in shape, but it is **sketched, not written out**, for Beurling
   systems. It needs a truncated explicit formula (quoted from Révész via S3 l.1203–1209).
4. **BE5 via Landau.** The statement "(1.1) ⟹ PNT with dlVP error" is restated in S1 l.70–76 and not re-proved
   here. It is classical (Landau's prime ideal theorem method), but I label it `CLASSICAL / CITED`, not `PROVED`.
5. **The misquotation finding.** The auditor should confirm independently that R150_001's "(DMV-a)" is a
   misquotation. Two points: no source gives `N(x) = ax + O(x e^{−c√log x})` for DMV, and S5's generalisation has
   `N = ax + O(x exp(−c log^β x))` for `β < 1`, with DMV as the case "β = 1" (S5 l.8–9, 106–108). Read literally,
   β = 1 gives `O(x^{1−c})`, i.e. a power saving, which is consistent with `O(x^θ)`.
6. **Scope unchanged.** T3 remains a statement about derivations from BE1–BE8. Nothing here says anything about
   the sign or about Weil positivity. Row D keeps no label. Filter F4 of `R157_000` ("not a Beurling-class
   argument") now rests on a cited result, not a hypothesis.

Sources consulted on the web: https://link.springer.com/article/10.1007/s00208-005-0638-2 (auth redirect, not
followed); https://deepblue.lib.umich.edu/handle/2027.42/46253 (HTTP 403). Neither was used.
