# 107.153 -- Frobenius-stable finite-dimension no-go for the additive stalk

## 1. Theorem

Fix a prime \(p\), put \(M_p=\mathbb Z[1/p]_+\), and let

\[
 R_p=\mathbb Z[T^{M_p}].
\]

The local Frobenius

\[
 \varphi_p(T^a)=T^{pa}
\]

is an automorphism of \(R_p\).  Let \(V\subseteq R_p\) be an additive
subgroup stable under both \(\varphi_p\) and \(\varphi_p^{-1}\).

> **Theorem.** If \(V\) contains a nonconstant element, then \(V\) has
> infinite rank as an abelian group.

Consequently no nonconstant Frobenius-stable bounded
\(\mathbb S[\pm1]\)-submodule of the canonical additive linearization can
have finite Connes--Consani integer dimension.

## 2. Proof

The positive exponents in \(M_p\) decompose into orbits under
multiplication by \(p\).  On each orbit choose a representative \(a\);
the corresponding free abelian summand has basis

\[
 \{T^{ap^k}:k\in\mathbb Z\}
\]

and is canonically the Laurent polynomial module
\(\mathbb Z[u,u^{-1}]\), with \(\varphi_p\) acting by multiplication by
\(u\).

Take a nonconstant \(f\in V\).  If necessary replace it by
\(\varphi_p(f)-f\); this is nonzero because a finite-support polynomial
fixed by exponent scaling has only its constant term.  Project \(f\) to
one exponent orbit on which it is nonzero.  The projection is a nonzero
Laurent polynomial \(P(u)\).

Suppose that finitely many Frobenius translates satisfy

\[
 \sum_{k=m}^n c_k\varphi_p^k(f)=0.
\]

After projection to the chosen orbit this becomes

\[
 \left(\sum_{k=m}^n c_k u^k\right)P(u)=0
\]

in the integral domain \(\mathbb Z[u,u^{-1}]\).  Since \(P\ne0\), every
\(c_k\) is zero.  Thus all translates
\(\{\varphi_p^k(f):k\in\mathbb Z\}\subset V\) are linearly independent,
and \(V\) has infinite rank. \(\square\)

## 3. Dimension consequence

If a bounded sphere submodule \(E\subset HR_p\) had a finite linear
generating family, its integral span would have finite rank.  If \(E\)
is stable under the invertible local Frobenius and contains a
nonconstant section, its span satisfies the theorem and has infinite
rank, a contradiction.

Therefore the three desired properties

\[
 \text{nonconstant local sections},\qquad
 \varphi_p^{\pm1}\text{-stability},\qquad
 \dim_{\mathbb S[\pm1]}<\infty
\]

cannot coexist in the ordinary additive monoid-ring lift.

## 4. Consequence for Phase 107

A denominator-depth cutoff makes the monomial set finite, but
\(\varphi_p^{-1}\) immediately leaves that cutoff.  A real-size cutoff
does not help: the set
\(\{a/p^k:k\ge0\}\) remains infinite in every interval containing a
positive exponent.

Hence the Cech realization required after 107_151 cannot be obtained by
choosing a finite truncation of \(\mathbb Z[T^{M_p}]\) while retaining
the local Frobenius automorphism.  A viable construction must change at
least one structural ingredient: use a non-free/derived additive
realization, replace finite integer dimension by a justified different
dimension, or encode Frobenius as a correspondence between truncation
levels rather than an automorphism at each level.

This theorem does not rule out the original spherical stalk.  It rules
out its ordinary additive linearization and every Frobenius-stable
finite-dimensional submodule inside that linearization.

