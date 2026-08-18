# 106.151 — Source-stable determinant and the oriented-surplus gate

## 1. Purpose

This note tests a source-first mechanism which had not been isolated in the
Phase-106 ledger: retain one independent variable for every ordinary
prime-power observation and apply real-stable/Lorentzian determinant
inequalities before the sources are collapsed.

The conclusion is exact.

1. The multiaffine determinant is real stable.
2. Its Rayleigh differences are literal squared resolvent overlaps.
3. These data are blind to the oriented phase alignment which enters the
   physical surplus.
4. Consequently total positivity of the omitted archimedean tail, real
   stability of the source determinant, and all inequalities depending only
   on its Rayleigh differences cannot prove the strict surplus.
5. A surviving source-first argument must retain the signed source column
   itself, not only the positive atom Gram matrix.

No zero-location hypothesis is used.

## 2. Finite source determinant

Let (H) be a finite-dimensional complex Hilbert space, let (B>0), and
let (v_1,ldots,v_m\in H).  For source variables
(x=(x_1,ldots,x_m)), put

\[
 B(x)=B+\sum_{e=1}^m x_e v_ev_e^*,
 \qquad
 Z(x)=\det B(x).
 \tag{1}
\]

In the physical application the (v_e) are the post-radical observation
columns associated with the literal shifts
(u_e=\log p^k), together with the finite Gamma quadrature columns.  The
weights may be absorbed into the vectors.  The polar source is not inserted
into (1), because it is the signed bordered column whose domination is being
tested.

### Theorem 1 — Stability and exact Rayleigh square

The polynomial (Z) is multiaffine and real stable.  For (e\ne f), its
Rayleigh difference

\[
 \Delta_{ef}Z
 :=(\partial_eZ)(\partial_fZ)-Z\,\partial_e\partial_fZ
 \tag{2}
\]

satisfies, wherever (B(x)>0),

\[
 \boxed{
 \Delta_{ef}Z(x)
 =Z(x)^2
 \left|v_e^*B(x)^{-1}v_f\right|^2.}
 \tag{3}
\]

In particular, (Delta_{ef}Z(x)\ge0).

#### Proof

For (operatorname {Im}x_e>0), suppose that (B(x)h=0).  Taking the
imaginary part of (langle h,B(x)h\rangle=0) gives

\[
 \sum_e(\operatorname {Im}x_e)|\langle v_e,h\rangle|^2=0.
\]

Thus every (langle v_e,h\rangle) vanishes, and then (Bh=0), contrary
to (B>0).  Hence (Z(x)\ne0) when all source variables lie in the open
upper half-plane, which is real stability.  Multiaffinity follows from the
rank-one matrix determinant lemma.

Jacobi's formula gives

\[
 \partial_e\log Z=v_e^*B(x)^{-1}v_e
\]

and, for (e\ne f),

\[
 \partial_e\partial_f\log Z
 =-\left|v_e^*B(x)^{-1}v_f\right|^2.
\]

Since

\[
 -\partial_e\partial_f\log Z
 ={(\partial_eZ)(\partial_fZ)-Z\partial_e\partial_fZ\over Z^2},
\]

equation (3) follows.  (square)

## 3. The oriented column is not determined by the stable determinant

Let (c=(c_1,ldots,c_m)\in\mathbb C^m) be the literal signed source
coefficients and define

\[
 z(c)=\sum_{e=1}^m c_ev_e,
 \qquad
 G(c)=z(c)^*B^{-1}z(c).
 \tag{4}
\]

The finite physical surplus is a bordered version of
(G(c)-\delta).  Unlike (1)--(3), it retains the common orientation of the
source coefficients and observation columns.

### Theorem 2 — Phase-blindness of every unbordered stable-determinant
certificate

The complete collection consisting of (Z), all of its principal-source
minors, and all Rayleigh differences (2) does not determine (G(c)) when
the coefficients (c_e) are kept fixed.

#### Proof

Replace the columns by

\[
 v_e^{(\theta)}=e^{i\theta_e}v_e.
 \tag{5}
\]

Every rank-one atom is unchanged:

\[
 v_e^{(\theta)}(v_e^{(\theta)})^*=v_ev_e^*.
\]

Therefore (B(x)), (Z), every principal-source minor, and every Rayleigh
difference remain unchanged.  On the other hand,

\[
 G^{(\theta)}(c)
 =\left\|B^{-1/2}\sum_e c_e e^{i\theta_e}v_e\right\|^2
 \tag{6}
\]

depends on the phases.

The failure already occurs in dimension one.  Take (B=1),
(v_1=v_2=1), and (c_1=c_2=1).  With
((\theta_1,\theta_2)=(0,0)), equation (6) gives (G=4); with
((\theta_1,\theta_2)=(0,\pi)), it gives (G=0).  The unbordered source
determinant is (Z(x)=1+x_1+x_2) in both cases, and all its Rayleigh data
are identical.  (square)

### Corollary 3 — Total-positive tails do not supply the missing sign

Any argument which uses the omitted archimedean tail only through a
positive Loewner increment, and the retained prime/Gamma source bank only
through (B(x)), its minors, or its Rayleigh differences, cannot establish
the oriented inequality (G(c)>\delta).

Indeed, all such inputs are unchanged by (5), while the desired left-hand
side can range from complete constructive to complete destructive
interference.

This does not diminish the value of total-positive tail estimates: they
certify truncation and preserve inertia once an oriented margin is known.
They cannot create that margin.

## 4. Exact bordered polynomial

The phase information is restored only after adjoining the signed column:

\[
 \mathcal Z_c(t,x)
 =\det
 \begin{pmatrix}
  B(x)&z(c)\\
  z(c)^*&t
 \end{pmatrix}.
 \tag{7}
\]

Schur complementation gives

\[
 \boxed{
 \mathcal Z_c(t,x)
 =Z(x)\{t-z(c)^*B(x)^{-1}z(c)\}.}
 \tag{8}
\]

Thus the desired finite inequality is a sign statement for the bordered
source polynomial at (t=\delta).  It is not a consequence of the real
stability of the unbordered polynomial.  Assigning the needed sign to (8)
without further source information is exactly the physical surplus.

## 5. The surviving mechanism class

The preceding calculation identifies the source datum which every future
attack must retain:

\[
 \boxed{
 \text{the oriented pair }(c_e,v_e)_{e\in E_Y}
 \text{ before }\sum_e v_ev_e^*\text{ is formed}.}
 \tag{9}
\]

A mechanism survives the present gate only if it meets all of the following
requirements.

1. **Literal-source specificity.**  It uses the placements
   (log p^k) and the coefficients (Lambda(p^k)), not an abstract
   positive atom family.
2. **Common orientation.**  It is not invariant under independent phase
   twists (5).
3. **Joint completion.**  Gamma and the pole enter the same identity before
   any modulus square or absolute-value estimate.
4. **Post-radical construction.**  The complete anti-short is performed
   before the oriented comparison.
5. **Countermodel rejection.**  The construction must fail for the planted
   off-line quartet and for the abstract Euler renewal countermodels.

The minimal mathematical target is therefore an oriented source transport
(mathcal T_Y) satisfying

\[
 \mathcal T_Y(c,v)^*\mathcal T_Y(c,v)
 \le z(c)^*B_Y^{-1}z(c)
 \tag{10}
\]

together with a literal arithmetic lower evaluation

\[
 \|\mathcal T_Y(c,v)\|^2>\delta_J
 \tag{11}
\]

for some finite ordinary-prime cutoff (Y).  Crucially,
(mathcal T_Y) must be nonlinear before source aggregation; otherwise the
metric-preserving rigidity theorem of 106.141 applies and (10)--(11) merely
restate the surplus.

## 6. Status

Proved in this note:

* real stability of the independent-source determinant;
* the exact Rayleigh-square identity (3);
* the phase-blindness theorem and its one-dimensional witness;
* the exact bordered identity (8);
* the exclusion of total-positive-tail or stable-polynomial closure by
  themselves.

Not proved:

\[
 G_J>\delta_J.
\]

The surviving research target is the nonlinear, source-oriented arithmetic
transport (10)--(11).  It is strictly narrower than an unspecified positive
factorization and is not supplied by determinant stability, total
positivity, Schur algebra, or a metric-preserving re-realization.
