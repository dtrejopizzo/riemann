# P123.023 — a compatible scalar test system on normalized class groups

## Status

`PROVED-IN-REPOSITORY` for the scalar pullback/convolution system below and
its algebraic identification with scalar Bruhat tests on the full normalized
class group. This corrects the direction and meaning of test transitions.
It does not prove an embedding of these tests in a faithful Fell carrier,
a trace/intersection comparison, or full completed bimodule descent.

## 1. Why the class embeddings do not give test embeddings by zero

P123.020 gives i_ST:H_S -> H_T by appending 1 in new unit factors.
If a prime is added, {1} is not open in Z_p^times. Extension by zero of a
nonzero test along i_ST is therefore not locally constant in that new
coordinate. It is not a Bruhat test on H_T.

There is instead a continuous **projection of normalized groups**

    pi_TS:H_T -> H_S

which forgets the new unit coordinates. This is not the ill-defined raw
projection A_T^times/Gamma_T -> A_S^times/Gamma_S: normalize first as in
P123.020. It has compact kernel U_new=product Z_p^times.

## 2. Pullback preserves the scalar algebra

Normalize Haar measure on every Z_p^times to total mass 1 and use the same
multiplicative real Haar measure in every chart. Let D(H_S) consist of
compactly supported functions, smooth in the real coordinate and locally
constant at a fixed finite level in the compact unit factors.

Define

    P_ST h = h compose pi_TS.

Its support is supp(h) times U_new, hence compact. It is smooth/locally
constant in the required sense, and P_TU P_ST=P_SU.

For product Haar measure, Fubini on compact supports gives

    (P_ST f * P_ST g)(x,u)
      =integral_HS integral_Unew f(y) g(y^-1 x) dv dy
      =P_ST(f*g)(x,u).

Inversion and complex conjugation commute with projection, so group-star
is preserved. The alternative half-density dagger is also preserved when
it differs by a character of the real modulus: that character is unchanged
by pi_TS. No convention for dagger may be silently changed in a trace.

At each fixed compact real support and finite unit level, P_ST is a
continuous linear inclusion of the corresponding smooth test steps, with
the same derivative seminorms. Its continuity for the test inductive-limit
topology follows from the **linear** universal property. No assertion about
joint bilinear LF continuity is deduced merely from that property.

## 3. Global scalar tests and the inverse system

The full normalized class group is

    H=R^times times product_p Z_p^times

in the positive-unit convention. Every compact unit group open subgroup
contains a basic open subgroup involving only finitely many primes and
finite congruence levels there. Thus a Bruhat test on H with a common open
unit stabilizer factors through H_S for some finite S and finite levels.
Conversely every P_S h is a Bruhat test on H. Therefore

    union_S P_S D(H_S)=D(H)

as scalar test algebras. The test topology may be defined by the same
compact-support/finite-level steps on both sides, giving the identical
inductive-limit topology. This is not the claim that the direct-limit
**group** of append-one embeddings is H.

The assertion concerns the Bruhat test class just defined, with uniform
local constancy on compact support. It does not concern all continuous
functions or arbitrary coefficient-valued smooth sections.

## 4. Compatibility with the repaired coefficient system

The global normalized group acts on A_S^u through its S-coordinates.
For h_T in H_T, each added component is a unit, and hence preserves 1_Zp.
Thus

    beta_(h_T) j_ST = j_ST beta_(pi_TS(h_T)).

This is a compatible system of actions even for h_T outside the append-one
image. For scalar compact tests, define on each A_S^u the integrated action

    Theta_S(f)(b)=integral_HS f(h) beta_h(b) dh.

It exists in the complete Frechet space: beta is continuous and isometric,
f has compact support, and each seminorm is bounded by ||f||_1 p_k(b).
Product Haar normalization and the displayed equivariance give

    Theta_T(P_ST f) j_ST = j_ST Theta_S(f).

Fubini gives Theta_S(f*g)=Theta_S(f)Theta_S(g). These are integrated
operators on the **coefficient algebra**; they are not identified here
with Meyer's operators on the Poisson quotient or with categorical trace.
A faithful scalar element in a Fell algebra also does not follow.

## 5. A concrete obstruction to extending all bimodule morphisms

For S={infinity}, Gamma_S^+={1}, so A_S^u=C_0(R)^+ is commutative. A compactly
supported nonzero t in C_0(R) defines an identity-bimodule endomorphism
x |-> x t. Add p. Its coefficient image is

    j_ST(t)(x,y)=t(x)1_Zp(y).

But

    alpha_p(j_ST(t))(x,y)=t(x/p)1_(p Zp)(y)

is different: take y a p-adic unit and x with t(x)!=0. Hence j_ST(t) does
not commute with U_p and is not an endomorphism of the target identity
bimodule. This proves that P123.020's gauge-generated Hom restriction is
necessary for the proposed map, not merely an unverified technicality.

A larger correspondence category needs a different change-of-coefficients
construction with its tensor/unit comparison proved. The scalar test
system above does not resolve that obstruction.
