# Paper 43: closure of the Hochschild front

Direct review of `main.tex`, lines 558–742 and 1200–2886. Verdict **(a)** for `prop:crossed`, `thm:excision-input`, `thm:kunneth` and `thm:shadow`, in the topologies and with the bimodule convention expressly declared. This verdict is not extended to the later completions, signature, determinants and rulings. The Schwartz equivalence of products is used as a classical result cited by the manuscript; its general proof is not redone.

## Excision and tensorisations

The topological point is not reduced to algebraic excision. The real partition of unity and the finite idempotents give a continuous right splitting, with sum of seminorms controlled by the loss `l→2l+2`. The block `χ_p` retains the value at 0: replacing it by a sum of shells would have been invalid, and the text does not do so. The sum defining h converges absolutely in the completed projective product. The identity `h(ab)=h(a)b` also holds for multipliers of the ambient algebra.

In excision 1678–1762, the topological complement produces a **finite** sum of patterns in each degree. The first quotient is filtered by the length of the tail from the first letter L: the faces not internal to I reduce that length. Its graded pieces are the reduced bar of I tensor a complete space and are contracted with h. In the second quotient one filters by the position of the first I. The auxiliary module N has action induced from A/I, so that I annihilates it. The maps Φ and Ψ are maps of complexes by right linearity of h; the residual term of degree 0 disappears precisely because I·N=0. The filtration is exhaustive in a finite number of steps per degree and the contractions extend compatibly; no infinite limit of operators in a fixed degree is taken.

Künneth 1765–1846 uses the bar of the unitisations and grading by supports. The free terms of the total tensor are indeed free bimodules over the tensor unitisation. The comparison by generators is continuous and the contractions preserve supports. The mixed part of the quotient `C⊕I⊕J`, with IJ=0, is contractible by excision, not discarded by intuition. The inclusions are the arrows of equivalence; their inverses need not be equivariant. The naturality required by Koszul is proved through the arrows and the cone argument, not by wrongly assuming equivariant homotopies.

## Rapid crossed product

In 2115–2392, the identification of spaces of ℓ¹ families with the projective tensor is proved by equality of seminorms and density of finite support; nuclearity of the p-adic algebra is not presupposed. The change of factors A by means of α_g costs a power of H(g), absorbed by rapid weights. The change `(g,h)→(g,gh)` preserves the family of weights by submultiplicativity.

The contraction of the Koszul resolution over Z uses finite sums between 0 and n: its norm of weight k is ≤`|n|p^{k|n|}≤p^{(k+1)|n|}`. Hence it is continuous in the topology actually used, which requires all the exponential weights. The induced bar resolution is continuously split; its columns are finite in the outer degree. The comparison by free bimodules preserves the total label γ.

The twist of the component γ is exactly `α_γβ` on the right. The initial Koszul operator is `α_p^{-1}−1`; the map in degree I given by `∏_{i∈I}(−α_pi)` identifies it with the Koszul of `α_p−1`. Indeed `(α^{-1}−1)(−α)=α−1`. The reversal 1222–1235 afterwards changes the right convention to the left one and respects the dilations. There is no lost inversion of γ.

## Local complexes and shadow

The block lemma 1849–1960 inserts the idempotent before the first non-matching edge. Cancellations of faces and the loss of seminorms needed to sum all the components are verified. For non-unit twist there are no diagonal blocks of shells; the single block of the origin survives as C. For units different from 1, a character κ with κ(u)≠1 gives an inverse of `z−ρ(z)` and a contraction with uniform loss `l→2l`. At the real place one enlarges by periodic multipliers, or by sign, uses a central homotopy and returns to the ideal by excision. The convention `A_ρ` is **left** twist, so `R_z−L_z=z−ρ(z)` has the correct sign.

For real trivial twist 2539–2662, `x=sinh t` transforms the condition of superexponential decay into the Schwartz topology. The resolution by the difference of coordinates has continuous division: near the diagonal the integral of the derivative is used; far away, the division by x−y and its derivatives are bounded. The map to the bar resolution gives in Hochschild the derivation D, with invertible factor cosh(t). Only the final map π has to be equivariant, as indeed it is.

For trivial shells 2664–2754, the contraction is constructed by the first separation of cosets. A test of conductor M requires only m≤M; indicators of the same coset have absolute Fourier sum 1. The cost is ≤16nM and is absorbed in the conductor `N'=N(n+2)+1`, uniformly in the shell j with weight 2l. This is why the contraction extends to the completion; density of finite characters alone would not have sufficed.

Finally 2756–2886: the projections to degree 0 and evaluation at 0 are equivalences and commute with dilations. If the real component of γw is different from 1, the local tensor contracts and only the outer scalar summand remains. If it is 1, the non-trivial finite components are evaluated at 0 and the trivial ones remain, while the real factor contributes degrees 0 and 1. Applying Koszul to the equivariant arrows preserves equivalences by the finitely filtered cone. One obtains exactly `thm:shadow(a)–(e)`.

## Scope and novelty

This closure discharges the topological pending item of the first report 07. It does not produce positivity of the Weil form: the computation itself leaves the limitations of the shadow visible, and the paper distinguishes its homological construction from the trace distribution. The explicit combination of semilocal algebra, twist by ideles and controlled contractions is a verifiable result that deserves bibliographic comparison; its priority is not established. The general Hochschild construction for crossed products and the adelic pattern have antecedents cited by the author himself. The possibility of developing this part as separate work does not depend on the chain towards RH being closed.
