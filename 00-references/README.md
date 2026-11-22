# 00-references — external source material

This folder holds the literature the research corpus reads, cites and checks its own statements
against: PDFs and arXiv source packages of papers by other authors, plus a few bibliographic notes.
Nothing here is my own work, except the README files, the bibliography note
[`PROLATE-REFERENCES.md`](PROLATE-REFERENCES.md), the survey reports in [`survey/`](survey/) and the
search records in [`arxiv-math-nt-2026-review/`](arxiv-math-nt-2026-review/). Where a phase or paper
uses one of these sources, it cites the exact result there; the notes below only say where in the
corpus each item is mainly used (found by searching the corpus for the arXiv identifier). An empty
note means no use could be located.

Conventions. arXiv source packages are folders named `arXiv-<id>v<n>` (or single `.tex` files with no
extension); PDFs keep their downloaded names. The year is that of the arXiv version held (or of the
journal version, where stated). Text extractions (`.txt`) sit next to some PDFs for searching; the
PDF is the document of record.

## Layout

| Folder | Topic |
|---|---|
| [`papers-nuevos/`](papers-nuevos/) | Background collection, grouped by theme (folder name kept, see below) |
| &nbsp;&nbsp;[`A/`](papers-nuevos/A/) | Connes–Consani: arithmetic site, scaling site, F₁, Riemann–Roch for Spec Z̄ |
| &nbsp;&nbsp;[`deninger-programme/`](papers-nuevos/deninger-programme/) | Deninger: foliated dynamical systems for arithmetic schemes |
| &nbsp;&nbsp;[`foliated-dynamics/`](papers-nuevos/foliated-dynamics/) | Leafwise cohomology, dynamical zeta functions, spectral interpretation |
| &nbsp;&nbsp;[`deninger-connes-consani-bridge/`](papers-nuevos/deninger-connes-consani-bridge/) | Morishita: Deninger's systems vs Connes–Consani adelic spaces |
| &nbsp;&nbsp;[`arithmetic-intersection-theory/`](papers-nuevos/arithmetic-intersection-theory/) | Arithmetic Hodge index, quadratic Riemann–Roch, arithmetic surfaces |
| &nbsp;&nbsp;[`mas-papers/`](papers-nuevos/mas-papers/) | Tropical geometry and characteristic-one algebra |
| &nbsp;&nbsp;[`weil-form-and-explicit-formula/`](papers-nuevos/weil-form-and-explicit-formula/) | Weil positivity, the explicit formula, Li coefficients |
| [`prolate-and-zeta-cycles/`](prolate-and-zeta-cycles/) | Connes–Consani–Moscovici: ζ-cycles, prolate operators, semilocal operators |
| [`papers-ref-phase-60/`](papers-ref-phase-60/) | Zeta spectral triples and later Connes papers (sources of phase 60) |
| [`beurling-dmv/`](beurling-dmv/) | Beurling generalized primes (Diamond–Montgomery–Vorhauer) |
| [`qrh-preprints/`](qrh-preprints/) | Quasi-Riemann hypothesis preprints (phase 210) |
| [`arxiv-math-nt-2026-review/`](arxiv-math-nt-2026-review/) | math.NT listing search, June–October 2026 |
| [`arXiv-2511.11199v1/`](arXiv-2511.11199v1/) | Riemann zeros and dynamical quantum phase transitions (physics) |
| [`survey/`](survey/) | My literature survey for row D (not external papers) |
| [`PROLATE-REFERENCES.md`](PROLATE-REFERENCES.md) | Bibliography of the prolate / time–band-limiting literature (no PDFs) |

Folder names. `papers-nuevos` ("new papers") and its subfolders `A` and `mas-papers` ("more papers")
keep their original names because about a hundred verification scripts in phases 107, 114 and 116 read
files from those paths; renaming them would break the scripts.

---

## `papers-nuevos/A` — Connes–Consani: arithmetic site and F₁

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `arXiv-1405.4527v1/` | A. Connes, C. Consani | The Arithmetic Site (CRAS note) | 2014 / 1405.4527 | Phases 114, 159 (candidate objects for rows A and D) |
| `arXiv-1502.05580v1/` | A. Connes, C. Consani | Geometry of the Arithmetic Site | 2015 / 1502.05580 | Phases 107, 114, 116 |
| `arXiv-1507.05818v2/` | A. Connes, C. Consani | The Scaling Site (CRAS note) | 2015 / 1507.05818 | Phases 107, 114, 159 |
| `arXiv-1509.05576v1/` | A. Connes | An Essay on the Riemann Hypothesis | 2015 / 1509.05576 | Phases 39, 113 |
| `arXiv-1709.05831v1/` | S. Haran | Geometry over F₁ | 2017 / 1709.05831 | Phases 114, 116 (Haran Picard / Frobenius-type checks, many scripts) |
| `arXiv-1805.10501v1/` | A. Connes, C. Consani | The Riemann–Roch Strategy | 2018 / 1805.10501 | Phases 107, 108, 158, 159 |
| `arXiv-2205.01391v2/` | A. Connes, C. Consani | Riemann–Roch for Spec Z̄ | 2022 / 2205.01391 | Phases 40, 114, 116 |
| `arXiv-2207.10419v1/` | A. Connes, C. Consani | Hochschild Homology, Trace Map and ζ-Cycles | 2022 / 2207.10419 | Phases 45, 71 |
| `arXiv-2401.08401v1/` | A. Connes, C. Consani | Knots, Primes and the Adele Class Space | 2024 / 2401.08401 | Phases 9, 61 |
| `arXiv-2602.15941v1/` | A. Connes, C. Consani | On the Jacobian of Spec Z̄ | 2026 / 2602.15941 | Phases 106, 107, 114, 116 |
| `arXiv-2606.06604v1/` | A. Connes, C. Consani | On the Absolute Geometry of Spec Z and the Fargues–Fontaine Curve | 2026 / 2606.06604 | Phases 107, 114, 159 |
| `2307.06748v1.pdf` | A. Connes, C. Consani | On the Metaphysics of F₁ | 2023 / 2307.06748 | Phases 41, 44, 160 (survey) |

## `papers-nuevos/deninger-programme` — Deninger

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `arXiv-math0204110v1` | C. Deninger | Number Theory and Dynamical Systems on Foliated Spaces | 2002 / math/0204110 | Phases 158, 159 |
| `arXiv-math0505354v1` | C. Deninger | Arithmetic Geometry and Analysis on Foliated Spaces | 2005 / math/0505354 | Phases 158, 159 |
| `arXiv-1807.06400v4` | C. Deninger | Dynamical Systems for Arithmetic Schemes | 2018 / 1807.06400 | Phases 32, 158, 159 |
| `arXiv-2301.11643v1` | C. Deninger | Primes, Knots and Periodic Orbits | 2023 / 2301.11643 | Phases 61, 184 |
| `arXiv-2504.15767v3/` | C. Deninger | Is There a Birch and Swinnerton-Dyer Conjecture for Dedekind Zeta Functions? | 2025 / 2504.15767 | Phase 184 (literature inventory) |
| `arXiv-2508.05329v1/` | C. Deninger | Rational Witt Vectors and Associated Sheaves | 2025 / 2508.05329 | Phases 114, 136 (row A candidate, Theorem 5.1) |

## `papers-nuevos/foliated-dynamics` — foliations and dynamical zeta functions

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `arXiv-1307.3851v1` | E. Leichtnam | On the Analogy between L-Functions and Atiyah–Bott–Lefschetz Trace Formulas for Foliated Spaces | 2013 / 1307.3851 | Phases 158, 159, 160 |
| `arXiv-1712.04181v2/` | J. Kim | On the Leafwise Cohomology and Dynamical Zeta Functions for Fiber Bundles over the Circle | 2017 / 1712.04181 | Phases 42, 43, 158 |
| `arXiv-1905.12912v3` | J. A. Álvarez López, Y. A. Kordyukov, E. Leichtnam | Analysis on Riemannian Foliations of Bounded Geometry | 2019 / 1905.12912 | Phase 184 |
| `arXiv-1912.02159v1/` | J. Kim | Leafwise Cohomological Expression of Dynamical Zeta Functions on Foliated Dynamical Systems | 2019 / 1912.02159 | Phase 184 |
| `arXiv-2410.20758v1` | J. A. Álvarez López, J. Kim, M. Morishita | Regularized Determinant Formulas for the Zeta Functions of 3-Dimensional Riemannian Foliated Dynamical Systems | 2024 / 2410.20758 | Phase 184; routes index |
| `arXiv-math0412277v3` | R. Meyer | A Spectral Interpretation for the Zeros of the Riemann Zeta Function | 2004 / math/0412277 | Phases 107, 108, 158, 160 |

## `papers-nuevos/deninger-connes-consani-bridge`

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `arXiv-2508.15971v5/` | M. Morishita | On a Relation between Deninger's Foliated Dynamical Systems and Connes–Consani's Adelic Spaces | 2025 / 2508.15971 | Phases 43, 107 (read in full, Theorem 3.6), 158 |

## `papers-nuevos/arithmetic-intersection-theory`

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `arXiv-1304.3538v1` | X. Yuan, S.-W. Zhang | The Arithmetic Hodge Index Theorem for Adelic Line Bundles I: Number Fields | 2013 / 1304.3538 | Phases 114, 116 (imported index theorems) |
| `arXiv-1304.3539v2` | X. Yuan, S.-W. Zhang | The Arithmetic Hodge Index Theorem for Adelic Line Bundles II | 2013 / 1304.3539 | Phase 114 |
| `arXiv-1810.06342v2/` | A. Carney | The Arithmetic Hodge Index Theorem and Rigidity of Dynamical Systems over Function Fields | 2018 / 1810.06342 | Phases 114, 184 |
| `arXiv-2403.09266v1/` | F. Déglise, J. Fasel | Quadratic Riemann–Roch Formulas | 2024 / 2403.09266 | Phases 184, 193 |
| `arXiv-2510.08033v2/` | Z. Zhu | Riemann–Hurwitz Formula for Arithmetic Surfaces | 2025 / 2510.08033 | Phases 184, 193; row D priority plan |
| `arXiv-2512.01811v2/` | W. He | Numerical Cohomology for Arithmetic Surfaces and Applications | 2025 / 2512.01811 | Phases 114, 115, 116 (quadratic h⁰) |

## `papers-nuevos/mas-papers` — tropical geometry and characteristic one

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `arXiv-1308.3813v4/` | D. Cartwright | Tropical Complexes | 2013 / 1308.3813 | Phase 184 |
| `arXiv-1506.02023v1/` | D. Cartwright | Combinatorial Tropical Surfaces | 2015 / 1506.02023 | Phases 107, 138, 193 |
| `arXiv-1511.00650v2/` | D. Cartwright | A Specialization Inequality for Tropical Complexes | 2015 / 1511.00650 | Phase 184 |
| `arXiv-1703.02325v1/` | A. Connes, C. Consani | Homological Algebra in Characteristic One | 2017 / 1703.02325 | Phases 40, 184 |
| `arXiv-1711.07900v4/` | P. Jell, J. Rau, K. Shaw | Lefschetz (1,1)-Theorem in Tropical Geometry | 2017 / 1711.07900 | Phases 15, 184 |
| `arXiv-2007.07826v1/` | O. Amini, M. Piquerez | Hodge Theory for Tropical Varieties | 2020 / 2007.07826 | Phases 138, 148, 158 |
| `arXiv-2105.12216v2` | K. Sumi | Riemann–Roch Inequality for Smooth Tropical Toric Surfaces | 2021 / 2105.12216 | Phase 184 |
| `arXiv-2209.08536v3/` | S. Haran | Non-Additive Geometry and Frobenius Correspondences | 2022 / 2209.08536 | Phases 114, 116 |
| `arXiv-math0612267v2/` | G. Mikhalkin, I. Zharkov | Tropical Curves, their Jacobians and Theta Functions (running title "Jacobians of tropical curves") | 2006 / math/0612267 | Phases 136, 148 |
| `1001.0448v3.pdf` | S. Yoshitomi | Generators of Modules in Tropical Geometry | 2011 (v3) / 1001.0448 | Phases 40, 41, 160 |

## `papers-nuevos/weil-form-and-explicit-formula`

| File | Authors | Title | Year / arXiv or journal | Use in the corpus |
|---|---|---|---|---|
| `2006.13771v1.pdf` | A. Connes, C. Consani | Weil Positivity and Trace Formula, the Archimedean Place | 2020 / 2006.13771; Selecta Math. 27 (2021) | Used throughout (phases 4, 5, 114, 154, 160, 183, 186): Theorem 6.11, archimedean positivity |
| `2301.00421v3.pdf` | M. Suzuki | On the Hilbert Space Derived from the Weil Distribution | 2025 (v3) / 2301.00421 | Phases 4, 154 (read in full for Paper 46), 159, 160 |
| `1910.14368.pdf` | A. Connes, C. Consani | The Scaling Hamiltonian | 2019 / 1910.14368 | Phases 57, 62 |
| `2511.22755.pdf` | A. Connes, C. Consani, H. Moscovici | Zeta Spectral Triples | 2025 / 2511.22755 | PDF of the source in `papers-ref-phase-60/` |
| `math-0404394.pdf` | J. C. Lagarias | Li Coefficients for Automorphic L-Functions | 2005 (v4) / math/0404394 | Phases 104, 108 |
| `math-9810169.pdf` | J.-F. Burnol | The Explicit Formula in Simple Terms | 1998 / math/9810169 | Phases 50, 52; Paper 44 |
| `math-9902080.pdf` | J.-F. Burnol | The Explicit Formula and the Conductor Operator | 1999 / math/9902080 | Phases 47, 101, 212 |

Suzuki's *Weil's quadratic form via the screw function* (arXiv 2606.09096) is in
`arxiv-math-nt-2026-review/` (v1 and v3).

## `prolate-and-zeta-cycles` — ζ-cycles and prolate operators

| File | Authors | Title | Year / arXiv or journal | Use in the corpus |
|---|---|---|---|---|
| `arXiv-2106.01715v1/` | A. Connes, C. Consani | Spectral Triples and ζ-Cycles | 2021 / 2106.01715 | Phases 60, 61, 158 |
| `arXiv-2112.05500v1/` | A. Connes, H. Moscovici | Prolate Spheroidal Operator and Zeta | 2021 / 2112.05500 | Phases 61, 71, 160 |
| `draft4.pdf` | A. Connes, H. Moscovici | Prolate Spheroidal Operator and Zeta (PDF of a draft of 2112.05500) | 2021 | Phase 160 |
| `connes-moscovici-2022-the-uv-prolate-spectrum-matches-the-zeros-of-zeta.pdf` | A. Connes, H. Moscovici | The UV Prolate Spectrum Matches the Zeros of Zeta | PNAS 119 (2022) | Phases 160, 183 |
| `arXiv-2310.18423v2/` | A. Connes, C. Consani, H. Moscovici | Zeta Zeros and Prolate Wave Operators: Semilocal Adelic Operators | 2024 / 2310.18423 | Phases 61, 114, 183, 186 (semilocal Sonin space) |
| `2310.18423v2.pdf` | same | same (PDF of v2) | 2024 / 2310.18423 | as above |
| `Zeta-zeros-and-prolateproofs-final-2024.pdf` | same | same (journal proofs) | Ann. Funct. Anal. (2024), doi:10.1007/s43034-024-00388-z | Phases 160, 183 |
| `arXiv-2402.13082v1/` | A. Connes | Heat Expansion and Zeta | 2024 / 2402.13082 | Phases 184, 186 |

The prolate / time–band-limiting literature that these papers rest on (Slepian–Pollak–Landau,
Landau–Widom, Bonami–Karoui and others) is listed, without copies, in
[`PROLATE-REFERENCES.md`](PROLATE-REFERENCES.md); it was compiled for phase 155.

## `papers-ref-phase-60` — zeta spectral triples and later Connes papers

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `arXiv-2501.06560v1/` | A. Connes, C. Consani | Knots, Primes and Class Field Theory | 2025 / 2501.06560 | Phases 123, 186 |
| `arXiv-2511.22755v1/` | A. Connes, C. Consani, H. Moscovici | Zeta Spectral Triples | 2025 / 2511.22755 | Phases 60, 61, 101; basis of `02-foundations/engine/` |
| `arXiv-2511.23257v1/` | A. Connes, W. D. van Suijlekom | Quadratic Forms, Real Zeros and Echoes of the Spectral Action | 2025 / 2511.23257 | Phases 60, 61, 101, 160 |
| `arXiv-2602.04022v1.tex` | A. Connes | The Riemann Hypothesis: Past, Present and a Letter Through Time | 2026 / 2602.04022 | Phases 71, 115; routes index |
| `compareplots3.pdf`, `weilcomp.png` | — | Figures included by `arXiv-2602.04022v1.tex` | — | not papers |

## `beurling-dmv` — Beurling generalized primes

The primary source, Diamond–Montgomery–Vorhauer, *Beurling primes with large oscillation*,
Math. Ann. 334 (2006), is not held; these open papers restate it. Mainly used in phases 157, 162, 163.

| File | Authors | Title | Year / arXiv |
|---|---|---|---|
| `2004.11501.pdf` | F. Broucke, G. Debruyne, J. Vindas | Beurling Integers with RH and Large Oscillation | 2020 / 2004.11501 |
| `2012.06220.pdf` | F. Broucke | Note on a Conjecture of Bateman and Diamond Concerning the Abstract PNT with Malliavin-Type Remainder | 2020 / 2012.06220 |
| `2207.00665.pdf` | Sz. Gy. Révész | The Method of Pintz for the Ingham Question about the Connection of Distribution of ζ-Zeroes and Order of the Error in the PNT in the Beurling Context | 2023 (v2) / 2207.00665 |
| `2211.08716.pdf` | F. Broucke, G. Debruyne | On Zero-Density Estimates and the PNT in Short Intervals for Beurling Generalized Numbers | 2022 / 2211.08716 |
| `2409.10051.pdf` | F. Broucke | On Zero-Density Estimates for Beurling Zeta Functions | 2024 / 2409.10051 |
| `zbMATH-records.txt` | — | zbMATH Open records (Zhang, Math. Ann. 337 (2007)) | — |

Each PDF has a `.txt` extraction beside it. Details in [`beurling-dmv/README.md`](beurling-dmv/README.md).

## `qrh-preprints` — quasi-Riemann hypothesis

Unrefereed preprints on zero-free half-planes, the sources of phase 210.

| File | Authors (as on the title page) | Title | Date |
|---|---|---|---|
| `openai-qrh-seven-eighths.pdf` | OpenAI | The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8 | 30 Sept 2026 |
| `openai-qrh-eleven-twelfths.pdf` | OpenAI | The Quasi-Riemann Hypothesis (Re s > 11/12) | 5 Oct 2026 |
| `kintali-qrh-short-proof.pdf` | S. Kintali | A Short Proof of the Quasi-Riemann Hypothesis | 7 Oct 2026 |

Each PDF has a `.txt` extraction beside it. Details in [`qrh-preprints/README.md`](qrh-preprints/README.md).

## `arxiv-math-nt-2026-review` — math.NT search, June–October 2026

A search of the complete math.NT listings (2278 entries), with the listing pages (`listing-2026-*.html`),
a catalogue (`catalog.json`), a title shortlist, 27 screened abstracts (`*-abs.html`,
`abstract-screening.json`) and the PDF and text of each screened paper. Reading order, assessments
and download records are in [`arxiv-math-nt-2026-review/README.md`](arxiv-math-nt-2026-review/README.md).
Papers held:

| arXiv | Authors | Title |
|---|---|---|
| 2606.09096 (v1, v3) | M. Suzuki | Weil's Quadratic Form via the Screw Function |
| 2606.24924 (v1, v2) | D.-P. Covei | Spectral Riccati–Gamma Concavity, Symmetric Zero Cancellation, and Conditional Criteria for the Riemann Hypothesis |
| 2606.29555 | M. B. Freedman | Finite-Core Volterra Reductions for a Weyl-Positive Riemann Phase Kernel |
| 2607.02828 (v1, v3) | A. Groskin | A Finite Guinand–Weil Dictionary and Archimedean Tail Order for the Truncated Weil Quadratic Form |
| 2607.04632 | C. L. Turnage-Butterbaugh | A Decades-Long Breakthrough in Zero-Density Estimates and Primes in Short Intervals |
| 2607.05560 | A. Fragkos, B. Krause, N. Miheisi, Y.-C. Sun | A Variation Norm Carleson Theorem along the Primes |
| 2607.15311 | E. Croot, J. Mao, C. Pohoata, C. H. Yip | A Sharp Inverse Theorem for the Quadratic Large Sieve |
| 2607.15574 | S. Menon | Improved Bounds for Multiplicative Functions in Almost All Short Intervals |
| 2607.16795 | W. Michalowski | An Explicit Uniform Cubic Wedge for Consecutive Toeplitz Minors of the Riemann ξ Coefficients |
| 2608.08682 | J. Holland | A New Hyperbolicity Wedge and a Joint Semicircle Limit for Jensen Polynomials of Riemann's ξ-Function |
| 2608.13637 | L. Alpöge, R. Furman | More than Two Thirds of the Zeta Zeros Are Simple and on the Critical Line |
| 2608.14777 | J. Maynard, M. Pandey, M. Radziwiłł | Exponential Sums over Primes |
| 2608.14852 | Z. S. Tang | Reciprocity for the Short Twisted Second Moment of the Riemann Zeta Function |
| 2608.24827 (v1, v2) | X. Zhu | Weil Positivity in Compact Windows: A Finite Reduction, Certified Two-Sided Bounds, and a Landau–Widom Decay Law |
| 2608.26814 | N. Tardy | Two-Point Correlations of Multiplicative Functions with Dense Orbits |
| 2608.31060 | Z. Dong, R. Wang, W. Wang, H. Zhang | Large Zeta Sums and Zeros of the Riemann Zeta Function |
| 2609.00537 | N. Dhiman, H. Kadiri, E. Quesada-Herrera | Explicit Exponential Sum Estimates and Approximate Functional Equations for the Zeta Function |
| 2609.11070 | N. Robles | Effective Estimates for Exponential Sums with Multiplicative Coefficients |
| 2609.17875 | E. Dubon | Zero-Density Concentration for Dirichlet Polynomials |
| 2609.20367 | M. Desogus | The Three Gates: A Rooted-Operator Approach to Weil Positivity |
| 2609.22624 | A. Fiori | Zero Density Theorems for Short Intervals |
| 2609.25879 | O. Ramaré | The Large Sieve through Parseval, Large Sifted Sets Are Regular |
| 2609.25885 | O. Ramaré | The Weighted Large Sieve through Parseval |
| 2609.33278 | Z. Liu | Prime-Detecting Identities from Dirichlet Inversion |
| 2609.33692 | T. Freiberg | Biases in the Distribution of Primes in Short Intervals |
| 2609.33953 | A. Irfan | Sums of von Mangoldt Convolutions via Trace-Sum Averages over U(N) |
| 2610.01035 | A. de Faveri, M. Pandey | The Sixth Moment of the Riemann Zeta Function |

## `arXiv-2511.11199v1` — physics background

| File | Authors | Title | Year / arXiv | Use in the corpus |
|---|---|---|---|---|
| `RH.tex` (+ figures, `RH.bib`) and the original `arXiv-2511.11199v1.tar.gz` | S. Wei, Y. Zhai, Q. Lu, W. Yang, P. Gao, C. Wei, J. Song, F. Nori, T. Xin, G. Long | The Riemann Hypothesis Emerges in Dynamical Quantum Phase Transitions | 2025 / 2511.11199 | Background only (phases 160, 184) |

## `survey` — literature survey for row D

My own survey of the literature relevant to row D: a brief, five domain reports (S1–S5) and a synthesis.
See [`survey/README.md`](survey/README.md).

## `PROLATE-REFERENCES.md`

A bibliography (no copies held) of the prolate spheroidal / time–band-limiting literature used for
eigenvalue bounds in phase 155. It complements [`prolate-and-zeta-cycles/`](prolate-and-zeta-cycles/).

---

Reference material only. See `03-research/` for what the work did with any of it, and
`05-meta-and-planning/ROUTES-MASTER-INDEX.md` for the conclusions drawn.
