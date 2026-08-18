# 107.199 -- Balanced bidirectional Dirac loop realizes the local determinant

## 1. Two-state loop

For \(|q|<1\), consider

\[
 D(a,b)=\begin{pmatrix}0&a\\b&0\end{pmatrix}.
\]

Its closed-loop weight is \(ab\), and

\[
 \det(1-D(a,b))=1-ab.
 \tag{1.1}
\]

Thus the local orbit determinant \(1-q\) requires \(ab=q\).

## 2. Transpose balance

The determinant condition alone leaves

\[
 a=q^\theta,\qquad b=q^{1-\theta}.
\]

Imposing compatibility with transpose, \(D^t=D\), gives \(a=b\).
On the source half-plane the canonical holomorphic branch is therefore

\[
 a=b=q^{1/2}=p^{-s/2}.
 \tag{2.1}
\]

The balanced operator

\[
 D_{p,s}=\begin{pmatrix}
 0&p^{-s/2}\\p^{-s/2}&0
 \end{pmatrix}
 \tag{2.2}
\]

satisfies

\[
 \det(1-D_{p,s})=1-p^{-s}.
 \tag{2.3}
\]

The square-root normalization is derived from transpose symmetry, not
chosen after evaluating the determinant.

## 3. Green connection

The inverse of (2.3) is the local Euler factor, and

\[
 d\log\det(1-D_{p,s})
 =\log p\,{p^{-s}\over1-p^{-s}}\,ds.
 \tag{3.1}
\]

The eigenvalues of \(D_{p,s}\) are \(\pm p^{-s/2}\).  Hence the same
half-weight that balances the function-field Frobenius form appears as
the unique transpose-symmetric factorization of the prime return weight.

## 4. Result and scope

Equations (2.2)--(3.1) give a finite-dimensional, bidirectional,
source-defined local determinant model.  It survives the one-way no-go
of 107_198 and realizes the relative determinant of 107_196 without an
infinite eta tail.

It also identifies a candidate odd endomorphism for a superconnection:
the two directions are the correspondence and transpose, each carrying
half of the return weight.

This is not yet a Bott--Chern or Bismut--Goette current.  No ambient
complex normal bundle, metric anomaly, heat-kernel transgression,
primewise gluing, top class, or Hodge pairing is constructed.

Determinant equality alone does not select (2.1): asymmetric
\(\theta\ne1/2\) factorizations collide.  Transpose symmetry is
load-bearing and must survive any global realization.

## 5. Falsifier

The verifier uses primes \(2,3,5,7,11\), real and complex spectral
parameters, and checks determinant, eigenvalues, transpose, and Green
derivative.  It rejects asymmetric factorizations
\(\theta=1/3,1/4,2/3\) despite their matching determinants, so it can
return NO for either a wrong factor or a false balance claim.
