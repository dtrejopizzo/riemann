# P123.094 — The exact continuous shadow of the orbit-decay boundary

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for J=J_orb of
P123.092. This computes the Hausdorff degree-zero shadow, not a
derived determinant target or the numerical quotient required by A.6.

Let A be the coefficient-unitized rapid boundary algebra, B_q=Z_q/Gamma,
and F:C(B_q)->eJe the corner isomorphism of P123.091–093. Then

    J / closure(span[J,J])
       = J / closure(span[A,J]) = C(B_q)                    (1)

as topological vector spaces. The map inducing these identifications is

    T(a)([z])=sum_(delta in Gamma) a_1(delta z).              (2)

## 1. A continuous function-valued trace

Choose a relatively compact fundamental section of the proper action.
The height/weight comparison of P123.093 gives, uniformly on that
section, w(delta z)>=c H(delta)^(1/2). Hence for any N>0,

    sum_delta |a_1(delta z)|
        <=C_N s_(0,N)(a) sum_delta H(delta)^(-N/2).

The series converges uniformly there. The same argument on arbitrary
compact sets of Z gives local uniform convergence upstairs; every term
is continuous. Reindexing proves invariance, so (2) defines a continuous
function on B_q and a continuous linear map J->C(B_q).

The same bound, summed also over the coefficient labels, proves that
pi_y(a) in P123.088 is trace class at every y, uniformly in trace norm
on the quotient, for a in J. Its trace is (2). For b in A, pi_y(b) is
bounded and the representation preserves products, so ordinary
trace-class cyclicity yields

    T(ab)=T(ba).                                            (3)

In particular both closed commutator spans in (1) lie in ker T.
The rank-one corner formula gives T(F(h))=h for all h in C(B_q),
so T has a continuous section and is onto.

## 2. Every element with zero trace is a limit of commutators

Use the explicit local frame r_j from P123.093 (j abbreviates i,gamma).
Its estimates prove convergence in J of both sums

    a=sum_j r_j r_j* a,
    b=sum_j r_j* a r_j in eJe.                              (4)

For the second sum, apply the continuous flip and multiplication to
the absolutely convergent unbalanced projective tensor series
sum_j r_j tensor r_j* a from P123.093. Thus this convergence is in
the actual Frechet topology, not only in operator norm or weak topology.

At each y, pi_y(r_j)=|f_j,y><v_y| and
sum_j |f_j,y><f_j,y|=1. Therefore the scalar corner coefficient of b
is sum_j <f_j,y,pi_y(a)f_j,y>=Tr pi_y(a). This equality also follows
from absolute convergence of the trace-class diagonal series: the
vectors f_j,y lie in individual orbit coordinates and their squared
weights partition one in each coordinate. Hence b=F(T(a)).

Subtracting the two convergent sums (4) gives

    a-F(T(a))=sum_j [r_j,r_j* a].                            (5)

Both entries in every commutator belong to J. Consequently ker T is
contained in closure(span[J,J]). Combining (3) and (5) proves both
kernel equalities in (1). The topological quotient identification
follows from the continuous section F, or the Frechet open mapping
theorem. The formula T itself is independent of the cutoff and frame.

## 3. Scalar tests and the original boundary trace

Every continuous scalar functional on J annihilating [A,J] factors
uniquely through T and a continuous functional on C(B_q). Equivalently
it is integration of T(a) against a finite complex Radon measure on
the compact quotient. Thus (1) determines all such continuous scalar
trace tests on this domain, rather than only exhibiting one nonzero test.

The previously constructed trace is the quotient Haar test:

    tau_q(a)=integral_(B_q) T(a)(y) dy.                       (6)

This follows from absolute convergence and the fundamental-domain
integral formula, with the same quotient volume log q as before.
External dilation transports (2) by

    T(beta_a x)(y)=T(x)(a_T^-1 y),

because it commutes with Gamma and preserves the boundary. Hence (6)
has the established external invariance and the shadow is covariant
under quotient translation. Transpose gives T(x*)=conjugate(T(x)).

## 4. Scope for A

This identifies a nonzero completed function-valued boundary shadow,
with exact kernel, all its continuous scalar tests, and compatibility
with the corner tensors and original trace. It is stronger than a
single scalar trace comparison, but it remains a degree-zero result
on the orbit-decay boundary domain. It does not identify the numerical
radical defined by the required full mixed intersection tests, nor
supply higher diagonal homology, a determinant line or mixed RR.
The full-source and multi-stratum comparisons are still necessary.
