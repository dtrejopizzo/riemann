# Construction 082 — Balanced defect with archimedean regularization

Status: formulas (1)–(2), domain and sign equivalence checked independently. It is a Birman–Schwinger type balance, not a new sign mechanism.

## Change with respect to the profile annihilators

BUILD079–081 did not reproduce the cancellation of the form on near-null vectors. Here that complete cancellation is included in the operator, without inverting the target form. This avoids fitting profiles, but it may transfer the sign obligation entirely; the residue is computed to check this.

Work in the primitive Hilbert space P_T. Let A be the self-adjoint operator associated with a_T, A_arch the one associated with the archimedean form compressed to P_T, and L=ΣΛ(n)/sqrt(n) U_log n. Put s=ΣΛ(n)/sqrt(n), with n<exp(2T), and

    β_T=1−C0+2s,
    B=A_arch+β_T I,
    P=β_T I+Q(L+L*)Q.

B≥(1+2s)I and P≥(1−C0)I>0, since ||L||≤s. They are operators on P_T; B is not the target form. One has A=B−P as an identity of forms and with bounded perturbation on Dom(B).

Define

    C=B^(-1/2) P B^(-1/2)≥0,
    V F=(I−C) B^(1/2)F
       =B^(1/2)F−B^(-1/2)PF,

for F in the form domain. The inverse only corresponds to the shifted archimedean part B, whose positivity is ensured in advance. On Dom(A), V=B^(-1/2)AF. No root or inverse of A nor its eigenvectors are used to define V.

## Exact square and residue

With x=B^(1/2)F,

    a_T(F)=<x,(I−C)x>,
    ||VF||²=<x,(I−C)²x>,
    ρ(F)=a_T(F)−||VF||²=<x,(C−C²)x>.                    (1)

In the original variables,

    ρ(F)=<F,PF>−<PF,B^(-1)PF>.                           (2)

All cross terms between contacts are present in PF and in the second term; they are not replaced by a sum of independent norms.

## Favourable diagnosis and logical limit

If F is an eigenvector of A with AF=λF, one obtains, only as a diagnosis,

    ||VF||²=λ²<F,B^(-1)F>≤λ²||F||²/(1+2s).

The candidate automatically suppresses every near-null direction with small operator residual, without choosing it in advance. A small Rayleigh quotient alone is NOT enough for this bound: AF must be controlled.

But C≥0 implies that C−C²≥0 if and only if C≤I. Moreover C≤I is equivalent to A≥0 by the first equality of (1). Since B≥constant>0, x ranges over all of P_T when F ranges over Dom(B^(1/2)); no subspace is missing in that equivalence.

Therefore this design resolves the extraction incompatibility on near-null eigenvectors, but it does NOT reduce the logical sign obligation. Proving ρ≥0 is exactly proving the contraction C≤I. That contraction is not assumed and (1) is not presented as a positivity proof.

## What an additional operation would be

Formula (2) leaves a concrete target: an arithmetic-archimedean identity controlling the pairing of PF with the positive Green function of B, keeping all cross terms. Defining that control as the optimal norm or refactoring I−C would be circular. The archimedean regularization is already written; an independent reason for the contraction is missing.

For falsifiers with positive weights, the same construction and identities exist after adapting s and P. In a negative window, C has a spectral direction above 1 and the residue also fails. That observation checks consistency; it does not yet identify an arithmetic law separating the true weight.

## Explicit expansion of the compensation of the two moments

Computation added for review. H0=L²(I) is distinguished from the primitive subspace. In H0 put

    B0=A_arch,full+β_T I, G0=B0^(-1),
    E(z+,z−)=z+ e+ + z− e−,
    Hpol=E*G0E.

B0≥(1+2s)I; G0 is positive and injective. E is injective and Hpol is a strictly positive 2x2 matrix. Define

    Gprim=G0−G0 E Hpol^(-1) E*G0.                        (3)

This is the extension by zero on P_T^perp of the inverse of the primitive compression B. Indeed, for a source f, u=Gprim f satisfies E*u=0 and B0u=f−E Hpol^(-1)E*G0f. Testing against any h∈P_T, one obtains b_B(h,u)=<h,f>; coercivity gives uniqueness. Moreover Gprim E=0 and E*Gprim=0. Gprim is not confused with QG0Q, which in general is different.

With P0=β_T I+L+L*, for F∈P_T formula (2) becomes

    ρ(F)=<F,P0F>−<P0F,G0P0F>+v(F)*Hpol^(-1)v(F),       (4)
    v(F)=E*G0P0F.

The last contribution is manifestly non-negative, but of rank at most 2. The pointwise kernel of Gprim is not assumed positive: positivity as an operator and positivity of the kernel are different properties.

The two functionals can be written without applying the inverse to the arithmetic source: kσ=G0eσ depends only on Arch, the window and β_T. Then

    vσ(F)=<kσ,P0F>=<rσ,F>,
    rσ=β_T kσ+Σ_n Λ(n)/sqrt(n)(U_log n+U_log n*)kσ.       (5)

All contacts and the two constraints appear in (4)-(5), with their cross terms preserved. The pending problem is to dominate the defect <P0F,G0P0F>−<F,P0F> by these two functionals for all F∈P_T. It is not claimed that rank two suffices for a dimensional reason: precisely that domination is what remains to be proved.

For F such that v(F)=0, the compensation disappears. Any proof based on (4) must therefore control the complete defect also on that subspace; it cannot use the mere positivity of Hpol^(-1) as a conclusion. This fixes a verifiable condition for a later cancellation attempt.


## Scope of the review

The general bound is ||VF||≤||AF||/sqrt(1+2s); for AF=λF+r, it is ≤(|λ|||F||+||r||)/sqrt(1+2s). Damping of all tests with small Rayleigh quotient is not deduced without controlling their operator residual.

Verified conceptual antecedent: P46 subsec:wh-det/thm:wh-pencil. Its trace-class conclusion is not imported: P≥(1−C0)I in infinite dimension is not trace class. The operator-order equivalence written here does not require that property.

The formula for the restricted Green function (3) was also confirmed as exact elimination of the two constraints. Exhibiting its positive rank-two term does not prove the pending domination in (4).
