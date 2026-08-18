# D.112 — Poisson--Calderón contraction and the sharp-norm obstruction

## Status

The two Tate jets admit an explicit orthogonal Calderón projection on every
finite logarithmic window.  Composing it with the prime--Gamma differential
of D.111 gives a canonical Poisson left inverse.  It is Real covariant,
Fourier compatible and retains every prime power and the complete Gamma
oscillator.

The norm of this left inverse can be computed exactly.  It is at most one
if and only if the primitive Dirichlet inequality of row D holds.  Moreover,
the Moore--Penrose inverse has the smallest norm among all left inverses, so
no different choice of Poisson solution can evade this equivalence.

Local conservative dilations do not repair the problem.  The prime Szegő
block crosses the unit sphere, the Gamma differential has zero low-frequency
symbol, and the Julia defect operator exists as a positive operator exactly
when the same global contraction is already known.  A Krein-unitary
dilation always exists formally, but reproduces the signed form rather than
proving its Hodge sign.

The only maximum principle strong enough is a two-Tate nonlocal oscillation
theorem fixing the Schur complement/inertia of the shifted Dirichlet
operator.  That principle is equivalent to D; it is not a consequence of
the ordinary Markov maximum principle.

No zeta zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Exact projection onto both Tate jets

Fix a symmetric window \(I_T=[-T,T]\) and work in \(L^2(I_T)\), extending
functions by zero outside the window.  Let

\[
 h_-(t)=e^{-t/2},\qquad h_+(t)=e^{t/2}.                 \tag{1.1}
\]

The two moments are \(M_\pm(F)=\langle F,h_\pm\rangle\).  Their Gram
matrix is

\[
 G_T=
 \begin{pmatrix}
 2\sinh T&2T\\2T&2\sinh T
 \end{pmatrix}.                                         \tag{1.2}
\]

It is positive definite for \(T>0\), since \(\sinh T>T\).  If

\[
 H_T:\mathbb C^2\longrightarrow L^2(I_T),\qquad
 H_T(a,b)=ah_-+bh_+,
\]

then

\[
 P_T=I-H_TG_T^{-1}H_T^*                                \tag{1.3}
\]

is the orthogonal projection onto

\[
 \mathcal P_T=\ker M_-\cap\ker M_+.                    \tag{1.4}
\]

It satisfies

\[
 P_T^2=P_T=P_T^*,\qquad \|P_T\|=1.                     \tag{1.5}
\]

Reflection \(JF(t)=\overline{F(-t)}\) exchanges \(h_-\) and \(h_+\), so
\(JP_T=P_TJ\).  Fourier--Laplace transform sends (1.4) to vanishing at
\(\pm i/2\).  Thus (1.3) imposes both jets with the required Real/Fourier
covariance.

## 2. The source-defined boundary operator

For a contact cutoff \(X\) compatible with the window, D.111 constructs

\[
 \partial_XF=
 \left(
  \left(\sqrt{{\Lambda(n)\over\sqrt n}}
       (F-S_{\log n}F)\right)_{2\leq n\leq X},
  \partial_\infty F
 \right).                                                \tag{2.1}
\]

Every coefficient in (2.1) is obtained from the D.110 Frobenius-depth
Green kernel and the A--B contact.  The last component is the quarter-shift
Gamma heat module.  Set

\[
 B_{X,T}=\partial_XP_T:\mathcal P_T\longrightarrow\mathcal K_X,
 \qquad H_{X,T}=B_{X,T}^*B_{X,T}.                       \tag{2.2}
\]

Put

\[
 c_X=2A_X+m_0,qquad
 A_X=\sum_{2\leq n\leq X}{\Lambda(n)\over\sqrt n},
 \qquad m_0=\log\pi-\psi(1/4).                         \tag{2.3}
\]

The exact boundary expansion is

\[
 \langle(H_{X,T}-c_XI)F,F\rangle=-B_{\rm nuc}(F,F)
 \quad(F\in\mathcal P_T).                              \tag{2.4}
\]

## 3. Canonical Poisson--Calderón inverse

Assume first that \(B_{X,T}\) is injective with closed range.  Its
minimum-norm left inverse is

\[
 B_{X,T}^\dagger
 =H_{X,T}^{-1}B_{X,T}^*.                                \tag{3.1}
\]

Define

\[
 C_{X,T}^{\rm can}=\sqrt{c_X}\,B_{X,T}^\dagger.         \tag{3.2}
\]

Then

\[
 C_{X,T}^{\rm can}B_{X,T}=\sqrt{c_X},I_{\mathcal P_T}. \tag{3.3}
\]

Because (3.1) is formed from the geometric differential, its adjoint and
the two-jet projection, it inherits Real covariance.  Functional calculus
also makes it Fourier compatible.  No coefficient is discarded.

If \(\lambda_1(H_{X,T})\) denotes the bottom of the primitive spectrum,
then

\[
 \boxed{
 \|C_{X,T}^{\rm can}\|
 =\sqrt{{c_X\over\lambda_1(H_{X,T})}}.}                 \tag{3.4}
\]

Thus

\[
 \|C_{X,T}^{\rm can}\|\leq1
 \quad\Longleftrightarrow\quad
 H_{X,T}\geq c_XI
 \quad\Longleftrightarrow\quad
 B_{\rm nuc}|_{\mathcal P_T}\leq0.                    \tag{3.5}
\]

This is the requested factorization, but its contractivity is exactly the
theorem to be proved.

## 4. No alternative left inverse has a smaller norm

Let \(C:\mathcal K_X\to\mathcal P_T\) satisfy

\[
 CB_{X,T}=\sqrt{c_X}I.                                  \tag{4.1}
\]

For a unit primitive vector \(F\),

\[
 \sqrt{c_X}=\|CB_{X,T}F\|
 \leq\|C\|\,\|B_{X,T}F\|.
\]

Taking an infimum gives

\[
 \|C\|\geq\sqrt{{c_X\over\lambda_1(H_{X,T})}}.       \tag{4.2}
\]

Equality is attained by (3.2).  Therefore a contractive left inverse of
any kind exists if and only if (3.5) holds.  This conclusion uses no
particular formula for the Poisson solver.

If the range is not closed, the minimum singular value is zero and no
bounded left inverse exists at all.  Hence closed range is necessary, but
not sufficient for the sharp normalization.

## 5. The local blocks cannot be contracted separately

For \(\rho=p^{-1/2}\), the prime cyclic/Szegő operator is

\[
 A_p=\sqrt{1-\rho^2}(I-\rho U_p)^{-1}.                 \tag{5.1}
\]

Its squared boundary symbol is the Poisson kernel

\[
 P_\rho(e^{i\theta})
 ={1-\rho^2\over1-2\rho\cos\theta+\rho^2}.             \tag{5.2}
\]

Consequently

\[
 \|A_p\|=\sqrt{{1+\rho\over1-\rho}}>1,qquad
 \|A_p^{-1}\|=\sqrt{{1+\rho\over1-\rho}}>1.          \tag{5.3}
\]

Neither orientation is a contraction.  The sign change of
\(P_\rho-1\) is precisely the obstruction to a placewise comparison.

At the real place, the Fourier multiplier of
\(\partial_\infty^*\partial_\infty\) is

\[
 \ell_\infty(\tau)
 =\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4),        \tag{5.4}
\]

which vanishes at \(\tau=0\).  Hence the Gamma differential has no bounded
inverse before window boundary conditions and the two jets are imposed.

Thus \(C_{X,T}\) must be a genuinely global prime--Gamma operator.  It
cannot be assembled as an orthogonal sum of local contractions.

## 6. Conservative dilation audit

Given a contraction \(C\), its Julia colligation is

\[
 \mathcal U_C=
 \begin{pmatrix}
 C&(I-CC^*)^{1/2}\\
 (I-C^*C)^{1/2}&-C^*
 \end{pmatrix},                                         \tag{6.1}
\]

which is unitary after the standard identification of defect spaces.  For
\(C=C_{X,T}^{\rm can}\), the positive square roots in (6.1) exist exactly
when (3.5) holds.  Therefore Sz.-Nagy/Julia dilation does not prove the
contractivity; it starts after contractivity.

A Krein analogue can always encode the signed defects of a noncontraction.
Its pullback metric is then

\[
 c_XI-H_{X,T}=B_{\rm nuc}|_{\mathcal P_T},              \tag{6.2}
\]

so it recovers the exact form but does not choose its sign.  This is the
same signed preparation already obtained in D.86--D.110.

## 7. Maximum principle audit

The unshifted operator \(H_{X,T}\) is generated by a positive Dirichlet
form, so its resolvent is positivity preserving.  The desired operator is

\[
 L_{X,T}=H_{X,T}-c_XI.                                  \tag{7.1}
\]

An ordinary maximum principle for \(L_{X,T}\) holds only below the relevant
first eigenvalue.  On the primitive space this condition is

\[
 c_X\leq\lambda_1(H_{X,T}|_{\mathcal P_T}),             \tag{7.2}
\]

which is again (3.5).

For a local second-order operator, a Sturm oscillation theorem can sometimes
deduce a codimension-two inequality from two boundary solutions.  Here the
operator is nonlocal and its prime symbol changes sign relative to the
threshold.  The required replacement would be:

> **Two-Tate nonlocal oscillation principle.**  The Schur complement of
> \(L_{X,T}\) along the moment map \((M_-,M_+)\) has no negative direction,
> and the boundary Green matrix accounts for the complete negative inertia.

By the constrained inertia formula, this principle is equivalent to
(7.2).  Neither the Markov maximum principle nor conservative dilation
implies it.  It is a meaningful geometric theorem to seek, but cannot be
listed as already proved.

## 8. Outcome

The Poisson--Calderón construction is now explicit:

\[
 \boxed{
 C_{X,T}^{\rm can}
 =\sqrt{2A_X+m_0}\,
   \bigl((\partial_XP_T)^*(\partial_XP_T)\bigr)^{-1}
   (\partial_XP_T)^*.}                                  \tag{8.1}
\]

It satisfies the exact factorization, both Tate jets, Real/Fourier
covariance and the full prime--Gamma typing.  Its norm-one assertion is not
an omitted estimate: by (3.4) it is exactly row D.

The next noncircular route must prove the two-Tate nonlocal oscillation
principle from an additional variation-diminishing, geometric monotonicity
or reflection-positive structure on the completed stratified moduli.  The
existing local Poisson blocks and ordinary maximum principle do not supply
that structure.

