# P123.114 — Exact quadratic identity relating determinant, product trace and anomaly

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY for the coupled
induced external Bruhat test representation. This is an analytic
second-variation identity, not the geometric mixed RR theorem.

## 1. The regularized compressed product

Retain R, E_L, Delta_F and b_F from P123.109–111, and put a=log q.
For two tests F,G define F_L=E_L R(F) E_L and G_L similarly. The bulk
coefficient of their product is

    sum_chi Tr(constant_coefficient(P_(F,chi)P_(G,chi)))
        =a(F*G)(1).                                       (1)

Indeed the symbol product is the symbol of the represented convolution
by P123.110, and P123.109 identifies its summed constant trace as the
first bulk coefficient of F*G. Thus define

    Q_(S,q)(F,G)=eventual [Tr(F_L G_L)-(L+1)a(F*G)(1)].      (2)

The eventual value exists: P123.043 gives the exact relative trace of
E_L R(F*G) E_L, while P123.111 gives exact stabilization of its difference
from F_L G_L. Subtraction proves existence of (2) without a new limiting
assumption. It also gives the exact identity

    W_q(F*G)=Q_(S,q)(F,G)+B_(S,q)(F,G),                    (3)

where B is the mixed anomaly pairing. This holds for all sufficiently
large L depending on the fixed test supports, not just asymptotically.

## 2. The determinant Hessian identifies the second term precisely

Define lambda(F)=log Delta_F(1) as a germ at the zero test, using its
logarithm equal to zero there. The estimates of P123.109 hold uniformly
on bounded coefficient sets with fixed supports and unit levels, so
lambda(sF+tG) is a holomorphic germ in s,t and its derivatives can be
taken termwise. Its first derivative is

    d lambda_0(F)=W_q(F).

Only the quadratic term in the logarithmic determinant series contributes
to the mixed second derivative. Cyclicity gives the same trace for
F_L G_L and G_L F_L; equation (1) subtracts the corresponding bulk term.
Hence

    d^2 lambda_0(F,G)=-Q_(S,q)(F,G),
    W_q(F*G)=B_(S,q)(F,G)-d^2 lambda_0(F,G).                (4)

This proves the sign and normalization of the determinant variation
directly. Identifying the anomaly alone with W_q(F*G) would omit the
second term of (4).

Equivalently, apply the composition law of P123.110 to sF and tG:

    lambda(sF+tG+st F*G)
       -lambda(sF)-lambda(tG)=log A(sF,tG).

Its st coefficient is d lambda_0(F*G)+d^2 lambda_0(F,G)=B(F,G),
which agrees with the direct cutoff derivation above. This is a
consistency between the actual convolution product and the constructed
determinant, rather than a choice of an intersection value.

## 3. Chart compatibility and the local distinction of signs

Each term of (4) is symmetric bilinear and continuous on the fixed
test domains. Normalized semilocal scalar pullbacks preserve W_q,
convolution, Delta and B by P123.043, P123.109 and P123.111. They
therefore preserve Q and the entire equality (4), with exact coherence
on chart triples. The same holds for adjoints and transported sections.

The corresponding local normal identity uses the probability-normalized
W_loc and the local normal determinant of P123.107. On the tests
e_chi,v_chi of P123.112, where c=c(chi)>0, it gives

    Q_loc(e_chi,e_chi)=-c,
    Q_loc(v_chi,v_chi^*)=-c-1.

Indeed the trace-of-product values are both -c, whereas the anomalies
are zero and one. Thus a positive anomaly energy can coexist with a
negative local trace-product form, with the determinant Hessian accounting
for the difference. This explains the explicit values already obtained;
it proves no global sign and assumes no positivity in defining lambda.

## 4. Exact remaining geometric task

Equation (4) supplies the analytic quadratic comparison among three
previously distinct constructions, with a common domain, original
normalization and semilocal maps. It determines the second variation
that a proposed geometric determinant comparison would have to reproduce.

It does not identify lambda with the logarithm of the metric of the
intrinsic ruling/mixed determinant, identify B with a geometric boundary
term, or realize every designated mixed correspondence by these scalar
test operators. Those identifications, higher diagonal homology and
multi-stratum gluing are still necessary for A. A second-variation
identity alone is not the full RR equality or its metric normalization.
