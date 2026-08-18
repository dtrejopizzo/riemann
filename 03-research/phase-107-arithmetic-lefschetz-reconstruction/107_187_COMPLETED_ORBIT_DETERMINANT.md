# 107.187 -- Prime holonomy and archimedean spectral determinants assemble to xi

## 1. Finite determinant

On the prime orbit \(C_p\), the twisted cellular differential of
`107_185` is \(1-p^{-s}\).  Its inverse determinant is the local Euler
factor.  Therefore

\[
 \Delta_{\rm fin}(s)
 =\prod_p\det(1-p^{-s})^{-1}
 =\prod_p(1-p^{-s})^{-1}
 =\zeta(s)
 \tag{1.1}
\]

for \(\Re(s)>1\).

## 2. Archimedean determinant

For \(a\notin\{0,-1,-2,\ldots\}\), the spectral zeta function of the
number operator is the Hurwitz zeta function:

\[
 \zeta_N(z;a)=\operatorname{Tr}(N+a)^{-z}=\zeta_H(z,a).
\]

Its zeta-regularized determinant is

\[
 \det_\zeta(N+a)
 =\exp(-\zeta_H'(0,a))
 ={\sqrt{2\pi}\over\Gamma(a)}.
 \tag{2.1}
\]

At \(a=s/2\), the archimedean completed factor is consequently

\[
 \Delta_\infty(s)
 =\pi^{-s/2}\Gamma(s/2)
 ={\sqrt{2\pi}\,\pi^{-s/2}\over
   \det_\zeta(N+s/2)}.
 \tag{2.2}
\]

## 3. Completed determinant

Include the degree-zero and degree-two factors.  The assembled
determinant is

\[
 \begin{aligned}
 \Delta_{\rm comp}(s)
 &={1\over2}s(s-1)\Delta_\infty(s)\Delta_{\rm fin}(s)\\
 &={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\\
 &=\xi(s).
 \end{aligned}
 \tag{3.1}
\]

Taking its negative logarithmic derivative recovers exactly the Green
trace assembled in `107_185`--`107_186`:

\[
 -{d\over ds}\log\Delta_{\rm comp}(s)
 =-{\xi'(s)\over\xi(s)}.
 \tag{3.2}
\]

Thus the finite orbit complexes, archimedean number operator, and
degree-zero/two terms form one completed analytic determinant object.

## 4. Result and exact limitation

The determinant-level row-(b)/(c) assembly is constructed without
postulating intersection numbers.  Its local factors come from actual
orbit and spectral complexes, and its global determinant is the
completed zeta function.

This is not yet a determinant **line bundle on a proper arithmetic
surface**.  It is a meromorphic determinant function of \(s\).  To enter
row (d), Phase 107 still needs:

1. a sheaf/cohomology complex on the absolute arithmetic space whose
   determinant line has (3.1) as its canonical section;
2. a real structure and metric producing the Green distribution of
   `107_184`;
3. a primitive intersection pairing on that line/class.

The construction remains Euler-sensitive and is unavailable for
Davenport--Heilbronn.

## 5. Falsifier

The verifier independently differentiates the Hurwitz zeta at zero to
check (2.1), forms the prime determinant through the fixed cutoff
\(10^5\), and compares the resulting completed determinant with
\(\xi(s)\) at real and complex points.  It also compares the logarithmic
derivative of (3.1) with `107_183`.  Any normalization mismatch returns
`VERDICT: NO`.
