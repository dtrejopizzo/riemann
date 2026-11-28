# P54: general periods and cross-review of the phase of Paper 49

Date: 2026-11-28. Direct reading of P54 `main.tex` 3944–4638, `plf:harm` 3685–3699, `plf:L4` 3701 and following, definition of the polynomial 498–508; collation of the Gram formula 1134–1235. This supplement discharges the general part of the periods, which THETA/TL04 had reconstructed only in rank one. This closure is not to be confused with that of the three exchange identities of 54 nor with `po:span`, which are separate obligations.

## 1. Cross-review of REVIEW-PHASE49-V2

No circularity or arithmetic loss was found in the supplementary proof of the TWO necessary consequences of δ_g, under the explicit normalisation P3/D2 and the property of the vacuum line. The collation of those properties with the primary sources belongs to the concurrent review of spanning.

The crucial point is to keep a common arithmetic model: the coefficients of the indicators, phases, Fourier transforms, changes of polarisation and their inverses lie in the indicated field A; the measures of supports are rational. That σ commutes with conjugation on A is proved first by means of the moduli of all the conjugates of υ(a); it is not deduced from abstract unitarity. The conjugation of the finite Gram identities is then legitimate.

The recovery of A_g from A_g⊗1 does not require choosing a transcendental phase: in compatible symplectic polarisations, the tensor of normalised indicators provides explicit algebraic coefficients. In residual characteristic p different from ℓ, the denominators of the changes of model, normalisations of vacua and Fourier are powers of p. Both the operator and its inverse preserve the integral structure. Above ℓ, the action of the compact stabiliser on the vacuum line is a smooth character of finite image. The primitivity of the vacuum, transported by an integral automorphism, forces the common coefficient of the expansion to be a unit, not simply integral.

Precision of wording: choosing representatives with ℓ-component equal to zero is a statement about adelic representatives. If rational representatives are required afterwards, simultaneous approximation allows them to be chosen **integral** above ℓ, which is exactly what S1 needs; one must not demand that a non-zero rational have ℓ-component zero. This does not alter the conclusion used.

This argument does not certify the stronger formula that classifies δ_g as ONE specific value of υ times a root of unity. The strong phase remains outside the proved content; its two sufficient consequences are indeed reconstructed.

## 2. The difference between rank one and general

The general Gram formula uses `po:glue`, in particular (G3), which refers to `po:periods=ppe:main`, and (G2), which refers to `po:span`. The compact formula `pex:rallis` of rank one proves neither of these two inputs by itself.

In the general instance, `rank W=r`, `rank V=n=r+t=6r`, `V` is positive definite and `N″=r+9m+1`. The tower is needed up to `p=N″`. Its hypothesis holds because `2r+2N″+3=4r+18m+5<6r`; one uses `r≥x^5`, `m≤2√x` and the enormous rank of the admissible data. The rank-one check `45<2z` is not substituted here.

## 3. Polynomial generation: explicit repair of a sentence that is too strong

In `ppe:harm`, 4202–4223, steps (a) and (b) are correct: Schur orthogonality and F1 give `L(p_ξ)=0` for all ξ, and differentiation through the source gives `L(ω(X)v)=R_XL(v)`. The integral is over the compact quotient of the target group; the derivatives of the Schwartz data allow the differentiation. The compact average removes the types distinct from the one that appears in the coefficients of Ξ.

The sentence of (d) that identifies the whole space of harmonics of that type with `{p_ξ}` needs, in general, the addition of generation by the compact subgroup of U(W): the minimal type of the source need not be one-dimensional. The conclusion that is used admits this more direct proof, without a new estimate or constant:

1. U(V) is compact; its centraliser in the symplectic group of the real space underlying Hom(W,V) is U(W).
2. The polynomial component of an irreducible type of U(V) is irreducible for the joint action of U(V) and the complexification of the Lie algebra of U(W).
3. The subspace `U(g_W,C)·{p_ξ}` is stable under both actions, because the actions commute and ξ↦p_ξ is equivariant. It contains a non-zero vector: the explicit product of minors of `plf:harm`.
4. By irreducibility, it is the whole polynomial component. Steps (a), (b) annihilate L on it; the compact average annihilates the rest.

Point 2 was collated directly in the facsimile of [Howe, *Transcending Classical Invariant Theory*, p.542, (3.9)(a)](https://www.math.utah.edu/~ptrapa/math-library/howe/howe-transcending-1989.pdf). On the same page, Proposition3.1/(3.10)(b) gives the generation by harmonics cited in the paper. This application uses the pair with a compact member; it does not suppose irreducibility of components of an arbitrary non-compact pair, nor does it require Short Forms or injectivity of a global lift.

Verdict: **(a) for the conclusion `ppe:harm` reconstructed by means of this precision; the literal sentence about the whole space of harmonics is not certified as written.**

## 4. Bottom: all matrices, not only columns

`ppe:row` is valid in general rank. If the upper block is singular one takes a row of its left kernel. If it is invertible but the lower quotient does not satisfy the required integrality/congruence, a row `(y_a,−e_a)` and a coefficient of maximal size produce exactly the annihilating row, including the strict congruence at Q.

In case A of `ppe:bottom`, the support of the normalised datum is a single orbit of K_ϑ, through the block matrix `(y′,0;y″,1)`. The average with character of the indicator of a coset becomes a multiple of that datum. The erratum already identified in TL04 persists: with the action `Ψ(T)↦Ψ(TA)`, the operator is `ω(A,1)`, not `ω(A^{-1},1)`. The argument of the translated function is also substituted; this function is zero for every argument, so that the vanishing and all the constants remain the same.

In case B, the elements `k_s=1+ι₀vl` fix the centre of the coset and its lattice. In M, `R_{k_s}Ξ=ψ(det s)^{-1}ϱ(s)Ξ`; the conjugate-linearity of Ξ↦L_Ξ is maintained on summing, so that one obtains exactly `L_{ϱ(η_{ψ,λ})Ξ}=0`. There is no need to replace η by its conjugate: the coefficient is already inside its argument. The literal mention of "linearity" must be read as additivity for this sum of weighted vectors. At Q, the surjectivity of the determinant of the hyperplane group and ψ≠1 annihilate the sum.

The verification of F2 for the general labels is `ppe:green`: the Harish–Chandra restriction of the squarefree label to GL1×GL(r−1) contributes only its linear roots. Pairing with ψ gives zero when its name is not a root. This concrete application is coordinated with the primary collation of Green/Zelevinsky in the spanning branch; it is not deduced from the rank-one case.

## 5. Tower and period

`ppe:transfer` is applied to `(X,V)` with `m_X=r+2p≤n`, at a split place outside the level. Moving the translations through the integral inverts the double coset; changing to the conjugate place again gives the required Hecke polynomial. Its factors have moduli `q^{m_X/2}` and `q^{n/2}`. Thus, for p≥1, the external factors do not vanish because their moduli are at most `q^{-p}<1`; the new root satisfies

`q^{m_X+1}|X′|=q^{(2r+2p+4−n)/2}≤1`.

The small-roots lemma dominates the sum over all the subspaces by `exp(1/q)<2`, valid also for q=2; it only needs the descent to be bounded. `ppe:bdd` uses R2/R3 and `pcx:mean` with l=A to cancel `ht(g)^A·δ^A`, where δ≪ht(g)^{-1}; this proof was reconstructed in AUXCORE and reread here at 4383–4411. It does not require rank one. The zero term uses the character shifted by υ₁ and a Schwartz evaluation in the mixed model, not a bounded evaluation in the Hilbert space.

`ppe:rallis` in general rank: the Fourier coefficient of Gram identity selects isometric frames; Witt gives a rational orbit with stabiliser U(V₂). Outside the level the integral frames are one orbit of the compact subgroup because their complement is unimodular and the extension is unramified. The norm of units and the residual trace justify the diagonalisation even in residual characteristic two. At the places of the level the compact indicators separate points; at infinity the restrictions of polynomials times a Gaussian are dense on the compact variety of frames. The continuous function of the period is zero at the identity, not merely almost everywhere.

For the last step of `ppe:main`, translating by g_s preserves the data outside Σ. Y₁ is multiplied by a kernel of W and the orthogonal sum of sources is used to obtain zero descent from H^{N″}. The factor of the kernel on V″ can be chosen non-zero for each fixed g, h: the finite data fix a discrete set of rational points, and a Gaussian concentrated at a point where the finite datum is not zero dominates the tail. Dividing by that value does not fix a uniform constant, nor does it require a hypothesis of non-vanishing of L. The factorisation over V″⊥V° uses source characters whose product is the original one and the same target character on both blocks, compatible with the V2 review of P53.

Result: `ppe:main` in general is reconstructed with the local precisions indicated, subject to the primary collation of the individually identified input F2. No new analytic obstacle of higher rank was detected on this route.

## 6. What remains separate for Gram

The algebraic identity 1150–1164 uses the determinant of the **compression** of U_ϑ to Z_ϑ. With G1, `Θ_ϑ*U_ϑΘ_ϑ=n_Aut H_°² |c′_ϑ|^{-2} Θ°*Θ°`; with `|c′_ϑ|²H_j(ϑ)=C_x`, one obtains the product of L-values with power d_j exactly as written. G2 guarantees positivity of C_j; invariance of Z_ϑ under U_ϑ is not presupposed. Integrality uses the resolution of the identity by the integral frame and the factor n_Aut; the conjugate bound uses cσc, and does not suppose that σ commutes with conjugation on all the coordinates of the forms.

This bookkeeping is reconstructed, but its inputs **po:exchange (three exchanges, sections pte/ptf/pfq) and po:span (psp/psq/psr/psv)** require their own closures. The compact rank1 proof of SW01 does not replace them. The closure map must show these obligations until they are audited by the assigned branches.

## 7. Closure of F2 by finite Mackey

The primary review of Green in the Selmer branch collated p.403 (product equal to parabolic induction), pp.436–437 and p.439, Theorems12–13. For the squarefree label c, each irreducible factor contributes a distinct cuspidal with partition (1); their product is the irreducible Ξ_c. There is no need to add a complete comultiplication formula as a black box.

Apply Mackey to the induction from those blocks and restrict by invariants of the radical of the parabolic of type (1,r−1). The double cells are parametrised by intersection matrices of flags. Their first row sums to one, so that it assigns exactly one dimension to one of the cuspidal blocks. If that block has degree d>1, its contribution contains the proper Jacquet module of type (1,d−1), which is zero by cuspidality. If it has degree one, a single cell survives, with character θ_α on GL1 and the product of the other blocks on GL(r−1); there is no index factor because the normalised average for invariants is used. The result is precisely the sum of `ppe:green`, with multiplicity one. For r=1 the second factor is the trivial group and the same count is immediate.

Hence, after this collation and the explicit Mackey deduction, **F2 and `ppe:main` in general are (a), reconstructed with the precisions of §§3–4**. The pending item that §5 kept on that input is discharged; the distinct obligations of §6 remain separate.
