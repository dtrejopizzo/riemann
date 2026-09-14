# P123.111 — The mixed anomaly is an exact boundary pairing

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY for the external
Bruhat test algebra in the induced single-zero representation. This
pairing measures escape from a normal cutoff; it is not identified
with the global arithmetic intersection form.

## 1. The mixed derivative has a source operator formula

Let R be the convolution representation of P123.043 and E=E_L its
transported normal cutoff. Write F_L=E R(F) E and G_L=E R(G) E.
The anomaly of P123.110 is a nonvanishing germ with value one at zero.
Define

    B_(S,q)(F,G)=partial_s partial_t
                    log A_(S,q)(sF,tG) evaluated at s=t=0. (1)

At finite cutoff the corresponding mixed derivative is

    B_L(F,G)=Tr(E R(F*G)E-F_L G_L)
            =Tr(E R(F)(1-E)R(G)E).                         (2)

To verify it, expand log det(1+sF_L+tG_L+st E R(F*G)E)
to degree st. The linear term contributes the first trace in (2),
and the quadratic term contributes -Tr(F_L G_L); the two separate
logarithmic determinants have no mixed term. All operators under a
trace are trace class by the coefficient construction of P123.109.

The defect in (2) is exactly W_L d(F,G) W_L* from P123.110, where
d is the fixed endpoint operator matrix for sufficiently large L.
Consequently the mixed derivative stabilizes exactly:

    B_(S,q)(F,G)=B_L(F,G)=Tr_Hend d(F,G)                    (3)

for all sufficiently large cutoffs depending on the two fixed supports
and unit levels. The locally uniform germ convergence in P123.110
justifies differentiating the limit as well. Thus (1) is computed by
an actual endpoint trace, not defined by a desired intersection value.

## 2. Bilinearity, symmetry and continuity

Formula (2) is bilinear. Since the external group is abelian,
R(F*G)=R(G*F). Also F_L,G_L are trace class, so
Tr(F_L G_L)=Tr(G_L F_L). It follows that

    B(F,G)=B(G,F).                                         (4)

Adjoints in (2) give B(G^*,F^*)=conjugate(B(F,G)). On fixed valuation
and unit supports the finitely many entries of d are finite sums of
products of tangential coefficient operators. The trace-ideal inequality
||UV||_1<=||U|| ||V||_1, together with the smooth-kernel estimates of
P123.109, proves continuity of (3) in the declared Bruhat test topology
on each such test domain. No uniform estimate over unrestricted growing
supports is asserted.

The normalized semilocal scalar pullbacks preserve the anomaly by
P123.110. Differentiation therefore gives

    B_(T,q)(F compose pi_TS,G compose pi_TS)=B_(S,q)(F,G).   (5)

The pairing is also unchanged by unitary changes of section with the
normal cutoff transported. These are exactly the chart and frame maps
already established, not new full coefficient transitions.

## 3. Its Hermitian specialization is a cutoff-escape energy

Define E_boundary(F,G)=B(F,G^*). For F=G, (2) becomes

    E_boundary(F,F)
      =Tr(E R(F)(1-E)R(F)^*E)
      =||(1-E)R(F)^*E||_2^2 >=0                           (6)

at every sufficiently large cutoff. The Hilbert--Schmidt assertion
follows because the bounded operator X=(1-E)R(F)^*E has X*X equal
to the positive trace-class defect in (2). In particular no trace of
an arbitrary non-trace-class positive operator is used. The stabilized
pairing is Hermitian by (4) and star, and satisfies Cauchy--Schwarz by
applying (6) to F+zG for arbitrary complex z.

Equation (6) identifies precisely the positivity obtained: it measures
the part of R(F)^* applied to the retained normal subspace that leaves
that subspace. Its null vectors have zero such escape for every
sufficiently large cutoff, by exact stabilization and vanishing of the
Hilbert--Schmidt norm. This is a property of this cutoff representation;
it is not a theorem about the numerical radical of all mixed source
correspondences, and no ideal-stability of that radical is inferred.

The local opposite-shift example of P123.108 has anomaly 1/(1-st),
whose mixed logarithmic coefficient is one. Thus endpoint contributions
can be nonzero even though each single-shift relative determinant is one.
That example is a local normal calculation, not an assertion that every
such normal test is a scalar external induced test.

## 4. Remaining geometric identification

The coupled analytic anomaly now has a source-defined continuous mixed
pairing, an exact endpoint formula, and prescribed semilocal invariance.
The Hermitian specialization has the explicit positive meaning (6).

None of this identifies B with the intersection required by A.8, fixes
the arithmetic metric, or proves the global Hodge/Weil sign required
by D. The determinant anomaly, the periodic ruling determinant and
the mixed source diagonal still need a common geometric comparison.
Higher diagonal homology and gluing across other strata remain open.
