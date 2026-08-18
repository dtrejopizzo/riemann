# D.62 — The continuum Hodge Green form and the exact arithmetic defect

## 1. Purpose

The finite-place part of the direct operator is the symmetrized translation
sum

\[
 V_{\rm ar}(F,G)=\sum_{n\geq2}{\Lambda(n)\over\sqrt n}
 \left(\langle F,S_{\log n}G\rangle
      +\langle F,S_{-\log n}G\rangle\right).              \tag{1.1}
\]

For compactly supported functions the sum is finite.  This note separates
from (1.1) an exactly soluble continuum model.  The model already contains
the two Tate rulings and has the desired Hodge sign by an elementary Green
identity.  What remains is a single, explicitly displayed arithmetic-defect
form.  No sign is asserted for that defect.

## 2. The continuum prime measure

The atomic measure underlying (1.1) is

\[
 d\nu_{\rm ar}(a)=\sum_{n\geq2}{\Lambda(n)\over\sqrt n}
                  \delta_{\log n}(da).                    \tag{2.1}
\]

Its prime-number-theorem continuum is

\[
 d\nu_0(a)=e^{a/2}\,da,\qquad a>0,                       \tag{2.2}
\]

because `x=e^a` gives `x^(-1/2)dx=e^(a/2)da`.  Define

\[
 V_0(F,G)=\int_0^\infty e^{a/2}
 \left(\langle F,S_aG\rangle+
       \langle F,S_{-a}G\rangle\right)da.                \tag{2.3}
\]

Fubini is legitimate for compact supports.  Splitting the `(x,y)` plane
into `x>y` and `y>x` gives the exact kernel

\[
 \boxed{
 V_0(F,G)=\iint_{\mathbb R^2}
 e^{|x-y|/2}\,\overline{F(x)}G(y)\,dx\,dy.}              \tag{2.4}
\]

Thus the continuum model is not an asymptotic slogan: it is the integral
operator with Green kernel

\[
 k(t)=e^{|t|/2}.                                          \tag{2.5}
\]

## 3. The two Tate jets are its boundary data

Let

\[
 (K_0F)(x)=\int_{\mathbb R}e^{|x-y|/2}F(y)\,dy.           \tag{3.1}
\]

If `supp(F) subset [-T,T]`, then outside the support

\[
 K_0F(x)=
 \begin{cases}
 e^{x/2}M_-(F),&x>T,\\
 e^{-x/2}M_+(F),&x<-T,
 \end{cases}                                              \tag{3.2}
\]

where

\[
 M_-(F)=\int e^{-y/2}F(y)dy,\qquad
 M_+(F)=\int e^{y/2}F(y)dy.                               \tag{3.3}
\]

Consequently

\[
 F\in\ker M_-\cap\ker M_+
 \quad\Longrightarrow\quad
 K_0F\text{ is supported in }[-T,T].                     \tag{3.4}
\]

This is the exact continuum meaning of the two rulings: they kill the two
exterior homogeneous solutions of the Green equation.

## 4. Strict Hodge sign of the continuum form

In distributions,

\[
 \left({d^2\over dx^2}-{1\over4}\right)e^{|x|/2}=\delta_0,
                                                                    \tag{4.1}
\]

because the first derivative has jump one at the origin.  Put `u=K_0F`.
For primitive `F`, (3.4) and (4.1) give

\[
 F=u''-{1\over4}u,
 \qquad u\in H^1_0([-T,T]).                               \tag{4.2}
\]

Integration by parts now proves

\[
 \boxed{
 V_0(F,F)=-\int_{-T}^T
 \left(|u'(x)|^2+{1\over4}|u(x)|^2\right)dx<0}           \tag{4.3}
\]

for every nonzero primitive `F`.  Equality forces `u=0`, hence `F=0` by
(4.2).  This is a literal index/Hodge identity, not a spectral or numerical
approximation.

## 5. Exact arithmetic-defect decomposition

Set

\[
 d\varepsilon(a)=d\nu_{\rm ar}(a)-e^{a/2}da.             \tag{5.1}
\]

Then

\[
 \boxed{V_{\rm ar}=V_0+V_\varepsilon,}                   \tag{5.2}
\]

where

\[
 V_\varepsilon(F,G)=\int_0^\infty
 \left(\langle F,S_aG\rangle+
       \langle F,S_{-a}G\rangle\right)d\varepsilon(a). \tag{5.3}
\]

Together with D.32 and D.52, the complete primitive form is therefore

\[
 B_{\rm nuc}|_{\mathcal P}
 =V_0|_{\mathcal P}+
   (V_\varepsilon+\Gamma)|_{\mathcal P}.                 \tag{5.4}
\]

The first summand has the strict negative square (4.3).  Every prime power,
including multiplicity, remains in `d epsilon`; the Gamma oscillator remains
complete in `Gamma`.  Nothing has been truncated or averaged in (5.4).

## 6. Why a prime-number-theorem norm bound is not enough

The strictness of (4.3) is not an `L^2` coercive bound uniform in frequency:
from (4.2), the continuum Green operator has symbol
`-(tau^2+1/4)^(-1)` on the primitive extension.  Its negative eigenvalues
approach zero at high frequency.  Therefore a total-variation or operator-
norm estimate on `V_epsilon` cannot by itself prove (5.4) negative.

Likewise, the classical prime-number-theorem error is far too large near a
moving endpoint if estimated before the two moment cancellations.  A valid
global theorem must compare `V_epsilon+Gamma` to the Green energy in (4.3)
in the correct graph norm, or prove the equivalent parity--Feshbach signs of
D.56.  Treating (5.1) merely as a small measure would lose the central
arithmetic cancellation and would not close row D.

## 7. Result and next gate

Closed here:

* the continuum analogue of every finite-place translation;
* the exact identification of the two A--B--C moments with Green boundary
  data;
* a strict negative-square Hodge identity on the primitive space;
* the exact, nonasymptotic isolation of the remaining arithmetic defect.

The surviving global statement is the graph-norm domination

\[
 (V_\varepsilon+\Gamma)(F,F)
 \leq -V_0(F,F),\qquad F\in\mathcal P,                   \tag{7.1}
\]

with strictness in the appropriate finite-window sense.  By (5.4), (7.1)
is exactly the row-D sign, so it is recorded as the next theorem to prove,
not assumed here.

