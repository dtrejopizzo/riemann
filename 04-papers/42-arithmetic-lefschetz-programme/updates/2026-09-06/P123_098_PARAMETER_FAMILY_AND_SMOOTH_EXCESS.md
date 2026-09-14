# P123.098 — A parameter-family obstruction and the smooth tangential excess

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for the obstruction
and the explicit smooth-circle model below. The latter is not yet
identified with the full arithmetic source or its semilocal completion.

## 1. The continuous corner calculations do not form a perfect family

Take the external path a_s=(exp(s),1,1), for s in a small real interval
I about zero, and Y=B_q. It lies in K_q only at s=0: the fixed-boundary
condition would require gamma exp(s)=1 in R and gamma=1 in Q_p;
injectivity of Q->Q_p forces gamma=1 and then s=0.

P123.096–097 thus compute the individual continuous corner diagonals as
zero for s!=0 and C(Y)[0] for s=0, in the specified strict-derived sense.
There cannot be a bounded complex of finite-rank continuous vector
bundles on I times Y whose restrictions have those perfect classes.

Indeed its virtual rank, the alternating sum of the ranks of its terms,
is locally constant. For each fixed y, it is constant along the connected
interval I times {y}. The asserted restrictions would have virtual rank
zero for s!=0 and one at zero, a contradiction. The same argument
applies to a locally perfect family near any point (0,y), after choosing
a finite bundle representative in that neighborhood.

This does not contradict the separate fixed-parameter computations.
It proves they cannot simultaneously be the fibers of a base-change
compatible perfect family of the type needed to apply P123.095 uniformly.
Thus that step must not be inferred merely by assigning the individual
fiber determinants. The obstruction concerns this perfect-family route;
it is not a nonexistence theorem for every nuclear or distributional target.

## 2. A smooth diagonal has an additional degree-one contribution

The following exact model shows how a tangential excess can restore
constant virtual rank. Let B_sm=C^infinity(S^1;C), with its usual
derivative seminorms, and R=C^infinity(S^1 times S^1;C). Coordinates
are angles theta,phi. Put g(theta,phi)=exp(i theta)-exp(i phi).
There is a continuously split resolution on underlying Frechet spaces

    0 -> R --g--> R --restriction_to_diagonal--> B_sm ->0.   (1)

Multiplication by g is injective because its zero set, the diagonal,
has empty interior. Its image is exactly the smooth functions vanishing
there. Locally write phi=theta+u. Then
g=exp(i theta)u v(u) with v smooth and nonzero near zero. For a function
f vanishing on the diagonal,

    f(theta,theta+u)/u
       =integral_0^1 partial_u f(theta,theta+t u) dt.

This proves smooth division by g and bounds derivatives of order m of
the quotient by derivatives up to m+1 of f near the diagonal. Away
from the diagonal division is ordinary multiplication by 1/g. A finite
partition of unity yields continuous division on the closed kernel of
restriction. Restriction has the continuous section h(theta,phi)=h(theta).
These formulas establish the asserted topological splitting.

The algebra R is B_sm tensorhat_pi B_sm: Fourier coefficients of smooth
functions are rapidly decreasing, and the absolutely convergent double
Fourier expansion gives the completed tensor identification with its
derivative seminorms. Thus (1) is a finite free resolution of the smooth
diagonal over its completed enveloping algebra, not just a formal equation.

## 3. Derived pullback to the moving graph

Pull (1) back to phi=theta+s. Since the terms resolving the diagonal
are finite free over R, the resulting derived intersection is represented
by the two-term complex

    [ B_sm --exp(i theta)(1-exp(i s))--> B_sm ],             (2)

in homological degrees one and zero. Removing the invertible factor
exp(i theta) identifies it with [B_sm --(1-exp(i s))--> B_sm].
For 0<|s|<2pi it is contractible by division by the nonzero scalar.
At s=0 its differential is zero and its homology is B_sm in each of
degrees zero and one. Its virtual rank is zero for every s.

The same formula over smooth functions on I times S^1 supplies a
finite free family, with ordinary restriction of these free terms equal
to the derived fibers (2). There is no rank-jump contradiction: at the
fixed parameter the degree-one tangential excess cancels the degree-zero
rank. This gives a concrete model of the contribution omitted by the
continuous coefficient topology in P123.097.

## 4. Consequence for the next A construction

The smooth model is a proved comparison target, not a replacement made
without justification. To use it for A one must construct the smooth
tangential boundary domain on the actual mapping torus, compare its
completed tensors and cutoff modules, and retain the original trace and
normal action. Passage through finite unit levels and semilocal charts
must also be proved; a circle model alone does not provide those maps.

P123.095 remains a valid determinant construction on its declared
perfect-module sector. P123.096–097 remain the fixed-parameter continuous
bar calculations. What is ruled out is combining them into the claimed
perfect parameter family without additional tangential structure.
The normal determinant, arithmetic metric and mixed RR remain open.
