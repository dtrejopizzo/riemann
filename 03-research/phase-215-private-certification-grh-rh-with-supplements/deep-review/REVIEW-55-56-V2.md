# Review of the corrected P55/P56 — V2

28-11-2026. The current `git diff` was read and the corrections were reconstructed in their contexts, without modifying manuscripts. The verdict distinguishes the corrected computation, its literal wording and its propagation. It is not presupposed that the simultaneous review of the exchange of 53 is already closed.

## Result

- **(a)** The repairs M3, tame generator G4 and restriction of BL(c) to γ_w in 55 correct the defects identified, without increasing constants.
- **(a), with the definition of level indicated below:** the new average of conjugates over D preserves the type e_c and satisfies exactly the Higman identity with c₀=#D|N. Its use in proof III does not incur a new loss.
- **(b) literal, repairable by a definition:** 55:6104 still incorrectly defines J_O^(1)=J_O∩J₁. Since J₁⊂J₀⊂J_O, that is J₁, not the level J_O made principal only at the auxiliary places. This erratum reappears at 58:67922 and contradicts the identification with H-invariants used by the new average.
- **(b) fidelity of two citations in 56:** BL keeps the old domain F(O) instead of e_cF(O); G4 keeps the false explanation by means of the norm F_(q^n)→F_(q^d). The corresponding corrections are indeed in 55 and 58. The other local modifications of 56 are only these citations: its proof of exponents of cup products was not changed.

## 1. Reconstruction of the average, without additional denominators

Sources 55:6045–6141; definition of the type 55:7535–7553. One has J₀ free, J₁ normal in J₀ and Γ=J₀/J₁, a product of GL groups at the auxiliary places. In the model of functions on representatives×Γ, let S be a section of the cosets kΓ′. Multiplication Ψ₁ by 1_S is integral and

\[
\sum_{h\in\Gamma'}h^{-1}\Psi_1h\,f(g,k)
=\#(S\cap k\Gamma')f(g,k)=f(g,k).
\]

This identity does not require division by |Γ′| and holds for every subgroup, including K₁ and Γ used later.

At the chosen places, D=∏GL_n(F_w) acts on the space of level J₁: J₁ is principal there and the representatives of D normalise both J₁ and its character, which is trivial on those factors. The choice of lift does not change the operator. The representatives are integral matrices with integral inverse, also in the factors above ℓ when there are any; hence R(d) and R(d)⁻¹ preserve the integrality gauges. Their supports are disjoint from those of Γ, so that the two actions commute.

Defining

\[
\Psi=\sum_{d\in D}R(d)^{-1}\Psi_1R(d)
\]

one obtains an integral operator. Conjugating by R(a) permutes the summands through d↦da, so that Ψ commutes with D. In particular it commutes with H=J_O/J₀ and with the operators ϱ(u)=ψ(det u)R(diag(u,1)) that define G_c; by linearity it commutes with e_c. **e_c is not applied again to Ψf**: its denominator does not appear. Finally,

\[
\sum_{h\in\Gamma'}h^{-1}\Psi h
=\sum_{d\in D}R(d)^{-1}1R(d)=|D|\,1.
\]

If y is Γ-invariant and e_cy=y, then |D|y=Σ_h h⁻¹Ψy=Σ_h hΨy. Moreover Ψy is still of type e_c. The identity of operators has been checked, not merely an equality in a rational quotient.

The size is permitted: n=r′+t′≤r+t=6r≤5r²=rt for r≥2. The block-diagonal inclusion GL_n(F_w)→GL_rt(F_w) implies divisibility of orders factor by factor; hence c₀=#D divides N_ch=∏#GL_rt(F_w). The stabilisers inject into H⊂D. That c₀ increases from #H to #D does not alter any bound written in terms of N.

### Definition of level that still fails literally

55:6061–6065 defines J₁ as the subgroup of J₀ obtained by imposing principal level at the w_j. At 55:6104 one writes J_O^(1)=J_O∩J₁. By inclusion this gives J_O^(1)=J₁. However 55:6130 identifies A(J_O^(1),χ_O) with A(J₁,χ)^H. For non-trivial H, the second condition adds invariance that the level J₁ does not impose: the equality does not follow and is not the correct identification of levels.

The definition needed is

\[
J_O^{(1)}=J_O\cap\{k:k_{w_j}\equiv1\pmod{w_j}\text{ for all }j\}.
\]

Thus J₁⊲J_O^(1), J_O^(1)/J₁=H, and A(J_O^(1),χ_O)=A(J₁,χ)^H exactly. This correction of the definition makes the preceding invariance steps valid without changing the group D, c₀, integrality or rank. The literal failure begins at 6104; the deduction that uses it is at 6130. It is not a counterexample to the possibility of constructing Ψ.

## 2. Later uses of the operator and absence of a new loss

The uses listed by `rg` at 55:2959–2974, 3017–3035, 3103–3128 and 7465–7511 were inspected.

1. The insertion for Γ′=K₁ uses only integrality and Σκ κ⁻¹Ψκ=c₀. The sum over D provides exactly that identity.
2. The induction of norms does not suppose that Ψ commutes with the Hecke algebra: 55:3017–3019 says so expressly. That it now commutes with e_c does not change that order of multiplication.
3. The space Y of 55:3103 is expressly restricted to e_c; Hecke, the groups at w_j and Ψ preserve it. Hence the new systems at principal level keep the type of the labels and BL(c) applies to them, once the definition of J_O^(1) is corrected.
4. For u=Ψ(d₁l), the norm is c₀d₁l; the computation 55:3029–3035 gives integrality of d₁c₀A∂_Jy. In the application d₁=N and c₀|N, so that Nc₀A∂_Jy integral implies N²A∂_Jy integral on multiplying by N/c₀. The divisibility condition with n₀c₀² is dominated by the one already chosen with n₀N². No factor N³ appears from a new projection.
5. The pairing is computed directly at level J_O and keeps its factor N; the change in the construction of Ψ does not renormalise that pairing.

These steps are independent of the exchange identity of 53. The existence and the properties of the lifts that enter the global data remain distinct earlier obligations.

## 3. M3, G4 and BL(c)

**M3, 55:883–890: (a).** If a root belongs to an irreducible factor of degree d≤r, its order divides p_i^d−1. This factor divides |GL_rt(F_w)| because d≤rt. If v_ℓ(ω−1)>0, ω is a root of order ℓ^a, and v_ℓ(ω−1)=1/(ℓ^(a−1)(ℓ−1))≤1. Each root contributes at most 1, so that v_ℓ det(R(γ)−1)≤r, and when there is a contribution ℓ|N_ch, hence r≤rv_ℓ(N_ch). The case ℓ=2 is also included. d|r is not needed. The absence of the root 1 remains the good-label condition used before, not a circular conclusion of regularity.

**G4, 55:3943–3950: (a) for the compatibility repair.** Tame inertia is pro-cyclic; the image of a topological generator in F_(q^d)^× is a generator. For each d_k|d=lcm(d_k), θ_(d_k) is the norm of θ_d. This allows the depth-zero description to be applied simultaneously to all the factors without the non-existent assumption d|n. The choice is compatible with the fixed generators of the conventions; it is not being asserted that all the elements of inertia have the same spectrum. The mixed rank 2+3, n=5, d=6, is included in this way.

**BL(c), 55:2260–2274 and 6569–6576: (a) for the corrected restriction.** The identity with the fixed polynomial o_w is now asserted at γ_w. For other s, it is only asserted that the eigenvalues are the corresponding powers and 1. In the application of condition (6), 55:2854–2864, one chooses precisely tame generators δ_v at the chosen places; one can and must take δ_v=γ_w. The fixed polynomial is not needed for all s. The later phrase "ρ_x|I_w ... eigenvalues" must be understood at those generators already fixed: the effective argument is written on δ_v. P56:7937–7988 uses polynomials q_s depending on s and does not require recovering the false assertion for all s.

The new definition base level=e_cF(O) appears in the statement of BL, the definition of the space and the application to Y. It is the restriction needed to preserve the label conditions in systems at auxiliary level.

## 4. Propagation to 58 and citations in 56

The comparison of diffs and searches for the modified fragments gives:

| Point |55|58|56 appendix|
|---|---|---|---|
|M3 irreducible degrees|883–890 corrected|22853 ff. corrected|No copy of that proof|
|BL domain e_cF(O)|2262–2264 corrected|24230–24232 corrected|8194–8195 keeps F(O) and the old (a): **out of sync**|
|BL polynomial only at γ_w|2270 and 6575 corrected|Same correction propagated|8202 corrected|
|G4 topological generator and explanation|3946–3950 corrected|25911–25915 corrected|8329 changes the generator, but 8331–8333 keeps the invalid norm: **out of sync**|
|Average over D|6117–6141 incorporated|67935 ff. incorporated|No copy of `pri:forms`|
|Erroneous definition J_O∩J₁|6104 persists|67922 persists|No copy of that proof|

Hence the fidelity verdict "45 copies (a)" of the V1 report **does not transfer to V2**: with the change of the source, two copies no longer coincide at mathematically relevant points. In particular the copy of BL in 56 has a wider domain than the new theorem of 55. This does not by itself invalidate the local computations of cup products; it does prevent certifying the fidelity of that junction as it is written.

## 5. Remaining obligations for the global verdict

Within the change reviewed here, what remains is to correct the definition of the auxiliary level and to synchronise the two citations in 56. The integral average that preserves e_c and its constants are already reconstructed; no open obligation of Higman algebra remains once that correction of the definition is made.

This document does not revalidate all the earlier automorphic material of 55 nor the whole local theory of 56: their verifications are in SELMER/HODGE and only the points indicated change. The regularity deduction of 55 continues to depend on IM of 54, including its case z=1 and, through that branch, on the exchange of 53. The `git diff` of 53 is being reviewed separately: this report does not declare that the new correction of 53 fails, nor that it succeeds. The local closures of M3/G4, norms/Higman and cup products are not enough to deduce GRH by themselves.

## 6. Explicit supplement usable for the private verdict

The level repair is not merely a suggestion: with J_O^(1) defined by imposing the congruence only at the w_j, all the necessary actions are preserved. At each chosen place, H_w has reduction matrices `[[I,B],[0,C]]`. Conjugating them by diag(u,I) again gives matrices of that form (B changes to u⁻¹B or uB according to the direction); hence G_c normalises H. At Q these representatives are 1, so that they preserve χ_O. At the w_j they are also 1, so that they preserve the added principal condition. The action ϱ and e_c are therefore well defined on A(J_O^(1),χ_O).

The quotient at the w_j is Γ and commutes with H/G_c by disjoint supports. The Hecke operators used are outside the chosen places; the auxiliary local operators are supported at w_j. Both preserve the type e_c. The average Ψ over D need not preserve H term by term: the sum commutes with H and hence preserves its invariants. In turn it commutes with G_c and preserves the e_c-invariants within them. The complete proof of identity, integrality and integer divisibility of §1 applies literally to this corrected space.

**Supplementary verdict:** the obligation to construct Higman operators that remain in the type e_c, with the budgeted loss N_ch, is proved by this argument and can be used in a supplemented private deduction. The written text requires the correction of one definition and the two synchronisations of citations. These errata must not be counted as new mathematical obstructions once the supplement is specified. The supplement does not supply the exchange identity of 53 nor any other distinct automorphic input.

## 7. Closure of I/II/III → regularity: quantifiers and boundary of dependence

For this review 55:430–715, the formulations G1–G5 and (L)/(C), and 46:4898–4935 were reread. The historical pending items of SELMER/HODGE were collated with their final batches: the obligations SCC, I2/I4/I5, scheme, sparse/any/data, odd/triangle, Fitting, norm or local chain already reconstructed are not kept as pending. The level supplement of §6 discharges the remaining obstacle of preservation of e_c. The result of this section is a deduction **conditional on the identified inputs from other papers**, not an automatic validation of the whole series.

### Quantifiers

A pair (ℓ,ι) is fixed first. For that pair, I produces the summands R_(j,q) and R_(ν,z). The set is finite: j≤m; the space of forms at fixed level is finite-dimensional and has a finite number of systems q; there is a finite number of main pairs. II is applied **simultaneously to that list**, not once separately for each q. It produces one and the same τ, its powers 1≤j≤m, both signs in the quotients of L-values, and Selmer conditions for each summand. The exponents chosen for the characters in II are greater than m, so that the powers used remain ramified at Q and form m-fold twists. There is no illegitimate interchange between "for each q there exists τ" and "there exists τ for all q".

In I and II ℓ is not required to be large: if ℓ is a chosen prime, M4/M5 use the other one; ℓ=2 uses ζ_*²−1 being a unit, not division by 2; the coefficient modules may be ramified. In the arguments with "for all sufficiently large O", the finite algebraic datum is placed in one and the same O and enlarging it afterwards is allowed: the length limits are normalised by [O:Z_ℓ], and do not depend on having fixed a minimal O. P56 supplies the three loss regimes, including the small ℓ, not a hidden invocation of the Fontaine–Laffaille range.

III is applied to each Z_j(τ^j) and to each line of a main pair. In the first case the equality of multiplicities carries the system of W_j to the list of W_m chosen **before** choosing τ. The good labels contain the necessary primitive label above each prime; it is not required that all be irreducible. The rescaling does not introduce the root 1, because such an original root would lie in F_w and would be q₂-torsion, forbidden by goodness. In the rank 1 case the labels are X−1 before rescaling, and ω_w^j≠1 because q₂>m. n_W, t′ odd and the other ranks of III are preserved.

For each ι its τ is chosen and one defines θ_ι=τ. **It is not required that all the embeddings above the same ℓ use the same twist.** It is required that their bound be the same, and the expressions e′_ℓ, β_ℓ depend only on ℓ and on the admissible data. R1 results from Q being prime to ℓ. For R2, the valuation of the inverted ratio is ≥−e′_ℓ, so its absolute value is ≤ℓ^(e′_ℓ); the sum Σe′_ℓlogℓ≤x₁ gives the height budget with multiplier 1. For R3 one uses B_ℓ=(β_ℓ+v_ℓ(h₁))logℓ, independent of ι; ΣB_ℓ≤fa(log b)³/(mk) for **each finite set of primes**, exactly as 46 asks. There is no need to sum over all the embeddings, nor to divide the bound by their number.

### Two inputs of 55 expressly reread

**(L), 55:3992–4086.** On the integral vacuum, the sum over subspaces U contained in the kernel of a matrix of rank ρ gives ∏_(l<n−ρ)(1−q^lX). The identity n−ρ=t+(r−ρ) separates the factor of length t and leaves the polynomial of the space of rank r in q^tX. The character factors are α^(dimU), β^(dimU), so the final variable is q^tαβ⁻¹X. Transferring to the lift uses the adjoint action on the source group and changes the bar of w; it preserves exactly the complete polynomial, not only its last factor. This count uses neither exchange nor regularity. It imports the action of the kernel and the equivariance L2 of 54, not the determinant result that is to be proved.

**(C), 55:4096–4165.** The scalar pair (z,zI) acts trivially on Hom and by the splitting character on the kernel; hence ϱ(z)⁻¹k(g)=k(gz). Summing over the finite class group gives invariance of L. Unitarity and centrality give the adjoint; integral representatives above ℓ exist by rational parametrisation/weak approximation of the norm-one torus. They preserve all the lattices for all the embeddings above ℓ. If y is a false lift and orthogonal to L, the sum Y=Σϱ(s_c)y has zero descent, because its pairing with k(g) is ⟨y,L⟩. Thus the average of a test form is orthogonal to all the necessary false lifts. On the line, the sum introduces exactly h₁ and the valuation of its scalar Λ is ≤β_ℓ, giving the cost β_ℓ+v_ℓ(h₁). No other factor h₁ appears, nor a dependence on ι in the budget. If the line is zero, the inequality is trivial.

### Minimal boundary of inputs

| Input | Status within this branch |
|---|---|
|Admissible data/sizes of 46; free principal level|Their exact hypotheses and bounds are used; this branch proves regularity **for every admissible datum**. The construction/existence of such data and their analytic application belongs to 46.|
|Automorphic Galois, base change and local compatibility|G123/G45 and normalisations reconstructed; primary collation with Labesse/BLGGT and ℓ=p compatibility in SELMER §12. They are published theorems used with their hypotheses, not results that this audit re-proves.|
|Classical cohomological theory|Reciprocity/Chebotarev, local/global duality and crystalline/Fontaine comparison are express standard inputs; their new combinations and integral estimates were reconstructed in SELMER/HODGE. No new lemma on cup products taken as a black box remains.|
|Green's finite representations and depth zero|The cuspidal property of the primitive type and the parametrisation of inertias are used; the local passage to the generator and the mixed rank are reconstructed. The complete documentary collation of Green is not attributed to this branch; it is not a new pending bound of P55.|
|Multiplicities of 46/51|Necessary in main(c). The count of multiplicities is in MULTIPLICITIES and the archimedean inputs in THETA; the V2 review of spanning confirms the repair of uniformity/FJ without loss. Its global certification belongs to the assembly of those ledgers, not only to the proof of 55.|
|Kernel of 49/54, gauges/Gram of 53|Necessary for (L), integrality of IM and pairing. The Gram identity and its scale are closed independently of exchange. The phase properties actually used can receive the phase supplement of 49; there is no need to assume a strong formula distinct from the required behaviour.|
|IM of 54 for z≥2|Reconstructed in SELMER §13 together with SW/Rallis of the theta review, including ℓ=d, both embeddings and Euler factors.|
|IM1, z=1|The reduction to the exchange of 53 is reconstructed with N=a=2, b=0, e=1, μ=c≥1, and cancellation of characters in the expansion. It requires the exchange with its non-vanishing and constant independent of the twist. This remains a mathematical dependence external to this branch; its V2 review is carried out in 53.|

**Within 55/56 there remains, after the level supplement, no new step without reconstruction that could be hidden under the old "c by breadth".** The closure of regularity for the private verdict is conditional on the inputs listed, especially on the exchange of 53 for IM1 and on the necessary properties of the kernel/phase and multiplicities examined in the other reviews. A lack of documentary collation of priority, or a stronger phase formula that is not used, must not be turned into a fictitious mathematical impediment.

### Absence of cycles in this deduction

The sizes of 46 precede the summands I. The construction of representations and lattices of 55 precedes the local estimate of 56: 56 receives the weights, the inertia types and the class of cocycles, not the conclusion of its own loss bound. Then 55 uses the bound for III and sums. II uses IM of 54, whose branch z≥2 comes from Rallis; z=1 receives the exchange of 53. The regularity being constructed is not used to prove exchange, the kernel, the equality of multiplicities or IM. The regularity copied in the appendix of 55 is the result to be obtained, not a premise of I/II/III. With these inputs ordered, the chain 55→56→55→46 contains no logical cycle in the audited segment.

## 8. Primary collation of Green completed

The [original text of Green1955, AMS](https://www.ams.org/tran/1955-080-02/S0002-9947-1955-0072878-2/S0002-9947-1955-0072878-2.pdf) was accessed through the indexed text of the PDF. Download and direct capture returned 403; no visual inspection of the facsimile is claimed.

The following were verified: p.403 defines ∘ as parabolic induction; pp.436–437 construct the homomorphism from symmetric functions to the algebra of characters; p.439, Lemma7.7 identifies simplexes of degree r with irreducible polynomials; Theorems12–13 parametrise the irreducibles by partitions over simplexes, with sum of weighted degrees equal to the rank.

The application 51:4951–4973 keeps those hypotheses. A character of rank r_i<r does not contain the simplex of degree r. Multiplying symmetric functions within each simplex only changes its partitions, without creating another simplex. Hence an induction from proper ranks does not contain the primary character (g^(1)) of degree r. By Frobenius reciprocity, its invariants under the unipotent radical of every proper parabolic are zero: exactly (G). A primitive label satisfies irreducibility, a sufficient condition; it is not needed that all the labels do. **Verdict (a) for this classical import**; the documentary pending item on Green mentioned in §7 and MULTIPLICITIES is discharged.

## 9. V2 coordination update

The theta review reported, after its V2 pass, complete cancellation of the characters in `product` and in its effective application with (γ,γ), also in `vantop`. It finds no new obligation in the kernel of 49/phase needed for IM; the fixed positive factor |d₀|_f^j omitted in one expression for κ₀ is absorbed into the existential constant and does not change the later calibration. The spanning review confirmed closure of uniformity on compacta and FJ, without change of constants, and the sufficient phase supplement of 49. These checks are in their respective V2 reports; they are recorded here as inputs of the joint review, not as a second independent audit of 53.

With them, with the primary closure on Green of §8 and with the level supplement of §6, **this branch identifies no additional pending mathematical obligation that would prevent I/II/III→regularity of 46**. The verdict on the whole must still take from the review of 53 the complete closure of exchange and its other inputs: removing the character obstruction is one concrete part of that closure, not an argument for inferring it by itself. The errata in the citations of 56 and in the definition of level remain expressly identified editorial repairs of the V2 text.
