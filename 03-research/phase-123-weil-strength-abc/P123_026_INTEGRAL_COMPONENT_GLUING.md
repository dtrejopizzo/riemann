# P123.026 — retain component gluing before analytic realization

Date: 2026-09-05.

## Status and relation to the corpus

`PROVED-IN-REPOSITORY`: the two-block integral gluing sequence below and
its four explicit finite defect modules. This identifies data that a
componentwise realization must retain. It does not construct that
realization or close A/B/C/D.

Phase 107.160 represents rooted labels by disjoint cyclotomic components.
Phase 107.218 proves that rooted inclusions and cellular power transitions
are different systems. P123.025 likewise distinguishes full power pullback
from top primitive extraction. The construction here retains the integral
intersection between the primitive component and its complement, before
passing to separated components. It does not change those transition maps.

## 1. An exact gluing sequence

Use R, P=Phi_n, Q=(T^n-1)/P, V, W, M from P123.025, with n>1.
Define G_n=R/(P,Q). There is a canonical exact sequence

    0 -> M -> V direct-sum W -> G_n -> 0,             (1.1)

where the first arrow is simultaneous reduction and the second is the
difference of reductions modulo (P,Q).

Indeed (P) intersection (Q)=(PQ): in the UFD Z[T,T^-1], P and Q have
no common irreducible factors, so divisibility by both implies divisibility
by their product. This proves injectivity. If representatives a,b have
a-b=P u+Q v, the element a-P u=b+Q v lifts the pair, proving exactness
in the middle. The last map is surjective.

G_n is finite: it is the cokernel of multiplication by Q on the finite
free lattice V. That multiplication is invertible over Q since P and Q
have disjoint roots. Thus its integral matrix has nonzero determinant.
The equality

    |G_n| = |det(Q(T) acting on V)|

is the ordinary lattice index formula. No rational projector reconstructs
this finite cokernel by itself.

Equivalently M is the ring fibre product V times_(G_n) W. The two maps
to G_n are surjective and the preceding exactness proves this assertion
on elements as well as multiplication. This is a two-block partial
separation; W need not itself be normal. We do not identify V direct-sum W
with the full normalization when Q is reducible.

## 2. Four explicit defects

Reduce Q in the integral power basis of V:

| n | Q modulo P | multiplication matrix | G_n |
|---|---|---|---|
| 2 | -2 | [-2] | Z/2 |
| 3 | T-1 | [[-1,-1],[1,-2]] | Z/3 |
| 4 | -2 | [[-2,0],[0,-2]] | Z/2 direct-sum Z/2 |
| 6 | -2(T+1) | [[-2,2],[-2,-4]] | Z/2 direct-sum Z/6 |

For the two-dimensional matrices, the first Smith invariant is the gcd
of all entries and the second is the absolute determinant divided by
that gcd. Their determinants have absolute values 3,4,12, respectively.
These gluing modules are not the unit-contact objects. In particular
G_6 is nonzero although the primitive unit contact at label 6 vanishes.
The latter therefore cannot serve as a complete record of integral gluing.

## 3. Derived unit contact of the defect

All terms of (1.1) are perfect R-complexes: this is already true of
M,V,W, and follows for G_n from their triangle. Apply
J(E)=E tensor_R^L Z, T acting on Z as 1. It gives a specified triangle

    J(M) -> J(V) direct-sum J(W) -> J(G_n) -> J(M)[1].

This triangle is necessary bookkeeping for an exact realization of the
component decomposition; replacing M by the direct sum omits its third
term and its attaching map.

For n=6 the defect is nevertheless invisible at the unit even derivedly.
In G_6, Phi_6(T)=T^2-T+1=0, so T(T-1)=-1. Consequently T-1 is an
automorphism on G_6. The free resolution of Z=R/(T-1) computes J(G_6)
as [G_6 --T-1--> G_6], which is acyclic. This proves directly that
nonzero integral gluing can lie away from the distinguished unit contact.
It is consistent with, and sharper than, comparing only the group orders.

## 4. Next acceptance condition

A candidate realization built on separated rooted charts must either
retain the fibre-product gluing and its exact triangle, or prove that the
chosen target legitimately annihilates it while retaining the arithmetic
determinant information required by B. Complexification annihilates the
finite G_n, so its existence alone cannot provide that retained information.

This adds a concrete diagram to the missing comparison, rather than a
new decorated correspondence family. The still-required theorem is a
single correspondence construction with composition, these integral
attaching maps, diagonal contact, and the analytic action. Neither the
fibre-product identity nor a list of matching contact values supplies it.

No novelty is claimed for the elementary exact sequence or Smith forms.
