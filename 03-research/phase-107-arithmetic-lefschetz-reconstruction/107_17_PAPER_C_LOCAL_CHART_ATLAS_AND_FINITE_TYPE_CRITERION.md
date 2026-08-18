# 107.17 -- Paper C, Part V: local chart atlas for \(\overline{\mathfrak P}_{\rm fr}\) and a finite-type criterion

## 1. Purpose

This note continues the concrete realization program of `107_15` and
`107_16`.  Its task is to replace the still-global compactification
picture by a local chart model for the compactified framed-divisor
factor

\[
 \overline{\mathfrak P}_{\rm fr},
 \tag{1.1}
\]

and to derive from that chart model a first finite-type criterion for
the closed graphs

\[
 \overline{\Gamma}_n^{\rm fr}\subset\overline{\mathfrak S}.
 \tag{1.2}
\]

The point is again concrete but limited:

\[
 \text{``local atlas fixed''}
 \quad\Longrightarrow\quad
 \text{``finite-support closures can now be tested chartwise.''}
 \tag{1.3}
\]

This is still short of a proof that the full compactification exists as
an arithmetic algebraic stack or scheme.  It does turn the next steps
into finitely many local conditions.

## 2. Minimal coordinate package

The inputs isolated in `107_16` suggest that one framed divisor should
be resolved into three types of local data:

1. a finite framing coordinate;
2. an archimedean scale coordinate;
3. a common phase coordinate.

### Definition 2.1: local framed-divisor coordinate triple

A local point of \(\overline{\mathfrak P}_{\rm fr}\) is modeled by a
triple

\[
 (\xi,q,\theta),
 \tag{2.1}
\]

where:

1. \(\xi\) is the finite framing coordinate, recording the rooted
   rank-one arithmetic lattice modulo the chosen local trivialization;
2. \(q\in[0,\infty]\) is the archimedean scale coordinate;
3. \(\theta\in\mathbb S^1\) is the common phase coordinate.

The interior corresponds to \(0<q<\infty\), the lower boundary to
\(q=0\), and the upper boundary to \(q=\infty\).

## 3. Four-chart atlas of the compactified factor

The smallest useful atlas is obtained by splitting according to the
archimedean scale regime.

### Chart A: interior chart

\[
 U_{\rm mid}=\{(\xi,q,\theta):0<q<\infty\}.
 \tag{3.1}
\]

This is the Riemann-sector chart on which the source moduli lives before
compactification.

### Chart B: lower boundary chart

\[
 U_0=\{(\xi,u,\theta):u=q,\ 0\le u<\varepsilon\},
 \tag{3.2}
\]

for a small formal boundary parameter \(u\).

This chart resolves the degeneration \(q\to0\).

### Chart C: upper boundary chart

\[
 U_\infty=\{(\xi,v,\theta):v=q^{-1},\ 0\le v<\varepsilon\}.
 \tag{3.3}
\]

This chart resolves the opposite boundary \(q\to\infty\).

### Chart D: scale-invariant overlap chart

Because the Phase 107 compactification identifies the two scale
extremes through the scaling action, we also retain the quotient chart

\[
 U_{\rm sc}=\{(\xi,\sigma,\theta)\},
 \qquad
 \sigma=\log q \ \text{mod the global scaling relation}.
 \tag{3.4}
\]

This is not an extra geometric stratum; it is the bookkeeping chart that
glues the lower and upper boundary descriptions to the same boundary
family after quotienting by scale.

## 4. Transition functions

The boundary atlas is useful only if the charts glue by explicit
transitions.

### Proposition 4.1: local transition laws

On the overlaps where both sides are defined, the chart transitions are:

\[
 u=q,
 \qquad
 v=q^{-1},
 \qquad
 uv=1
 \quad
 (0<q<\infty),
 \tag{4.1}
\]

with \(\xi\) and \(\theta\) unchanged.

Proof.  The finite framing and common phase are source invariants of the
local point.  Only the archimedean size variable changes between
interior and boundary charts, and the compactification protocol of
`107_16` records precisely the two reciprocal degenerations \(q\to0\)
and \(q\to\infty\).  \(\square\)

Thus the local compactification behaves like a one-parameter normal
crossing completion over a fixed finite/phase base.

## 5. Local charts on the square

Passing to the square doubles the scale coordinates and keeps one phase
coordinate per factor.

### Definition 5.1: square chart coordinates

A local chart of \(\overline{\mathfrak S}\) is described by

\[
 (\xi_1,q_1,\theta_1;\xi_2,q_2,\theta_2).
 \tag{5.1}
\]

The vertical boundary is \(q_1\in\{0,\infty\}\), the horizontal
boundary is \(q_2\in\{0,\infty\}\), and the common corner of `107_16`
occurs when both factors are at a boundary value after scale
identification.

### Definition 5.2: corner chart

The corner chart is modeled by

\[
 U_{\rm cor}=\{(\xi_1,u_1,\theta_1;\xi_2,u_2,\theta_2)\},
 \tag{5.2}
\]

with \(u_1,u_2\) boundary parameters and the common-corner locus cut out
by the phase-matching equation

\[
 \theta_1=\theta_2.
 \tag{5.3}
\]

On the diagonal one also imposes \(\xi_1=\xi_2\).

## 6. Local form of the diagonal

### Proposition 6.1: diagonal equations in local charts

In every local square chart, the compactified diagonal is cut out by the
equations

\[
 \xi_1=\xi_2,
 \qquad
 \theta_1=\theta_2,
 \qquad
 q_1=q_2
 \tag{6.1}
\]

whenever the scale coordinates are simultaneously defined, and by their
boundary-chart versions

\[
 \xi_1=\xi_2,
 \qquad
 \theta_1=\theta_2,
 \qquad
 u_1=u_2
 \tag{6.2}
\]

or

\[
 \xi_1=\xi_2,
 \qquad
 \theta_1=\theta_2,
 \qquad
 v_1=v_2
 \tag{6.3}
\]

near the lower or upper boundary.

Proof.  The diagonal is equality of framed divisors.  In the local atlas
of Definition 2.1 this means equality of all three coordinate types.
\(\square\)

This gives the first genuinely local description of where the
Gamma--polar correction must meet the diagonal.

## 7. Local form of the prime-power graphs

The graphs \(\Gamma_n^{\rm fr}\) become explicit in the same charts.

### Definition 7.1: finite action on local coordinates

For \(n\in N_T\), define its local action by

\[
 n\cdot(\xi,q,\theta)
 =
 (\mu_n(\xi),q,\theta),
 \tag{7.1}
\]

where \(\mu_n\) is the finite framing action induced by multiplication by
the framed divisor labeled by \(n\).

The source reason for keeping \(q\) and \(\theta\) unchanged is that the
prime-power return acts on the arithmetic lattice/framing sector while
the common phase boundary is shared across towers.

### Proposition 7.1: graph equations in local charts

In every local square chart, the graph \(\Gamma_n^{\rm fr}\) is cut out
by

\[
 \xi_2=\mu_n(\xi_1),
 \qquad
 q_2=q_1,
 \qquad
 \theta_2=\theta_1.
 \tag{7.2}
\]

Near the lower boundary these become

\[
 \xi_2=\mu_n(\xi_1),
 \qquad
 u_2=u_1,
 \qquad
 \theta_2=\theta_1,
 \tag{7.3}
\]

and similarly with \(v_1,v_2\) near the upper boundary.

Proof.  By definition \(\Gamma_n^{\rm fr}\) is the graph of the
finite-action map \(x\mapsto n\cdot x\).  Under Definition 7.1 this map
changes only the finite framing coordinate.  \(\square\)

This is precisely what makes the graph closures compatible with the
corner \(C_\infty\): they all share the same phase and scale equations at
the boundary.

## 8. First finite-type criterion

The finite-support graphs are now local equalizers of finitely many
coordinate equations.

### Criterion 8.1: chartwise finite-type closure test

Fix \(T\) and hence the finite monoid \(N_T\).  Suppose that on every
chart of the atlas above:

1. the finite framing coordinate \(\xi\) is modeled by a finite-type
   arithmetic parameter space for the labels visible up to \(T\);
2. the boundary parameters \(u,v\) are one-dimensional normal-crossing
   coordinates;
3. the phase coordinate \(\theta\) is carried by one fixed compact
   phase factor;
4. each local action \(\mu_n\) is given by a finite-type morphism on the
   finite framing chart.

Then every closed graph

\[
 \overline{\Gamma}_n^{\rm fr}
 \subset
 \overline{\mathfrak S}
 \tag{8.1}
\]

is locally cut out by finitely many equations inside a finite product of
finite-type local spaces.  Consequently the union

\[
 \overline{\Delta}_{\rm fr}
 \cup
 \bigcup_{n\in N_T}\overline{\Gamma}_n^{\rm fr}
 \cup
 B_{\rm v}\cup B_{\rm h}
 \tag{8.2}
\]

is a chartwise finite-type incidence locus.

This is not yet a global theorem because the finite-type status of the
framing charts and of the phase factor has not been fully proved in the
current Phase 107 tree.  It is the first explicit local criterion the
future proof must check.

## 9. Boundary metric in local charts

The line \(\mathcal L_\infty\) from `107_16` also becomes local in these
charts.

### Definition 9.1: local corner generator

On the corner chart \(U_{\rm cor}\), let \(s_{\rm cor}\) be the local
generator of the boundary metric line defined by the normal-crossing
product

\[
 s_{\rm cor}=u_1u_2
 \tag{9.1}
\]

in lower-boundary coordinates, or by the corresponding \(v_1v_2\)
expression in upper-boundary coordinates.

The Gamma--polar metric descent protocol is then:

\[
 \|s_{\rm cor}\|_{\Gamma,\rm pol}
 =
 \exp(-G_{\Gamma,\rm pol}),
 \tag{9.2}
\]

where \(G_{\Gamma,\rm pol}\) is the same Green potential already fixed
abstractly in `107_05` and `107_16`.

### Proposition 9.1: local metric compatibility target

If the local norm (9.2) glues across chart transitions, then the
boundary metric line \(\mathcal L_\infty\) acquires a well-defined
candidate Green metric on the compactified square.

Proof.  The only nontrivial gluing issue is compatibility under the
transition laws (4.1).  Those laws affect only the scale coordinates, so
the Green potential must be invariant under the scale-identified change
of boundary chart.  This is exactly the descent statement to be checked.
\(\square\)

This makes the metric descent problem explicitly local.

## 10. Immediate consequences for \(\mathcal X_T^{(1)}\)

With the local atlas fixed, the regularization candidate of `107_15`
becomes more concrete.

1. Singularities of the incidence locus are now localized to finite
   intersections of the equations in (6.1)--(7.3).
2. The corner \(C_\infty\) is locally modeled by a normal-crossing pair
   of boundary parameters.
3. The diagonal and every graph closure meet the same local corner
   equations.
4. The admissibility problem for the metric is reduced to gluing the
   local norm (9.2).

This is enough to identify the next unresolved issue sharply.

## 11. Next technical front

The most immediate unresolved front after this note is:

\[
 \text{construct explicit finite-type local models for the framing coordinate } \xi.
 \tag{11.1}
\]

Once those framing charts are explicit, Criterion 8.1 can be tested for
real rather than formally.

The next note should therefore attack one of two paths:

1. an candid finite-type atlas for the finite framing sector visible up
   to \(T\); or
2. a comparison between the finite framing sector and the rooted
   cyclotomic charts already used in `107_04`.

## 12. Status

Part III now has:

1. a first candidate model \(\mathcal X_T^{(1)}\) in `107_15`;
2. a first compactified square and boundary metric protocol in
   `107_16`;
3. a local chart atlas and a first finite-type criterion in the present
   note.

This is still not a finished construction, but it is no longer a purely
global wish list.  The compactification, graph closure, and metric
descent problems have all been reduced to chartwise checks with a single
remaining load-bearing unknown: the explicit finite-type geometry of the
framing coordinate.
