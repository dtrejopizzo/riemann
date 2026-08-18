# Independent audit: the integrated strong margin

## Question and verdict

The surviving scalar assertion is

\[
 D_n:=2\lambda_n-\lambda_n^{\rm arch}\ge0. \tag{1}
\]

It has an exact Dirichlet/Fejer representation, but that representation does
not supply an unconditional positive measure.  In particular, neither the
Euler factors nor the pointwise completed Euler--Gamma symbol has the needed
sign.  A proof of (1) for all sufficiently large \(n\), together with the
finite Li coefficients and the already required positivity of the
archimedean term, would prove RH.  Thus the statement is genuinely
RH-strength, not a positivity theorem that follows formally from the Euler
product.

This note establishes exact identities and falsifies the local-sign routes.
It does not claim RH.

## 1. Exact Fejer identity

Let

\[
 g_0^{\rm SM}=2\lambda_1-\lambda_1^{\rm arch},\qquad
 g_m^{\rm SM}=(\lambda_{m+1}-2\lambda_m+\lambda_{m-1})
 -\frac12(\lambda_{m+1}^{\rm arch}-2\lambda_m^{\rm arch}
 +\lambda_{m-1}^{\rm arch})\quad(m\ge1).
\]

Twice summation by parts gives, with no sign assumption,

\[
\begin{aligned}
 n g_0^{\rm SM}+2\sum_{m=1}^{n-1}(n-m)g_m^{\rm SM}
 &=2\lambda_n-\lambda_n^{\rm arch}\\
 &=D_n. \tag{2}
\end{aligned}
\]

For a radial regulator \(0<r<1\), write

\[
 C_{{\rm SM},r}(e^{i\theta})
 =g_0^{\rm SM}+2\sum_{m\ge1}r^m g_m^{\rm SM}\cos(m\theta),
\]

and let

\[
 F_n(\theta)=\left|\sum_{j=0}^{n-1}e^{ij\theta}\right|^2
 =n+2\sum_{m=1}^{n-1}(n-m)\cos(m\theta).
\]

Coefficient orthogonality gives the exact regulated identity

\[
 \frac1{2\pi}\int_{-\pi}^{\pi}F_n(\theta)
 C_{{\rm SM},r}(e^{i\theta})\,d\theta
 =n g_0^{\rm SM}+2\sum_{m=1}^{n-1}(n-m)r^m g_m^{\rm SM}. \tag{3}
\]

Taking the coefficientwise Abel limit \(r\uparrow1\) recovers (2).  This
is the precise sense in which (1) is an *integrated* Fejer sign: it is not a
pointwise sign of the symbol.

## 2. Completed Euler--Gamma form and why pointwise positivity fails

For \(s=(1-z)^{-1}\), the exact completed expression is

\[
 C_{\rm SM}(z)
=\frac12 C_{\rm arch}(z)+2\left(\frac1{s-1}+\frac{\zeta'}\zeta(s)\right),
\qquad
 C_{\rm arch}(z)=\frac2s-\log\pi+\psi(s/2). \tag{4}
\]

The full Carathéodory assertion \(\Re C_{\rm SM}\ge0\) is not merely
unproved: it is false even assuming RH.  On the disk boundary corresponding
to \(s=1/2+it\), away from zero ordinates, RH gives
\(\Re C_1=0\), whereas the explicit digamma remainder estimate of `103_25`
gives \(\Re C_{\rm arch}>0\) for \(|t|\ge30\).  Therefore

\[
 \Re C_{\rm SM}=-\frac12\Re C_{\rm arch}<0
\]

at such boundary points and, by radial continuity away from the zero images,
at nearby interior points.  Since \(F_n\ge0\), this does **not** disprove
(1): a particular positive kernel can have positive integrals against every
member of one restricted family despite changing sign.  It does disprove the
only direct Herglotz/Loewner proof of (1).

## 3. Euler factors have no local positive sign

This can be checked in the candid Euler-product half-plane, without a
boundary rearrangement.  Fix \(a>1\), put \(s=a/(1-z)\), and use

\[
 \frac{\zeta'}\zeta(s)=-\sum_{m\ge2}\Lambda(m)m^{-s}.
\]

The contribution of one prime power \(m\) to
\(z\,d(\log\zeta(s))/dz\) is

\[
 -a\Lambda(m)m^{-a}\,
 \frac{z}{(1-z)^2}
 \exp\!\left(-\frac{a(\log m)z}{1-z}\right).
\]

The Laguerre generating function

\[
 \frac1{(1-z)^2}\exp\!\left(-\frac{xz}{1-z}\right)
 =\sum_{k\ge0}L_k^{(1)}(x)z^k
\]

therefore gives the exact, absolutely convergent coefficient contribution

\[
 \lambda_{n,m}^{\rm prime}(a)
 =-a\Lambda(m)m^{-a}L_{n-1}^{(1)}(a\log m). \tag{5}
\]

Already for \(n=1\), every nonzero local term in (5) is negative.  For
\(n=2\), its sign is that of \(-[2-a\log m]\), so it changes as \(m\)
varies.  Higher \(n\) have further Laguerre oscillations.  Hence no proof of
(1) can be obtained by assigning nonnegative contributions to the Euler
factors coefficientwise.

At \(a=1\), the individual coefficient series in (5) is not absolutely
summable, so a formal term-by-term “prime positivity” argument at the Li
base point is additionally invalid.  One must first retain \(a>1\) (or an
equivalent Abel regulator) and only then take a justified paired limit.

## 4. RH-strength and the exact remaining content

For \(n\ge8\), the program's archimedean term is positive.  Thus (1) gives

\[
 \lambda_n\ge\frac12\lambda_n^{\rm arch}>0\qquad(n\ge8). \tag{6}
\]

The finite coefficients \(1\le n\le7\) can in principle be settled by
independent interval arithmetic.  Consequently an all-\(n\) proof of (1),
or an eventual proof combined with finite certificates, proves Li
positivity and hence RH.  This is a logical reduction, not circularity; it
does mean that no derivation from elementary Euler-factor signs, Fejer
positivity alone, or the gamma factor can be accepted unless it contains the
missing RH-strength input.

The feasible narrow target is exactly the family of signed integrals (3):
obtain a lower bound for their *specific* Fejer averages after the completed
prime--pole--gamma cancellation.  The current identities neither prove nor
falsify those averages.  They do prove that a pointwise symbol inequality
and every coefficientwise Euler-factor inequality are unavailable.
