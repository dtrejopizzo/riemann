# arXiv readings for Paper 47

Reading order fixed at the outset:

1. **Eric Dubon**, [Zero-Density Concentration for Dirichlet Polynomials](https://arxiv.org/abs/2609.17875), v1. [Local PDF](2609.17875v1.pdf).
2. **Marvin B. Freedman**, [Finite-core Volterra reductions for a Weyl-positive Riemann phase kernel](https://arxiv.org/abs/2606.29555), v1. [Local PDF](2606.29555v1.pdf).

This order is kept even if further candidates appear. The selected
anticoncentration proofs of Dubon and the lifting and boundary-repair steps of
Freedman were reviewed. Scope and results are in
[R170_804](../../03-research/phase-170-global-prime-inequality/R170_804_LITERATURE_TRANSFER_REVIEW.md).
No full audit of these two manuscripts has been completed.

## Coverage and traceability

The complete math.NT listings (including cross-lists) were retrieved with the
URL format `https://arxiv.org/list/math.NT/2026-MM?skip=0&show=2000`.
An earlier attempt with `2609` did not work; `2026-09` does.

| Month | Entries retrieved |
|---|---:|
| June | 428 |
| July | 467 |
| August | 536 |
| September | 812 |
| October, available at query time | 35 |
| Total, distinct identifiers | 2278 |

`listing-2026-*.html` keeps the pages consulted; `catalog.json` contains the
identifier, title and listing month of each entry. A broad title filter produced
330 candidates (`title-shortlist.json`). 27 abstracts chosen for relevance were
read and are kept with their pages in `abstract-screening.json` and `*-abs.html`.
Introductions and statements of some candidates were also consulted. The 2278
papers were not all read, nor was every proof audited. The filter may miss
relevant titles; it does not systematically cover recent revisions of older
preprints.

The two priority PDFs were downloaded with explicit version and a checked PDF
header. `downloads.json` records URL, size and SHA-256. The PDF and extracted
text of the 27 candidates were also kept; `fulltext-retrieval.json` records that
retrieval. There are also v3 revisions of Suzuki and Groskin and v2 of Zhu and
Covei. Downloading the full text is not the same as reviewing all proofs.

## Questions for the two priority readings

**Dubon.** Extract the exact hypotheses of the isolated-primes block and of the
translation-uniform anticoncentration. Distinguish: independence of coordinates
under Haar measure, vertical averaging, and the value at the frequency selected
by first contact. Prove or refute any transfer before using it; logarithmic
averaging does not give our one-sided upper bound.

**Freedman.** Identify the certified domain and form, follow each boundary term
and the Schur range conditions. Do not import positivity of the quotient model
as positivity of W_T: first check the transport to the original operator and the
uniformity the text leaves open.

## Further candidates: preliminary assessment

| Priority after the two readings | Work | Potential use / obstacle |
|---|---|---|
| High, tools | [Fragkos–Krause–Miheisi–Sun, 2607.05560](https://arxiv.org/abs/2607.05560) | Maximal and variational operator along primes. The supremum over modulations tolerates frequency selection, but with additive phase, ℓ^p norm and weight 1/n; not our constant-one Mellin budget. |
| High, tools | [Robles, 2609.11070](https://arxiv.org/abs/2609.11070) | Effective estimates with prime-dependent prefixes. Its handling of selection is of interest; the phase is additive and the hypotheses are for multiplicative f, not directly Λ. |
| High, structural comparison | [Suzuki, 2606.09096, v3](https://arxiv.org/abs/2606.09096) | Weil form via continuous functions and non-local operators. Already in the local inventory; check what changes in v3. Its spectral limit is stated as a conjecture. |
| Medium, arithmetic | [Maynard–Pandey–Radziwiłł, 2608.14777](https://arxiv.org/abs/2608.14777) | New bound for prime sums with additive phase. Do not replace e(nα) by n^{iγ} without estimating the cost of the reduction; a power saving does not prove a sign without margin. |
| Medium, inverse structure | [Dong–Wang–Wang–Zhang, 2608.31060](https://arxiv.org/abs/2608.31060) | Large values of sums of n^{it} force nearby zeros. A different direction from the required one-sided bound; examine a possible incompatibility with minimality, do not assume it. |
| Medium, tools | [Ramaré, 2609.25879](https://arxiv.org/abs/2609.25879) and [2609.25885](https://arxiv.org/abs/2609.25885) | Parseval, regularity and weighted sieve. Smaller loss in inequalities, but control of the selected witness is missing. |
| Already incorporated | [Groskin, 2607.02828](https://arxiv.org/abs/2607.02828) and [Zhu, 2608.24827](https://arxiv.org/abs/2608.24827) | Paper 47 already cites and discusses them. Not to be counted as new. Revisions/certificates may help implementation. |
| Separate audit | [Desogus, 2609.20367](https://arxiv.org/abs/2609.20367) | The manuscript claims RH via Schur induction with inherited response and polar debit. Not validated here. Audit the conservation of budgets before the common infimum and the induction, without adopting its conclusion. |

The Carleson candidate is a math.CA cross-list in math.NT: it is kept because the
search includes cross-listed categories, not only the primary one.

## Remaining screening and kept readings

- [Turnage-Butterbaugh, 2607.04632](https://arxiv.org/abs/2607.04632): kept as background on Guth–Maynard; an exposition of an earlier advance.
- [Covei, 2606.24924](https://arxiv.org/abs/2606.24924): kept as a conditional comparison; math.GM, inherited from the earlier search, outside the math.NT catalogue.
- [Alpöge–Furman, 2608.13637](https://arxiv.org/abs/2608.13637): kept as rank–trace background; do not confuse proportions with exclusion of a negative direction.
- [Menon, 2607.15574](https://arxiv.org/abs/2607.15574): improvement for almost all intervals; does not exclude an exceptional witness.
- [Croot–Mao–Pohoata–Yip, 2607.15311](https://arxiv.org/abs/2607.15311): inverse structure of sets with residue restrictions; our witness would first have to be connected to those hypotheses.
- [Dhiman–Kadiri–Quesada-Herrera, 2609.00537](https://arxiv.org/abs/2609.00537): explicit constants and approximate functional equations; possible computational use.
- [Fiori, 2609.22624](https://arxiv.org/abs/2609.22624): explicit density near the edge; not exclusion of an off-line zero.
- [Irfan, 2609.33953](https://arxiv.org/abs/2609.33953): unitary model and variances of convolutions of Λ; distinguish the result on matrix integrals from its conjectural application to integers.
- [Tang, 2608.14852](https://arxiv.org/abs/2608.14852): twisted second-moment reciprocity; averaged in height.
- [Tardy, 2608.26814](https://arxiv.org/abs/2608.26814): correlations and dense orbits; logarithmic density, not a bound at our frequency.
- [Holland, 2608.08682](https://arxiv.org/abs/2608.08682) and [Michalowski, 2607.16795](https://arxiv.org/abs/2607.16795): regions of hyperbolicity/positivity of minors. They do not cover all the indices required.
- [Liu, 2609.33278](https://arxiv.org/abs/2609.33278): prime-detecting identities; they do not by themselves give the spectral inequality.
- [Freiberg, 2609.33692](https://arxiv.org/abs/2609.33692): corrections to independent models under uniform Hardy–Littlewood. Useful as a warning against postulating exact independence, but conditional.
- [de Faveri–Pandey, 2610.01035](https://arxiv.org/abs/2610.01035): sixth moment and large-value sets; not a theorem about the selected exceptional point.

## Admission criterion for the construction

For each tool, record: domain, weight, type of phase, quantifiers, constants,
type of averaging and any RH/GRH or correlation hypothesis. An adaptation must
keep the polar part and the infinite complement and produce a new inequality, not
only an identity. Up to this search, no law closing the global sign of Paper 47
has been identified.
