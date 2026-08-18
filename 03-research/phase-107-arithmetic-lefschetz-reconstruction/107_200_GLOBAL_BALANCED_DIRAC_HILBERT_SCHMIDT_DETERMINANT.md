# 107.200 -- Global balanced prime Dirac operator has determinant zeta inverse

## 1. Global operator

For \(s\in\mathbb C\) with \(\sigma=\Re(s)>1\), define

\[
 \mathcal H_{\mathbb P}=\bigoplus_{p\ {m prime}}\mathbb C^2,
 \qquad
 D_s=\bigoplus_p
 \begin{pmatrix}
 0&p^{-s/2}\\p^{-s/2}&0
 \end{pmatrix}.
 \tag{1.1}
\]

Each block is the transpose-balanced local loop of 107_199.

## 2. Correct Schatten class

The singular values of the \(p\)-block are both \(p^{-\sigma/2}\).
Therefore

\[
 \|D_s\|_2^2=2\sum_p p^{-\sigma}<\infty
 \qquad(\sigma>1).
 \tag{2.1}
\]

Thus \(D_s\) is Hilbert--Schmidt throughout the Euler half-plane.  Its
trace norm is

\[
 \|D_s\|_1=2\sum_p p^{-\sigma/2},
\]

which is finite only for \(\sigma>2\).  Hence ordinary Fredholm
determinants do not cover the full required domain; the order-two
Carleman--Fredholm determinant is the canonical one.

## 3. Determinant theorem

For a Hilbert--Schmidt operator,

\[
 \det{}_2(1-D)=\prod_\lambda(1-\lambda)e^\lambda.
\]

The eigenvalues in a prime block are
\(\lambda_{p,\pm}=\pm p^{-s/2}\), so the exponential corrections
cancel pairwise:

\[
 (1-p^{-s/2})e^{p^{-s/2}}
 (1+p^{-s/2})e^{-p^{-s/2}}
 =1-p^{-s}.
 \tag{3.1}
\]

Absolute convergence follows from (2.1), and therefore

\[
 \boxed{
 \det{}_2(1-D_s)=\prod_p(1-p^{-s})={1\over\zeta(s)}
 }
 \qquad(\Re s>1).
 \tag{3.2}
\]

No zeros are used in defining either side.

## 4. Green trace

Differentiating the convergent determinant gives

\[
 d\log\det{}_2(1-D_s)
 =\sum_p\log p\,{p^{-s}\over1-p^{-s}}\,ds
 =-\frac{\zeta'(s)}{\zeta(s)}\,ds.
 \tag{4.1}
\]

Thus one global Hilbert--Schmidt operator simultaneously carries:

1. the balanced half-weight \(p^{-s/2}\);
2. every prime orbit determinant;
3. the finite Green channel;
4. the Euler failure demanded by Davenport--Heilbronn.

## 5. Exact scope

This is a genuine global spectral realization of the finite row-(c)
determinant in the Euler half-plane.  It improves the directed product
of 107_188 by placing all local blocks in one Schatten-class operator.

It does not yet provide:

1. analytic continuation of the operator family across \(\Re s=1\);
2. the Gamma and pole blocks inside the same \(\det_2\);
3. a sheaf or cycle on the Connes--Consani square;
4. a secondary current or arithmetic intersection;
5. a Hodge-index theorem.

The next operator problem is to incorporate the archimedean number
operator and degree-zero/two factors into one graded regularized
determinant family without prescribing \(\xi\).

## 6. Falsifier

The verifier fixes primes through \(10^5\), real and complex spectral
points, and compares finite block products independently with
\(1/\zeta(s)\) and (4.1).  It checks paired block cancellation,
Hilbert--Schmidt convergence, and trace-norm growth in the strip
\(1<\sigma\le2\).  Breaking one transpose pair must destroy the
order-two cancellation.
