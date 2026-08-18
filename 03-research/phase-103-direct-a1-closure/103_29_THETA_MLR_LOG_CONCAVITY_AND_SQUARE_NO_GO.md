# Theta MLR, log-concavity, and the square-representation no-go

## Purpose

This note tests three proposed ways in which the *specific* theta kernel
might force the remaining strong margin
\[
 D_n=2\lambda_n-\lambda_n^{\rm arch}\ge0.                         \tag{1}
\]
The result is an exact limitation, not a claim about RH: the monotone
likelihood-ratio and order-two total-positivity structures of the theta
tilts are automatic for every positive base measure, and even log-concavity
does not turn functional symmetry into critical-line zeros.  A square
identity based only on these properties would therefore be circular at the
same point as the Fejer construction.

## 1. Exact theta tilt and its universal MLR property

Let
\[
 d\mu_a(u)={\Phi(|u|)e^{(a-1/2)u}\,du\over
 \int_{\mathbb R}\Phi(|v|)e^{(a-1/2)v}\,dv},\qquad a>1,           \tag{2}
\]
with the positive modular theta kernel \(\Phi\) from `103_15`.  For
\(b>a>1\), the Radon--Nikodym ratio is exactly
\[
 {d\mu_b\over d\mu_a}(u)
 ={\xi(a)\over\xi(b)}e^{(b-a)u}.                                 \tag{3}
\]
It is strictly increasing in \(u\).  Thus the theta family has the
monotone-likelihood-ratio property, with no zero-location input.

The corresponding order-two total positivity is equally elementary.  If
\(a_1<a_2\) and \(u_1<u_2\), then
\[
\begin{aligned}
 &e^{a_1u_1}e^{a_2u_2}-e^{a_1u_2}e^{a_2u_1}\\
 &\quad=e^{a_1u_1+a_2u_2}
 \left[1-e^{(a_1-a_2)(u_2-u_1)}\right]>0.                         \tag{4}
\end{aligned}
\]
Multiplication by the positive factor \(\Phi(|u|)\) preserves this
statement.  Therefore neither MLR nor TP2 distinguishes the Riemann theta
kernel from an arbitrary positive even base measure.

## 2. Log-concavity does not repair the implication

There is an algebraic countermodel with all of the preceding order
properties.  For \(q>2\), take the even three-point measure
\[
 \nu_q={\delta_{-1}+q\delta_0+\delta_1\over q+2}.                \tag{5}
\]
Its lattice weights \((1,q,1)\) are log-concave:
\[
 q^2\ge1\cdot1.                                                   \tag{6}
\]
Its exponential tilts obey exactly (3), hence MLR and TP2.  Its completed
symmetry transform is, up to a positive factor,
\[
 X_q(s)=q+2\cosh(s-1/2).                                          \tag{7}
\]
Writing \(y=s-1/2\), its zeros satisfy
\[
 \cosh y=-{q\over2}<-1.
\tag{8}
\]
Thus
\[
 y=\pm\mathrm{arcosh}(q/2)+(2k+1)\pi i,qquad k\in\mathbb Z,
\tag{9}
\]
and all these zeros have nonzero real part.  This countermodel is more
restrictive than the positive-even measure witness in `103_15`: it also has
the exact exponential-family MLR/TP2 structure and discrete log-concavity.

Consequently, proving ordinary log-concavity of the actual \(\Phi\), even
if available, would not imply (1), Li positivity, or RH.  The same applies
to every argument which uses only (3)--(4) plus evenness/modular symmetry.

## 3. Why integration by parts does not create a universal square

The theta identity gives, for the regulated coefficients,
\[
 \lambda_n(a-1)
 =n[z^n]\log\mathbb E_{\mu_a}
 \exp\!\left({az\over1-z}U\right).                              \tag{10}
\]
The logarithm is essential.  It makes the coefficient a cumulant
combination rather than a positive linear functional of \(\Phi\):
\[
 \lambda_n(a-1)=n\sum_{j=1}^n{a^j\over j!}
 {n-1\choose j-1}\kappa_j(a).                                   \tag{11}
\]
In particular, integration by parts against a positive theta density cannot
turn (11), for all \(n\), into a square merely from positivity of the
density.  The actual theta kernel already has
\[
 \kappa_3(a)=(\log\xi)'''(a)<0\qquad(a>36),                       \tag{12}
\]
by the elementary Euler--Gamma estimate proved in `103_15`.  Hence every
proposed square proof which makes the individual cumulant contributions in
(11) nonnegative is false for the actual theta kernel.

More generally, a positive Parseval identity for all Dirichlet tests would
give the Toeplitz positivity of the increment sequence.  By `103_27`, its
spectral support would have to lie on \(|w_\rho|=1\), which is equivalent
to RH.  A theta integration-by-parts formula can be useful only if it
supplies a new, specifically modular estimate for the *single integrated
energy* (1); it cannot obtain coercivity from MLR, log-concavity, or a
formal square completion alone.

## Status

The following statements are proved here:

1. the exact theta exponential family has MLR and TP2, equations (3)--(4);
2. those properties, even supplemented by discrete log-concavity, admit the
   off-line-zero model (5)--(9);
3. termwise cumulant/square positivity is false for the actual theta kernel
   by (12).

No theta-specific total-positivity or modular coercivity theorem sufficient
for (1) is obtained.  Such a theorem would have to use information beyond
the order properties audited above and would remain RH-strength.
