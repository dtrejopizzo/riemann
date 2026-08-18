# 107.168 -- Fourier realization of the support lift and its mass obstruction

## 1. The published Fourier algebra

In the proof of Proposition 5.7 of the 2018 Riemann--Roch strategy,
Connes--Consani use the algebra

\[
 \mathcal B=\mathbb C[\mathbb Q]
 =\bigoplus_{q\in\mathbb Q}\mathbb C e_q,
 \qquad e_qe_{q'}=e_{q+q'},
\]

of finite Fourier sums on
\(G=\mathbb A_{\mathbb Q}/\mathbb Q\).  Since \(\widehat G=\mathbb Q\),
the characters \(e_q\) are linearly independent.

For every prime \(p\), the support enrichment of 107_165 has the
canonical injective realization

\[
 \iota_p:\mathbb Z[H_p]\hookrightarrow\mathcal B,
 \qquad T^q\longmapsto e_q,
 \qquad H_p=\mathbb Z[1/p].
 \tag{1.1}
\]

On the square,

\[
 \iota_p^\square:
 \mathbb Z[H_p\times H_p]hookrightarrow
 \mathbb C[\mathbb Q\times\mathbb Q].
 \tag{1.2}
\]

Thus the enriched support is not external to the complex lift: it is an
integral Fourier subalgebra of the functions used in its de Rham proof.

## 2. Exact compatibility

Multiplication by \(p\) on \(G\) sends characters by

\[
 e_q(px)=e_{pq}(x).
\]

Hence (1.1) intertwines local Frobenius
\(T^q\mapsto T^{pq}\) with the published mapping-torus action.  Likewise,
for coprime \((n,m)\),

\[
 e_a\otimes e_b\longmapsto e_{na+mb}
\]

is exactly the Fourier realization of \(\Lambda_{n,m}\) from 107_163.
Its kernel therefore supplies the same diagonal/Frobenius incidence
relations inside the Fourier algebra.

This proves compatibility of the coefficient support, Frobenius action,
and rational correspondences with the periodic complex lift.

## 3. The differential obstruction

The leafwise vector fields act on a Fourier coefficient \(f(y,q)e_q\)
by

\[
 X(f)(y,q)=2\pi i,yq f(y,q),
 \qquad
 Y(f)(y,q)=y\partial_y f(y,q).
 \tag{3.1}
\]

The operator \(X\) is diagonal on support, but it is not a morphism of
the bounded \(\ell^1\) modules used for the integer dimension.  On a
finite Fourier support \(S\), its coefficient-mass norm is

\[
 \|X\|_{S,y}=2\pi y\max_{q\in S}|q|.
\]

For the pro-Frobenius levels of 107_154,

\[
 \max_{q\in M_p(A,R)}|q|=A p^R
\]

up to the removal of numerators divisible by \(p\).  This tends to
infinity with either \(A\) or \(R\).  Therefore no uniform mass bound
survives the filtered colimit.  The operator \(Y\) also leaves the
integral coefficient category because it differentiates the continuous
\(y\)-dependence.

It follows that the diagram

\[
 \text{bounded }\mathbb S[\pm1]\text{-modules}
 \xrightarrow{\ d\ }
 \text{bounded }\mathbb S[\pm1]\text{-modules}
\]

does not arise by simply restricting the published leafwise de Rham
differential.  The integer dimension of 2022 cannot yet be applied to
that complex.

## 4. Exact remaining choices

A compatible geometric three-term complex now requires one of the
following, proved rather than selected for convenience:

1. a graph norm/filtration in which \(X,Y\) are bounded and whose
   dimension has the required RR asymptotic;
2. a cellular or difference model quasi-isomorphic to the leafwise
   complex, with integral mass-controlled differentials;
3. a determinant/Fredholm formulation replacing finite generator
   dimension while retaining the terminal intersection identity.

The cellular torus calculation of 107_167 proves the correct amplitude
for constant coefficients, but it does not yet supply option 2 for the
divisor modules.

## 5. Scope

This is a mixed positive/negative result.  It proves the first actual
coefficient-level bridge between the Phase 107 support lift and the CC
complex geometry.  It also proves that the naive transport of the CC
\(\ell^1\) mass through the de Rham differential fails.  It does not
rule out a weighted or cellular realization.

## 6. Falsifier

The verifier checks Frobenius and \(\Lambda_{n,m}\) identities on actual
prime-local rational supports.  It then computes the normalized
amplification \(\max|q|\) through increasing \((A,R)\) and requires it
to be unbounded.  A bounded outcome would return `VERDICT: NO` and
reopen the direct mass-preserving route.
