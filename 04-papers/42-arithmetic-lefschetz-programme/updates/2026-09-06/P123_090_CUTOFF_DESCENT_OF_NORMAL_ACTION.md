# P123.090 — Explicit cutoff descent to the induced normal action

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY on the single-zero
boundary. The projection and transport coefficients below are elements
of the boundary crossed product. No idempotent lift to the full source
across its other strata is asserted.

## 1. The quotient Hilbert space and its isometric cutoff realization

Retain Z=Z_q, Gamma, V=L2(Q_q), D and the covering representation
sigma,R of P123.089. Let H_Q be the measurable V-valued equivariant
sections on Z satisfying

    F(gamma z)=D_gamma F(z),
    ||F||^2=integral_(B_q) ||F(s(y))||^2 dy < infinity.

This is a separately defined quotient Hilbert space, not the invariant
subspace of L2(Z;V), where nonzero equivariant sections need not be
square-integrable. Unitarity of D makes its norm independent of s.

Choose the compact nonnegative cutoff c with Pc=1 from P123.087.
Define J_c:H_Q->H=L2(Z;V) by J_c F(z)=sqrt(c(z))F(z). Periodization
gives ||J_c F||=||F||. Its adjoint, initially on compactly supported
vectors, is the equivariant section

    (J_c* psi)(z)=sum_gamma sqrt(c(gamma^-1 z))
                                  D_gamma psi(gamma^-1 z).   (1)

The formula follows by splitting the inner product over the fundamental
domain; equivariance follows by reindexing. It extends to the bounded
adjoint on all H. In particular P_c=J_c J_c* is an orthogonal projection.

In the covering crossed-product representation it is explicit:

    P_c=sigma(e_c),
    (e_c)_gamma(z)=sqrt(c(z)c(gamma^-1 z)).                    (2)

Properness of the action and compactness of supp(c) imply only finitely
many nonzero labels. Coefficients are compactly supported continuous
functions on Z. The boundary algebra element e_c is self-adjoint and
idempotent: direct multiplication uses sum_eta c(eta^-1 z)=1.
Alternatively (2), the projection identity and the boundary faithfulness
of P123.088–089 prove the same assertion. This is a boundary idempotent,
not an asserted idempotent in the full ambient coefficient algebra.

## 2. Transfer between cutoffs

For two such cutoffs c,d put V_(c,d)=J_c J_d*. Its boundary coefficients
are sqrt(c(z)d(gamma^-1 z)), again with finitely many labels. They obey

    V_(c,d)*=V_(d,c),
    V_(c,d) V_(d,e)=V_(c,e),
    V_(c,d)* V_(c,d)=P_d,  V_(c,d) V_(c,d)*=P_c.              (3)

These follow from J_d*J_d=1. Thus the changes of cutoff are explicit
partial isometries with exact coherence, not an unspecified equivalence.

## 3. External action with the necessary cutoff transport

On H_Q the formula

    (R_Q(a)F)(z)=D_(a_q) F(a_T^-1 z)

preserves equivariance, has the group law, and is unitary since the
quotient measure is invariant. Set c_a(z)=c(a_T^-1 z). It is another
compact normalized cutoff, and the covering action satisfies

    R_a J_c=J_(c_a) R_Q(a).                                  (4)

Consequently the transported covering operator

    T_c(a)=V_(c,c_a) R_a=J_c R_Q(a) J_c*                     (5)

has support P_c on both sides and satisfies

    T_c(a) T_c(b)=T_c(ab),
    T_c(a)*=T_c(a^-1),  T_c(1)=P_c.                          (6)

It is a unitary representation on P_c H, extended by zero on the
orthogonal complement. Formula (5) follows from (4) and its adjoint;
it proves that the transport is exactly what restores the group law.
The bare compression P_c R_a P_c is not substituted for (5).

For diagonal gamma, equivariance gives R_Q(gamma)=1. Therefore this
representation descends to the external quotient G=H_S. It is strongly
continuous: local quotient trivializations reduce continuity to the
continuous normal dilation representation and ordinary translations;
dense compact continuous sections and unitarity finish the argument.
Alternatively the identification in the next section gives continuity
from P123.043. Changing c to d intertwines these representations by
V_(d,c), coherently by (3).

## 4. Identification with the induced normal bundle

The bundle (Z times V)/Gamma, with action
(z,v)->(gamma z,D_gamma v), is homogeneous under the external group.
At the base orbit of z_0=(0,1), the stabilizer is K_q=Q_q^* via its
local-idele class. Its action on the fiber is exactly D: use the
unnormalized representative with only q component nontrivial.

Explicitly, send (g,v) in G times V to the external translate of
[z_0,v]. Replacing (g,v) by (gk,D_k^-1 v) preserves this point.
The induced map G times_(K_q) V -> (Z times V)/Gamma is bijective
on fibers over G/K_q=B_q and is continuous in local trivializations.
It identifies their L2 section spaces, with the same quotient measure
of total mass log q. Under it R_Q is exactly the induced representation
R of P123.043, rather than merely having an equal scalar trace.

## 5. Normal cutoff and relative character commute with this descent

Let E_L be the fiberwise finite normal cutoff on H_Q in the regular
section of P123.043, and define its transported projection
E_(c,L)=J_c E_L J_c* on H. For a scalar external Bruhat test f,

    T_c(f)=J_c R_Q(f) J_c*,
    E_(c,L) T_c(f) E_(c,L)
       =J_c [E_L R_Q(f) E_L] J_c*.                           (7)

The operator on the right is ordinary trace class by P123.043.
Isometric transport preserves that trace. Thus for all sufficiently
large L, with the precise unit-level threshold of that note,

    Tr(E_(c,L) T_c(f) E_(c,L))-(L+1)(log q)f(1)=W_q(f).      (8)

Equations (3), (5) and (7) make (8) independent of the chosen cutoff.
The projection is transported along with the action; it is not an
unrelated constant normal cutoff imposed on the covering coordinates.

## 6. Remaining full-source obligations

This proves an explicit descent of the covariant covering normal action
to the induced quotient action, preserving external composition, star,
normal compressions and their relative character. All coefficients in
the descent construction are on the proper single-zero boundary.

For arbitrary x, the map x -> J_c* sigma(x) J_c is a compression;
it is not claimed multiplicative on the full boundary algebra. It is
multiplicative on the corner e_c A_boundary e_c. Transporting general
source correspondences requires the associated modules and tensor maps,
and gluing them to generic and multiple-zero strata remains unproved.
The determinant-valued diagonal and mixed RR are still obligations for
A; this single-boundary descent does not close that row.
