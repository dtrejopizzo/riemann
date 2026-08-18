# 107.18 -- Paper C, Part VI: the finite framing coordinate from rooted cyclotomic charts

## 1. Purpose

This note addresses the load-bearing unknown isolated in `107_17`: the
finite-type geometry of the framing coordinate \(\xi\).

The aim is not to solve the full Connes--Consani square.  The aim is to
show that, at finite support level \(T\), the framing coordinate needed
for Phase 107 can be modeled by the same rooted/cyclotomic data already
used in the determinant-line package of `107_04`.

The guiding claim is:

\[
 \text{finite framing at level }T
 \quad\approx\quad
 \text{finite rooted cyclotomic quotient at level }T.
 \tag{1.1}
\]

If this approximation is kept literal and finite, it is enough to turn
the chartwise finite-type criterion of `107_17` into an effective
construction target.

## 2. Source inputs

Four earlier ingredients are now combined.

### 2.1. The rooted Jacobian datum

`106.164` identifies the finite root datum of the arithmetic Jacobian
with the character group of

\[
 X=\widehat{\mathbb Z}=\prod_p\mathbb Z_p,
 \qquad
 X^\vee=\mathbb Q/\mathbb Z.
 \tag{2.1}
\]

The multiplicative semigroup action is given by the operators \(V_n\),
whose range projections are the arithmetic singular strata.

### 2.2. Prime periodic fibres

`106.153` and `107_08` identify the prime fibres \(C_p\) and the
prime-power return labels \(p^k\), already organized by logarithmic
length \(k\log p\).

### 2.3. Finite cyclotomic charts

`107_04` proves that the local finite intersection package is controlled
by the cyclotomic strata \(V(\Phi_n)\), with exact support on prime-power
ratios.

### 2.4. Local atlas requirement

`107_17` requires a finite-type local model for the framing coordinate
\(\xi\) on every chart of \(\overline{\mathfrak P}_{\rm fr}\).

## 3. Which roots are visible at level \(T\)

Fix a support bound \(T>0\), and let

\[
 S_T=\{(p,k):k\log p\le T\}.
 \tag{3.1}
\]

Define the visible order set

\[
 \mathcal N_T
 :=
 \{n\ge1:\text{ every prime-power factor }p^k\mid n
 \text{ satisfies }(p,k)\in S_T\}.
 \tag{3.2}
\]

Equivalently, put

\[
 L_T=\prod_{\log p\le T}p^{\lfloor T/\log p\rfloor}.
\]

Then \(\mathcal N_T=\{n:n\mid L_T\}\).  It is a finite lattice under
gcd and lcm, not a multiplicative monoid.  Multiplication is only
partially defined at level \(T\), when the product still divides
\(L_T\); otherwise it maps to a larger support level.

Only torsion characters of order in \(\mathcal N_T\) can be detected by
the finite-support correspondence package at level \(T\).

## 4. Finite visible root space

### Definition 4.1: visible torsion quotient

Let

\[
 X_T^\vee
 :=
 \bigcup_{n\in\mathcal N_T}\frac1n\mathbb Z/\mathbb Z
 \subset
 \mathbb Q/\mathbb Z.
 \tag{4.1}
\]

This is the finite visible rooted dual at level \(T\).

Its Pontryagin dual is the finite quotient

\[
 X_T
 :=
 \widehat{X_T^\vee},
 \tag{4.2}
\]

which is a finite quotient of \(\widehat{\mathbb Z}\) remembering only
the torsion orders visible to level \(T\).

### Proposition 4.1: finite support makes the framing coordinate finite

At fixed level \(T\), the rooted datum needed by Phase 107 factors
through \(X_T\).

Proof.  Every visible generator is labeled by a prime power
\((p,k)\in S_T\).  The finite determinant support of `107_04` detects
only ratios whose orders remain in the multiplicative closure generated
by these labels.  Therefore no rooted character of order outside
\(\mathcal N_T\) can change the finite-support incidence data at level
\(T\).  \(\square\)

This is the first reduction from the infinite rooted datum to a genuine
finite-level object.

## 5. Framing coordinate as cyclotomic label

The local charts of `107_17` used a symbol \(\xi\).  We can now refine
it.

### Definition 5.1: rooted cyclotomic framing coordinate

On a level-\(T\) chart, define the framing coordinate as

\[
 \xi_T=(n,\chi),
 \tag{5.1}
\]

where:

1. \(n\in\mathcal N_T\) is a visible cyclotomic order;
2. \(\chi\in X_T^\vee\) is a torsion character of exact order \(n\).

The pair \((n,\chi)\) is the finite rooted substitute for the abstract
framing datum at level \(T\).

### Interpretation

1. the integer \(n\) is the cyclotomic chart index;
2. the primitive character \(\chi\) chooses a rooted component inside
   that chart;
3. passing from \((n,\chi)\) to \((m,\psi)\) is the finite framing
   change that the graph equations of `107_17` must track.

## 6. Relation with the cyclotomic strata

### Proposition 6.1: visible framing charts map to visible cyclotomic strata

For every \(n\in\mathcal N_T\), the chart labeled by \(n\) maps to the
cyclotomic stratum

\[
 Z_n=V(\Phi_n)
 \tag{6.1}
\]

used in `107_04`.

Proof.  The cyclotomic stratum \(V(\Phi_n)\) is exactly the locus of
primitive \(n\)-torsion roots on the finite side.  The visible rooted
dual \(X_T^\vee\) records torsion characters of the same orders.
Therefore the order parameter in the framing chart and the order
parameter in the cyclotomic chart coincide.  \(\square\)

This does not identify the full moduli problem with the affine
cyclotomic divisor.  It does show that the finite support coordinate
system is already compatible with the local determinant charts.

## 7. The finite action \(\mu_n\)

`107_17` left the local action \(\mu_n\) abstract.  It can now be made
effective.

### Definition 7.1: level-\(T\) finite action

For \(m\in\mathcal N_T\), define

\[
 \mu_m(n,\chi)
 :=
 (mn,\chi^{(m)}),
 \tag{7.1}
\]

whenever \(mn\in\mathcal N_T\), where \(\chi^{(m)}\) is the rooted
character obtained by the multiplicative semigroup action of \(m\) on
the visible torsion quotient.

If \(mn\notin\mathcal N_T\), the action is undefined on the level-\(T\)
chart and belongs to a larger support level.

### Proposition 7.1: \(\mu_m\) is finite-type on level-\(T\) charts

The map \(\mu_m\) is a finite combinatorial morphism on the finite chart
set of Definition 5.1.

Proof.  Both \(n\) and \(\chi\) take values in finite sets at fixed
level \(T\), and multiplication by \(m\) preserves the visible set
precisely when \(mn\in\mathcal N_T\).  Thus \(\mu_m\) is a finite map of
finite chart data.  \(\square\)

This is exactly the missing finite-type ingredient required by
Criterion 8.1 of `107_17`.

## 8. Effective chartwise finite-type criterion

We can now restate the chartwise criterion in effective form.

### Criterion 8.1: effective finite-type test for \(\overline{\Gamma}_m^{\rm fr}\)

Fix \(T\) and \(m\in\mathcal N_T\).  In the local chart coordinates

\[
 ((n_1,\chi_1),q_1,\theta_1;
  (n_2,\chi_2),q_2,\theta_2),
 \tag{8.1}
\]

the graph closure \(\overline{\Gamma}_m^{\rm fr}\) is cut out by

\[
 (n_2,\chi_2)=\mu_m(n_1,\chi_1),
 \qquad
 q_2=q_1,
 \qquad
 \theta_2=\theta_1,
 \tag{8.2}
\]

or by the corresponding \(u\)- or \(v\)-boundary versions.

Since:

1. \((n_i,\chi_i)\) lie in a finite chart set;
2. \(q_i\) and \(\theta_i\) are one-dimensional local coordinates;
3. \(\mu_m\) is finite combinatorial data;

the chartwise graph closure problem is reduced to finitely many local
equations on finite chart packets.

This is still not a proof that the global compactification is of finite
type, but it is an candid effective reduction of the problem.

## 9. Consequences for \(\mathcal X_T^{(1)}\)

The candidate model of `107_15` becomes more concrete in two ways.

1. The finite framing coordinate \(\xi\) can now be replaced by the
   explicit visible rooted cyclotomic coordinate \((n,\chi)\).
2. The graph closures and diagonal equations can be tested on finitely
   many local root/cyclotomic packets rather than on an abstract infinite
   moduli problem.

This is exactly the sort of finite-support reduction the Phase 107
design principle predicted.

## 10. What is still missing

The present note does not prove three things.

1. That the framed-divisor charts with coordinates \((n,\chi)\) glue to
   the full compactified factor \(\overline{\mathfrak P}_{\rm fr}\).
2. That the resulting regularization of the incidence locus is proper and
   regular over all of \(\operatorname{Spec}\mathbb Z\).
3. That the Gamma--polar boundary metric descends adelically or
   Arakelov-theoretically on the regularized model.

Those are still the next real construction/proof fronts.

## 11. Next technical front

The natural next step after this note is to use the effective framing
coordinate \((n,\chi)\) to define the realized generator cycles
\(\Gamma_{p,k,T}^{(1)}\), \(\Delta_T^{(1)}\), \(F_{{\rm v},T}^{(1)}\),
\(F_{{\rm h},T}^{(1)}\) more explicitly on the finite packet charts and
to compare their local intersections with the determinant lines of
`107_04`.

That would be the first direct bridge from the candidate model of
Part III back to the already proved arithmetic package of Part I.

## 12. Status

Part III has now moved one step further from abstract geometry toward
effective finite charts.

1. `107_15` gave a candidate model \(\mathcal X_T^{(1)}\).
2. `107_16` gave the compactified square and the boundary metric line.
3. The present note gives an effective finite replacement for the
   framing coordinate \(\xi\), derived from the same rooted/cyclotomic
   data that controls the determinant package.

The next unresolved issue is no longer "what could \(\xi\) be?" but
"how do these finite framing packets glue and how do their cycle
intersections reproduce the source determinant lines?"
