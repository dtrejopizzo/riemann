> **V2 review in progress.** The verdict of this version refers to the earlier sources. The character objection to 53 and its global propagation are being reviewed after the correction and must not be cited as the current conclusion. See [V2 status](../review-v2/STATUS.md).

# Final report of the mathematical audit — series 43–46 and 49–56

Consolidated version of the audit, 28-11-2026. Manuscripts at commit `97fb4e78d5a858baa926829a42336ae3b914e59a`. Papers 47–48 excluded. This matrix replaces the initial verdicts that only expressed pending reading. The detailed records linked contain the reconstructions and sources.

**Current global verdict: the proof presented cannot be certified as written.** There is a proved algebraic failure in `pcu:product` of 53, used by the exchange and by its non-vanishing. It is not simply a limitation of time or of the reviewer's speciality. Nor is it a counterexample to RH or to the statement of the exchange. No repair preserving the periods and the exact factors required has been completed.

The requested categories are used: **(a)** checked within the scope indicated; **(b)** written argument incorrect, with first defective line; **(c)** not verified, with identified obligation. A proof reconstructed after correcting a false line does not receive a global "correct as written". The reconstructed mathematical result and the literal evaluation of the proof are reported separately. A numerical run is not presented as verification of a functional argument that it does not cover.

## 2. Paper 46: form and windows

| Question | Answer and scope |
|---|---|
| 2.1 Positivity of W_T in every window equivalent to RH | **(a).** Explicit formula, real/complex passage, form density and negative primitive test off the line reconstructed. "Every window" is indispensable. The auxiliary hermitian formula of 46:277 contains a misprint, detailed below, which does not change the diagonal W_T. |
| 2.2 Bounds 10⁻¹⁸ and 2.5·10⁻¹² | **(a) by independent reproduction**, keeping T fixed. The Arb640 matrices were generated, the remainder <2·10⁻⁴² was justified and the four inertias were verified. The complete even case requires certified preconditioning and Gershgorin; direct interval elimination widens. Neither the finer figure 1.5·10⁻⁴³ nor the "fails at" column is certified; they are unnecessary for these bounds. The decimals c_* and ω_- must be treated as abbreviations, not as upper bounds. |
| 2.3 Three facts on zeros and window 2.8022 | **(a) facts and inequality reconstructed with annexes.** Z1 was isolated and counted with Arb, Z2 was collated with Platt–Trudgian and Z3 with the published formulation. The public programme located passes 17 checks; the functional bridge was reconstructed and independently reviewed. **Strictly self-contained reading of 46: (c) at 1915–1930**, because only the certificate is reported there. Incorporating or citing precisely the programme and the proof of the annexes resolves that documentary omission. |

Evidence: [CHECKLIST-46-PURE](../deep-review/CHECKLIST-46-PURE.md), [NUMERICS-46](../deep-review/NUMERICS-46.md), [cross-review](../deep-review/NUMERICS-46-CROSS-REVIEW.md), [WINDOW-28022](../deep-review/WINDOW-28022.md), [functional bridge](../deep-review/WINDOW-28022-BRIDGE.md), [ANALYTIC](../deep-review/ANALYTIC.md).

The one-sided criterion, the selection of admissible data, the use of large sieve/density and the final assembly of 46 were reconstructed **conditionally on the three automorphic inputs**. That condition is not discharged by the fact of having verified the finite windows. The Gram proposition for all degrees also declares its arithmetic input: it is not an independent proof that could make up for the failure in 53.

## 3. Papers 43–45: rows A, B and C

| Paper / question | Answer and scope |
|---|---|
| 43, main theorems | **(a)** for the statements `introA/H/B/C/D`: fast crossed product, twisted Hochschild, complete symbol, signature and completions were reconstructed. The convolution of correspondences is the one defined in the text; it does not by itself constitute a geometric intersection theory over Spec Z. |
| 44, main theorems | **(a)** for `introA/B`: Haar composition of cosets, recovery of the index and contact coefficients. The hypothesis P(n)⊂S_f remains active. A distribution is not evaluated on a measure outside its domain. |
| 45, comparison and normalisation | **(a)** for `thm:comparison`, explicit formula and primitive criterion. Sign, factor 2π, inversion of the profile and polar term were preserved. The limit is stabilisation for fixed support; not a spectral limit that would authorise another positivity. |
| Novelty of each row | The explicit formula and its reading as a trace have antecedents in Connes, Meyer, Burnol and Connes–Consani. **(c)** for priority of the exact package of 43 and of the semilocal presentation of 44: an absence of equivalent antecedents was not established. 45 is compatibility of normalisations of a classical formula, not a new explicit formula. |

Evidence: [rows A/B/C](../07-rows-a-b-c.md), [Hochschild 43](../deep-review/HOCHSCHILD-43.md), [form and completion 43](../deep-review/COMPLETION-FORM-43.md). These rows are not premises of the automorphic deduction of RH in 46.

## 4. Paper 50: elementary divisors

| Question | Answer and scope |
|---|---|
| 4.1 Proof in the range ph:eq-large | **(a)** for the theorem with its definitions and its range. It controls the truncated colength of Λ/(YΛ+pʲΛ), with exponent ≤(3c_d+θj)dimΛ; it does not assert invertibility nor a finite mean of exponents without truncation. The algebraic argument and its arithmetic realisation were reconstructed. |
| 4.2 ph:root, ph:count and ph:av | **(a)** in the instances used: cycles and free arcs, weak approximation, transposition and count were collated with the data supplied by 49. The estimate is not deduced for an arbitrary Hecke operator. |
| 4.3 Later coincidence of range | **(a)** in the application of 49 `pa:partner/mark`, `pl:N/wa/wacor`: no omitted structural hypothesis was identified. |

Evidence: [THETA, HE01 and EX01](../deep-review/THETA.md), plus the algebraic development of the [initial report on 50](../02-theta-hecke-covolume.md). The scope is the divisor statistic defined by the theorem itself; it should not be replaced by a mean without its truncations or conventions.

## 5. Paper 49: Short Forms

| Question | Answer and scope |
|---|---|
| 5.1 Seesaw and constant independent of the twist | Chain of lifts, support, real rigidity, finite factors and dependence of constants **reconstructed**. **(b) local in the FJ proof**, 49:2248–2250: the order of translations in the inner product is not the one written. The direct substitution F=R(e)F and x=gh gives the correct formula without changing the constant. For that reason the whole proof is not approved literally, although the required result is recovered with the repair. |
| 5.2 Bound in each conjugate with exact CS constant | The exact Chowla–Selberg constant and its normalisation **(a)**. **(c) for the stronger description of the phase δ_g at 49:5472**: it is attributed to W4, which does not prove it there. The audit proves by Rao and algebraic unitarity the consequences actually needed, including the modulus in all the conjugates. Replacing that sentence by that proof discharges the necessary step; it is not equivalent to having proved the stronger classification of the phase. |
| 5.3 Divisibility at all primes, non-split and level | Local arguments, exceptional cases, finite Fourier, level N, branching and assembly **reconstructed in the declared range**. The same literal reservation about the phase formula remains; the necessary integrality has an independent proof in the report. No other failure of scope was found in `pa:count` nor in the four branches of `pa:divis`. |

Evidence: [THETA](../deep-review/THETA.md), CJ01–08, SS01, AR01–03, CM01, KI01, LN01, BR01, EX01 and AS01; [SPANNING](../deep-review/SPANNING.md) for FJ. These closures do not repair the exchange of 53.

## 6. Papers 51–52: Spanning

| Question | Answer and scope |
|---|---|
| 6.1 Uniform second moment and exact constant | Result **reconstructed with the local repairs** identified below. No rank-dependent factor was lost in the main term. Literally there are **(b)** steps in the auxiliary proofs, so an indiscriminate (a) for all their lines is not appropriate. |
| 6.2 Open cell, Siegel and Poisson | Measures, unipotent volume, ratio of masses, formal degree and cancellations of gauges reconstructed. **(b)** in 52 `pff:S`: the cut tending to zero does not recover the intended density. A local example and a repair with growing balls are given; the later lemma on fibres already uses that correct direction. |
| 6.3 Remaining pairs and ranges | **(a) for the reconstructed coverage**, including non-near pairs, all l≤n³ and non-concordant blocks. At 51:10498 the Jacobian exponent of `pbo:tube` must be 2ρk+2ρ², not 2ρk+ρ²; the corrected exponent still satisfies the global bound used. No omitted interval of parameters was found that survives that repair. |
| 6.4 Multiplicities and attribution | The equality was reconstructed **with the specific hypotheses of the comparison and its archimedean types**; not for any pair of groups merely isometric at finite places. At 51:4453/4511 the uniform convergence of the series over all g is false; compacta in both arguments and the uniform total bound suffice, and these are indeed justified. The classical sources on representation and mass are separated from the new comparison; a broader theorem is not attributed to a cited author. |

Evidence: [SPANNING](../deep-review/SPANNING.md), [MULTIPLICITIES](../deep-review/MULTIPLICITIES.md). The auxiliary assertion of 52 that U(<l) fixes each e_b also needs to be replaced by the unitriangular property actually used.

## 7. Papers 53–54: Covolume

| Question | Answer and scope |
|---|---|
| 7.1 Exchange and modulus of the constant | **(b), proof incorrect as written.** 53:3351–3352 omits α(det g)α(det y)β(det l); first invalid inference 3359–3360. In the period β(det u) remains inside the integral. Its modulus one does not allow it to be taken out. The final modulus of exchange is not certified by this route. |
| 7.2 Injectivity and Z(1)/Z(θ) | **(c) for an unconditional conclusion of this proof:** it receives the exchange without proof. The chain algebra was checked conditionally in [CHAIN-53](../deep-review/CHAIN-53.md). The inputs H/Hc/F were reconstructed later in CHAIN-53§6. The relation RS/T1 still receives the defective exchange; an abstract Gram identity is not confused with the complete construction of the triangle. The statement of injectivity is not declared false. |
| 7.3 Gram of one lift and L-values | **(c) for the general Gram `au:onelift`**, whose deduction uses the exchange of 53; the algebraic bookkeeping and the constants were reconstructed conditionally. **(a) for the norm of the lift of a character in the compact branch z≥2**, by SW/Rallis, which feeds CL without using the defective exchange. The branch z=1 of IM54 does use it. The closure of the rank-one norm should not be extended to every compressed determinant. |
| 7.4 Test form and valuation attained | Local construction, twelve factors and selection of a coefficient of minimal valuation **reconstructed**; ultrametric inequality is not confused with automatic equality. The archimedean comparison uses CL53, reconstructed with its constants independent of the character. The global bounded descent of 54 was reconstructed and, with CL, `normL` and `psu:I`, closes **(a) the reconstructed archimedean comparison**. `pc:auxcore` is not a direct dependency of that argument; it is audited separately for covolume. For the global applications the correct covolume input remains necessary. |

Evidence: [error 53](../deep-review/ERROR-53-CHARACTERS.md), [COVOLUME](../deep-review/COVOLUME.md), [MAP-53](../deep-review/MAP-53.md), [THETA](../deep-review/THETA.md). Other defects of 53: `pcx:decay` requires P≠∅, already present in the main application; sl(x) is not bounded from Hilbert to Hilbert and must be defined with moment norms. The repair of topology does not repair the characters.

## 8. Paper 55: twists, Selmer and Ribet

| Question | Answer and scope |
|---|---|
| 8.1 Twist for each ℓ, including small ones | Constructions and budgets per prime reconstructed. **(c) for the global conclusion without inputs**, because II receives IM54, whose branch z=1 uses the exchange of 53. In addition there are literal corrections of orders and inertia that must be incorporated; the problem is not removed by excluding small primes. |
| 8.2 Ribet modulo powers, lattices and irreducibility | **(a)** for the reconstructed lattice arguments: no missing residual irreducibility hypothesis was identified. The separation denominators are paid for; rational averages are not confused with integral divisions. The preservation of the idempotent e_c in the Higman argument requires making precise the base level and the equivariant construction indicated in the report. |
| 8.3 Local loss and odd classes | **(a)** for the local segment with the declared data, including ℓ=2 in the authorised alternatives. Cup products, detection classes, Kolyvagin, duality and passage from exponents to lengths were reconstructed. |
| 8.4 Sum over primes | **(a) as assembly of the local bounds**: weights log ℓ, denominators and terms of M preserved. It does not turn the defective input IM into a proved one. |

Evidence: [SELMER](../deep-review/SELMER.md), [HODGE](../deep-review/HODGE.md) and [junctions](../deep-review/JUNCTIONS-MATRIX.md). Literal errors: norm F_(q^n)→F_(q^d) not defined if d=lcm(d_k) does not divide n; order p_i^r−1 does not cover all the mixed degrees; a fixed polynomial does not kill all the elements of inertia. The statements actually needed use the appropriate generator and orders that divide N_ch; the repairs are developed without increasing that budget.

## 9. Paper 56: integral cup products

| Question | Answer and scope |
|---|---|
| 9.1 Exponent for every ℓ without FL restriction | **(a)** for the local chain under the printed hypotheses: T3, I2, I4, I5, SCC and scheme reconstructed. "Without Fontaine–Laffaille restriction" does not mean without any hypothesis on data, weights or windows. |
| 9.2 NM necessary and sufficient | **Sufficient: (a). Necessary: no.** The paper does not need the converse. There is an example of zero pairing even though NM fails; see HODGE and the initial report. NM should not be presented as a characterisation if only sufficiency is proved. |
| 9.3 Tame potentially crystalline | **(a)** in the express alternatives and ranges, with degrees of the polynomials, bound e₀ and descent losses checked. No unnecessary extension of coefficients nor hidden dependence on the rank of Y is introduced. |
| 9.4 Novelty and FL compatibility | Compatibility on the overlap: **(a)**. Absolute priority: **(c)**. The integral theory outside FL already exists; the specific candidate for novelty is these exponents of cup products depending on windows and thickness, not the creation of the whole integral theory. |

Evidence: [HODGE](../deep-review/HODGE.md), especially §§6–7 and primary sources Fontaine–Laffaille, Liu and Caruso–Liu.

## Junctions, connections and external review

[JUNCTIONS-MATRIX](../deep-review/JUNCTIONS-MATRIX.md) distinguishes textual copy from semantic check and documents the propagation of the failure in 53. The mutual citations 55↔56 and 53↔54 are not enough to diagnose circularity; the concrete orders of dependencies were reconstructed. The complete network is not certified by a TSV of labels: the junctions not yet individualised keep (c) until their notes are completed.

The proposed connection that deserves development is: integral theta data and control in all the conjugates → divisibility/height → lattices of sufficient rank → determinant/covolume → one-sided inequality on primes. The covolume bridge is precisely where the proved failure lies. Rows A–C provide a Weil interpretation, but do not supply the positivity used by D. The [programme of connections](../06-connections-and-programme.md) distinguishes checked mechanisms, antecedents and priority not established.

The review was organised by speciality. No actual mathematician on the list was contacted or certified these results. The [human dossier](../deep-review/EXTERNAL-REVIEW-DOSSIER.md) prepares the questions, sources and findings for an external review, without attributing endorsements or availability.

## Closure of auxcore

[AUXCORE-53-54](../deep-review/AUXCORE-53-54.md) completed the reading of line inversion, G1–G4, twists and bounds. Auxcore remains conditional on the defective exchange, not on an omission of review of those blocks. Two local repairs that preserve constants were added to the inventory: order r₀⁻¹r in the estimate of slices and cancellation of conjugate norms in the finite determinant.


## What must be corrected before requesting global certification

The priority is to repair the character identity of 53 and prove again the correct period, its non-vanishing and the modulus of the exchange constant. A constant of modulus one outside an integral does not resolve a character that varies inside it. After that, the constructions that consume exchange have to be checked again, including the branch z=1 of IM54, regularity 55 and the covolume triangles of 53.

The [inventory of corrections](../deep-review/CORRECTIONS-INVENTORY.md) provides the first invalid lines, the reconstructed local repairs and the effects on the constants. Those repairs are not yet incorporated into the manuscripts: the audit left them intact. They must also be propagated to volume 58 and its appendices.

The rest of the (c) obligations refer to concrete points: the strong formula for the phase δ_g that exceeds the reconstructed necessary consequences, finite comparisons of 46 expressly without proof, bibliographic priority and formal Lean certification not reproduced. Those limitations are not invoked to hide the confirmed (b) failure of 53.

## Dossier and evidence

- [Inventory of corrections](../deep-review/CORRECTIONS-INVENTORY.md).
- [Main junctions](../deep-review/JUNCTIONS-MATRIX.md), [275 theta copies](../deep-review/JUNCTIONS-THETA.md), [51 spanning copies](../deep-review/JUNCTIONS-SPANNING.md) and [45 Selmer/Hodge copies](../deep-review/JUNCTIONS-SELMER-HODGE.md).
- [Programme of mathematical connections](../06-connections-and-programme.md).
- [Dossier for specialists](../deep-review/EXTERNAL-REVIEW-DOSSIER.md).
- [Scope of Lean](../08-lean-records.md): a log is not equated with a repeated compilation, nor is the complete translation certified.
- [Sources examined](../evidence/sources.json), [certificates of the first window](../evidence/manifest_certificates_46.json) and scripts/outputs of both windows in evidence.

The reports of the first pass are kept as history in `history/`; their superseded pending items are not the current verdict. This report is an audit with the reconstructions and computational certificates indicated, not an endorsement by the named specialists nor a formal certificate of GRH/RH.
