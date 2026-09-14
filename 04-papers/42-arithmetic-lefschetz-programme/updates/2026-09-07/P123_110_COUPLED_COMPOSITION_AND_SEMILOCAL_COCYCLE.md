# P123.110 — Coupled determinant composition and a semilocal boundary cocycle

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY for external Bruhat
test germs in the induced representation of P123.109. This establishes
the analytic correction and its coherence, not its geometric RR origin.

## 1. Operator symbols respect the original convolution

Let F,G be external Bruhat tests and H=F+G+F*G, using external Haar
convolution. Choose them sufficiently small that the sums of operator
norms of the coefficients T_(k,chi) in P123.109 are less than 1/4 for
each test. Then the corresponding bound for H is less than one.

The operator Laurent symbols in that note satisfy

    P_(F*G,chi)(w)=P_(F,chi)(w) P_(G,chi)(w),
    1+P_(H,chi)=(1+P_(F,chi))(1+P_(G,chi)).                 (1)

Indeed the uncut induced representation preserves convolution. On each
unit-character part of the full normal Hilbert space, normalized shells
indexed by all integer valuations identify D_q with the bilateral shift.
The finitely many shift coefficients in this representation are unique:
the matrix entry between shells j and j+k recovers T_(k,chi). Comparing
coefficients of the represented convolution proves (1), retaining their
operator order. No commutativity of individual T coefficients is needed.

Multiplicativity of trace-class Fredholm determinants in (1) gives

    b_H(1)=b_F(1)+b_G(1),                                   (2)

where b is the bulk function of P123.109 and all logarithms are germs
vanishing at zero tests. This determinant identity can be obtained by
finite-rank approximation in trace norm from the finite-dimensional
identity; the small norm neighborhood fixes the logarithm branch.

## 2. Endpoint defect on finitely many copies of the tangential space

Write F_L=E R(F) E and G_L=E R(G) E. The exact defect is

    D_L=E R(F*G)E-F_L G_L=E R(F)(1-E)R(G)E.

As in P123.108, finite valuation bandwidth implies that for large L
this defect has row and column support at the two endpoints of each
active unit-character block. Choose a fixed width larger than the sum
of the two valuation bandwidths plus two. Let H_end be the finite direct
sum of copies of H_tan indexed by these endpoints, and W_L its isometric
insertion into the cutoff space. Then

    D_L=W_L d W_L*,                                        (3)

where the endpoint operator matrix d is independent of sufficiently
large L. It is trace class on H_end: its finitely many entries are
finite sums of products of bounded and trace-class T coefficients.
Although there are finitely many endpoint indices, H_end itself is
usually infinite-dimensional; the determinant below is a Fredholm
determinant, not a finite-dimensional determinant.

Put

    C_L=W_L*(1+G_L)^-1(1+F_L)^-1 W_L.

The Neumann expansion proves convergence in operator norm to C_infinity.
For any fixed pair of powers in the expansion, the endpoint entries
stabilize exactly once the normal interval is sufficiently long, by
the finite-band path argument with ordered operator products. The
geometric norm bound is uniform in L, so the remaining double-series
tail tends to zero uniformly. It follows that

    ||(C_L-C_infinity)d||_1
         <=||C_L-C_infinity|| ||d||_1 ->0.                  (4)

Thus the endpoint determinants converge. For completeness, continuity
here follows from the absolutely convergent exterior-power series for
det(1+X) on trace-class operators; on a bounded trace-norm set its
difference is bounded by ||X-Y||_1 times an exponential in their trace
norms. Equation (4) supplies exactly the required convergence.

## 3. The coupled analytic composition law

Finite-cutoff determinant multiplication and the rectangular Fredholm
identity give

    det(1+E R(H)E)
      =det(1+F_L)det(1+G_L) det_Hend(1+C_L d).              (5)

The rectangular identity follows by finite-rank approximation of d;
the other factors are bounded. Divide by the bulk counterterms, use
(2), and pass to the limit via P123.109 and (4). The result is

    Delta_H(1)=Delta_F(1)Delta_G(1) A_(S,q)(F,G),
    A_(S,q)(F,G)=det_Hend(1+C_infinity d).                   (6)

This is an explicit convergent endpoint-operator formula for the
correction of the actual coupled induced action. It is not obtained
by multiplying independently selected scalar corrections.

Writing F diamond G=F+G+F*G, associativity of the original convolution
and nonvanishing of the germs imply

    A(F,G) A(F diamond G,K)=A(G,K) A(F,G diamond K).          (7)

All equalities hold as germs on fixed test supports and levels; values
can be taken in any common sufficiently small norm neighborhood.
The cutoff formulation and adjoints also imply
A(G^*,F^*)=conjugate(A(F,G)) there, with reversal of the factor order.

## 4. Compatibility with the prescribed semilocal maps

Normalized scalar pullback from S to T preserves external convolution
by P123.023 and satisfies Delta_(T,q,F_T)=Delta_(S,q,F) by P123.109.
Apply (6) to F,G and F diamond G at both levels. Since the determinant
germs are nonzero near zero, their ratios give

    A_(T,q)(F_T,G_T)=A_(S,q)(F,G).                          (8)

This agrees on chart triples by (7) and the coherent pullbacks. It does
not require a choice of endpoint basis compatible across all charts;
the ratio and its operator formula identify the same scalar germ.
Changes of regular section with all cutoffs transported unitarily have
the same invariance.

## 5. Remaining burden for A

The coupled analytic determinant now has its full local composition
correction, associative cocycle, adjoint compatibility and prescribed
semilocal scalar-test compatibility. These are substantive analytic
identities on the already constructed source test representation.

Locally the cocycle in (6) is a ratio of determinant germs; its existence
alone does not construct a geometric biextension or prove uniqueness
of the arithmetic metric. The required identification with the mixed
diagonal determinant, higher diagonal homology and gluing across all
strata remain unproved. Therefore row A and the global proof remain open.
