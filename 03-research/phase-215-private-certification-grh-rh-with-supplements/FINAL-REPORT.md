# Private mathematical verdict — second review

28 November 2026. Exact sources: [manifest V2](review-v2/sources-v2.json), fourteen files whose hashes were checked at closure. The manuscripts were not modified nor was any commit made. Papers 47–48 excluded.

## Result

**Favourable verdict on the mathematical chain reconstructed with the explicit supplement of this review. Verdict (b) on the version currently written, which still contains incorrect steps.** These are two distinct objects: the current PDFs, and the identified sources plus the substitutions and proofs of the supplement.

The review reconstructed the necessary inputs and the deduction SF + Sp + Cv → main inequality → GRH for Dirichlet → RH. For that reconstruction the exact corrections of [MATHEMATICAL-SUPPLEMENT](review-v2/MATHEMATICAL-SUPPLEMENT.md) are required, with their linked proofs. The former supposed residual character of 53 is not kept as a pending premise. Nor is the mere absence of a counterexample presented as verification: the notes detail the computations, hypotheses, ranges and dependencies that justify each closure.

This is the scope of the private mathematical certification of this review: **the reconstructed deduction, with the supplement, has a positive verdict; the manuscripts without incorporating it do not receive “correct as written”.** It is not a formal Lean certificate nor an endorsement by the mathematicians mentioned by the author. None of them was contacted. The individualised classical theorems are accepted with their hypotheses, as in an ordinary mathematical review; it is not claimed that all the literature used has been re-proved.

## Necessary corrections that remain outside the manuscripts

| Place | First incompatibility or insufficient step | Repair and scope verified |
|---|---|---|
| 54:2695,7584; 58:51272,56151 | νflat=ν″υ^m/χ′ contradicts 54:2730 and the weight in 6448 | Define νflat=ν″/χ′; maintain the uses νflatυ^m. The three exchanges, H5, spanning and the same H_j are recovered. |
| 55:6104; 58:67922 | J_O∩J1=J1 does not have the quotient H that is used afterwards | Define J_O^(1) by means of congruence at the auxiliary places inside J_O. The Higman average keeps integrality, e_c and c0∣N_ch. |
| 49, phase δ_g | The strong classification attributed to W4 is not proved there | Replace it by the two sufficient consequences, proved arithmetically: modulus at all the conjugates and unit above ℓ when g is integral. |
| 53, pcu:coeff | The printed formula of κ0 keeps only the infinite modulus | Use (ε_T/ε_U)|d0|_(A_E)^j. The additional finite factor is fixed and is absorbed in K; it does not change the dependence on the twist. |
| 54, ppe:harm/bottom | Generation of harmonics incomplete in one sentence; inverse of A incorrect | Add generation by the joint action; correct A and respect conjugate-linearity. Vanishing and constants kept. |
| 54, explicit/carriernz/psv:c | Some justifications use too weak a topology or an unnecessary identification | Use density and continuity in Schwartz/moments, and Parseval for non-vanishing. Supplementary proofs without loss. |
| 56, appendix BL/G4 | Citations not synchronised with 55 | Copy the domain e_cF(O) and the formulation by the tame generator; synchronise 58 as well where appropriate. |

The new defect of 54 has a real effect on the literal proof. With the printed definition, H5 receives det(h)^−m and the integrand of F⁰(1) has central character z^−3m² at an infinite place. Since m>0, Haar invariance and absolute convergence force F⁰(1)=0, while the proof needs it to be non-zero. The repair indicated eliminates exactly that character; no attempt is made to absorb it in a constant.

The [inventory V2](review-v2/INVENTORY-V2.md) and the supplement contain the locations and the proofs. The earlier corrections that the author had already incorporated were checked in [REVIEW-ANALYSIS-SPANNING-V2](deep-review/REVIEW-ANALYSIS-SPANNING-V2.md) and [REVIEW-55-56-V2](deep-review/REVIEW-55-56-V2.md).

## Correction of the earlier verdict on 53

The earlier objection on a residual character β(det u) in the application of pcu:period **is withdrawn**. The application uses the same target character γ in the blocks. The new product identity distributes the source and keeps a single target; the period is the one corresponding to θ_(γ,γ).

The finite accounting was recomputed: the Levi ratio contributes ν_bc(det q), the finite data ν_bc(det x_f)^−1, the period ν_bc(ζ_B)^−1 and the change of target ν(det y)^−2. With B=y⁻¹Y and q=s0x_UY, their product is ν_bc(det(s0x_U)), independent of the integrated variable. The clarification of the fixed modulus κ0 is distinct from that refuted objection.

Hence the old classifications (c) of injectivity, chain factor, auxcore, IM of 54 and regularity of 55 whose sole reason was that residual character **are not the current verdict**. The applications were reconstructed with the corrected formula; they were not approved merely by deleting the objection. Evidence: [characters 53](deep-review/REVIEW-53-CHARACTERS-V2.md), [chain 53](deep-review/CHAIN-53.md), [auxcore](deep-review/AUXCORE-53-54.md).

## Closure of the inputs and their junctions

In this table, “reconstructed” includes the supplement expressly indicated; it does not mean literal (a) for each line of the manuscript.

| Necessary input | Positive check and evidence |
|---|---|
| Data, one-sided criterion and selection of twists of 46 | Existence and sizes, large sieve, density, transform and Landau reconstructed in [ANALYTIC](deep-review/ANALYTIC.md). C0 of 49 is fixed before the thresholds. |
| SF 49/50 | Seesaw, exact Chowla–Selberg, divisibility in all the branches and range of the truncated Hecke: [THETA](deep-review/THETA.md). FJ corrected by the author; sufficient phase: [PHASE49](deep-review/REVIEW-PHASE49-V2.md). |
| Common normalisations of 49 | Levi, unipotent, Weyl, factor 2, Gaussian index, doubling and change of character reconstructed in [SPLITTING](review-v2/REVIEW-SPLITTING-V2.md). No arbitrary phase accepted by unitarity alone remains. |
| Sp 51/52 | Second moment, leading constant, coverage of pairs, Siegel/Poisson and range: [SPANNING](deep-review/SPANNING.md), [corrections V2](deep-review/REVIEW-ANALYSIS-SPANNING-V2.md). Multiplicities only under the specific hypotheses used. |
| Exchange, chain and auxiliaries of 53 | Finite characters and modulus, injectivity, H/Hc/F, determinant and auxiliaries reconstructed; earlier references and [COVOLUME](deep-review/COVOLUME.md). |
| General Gram of 54 | The general rank was reviewed, not extrapolated from rank one: [periods](deep-review/REVIEW-54-GENERAL-PERIODS-V2.md), [three exchanges](deep-review/REVIEW-54-THREE-EXCHANGES-V2.md), [spanning](deep-review/REVIEW-54-GENERAL-SPAN-V2.md). The compressed determinant and the power d_j of the L-product are kept. |
| Attained valuation of 54 and CL of 53 | Selection of minimal coefficient, archimedean comparison and compact norm z≥2 reconstructed; the compact norm feeds CL before the exchange and avoids circularity. [THETA](deep-review/THETA.md), [AUXCORE](deep-review/AUXCORE-53-54.md). |
| Regularity of 55 and local loss of 56 | Integral average, Ribet, cup products, all the primes including the small ones, quantifiers of the embeddings and sum of budgets: [review 55/56](deep-review/REVIEW-55-56-V2.md), [SELMER](deep-review/SELMER.md), [HODGE](deep-review/HODGE.md). NM is used as a sufficient condition, not a necessary one. |
| Heights and Cv → inequality → GRH/RH | Product with prime-dependent twist, conjugation cσc, costs and signs: [assembly](review-v2/GLOBAL-ASSEMBLY.md), with [cross-review](review-v2/GLOBAL-CROSS-REVIEW.md). |

The junctions were reviewed by their content and their applications: same range, same hypotheses, independence of the twist, normalisation of constants and quantifiers. The old counts of textual copies are not used as a substitute. The two outdated citations of 56 remain necessary documentary corrections, expressly listed.

## Scope not to be confused with the conclusion

The strong classification of δ_g remains (c); the two sufficient consequences have a supplementary proof. The finite comparisons of 46 that the text itself declares without proof and the documentary link to the window certificates are not incorporated as premises of this deduction. The values of T were not recomputed in this pass. The earlier numerical reproductions remain in the dossier and are not a basis for the global conclusion.

Rows 43–45 remain separate: their results and explicit normalisation were reviewed in [rows A/B/C](07-rows-a-b-c.md), [Hochschild](deep-review/HOCHSCHILD-43.md) and [completion](deep-review/COMPLETION-FORM-43.md). They do not supply a missing premise to Row D. Absolute bibliographic priority is not certified, neither for those rows nor for the new integral exponents of 56.

The mathematical connection identified by the audit is the chain: integral control at all the conjugates → divisibility and heights → spanning of sufficient rank → determinants/covolumes → a one-sided bound over primes. The candidate contribution to novelty lies in those specific quantitative bridges, not in having created the theta or integral Hodge theories from scratch. See the [programme of connections](06-connections-and-programme.md), keeping its separation between mathematical mechanism and priority yet to be established.

## Use of the verdict

The object reviewed favourably is defined by the V2 hashes plus the supplement and the linked proofs. To assert the same of the PDFs one must incorporate those substitutions and check the propagation of the resulting text. No source was edited during this review. The earlier reports are kept in history and the old notes are read with the V2 rectifications; their superseded objections must not be cited as current.
