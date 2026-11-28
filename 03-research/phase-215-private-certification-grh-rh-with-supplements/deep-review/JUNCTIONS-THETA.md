> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the other results are being consolidated.

# Itemised junctions of theta, Hecke and covolume

28-11-2026. Sources: the `main.tex` of 46, 49, 50, 53, 54, the appendices of 49/50/53/54 and the reconstructions of THETA.md. 47/48 are excluded. "(a) junction" means that the mathematical instance described was checked, not only a textual similarity. "(c) by exchange" means that the deduction receives a premise whose written proof fails: **not** that the descendant result has been shown false. The reconstructions with express repairs do not certify all the literal lines of the original either.

## Entries of the table of 46:5072–5087 in this specialty

| Target 46 | Mathematical origin | Hypotheses, normalisation and range actually checked | Verdict and exchange |
|---|---|---|---|
| `au:seesaw`,4314 | 49 `ps:onestep`,3984; `ps:double`,4062; assembly 4265–4364, `pk:chi0` | The datum Ψ may depend on the twist; c_ss does not. The resulting function is not required to be non-zero. Self-dual Haar measure and class volume preserved; cancellation of the three exponents of upsilon in chi0; support and finite families treated in AS01. | (a) reconstruction of this junction in SS01/AR01–03/AS01, with the FJ erratum in the order of translation repaired according to SPANNING. Does not depend on product53. Does not give a non-vanishing that the statement does not promise. |
| `au:divis`,4368 | 49 `pa:divis`,3184–3277; `pa:eldiv`,3156; 50 `ph:thm`,396 | All primes, twist of conductor prime to ℓ, same integral lattice. Exceptional ones: first S₀=Y_Λ^m S_j+ℓ^j S_j and then S=S₀∩S^ram; it is not asserted that each Hecke operator preserves S^ram. Level N uses U_N and lattice L₀, not the exceptional cycle of 50. | (a) junction reconstructed CM01/KI01/LN01/EX01/BR01/AS01/HE01. No exchange. |
| `au:count`,3900 | 49 `pa:count`,2522, and `pa:schur`,2673 | Prior normal form; columns of height<n′; B≥1; Schur entries with standard row or nested minors, not arbitrary polynomials. The additional deduction e=0 for p=d and v(π_d)=1/2 is kept. | (a), CM01 and reading of the bound. Application to the normal norm reviewed, not only the statement copied. No exchange. |
| `au:kernel`,4497 | 49 `ps:conj`,3845; `pk:conj`,5433; `ps:monomial`,3862 and packing | Each conjugate, translated vacuum, same factorials and exact Ω; see CS detail below. The stronger formula for the phase δ_g is not certified literally; the consequences used are reconstructed separately. | (a) junction for the bound actually used, CJ01–08. Not equivalent to declaring the strong phase formula proved. No exchange. |
| `au:restrict`,4516 | 49 `ps:branching`,3803; `pk:branching`,5080–5198 | Same Schur representation and metric; hook factor removes denominators; the saturation is used after clearing the principal variable. | (a), BR01, with constant and lattice. No exchange. |
| `au:expansion`,4532 | 49 §5.1.6,3922–3967 | Gluing gives a finite sum of roots of unity times original data. Denominators N permitted by K1_N; ordinary integrality is not to be declared outside the range. Invariance is applied to the complete tensor. | (a), AS01. No exchange. |
| `au:equiv`,4584 | 49 §5.1.3,3627–3766, W1/W4/W5 | Levels and characters of Y_j, transport of the vacuum and lattices. The closure of the local properties used is in KI01/AS01; the strong phase assertion remains separate. | (a) for the transport used in SF; not a universal certification of every auxiliary formula W4. No exchange. |
| `au:shortbasis`,4427 | 49 `ps:transfer`,3589 and proof 3608–3624 | n≥1 and positive integer c₀ in the different. Lattice L unimodular, real product Tr/2; Λ=(2/c₀)L has dual⊂L. Real dimension 2fn produces exactly 6c₀(fn)². | (a), direct rereading in this consolidation; no stronger transference needed. No exchange. |
| `au:inj`,4794 | 53 `pc:tri-inj`,557; `pc:tri`,1248; `pc:first`,1270; 54 first lifts | Triangle algebra (T1–T3) correct; there is no division by the scalar before proving first that it is non-zero. The automorphic realisation requires the exchange identities. | (c) global conclusion by exchange; (a) algebraic deduction under T1–T3. The algebraic closure is not to be transferred to automorphic injectivity. |
| `au:factor`,4850 | 53 `pc:tri-gram`,582; realisation of the triangle and multiplicities 51 | Normalisation of Z_j=det(u* u), exponents d_T and twists θ^j; ramified ratios and factor Nm(Q)^{e/2} preserved. | (c) by exchange and the realisation of the triangle, although the transfer of the Gram formula is conditionally correct. See COVOLUME/MULTIPLICITIES for the other inputs. |
| `au:aux`,4878 | 53 `pc:auxcore`,1616 and development §5 | The junction requires integrality and size of the second grid, not only that lifts exist. | (c) in this individual review: the whole proof of auxcore was not redone here. Consult the closure of the main review in COVOLUME; (a) is not to be assigned for citing Theorem2.28. |
| `au:onelift`,4965 | 54 `po:ss-proof`,1134; `po:glue`,1061; `po:exchange`,995 | Determinant of the operator **compressed** to the image, not a restriction presupposing invariance. C_j independent of the twist, exponent d_j, condition ℓ∤NmQ and denominators β. The first identity depends on three exchanges. | (a) conditional algebra and agreement; (c) complete result by exchange53. Not to be confused with the rank-one norm, which does have an independent SW route. |
| `au:hecke`,4992 | 54 §2.7,1224; `po:rallis`,1395; `psu:small`,9118; `psu:arch`,9217; CL53 | Principal pairs m<z≤r; k/2 pairs squared, the other 5m ramified; corrected constant 3x³⁵ preserved. R2/R3 of regularity are kept as hypotheses. | Local deduction of heights and constants reconstructed; its use for a regular family requires in addition regularity 55. Does not remove the branch z=1 of IM. CL/norm are distinguished below; GRH is not to be asserted from this closure. |

`au:moment`, `au:mult` and `au:regular` are itemised in SPANNING, MULTIPLICITIES and JUNCTIONS-MATRIX/SELMER; this division of work does not automatically convert their status into (a).

## Exact constant, Hecke cycle and tame parts

**49→46/53/54, CS and conjugates.** In `ps:conj`/`pk:conj` one needs |t_σ|²=Ω⁻¹, with Ω=2πexp(c_CS)/rd_E, not equivalence up to an algebraic number. CJ01 compared the original page of Chowla–Selberg; CJ02–04 reconstructed the model, good reduction at 2, normalisation unit and reciprocity. The area identity is (2π²exp(c_CS)/sqrt(d))^h. On combining |σ(varpi_vac)|²=rd_E/sqrt(d), c_ψ²=2π/sqrt(d) and areaΛ_σ=|Ω_σ|²sqrt(d)/2, the result is exactly Ω⁻¹. In 53 CL and 54 normL this same normalisation is used. The Weil phases require the independent reconstruction CJ05b; the printed strong formula for δ_g is not thereby converted into a literally checked theorem.

**49→50→49.** 50 `ph:thm` controls truncated colength: col(Λ,YΛ+p^jΛ)|p^l, l≤(3c_d+θj)dimΛ. It promises neither a finite mean uniform in j nor invertibility. In the application one has even cycle N=o/o₀, P=p^{o₀}≥5, q=P^N, n=a, r=ceil(log_p m), θ=(m²f)⁻¹. The freeness of edges is checked by integral representatives and free level; it is not replaced by freeness of vertices. HE01 verifies n⁴≤q and (Nk log(q)/θ)^5 P^{3r}≤n from the data. One deduces precisely 12A_l/(mp)+j₀/(m²f) in `pa:eldiv`, and on iterating m·#Λ times the declared term j_p/m remains. `ph:root`, `ph:count`, `ph:av` were proved in the algebraic reading; they are not hidden additional axioms. The reverse arrow of appendix 50 that reproduces `pa:eldiv` and `pa:divis` is also a presentation of application results: it does not authorise using them as premises of the abstract proof. No circularity was identified in that deduction.

**54→49/46, tame.** Complete rereading of 54:7499–7615, `pfq:roots`, `pfq:mu`, `pfq:def-chars`, `pfq:tame`; target 49:8968–8997 and 49 `pz:mu` (Lemma8.6). Compatibility on μ_E is necessary and sufficient because U(1)(E⁺)∩U=μ_E and the character of an open subgroup extends. D4 makes q₁|κ(τ), and p_i≡1 mod q₂² guarantees that each residual root of unity is a q₂-th power. Thus one chooses ω_w of order exactly q₂ and μ_j⁰=μ^flat(upsilon^{-Δ}χ_M)^j with tame part ω_w^j. q₂≥m²²>8m ensures non-triviality for 1≤|n|≤8m, not only for j=1. The twists are unramified at M, which is why they do not change those tame parts. For ν^flat, χ_M^jθ cancels, giving independence of θ. **(a) this junction, range and existence; independent of the defective exchange.**

## Norm of a lift, test form and return to Selmer

| Specific junction | Mathematical check | Verdict |
|---|---|---|
| 53 `pc:SW/clean/sharp/rallis`,897–1108 →54 `pex:rallis`,Prop3.4 | SW01 collates Weil1965: ε=1/2, doubled rank M′>2n, Haar normalisation of mass 1. For the definite source/target of 54 both quotients are compact. Doubling uses the tensor with the conjugate and cancels characters; it does not use product53. | (a) specialisation of rank one and z≥2; not extrapolated to non-compact sources. |
| 54 `pex:vac`, `pex:arch`, `pex:rallis` →53 CL and 54 `psu:normL` | Split series=(1−q^{-2z})/((1−aq^{-z})(1−a^{-1}q^{-z})); inert 1. Indices of M, factors q^{2z−1} of Q and Fock factorials are preserved; non-vanishing z≥2 precedes CL. | (a), TL05/SW01. This return 53↔54 is not a circle: CL is not used to prove the non-vanishing that it receives. |
| 49 `pl:vac` Lemma6.8 →54 `ppe:transfer` | Cosets give Gaussian binomials; passing a Hecke operator through the integral inverts the double coset and the conjugate place. Constants α=q^{m_X/2},β=q^{n/2} preserved. | (a), TL05. |
| 49 normal form/count →54 `psm:katz/coupling/twelve/attained` | Twelve copies and finite sums produce a coefficient of minimal valuation; attainability is not presupposed from a lower bound alone. TL02 contains the proof. | (a) local segment reconstructed, all the primes described, including the ramified branch. |
| 54 `psm:attained` → `psu:small` → `po:small` →46 `au:hecke` | t=M^{12f}c_vac,y∏B(l_τ)² cancels factors and factorials; the minimum of an integral sum gives the necessary one-sided inequality. The corrected version is fmb/k+3x³⁵ and 46 cites it expressly. | (a) transfer of valuation and constant. The global properties of the test form use periods/tower; TL04 and the independent closure of bounded descent reported by the spanning review complete that obligation, without using the defective exchange. |
| 53 mixed laws/moments →54 `ppe:zero/bdd/rallis`,tower | Law of the Levi reconstructed on Schwartz functions, where the upsilon factors of the target cancel. The slice is NOT a bounded operator on Hilbert L²; its use requires moment norms. Range of tower for r=1,p=20: 45<2z, satisfied by flat pairs. | (a) local law and range; bounded descent closed by the spanning review: R2 with A≥2s, R3 and pcx:mean with l=A cancel ht^Aδ^A, uniformly on compacts. The false Hilbert boundedness is not to be used as a shortcut. |
| 53 `pcj` CL →54 `psu:arch` → `po:arch` | The same a_σ(z) is required for the principal and the flat pair; thus it cancels with B(z). NormL is exact, not only proportional to an L-value. The main review reconstructed CL by reciprocity 49 and non-vanishing 54. | (a) reconstructed with CL closed in the review of 53, normL and psu:I(b); 9217–9255 was reread. Does not use auxcore53. See COVOLUME and THETA TL05/SW01. |
| 54 `pex:IM`/`pex:IM1` →55 II | Finite expansion, Euler factors and quotient of L preserved; n_p may depend on the pair but not on the twist/conductor. | (a) transfer under IM; z≥2 reconstructed. (c) branch z=1 by exchange53, according to SELMER§13. |

## C275 — Completed semantic collation of the 275 reproductions

The complete bodies of the 275 environments quoteddef/quotedthm and the bodies of their source statements were extracted, not only their titles. 188 coincide after normalising spaces, labels and references; the remaining 87 diffs were inspected manually. Only internal references replaced by external citations, numbering of equations/align and spacing change. No suppression of hypotheses, widening of quantifiers or ranges, or change of constant, sign, exponent or non-vanishing condition was identified.

To prevent the normalisation from hiding an incorrect reference, papers 46, 49, 50, 51, 52, 53, 54, 55 were compiled in draft mode, in isolated evidence directories. The eight compilations ended with code 0. Their aux files resolved the references of each statement and of its reproduction: **the 275 lists of references coincide after resolving their target**, discounting the equation labels added to show the number of origin. The sub-items were also inspected: for example L3 is preserved between cite[2.2(L3)] and ref(po:facts)(L3), and K1/K2/S3 are maintained when they become part of the optional argument of cite. The compendium of reference differences contains 89 groups, all compatible.

The newcommand/renewcommand/providecommand definitions of all the macros used by these bodies, and their transitive closure, were also extracted. **Zero differences of definition between source and target.** The mathematical definitions reproduced as quoteddef were collated by the same procedure; the definitions referred to by means of references keep the same target. This controls the interpretation of the copied statement in the notation of its source; it does not replace checking that the objects of a later application satisfy those definitions.

Hence the column "Semantic copy" is **(a) in the 275 rows**. The column "Proof/application" remains separate: it may be (c), or be affected by a source proof (b), even though the copy is faithful. In particular, copying exchange53 correctly does not repair its character error. The P codes of the inventory refer only to the check of application not itemised by this review, **no longer to the collation of the reproduced statement**.

Reproducible evidence: `../evidence/collation_275_theta.json`, `collation_275_theta.tsv`, `collation_275_theta_diffs.txt`, `collation_275_theta_references.txt`, `collation_275_theta_macros.json` (empty list); scripts `compare_theta_quotes.py`, `compare_theta_macros.py`, `check_theta_refs.py`; auxiliaries `aux-collation/<paper>/main.aux`. The scripts are run from the root of the repository. The 87 diffs include some technical difference of the normaliser on removing a tag from an align line; reading the source confirms that no real mathematical separator is lost.

## How to read the exhaustive inventory of appendices that follows

**All** the quoteddef/quotedthm environments of the four appendices are enumerated. The numbered citation is linked to the label and line of its source by means of the theorem counter shared per section. The mapping is saved in `../evidence/number_map_theta.json`; the anchors ph:thm=2.2, ps:conj=5.7 and pfq:tame=6.15 were compared. This inventory also uncovers secondary imports that do not appear in the table of 46.

The evidence codes mean: **HE**=THETA HE01 and algebra of 50; **CM**=CJ01–08/CM01/KI01/LN01/BR01/AS01; **AR**=AR01–03 and SPANNING/FJ with the erratum repaired; **SW**=SW01, only the compact specialisation indicated; **EX**=dependence on exchange with failure demonstrated in product; **TAME**=the rereading above; **P**=individual pending item, to check the complete application of that label in the target. A P row does not assert that the source result is false or unknown in the whole audit: it identifies the limit of this consolidation by review, to be resolved against the ledger of the review responsible. (a) is not declared on the basis of an automatic extraction. In the secondary rows, "segment reconstructed" qualifies the source proof and its application described in the ledger; it does not certify a different additional application merely because it appears in the appendix. Such an additional application keeps (c) until the instance is identified. Those responsible can replace P with their concrete proofs: P is neither a demonstrated failure nor a permanent global pending item.

### Appendix of P49: 49 imports

| Target line | Numbered source | Source label and line | Semantic copy | Evidence | Proof/application |
|---:|---|---|---|---|---|
| 8343 | 46 13.1 | `an:def-param` (2886) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8349 | 46 13.3 | `an:def-data` (2954) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8383 | 46 13.4 | `an:lem-sizes` (2989) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8421 | 46 13.9 | `an:thm-data` (3198) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8430 | 46 14.5 | `au:free` (3598) | (a), C275 | HE | (a) freeness applied to edges in HE01 |
| 8435 | 46 14.8 | `def:au-hmain` (3804) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8456 | 46 14.9 | `au:gains` (3833) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8479 | 46 14.10 | `au:count` (3900) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8497 | 46 14.13 | `thm:srcA` (3993) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8516 | 46 14.18 | `au:errsum` (4213) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8521 | 46 14.19 | `au:seesaw` (4314) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8533 | 46 14.20 | `au:divis` (4368) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8558 | 46 14.21 | `au:shortbasis` (4427) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8564 | 46 14.22 | `au:short` (4438) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8570 | 46 14.23 | `au:kernel` (4497) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8580 | 46 14.24 | `au:restrict` (4516) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8587 | 46 14.25 | `au:expansion` (4532) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8595 | 46 14.26 | `au:size` (4544) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8604 | 46 14.27 | `au:equiv` (4584) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 8611 | 46 14.28 | `au:good` (4597) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8621 | 46 14.29 | `au:ramcount` (4619) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8625 | 46 14.32 | `au:moment` (4692) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8639 | 50 2.2 | `ph:thm` (396) | (a), C275 | HE | (a) instance HE01; truncated theorem and range, not an untruncated mean |
| 8653 | 50 2.3 | `ph:col` (429) | (a), C275 | HE | (a) instance HE01; truncated theorem and range, not an untruncated mean |
| 8663 | 50 2.10 | `ph:root` (661) | (a), C275 | HE | (a) instance HE01; truncated theorem and range, not an untruncated mean |
| 8672 | 50 2.12 | `ph:count` (687) | (a), C275 | HE | (a) instance HE01; truncated theorem and range, not an untruncated mean |
| 8677 | 50 2.13 | `ph:av` (696) | (a), C275 | HE | (a) instance HE01; truncated theorem and range, not an untruncated mean |
| 8686 | 51 2.14 | `pb:lattice` (1027) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8719 | 51 4.7 | `pm:kernel` (4346) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8733 | 51 4.8 | `pm:cusp` (4377) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8738 | 51 4.43 | `pbr:degree` (5823) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8743 | 51 5.2 | `pds:haar` (6029) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8749 | 51 5.4 | `pds:blockdet` (6056) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8754 | 51 5.5 | `pds:fischer` (6070) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8759 | 51 5.6 | `pds:decay` (6102) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8768 | 51 5.10 | `pds:kappa` (6219) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8776 | 53 2.14 | `pc:clean` (961) | (a), C275 | SW | Source: (a) compact specialisation 54 in SW01. Target instance 49: (c) except for the explicit return 54Prop3.4→53CL described above; review the local use of this label. |
| 8793 | 53 3.27 | `pcx:def-ht` (2272) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8801 | 53 3.28 | `pcx:reduce` (2320) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8809 | 53 3.30 | `pcx:superpos` (2408) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8835 | 53 4.10 | `ptr:conv` (6761) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8855 | 53 4.40 | `ptv:rev` (7908) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8871 | 53 5.37 | `pgu:line` (10296) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8890 | 53 6.9 | `pgv:alpha` (11015) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8901 | 53 6.30 | `pgx:vac` (12086) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8908 | 53 6.31 | `pgx:conv` (12106) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8919 | 53 6.32 | `pgx:dict` (12140) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 8968 | 54 6.14 | `pfq:def-chars` (7558) | (a), C275 | TAME | (a) weight, order q₂, independence of the twist in the tame parts |
| 8981 | 54 6.15 | `pfq:tame` (7571) | (a), C275 | TAME | (a) weight, order q₂, independence of the twist in the tame parts |

### Appendix of P50: 8 imports

| Target line | Numbered source | Source label and line | Semantic copy | Evidence | Proof/application |
|---:|---|---|---|---|---|
| 1545 | 49 4.2 | `pa:elim` (2538) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 1551 | 49 4.11 | `pa:partner` (2927) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 1559 | 49 4.17 | `pa:mark` (3123) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 1563 | 49 4.18 | `pa:hecke` (3149) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 1569 | 49 4.19 | `pa:eldiv` (3156) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 1576 | 49 4.21 | `pa:divis` (3184) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 1602 | 49 6.3 | `pl:wa` (5932) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 1608 | 49 6.4 | `pl:wacor` (5953) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |

### Appendix of P53: 120 imports

| Target line | Numbered source | Source label and line | Semantic copy | Evidence | Proof/application |
|---:|---|---|---|---|---|
| 16079 | 46 13.4 | `an:lem-sizes` (2989) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16117 | 46 14.1 | `def:au-height` (3394) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16124 | 46 14.3 | `def:au-lattice` (3425) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16154 | 46 14.4 | `au:twistprime` (3461) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16170 | 46 14.5 | `au:free` (3598) | (a), C275 | HE | (a) freeness applied to edges in HE01 |
| 16175 | 46 14.8 | `def:au-hmain` (3804) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16196 | 46 14.15 | `thm:srcC` (4020) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16204 | 46 14.21 | `au:shortbasis` (4427) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 16210 | 46 14.22 | `au:short` (4438) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16216 | 46 14.23 | `au:kernel` (4497) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 16226 | 46 14.27 | `au:equiv` (4584) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 16233 | 46 14.28 | `au:good` (4597) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16243 | 46 14.35 | `au:inj` (4794) | (a), C275 | EX | (c) conclusion conditional on the exchange, see individual row |
| 16248 | 46 14.36 | `au:mult` (4812) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16260 | 46 14.37 | `au:factor` (4850) | (a), C275 | EX | (c) conclusion conditional on the exchange, see individual row |
| 16275 | 46 14.38 | `au:aux` (4878) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16284 | 46 14.39 | `def:au-regular` (4895) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16305 | 46 14.40 | `au:regular` (4921) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16309 | 46 14.41 | `au:onelift` (4965) | (a), C275 | EX | (c) conclusion conditional on the exchange, see individual row |
| 16325 | 46 14.42 | `au:hecke` (4992) | (a), C275 | CM+SW | (a) deduction with a given regular family; existence of the family is another input |
| 16330 | 46 14.43 | `au:Zj` (5013) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16335 | 49 2.1 | `pwf:def` (589) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16364 | 49 2.3 | `pwf:dist` (650) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16374 | 49 2.4 | `pwf:siegel` (690) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16378 | 49 2.5 | `pwf:sum` (740) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16385 | 49 2.17 | `pwf:W5` (1101) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16398 | 49 3.2 | `par:A1` (1421) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16406 | 49 3.3 | `par:A2` (1444) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16413 | 49 3.4 | `par:D3` (1491) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16417 | 49 3.5 | `par:rigid` (1516) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16425 | 49 3.6 | `par:vac` (1564) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16440 | 49 3.7 | `par:match` (1613) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16444 | 49 3.9 | `par:def-harm` (1642) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16452 | 49 3.10 | `par:relw` (1654) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16458 | 49 3.11 | `par:exist` (1680) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16468 | 49 3.12 | `par:polar` (1711) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16476 | 49 3.13 | `par:unique` (1730) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16480 | 49 3.14 | `par:casimir` (1753) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16488 | 49 3.15 | `par:A3` (1776) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16498 | 49 3.17 | `pco:FJ` (1876) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16502 | 49 3.18 | `pco:minors` (1898) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16517 | 49 3.19 | `pco:equiv` (1938) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16531 | 49 3.20 | `pco:density` (1968) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16536 | 49 3.21 | `pco:indep` (2029) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16542 | 49 3.22 | `pco:local` (2084) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16549 | 49 3.23 | `pco:K` (2097) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16561 | 49 3.25 | `pco:decay` (2148) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16566 | 49 3.29 | `pco:V` (2337) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16573 | 49 5.2 | `ps:weil` (3428) | (a), C275 | CM | (a) properties used reconstructed; (c) strong formula δ_g if it is required literally |
| 16622 | 49 5.4 | `ps:transfer` (3589) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16628 | 49 5.5 | `ps:level` (3730) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16635 | 49 5.7 | `ps:conj` (3845) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16650 | 49 5.8 | `ps:monomial` (3862) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16656 | 49 5.14 | `pk:cauchy` (4557) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16665 | 49 5.22 | `pk:hook` (5085) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 16672 | 49 5.24 | `pk:branching` (5131) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16679 | 49 5.26 | `pk:dict` (5354) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 16691 | 49 5.27 | `pk:conj` (5433) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16697 | 49 5.30 | `pk:K12` (5606) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 16702 | 49 6.4 | `pl:wacor` (5953) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16713 | 49 7.9 | `pf:recip` (7111) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 16729 | 49 7.11 | `pf:frame` (7210) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 16733 | 49 7.13 | `pf:semi` (7284) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 16744 | 49 7.15 | `pf:std` (7362) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 16758 | 49 7.17 | `pf:flip` (7455) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16775 | 49 7.20 | `pf:classes` (7605) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16789 | 49 8.1 | `pz:def-type` (7759) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16803 | 49 8.2 | `pz:growth` (7791) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16816 | 49 8.3 | `pz:absgrowth` (7850) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16843 | 49 8.4 | `pz:types` (8021) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16865 | 49 8.5 | `pz:lastlevel` (8124) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16875 | 49 8.7 | `pz:C0` (8191) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16887 | 49 8.8 | `pz:sizes` (8235) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16899 | 51 4.6 | `pm:mult` (4331) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16912 | 51 4.7 | `pm:kernel` (4346) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16926 | 51 4.8 | `pm:cusp` (4377) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16931 | 51 4.9 | `pm:siegel` (4442) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16946 | 51 4.10 | `pm:decay` (4515) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16955 | 51 4.11 | `pm:bound` (4562) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16966 | 51 5.1 | `pds:chamber` (5983) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16977 | 51 5.2 | `pds:haar` (6029) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16983 | 51 5.4 | `pds:blockdet` (6056) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16988 | 51 5.5 | `pds:fischer` (6070) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 16993 | 51 5.6 | `pds:decay` (6102) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17002 | 51 5.7 | `pds:lip` (6138) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17006 | 51 5.9 | `pds:tail` (6185) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17015 | 51 7.10 | `pbp:residue` (7035) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17021 | 51 7.16 | `pbp:third` (7199) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17029 | 51 7.17 | `pbp:second` (7229) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17034 | 51 7.18 | `pbp:minorsize` (7254) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17039 | 51 7.19 | `pbp:minorconj` (7266) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17052 | 51 7.20 | `pbp:reduced` (7320) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17060 | 51 7.21 | `pbp:dLambda` (7349) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17064 | 51 7.22 | `pbp:gauss` (7367) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17069 | 51 7.25 | `pbp:rows` (7430) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17074 | 51 7.26 | `pbp:leftX` (7451) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17078 | 51 7.27 | `pbp:far` (7463) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17082 | 51 7.28 | `pbp:localise` (7472) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17087 | 51 7.29 | `pbp:cone` (7492) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17091 | 51 7.31 | `pbp:cover2` (7535) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17095 | 51 8.22 | `pbc:pack` (8356) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17102 | 51 8.32 | `pbc:tb-covol` (8695) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17108 | 51 8.34 | `pbc:siegel` (8727) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17116 | 54 2.1 | `po:naut` (478) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17123 | 54 2.2 | `po:facts` (544) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17136 | 54 2.15 | `po:exchange` (995) | (a), C275 | EX | (c) receives exchange53, not proved by the written route |
| 17148 | 54 2.24 | `po:arch` (1411) | (a), C275 | CM+SW | (a) arch reconstructed with CL and normL; does not depend on auxcore |
| 17153 | 54 3.2 | `pex:vac` (1639) | (a), C275 | SW | Source: (a) compact specialisation 54 in SW01. Target instance 53: (c) except for the explicit return 54Prop3.4→53CL described above; review the local use of this label. |
| 17166 | 54 3.3 | `pex:arch` (1688) | (a), C275 | SW | Source: (a) compact specialisation 54 in SW01. Target instance 53: (c) except for the explicit return 54Prop3.4→53CL described above; review the local use of this label. |
| 17173 | 54 3.4 | `pex:rallis` (1713) | (a), C275 | SW | Source: (a) compact specialisation 54 in SW01. Target instance 53: (c) except for the explicit return 54Prop3.4→53CL described above; review the local use of this label. |
| 17189 | 54 4.3 | `plf:A12` (3554) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17197 | 54 4.7 | `plf:harm` (3685) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17202 | 54 4.8 | `plf:L4` (3700) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17209 | 54 4.10 | `plf:KS` (3792) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17223 | 54 5.39 | `psr:series` (5943) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17233 | 54 5.40 | `psr:SW` (5987) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17239 | 54 5.41 | `psr:Egrowth` (6017) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17245 | 54 7.27 | `psu:flat` (8714) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 17259 | 54 7.43 | `psu:arch` (9217) | (a), C275 | CM+SW | (a) arch reconstructed with CL and normL; does not depend on auxcore |
| 17264 | 55 6.7 | `pga:L` (4010) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |

### Appendix of P54: 98 imports

| Target line | Numbered source | Source label and line | Semantic copy | Evidence | Proof/application |
|---:|---|---|---|---|---|
| 9261 | 46 13.1 | `an:def-param` (2886) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9267 | 46 13.2 | `an:def-sparse` (2930) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9278 | 46 13.3 | `an:def-data` (2954) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9312 | 46 13.4 | `an:lem-sizes` (2989) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9350 | 46 14.1 | `def:au-height` (3394) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9357 | 46 14.5 | `au:free` (3598) | (a), C275 | HE | (a) freeness applied to edges in HE01 |
| 9362 | 46 14.6 | `def:au-target` (3674) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9367 | 46 14.8 | `def:au-hmain` (3804) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9388 | 46 14.9 | `au:gains` (3833) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9411 | 46 14.10 | `au:count` (3900) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 9429 | 46 14.15 | `thm:srcC` (4020) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9437 | 46 14.21 | `au:shortbasis` (4427) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 9443 | 46 14.23 | `au:kernel` (4497) | (a), C275 | CM | See individual row above: target result, not a circular independent premise |
| 9453 | 46 14.37 | `au:factor` (4850) | (a), C275 | EX | (c) conclusion conditional on the exchange, see individual row |
| 9468 | 46 14.39 | `def:au-regular` (4895) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9489 | 46 14.41 | `au:onelift` (4965) | (a), C275 | EX | (c) conclusion conditional on the exchange, see individual row |
| 9505 | 46 14.42 | `au:hecke` (4992) | (a), C275 | CM+SW | (a) deduction with a given regular family; existence of the family is another input |
| 9510 | 46 14.43 | `au:Zj` (5013) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9515 | 49 2.14 | `pwf:W2` (1003) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9533 | 49 2.20 | `pwf:delta-red` (1206) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9540 | 49 2.21 | `pwf:eplus` (1229) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9547 | 49 3.2 | `par:A1` (1421) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9555 | 49 3.3 | `par:A2` (1444) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9562 | 49 3.5 | `par:rigid` (1516) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9570 | 49 3.6 | `par:vac` (1564) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9585 | 49 3.9 | `par:def-harm` (1642) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9593 | 49 3.10 | `par:relw` (1654) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9599 | 49 3.11 | `par:exist` (1680) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9609 | 49 3.14 | `par:casimir` (1753) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9617 | 49 3.15 | `par:A3` (1776) | (a), C275 | AR | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9627 | 49 3.17 | `pco:FJ` (1876) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9631 | 49 3.29 | `pco:V` (2337) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9638 | 49 4.5 | `pa:model` (2705) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9644 | 49 4.6 | `pa:param` (2743) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9657 | 49 4.7 | `pa:units` (2809) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9667 | 49 4.9 | `pa:onecurve` (2861) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9678 | 49 4.12 | `pa:product` (2953) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9689 | 49 4.13 | `pa:kernel` (3006) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9721 | 49 5.2 | `ps:weil` (3428) | (a), C275 | CM | (a) properties used reconstructed; (c) strong formula δ_g if it is required literally |
| 9770 | 49 5.7 | `ps:conj` (3845) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9785 | 49 5.22 | `pk:hook` (5085) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9792 | 49 5.25 | `pk:curve` (5215) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9820 | 49 5.26 | `pk:dict` (5354) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9832 | 49 5.27 | `pk:conj` (5433) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9838 | 49 5.30 | `pk:K12` (5606) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9843 | 49 6.4 | `pl:wacor` (5953) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9854 | 49 6.8 | `pl:vac` (6092) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9863 | 49 6.9 | `pl:onelift` (6123) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 9873 | 49 7.1 | `pf:chi` (6815) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9890 | 49 7.2 | `pf:two` (6848) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9897 | 49 7.3 | `pf:CS` (6911) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9903 | 49 7.4 | `pf:eps` (6941) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9910 | 49 7.5 | `pf:values` (6985) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9919 | 49 7.6 | `pf:pull` (7023) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9932 | 49 7.9 | `pf:recip` (7111) | (a), C275 | CM | (a) segment reconstructed; keeps the hypotheses of the source statement |
| 9948 | 49 7.11 | `pf:frame` (7210) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9952 | 49 7.12 | `pf:scale` (7250) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9959 | 49 7.13 | `pf:semi` (7284) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9970 | 49 7.14 | `pf:fourier` (7314) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9978 | 49 7.15 | `pf:std` (7362) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 9992 | 49 7.16 | `pf:K1` (7404) | (a), C275 | CM | (a) CM/integral consequences used; caveat on the strong phase δ_g in the main text |
| 10004 | 49 7.20 | `pf:classes` (7605) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10018 | 49 8.1 | `pz:def-type` (7759) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10032 | 49 8.2 | `pz:growth` (7791) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10045 | 49 8.4 | `pz:types` (8021) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10067 | 49 8.6 | `pz:mu` (8144) | (a), C275 | TAME | (a) compatibility of characters and range made explicit above |
| 10080 | 49 8.7 | `pz:C0` (8191) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10092 | 51 4.7 | `pm:kernel` (4346) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10106 | 51 5.6 | `pds:decay` (6102) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10115 | 51 5.9 | `pds:tail` (6185) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10124 | 51 5.10 | `pds:kappa` (6219) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10132 | 53 2.9 | `pc:level` (705) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10142 | 53 2.10 | `pc:arch` (749) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10158 | 53 2.11 | `pc:series` (780) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10177 | 53 2.13 | `pc:SW` (897) | (a), C275 | SW | (a) compact specialisation of 54; non-compact generality requires COVOLUME |
| 10215 | 53 2.14 | `pc:clean` (961) | (a), C275 | SW | (a) compact specialisation of 54; non-compact generality requires COVOLUME |
| 10232 | 53 2.15 | `pc:sharp` (1007) | (a), C275 | SW | (a) compact specialisation of 54; non-compact generality requires COVOLUME |
| 10242 | 53 2.16 | `pc:rallis` (1017) | (a), C275 | SW | (a) compact specialisation of 54; non-compact generality requires COVOLUME |
| 10255 | 53 2.18 | `pc:algpet` (1128) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10263 | 53 3.1 | `pcx:def-matched` (1757) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10273 | 53 3.2 | `pcx:X` (1767) | (a), C275 | EX | (c) import not justified by the proof of exchange; failure (b) in product3359 |
| 10297 | 53 3.4 | `pcx:cne0` (1843) | (a), C275 | EX | (c) import not justified by the proof of exchange; failure (b) in product3359 |
| 10301 | 53 3.24 | `pcx:mod` (2098) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10310 | 53 3.26 | `pcx:decay` (2257) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10323 | 53 3.27 | `pcx:def-ht` (2272) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10331 | 53 3.28 | `pcx:reduce` (2320) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10339 | 53 3.29 | `pcx:thetagrowth` (2368) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10350 | 53 3.30 | `pcx:superpos` (2408) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10376 | 53 3.32 | `pcx:mean` (2521) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10392 | 53 3.34 | `pcx:conv` (2639) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10402 | 53 3.62 | `pcu:laws` (3766) | (a), C275 | CM | (a) law on Schwartz functions with moment norms; not Hilbert boundedness |
| 10413 | 53 4.24 | `ptq:vac` (7256) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10418 | 53 6.9 | `pgv:alpha` (11015) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10429 | 53 6.30 | `pgx:vac` (12086) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10436 | 53 6.31 | `pgx:conv` (12106) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10447 | 53 6.32 | `pgx:dict` (12140) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
| 10496 | 53 9.1 | `pcj:CL` (15463) | (a), C275 | CM+SW | (a) CL reconstructed in the review of 53; same constant per rank |
| 10505 | 55 2.2 | `pg:main` (440) | (a), C275 | P | (c) here: collate hypotheses and use of this label in the target; responsibility according to the main row |
