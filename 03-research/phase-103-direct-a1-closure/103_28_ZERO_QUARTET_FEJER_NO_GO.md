# Functional-equation quartets do not force the Fejer sign

## Result

The functional symmetry

\[
 \rho,\quad 1-\rho,\quad\bar\rho,\quad1-\bar\rho
\]

does not force a nonnegative Li contribution, nor a nonnegative integrated
Fejer contribution.  A critical-line quartet has nonnegative contribution
term by term.  An off-line quartet has negative contribution for infinitely
many indices.  Thus functional symmetry by itself cannot prove

\[
2\lambda_n-\lambda_n^{\rm arch}\ge0.
\]

The last expression includes a global archimedean term and therefore cannot
be allocated canonically to a single zero quartet.  What the calculation
does prove is that the zero-side/Fejer part supplies no local positive
mechanism capable of overcoming that issue.

## 1. Exact quartet contribution

For one zero \(\rho\), put

\[
 b=1-\frac1\rho=\frac{\rho-1}{\rho}=re^{i\theta}.
\]

The reflection satisfies

\[
 1-\frac1{1-\rho}=b^{-1},
\]

and conjugation replaces \(b\) by \(\bar b\).  Therefore the contribution
of the quartet, counted with these four multiplicities, to the Li coefficient
is exactly

\[
\begin{aligned}
 L_n(\rho)
 &=\sum_{\eta\in\{\rho,1-\rho,\bar\rho,1-\bar\rho\}}
       \left[1-\left(1-\frac1\eta\right)^n\right]\\
 &=4-2\mathrm{Re}(b^n+b^{-n})\\
 &=\boxed{\,4-2(r^n+r^{-n})\cos(n\theta)\,}. \tag{1}
\end{aligned}
\]

This is an algebraic identity; it uses neither RH nor a limiting convention.
Moreover

\[
 r^2=\frac{(1-\Re\rho)^2+(\Im\rho)^2}
 {(\Re\rho)^2+(\Im\rho)^2}.
\]

Thus \(r=1\) exactly when \(\Re\rho=1/2\).

If \(\Re\rho=1/2\), (1) becomes

\[
 L_n(\rho)=4-4\cos(n\theta)=8\sin^2(n\theta/2)\ge0. \tag{2}
\]

This is the familiar elementary zero-by-zero positivity under RH.

## 2. Off-line quartets are negative infinitely often

Suppose \(r\ne1\).  There are infinitely many positive integers \(n\) for
which \(\cos(n\theta)\ge1/2\).  For a rational angle this follows from
periodicity (a positive multiple has cosine 1).  For an irrational angle,
the elementary pigeonhole approximation to rotations gives arbitrarily large
returns of \(n\theta\) modulo \(2\pi\) to \((-\pi/3,\pi/3)\).  Hence, along
an infinite subsequence,

\[
 L_n(\rho)\le4-(r^n+r^{-n}). \tag{3}
\]

Since \(r^n+r^{-n}\to\infty\), this is strictly negative for all
sufficiently large members of that subsequence.  No claim follows about the
sum over *all* zeta zeros: other quartets could in principle compensate.
The lemma only rules out an independent nonnegative contribution from each
functional-equation orbit.

## 3. Exact nonreal algebraic counterexample

Take

\[
 \rho=\frac{1+2i}{5}=\frac15+\frac25i.
\]

Then

\[
 \frac1\rho=1-2i,\qquad b=1-\frac1\rho=2i.
\]

This is a nonreal point strictly inside the critical strip and its quartet is
distinct.  Equation (1) gives, for every \(k\ge1\),

\[
 L_{4k}(\rho)=4-2\left(2^{4k}+2^{-4k}\right)<0. \tag{4}
\]

If a literal functional-equation-symmetric, real entire toy divisor is
desired, use

\[
 P(s)=(s-\rho)(s-(1-\rho))(s-\bar\rho)(s-(1-\bar\rho)).
\]

It has real coefficients and \(P(1-s)=P(s)\).  Its four-zero Li sum is
precisely (1), hence (4).  Functional equation and conjugation alone
therefore permit negative Li/Fejer energies.

## 4. Consequence for the integrated Fejer target

For any sequence \(a_n\), with the standard second-difference Toeplitz
coefficients \(g_0=2a_1\) and
\(g_m=a_{m+1}-2a_m+a_{m-1}\), the Dirichlet-vector energy is exactly

\[
 n g_0+2\sum_{m=1}^{n-1}(n-m)g_m=2a_n. \tag{5}
\]

Apply this to \(a_n=L_n(\rho)\).  The Fejer energy of the quartet is
\(2L_n(\rho)\), so (4) produces negative Fejer energy at every \(n=4k\).
Subtracting an externally chosen archimedean sequence does not create a
local zero-orbit positivity theorem; it merely changes the global target.

Accordingly, the remaining strong-margin inequality can only arise from a
global completed cancellation involving the actual zero divisor, Euler
product, and Gamma factor.  It cannot follow from reflection symmetry, from
conjugation symmetry, or from a Fejer average of a single quartet.
