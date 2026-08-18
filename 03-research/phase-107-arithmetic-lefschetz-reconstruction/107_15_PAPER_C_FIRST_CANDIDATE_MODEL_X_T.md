# 107.15 -- Paper C, Part III: first concrete candidate for the finite model \(\mathcal X_T\)

## 1. Purpose

This note makes the first concrete move beyond the blueprint level of
`107_10`.  Its goal is to propose an actual candidate construction for
the finite-support model \(\mathcal X_T\), using only ingredients that
already appear in the current program:

1. the Connes--Consani moduli of framed arithmetic divisors;
2. the cyclotomic/root-cover local charts;
3. the common archimedean boundary page.

The claim of the present note is modest but real:

\[
 \text{``candidate model produced''}
 \quad\text{is stronger than}\quad
 \text{``model existence merely postulated.''}
 \tag{1.1}
\]

No proof of correctness is claimed yet.  The output is a first explicit
construction protocol for \(\mathcal X_T\) and for its basic generator
cycles.

## 2. Inputs

The construction uses four already fixed inputs.

### 2.1. Framed arithmetic divisors

Phase 39 records Connes--Consani's 2026 identification of the adelic
monoid \(Y_{\mathbb Q}\) with the moduli of framed arithmetic divisors
\((L,\xi,\tau)\), where:

1. \(L\) is a torsion-free rank-one abelian group;
2. \(\xi\) is framing data at the finite part;
3. \(\tau\) is the archimedean seminorm datum.

This gives a source moduli object with genuine multiplicative/tensor
structure and a built-in boundary.

### 2.2. Local cyclotomic charts

`107_04` and `106.210` identify the correct finite local prime-power
support through the cyclotomic/root-cover strata.  These are the charts
that must be visible in any classical realization.

### 2.3. Common phase boundary

`107_08` fixes the common archimedean phase boundary as the structure
that glues the prime towers, while `107_05` and `106.195` determine the
Gamma--polar metric that must appear on that boundary.

### 2.4. Two-ruling and diagonal requirements

`107_10` requires two transverse rulings, a diagonal class, and
nontrivial degree one.  Therefore a single chart such as
\(\mathrm{Spec}\,\mathbb Z[x]\) is insufficient from the outset.

## 3. Finite support data at level \(T\)

Fix \(T>0\) and define

\[
 S_T=\{(p,k):k\log p\le T\}.
 \tag{3.1}
\]

Put

\[
 L_T=\prod_{\log p\le T}p^{\lfloor T/\log p\rfloor}
\]

and let \(N_T=\{n:n\mid L_T\}\).  This is the finite divisor lattice of
rooted return labels visible at level \(T\).  It is closed under gcd and
lcm, but it is not a multiplicative monoid unless it is trivial.
Multiplication is a partial operation at fixed level: \(m,n\in N_T\)
may be multiplied only when \(mn\mid L_T\).  Unrestricted
multiplication maps to a larger support level.

The construction of \(\mathcal X_T\) should remember only these finite
support labels while remaining proper over all of
\(\mathrm{Spec}\,\mathbb Z\).

## 4. Ambient square before regularization

### Definition 4.1: framed-divisor square

Let \(\widetilde{\mathrm{Pic}}_{\rm fr}\) denote the Connes--Consani
moduli of framed arithmetic divisors \((L,\xi,\tau)\).  Define the
ambient square

\[
 \mathfrak S:=\widetilde{\mathrm{Pic}}_{\rm fr}\times
 \widetilde{\mathrm{Pic}}_{\rm fr}.
 \tag{4.1}
\]

Its two projections provide the formal source of the vertical and
horizontal rulings, and its diagonal provides the formal equality locus
of arithmetic divisor data.

The object \(\mathfrak S\) is not yet a regular proper arithmetic
surface.  It is the ambient moduli square in which the finite-support
classical envelope will be cut out.

## 5. Finite-support incidence locus

The square \(\mathfrak S\) becomes useful once one inserts the actual
finite visible order set \(N_T\).

### Definition 5.1: prime-power incidence correspondence

For each \(n\in N_T\), define the framed-divisor graph

\[
 \Gamma_n^{\rm fr}
 :=
 \{(x,y)\in\mathfrak S:\ y=n\cdot x\},
 \tag{5.1}
\]

where \(n\cdot x\) denotes tensor multiplication by the framed
prime-power arithmetic divisor corresponding to \(n\).

This is the exact source analogue of the Frobenius-graph picture from
Paper 0 and of the return graphs \(\Gamma_{p,k}\) of `107_07` and
`107_08`.

### Definition 5.2: finite-support union

Let

\[
 \mathfrak U_T
 :=
 \Delta_{\rm fr}\cup
 \bigcup_{n\in N_T}\Gamma_n^{\rm fr}\cup
 B_{\infty,{\rm v}}\cup B_{\infty,{\rm h}},
 \tag{5.2}
\]

where:

1. \(\Delta_{\rm fr}\subset\mathfrak S\) is the diagonal;
2. \(B_{\infty,{\rm v}}\) and \(B_{\infty,{\rm h}}\) are the two
   boundary divisors coming from degeneration of the archimedean
   seminorm in the first and second factor respectively.

The role of the boundary components is to keep the two rulings visible
and to host the Gamma--polar completion.

## 6. Classical envelope candidate

### Definition 6.1: first finite classical envelope

The first candidate model \(\mathcal X_T^{(1)}\) is defined in three
steps.

1. Take the Zariski closure of the finite-support incidence locus
   \(\mathfrak U_T\) inside a chosen compactification
   \(\overline{\mathfrak S}\) of the framed-divisor square.
2. Normalize that closure.
3. Resolve singularities and boundary crossings by a sequence of
   blow-ups supported over:
   the diagonal/boundary intersection strata,
   the self-intersections of distinct \(\Gamma_n^{\rm fr}\),
   and the singular boundary points created by the finite-support
   incidence closure.

The resulting regular proper surface candidate is denoted

\[
 \mathcal X_T^{(1)}.
 \tag{6.1}
\]

This is a candidate rather than a theorem because the present note does
not yet prove that a compactification \(\overline{\mathfrak S}\) with all
the desired comparison properties has been fully constructed.

## 7. Why this candidate avoids the genus-zero trap

### Proposition 7.1: \(\mathcal X_T^{(1)}\) is not built from a genus-zero chart alone

The candidate \(\mathcal X_T^{(1)}\) avoids the precise defect of
\(\mathbb P^1_{\mathbb Z}\) isolated in `106.210`.

Proof.  The genus-zero obstruction in `106.210` came from compactifying a
single cyclotomic chart with no nontrivial degree-one carrier.  By
contrast, \(\mathcal X_T^{(1)}\) is constructed inside the square of the
framed-divisor moduli, whose very purpose is to retain the arithmetic
Picard/Jacobian degree-one information.  The cyclotomic charts enter only
as local support loci inside that larger square.  \(\square\)

This does not yet prove nontrivial degree one on the final regularized
surface, but it removes the most immediate structural failure.

## 8. Realized generator cycles on \(\mathcal X_T^{(1)}\)

The candidate model provides natural first definitions of the source
generators.

### Definition 8.1: rulings

Let

\[
 F_{{\rm v},T}^{(1)},\qquad F_{{\rm h},T}^{(1)}
 \tag{8.1}
\]

be the pullbacks to \(\mathcal X_T^{(1)}\) of the two boundary divisors
of \(\overline{\mathfrak S}\) corresponding to archimedean degeneration
in the first and second factor.

### Definition 8.2: diagonal

Let

\[
 \Delta_T^{(1)}
 \tag{8.2}
\]

be the strict transform on \(\mathcal X_T^{(1)}\) of the framed-divisor
diagonal \(\Delta_{\rm fr}\subset\mathfrak S\).

### Definition 8.3: prime-power correspondences

For \((p,k)\in S_T\), let

\[
 \Gamma_{p,k,T}^{(1)}
 \tag{8.3}
\]

be the strict transform of the graph
\(\Gamma_{p^k}^{\rm fr}\subset\mathfrak S\) on \(\mathcal X_T^{(1)}\).

### Definition 8.4: archimedean fiber

Let

\[
 Z_{\infty,T}^{(1)}
 \tag{8.4}
\]

be the divisor on \(\mathcal X_T^{(1)}\) obtained by pulling back the
common-phase degeneration locus of the framed-divisor boundary and then
taking the component singled out by the Gamma--polar determinant
normalization.

These are the first realized candidates for the generators listed in
`107_03`.

## 9. Expected comparison properties

The candidate \(\mathcal X_T^{(1)}\) is useful only if it is expected to
satisfy the comparison items of `107_10`.  The relevant ones become:

1. off-diagonal intersections of
   \(\Gamma_{p,k,T}^{(1)}\) should reproduce the cyclotomic determinant
   lines of `107_04`;
2. the metric on \(Z_{\infty,T}^{(1)}\) should reproduce the
   Gamma--polar boundary page of `107_05`;
3. \(\Delta_T^{(1)}\) should be the same diagonal locus used in the
   fixed-point formula of `107_09`;
4. the map from framed-divisor data to the Jacobian quotient should make
   the eventual Picard realization of `107_11` visible on the same model.

These expectations are now concrete comparison problems rather than
abstract desiderata.

## 10. New technical subproblems exposed by the candidate

Producing \(\mathcal X_T^{(1)}\) turns Part III into a shorter list of
sharper tasks.

### 10.1. Compactification problem

Construct an explicit compactification \(\overline{\mathfrak S}\) of the
framed-divisor square with boundary components adapted to the
archimedean seminorm degeneration.

### 10.2. Incidence-closure problem

Show that the closure of the finite graphs \(\Gamma_n^{\rm fr}\) inside
\(\overline{\mathfrak S}\) is of finite type and stable under the
required blow-up regularization.

### 10.3. Metric descent problem

Prove that the Gamma--polar determinant metric descends to a genuine
Green metric on the boundary components of \(\mathcal X_T^{(1)}\).

### 10.4. Degree-one visibility problem

Show that passing from the framed-divisor square to the regularized
classical envelope does not kill the relevant degree-one classes.

This is the concrete heart of the future III-B map.

## 11. Status

The current state of Part III is now stronger than it was in `107_10`.

1. `107_10` fixed the abstract architecture of the universal finite
   models.
2. The present note supplies a first explicit candidate:
   a regularized closure of the finite-support framed-divisor incidence
   locus inside a compactified square of Connes--Consani framed
   arithmetic divisors.
3. It also provides first realized candidates for the generator cycles
   \(F_{\mathrm v}\), \(F_{\mathrm h}\), \(\Delta\),
   \(\Gamma_{p,k}\), and \(Z_\infty\).

What remains unproved is exactly what should remain unproved at this
stage:
the compactification, regularization, metric descent, and exact
comparison with Papers A, B, and III-B.
