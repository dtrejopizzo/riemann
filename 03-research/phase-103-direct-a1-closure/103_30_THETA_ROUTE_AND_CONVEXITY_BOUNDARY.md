# Theta route to the integrated margin: exact reduction and boundary

## Verdict

Riemann's positive theta kernel gives an exact integral representation of
the *completed function* \(\xi\), and hence an exact formula for the Li
generating function.  It does not give a positive integral representation of
the logarithmic derivative needed for

\[
D_n=2\lambda_n-\lambda_n^{\rm arch}.
\]

Real-axis convexity, positivity of the theta kernel, and total-variation
control are insufficient: there are positive, even, smooth, rapidly
decreasing kernels whose bilateral Laplace transforms have off-axis zeros.
Accordingly, a theta proof would need an additional, genuinely zero-location
property of the *specific* theta kernel.  The standard positivity/convexity
properties alone do not reach the target.

## 1. Exact theta representation and the Li generator

Put \(\Xi(w)=\xi(1/2+w)\).  Riemann's theta transformation gives the exact
integral

\[
 \Xi(w)=\int_0^\infty \Phi(u)\cosh(wu)\,du, \tag{1}
\]

initially on the imaginary axis and then for every complex \(w\) by entire
continuation, where

\[
 \Phi(u)=\sum_{m\ge1}
 \left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)
 e^{-\pi m^2e^{2u}}. \tag{2}
\]

For \(u\ge0\), every summand is positive because its first parenthesis is
\(\pi m^2e^{5u/2}(2\pi m^2e^{2u}-3)\) and \(2\pi-3>0\).  The series and
all of its polynomially weighted derivatives converge absolutely on compact
sets; its double-exponential tail permits differentiation of (1).

The disk coordinate for the Li coefficients is

\[
 s=\frac1{1-z},\qquad w=s-\frac12=\frac{1+z}{2(1-z)}.
\]

Therefore, without an assumption on zeros,

\[
 \mathcal L(z):=\sum_{n\ge1}\lambda_nz^n
 =z\frac d{dz}\log\!\left[
 \int_0^\infty\Phi(u)
 \cosh\!\left(\frac{1+z}{2(1-z)}u\right)du\right]. \tag{3}
\]

If \(\mathcal A(z)=\sum_{n\ge1}\lambda_n^{\rm arch}z^n\) denotes the
already paired explicit Gamma--pole generator, the desired generating
function is exactly

\[
 \mathcal D(z):=\sum_{n\ge1}D_nz^n
 =2z\frac d{dz}\log\!\left[
 \int_0^\infty\Phi(u)
 \cosh\!\left(\frac{1+z}{2(1-z)}u\right)du\right]-\mathcal A(z). \tag{4}
\]

Equations (3)--(4) are the candid theta formulation of the problem.  The
logarithm is indispensable: replacing it by a linear theta integral changes
the Li coefficients.

## 2. What positivity of theta does prove

Extend \(\Phi(|u|)/2\) to an even positive measure on \(\mathbb R\).  For
real \(x\), (1) is its bilateral Laplace transform.  Cauchy--Schwarz gives

\[
 \Xi(x)\Xi''(x)-\Xi'(x)^2\ge0, \tag{5}
\]

so \(\log\Xi(x)\) is convex on the real axis.  More generally its
derivatives there are moments/cumulants of a positive tilted measure.  The
fast tail in (2) also gives finite total variation and all exponential
moments on every compact real strip.

These facts concern real \(x\).  Formula (4), however, asks for Taylor data
of a logarithm at a disk map whose natural boundary probes complex values of
\(w\).  Real convexity cannot control poles of \(\Xi'/\Xi\) away from the
real axis.

## 3. Smooth positive-kernel counterexample to the proposed mechanism

Choose \(0<a<1\).  The positive even atomic measure

\[
 \mu_a=\delta_0+\frac a2(\delta_{-1}+\delta_1)
\]

has bilateral Laplace transform

\[
 F_a(w)=1+a\cosh w. \tag{6}
\]

It is positive for real \(w\), and it obeys the same real-axis log-convexity
calculation as (5):

\[
 F_aF_a''-(F_a')^2=a\cosh w+a^2>0\qquad(w\in\mathbb R). \tag{7}
\]

Nevertheless it has the off-imaginary zeros

\[
 w=\pm\operatorname{arcosh}(1/a)+(2k+1)\pi i. \tag{8}
\]

This is not an artefact of atoms or lack of decay.  If
\(g_\sigma(u)=(2\pi\sigma^2)^{-1/2}e^{-u^2/(2\sigma^2)}\) and

\[
 \phi_{a,\sigma}(u)=g_\sigma(u)+\frac a2
 [g_\sigma(u-1)+g_\sigma(u+1)],
\]

then \(\phi_{a,\sigma}\) is strictly positive, even, smooth, and Schwartz,
while its Laplace transform is

\[
 e^{\sigma^2w^2/2}(1+a\cosh w). \tag{9}
\]

It has exactly the same off-axis zeros as (6), while retaining positivity,
all moments, finite variation, and real-axis log convexity.  Thus none of
these properties can prove a zero-free half-plane or the Fejer inequalities.

## 4. Consequence for \(D_n\)

The zeros in (8), after the shift \(s=1/2+w\), occur off the critical line
and in functional-equation-symmetric pairs.  The quartet calculation of
`103_28` then gives negative Li/Fejer contributions on an infinite
subsequence.  Hence a proof that uses only the generic positive-kernel
properties listed in Section 2 would apply equally to (9), which is
impossible.

The exact remaining theta task is more restrictive: exploit a special
identity of the explicit kernel (2), beyond positivity, evenness, smoothness,
decay, moment bounds, or real convexity, to establish the signed Taylor/Fejer
averages of (4).  No such identity is proved here.  Since eventual
nonnegativity of \(D_n\), plus finite certificates, implies Li positivity,
any successful additional identity must carry RH-strength information.
