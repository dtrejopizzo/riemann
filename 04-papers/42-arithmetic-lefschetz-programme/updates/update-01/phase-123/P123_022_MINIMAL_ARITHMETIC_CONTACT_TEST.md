# P123.022 — the minimal contact test and the integral-source obstruction

## Verdict

`PROVED-EXISTING-INTEGRAL-CONTACT` for the four cyclotomic complexes already
constructed in paper 42. `REFUTED` for recovering their nonzero integral
torsion by an additive contact functor from a purely C-linear category.

`OPEN` for constructing a multiplicative family in the repaired common
carrier whose derived diagonal contact is those complexes. P123.019–020
repair analytic operations but do not close B.

## 1. Reuse the existing actual derived intersection

Paper 42, equations `derivedWittContact` and `derivedWittContactModel`,
sets R=Z[T,T^-1] and constructs

    K_n^W=R/(Phi_n(T)) tensor_R^L R/(T-1).

The polynomial Phi_n is a non-zero-divisor in R. Resolving its quotient
by [R --Phi_n(T)--> R] gives

    K_n^W ~= [Z --Phi_n(1)--> Z],

in degrees -1,0. This is a genuine intersection of the cyclotomic
lambda-characteristic locus with the unit section in Spec R. It is not
already the intersection of Gamma_n with the diagonal of the semilocal
square.

| n | Phi_n(T) | Phi_n(1) | H^-1(K_n^W) | H^0(K_n^W) |
|---|---|---:|---|---|
| 2 | T+1 | 2 | 0 | Z/2 |
| 4 | T²+1 | 2 | 0 | Z/2 |
| 3 | T²+T+1 | 3 | 0 | Z/3 |
| 6 | T²-T+1 | 1 | 0 | 0 |

The lattice torsion degree is respectively log2, log2, log3, 0. Neither
these values nor their supports need to be rediscovered computationally.
For n=1 the differential is zero; it is a separate excess/identity object.

## 2. Integral torsion cannot be recovered additively from C-linear objects

### Proposition

Let C be an additive category in which p*id_X is invertible for every
object X and every positive integer p (in particular any Q-linear or
C-linear category). For an additive functor F:C -> D(Z), multiplication
by p is invertible on F(X), hence on every H^j(F(X)). Therefore no F(X)
is isomorphic to the nonzero complex [Z --p--> Z] for p prime.

### Proof

Additivity gives F(p*id_X)=p*id_F(X). Functors preserve inverses, and
(p*id_X)^-1 exists in C. Thus p*id_F(X) is invertible. Cohomology preserves
isomorphisms, so p acts bijectively on H^j(F(X)). On H^0([Z --p--> Z])=Z/p
it is the zero map on a nonzero group, a contradiction.

Equivalently, base change of [Z --p--> Z] to C is acyclic: p is invertible.
An underlying C-linear derived kernel contact therefore cannot itself
supply this integral torsion object. QED.

### Scope

The proposition does not forbid an integral or lattice category with a
complex realization. That realization may send a nonzero torsion object
to zero while a metrized determinant retains an arithmetic degree.
It also does not prohibit a scalar regularized trace or a nonlinear
construction using extra integral data. Such additional structure must be
constructed, however; it is absent from the pure C-linear kernel category.

Thus the repaired A_S^u is an analytic realization candidate, not by
itself the full arithmetic source demanded by B and RR.

## 3. A simple integral enlargement also fails multiplicative realization

Consider the integral cyclotomic lattices

    V_n=Z[T]/Phi_n(T), with automorphism T.

Since Phi_n(0)=1 for n>1, T is invertible over Z. Their fixed-contact cones
of 1-T recover the appropriate torsion degrees. But ordinary tensor of
these objects does not satisfy V_m tensor V_n ~= V_mn.

Indeed V_2 has rank one and T=-1. Its tensor square has rank one and T=+1,
whereas V_4 has rank two and T satisfies T²=-1. Their fixed cones likewise
differ: the tensor square has zero differential and free cohomology,
whereas the V_4 fixed cone has finite cokernel Z/2 and no kernel.

This refutes only the candidate that identifies correspondence composition
with tensor of these cyclotomic lattice objects. It does not refute Witt
Frobenius/Verschiebung as **endomorphisms of a larger source**, where
composition is a different operation. That distinction is indispensable.

## 4. Contact itself need not be a monoidal functor

The reduced contact law in paper 42 is

    P(a) star P(b)=H^0(P(a) tensor_Z^L P(b))=Z/gcd(a,b).

It gives P_m star P_n=P_mn for the listed cyclotomic values, but deliberately
forgets Tor. Full derived tensor of Z/p with itself has Tor_1=Z/p as well
as H^0=Z/p, unlike K_(p²)^W. The paper explicitly records this limitation.

It is therefore invalid to use the reduced law as the proof of a full
ambient derived-composition theorem. Conversely, failure of monoidality
of contact does not refute multiplicativity of the correspondences:
intersection with a fixed diagonal is not required to preserve tensor.

The target remains

    Gamma_m star Gamma_n ~= Gamma_mn          in a source category,
    LDelta* Gamma_n ~= K_n^W                  by a separate comparison.

No claim that LDelta* is monoidal is part of this test.

## 5. Prior failures to keep in view

The bounded source scan found these exact earlier controls:

- phase 114 `114_a_41_I7_WITT_GRAPH_DIAGONAL_EXCESS_NOGO.md`:
  ordinary Witt graph fixed locus contains the horizontal Spec Z component.
- `114_a_42_I7_STANDARD_DERIVED_FIXED_CONE_NOGO.md`:
  the tested reduced fixed cone has determinant degree zero.
- `114_a_43` through `114_a_45`:
  integral branch contacts and primitive layers exist, but their transport
  to a common moving correspondence remains separate.
- `114_a_133_I7_UNDECORATED_DIAGONAL_CHOW_NOGO.md`:
  scalar multiples of a single diagonal cannot retain both the exact
  multiplicative labels and Lambda contact.

Paper 42's `Gamma_n=(F_n,rho_n,T_n,P_n)` is a faithful decorated family.
Its cyclotomic contact is genuine in Spec R; its common-carrier diagonal
comparison is still missing. This note does not retract that restricted
construction.

## 6. Decision after the first test

The four integral contact complexes pass their original coefficient-level
test. The repaired analytic-only source fails the stronger B test by §2.
The simplest integral cyclotomic tensor replacement fails by §3.

Next investigate an integral exact correspondence category with Witt
endomorphisms and a geometric contact functor, together with a complex
analytic realization. It must explain the horizontal-excess removal and
retain full derived contact rather than decorate a scalar trace. The
semilocal algebra remains available as its possible analytic realization.

This decision occurs before full numerical completion or RR, exactly as
required by the approved viability plan. B is not closed, and no new
positive-sign mechanism for D has been obtained.
