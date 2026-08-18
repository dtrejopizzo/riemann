# 107.155 -- Exact stabilization criterion for pro-finite stalk cohomology

## 1. Setting

Let \(B_1\subseteq B_2\subseteq\cdots\) be increasing finite subsets of
a monomial basis \(B\).  A divisor rule selects nested subsets

\[
 S_D(r)\subseteq B_r,
 \qquad S_D(r)\subseteq S_D(r+1).
\]

Define the finite-level section module

\[
 H^0_r(D;n)=
 \left\{
 \sum_{b\in S_D(r)}x_b b:
 \sum_b|x_b|\le n
 \right\},
 \qquad n\ge1.
\]

This is the form forced by the coefficient-mass realization of
107_154.

## 2. Stabilization theorem

> **Theorem.** The integer dimensions
> \(\dim_{\mathbb S[\pm1]}H^0_r(D;n)\) stabilize with \(r\), for every
> fixed \(n\ge1\), if and only if
> \[
>  S_D(\infty):=\bigcup_rS_D(r)
> \]
> is finite.

**Proof.**

If \(S_D(\infty)\) is finite, nestedness implies that there is \(r_0\)
with \(S_D(r)=S_D(\infty)\) for all \(r\ge r_0\).  The bounded modules,
and hence their dimensions, are then identical.

Conversely, put \(s_r=|S_D(r)|\).  Since \(n\ge1\), the radius-\(n\)
ball contains every basis vector indexed by \(S_D(r)\).  Any linear
generating family must span the free abelian group on those vectors, so

\[
 \dim_{\mathbb S[\pm1]}H^0_r(D;n)\ge s_r.
\]

If \(S_D(\infty)\) is infinite, nestedness forces \(s_r\) to be
unbounded; the dimensions cannot stabilize. \(\square\)

## 3. Frobenius covariance

Finite support is compatible with Frobenius only as a rule on divisors,
not as invariance of one divisor:

\[
 S_{\varphi_pD}=p\,S_D,
 \qquad
 S_{\varphi_p^{-1}D}=p^{-1}S_D.
\]

Each set remains finite, while its orbit through different divisors may
be infinite.  This is exactly the between-level behavior of 107_154 and
does not contradict the no-go of 107_153.

On the square, the same criterion applies to finite subsets of
\(M_p\times M_p\), with the two covariance laws

\[
 S_{\varphi_{\rm v}D}=(p,1)S_D,
 \qquad
 S_{\varphi_{\rm h}D}=(1,p)S_D.
\]

## 4. Consequence

The full finite-level stalk cannot be used as \(H^0(D)\): its admitted
monomial set grows without bound.  A viable divisor sheaf must prove,
from geometry and before computing dimension, that each finite-support
divisor admits only finitely many monomial rays.  Once this is proved,
the pro-system introduces no further \(H^0\)-stabilization ambiguity.

This criterion does not provide the support rule.  It converts
"cohomology should stabilize" into the exact geometric statement that
the future square construction must establish.

