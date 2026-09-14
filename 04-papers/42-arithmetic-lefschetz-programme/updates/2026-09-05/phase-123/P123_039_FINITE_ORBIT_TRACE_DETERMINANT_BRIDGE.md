# P123.039 — finite orbit trace, integral torsion and the prime packet

Date: 2026-09-05. Status: CONSTRUCTED, with the finite trace/determinant
comparison below proved on the orbit lattices of P123.038. A global
mixed-correspondence shadow and its nuclear realization remain OPEN.

## 1. Keep the operator and its lattice together

For n>1 let V_n=Z[T]/Phi_n(T), realized inside the integral orbit module
Z[L_S/nL_S] as in P123.038. Translation by the diagonal integer 1
induces the automorphism T on V_n, with T^n=1. There is no eigenvalue 1
over C. The two-term integral complex

    D_n=[V_n --(1-T)--> V_n], degrees -1,0,

has H^(-1)=0 and

    H^0(D_n)=Z[T]/(Phi_n(T),1-T)=Z/Phi_n(1).

This explicitly identifies it with K_n^W from P123.025 in D(Z).
The domain and codomain use the same lattice V_n; consequently

    det(1-T|V_n)=Phi_n(1)>0,
    log #H^0(D_n)=log det(1-T|V_n).                 (1.1)

These are equalities of the lattice index and its actual determinant.
After complexification D_n is acyclic, but its integral model still
specifies the torsion determinant. Its ordinary categorical supertrace
is zero; (1.1) is not obtained by assigning that supertrace a nonzero value.

## 2. Obtain the determinant from cyclic finite traces

Let c_n(j)=Tr(T^j|V_n). Trace is the usual basis-independent integral
trace and satisfies Tr(AB)=Tr(BA), including rectangular compositions
between different finite free lattices. It extends to the ordinary
supertrace on their bounded complexes.

On the full orbit module M_d=Z[Z/d], translation has trace d if d divides
j, and zero otherwise, since its permutation fixes exactly those points.
The cyclotomic integral filtrations imply additivity of traces with
successive primitive pieces. Moebius inversion therefore gives

    c_n(j)=sum_(d divides gcd(n,j)) d mu(n/d).       (2.1)

This derives the Ramanujan trace from finite translations on the actual
quotient lattice. It does not replace the integral filtration with
unjustified integral eigenspace projectors.

Choose a T-invariant Hermitian norm on V_n tensor C by averaging a
Hermitian inner product over the finite cyclic group. For 0<=r<1, the norm-convergent series

    log(1-rT)=-sum_(j>=1) r^j T^j/j

gives

    log det(1-rT)=-sum_(j>=1) r^j c_n(j)/j.         (2.2)

Absolute convergence follows from |c_n(j)|<=rank(V_n) and r<1.
The determinant is positive on this real interval: nonreal eigenvalues
occur in conjugate pairs and the possible real eigenvalue -1 contributes
1+r. Thus the logarithm in (2.2) is the real branch starting at zero.

As r increases to 1, 1-T remains invertible on V_n tensor C. Continuity
of its finite determinant proves

    log #H^0(D_n)
       =-lim_(r -> 1-) sum_(j>=1) r^j c_n(j)/j.    (2.3)

This is a trace-to-torsion comparison with a specified integral complex,
not a numerical degree imposed on an unrelated analytic object.

## 3. Cancellation occurs before evaluating the limiting degree

The full orbit determinant is det(1-rT|M_d)=1-r^d. Its primitive
factorization, or (2.1) in (2.2), yields

    det(1-rT|V_n)=product_(d divides n)(1-r^d)^mu(n/d).

For n>1 the exponents sum to zero. Divide each factor by 1-r and let
r tend to 1. This gives

    det(1-T|V_n)=product_(d divides n) d^mu(n/d).

It equals p for n=p^k and 1 for mixed n, in agreement with the perfect
contact object rather than only a postulated logarithmic coefficient.
The four cases 2,4,3,6 therefore give determinants 2,2,3,1 and contact
groups Z/2,Z/2,Z/3,0. The series in (2.3) is not asserted absolutely
convergent at r=1. In fact c_n(j) is periodic with mean zero, which
also gives ordinary Dirichlet convergence for fixed n; neither fact is
a uniform estimate as n tends to infinity.

## 4. Realize the compact finite-place radial packet as a trace limit

For h in C_c^infinity(R) supported in [-R,R], set

    w_n(h)=n^-1/2 [h(log n)+h(-log n)],
    B_R=direct-sum_(2<=n<=exp R) (V_n tensor C).

This is a finite-dimensional space constructed from the finite quotients
of P123.038. On it define the block operator

    A_h(r)=direct-sum_n w_n(h) log(1-rT_n).

Equations (1.1)–(2.3) imply

    lim_(r -> 1-) Tr(A_h(r))
      =sum_n w_n(h) log #H^0(D_n)
      =sum_(p,k>=1) (log p)p^-k/2
                         [h(k log p)+h(-k log p)]. (4.1)

All sums over n here are finite by support, so passage to the limit
requires no unproved uniform estimate across labels. This is exactly
the radial finite-place packet of P123.032, now realized by traces of
logarithms of operators on actual finite orbit lattices. The factor
n^-1/2 is the half-density factor of the external class of n from
P123.038. No zero of zeta is used in this construction.

## 5. The remaining categorical comparison is explicit

Finite endomorphism traces are cyclic, and the torsion determinant
comparison is now proved. But the assignment h -> A_h(r) has not been
shown to preserve convolution; point evaluations w_n(h) do not by
themselves make it an integrated group representation. Likewise T_n is
the finite translation, not the external dilation E_n. The construction
must not be called Meyer's representation or the full A.5 shadow.

What remains is to realize this finite logarithmic determinant operation
as the arithmetic restriction of the common mixed-correspondence
shadow, preserving its composition and analytic test action, and then
to join the unit, archimedean and Tate sectors by that same comparison.
A collection of equal trace values is insufficient for those functorial
claims. This note supplies the finite operator/lattice comparison that
such a functor would have to extend. It does not prove effectivity,
mixed RR, the global sign, or closure of A/B/C/D.
