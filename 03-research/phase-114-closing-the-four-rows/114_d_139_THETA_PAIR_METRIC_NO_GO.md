# D.139 — The theta operator pair has no full-domain positive translation metric

## Verdict

The Jacobi-theta eigenvalue problem of Hedenmalm gives a new and very
natural possible source for the missing Hilbert metric.  In logarithmic
coordinates its operator pair is

\[
 (LD,L),\qquad D=-i\partial_x,\qquad
 L=-i(\partial_x+\phi'(x)),                            \tag{0.1}
\]

where

\[
 k(x)=e^{-\phi(x)}
 =\varTheta_{00}(i e^{2x})>0,\qquad
 \widehat k(\tau)=c_\Theta\Xi(\tau),\quad c_\Theta>0.  \tag{0.2}
\]

There is an exact obstruction to obtaining row D from a positive metric
defined on the whole source.  Let \(W\ge0\) be a Hilbert metric on the
range of \(L\), and suppose the pair is symmetric on a common
translation-invariant core:

\[
 \langle LDu,Lv\rangle_W=\langle Lu,LDv\rangle_W.     \tag{0.3}
\]

Writing \(C=\partial_x+\phi'\), condition (0.3) is equivalent to

\[
 [\partial_x,S]=0,\qquad S=C^*WC\ge0.                 \tag{0.4}
\]

Thus \(S\) is a positive translation-invariant operator, hence a
nonnegative Fourier multiplier.  But \(Ck=0\), so \(Sk=0\).  Since
\(\widehat k=c_\Theta\Xi\) is an entire function not identically zero, it is
nonzero almost everywhere on the real axis.  Therefore the multiplier of
\(S\) vanishes almost everywhere:

\[
 \boxed{S=0.}                                         \tag{0.5}
\]

Consequently there is no nondegenerate full-domain positive metric of this
kind.  In particular, no positive weighted \(L^2\) metric can make the
theta pair symmetric on all compactly supported smooth vectors.

This does not contradict Hedenmalm's conditional criterion: there
self-adjointness is required only on the finite span of the zero
eigenfunctions.  Constructing a positive metric on that spectral span is
already strong enough to imply RH.  The calculation here proves that such
a metric cannot be obtained by first defining a source-wide
translation-covariant Hilbert metric and then restricting it.

For the A--B--C program this has a concrete consequence.  The desired
comparison \(C_TX_T=Y_T\) cannot come from a local theta weight or from a
global convolution metric before the two Tate moments are shorted.  A
successful construction must be genuinely primitive, nonlocal, and
support-compatible; it must not extend to the unshorted theta source.

No location of a nontrivial zero is used, and the paper is not modified.

## 1. The theta vector and the logarithmic operator

Put \(t=e^x\).  Hedenmalm's positive inverse-symmetric theta function is

\[
 \varTheta_{00}(it^2)
 =\pi t^{9/2}\sum_{n\ge1}n^2(2\pi n^2-3t^{-2})
       e^{-\pi n^2t^2}.                               \tag{1.1}
\]

It satisfies

\[
 \varTheta_{00}(it^2)=\varTheta_{00}(it^{-2})          \tag{1.2}
\]

and has Gaussian decay at both ends.  Hence

\[
 k(x)=\varTheta_{00}(ie^{2x})                         \tag{1.3}
\]

is a positive even Schwartz function on \(\mathbb R\).  Its Fourier
transform is Riemann's Mellin representation:

\[
\begin{aligned}
 \widehat k(\tau)
 &=\int_{\mathbb R}k(x)e^{-i\tau x}\,dx\\
 &=\int_0^\infty\varTheta_{00}(it^2)t^{-i\tau}{dt\over t}
 =c_\Theta\Xi(-\tau)=c_\Theta\Xi(\tau).               \tag{1.4}
\end{aligned}
\]

Evenness is used in the last equality.  With the coefficient in (1.1) and
the standard normalization
\(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), direct Mellin
integration gives

\[
 c_\Theta={1\over2}.                                  \tag{1.5}
\]

Indeed, writing \(s=\tfrac12-i\tau\), the Mellin transform of (1.1) is

\[
 \pi^{-s/2}\zeta(s)
 \left(\Gamma\!\left({s+4\over2}\right)
 -{3\over2}\Gamma\!\left({s+2\over2}\right)\right)
 ={s(s-1)\over4}\pi^{-s/2}\Gamma(s/2)\zeta(s)
 ={1\over2}\xi(s).                                    \tag{1.6}
\]

Thus the displayed theta formula and a formula claiming \(c_\Theta=1\)
differ by a harmless global factor two.  The verifier below checks (1.5)
numerically.  The entire function \(\Xi\) is
not identically zero; its real zero set is discrete.  In particular,

\[
 \widehat k(\tau)\ne0\quad\text{for almost every }\tau\in\mathbb R. \tag{1.7}
\]

Set \(\phi=-\log k\).  In logarithmic coordinates,
Hedenmalm's multiplicative differential is \(D=-i\partial_x\), and

\[
 L=D+(D\phi)=-i(\partial_x+\phi')
 =-iC,\qquad C:=\partial_x+\phi'.                     \tag{1.8}
\]

The theta vector is the exact null vector:

\[
 Ck=(\partial_x+\phi')e^{-\phi}=0.                    \tag{1.9}
\]

## 2. Formal symmetry forces translation invariance

Let \(\mathscr D\) be a common core invariant under \(D,L\), and let
\(\langle f,g\rangle_W=\langle Wf,g\rangle_{L^2}\), where \(W\ge0\).
The same argument applies to a closed positive form provided every
composition below is interpreted in form sense.

Since

\[
 LD=(-iC)(-i\partial_x)=-C\partial_x,                 \tag{2.1}
\]

and \(\partial_x^*=-\partial_x\), one has

\[
 (LD)^*=\partial_x C^*,\qquad L^*=iC^*.               \tag{2.2}
\]

Condition (0.3) for all \(u,v\in\mathscr D\) is the operator-form identity

\[
 (LD)^*WL=L^*W(LD).                                   \tag{2.3}
\]

Substituting (2.1)--(2.2) gives

\[
 -i\,\partial_x C^*WC=-i\,C^*WC\,\partial_x.          \tag{2.4}
\]

Thus, with

\[
 S=C^*WC\ge0,                                         \tag{2.5}
\]

the exact symmetry equation is

\[
 \boxed{[\partial_x,S]=0.}                            \tag{2.6}
\]

This derivation is prior to any spectral decomposition of \(\Xi\).

## 3. Fourier multiplier rigidity

A closed positive operator (or closed positive form) commuting with the
translation group is diagonal under Fourier transform.  Thus there is a
measurable function \(s(\tau)\ge0\), possibly unbounded, such that

\[
 \widehat{Sf}(\tau)=s(\tau)\widehat f(\tau)            \tag{3.1}
\]

on its natural domain.

By (1.7) and (2.5),

\[
 Sk=C^*WCk=0.                                         \tag{3.2}
\]

Equations (1.4) and (3.1)--(3.2) imply

\[
 s(\tau)\Xi(\tau)=0\quad\text{for almost every }\tau. \tag{3.3}
\]

Using (1.5), \(s=0\) almost everywhere.  Hence \(S=0\).  If the metric is
supposed to be nondegenerate on \(\mathrm{Ran}\,C\), this is impossible,
because

\[
 \|Cu\|_W^2=\langle u,Su\rangle=0                     \tag{3.4}
\]

for every \(u\) in the core.

The argument uses only that \(\Xi\) is a nonzero entire function.  It does
not use whether any of its zeros is real or non-real.

## 4. The local weighted-\(L^2\) corollary

The same obstruction can be seen at the differential-coefficient level.
Suppose \(W\) is multiplication by a positive \(C^2\) weight \(w(x)\).
Then

\[
\begin{aligned}
 S&=C^*wC\\
  &=-w\partial_x^2-w'\partial_x
    +\bigl(-(w\phi')'+w(\phi')^2\bigr).               \tag{4.1}
\end{aligned}
\]

Commutation with \(\partial_x\) first forces \(w'=0\), and then forces

\[
 ((\phi')^2-\phi'')'=0.                               \tag{4.2}
\]

But as \(x\to+\infty\),

\[
 \phi(x)=\pi e^{2x}-{9\over2}x+O(1),                 \tag{4.3}
\]

so

\[
 (\phi')^2-\phi''
 =4\pi^2e^{4x}+O(e^{2x}),                             \tag{4.4}
\]

which is not constant.  Therefore no positive local weight works, even
before applying the Fourier rigidity theorem.

## 5. Why quotienting by the theta null vector is not enough

One may try to define

\[
 \|Lu\|_2:=\|u\bmod\mathbb Ck\|_{L^2}.                \tag{5.1}
\]

This is a legitimate quotient norm on \(\mathrm{Ran}\,L\), but it
does not make the original pair symmetric.  The reason is that \(D\) does
not preserve \(\ker L=\mathbb Ck\):

\[
 LD(u+ck)=LDu+c\,LDk,\qquad LDk\ne0.                  \tag{5.2}
\]

Equivalently, if \(Q\) is the orthogonal projection onto
\(k^\perp\), the symmetry defect is the rank-two form

\[
\begin{aligned}
 &\langle QDu,Qv\rangle-\langle Qu,QDv\rangle\\
 &\quad={-\langle Du,k\rangle\langle k,v\rangle
 +\langle u,k\rangle\langle k,Dv\rangle\over\|k\|^2}. \tag{5.3}
\end{aligned}
\]

This formula is the theta analogue of a boundary-polar defect.  Removing it
requires additional conditions on both \(u\) and \(Du\), not merely
quotienting by \(k\).

## 6. Consequence for the A--B--C contraction

D.137 reduced row D to a support-compatible contraction

\[
 C_T:\overline{X_T(\mathcal P_T)}\longrightarrow\mathcal Y_T,
 \qquad C_TX_T=Y_T.                                   \tag{6.1}
\]

The theta kernel packages Poisson summation, the Gamma factor and the
integer dilation sum in one positive source function.  It was therefore a
candidate for constructing (6.1).  Theorems (2.6)--(3.4) show exactly what
that candidate can and cannot do:

* a metric on the full theta source cannot be both positive and
  pair-symmetric;
* a local weighted \(L^2\) repair is impossible;
* quotienting by the theta kernel leaves the rank-two anomaly (5.3); and
* any successful metric must be imposed only after the primitive
  boundary data have been shorted.

This is consistent with the A--B--C typing: the two Tate moments are not
ordinary null vectors of the positive theta generator.  They are boundary
characters.  The next viable construction is therefore a **primitive
nonlocal metric** on the joint kernel of those characters.  Its acceptance
test remains (6.1), but D.139 proves that it cannot be inherited from a
source-wide Poisson \(L^2\) metric.

## 7. Exact outcome

The theta operator route provides a new source-derived eigenvalue pencil,
but its most natural Hilbert completions are ruled out before any zero
location is considered:

\[
\begin{array}{c|c}
\text{candidate metric}&\text{outcome}\\ \hline
\text{positive local }w(x)\,dx&\text{impossible by (4.2)--(4.4)}\\
\text{positive translation metric on full source}&S=0\\
\text{quotient by }\ker L&\text{rank-two anomaly (5.3)}\\
\text{metric only on the zero-eigenfunction span}&\text{would imply RH}\\
\text{primitive nonlocal A--B--C metric}&\text{remaining route}
\end{array}
\]

Thus the recent theta eigenvalue problem does not by itself furnish the
missing contraction.  It sharpens the construction target: \(C_T\) must be
primitive and nonlocal from the outset.
