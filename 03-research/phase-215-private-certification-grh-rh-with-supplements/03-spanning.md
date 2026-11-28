# Mathematical review of papers 51 and 52

Date: 28 November 2026. Sources examined: the local `main.tex` of 51 and 52, the corresponding statements and applications of 46 and the map 57. The line numbers refer to those sources, not to the PDFs. 47 and 48 were not read.

**Update after deep audit.** The preliminary state of this report has been superseded by the reconstruction documented in [SPANNING.md](deep-review/SPANNING.md) and the independent front [MULTIPLICITIES.md](deep-review/MULTIPLICITIES.md). The local proofs of P52, the Bessel and stationary bounds, the counts G/C1/C2/S/O1, the unipotent covolume, the exact ratio of masses and the assembly of P51 were reconstructed. The written version contains repairable local failures; it is not appropriate to classify it as entirely correct as written.

## Updated verdicts by question

| Question | Verdict and scope |
|---|---|
| Uniform second moment and exact constant | **(b) for the proof as literally written**, because of the local steps below and the FJ order error P49:2250–2251. The reconstruction with repairs preserves `1+9b^{-4}`, conditional on the ambient data and the external representation inputs identified in the ledgers. No counterexample to the theorem was obtained. |
| Siegel and Poisson, leading constant | **(b)** in P52:4364–4365: the cutoff `u→0` contracts the domain instead of exhausting it. The ledger gives an explicit local model and reconstructs the repair `u→∞`, with domination and constants without losses. |
| Coverage and bounds of the pairs | **(b)** in P51:10499–10500: the homogeneous exponent is `2ρk+2ρ²`, not `2ρk+ρ²`. The repair keeps the final bound. The complete coverage of ranges and the counts were reconstructed; no omitted family of pairs appeared. |
| Equality of multiplicities | See MULTIPLICITIES: it is verified in the cuspidal scope and with the precise parameters; it contains a local correction of uniformity of a series. It is not equivalent to unconditional invariance of the spectrum for all groups with equal finite places. |

The additional size hypothesis required by C0 is available in the ambient data; it must be made explicit if the lemma is presented in isolation. Green's classification was not re-proved from scratch. The authorities named by the author did not take part in this review.

**Reading note:** the remaining text keeps the checks and questions of the first batch as a record. The sentences there indicating that R/F/S, DS, G/C1/C2/S/O1, covolume or masses were pending are replaced by their closures in SPANNING.md. They are not current pending items.

## Second moment and the constant of the leading term

P46:4692–4706, `au:moment`, asks for

\[
\sum_{s\in\overline G}\|P^*\varrho(s)P\|_{HS}^2
\le (1+9b^{-4})\frac{D_X^2}{\deg\,\operatorname{mass}_r}.
\]

P51:180–195 reproduces the same three statements; `pb:thmB`, P51:1112–1128, deduces them from `pb:est` and the comparison of multiplicities. The norm is Hilbert–Schmidt. It must not be confused with the operator norm, for which the passage to spanning would have a different content.

The need for a leading constant close to one is real. If the images of an isometric map are distributed in a subspace of dimension `d/C`, a second moment with constant `C` can still be compatible with that concentration. For that reason a bound with an arbitrary absolute constant does not replace the one written.

**Check (a), conditional reduction of L2.** In P51:3994–4026, if (R), (F), (S), the sieve theorem and the bounds (C0), (C1) are accepted, the final factors are

\[
(1+b^{-6})\left[(1+b^{-9})^2(1+b^{-6})+b^{-10}\right]
\le 1+b^{-4}.
\]

This holds for `b≥1000`; the terms other than one are of order `b^{-6}`, much smaller than `b^{-4}`. The factor `b^{-6k#A}` is recovered from the error term using `#A≤f`. There is no hidden loss of an absolute factor in this last deduction.

**Check (a), cancellations of C0.** In P51:3925–3963, `pbm:const`, taking `n=ρ+1`, `r=k+2ρ+1`, `v=(2/rd_E)^f`, the exponent identities

\[
\tfrac12-k-n-2\rho(\rho+k)
=\rho-(2\rho+1)(k+\rho+\tfrac12),
\]

\[
k+n+2\rho(\rho+k)
=1+(2\rho+1)k+\rho(2\rho+1).
\]

are verified. They are precisely the exponents of `rd_E` and `2`. The identity of compact volumes used there is obtained directly from `vol U(j)=∏_{a=1}^j 2π^a/(a−1)!`. Accepting the masses and the covolume indicated, there remains the scalar inequality

\[
\mathsf L\le(1+b^{-9})(1-N^{-k})^f.
\]

It is incorrect to describe the leading term as an exact equality without correction: the text keeps `L` and `(1−N^{-k})^{-f}`, and absorbs their deviation in the explicit margin.

**Inherited size hypothesis that should be made explicit.** The last estimate of (C0), P51:3961, uses `f·2^{3−k}≤b^{−10}`. It is not deduced from the inequalities listed in the heading of `pbm:const` alone: with `k,n,f` fixed, increasing `b` preserves their upper bounds and makes that inequality fail. In the admissible data the additional information `k≥x⁵/2` and `x≥(log b)¹⁰⁰` is indeed available, which guarantees it. A sufficient local condition is `k≥20 log b+4`, together with `f≤b/1000`. This does not refute the application to the data of the paper, but the assertion of sufficiency of an isolated list of parameters must incorporate that condition or cite explicitly the inherited bounds. The algebraic cancellations verified above do not depend on this observation; the numerical closure of C0 does.

The exact ratio of masses is in P51:1336–1357, `pb:massratio`. It is compatible with the factor `2^{1-lf}` of Gan–Hanke–Yu for the unimodular genus in the unramified case: the global factor 2 cancels in the ratio, but `2^{-f}` does not. See propositions 4.4–4.5 of [Gan, Hanke and Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf). This check does not replace the audit of each identification of lattices that allows that formula to be applied.

## Poisson, Siegel and the local inputs

**(a), one-sided Poisson lemma `pbm:poisson`, P51:3661–3684.** In the adelic group used, the periodisation of a non-negative integrable function has Fourier coefficients `c_L^{-1} F̂(η)`. If the absolute sum of those coefficients is infinite the bound is trivial. If it is finite, it represents a continuous function, equal almost everywhere to the periodisation and bounded by that sum. The lower semicontinuity on the finite set of points allows one to approach zero through points of almost-everywhere equality. This proves the inequality with the factor `1/c_L` written. It does not require pointwise equality of a classical Poisson formula for an arbitrary function.

**Checks of the Siegel normalisation.** P52:5442–5460 correctly obtains the products of additive measures of covolume one:

\[
\operatorname{covol}(\mathcal O_E\subset\mathbb C^f)
=2^{-f}|D_E|^{1/2},\qquad
\operatorname{vol}(\widehat{\mathcal O}_E)=2^f|D_E|^{-1/2}.
\]

It also uses `|D_E|=|D_{E^+}|²` when `E/E^+` is unramified at the finite places. P52:5504–5513 correctly computes the archimedean density

\[
\int_{\mathbb C^k}\delta(|x|^2-a)\,dx
=\frac{\pi^k a^{k-1}}{(k-1)!},\quad a>0.
\]

It is deduced by differentiating the volume of the ball of radius `√a`; no additional factor 2 appears.

The Siegel–Weil theorem that the manuscript invokes is expressed with measure **of mass one** on the compact unitary quotient, P52:5426–5440. It would not be correct to insert without compensation a Tamagawa measure of mass 2. The original cited is [Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf). This review did not certify the whole translation of its theorem 5 to the Weil representation and the characters of the manuscript; that point remains (c).

**Concrete limit of the review:** even accepting that translation and the two measures above, it remains to prove the passage from the representation formula to `pff:S`, with separation of fibres, weights and pairs of terms. That work is in P52:4279–4556. The computation of the density does not by itself prove the second-moment inequality. The bounds of the real and finite systems depend on the lemmas of descent, depth, frequencies and sum of layers, P52:708–871 and their later proofs; they have not been certified in full.

## The range of the count of pairs

An objection that is **not** justified by the version examined is to assert that the author only counts `l≤n³` and forgets all the other coranks. The closure of the range is written in `pbe:rank(c)`, P51:2941–2955:

\[
1\le\mathsf d,\qquad
\mathsf d^2\le(2/M)^{2if}b^{2n^3f},\qquad M/2\ge b^{18}
\ \Longrightarrow\ 18i\le n^3.
\]

Since `l≤i+1`, it follows that `l≤n³` in the range of the manuscript. This deduction is **(a) conditional** on the gain (G), on the limit of the gauge and on the integrality that gives `d≥1`.

The passage from (C1) and (C2) to (C), P51:6632–6659, is also correct as a reduction. Two terms are sent to the same pair `(t,L_{γγ′})`; the square of the bound for one term gives `b^{4000n^6(l+1)f}`, which is at most `b^{kf/4}` because `l+1≤2n³` and `k≥512000n⁹`. The weighted sum over the lattices then applies (C2).

The points still open in this review are the proof of (G) by means of cuts and indices (`pbg:main`, P51:8176), the count of frames of (C1) (`pbc:C1`, P51:8468) and the height and sum of sublattices of (C2) (`pbc:C2`, P51:8769). The coverage of non-near pairs and of non-concordant blocks uses in addition the truncation and the vanishing of amplitudes; that whole argument has not been certified. Hence it is not appropriate to assert that the complete count is correct, but nor to flag an omitted range without first refuting those reductions.

## Multiplicities and attribution

`pm:main`, P51:4299, is a comparison with:

- a comparison datum of hermitian spaces and identified levels;
- discrete series parameters with separation at least `500n³+10n⁵` between coordinates of different signs;
- even real degree `f`;
- a supercuspidal test component at a split finite place.

`pm:mult`, P51:4331–4343, is then applied to the idempotent `e_0`; an irreducible label at one place provides the cuspidal component by property (G) of Green. The equality is for the multiplicities of characters of the specified Hecke algebra, in the projected spaces, with fixed archimedean types. The sentence without these conditions, "groups isometric at all finite places have the same multiplicities", is too broad.

The comparison of stable classes `pm:classes`, P51:4729–4777, explains why the parity appears: the product of the signs that one wishes to change is `(-1)^{f(q−q′)}`. The argument uses global norms and the hermitian local-global principle; it is not obtained from a mere identification of the finite adelic points. The sum of orbital integrals in P51:4819–4836 employs in addition `pm:arch(b)`. The complete proof of the latter is referred to `pbr:main`, P51:5122 and following; it was not certified in this review. The global bounds that justify the trace of the kernel without truncation also remain pending.

The broad attribution to Labesse is reasonable as an antecedent of comparison and stability. It was **not** verified that the exact proposition of P51 is a literal citation of a theorem of his, and the manuscript should not present it so. [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf), introduction and theorems 5.4–5.5, imposes hypotheses of non-ramification at inert places for his results of multiplicity one and stability. P51 announces, by contrast, a specific proof by direct comparison and also cites the simple formula of Flicker–Kazhdan. Those distinctions must not be removed.

## Junctions checked

| Junction | Result of the comparison |
|---|---|
| P51 `pb:thmB` → P46 `au:moment` | Same three limits, same factors `5b^{-4}` and `1+9b^{-4}`, and same normalisation of `D_X²/(deg mass_r)`. Checked as a statement. |
| P52 `pfr:R` → P51 `pbm:inputs(R)` | Mass `(1+b^{-10})/deg_τ`, weights and decay coincide. The identification of the upper form with the Gram form, necessary for Siegel, appears in P52 (R-b) and in P51:3898–3900. |
| Real hypotheses of P52 → use in P51 | P52 requires `ρ≥10⁸`, in addition to other bounds (H0)–(H5). P51:4033–4038 and P52:958–964 expressly mention that condition and its satisfaction by the data. `n≥100` is not enough, but the use is not limited to that condition. The complete verification of (H1)–(H5) remains (c). |
| P52 `pff:F` → P51 `pbm:inputs(F)` | Mass `(1+b^{-6})b^{-6k#A}`, weights, exponent and denominator coincide. The system depends on the intermediate group `Z(A,d)`, not only on `T`. |
| P52 `pff:S` → P51 `pbm:inputs(S)` | The factors `r_*²`, `(1+b^{-6})a_*`, the set of distinct values of `t` and the condition of using the same finite form of (F) coincide. `T` must also contain the non-unitary places of the base; this is written in both. |
| P51 `pm:mult` → P46 `au:mult` | P46 asks in addition for the full spherical algebra, not only the split places. P51:5021–5030, `pm:rem-full`, expressly extends the identity to inert places; for that reason there is no discrepancy of scope in this version. |
| Lattice of P51 → lattice of P49/P46 | They are not identical. P51:1027–1110, `pb:lattice`, offers a transport by an adele of norm one and unitary conjugation of the Poincaré maps. The invariance of the Hilbert–Schmidt norms under that transport is indeed checked; the complete identification of the original data of P49 is left to the audit of that paper. |
| P51 → P53 | The comparison of multiplicities is a relevant input for the chain. This review did not certify all the applications in P53 nor all the reproductions in its appendices. Status (c), with no concrete discrepancy demonstrated here. |

The reciprocity of citations 51↔52 does not by itself prove circularity: the text separates the identities of coordinates and measures, used by 52, from the L2 estimate that returns to 51. To certify the absence of cycles one must follow the proofs of those base lemmas; the design of dependencies was checked, not its whole transitive expansion.

## Work needed to change the verdicts

To pass from (c) to (a) three independent and reproducible verifications are needed: one of `pbe:ds` and of the stationary period `pbp:main`; another of the local systems (R), (F), (S), especially of the separation of fibres and of all the uniform estimates; and another of the trace kernel and the orbital integrals of `pbr:main`. For the count, it is advisable to issue separate certificates of (G), (C1) and (C2) with the parameter inequalities included. The reductions already checked indicate which constants must be preserved and avoid repeating objections that the current version does treat.
