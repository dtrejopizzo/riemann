# P123.061 — Integral deformation from power maps to normal dilation

Date: 2026-09-05. Status: PROVED for the composable polynomial family
and its primitive relative-fiber contact. Trace specialization and the
global diagonal comparison remain open.

## 1. A single integral family of composable morphisms

Over Z[t], on the affine coordinate z, define

    F_n(t,z)=((1+tz)^n-1)/t
            =sum_(j=1)^n binomial(n,j)t^(j-1)z^j.

The second expression defines the polynomial at t=0, so no inversion
of t is part of the construction. Direct substitution gives

    1+t F_n(t,z)=(1+tz)^n,
    F_m(t,F_n(t,z))=F_(mn)(t,z).                 (1.1)

For t invertible this is the power map w -> w^n in coordinate w=1+tz.
Restricting to the open set where w is invertible gives its G_m version.
At t=0 it specializes to z -> nz, the normal dilation of P123.060.
The zero section is fixed for every t, and its derivative is always n.
Thus the pulled-back ramification cotangent complex along that section
is [Z[t] --n--> Z[t]], with the transitivity maps induced by (1.1).

## 2. Carry the primitive relative fiber through the same family

For n>1 set

    P_n(t,z)=Phi_n(1+tz).

Cyclotomic factorization gives the integral identity

    F_n(t,z)=z product_(d|n,d>1) P_d(t,z).        (2.1)

Hence P_n cuts out the primitive factor of the relative fiber F_n=0.
Its derived intersection with the zero section z=0 is computed by the
Koszul resolution for P_n, which is a nonzero divisor in Z[t,z]:

    K_prim(n,t)=[Z[t] --Phi_n(1)--> Z[t]].       (2.2)

This is constant as a perfect complex over Z[t]. At any specialization
t=c its derived pullback is [Z --Phi_n(1)--> Z]. For n=2,4,3,6 this
gives Z/2,Z/2,Z/3,0 in degree zero and no degree -1 homology, matching
the previously constructed primitive contact complexes.

In particular the four defining polynomials are

    P_2=2+tz,
    P_4=2+2tz+t²z²,
    P_3=3+3tz+t²z²,
    P_6=1+tz+t²z².

These formulas exhibit the contact through the deformation itself;
the value is not inserted as an independent label weight.

## 3. Primitive data survive as vertical structure at the normal fiber

At t=0, P_n becomes the constant Phi_n(1). For a prime power n=p^k,
its primitive relative-fiber factor is therefore the vertical scheme
Spec((Z/p)[z]) in the normal special fiber. Its intersection with z=0
retains Z/p. For a mixed n with Phi_n(1)=1, that factor is empty.

Thus the primitive factor does not specialize to a finite collection
of complex normal eigenpoints. It can acquire a vertical component
over p, invisible after complex scalar extension. This explains how
the integral primitive contact can persist in the same deformation
whose generic analytic normal action is dilation by n.

The ordinary specializations here agree with derived specialization:
P_n(0,z)=Phi_n(1) is nonzero in Z[z], so t is a nonzero divisor modulo
P_n. More directly, (2.2) is a complex of free Z[t]-modules, and its
derived specialization is computed term by term. No flat finite-rank
orbit family across t=0 is inferred; the vertical degeneration is real.

## 4. Preserve the distinction from fixed graph contact

The fixed graph equation for the family is F_n(t,z)-z=0. Its normal
specialization is (n-1)z=0. The primitive factor (2.1) instead belongs
to the relative fiber F_n(t,z)=0. Therefore (2.2) does not contradict
the mismatch proved in P123.060 and is not a quasi-isomorphism to the
transverse fixed complex [Z --n-1--> Z].

What has been constructed is a common integral deformation containing
both the power-map ramification contact and the composable normal action.
It supplies an explicit route for a relative specialization comparison,
while showing exactly which primitive vertical information that comparison
must retain. Composition of F_n is proved by (1.1); a monoidal primitive
extraction n -> P_n is not claimed, consistently with the earlier divisor
and pullback calculations.

## 5. Remaining B/C comparison

To obtain the intended bridge, the source shadow must transport this
relative-fiber contact through the deformation and relate it to the
normal relative trace, with its graph/diagonal and excess operations
specified. The polynomial identities and constant contact complex do
not prove invariance of a regularized analytic trace under t, nor supply
a missing global mixed RR theorem. They do provide a concrete integral
family on which that specialization claim can now be formulated and
tested without identifying the incompatible differentials n and n-1.
