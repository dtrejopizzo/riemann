# A — working construction of the trace-product metric

2026-09-07. Research work only; do not insert into paper42 automatically.
The theorem below is local on the fixed external test domains of P123.109.
The final section records the precise missing arithmetic comparison.

## Source-defined metric whose curvature is the trace-product form

Write R for the actual induced star representation, E_L for its normal
cutoff, and Delta_H(z), b_H(z) for P123.109. Use F^* for test involution
and juxtaposition with * between two tests for convolution. Fix finitely
many Bruhat test directions and a common enlarged domain containing their
involutions and pairwise convolutions. For F sufficiently small put

    H(F)=F^* * F,
    k(F)=Delta_(H(F))(1),
    mu(F)=log k(F).                                      (1)

The logarithm is normalized to zero at F=0. These are not obtained by
setting a desired intersection form equal to a metric by definition:
they are limits of the original source operator Gram determinants with
the already fixed nonlinear bulk subtraction, as proved next.

Let Z_L(F)=R(F)E_L from E_L H to the full represented Hilbert space.
Then

    Z_L(F)^* Z_L(F)=E_L R(F)^*R(F)E_L=E_L R(H(F))E_L.

The right side is positive trace class by the trace-class compression
theorem for the compact test H(F). Thus Z_L(F) is Hilbert–Schmidt and

    k_L(F)=det(1+Z_L(F)^*Z_L(F))
                         exp(-(L+1)b_(H(F))(1))          (2)

is a positive real number. In fact the symbol of H(F) is
P_F(w)^*P_F(w) for |w|=1, by the source convolution and adjoint, so
b_(H(F))(1) is real. All determinants in (2) are the actual Fredholm
determinants of these positive trace-class Gram perturbations.

P123.109 gives locally uniform convergence of (2) to k(F), with its
quantitative trace-series tail, since the coefficient operator norm of
H(F) is quadratic in the size of F. Its limiting nonvanishing logarithmic
series is real, so k(F)>0 near zero. Thus ||1||_F^2=k(F)^-1 is a genuine
positive Hermitian metric on a trivial line over this test neighborhood.
Unlike the normalized escaping-graph metric of P123.117, it is not
asserted to have nonnegative curvature.

Complexify F and its conjugate as independent finite test variables.
The bounds in P123.109 make log Delta_H(1) a locally uniformly convergent
holomorphic series in these variables. Consequently (1) is real analytic
on their conjugate diagonal and its derivatives can be taken termwise.
At zero, H has vanishing first derivative. Only the linear term
W_q(H) of log Delta_H contributes to its quadratic variation. Therefore

    partial_z partial_bar_w mu(zU+wV)|_0
        = W_q(V^* * U).                                  (3)

All higher trace powers have total test degree at least four. Equation
(3) is precisely the Hermitian trace-product form, including its existing
normalization. It is not the anomaly energy B(U,V^*). The absence of a
holomorphic Hessian correction here follows from using the quadratic
source family H(F); it is not a claim that the correction in P123.114
vanishes for its different family.

The finite-cutoff version of (3) is

    Tr(E_L R(V)^*R(U)E_L)
           -(L+1)(log q)(V^* * U)(1).

For sufficiently large L this is already W_q(V^* * U), by the relative
trace theorem. Thus the curvature calculation can also be made before
the determinant limit. The limit proof above controls the metric itself,
not only the second derivative.

## Comparison with the previous boundary metrics

The difference from P123.115 is concrete: that construction used only
(1-E_L)R(F)E_L. The new Z_L contains the retained part E_LR(F)E_L as
well. Its bulk subtraction is essential. Positive finite-cutoff Gram
curvatures minus their bulk terms need not have a positive limit.
This explains why (3) can be indefinite without contradicting positivity
of the finite-cutoff metric or of the endpoint energy.

In the local normal test model of P123.112, let e_chi be a nontrivial
unit-character projector, with conductor c, and v_chi its valuation
shift. Both obey f^* * f=e_chi. P123.105 then gives the exact metric
along each of these two rays:

    k(t e_chi)=k(t v_chi)=(1+|t|^2)^(-c).

Their curvature at zero is -c, as required by the trace-product form.
The endpoint metric instead assigns zero energy to e_chi and nonzero
energy to v_chi. The new metric therefore does not inherit that specific
radical defect at the origin. More generally the radical of (3) against
all tests in the local normal algebra is zero by P123.113. This statement
is local; it does not assert the radical of the full arithmetic category.

## Prescribed semilocal compatibility

The normalized scalar pullbacks of P123.109 preserve involution and
convolution. Thus H(F_T)=H(F)_T and

    k_T(F_T)=k_S(F),
    mu_T(F_T)=mu_S(F).

These are equalities of the actual determinant germs; the metrics and
curvatures therefore pull back exactly, with their existing triple
compatibility. Unitary section changes have the same invariance when
cutoffs are transported. No independent-cutoff comparison is added.

## What the intrinsic ruling metric requires next

The paper's fixed ruling line has norm exp(-d_1(x)d_2(x)); its polarized
form is d_1(x)d_2(y)+d_2(x)d_1(y). The construction above now supplies
an operator-defined Hermitian metric with the trace-product curvature on
the actual external test domain. It is still necessary to construct a
geometric map from the admissible mixed/ruling objects into the determinant
data, compare its line with the intrinsic ruling line, and prove the
metric equality with the correct normalization (including the distinction
between a norm and its square). Neither choosing an abstract hyperbolic
plane of tests nor adjusting a scalar normalization establishes that map.

Likewise (3) is an equality at the identity tangent space. It does not
prove global biextension additivity of mu, principal descent on a full
geometric Picard group, effectivity, or the identification of every mixed
correspondence with an external scalar test. These remain mathematical
requirements for A. The relevant next task is the object-level ruling/
mixed determinant comparison, rather than returning to the endpoint
Gram metric whose curvature computes a different pairing.

## An all-amplitude quadratic determinant limit and its biextension

There is a further construction that removes the smallness restriction
for a *different*, explicitly normalized determinant line. For a fixed
test F and sufficiently large positive integer N, take N copies of the
source Gram family at F/sqrt(N). Define

    ||1||_(N,F)^2 = k(F/sqrt(N))^(-N).                    (4)

These are actual tensor powers of the locally constructed metric. The
logarithmic determinant series gives, uniformly on bounded subsets of
any fixed finite-dimensional test domain,

    N mu(F/sqrt(N))=W_q(F^* * F)+O(1/N).                  (5)

Indeed H(F/sqrt(N))=H(F)/N; the term linear in H is W_q(H)/N, while
all trace powers r>=2 sum to O(N^-2) on a fixed bounded coefficient set
by P123.109. Thus (4) converges for every F in the stated test algebra to

    L_tan(F)=(C1, ||1||^2=exp(-I(F,F))),
    I(F,G)=W_q(G^* * F).                                 (6)

This limit comes from the source determinant and its fixed bulk subtraction.
It is not the assertion that the original unscaled metric mu was quadratic.
It also fixes the norm convention: ||1||=exp(-I(F,F)/2).

The polarized line

    P(F,G)=L_tan(F+G) tensor L_tan(F)^-1 tensor L_tan(G)^-1

has distinguished-generator norm

    ||1||_(P(F,G))=exp(-Re I(F,G)).                       (7)

Since I is sesquilinear, (7) is biadditive on the underlying real test
space. Sending distinguished generators to their tensor products gives
isometries P(F+F',G)=P(F,G) tensor P(F',G), and in the other variable.
Both orders of applying these maps agree, since each sends 1 to 1 and
the metric exponents add identically. Symmetry follows from Hermitian
symmetry. Therefore (7) is a based Hermitian biextension of this additive
test space, with its exact interchange and associativity identities.
It respects every prescribed semilocal pullback preserving I.

An isometry of scalar forms on a ruling plane is insufficient for the
arithmetic comparison. For example the local normal tests e and r^-1 v
of P123.113 span a hyperbolic Hermitian plane with matrix [[0,1],[1,0]].
Formula (6) on real coordinates x,y in that plane has norm exp(-xy),
matching the fixed ruling expression numerically. This does NOT identify
those tests with the two geometric ruling objects; the normalization and
that object-level map would still need a proof. Accordingly (6)–(7)
construct the analytic determinant/biextension target for the comparison,
not its missing geometric source functor or the full A.8 assertion.
