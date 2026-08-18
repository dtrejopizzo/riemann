# 106.129 — Operator-valued Picone transform and the radical-connection gate

## 1. Purpose and verdict

The complete ordinary-prime--Gamma generator \(A\) has the infinite exact
threshold eigenspace

\[
 \mathcal R\subset L^2_0(\mu_K),
 \qquad
 Ar=\frac12r
 \quad(r\in\mathcal R).
 \tag{1}
\]

A scalar positive threshold state would give a Picone--Doob transform of
\(A-\frac12\).  Document 106.19 tested that rank-one mechanism.  The
present note tests the genuinely different possibility suggested by the
full radical: use all threshold states as a vector-valued ground state,
then absorb their rotations by a matrix connection.

There is an exact answer.

1. Every finite or regularized infinite threshold frame satisfies a
   vector-valued Picone identity.  Its transformed edge conductance is the
   radical correlation kernel

   \[
    P_{\mathcal V}(x,y)
    =\langle\mathcal V(x),\mathcal V(y)\rangle.
    \tag{2}
   \]

2. This conductance is necessarily signed.  Every radical coordinate is
   centered, hence \(P_{\mathcal V}(x,\cdot)\) has mean zero.  Wherever
   \(\mathcal V(x)\ne0\), it takes both signs.  The continuous Gamma
   channel sees both sign regions with strictly positive edge measure.
   No positive pointwise normalization changes those signs.
3. Polar alignment replaces \(P_{\mathcal V}\) by
   \(|P_{\mathcal V}|\), but creates an exact nonnegative connection
   defect supported on the negative-correlation edges.  The transformed
   identity is a Krein difference of two squares, not a Hilbert square.
4. The mean-periodic equation does not annihilate the connection defect.
   The local universality theorem of 106.126 constructs exact
   mean-periodic rows with arbitrary prescribed difference across any
   negative-correlation rectangle.
5. There is also a pointwise rank obstruction: evaluation of an
   infinite-dimensional scalar eigenspace is a rank-one map.  The
   operator-valued transform controls the vector family
   \((ae_j)_j\), not an arbitrary scalar \(q\).  Passing through its
   Moore--Penrose inverse is exactly where the signed connection reappears.

Consequently the multi-radical transform is exact but does not prove
\(A-\frac12\ge0\) on the complement.  It gives the precise missing
inequality: the positive aligned energy must dominate the radical
connection defect.  That domination is another form of the physical
surplus, not a consequence of the threshold eigenmap.

## 2. Prior-route audit

The calculation below is not the rank-one ground-state transform of
106.19.

* 106.19 uses one strictly positive scalar \(v\) and obtains conductance
  \(v(x)v(y)\ge0\).  The problem there is the missing Poincare constant.
* 106.41 proves the strong identities \(Ar=\frac12r\) on the whole
  radical and identifies the desired inequality with the spectral floor
  on \((\mathbf1\oplus\mathcal R)^\perp\).
* 106.51 and 106.54--106.60 audit the scalar \(\Gamma_2\), ordered-current
  and primitive-\(j_2\) routes.  They retain intermediate positions but do
  not use an operator-valued threshold frame.
* 106.68 and 106.121 compute the maximal Gamma anti-short.  Its missing
  term is the shorted positive prime-tail distance.
* 106.105 proves that every exact source-side transfer has the same
  singular-value threshold; changing its realization cannot create a
  contraction.
* 106.111 and 106.113 exclude local Hodge squares and infinite bounded
  boundary fluxes.
* 106.126 proves local universality of the exact mean-periodic complement,
  which is used below to test whether the new connection defect vanishes
  on physical rows.

The new object is the radical correlation conductance (2), together with
its exact positive/negative edge decomposition.

## 3. Reversible-jump setup

Let

\[
 \mathscr H=L^2(\mu_K)
 \tag{3}
\]

and let \(\mathfrak j\) be the symmetric edge measure of the complete
ordinary-prime--Gamma generator.  On the common form core,

\[
 \mathscr E_K(f,g)
 =\frac12\iint
   \{\overline{f(x)-f(y)}\}\{g(x)-g(y)\}
   \,d\mathfrak j(x,y)
 =\langle f,Ag\rangle_{\mu_K}.
 \tag{4}
\]

The Gamma part has the everywhere-positive off-diagonal density

\[
 d\mathfrak j_\Gamma(x,y)
 =K(x)K(y)g(|x-y|)\,dx\,dy,
 \qquad
 g(u)=\frac{e^{-u/2}}{1-e^{-2u}}>0.
 \tag{5}
\]

Thus every nonempty open rectangle disjoint from the diagonal has positive
\(\mathfrak j\)-measure.

Fix a finite-dimensional threshold subspace
\(\mathcal R_m\subset\mathcal R\), and let
\(e_1,\ldots,e_m\) be a real orthonormal basis.  Define the evaluation
feature and its correlation kernel by

\[
 \mathcal V_m(x)
 =(e_1(x),\ldots,e_m(x))\in\mathbb R^m,
 \qquad
 P_m(x,y)
 =\mathcal V_m(x)\cdot\mathcal V_m(y).
 \tag{6}
\]

Every component obeys

\[
 Ae_j=\lambda_*e_j,
 \qquad
 \lambda_*=\frac12.
 \tag{7}
\]

## 4. The exact vector-valued Picone identity

### Theorem 1 — Radical-frame Picone identity

For every real scalar \(a\) in a common bounded form core,

\[
 \boxed{
 \sum_{j=1}^m
 \left\{
   \mathscr E_K(ae_j)-\lambda_*\|ae_j\|^2
 \right\}
 =
 \frac12\iint
 P_m(x,y)|a(x)-a(y)|^2\,d\mathfrak j(x,y).}
 \tag{8}
\]

More generally, for positive weights \(w_j\), the same identity holds with

\[
 P_{m,w}(x,y)=\sum_{j=1}^m w_je_j(x)e_j(y)
 \tag{9}
\]

and the left side weighted by \(w_j\).

#### Proof

The vector energy of \(a\mathcal V_m\) is

\[
 \begin{aligned}
 &\frac12\iint
 \|a(x)\mathcal V_m(x)-a(y)\mathcal V_m(y)\|^2
 \,d\mathfrak j(x,y)\\
 &\quad=\sum_{j=1}^m\mathscr E_K(ae_j).
 \end{aligned}
 \tag{10}
\]

The componentwise eigen-equation gives, after disintegrating the symmetric
edge measure,

\[
 \int
 \{P_m(x,x)-P_m(x,y)\}\,d\mathfrak j_x(y)
 =\lambda_*P_m(x,x).
 \tag{11}
\]

Expand (10), subtract
\(\lambda_*\int |a(x)|^2P_m(x,x)d\mu_K(x)\), use (11), and symmetrize.
The coefficients of \(|a(x)|^2\) and \(|a(y)|^2\) reduce to
\(P_m(x,y)\), while the cross term is
\(-2P_m(x,y)a(x)a(y)\).  This gives exactly the right side of (8).
The weighted formula follows by replacing \(e_j\) with
\(\sqrt{w_j}e_j\). \(\square\)

This is the genuine multi-ground-state analogue of Picone.  It involves
no chosen positive radical vector and no spectral assumption away from
the exact threshold identity (7).

### Normalized form

Put

\[
 \rho_m(x)=\|\mathcal V_m(x)\|,
 \qquad
 \Phi_m(x)=\frac{\mathcal V_m(x)}{\rho_m(x)}
 \tag{12}
\]

where \(\rho_m>0\), and define

\[
 \kappa_m(x,y)
 =\langle\Phi_m(x),\Phi_m(y)\rangle.
 \tag{13}
\]

For \(a=f/\rho_m\), (8) becomes

\[
 \boxed{
 \sum_{j=1}^m
 \left\{
 \mathscr E_K\!\left(\frac{f}{\rho_m}e_j\right)
 -\lambda_*
  \left\|\frac{f}{\rho_m}e_j\right\|^2
 \right\}
 =
 \frac12\iint
 \rho_m(x)\rho_m(y)\kappa_m(x,y)
 \left|
 \frac{f(x)}{\rho_m(x)}
 -\frac{f(y)}{\rho_m(y)}
 \right|^2d\mathfrak j.}
 \tag{14}
\]

Positive normalization changes the magnitude of the conductance but not
the sign of \(\kappa_m\).

## 5. The radical correlation is necessarily signed

### Theorem 2 — Zero-mean correlation obstruction

For every nonzero finite radical frame and for almost every \(x\) with
\(\mathcal V_m(x)\ne0\), the function

\[
 y\longmapsto P_m(x,y)
 \tag{15}
\]

takes both positive and negative values on sets of positive
\(\mu_K\)-measure.  Consequently its positive and negative regions both
have positive Gamma edge measure.

#### Proof

Every \(e_j\) is centered.  Therefore

\[
 \int P_m(x,y)\,d\mu_K(y)
 =\sum_{j=1}^me_j(x)\int e_j(y)\,d\mu_K(y)
 =0.
 \tag{16}
\]

On the other hand, orthonormality gives

\[
 \int P_m(x,y)^2\,d\mu_K(y)
 =\sum_{i,j}e_i(x)e_j(x)\langle e_i,e_j\rangle
 =P_m(x,x)>0.
 \tag{17}
\]

Thus (15) is nonzero and has mean zero.  It cannot be nonnegative or
nonpositive almost everywhere, so it has both signs on positive-measure
sets.  The radical functions are analytic.  A strict sign at one pair
therefore persists on an open rectangle.  Equation (5) assigns positive
Gamma edge measure to every such rectangle. \(\square\)

### Corollary 3 — Positive Doob normalization is impossible

For any positive measurable \(d(x)\), the normalized kernel

\[
 d(x)P_m(x,y)d(y)
 \tag{18}
\]

has the same negative edge region as \(P_m\).  Hence no positive scalar
normalization of the threshold frame turns (8) into a positive Dirichlet
form.

This is an intrinsic consequence of centering the whole threshold
eigenspace.  It is not a poor choice of basis: \(P_m\) is the integral
kernel of the orthogonal projection onto \(\mathcal R_m\), so it is
basis-independent.

## 6. Polar alignment and the exact connection defect

Write

\[
 P_m=P_m^+-P_m^-,
 \qquad
 P_m^\pm\ge0,
 \qquad
 |P_m|=P_m^++P_m^-.
 \tag{19}
\]

Define the aligned energy and the connection defect by

\[
 \begin{aligned}
 \mathscr P_m(a)
 &:=\frac12\iint |P_m(x,y)|
       |a(x)-a(y)|^2\,d\mathfrak j(x,y),\\
 \mathscr C_m(a)
 &:=\iint_{\{P_m<0\}}|P_m(x,y)|
       |a(x)-a(y)|^2\,d\mathfrak j(x,y).
 \end{aligned}
 \tag{20}
\]

### Theorem 4 — Krein factorization of the vector Picone transform

\[
 \boxed{
 \sum_{j=1}^m
 \left\{\mathscr E_K(ae_j)-\lambda_*\|ae_j\|^2\right\}
 =\mathscr P_m(a)-\mathscr C_m(a).}
 \tag{21}
\]

Equivalently, with

\[
 (Q_m^\pm a)(x,y)
 =\sqrt{\frac{P_m^\pm(x,y)}2}\{a(x)-a(y)\},
 \tag{22}
\]

one has

\[
 \boxed{
 \sum_{j=1}^m
 \left\{\mathscr E_K(ae_j)-\lambda_*\|ae_j\|^2\right\}
 =\|Q_m^+a\|^2-\|Q_m^-a\|^2.}
 \tag{23}
\]

#### Proof

Substitute (19) into (8).  Since
\(|P_m|-P_m=2P_m^-\), equations (20)--(23) follow directly. \(\square\)

The operation which rotates each pair of radical feature vectors to make
their correlation positive replaces \(P_m\) by \(|P_m|\).  Equation (21)
shows the exact price of that edgewise polar alignment:
\(\mathscr C_m\).  It is nonnegative, nonlocal and of the same quadratic
order as the proposed square.  Dropping it is precisely the invalid step.

## 7. Mean periodicity does not remove the connection defect

One could hope that the physical constraint

\[
 q\perp\mathbf1\oplus\mathcal R
 \quad\Longleftrightarrow\quad
 (hq)*K=0
 \tag{24}
\]

forces \(\mathscr C_m(q)=0\).  It does not.

### Theorem 5 — Nonvanishing on exact mean-periodic rows

For every nonzero finite radical frame there is a real-even exact
mean-periodic graph-domain row \(q\) for which

\[
 \boxed{\mathscr C_m(q)>0.}
 \tag{25}
\]

#### Proof

By Theorem 2, choose disjoint bounded open intervals \(U,V\), together
with their reflections, so that

\[
 P_m(x,y)<-\eta<0
 \qquad(x\in U,\ y\in V)
 \tag{26}
\]

for some \(\eta>0\).  Choose an even smooth profile which is one on
\(U\cup(-U)\) and zero on \(V\cup(-V)\).  By the local universality
theorem 106.126, exact real-even elementary mean-periodic rows approximate
this profile in the local second-logarithmic topology on the union of
these intervals.  Multiplication by \(h^{-1}\) is a local isomorphism in
that topology, so one obtains a graph-domain
\(q\in(\mathbf1\oplus\mathcal R)^\perp\) whose difference is nonzero on a
positive-measure subset of \(U\times V\).

Equations (5), (20) and (26) then give

\[
 \mathscr C_m(q)
 \ge
 \eta\iint_{U\times V}|q(x)-q(y)|^2
 \,d\mathfrak j_\Gamma(x,y)>0.
 \tag{27}
\]

Thus (24) does not annihilate the connection defect. \(\square\)

The use of 106.126 is decisive: the mean-periodic divisor is locally
overcomplete, so no nonzero local edge functional can vanish on all
physical rows.

## 8. Why the trace identity is not a factorization of \(A-\frac12\)

At each point \(x\), evaluation on the radical is the map

\[
 \mathrm{ev}_x:\mathcal R_m\to\mathbb C,
 \qquad r\mapsto r(x).
 \tag{28}
\]

For \(m>1\), this map has rank at most one.  It is not an invertible matrix
ground state.  Accordingly, Theorem 1 controls the vector family

\[
 a\mathcal V_m=(ae_1,\ldots,ae_m),
 \tag{29}
\]

not an arbitrary scalar row \(q\).

The normalized embedding

\[
 J_mf(x)=f(x)\Phi_m(x)
 \tag{30}
\]

is pointwise isometric into a vector bundle, but its edgewise parallel
transport has correlation \(\kappa_m(x,y)\).  Taking the polar part of
that transport produces \(|\kappa_m|\) and hence exactly the defect
\(\mathscr C_m\).  Taking a Moore--Penrose inverse of (28) produces the
same projective connection, now as derivatives or jumps of the rank-one
projection

\[
 \Pi_m(x)=|\Phi_m(x)\rangle\langle\Phi_m(x)|.
 \tag{31}
\]

Therefore there is no algebraic passage from (21) to

\[
 \langle q,(A-\tfrac12)q\rangle
 =\|Qq\|^2
 \qquad(q\perp\mathbf1\oplus\mathcal R)
 \tag{32}
\]

without proving a new domination of the connection term.  If (32) held,
it would already be the physical floor.

## 9. Regularized infinite radical

The obstruction is not caused by truncating the radical.  Let
\((e_j)_{j\ge1}\) be an orthonormal basis of \(\mathcal R\), and choose
positive weights \(w_j\downarrow0\) so rapidly that

\[
 P_w(x,y)=\sum_{j\ge1}w_je_j(x)e_j(y)
 \tag{33}
\]

converges locally with the derivatives required by the form core.  The
weights may be chosen still faster so that the two series in Theorem 1
are absolutely convergent on any prescribed countable core.  The weighted
identity then passes to the limit by dominated convergence before the
positive/negative split.
Moreover,

\[
 \int P_w(x,y)\,d\mu_K(y)=0,
 \qquad
 \int P_w(x,y)^2\,d\mu_K(y)
 =\sum_jw_j^2e_j(x)^2.
 \tag{34}
\]

Thus every nonzero row of \(P_w\) again has both signs.  The infinite
operator-valued threshold eigenmap therefore produces the same Krein
factorization and the same connection defect.  No limiting choice of
positive weights converts it into a positive edge kernel.

## 10. Exact surviving inequality

The vector-valued Picone construction reduces its own positivity to

\[
 \boxed{
 \mathscr P_m(a)\ge\mathscr C_m(a)}
 \tag{35}
\]

for the amplitudes generated by the physical scalar row, uniformly along
a cofinal radical frame.  Equation (35) is not supplied by mean
periodicity, by Theorem 5.  Nor is it automatic from Cauchy--Schwarz:
\(\mathscr P_m-\mathscr C_m\) is exactly the signed right side of (8).

The full scalar target remains

\[
 \boxed{
 \langle q,(A-\tfrac12)q\rangle\ge0,
 \qquad
 q\perp\mathbf1\oplus\mathcal R.}
 \tag{36}
\]

The multi-radical transform explains why no positive ground-state
factorization has emerged.  A scalar positive ground state has positive
edge products but cannot span the centered radical.  The complete
operator-valued ground state spans the radical but necessarily has signed
edge correlations.  Polar alignment restores positivity only by adding
the nonzero connection cost (20).

Thus this route does not give \(A-\frac12=Q^*Q\).  Its exact obstruction
is the radical projective connection on negative-correlation Gamma edges.
A successor would have to dominate that connection by a jointly signed
ordinary-prime--Gamma term after anti-shorting.  Such a domination is the
physical surplus in a new exact coordinate, not a free Riccati identity.
