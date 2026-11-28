# P54: three exchanges, first factors and correction of ν^flat

Date: 2026-11-28. Review of `main.tex`: 2111–3448, 3496–3550, 3780–3940, 7137–7608. Independent audit of the characters, scalars, congruences, integrality and sizes. The manuscript was not modified.

## 1. Literal failure located and concrete repair

**(b) for the equality of characters of `pte:third`, line 2730, with the printed definitions.** Line 2695 defines

`ν^flat = ν″_ϑ υ^m / χ′`.

Hence `χ′ν^flat υ^m=ν″_ϑ υ^{2m}`, whereas 2730 identifies it with `ν″_ϑ υ^m`. Since υ has infinite weight one and m>0, the characters really differ. The same definition reappears in `pfq:tame(T4)`, 7584, including the final exponent `+m`; and the incorrect equality reappears in `ptf:leftside`, 3366. It is not a constant phase: it is a difference of weight of a character of an integrated variable.

The repair that preserves the formulas used is to define, at 2695 and 7584,

`ν^flat := ν″_ϑ / χ′ = μ^flat υ^{-jΔ+j+(t+k−1)/2}`,

that is, to remove the factor υ^m and the final summand +m **in those two definitions**, keeping the character `ν^flat υ^m` in F_i and in the operative formulas. ν^flat remains independent of the twist and unramified at all finite places. Its weight becomes `−#ι(τ)`, as the later computations require.

With this corrected definition:

- `α=χ′ν^flat υ^m=ν″_ϑ υ^m`, with weight `m−#ι(τ)`;
- `β=ν″_ϑ`, and `αβ^{-1}=υ^m`, exactly the target character on the reversed side;
- `n=3m+N″`, `b=3m`, `a=N″`, `a−b=7m+k=2z_*`;
- `α^{-1}υ^{3m+z_*}=(ν_*ϑ)^{-1}`, because `j+(t+k−1)/2−2m−z_*=j+(t−11m−1)/2=n′`;
- the source character of the kernel F_i is `ν^flat υ^m`, of weight `m−#ι(τ)`, not `2m−#ι(τ)`.

z_*, the number of critical pairs and H_j do not change. This correction must be propagated to the interpretation of F_i in psp/psv; the branch in charge of that proof was expressly notified. The following verification is for this corrected reconstruction, not a literal certification of the current version.

## 2. Explicit exchange: independent constants and archimedean projection

The application of P53 has `μτ=#ι(τ)+n/2−l≥1`, `γ=α`, `a=b+2d`, `q_W=l=q_{I_a}+q_{V′}` and `2l+2≤n`. The input vector Q₀ is fixed before the modulus/character. P53 gives x₀ and C independent of them; `|c₀|²=C L_*` and c₀≠0.

The circular average of `pte:explicit` removes all the variables except the square block x^flat. The compact target average selects its power of the determinant. The extension of polynomials to x₀ must be made in the moment/Schwartz norms in which the integrated theta functionals are continuous; mere Hilbert density is not enough. With the smoothing and density of P53 `pcn:smooth`, this precision allows the step without changing κ or introducing a dependence on the modulus.

`ptf:fock` and `ptf:SDlaw` were recomputed: on the variables of positive product sign the substitution is `h^t X g^{-t}`; on the negative ones, `h^{-1}Xg`. The character of the vacuum is the inverse of the determinant of the negative block. The factors of det(u) of the minors cancel exactly the target character `l−#ι`; on the circle, the power `z^{aNι}` cancels the prefixed one, and the MP homogeneity produces `z^{-2pNι}` against `z^{(2p+a)Nι}`. No phase depending on z remains.

The polarisation uses the irreducible module of products of maximal minors (Cartan/Grassmannian). The stackeval identity transports the same coefficients to SD, even if the lower matrix loses rank, since then its complementary determinant d may be zero. The case p=0 is the constant space and does not demand a non-trivial Grassmannian.

The final normalisation is `c=κ/c₀`; hence `|c|² L_*=|κ|²/C`. There is no division by κ. It is legitimate for this scalar to be zero initially; its non-vanishing is obtained later with global spanning. The passage from integral to sum over classes uses masses one and the stabilisers, with no index omitted.

## 3. Negation and first two exchanges

`ptf:conj` is reconstructed using the antilinear intertwiner that preserves the vacua and the mean-square normalisation of theta. Its constant ε has modulus one and depends neither on the character nor on the modulus. The splitting correction is `Aω_W(g)A^{-1}=υ(det g)ω_{W^-}(g)`. Applied to Hom(S,T), `det(g,h)=det(h)^{rank S}det(g)^{-rank T}`, it gives the character shifts `(α^{-1}υ^{rank T},β^{-1}υ^{rank S})`. The classical content needed on change of the splitting character is collated in parallel with P3; this character is not inferred from the uniqueness of Heisenberg alone.

In the first exchange, d=m/2 and α=c^{-1}; its conjugate has both characters `cυ^m`. The second uses `(W,V′,I_a)=(I_m⊕S,I_m^-,I_{3m})`, d=m, α=cυ^m. In the product over the target, the source characters are distributed as `(cυ^m)·1` and the common target remains cυ^m. In the product over the source, the target is distributed as `c·υ^m` and the common source remains 1. The exterior factor c(det x) appears on both sides and cancels. Thus

`|γ|² L_*(c^{-1}υ^m,m)L_*(cυ^{m/2},m/2)=C₁C₂`.

The non-vanishing of the carrier does not use those c nor a circular identity. Its Fourier coefficient of Gram identity reduces, by finite support, to a single compact class; the archimedean slice is non-zero at some invertible point. The Heisenberg translations separate a non-zero vector by the Parseval identity of theta. The latter is the precise justification for the conclusion; it is not enough to assert that the kernel of a theta functional is closed in the Hilbert norm. The concurrent review of the carrier verified this substitution.

## 4. Third exchange and first forms

With ν^flat corrected, `pte:one` is applied with `(a₁,a₂,β₀)=(χ′,ν^flat υ^m,υ^m)`. The sum of translates removes the finite average with the exact factor `N=#GL_{3m}(O_E/π_M²)`, because the carrier is K_S-invariant and a₂ has no tame part. Hence `c′_ϑ=c₃γ/N` and `|c′_ϑ|²H_j(ϑ)=C₃C₁C₂/N²`. All the moduli of π_M² are used with their primes once only in L_*; the conductor factor is not duplicated.

`pte:matched` is an identity of Schur complements over the finite ring, and the non-invertible supports annihilate both sides. `pte:column` recovers simultaneously σ≡ι₀ modπ_M and Λ(σ−ι₀)≡0 modπ_M². `pte:rowstab` divides the invertible support into cosets AH. The orbit–stabiliser count converts the original sum into the sum over classes at the lower level; the Haar index must not be inserted in addition, since the expansion of the datum already supplies the sum over cosets.

In `ptf:laplace`, the constant rows remove the columns of X after h and each coefficient depends only on Z. The conjugate-linear map ξ↦p″_ξ has kernel W″⊥; choosing a basis of W″ makes the expansion unique. `ptf:sum` keeps the same source character and multiplies the targets. `υ^{m−j}` and `ν″υ^j` are distributed, whose product is `ν″υ^m`, as the corrected third exchange requires.

The transformations of the first forms are exact: the coefficients c_λ receive χ′(det k), and their conjugates receive χ′(det k)^{-1}; the kernel W also receives χ′^{-1}, which cancels on inserting the form by conjugate-linearity. The rational action is obtained by comparing coefficients in SD, invariant under U(V″)∞. The identity `ν″υ^{m/2−j}=μυ^{n/2}` uses `r=k+m−1`, `t=5r`; its exponents are `(5r+k−1+m)/2=3r`. Hence one obtains exactly the kernel θ″ used in glue, not another isomorphic kernel without fixed normalisation.

## 5. Integral scale, complementary hook and bounds

`pfq:hook` uses the integral and unitary star map on each exterior power: it transports the lattice and the projection to the complementary diagram. The factor H^c makes the projection integral. The notation `e^{3e}` in that lemma has as base **the integer e=|μ^c|**; the proof correctly uses `log H^c≤3e log e`, not the exponential of natural base.

In `pfq:Q`, each coefficient is a complementary determinant of size ≤12m+1, homogeneous of degree N″−h. Cauchy–Binet sums squares of its minors and Hadamard gives the joint bound, avoiding multiplication once more by the number of fillings. The rational substitution in the block W^flat changes Y to γY and contributes the determinant character that cancels the source character of weight −#ι. These computations depend on ν″, not on the incorrect definition of ν^flat, and do not need to be modified.

`plf:KS` is reconstructed with the inputs of 49 already audited. The expansion by vacua has Nm(m)^{2ln_N} terms and denominator Nm(m)^{ln_N}. If qM²∈m and ℓ∤q, M^{4fln_N}/Nm(m)^{ln_N} is integral above ℓ; the translations are of level M². At places where a_w is not a unit, these can only enter via Q and are excluded from ℓ∤NmQ, so that the vacuum of the unscaled lattice is not falsely invoked. The scale `(dM²s₀/κ_F)^e` converts the jets into integral derivatives; at ℓ=d one uses explicitly `v(g″(0))>−2`, and the derivatives of g(dz) are integral. The exponentials preserve integral derivatives by the Bell polynomials with integer coefficients.

For KS2 the TWO consequences of δ_g reconstructed in REVIEW-PHASE49-V2 are used, not its strong classification. The Gaussian integral, with ρ=dΩ^{-1/2}M^{-2}≪b^{-37}, gives a factor ≤2^{D+1}; the number of terms and M^{4f ln_N} are maintained. The total logarithm is ≤x^{200}≤x₁ in the declared range. The kernel constant does not depend on the character, on the finite datum nor on the choice of i.

In `pfq:ff`, the normalisation is `κ₁=n′_Aut² c_{m,3m,0} conj(c_{j,N″,0}) ε_j c_{12m+1−j,N″,e}`, `κ=H^c conj(κ₁)`. The ε_j cancels that of the negation; n′_Aut removes both stabiliser denominators. The forms are projected as `H^c π(conj(κ₁a))`; hence integrality is proved in the conjugate embedding, as written. For sizes, σ′=σ∘c acts on the coefficients and the rational projection has norm one. Duality for the vector of all the C_U avoids a factor for its dimension. The final bounds are `2logH^c≤6072 fmb logb` and the term of minors ≤10764 fmb logb`, both below `1.7·10⁴ fmb logb`; the other losses fit in 8x₁. No false universal commutation σc=cσ is used.

The substitution of the first factors by κ times the original ones changes Ξ by conj(κ), c′ by c′/conj(κ) and C_x by C_x/|κ|². Only the fixed constant C_j in Gram changes. The tame characters are constructed by extension of a character of the open subgroup, with compatibility on μ_E; this is checked with q₁|q₂ and the primes ≡1 modq₂². The correction of ν^flat in T4 leaves all those conditions intact.

## 6. Verdict on scope

- **(b), literal:** definition of ν^flat at 2695/7584 incompatible with the equality 2730 and the uses 3366/6448.
- **(a), corrected reconstruction:** three exchanges and their first factors, with ν^flat=ν″/χ′, topological correction of the average of explicit and Parseval justification of the carrier; the constants and H_j remain exact.
- **Individually identified classical input:** the compatibility of splitting under negation/change of character must be received from the normalisation P3 collated by the corresponding branch; the whole count of signs starting from it has been checked.
- **General Gram:** the algebra of glue and of the compressed determinant is verified; general periods already closed in REVIEW-54-GENERAL-PERIODS-V2. The global spanning `po:span` follows the separate audit of psp/psr/psv, with the same corrected definition of ν^flat. Gram is not declared complete before that result is received.

## 7. Cross closures and synchronisation with P58

The primary review of splitting was closed in `SPLITTING-V2`, §§6–7: in Murase's left normalisation the character is υ^{-1}; the form R_g=Q(g−1) on the quotient by the kernel satisfies `R_g*=R_g g^{-1}`, whence `Δ/conj(Δ)=det g`. Replacing υ by `υ·(μ∘bc)` multiplies the splitting by `μ(det g)^{-1}`. This is exactly K3 with s=−1, also under doubling D2; the orthogonal factorisation of M and Δ preserves the compatibility of products. Thus the classical input that §6 left individually identified is discharged, without an arbitrary residual phase.

The spanning branch confirmed the precise effect of the printed definition on H5, 6448: the weight would be `2m−μ₁`, and the computed coefficient would have an additional factor `det(h)^{-m}`. In the average that must give the initial positive value, that central weight forces zero. Hence it cannot be asserted that the printed definition is harmless. With the corrected definition the weight returns to `m−μ₁` and the identity H5 is restored; the formula `psv:char` uses ν″ directly and does not change. The complete closure of span is recorded in its own ledger.

In the volume P58 the same defective definition appears at **51272** and **56151** of `main.tex`. The second also includes the final exponent `+m`. These are the two locations that require the same correction; the uses of `ν^flat υ^m` are kept. This is a supplementary reconstruction, not a change already incorporated in the manuscript.
