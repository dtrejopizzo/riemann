# P123.074 — Half-density adjoint and source graph effectivity

Status: PROVED for the fixed-S graph-kernel sectors.
This gives a geometric adjoint and effective cone in that sector, not
their full numerical/RR descent on the stable category.

Give X_S additive product Haar measure mu, with finite local unit balls
of additive volume one. Write |a|_S=product_(v in S)|a_v|_v. For each
positive S-unit gamma, the elementary product formula gives |gamma|_S=1.
Thus gamma dilation is measure preserving. External dilation has its
unitary half-density action

    U_a f(x)=|a|_S^-1/2 f(a^-1 x)

on L²(X_S,mu). The crossed representation

    pi(b)=sum_gamma M_(b_gamma) U_gamma

converges in operator norm with ||pi(b)||<=p_0(b). Haar change of
variables gives pi(b*)=pi(b)* and U_a pi(b) U_a^-1=pi(beta_a(b)).
Consequently the half-density version of P123.073 is

    Pi(b,a)=pi(b)U_a=|a|_S^-1/2 T_(b,a),
    Pi(b,a)Pi(c,d)=Pi(b beta_a(c),ad),
    Pi(b,a)*=Pi(beta_a^-1(b*),a^-1).             (1)

These are equalities of bounded Hilbert operators, with no assertion
of trace class. Faithfulness on each fixed-a sector follows from the
row-measure argument in P123.073: zero operator gives zero rows almost
everywhere, using a countable dense collection of C_0 tests, which can
be chosen with compact support and hence in L². The absolutely summable
row measures then vanish on all C_0 tests outside one null set. On the
conull subset with nonzero real coordinate their atoms are distinct, so
each coefficient vanishes almost everywhere. Full support of Haar and
continuity force every coefficient to vanish identically.

Formula (1) identifies the elementwise dagger of the graph sector with
the Hilbert adjoint. It is exactly the earlier formula
j_beta(b)=beta^-1(b*), now with its geometric half-density normalization.
It reverses graph composition and squares to identity. This statement
concerns elements and sectors; it does not by itself provide a
contravariant duality on every dg morphism between arbitrary complexes.

Define an effective graph element by requiring every coefficient
b_gamma to be real and nonnegative. The corresponding half-density row
measures are positive. Conversely positivity of all row measures implies
coefficient nonnegativity on the dense set where their atoms are distinct,
and therefore everywhere by continuity. Thus the cone is intrinsic to
the represented graph measures, rather than selected from an eventual
quadratic-form sign.

The cone is closed in the rapid topology, closed under addition and
nonnegative real scaling, and preserved by composition: each crossed
coefficient is a convergent sum of products of nonnegative functions.
The adjoint formula (1) preserves it as well. Gauge changes preserve it
by relabelling, and the repaired coefficient chart maps preserve it by
adjoining nonnegative lattice characteristic functions and constant
coefficients as specified in P123.020.

This cone is not the positive-semidefinite operator cone. For example
the effective permutation kernel exchanging two points is self-adjoint
with eigenvalues 1 and -1. Hence preservation of source graph effectivity
does not prove the Hodge sign required by D. No identification of that
cone with classes of arbitrary complexes or their numerical quotient
is made here. Extending effectivity through the stable geometric category
and proving the descent required by mixed RR remain A.7–A.8 obligations.

The fixed-S graph construction now has a faithful half-density star
representation and a closed geometric effective cone with the correct
distinction from operator positivity. The unresolved global dagger,
geometric descent, diagonal trace target and RR are not replaced by
these local operator identities.
