# P123.116 — Boundary Gram curvature at every amplitude and its fixed kernel

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY, conditional only on
explicit operator and stabilization constructions P123.110–115 on their
declared test domains. This is not a metric comparison with arithmetic RR.

## 1. Statement and domain

Fix a finite-dimensional complex space V of external Bruhat tests, a
base test F in the same fixed support/conductor domain, and directions
U,V_1. Choose the normal cutoff L sufficiently large for the entire
span of these tests and their pairwise products. P123.110–115 then
stabilize the endpoint Gram coefficients simultaneously. In particular
h(F+zU+wV_1) is independent of all larger L for every complex z,w.
No bound on their amplitudes is required.

At this fixed cutoff regard

    X=X_L(F): E_L H -> (1-E_L)H,
    A=X_L(U), C=X_L(V_1),
    P=1+X*X, Q=1+XX*.

All three off-diagonal operators are Hilbert–Schmidt. P and Q are
bounded positive invertible operators on their respective Hilbert
spaces. The potential Phi(F)=log det(P) has Levi form

    K_F(U,V_1) = Tr(P^-1 C* Q^-1 A).                       (1)

The convention is linear in U and conjugate linear in V_1. Formula
(1) is exact at every amplitude, not just a Taylor formula at zero.
Its value is independent of sufficiently large L.

## 2. Differentiation in trace norm

Products of Hilbert–Schmidt operators are trace class. Consequently
P(z,w)-1 is a quadratic, trace-norm smooth function of z,w and their
conjugates. In a neighborhood of any base point P_0, write

    P(z,w)=P_0 [1+P_0^-1(P(z,w)-P_0)].

The second factor is near the identity in operator norm, and its
trace-class perturbation admits the convergent logarithmic trace
series. Differentiating this series and cyclically permuting a
trace-class factor gives d log det(P)=Tr(P^-1 dP).
This justifies differentiation at every base point without assuming
that X is small. Positivity fixes the real logarithm of det(P).

At z=w=0 for X(z,w)=X+zA+wC,

    partial_z P=X*A,
    partial_bar_w P=C*X,
    partial_z partial_bar_w P=C*A.

Thus the mixed derivative of log det(P) is

    Tr(P^-1 C*A - P^-1 C*X P^-1 X*A)
       =Tr(P^-1 C* [1-X P^-1 X*] A).

The identity 1-X(1+X*X)^-1 X*=(1+XX*)^-1 follows by
multiplication by Q. This proves (1). Every displayed trace contains
a product of two Hilbert–Schmidt factors and bounded factors, so its
cyclic uses and its derivatives are legitimate.

## 3. Positivity and the kernel at every base point

For a direction U, formula (1) becomes

    K_F(U,U)=||Q^-1/2 X_L(U) P^-1/2||_HS^2.               (2)

In particular Phi is plurisubharmonic on every finite-dimensional
affine test slice, at all amplitudes. Since P^-1/2 and Q^-1/2 are
boundedly invertible, its zero directions are exactly

    ker K_F = {U: X_L(U)=0}.                              (3)

They do not depend on F. More quantitatively,

    (1+||X_L(F)||^2)^-2 ||X_L(U)||_HS^2
       <= K_F(U,U) <= ||X_L(U)||_HS^2.                    (4)

For the lower bound, recover X_L(U) by multiplying the operator in
(2) on the left and right by Q^1/2 and P^1/2; both norms are at most
(1+||X_L(F)||^2)^1/2. The upper bound uses that both inverse square
roots are contractions. At F=0, this recovers exactly P123.115:
K_0(U,V_1)=B(U,V_1^*).

Because h on an entire affine test slice has already stabilized,
its derivatives (1) have stabilized as well. Alternatively, all
cross-Gram coefficients are fixed endpoint operators on that slice.
No differentiation of a merely pointwise limit is being used.

## 4. Semilocal transport and holomorphic changes of frame

The prescribed scalar pullback of P123.115 gives X_T=J X_S J*,
and the same identity for A,C. On the orthogonal complement of the
range of J the Gram operators are identity. Taking the trace of
(1) therefore gives exactly K_T=K_S on pulled-back directions.
The argument applies to unitary section changes with transported
cutoffs, with the existing triple compatibility.

Multiplying the metric h^-1 by |g(F)|^2 for a nowhere-zero
holomorphic g changes its potential by -2 Re log g locally. This has
zero Levi form. It cannot change (1), (3), or (4). In particular a
holomorphic relative-determinant factor cannot repair a failure of
composition stability of the curvature kernel.

## 5. The local normal obstruction persists at every amplitude

Apply the same computation to the local normal test algebra in
P123.112; this does not assume that every such test lifts to an
external scalar test. For its nontrivial unit-character projector
e_chi and valuation shift v_chi,

    X_L(e_chi)=0,
    ||X_L(v_chi)||_HS^2=1,
    e_chi*v_chi=v_chi.

The norm assertion is also immediate from the other orientation
of the shift defect: Tr(I_n-T_n* T_n)=1. Hence e_chi is a null
direction for the Gram curvature at EVERY base test f, while v_chi
is non-null at EVERY base test f, by (4). For this unchanged local
algebra the curvature kernel is not an ideal at any base point.

It follows that the vector-space quotient by these null directions
cannot inherit the original convolution product: [e_chi]=0 but
[e_chi*v_chi]=[v_chi] is nonzero. Changing the amplitude, or a
holomorphic frame, does not fix this obstruction. This conclusion
concerns that local algebra and that specific quotient. It does not
preclude a different metric with additional geometric terms, or a
full arithmetic quotient with other local and archimedean data.

## 6. Consequence for the A programme

P123.115 is strengthened from a curvature computation at zero to an
all-amplitude curvature formula, uniform kernel identification and
quantitative energy comparison. It also closes a possible ambiguity:
the local radical problem is structural, not a defect of linearizing
at the origin. The next geometric comparison must account for the
trace-product term and ruling data, rather than obtaining A.6 by
changing frame or base point in this Gram metric. No multiplicative
metric law, full mixed diagonal determinant, arithmetic RR identity,
or complete A/B/C/D row is claimed here.
