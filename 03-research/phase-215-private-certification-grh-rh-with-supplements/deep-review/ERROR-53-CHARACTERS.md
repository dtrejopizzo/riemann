> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the remaining results are being consolidated.

# Incompatibility of characters in `pcu:product` (paper 53)

## Local verdict

**(b) Incorrect as written.** The formula of `pcu:product`, lines 3351–3352, does not respect the definition of the two splitting characters of lines 671 and 1732. The first invalid inference of the proof is at 3359–3360: after restricting αβ to each block, it is asserted that β can be assigned to the first and α to the second "by the convention" of twisting. That convention does not allow characters to be removed.

This defect is also present in volume 58, lines 37993–37994. It is not a discrepancy between an old version and the unified volume.

The computation was checked independently by the theta review, which collated the definitions, the twist law, the external product and the application to the period. The external product contains no hidden dependence on α or β that would remove the factors.

## Direct computation

The manuscript defines

`ω_{α,β}(g,h)=α(det g)⁻¹ β(det h) ω_Hom(g,h)`.

Write A(g)=α(det g) and B(g)=β(det g). The Heisenberg translation and the data do not modify these scalar factors. Under the orthogonal factorisation of the untwisted representation which the proof itself invokes:

| Expression | Character factor |
|---|---|
| Left-hand side of 3351 | A(g)⁻¹ A(y)B(y) A(l)B(l) |
| Right-hand side of 3352 | A(g)⁻² B(y) A(l) |

Hence the factor

`A(g) A(y) B(l)`

is missing.

The identity compatible with the definitions would be

`LHS = α(det g) α(det y) β(det l) · RHS`,

with the same product normalisations that the text intends to use. A fixed constant of tensor identification cannot remove a factor that varies with the characters and with g,y,l.

A general way of distributing the twists correctly is: on decomposing the target group into two blocks, the same target character appears in **both**; the source characters assigned to the two factors must have product equal to the original source character. In the printed formula neither of these two things happens.

## Why it is not an identity only on a support where the factor equals 1

The lemma quantifies over characters α,β, finite data and arbitrary real vectors, and over g,y,l. It does not impose α(det g)α(det y)β(det l)=1.

Already with α=1 and g=y=1, varying β only introduces the factor β(det l) on the left-hand side. On the right-hand side β(det l) does not appear. Choose an automorphic character with non-trivial archimedean component, such as those of positive weight which the context contemplates, and l infinite close to 1 with β(det l)≠1. The data can be chosen with both untwisted theta functionals non-zero at 1; by continuity they remain non-zero in a neighbourhood. This excludes the omitted factor becoming harmless through universal vanishing of the kernel.

The incompatibility can also be checked directly at the level of representations, before applying theta: the determinant factors are different for invertible operators and non-zero tensors.

## Dependence in the global proof

The explicit use is in `pcu:period`, lines 3407–3410, with α=γ and l=u, a variable that is integrated over [U(W₀)]. On keeping the characters, the integral which the text identifies with I₀(ν) carries in addition **β(det u)**, and outside there appear γ(det g)γ(det y). The modulus one of that factor does not allow it to be taken out of an oscillating integral.

The chain of uses as written is:

`pcu:product → pcu:period → pcu:coeff → P-top → P-std → P-matches/P-equal → pcx:X`.

`pcu:coeff` uses the replacement by the period at 3622; `P-top` rests on that lemma at 3732–3740; `P-std` uses `P-top` at 4513. The exchange is used afterwards in the squares and in the factorisation of the determinant of the chain.

**Impact demonstrated:** this route does not prove the exchange as written. It does not follow that the statement of the exchange is false, nor that RH is false. Nor is it enough to correct a single equality of characters in order to declare the whole argument repaired: the correct period, its non-vanishing and its exact dependence on ν must be reconstructed, and it must be checked that the subsequent identities preserve the required factor L_*.

## Work needed for a repair

1. Fix consistently the characters of each factor on decomposing Hom(W₀,U⊕W₀).
2. Recompute `pcu:period` and the inner coefficient of `pcu:coeff` with those characters.
3. Prove that the resulting period is the one entering the equal-rank ratio, or prove a new identity comparing it with that ratio.
4. Redo the deductions of `P-top`, the constancy of the ratio and the absolute value of c. A complete repair has not yet been supplied in this audit.

## Limit of a repair by a mere change of names

The general factorisation compatible with the definition is

`ω_{a,b}(g,y⊕l)=ω_{a₁,b}(g,y) ⊗ ω_{a₂,b}(g,l)`, with `a₁a₂=a`.

Here the characters are understood as restricted to the relevant determinant groups. In particular, the target character is the same in both blocks. If one wishes to keep exactly the small factor `ω_{γ,β}` and the equal-rank factor `ω_{γ,γ}` employed in `pcu:period`, the source of the product would be γ², and the target restricted to the blocks would be β⊗γ. A single twist by the determinant of the large group restricts as b⊗b, and so does not produce β⊗γ for distinct characters. This shows why changing only the name of a source character does not fix the identity while keeping the two periods of the argument.

This observation does not exclude a repair by means of a different construction of the datum, a twisted period or an additional identity. It delimits the obligation: one must explain how the new construction preserves the period and its L-factor, and not merely obtain a different formal tensor identity. For the arbitrary characters over which the lemma quantifies, those additional conditions are not available in its statement.
