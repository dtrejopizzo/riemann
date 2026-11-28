# Supplements to the corrected sources

This note proposes exact, verifiable formulations to complete the version identified in sources-v2.json. The manuscripts were not edited. Their inclusion in a verdict must be explicit: proofs that the current text does not yet contain are not attributed to it.

## Auxiliary level of pri:forms of 55

Replace J_O^(1)=J_O∩J_1 by

`J_O^(1) = {k∈J_O : k_(w_j) ≡ 1 mod w_j for all j}`.

The places w_j are disjoint from the chosen places. Then J_1 is normal in J_O^(1), the quotient is H=J_O/J_0 and the forms of level J_O^(1) are exactly the H-invariants in the space of level J_1. With this definition, the integral average Ψ=Σ_(d∈D)R(d)^−1Ψ_1R(d) preserves that level and commutes with e_c. The identity Σ_(k∈Γ′)k^−1Ψk=#D remains valid because D and Γ have disjoint supports. There is no division by |D|. Since #D|N_ch, all the losses are preserved. Proof and applications: [review of 55/56](../deep-review/REVIEW-55-56-V2.md).

## Fixed coefficient of pcu:coeff of 53

With the notation of U2, d_0=det(s_0x_U), B=y^−1Y, q=s_0x_UY. The ratio of Levi characters is ν_bc(det q), the ratio of finite data is ν_bc(det x_f)^−1, the period contributes ν_bc(ζ_B)^−1 and the difference of target characters is ν(det y)^−2. Since det B=ζ_B det x_f and ν_bc(det y)=ν(det y)^2, their product is exactly ν_bc(d_0).

The positive quotient of moduli must be kept in adelic form:

`|det q|_(A_E)^j / N(ζ_B)^j = |d_0|_(A_E)^j`,

since det x_f is a unit and det y has adelic modulus 1. Therefore the full expression of the fixed factor is

`κ_0 = (ε_T/ε_U) |d_0|_(A_E)^j`.

The printed formula keeps only the infinite part. The frames and s_0 are fixed before ν and its modulus are chosen, so the additional finite factor is fixed, positive and non-zero. It can be incorporated into K, whose assertion in pcu:coeff is existential; the dependence on ν, the period I_0, the non-vanishing and the normalised ratios are not modified. This clarification is different from the supposed residual character of V1: that residual character does not survive in the corrected application.

## Phase of Paper 49: sufficient lemma

Instead of the strong classification of δ_g attributed to W4, use the lemma and proof of [REVIEW-PHASE49-V2](../deep-review/REVIEW-PHASE49-V2.md): all its conjugates have modulus I_g^−1/2; if g is integral above l, δ_g is an l-adic unit and the translations are chosen integral above l. The arithmetic proof by means of finite Schrödinger models must accompany the statement; complex unitarity alone does not prove it. The exact normalisation has been reconstructed in [REVIEW-SPLITTING-V2](REVIEW-SPLITTING-V2.md), §§6–9: the Weil index coincides with the Gaussian constant of the norm, with ψ_K=2ψ_k; doubling, change of character and negation preserve this normalisation. The impossibility of consulting Kudla's original does not remain as a mathematical obligation: an explicit reconstruction is supplied with Murase and the conventions reproduced by Chan.

## Documentary synchronisation

In the appendix of 56, update the domain of BL to e_cF(O) and replace the old explanation of G4 by means of a non-existent norm with that of the compatible tame generator of 55. In 58, replicate the corrected definition of level above and any clarification of κ_0. The finite comparisons without proof of 46 and the links to certificates are not premises of the automorphic deduction of GRH/RH; they are kept outside the certification of that chain until they are treated separately.

## Character νflat of 54 and its propagation

At 54:2695 and 7584, replace the definition by

`νflat = ν″_ϑ / χ′ = μflat υ^(−jΔ+j+(t+k−1)/2)`.

Remove the factor υ^m and the final summand +m in those definitions only. Keep νflat υ^m in the kernels, in F_i and in the applications. Replicate at 58:51272 and 56151.

The proof of sufficiency is recorded in [three exchanges](../deep-review/REVIEW-54-THREE-EXCHANGES-V2.md): α=χ′νflat υ^m=ν″υ^m, β=ν″, αβ⁻¹=υ^m, and α⁻¹υ^(3m+z*)=(ν*ϑ)⁻¹. The identity of exponents is j+(t+k−1)/2−2m−z*=j+(t−11m−1)/2. The source weight returns to m−μ1. By [general spanning](../deep-review/REVIEW-54-GENERAL-SPAN-V2.md), one recovers H5 and F⁰(1)=I_(u3)φ°(g1)||v||²≠0. Neither H_j, z*, the levels nor the bounds of the first factors change. In the uncorrected text, the additional central character forces F⁰(1)=0; this is why the correction is indispensable for the written proof.

## Generation and functionals of 54

These clarifications also form part of the supplement; they are not silently attributed to the manuscript:

1. In ppe:harm, use the generation of the polynomial component by U(g_W,C) and U(V) starting from the p_ξ. The member U(V) is compact and the relevant joint irreducibility is collated with Howe (3.9a). The proof is in [general periods, §3](../deep-review/REVIEW-54-GENERAL-PERIODS-V2.md).
2. In ppe:bottom, the action Ψ(T)↦Ψ(TA) corresponds to the operator by A, not A⁻¹; translate the argument as well. The vanishing for all arguments is preserved. In the weighted sum, respect the conjugate-linearity with respect to Ξ; same note, §4.
3. In pte:explicit, extend from polynomials in the topology of moments/Schwartz, with pcn:smooth of 53; do not use Hilbert density alone. The integrated functionals are continuous in that topology and the compact average preserves the required seminorms.
4. In pte:carriernz, replace the assertion about a closed Hilbert kernel by Parseval: the integral of |θ(ρ(w)Λ)|² is ||Λ||²>0 for the non-zero Schwartz slice. Therefore some translate has non-zero value.
5. In psv:c and psv:F, apply pss:coefs with E=Schwartz and the C∞ orbit proved in pss:carrier; do not simply identify the smooth vectors of an arbitrary subgroup with Schwartz.

The proofs of points 3–5 are in the notes on [exchanges](../deep-review/REVIEW-54-THREE-EXCHANGES-V2.md) and [general spanning, §7](../deep-review/REVIEW-54-GENERAL-SPAN-V2.md). None adds a loss to the constants. The supplement includes these proofs by reference, not merely the instruction to correct words.
