# P123.025 — integral cyclotomic filtration and its contact triangle


## Status

`PROVED-IN-REPOSITORY` for the exact integral filtration, its derived
unit-contact triangle and the explicit connecting map below. It exhibits
the torsion contact as the cokernel of a comparison between two horizontal
Tor lines, rather than as a degree attached to an analytic object.

`PROVED` for the effect of power-map pullback on the cyclotomic components.
It shows why the primitive component alone is not stable under the naive
multiplicative action. This is a source-side construction and a constraint
on the missing functor; it does not identify contact with the diagonal of
A, close B, or prove a Hodge sign.

## 1. The integral category and filtration

Let R=Z[T,T^-1]. Work in Perf(R), retaining the ordinary integral module
models below. For n>1 write

    P_n(T)=Phi_n(T),
    Q_n(T)=(T^n-1)/Phi_n(T),
    V_n=R/(P_n),   M_n=R/(T^n-1),   W_n=R/(Q_n).

All polynomials are monic, have constant term a unit, and are
non-zero-divisors. Thus these are finite free Z-modules with invertible
T-action and perfect R-modules. They fit into the exact sequence

    0 -> V_n --multiply by Q_n--> M_n -> W_n -> 0.    (1.1)

Injectivity follows by cancellation of Q_n in the domain R:
Q_n f belongs to (P_n Q_n) exactly when f belongs to (P_n). The quotient
is R/(Q_n). No integral Chinese-remainder splitting is used.

The lattice V_n is therefore realized as an actual submodule of the full
root-of-unity lattice M_n, with a specified integral extension class. This
is stronger than choosing a rational eigenspace and then forgetting the
integral gluing. It is still not a multiplicative correspondence family.

## 2. Apply the derived unit-section functor

Define the exact derived functor

    J:Perf(R) -> Perf(Z),   J(E)=E tensor_R^L R/(T-1).

For any monic polynomial A(T) as above, the resolution [R --A--> R]
shows J(R/(A))=[Z --A(1)--> Z], in degrees -1,0. Set

    a_n=Phi_n(1),  which is a positive integer for n>1.

Since Q_n contains T-1,

    J(V_n)=[Z --a_n--> Z],
    J(M_n)=[Z --0--> Z],
    J(W_n)=[Z --0--> Z].                              (2.1)

Apply J to (1.1), obtaining a distinguished triangle. The quotient map
M_n -> W_n is lifted between the displayed R-free resolutions by

    degree -1: multiply by P_n,
    degree  0: identity.

It is a chain map because Q_n P_n=T^n-1. After J it induces multiplication
by a_n in degree -1 and the identity in degree 0. The injection V_n -> M_n
is lifted by identity in degree -1 and multiplication by Q_n in degree 0.
Their composite is null-homotopic (with degree-zero-to-degree-minus-one
homotopy equal to the identity), as required by the triangle.

The resulting long exact cohomology sequence is

    0 -> Z --a_n--> Z --boundary--> Z/a_n
        -> Z --id--> Z -> 0.                          (2.2)

The boundary map is reduction modulo a_n, with the sign fixed by the
usual triangle convention. In particular the nonzero torsion is exactly
the cokernel of the map between the two horizontal Tor lines.

This supplies the comparison map, not merely its numerical determinant.
Acyclicity after complexification follows because a_n becomes invertible;
it is consistent with P123.022 and loses precisely the integral cokernel.

## 3. The minimal arithmetic cases

| n | P_n | Q_n | map of horizontal H^-1 lines | resulting contact |
|---|---|---|---:|---|
| 2 | T+1 | T-1 | 2 | Z/2 |
| 4 | T²+1 | T²-1 | 2 | Z/2 |
| 3 | T²+T+1 | T-1 | 3 | Z/3 |
| 6 | T²-T+1 | (T-1)(T+1)(T²+T+1) | 1 | 0 |

Thus the mixed label 6 has an isomorphism between its horizontal Tor
lines and no torsion contact, whereas the prime-power labels have a
nontrivial finite cokernel. This is an exact integral excess comparison
at the unit section of Spec R. It does not assert that W_n is the physical
horizontal component of the semilocal graph-diagonal intersection: that
identification is still missing.

For the standard lattice bases the torsion degree is log|a_n|. The
triangular determinant isomorphism identifies it with the index of the
map in (2.2). This is a local lattice determinant calculation; no global
RR, metric descent or Fredholm comparison is inferred.

## 4. Why an integral primitive projector would erase relevant gluing

Sequence (1.1) splits as R-modules exactly when (P_n,Q_n)=R.
Indeed a section of M_n -> W_n sends 1 to u with u=1 modulo Q_n and
Q_n u=0 modulo P_n Q_n. The second condition forces u=P_n v. Therefore
P_n v=1 modulo Q_n, which is the Bezout condition. Conversely that
condition constructs the section.

If n=p^k, evaluation at T=1 sends the ideal (P_n,Q_n) into (p), so it
cannot contain 1. The extension is not split integrally. Over Q, the two
polynomials have disjoint root sets, and a rational splitting exists.
That passage can lose precisely the integral torsion seen by (2.2).

For n=p the obstruction is especially elementary. In
M_p=Z[T]/(T^p-1), a T-invariant element is c(1+T+...+T^(p-1)). Its
augmentation is p c. Thus the augmentation M_p -> Z has no T-equivariant
integral section: it would require p c=1.

This does not prove that every non-split extension is detected at T=1.
For n=6 the contact there is zero even though other component collisions
can remain. One must keep the full extension, not just its unit contact.

## 5. What the multiplicative power maps actually do

Let pi_m:G_m -> G_m be T |-> T^m. Its ring map makes R a free rank-m
module over the source copy, with basis 1,T,...,T^(m-1). Hence its pullback
is exact on the module sequences considered here, preserves perfectness,
and satisfies pi_l^* pi_m^* ~= pi_(lm)^*.

On full root-of-unity lattices it gives

    pi_m^* M_n ~= M_(mn).                             (5.1)

On a primitive component the actual result is

    pi_m^* V_n = R/(Phi_n(T^m)),                       (5.2)

where

    Phi_n(T^m)
       = product_{d : d/gcd(d,m)=n} Phi_d(T).         (5.3)

All listed d divide mn. To prove (5.3), a characteristic-zero root z of
order d satisfies that z^m has order d/gcd(d,m). Thus the two sides have
exactly the same simple roots; both are monic, yielding equality over Z.

The first discriminating examples are

    pi_2^* V_2 = V_4,
    pi_2^* V_3 = R/(Phi_3 Phi_6),
    pi_3^* V_2 = R/(Phi_2 Phi_6).                     (5.4)

The latter two are integral extensions, not automatically direct sums.
For example multiplication by Phi_3 supplies

    0 -> V_6 -> pi_2^* V_3 -> V_3 -> 0.

So the full power-pullback action composes, but it does not act by
V_n |-> V_mn on every primitive component. The extra components are
forced by actual geometry. Retaining only V_mn requires an additional
filtered/subquotient construction with its own coherence theorem.

This distinguishes ordinary geometric power pullback from an operator
that shifts a specially chosen cyclotomic basis. A notation 'V_m' for both
does not identify them. Deninger's geometric Witt correspondence theorem
provides a relevant comparison target, but its maps must be used with
these actual pullback multiplicities. See
[Deninger, Theorem 5.1 and Proposition 5.2](https://arxiv.org/html/2508.05329v1#S5).

## 6. Consequence for the common-source problem

### A necessary compatibility test at the unit

The unit section is fixed by every power map. Derived tensor associativity
therefore gives a natural isomorphism

    J(pi_m^* E) ~= J(E)    for E in Perf(R).          (6.1)

Indeed the composite ring map R --T->T^m--> R --T->1--> Z is
the original evaluation at 1. In particular the contact of the full
pullback of V_n is [Z --Phi_n(1)--> Z], independent of m.
For n=3,m=2 it is Z/3, whereas J(V_6)=0; for n=2,m=3 it is
Z/2, again whereas J(V_6)=0. In the first example the triangle
V_6 -> pi_2^* V_3 -> V_3 explains exactly where the surviving contact
lies: after J, the last arrow is an isomorphism.

Consequently extracting the top primitive component cannot both replace
pi_m^* V_n by V_mn and preserve its unit-contact complex in general.
This refutes that particular compatibility requirement, not a filtered
correspondence theory. Such a theory must specify the extra-component
triangle and how its contribution changes contact. A contact-preserving
projection is already impossible in the minimal mixed case.

### Remaining construction

There is now a concrete integral candidate diagram:

    full root lattice M_n
        -> canonical exact primitive filtration (1.1)
        -> derived unit-section triangle (2.1)
        -> horizontal map a_n and finite contact.

The full lattices admit the multiplicative action (5.1), while the
primitive contact retains the integral extension class. What is not yet
constructed is a correspondence/shadow formalism in which that action and
that primitive extraction become the required single diagonal-contact
operation, compatible with composition and the analytic realization.

This is the next obligation to attack. It cannot be bypassed by replacing
(5.2) with V_mn, splitting over Q, or imposing the reduced H^0 product.
A proof would have to retain the filtered extension data and account for
all components in (5.3).

## Verification scope

The accompanying verifier checks polynomial identities, contact matrices
and power-pullback component formulas with exact integer arithmetic.
The proofs of the integral exact sequence and of (5.3) apply to all n,m
in their stated ranges; finite checks are only regression evidence.
No novelty claim is made for this elementary cyclotomic/derived algebra.
