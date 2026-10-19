# AUDIT  A — three arXiv papers (adversarial audit)
Sources: arxiv.org/abs pages fetched  (abstract level). Full PDFs were NOT read; every claim below is labelled from the abstract only.


## 1. arXiv 2602.20313 — W. Michalowski, "On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five" (v1 , v2 )
- **Statement (abstract):** K(u)=Φ(|u|) (dBN kernel) is not PF₅. Witness: one 5×5 Toeplitz minor det[K(u₀+(i−j)h)] at (u₀,h)=(0.01,0.05) is rigorously negative. PF₄ is left OPEN globally; locally positive at the tested configurations.
- **Method:** 80-digit outward-rounded interval arithmetic; theta-series truncation with proved tail bounds; cross-check by Leibniz expansion plus an independent interval determinant; mpmath ancillary scripts.
- **Correctness (as far as checkable, abstract level):** the claim is finite and falsifiable: one minor, one point, certified enclosure. The method is sound in kind. A small h=0.05 makes the minor nearly singular (Toeplitz minors scale like h^{20}·Wronskian), so the result rests entirely on the interval width. 80 digits is ample if the tail bounds are right. We did not re-run it. Label: **CITED (certified numerics, unrefereed)**.
- **What it implies:** Schoenberg: PF∞ ⇔ 1/𝓛K is Laguerre–Pólya type. PF₅ failure kills every route that needs Φ to be PF_k for k≥5 (PF∞/TP of the kernel, variation-diminishing of order ≥4 for convolution by Φ, Karlin-type sign-regularity of order ≥5). It does NOT touch: PF₄ or lower, Laguerre–Pólya properties of Ξ itself (Ξ in LP class is not equivalent to Φ being PF; Φ is not PF∞, so the de Bruijn/Pólya universal-factor routes run through the Fourier side and not through the kernel's TP), Turán/Jensen-polynomial routes (GORZ), or sign-regularity of Φ on restricted grids.
- **Corpus comparison:** 104_21 shows PF₂ failure for the *prime-exponent lattice law*, which is a different object, so this result is not redundant with it. 104_83 (Ξ Fourier gate) and R155_046/047 (Sturm/nodal, Karlin): this sharpens them by giving a certified ceiling of 4 on the kernel's TP order. R162_1701 §2.4 and R186_041 TP mentions: any step there that assumed TP/PF∞ of Φ is now dead. **Closes more routes: yes, at order ≥5 only.**

## 2. arXiv 2609.02882 — Y. Lamzouri, "A new proof that more than 2/3 of the zeros of ζ are simple and on the critical line" (v1 , v2 )
- **Statement:** >67.25% of zeros are simple and on the line; ≥88.76% are simple or on the line.
- **Method:** this is NOT an inertia count. The abstract says it *replaces* the matrix (finite-compression/Sylvester) framework of Alpöge–Furman 2608.13637 with "a single Hilbert-space inequality" plus Montgomery's pair-correlation theorem.
- **Mis-attribution:** the task brief and 05_LITERATURE L52 describe it as "inertia counts on finite compressions". That is wrong for this paper. Only 2608.13637 uses the compression plus Sylvester.
- **Correctness:** it is a streamlined version of a known-to-be-verified result. Label CITED (unrefereed).
- **Relation to Paper 47 Theorem P / thm:index / R186_028:** no inertia number is produced, so it neither agrees with, sharpens, nor contradicts n₋ ≤ 5/7/8 or index one. It is a proportion statement (density), and a proportion is blind to finitely or infinitely many exceptional quartets of density zero. That gives it no purchase on row D, a ∀-test positivity statement. The Hilbert-space inequality is quadratic in a mollified test, which is the same structural position as R184_009 §2(b).

## 3. arXiv 2609.15329 — A. Pearce-Crump, "Optimising Selberg's method for critical zeros"
- **Statement:** ≥7% of zeros on the line via Selberg's sign-change method (optimised Zhuravlev 1974): closed form for the reciprocal-square-root coefficients, plus PSD mollifiers.
- **Not an inertia paper either.** It is a sign-change counting method. The bound is weaker than Levinson–Conrey, Lamzouri, and Alpöge–Furman. Correctness: plausible, CITED.
- **Relation:** none to Theorem P or thm:index. The one transferable detail is a "PSD mollifier" optimisation, i.e. a positive-semidefinite constraint on mollifier coefficients. The corpus already covers that through the dual-certificate LP/SDP of Paper 47, so it adds nothing.

## Alpöge–Furman 2608.13637 (context; already audited in R184_009 §2(b))
- Re-stated without the reasoning used in R184_009: on a finite compression, Sylvester inertia counts negative directions. That count is class-blind: the falsifier M_m shifts the index by 4m and the count cannot tell the difference without prior knowledge of the index. A density statement also cannot exclude a density-zero exceptional set, and DH is the separator.
- It is consistent with Theorem P: both bound n₋ of a finite compression from above. Theorem P is archimedean-only per window (n₋(A_∞|P_T) ≤ 5/7/8). AF bounds the off-line contribution on the zero side. Neither contradicts the other, and AF does not sharpen 5/7/8 because it gives no window-indexed count.

## NEW index rows
| ID | Route | Tool family | Where | Outcome | Why |
|---|---|---|---|---|---|
| A14a-1 | Positivity via PF_k / TP of order k≥5 of the dBN kernel Φ (variation-diminishing, Karlin sign-regularity, PF∞ factorisation) | total positivity | arXiv 2602.20313; 104_83; R155_046/047 | NO-GO (falsifier, certified numerics, CITED) | An explicit 5×5 Toeplitz minor at (0.01,0.05) is certified negative |
| A14a-2 | Same at order ≤4 (PF₄, PF₃ of Φ) | total positivity | 2602.20313 | OPEN (do-not-assume) | PF₄ is not proved globally; local positivity only. Use only with a proof |
| A14a-3 | Read 2609.02882 / 2609.15329 as inertia bounds to compare with Theorem P | inertia / Sylvester | 05_LITERATURE L52 | DEAD (mis-attribution) | Neither paper computes an inertia count. Lamzouri uses a Hilbert-space inequality plus pair correlation; Pearce-Crump uses Selberg sign changes |
| A14a-4 | Positive-proportion upgrades (Hilbert-space inequality, Selberg/Zhuravlev PSD mollifiers) as a source of a row-D sign | zero-density / mollifier | 2609.02882, 2609.15329 | NO-GO | A density statement cannot exclude density-zero exceptional sets (DH separator), and it is quadratic in the test with no ∀-test positivity |
| A14a-5 | Sharpen Theorem P (n₋ ≤ 5/7/8) via Alpöge–Furman compression inertia | inertia | 2608.13637; R184_009 §2(b); Paper 47 thm:index | NO-GO (no transfer) | AF has no window-indexed count; the inertia is class-blind (falsifier M_m, κ shift by 4m) |

Correction to make in 05_LITERATURE L52: 2609.02882 and 2609.15329 are not "finite-compression inertia" papers.
