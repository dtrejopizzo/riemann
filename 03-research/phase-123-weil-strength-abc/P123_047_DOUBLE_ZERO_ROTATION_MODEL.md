# P123.047 — The two-prime double-zero complement as a rotation groupoid

Date: 2026-09-05. Status: PROVED for the explicit groupoid reduction,
its compact transversal algebra and trace. Transport of the desired
relative shadow to this complement remains open.

## 1. Compute the actual complementary action

Take S_f={p,q}, p!=q, and let a=log p, b=log q. The closed complement
F in P123.045 is exactly

    F={(x_infinity,0,0): x_infinity>0} ~= R,

in logarithmic real coordinate t. The action of Gamma=p^Z q^Z is

    (m,n)t=t+ma+nb.                              (1.1)

The ratio b/a is irrational: a rational relation would give an equality
of positive powers of the distinct primes p and q. Thus the subgroup
aZ+bZ is dense in R. For example, the pigeonhole principle applied to
fractional parts of j b/a gives arbitrarily small nonzero elements of
Z+(b/a)Z; integer multiples of such elements approximate any real number.

The action (1.1) is free but not proper, and its ordinary orbit quotient
is not a Hausdorff space. This is an actual remaining part of the source,
not a compact boundary orbit of the type in P123.041.

## 2. An explicit compact transversal presentation

First divide by aZ. This subgroup acts freely and properly, with quotient
circle C_a=R/aZ. The residual generator q acts by rotation

    r_b:[t] -> [t+b].                            (2.1)

Retaining the action groupoids gives the equivalence

    [R/(Z times Z)] ~= [C_a/Z],                  (2.2)

where the right side uses (2.1). One can verify (2.2) directly by pulling
the right groupoid back along the covering R -> C_a. An arrow between
lifts t and t' with rotation label n obeys

    t'=t+nb+ma

for a unique integer m. Thus the pulled-back arrows, with composition,
are exactly those of (1.1). Local sections of the covering recover all
objects and arrows, which proves the groupoid equivalence. The integer
m is retained in this pullback; it has not been silently discarded.

This is a concrete presentation of the double-zero source by a compact
transversal with irrational return rotation. It does not assert an
isomorphism of the original rapid crossed-product algebra with a chosen
completed transversal algebra; the required equivalence of completions
and correspondence categories must still be established.

## 3. Construct the transversal convolution algebra and trace

On C(C_a) let alpha_n f(t)=f(t-nb). Form the algebra of finite sums

    B_alg={sum_n f_n V^n},
    (f_n V^n)(g_m V^m)=f_n alpha_n(g_m) V^(n+m),
    (f_n V^n)*=alpha_(-n)(conjugate(f_n)) V^(-n).

Its unit is the constant function at label zero. The normalized Haar
functional

    tau(sum_n f_n V^n)=(1/a) integral_0^a f_0(t)dt  (3.1)

is a trace. Indeed the identity coefficient of a product is
sum_n f_n(t)g_(-n)(t-nb); translation invariance of circle Haar, followed
by replacing n with -n, makes its integral equal to that of the reversed
product. Furthermore

    tau(z* z)=sum_n (1/a) integral_0^a |f_n(t)|²dt. (3.2)

Thus tau is positive and faithful on the algebraic algebra, and tau(1)=1.
This supplies a nonzero trace-bearing model for the complementary stratum.
It does not prove that the particular Weil relative shadow equals tau.

For an explicit topological version, use

    B_rapid={ (f_n): sum_n ||f_n|| exp(k|n|)<infinity
                              for every integer k>=0 }.

The submultiplicative weights and isometry of alpha prove completeness,
continuous crossed convolution and involution by the same estimates as
P123.019. The trace is continuous, |tau(z)|<=sum_n ||f_n||, and (3.2)
extends by absolute convergence. These exponential weights specify a
transversal algebra; no unproved assertion that they are automatically
the image of the original two-label height completion is being made.

If U(t)=exp(2 pi i t/a), its relation with V is

    V U = exp(-2 pi i b/a) U V.                   (3.3)

Equation (3.3) is the irrational rotation relation, now derived from the
original two-prime zero stratum. It shows why treating that stratum as
another compact homogeneous orbit with discrete real period loses its
actual return action.

## 4. External action and the failure of the closed-stabilizer model

On this stratum the finite unit coordinates act trivially. The normalized
external real coordinate s acts by t -> t+s; on the transversal algebra
it translates all coefficient functions and fixes V. It commutes with
alpha and preserves tau. For example the external class of a local
p-uniformizer has s=-a and acts as identity on C_a, while that of a
q-uniformizer has s=-b and acts by the inverse return rotation.

Set-theoretically the stabilizer of a point of F/Gamma inside
G=R times Z_p^* times Z_q^* is

    K_F=(aZ+bZ) times Z_p^* times Z_q^*.

It is not closed. Hence the compact homogeneous-space induction and
quotient-Haar argument used for a single zero cannot be repeated with
this stabilizer. The rotation groupoid above retains the missing return
arrows and is an explicit replacement for that attempted construction.

## 5. The precise next comparison

The first multiple-zero complement now has a concrete groupoid model,
convolution algebra, external action and nonzero normalized trace.
These data do not determine its contribution to the desired global
relative trace. In particular neither a zero contribution nor a copy of
tau may be inserted without a comparison from the source shadow.

The next load-bearing operation is to transport the rapid extension of
P123.045 through a compatible groupoid/correspondence realization and
derive the boundary map seen by its regularized trace. This must explain
how the double-zero term combines with the single-zero cutoff characters
of P123.046. More-prime strata and the real-zero boundary remain in scope.
The positivity of (3.2) is ordinary positivity of a trace; it supplies
no Weil-form sign theorem for D.
