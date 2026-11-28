# Verdict of the mathematical review

> **HISTORICAL RECORD OF THE FIRST PASS.** Its pending items and global verdicts do not represent the current state. The second audit resolved numerous points and proved a character failure in the proof of 53. Consult the [updated status](../deep-review/STATUS.md), [error 53](../deep-review/ERROR-53-CHARACTERS.md) and the certificates of 46 linked from README. The text below is kept for traceability; it must not be cited as the current final conclusion.


Date: 28 November 2026. Local copy of the repository at commit `97fb4e78d5a858baa926829a42336ae3b914e59a`; individual hashes in `evidence/sources.json`. Papers 47 and 48 were excluded from the reading. The work was done on the LaTeX and the records indicated, not on a remote version that could change during the review.

**The review does not certify the proof of GRH/RH of the series. Nor did it produce a confirmed counterexample to its main theorems.** There are concrete arguments that were checked and central steps that remain **(c), not verified**, with their locators and the check needed to resolve them. Most of those steps have a written proof in the manuscript: the limit is that of this audit, not a claim that the author has omitted every proof.

The verdicts follow the requested scheme:

- **(a) correct as written**, within the scope that is specified. When an implication is verified from lemmas, it is stated expressly that not all of its antecedents were certified.
- **(b) incorrect**, with a proved first failure. No defensible (b) was obtained for the main theorems. Points of precision in data or formulation are identified separately.
- **(c) not verified**, indicating the exact step and what remains to be checked. It is not equivalent to "false", nor to "correct because no error was found".

## Central results

| Block | Result of this review |
|---|---|
| 46, equivalence between positivity in all windows and RH | **(a)**. The explicit formula, form domain and construction of the negative primitive test in 45 were checked. |
| 46, bounds up to `(log 5)/2` | **(c)**. The reduction to inertia can be checked; executable certificates and matrices are missing to validate the reported numbers. |
| 46, window `2.8022` | **(c)**. Z2 and the published bound Z3 were collated; the filter and the 17 verifications are not reproduced. Z1 was not independently certified. |
| 43 | **(c)** globally. Decomposition of the group, radial symbol and stabilisation checked; complete Hochschild computation, signature and completion not certified. |
| 44 | **(a)** for the two main composition/contact theorems examined, with their range; no automatic approval of all the secondary results. |
| 45 | **(a)** for comparison with the explicit formula, radial normalisation and primitive criterion. Those results have classical antecedents. |
| 50 | **(a)** for the algebraic theorem with its hypotheses and its internal inputs; **(c)** for certifying in full its application to all the later automorphic data. |
| 49 | **(c)** for global seesaw, exact constant in all the conjugates and complete divisibility. There are partial steps that were checked. |
| 51–52 | **(c)** for complete second moment, local estimates and multiplicities. Several constants, reductions and range closures were verified. |
| 53–54 | **(c)** for complete exchange, automorphic chain, one-lift formula and minimal-valuation test. Algebra of injectivity and of determinant compression checked. |
| 55 | **(c)** for complete global existence of twists, Ribet/Selmer and odd classes. The irreducibility is indeed made explicit; duality and sum of losses were checked in the reductions indicated. |
| 56 | **(c)** for the complete integral theorems. Substitutions and NM were verified in the application; NM is not a necessary condition for every vanishing, and the text does not formulate such an equivalence. |
| Junctions | Central entries of the table of 46 collated with explicit degrees of coverage; **(c)** for certifying all the transitive imports and their applications. |
| Novelty and connections | Antecedents and a proposed quantitative connection identified; neither global priority nor the birth of a new field is certified. |

## Observations that allow the manuscript to be improved

1. **Paper 46, line 1766:** `omega_-` must be at least `2A=5.88394705…` for the specified cut. `5.8839` may be a decimal summary, but not a literal upper bound. The certificate must keep exact values or directed roundings. The bounds for the two tails are numerically consistent; this does not certify the inertia.
2. **Paper 51, line 3961:** the absorption `f·2^(3−k)≤b^-10` needs a relation between k and `log b`, in addition to the bounds listed locally. The relation comes from the admissible data; it would be advisable to include it when isolating the lemma. No contradiction was found in the current application.
3. **Paper 50:** its conclusion is one of truncated colength, with exceptional term `θj`. Presenting it as a uniform bound on all the elementary divisors would lose an essential part of the statement.
4. **Paper 56:** "for every ℓ" does not remove the conditions on weights, windows and distribution of letters. NM is a sufficient condition of the generic argument, not a necessary characterisation of vanishing. The report offers an example of positive rank that distinguishes the two concepts.

Objections that would be unfair to this version were also discarded: the residual irreducibility of 55 is indeed written; 51 does treat the extension of the comparison to inert places and closes the range of coranks; the corrected constant `3x^35` of 54 does reach 46; and the difference between the lattices of 49 and 51 does have a proposed transport.

## Reading of the proposed connection

The idea that deserves to be isolated is to convert divisibility of theta coefficients into a one-sided bound on primes, by comparing the size of many forms with a lower limit for their covolume. The second moment guarantees almost full rank; the CM periods, the twists and the Selmer groups must make the two counts compatible.

The series acknowledges that the automorphic route and its mathematics are attributed to Levent Alpoge, while the organisation into three theorems and its presentation in this series are due to the author of the manuscripts. The names of specialists supplied by the author were used to define the tasks of the specialised reviews; none of those researchers took part in or endorsed this review.

A describable line of research would be **slope methods for automorphic lattices and theta divisibility**. It is a proposal for a programme, not a declaration of a new discipline. The chapter on connections gives concrete intermediate results that could be validated and developed without depending on RH.

## Method and material scope

The work consisted of a main review and three specialised reviews: theta/Hecke/covolume; second moment/trace and connections; Selmer/integral Hodge. There were cross re-readings of the positive verdicts and of the examples. The review does not reproduce an exhaustive line-by-line refereeing of all the manuscripts nor the complete formal Lean construction.

The inventory contains 14 sources, 1910 shared labels and 3526 explicit internal references with the keys recognised by the script. Those numbers include repetitions and volume 58; **they are not a number of verified theorems**. The tables of the chapters explain exactly what was collated. The references that are not individualised remain (c).

The certificates of the finite windows were not executed because they were not located in the artefacts examined. The review's own checks of constants use multiple precision without intervals and are identified as consistency, not as certification. The large-scale Lean archive was not recompiled. The papers and the untracked file `06-alpoge-verification/README-mio.md` remained intact.

## Priorities for closing the review

The global certification requires resolving several independent pieces of work, not only correcting the two editorial details: supplying the reproducible inertias of 46; completing the audit of periods and divisibility of 49; certifying the local systems and the uniform main term of 51–52; checking exchange and test forms of 53–54; closing Selmer and odd classes of 55; and verifying the central integral lemmas of 56. The chapters indicate their precise labels. Only afterwards can a complete semantic comparison of the junctions support a verdict on the whole chain.
