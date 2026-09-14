# P123.045 — Strict rapid excision for the boundary cover and its complement

Date: 2026-09-05. Status: PROVED for the explicit completed sequences
below. These are source-level excision data, not yet a localization
theorem for the regularized shadow.

## 1. Use the existing rapid completion

Keep X^+, Gamma, O, U_p and U from P123.044. For an invariant locally
closed space Z define

    A(Z)={b=(b_q): b_q in C_0(Z),
           p_k(b)=sum_q ||b_q||_infinity H(q)^k < infinity for all k}.

Multiplication is the crossed convolution of P123.019. All actions on
coefficients are isometries, so its same seminorm estimates apply.
For invariant open Z in X^+, extension by zero identifies A(Z) with a
closed ideal of A(X^+). The latter is itself an ideal in the repaired
full additive-carrier algebra, since the positive real component is
invariant and open. No coefficient unitization is required here.

## 2. The chart-cover sequence survives completion strictly

The sequence of P123.044 lifts coefficientwise to

    0 -> A(O)^(r-1) --d--> direct_sum_p A(U_p)
           --sigma--> A(U) -> 0.                    (2.1)

These are continuous bimodule maps over A(U), not a sequence of algebra
homomorphisms: sigma sums ideals and retains their cross-products.
Exactness in the middle follows label by label. The inverse from the
kernel of sigma to A(O)^(r-1) simply retains the components p!=p_0;
restriction to O preserves their coefficient norms. Hence that inverse
is continuous for every p_k and the image of d is closed.

For surjectivity with topological control, choose bounded nonnegative
continuous functions eta_p subordinate to the finite cover U_p, with
sum eta_p=1. Define a linear section

    s(b)_p,q = eta_p b_q.

The products, restricted to U_p, lie in C_0(U_p). In the direct-sum
seminorm given by the sum of component p_k norms,

    sum_p p_k(s(b)_p) <= r p_k(b).                  (2.2)

Thus s is a continuous linear right inverse in the actual rapid
topology, and (2.1) is split exact as a sequence of Fréchet spaces.
The partition is not assumed equivariant; s is not asserted to be a
bimodule map. The maps d and sigma themselves are equivariant, since
they are built from invariant open inclusions. Their crossed-product
bimodule identities follow directly from the convolution formula.

## 3. An explicit bounded extension from the multiple-zero complement

Let F=X^+\U, the closed subset with at least two zero finite coordinates.
Assume r>=2; for r=1 it is empty. Fix chi_i=1_(Z_i) in C_c(Q_i), so
chi_i(0)=1 and ||chi_i||=1. On C_0(X^+) define commuting bounded
projections

    (E_i f)(x)=chi_i(x_i) f(x with coordinate i replaced by 0).

They map C_0(X^+) to itself, have norm at most one and satisfy E_i²=E_i.
For J contained in S_f put

    P_J = product_(i in J) E_i product_(i notin J)(1-E_i),
    P_F = sum_(|J|>=2) P_J.

The P_J are pairwise annihilating projections and their sum is identity.
Hence P_F is a bounded projection. Every term in its expansion evaluates
f only at a point with at least two specified coordinates zero. Therefore
P_F f depends only on f restricted to F. Also

    (P_F f)|_F = f|_F.                             (3.1)

To see this, at a point with zero-coordinate set Z, evaluating any term
containing (1-E_i) for i in Z gives zero. Only J containing Z survive;
if |Z|>=2 all those terms occur in P_F, and their sum evaluates to f.

This gives an extension without choosing an arbitrary lift. For
g in C_0(F), expand P_F in products E_I; all occurring I have |I|>=2.
In each such term use

    product_(i in I) chi_i(x_i) g(x with coordinates I set to zero).

These functions are continuous and vanish at infinity on X^+: compact
support of the chi_i controls the replaced coordinates, while g controls
the remaining coordinates. Their finite linear combination defines
e_F(g) in C_0(X^+). Equation (3.1) shows res_F e_F=id. For example the
coarse uniform bound

    ||e_F(g)|| <= 3^r ||g||                       (3.2)

follows by summing 2^(r-|J|) over J. No optimal constant is needed.

## 4. Strict completed localization at the closed complement

Restriction is a Gamma-equivariant star homomorphism. Its coefficient
kernel consists precisely of functions vanishing on F, namely C_0(U)
extended by zero. Applying e_F independently to every label, (3.2)
gives p_k(e_F b)<=3^r p_k(b). Consequently

    0 -> A(U) -> A(X^+) --res_F--> A(F) -> 0        (4.1)

is an exact sequence of Fréchet star algebras and is continuously split
as a sequence of vector spaces. The extension e_F need not commute with
Gamma, multiplication or external scaling. None of those properties is
needed for the linear splitting or strictness; restriction itself does
commute with those actions and preserves crossed convolution.

For r=2 the extension has particularly transparent form:

    e_F(g)(t,x_p,x_q)=chi_p(x_p)chi_q(x_q)g(t,0,0).

In particular the complement algebra is nonzero. Its presence cannot
be dismissed by the absence of mixed prime labels on single-zero fixed
strata. For r>2 the projection retains all zero sets of size at least
two, with their intersections, rather than treating those pieces as
disjoint.

## 5. Exact scope of this advance

Equations (2.1) and (4.1) now hold in the repaired rapid completion,
with explicit continuous splittings and bounds at every defining
seminorm. This removes the completion/exactness obligation left at
coefficient level in P123.044. The constructions are on the original
space with its group action, so they do not require a Hausdorff global
orbit quotient.

A strict algebra extension does not automatically provide the desired
trace localization or an exact triangle in every proposed correspondence
category. The next necessary result is an excisive shadow applicable to
these particular extensions, agreeing on each chart with P123.043 and
controlling its value on A(F). Compatibility of that shadow with the
integral contact, semilocal transitions and the archimedean boundary also
remains to be constructed. No full A/B/C/D closure is claimed.
