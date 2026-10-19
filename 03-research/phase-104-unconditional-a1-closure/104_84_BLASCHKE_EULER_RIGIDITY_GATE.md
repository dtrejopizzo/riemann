# 104_84 — Inner Blaschke factor and rigidity of local Euler identities

**Result.** The deep observable of `104_75` admits a canonical boundary
on the disk. Define

\[
 s(z)={1\over1-z},\qquad
 E(z)=(s(z)-1)\zeta(s(z)),\qquad E(0)=1.                 \tag{1}
\]

The zeros of \(E\) in \(\mathbb D\) are exactly

\[
 w_\rho={\rho-1\over\rho},\qquad \Re\rho>{1\over2}.    \tag{2}
\]

They form a Blaschke sequence. If \(B\) is its inner product, then

\[
 \boxed{
 {1\over2\pi}\int_{-\infty}^{\infty}
 {\log|\zeta(\tfrac12+it)|\over t^2+\tfrac14}\,dt
 =-\log B(0)
 =\sum_{\Re\rho>1/2}m_\rho
       \log{|\rho|\over|\rho-1|}\ge0.}                 \tag{3}
\]

The deep limit, the absence of interior poles of `104_80`,
\(B\equiv1\), equality to zero in (3), and RH are the same statement. Equation
(3) is the Balazard--Saias--Yor criterion written in the coordinate
of this phase.

There is also an algebraic rigidity. Every modification by analytic local
Euler factors whose first prime coefficient is constant factors
as a power of \(\zeta\) times a holomorphic, non-vanishing factor in
\(\Re s>1/2\). For this reason Möbius, *squarefree*, \(\zeta(2s)\), and any
finite local Euler identity have an exact dichotomy: they preserve the
inner factor with the same multiplicity, or they also cancel the entire
observable. They cannot prove (3) with equality.

This does not prove Deep-\(\Lambda\), A1, or RH. It identifies precisely the
only non-ruled-out successor: a genuinely non-local inequality between
primes that proves \(B(0)=1\). A new local factorization, a boundary
modulus bound, or a convolution identity do not suffice.

---

## 1. Geometry of the disk

The map \(s=(1-z)^{-1}\) sends \(\mathbb D\) onto
\(\Re s>1/2\), and

\[
 |w_\rho|<1
 \quad\Longleftrightarrow\quad
 |\rho-1|<|\rho|
 \quad\Longleftrightarrow\quad
 \Re\rho>{1\over2}.                                    \tag{4}
\]

Moreover,

\[
 1-|w_\rho|^2={2\Re\rho-1\over|\rho|^2}
 \le {1\over|\rho|^2}.                                 \tag{5}
\]

Riemann--von Mangoldt implies
\(\sum_\rho |\rho|^{-2}<\infty\). By (5), the interior zeros
satisfy

\[
 \sum_{\Re\rho>1/2}m_\rho(1-|w_\rho|)<\infty.          \tag{6}
\]

Its Blaschke product converges:

\[
 B(z)=\prod_{\Re\rho>1/2}
 \left\{
 { |w_\rho|\over w_\rho}
 {w_\rho-z\over1-\overline{w_\rho}z}
 \right}^{m_\rho}.                                    \tag{7}
\]

The function in (1) is of Smirnov class on the disk: after cancelling the
pole of \(\zeta\) at \(s=1\), the polynomial growth bounds of
\((s-1)\zeta(s)\) on \(\Re s\ge1/2\), transported by the conformal map,
give integrability of \(\log^+|E|\). It continues across every arc of
\(\partial\mathbb D\) except \(z=1\); there it has polynomial growth.
Hence no singular inner factor appears and the canonical factorization
has the form

\[
 E(z)=B(z)O(z),                                         \tag{8}
\]

with \(O\) outer.

## 2. Jensen identity

On the boundary, away from \(z=1\), write \(z=e^{i\theta}\). Then

\[
 s(e^{i\theta})={1\over2}+{i\over2}\cot{\theta\over2}
 ={1\over2}+it,\qquad
 |d\theta|={dt\over t^2+1/4}.                           \tag{9}
\]

The radial Jensen formula, followed by the limit \(r\uparrow1\), gives

\[
 {1\over2\pi}\int_0^{2\pi}\log|E(e^{i\theta})|\,d\theta
 =\sum_{\Re\rho>1/2}m_\rho\log{1\over|w_\rho|},        \tag{10}
\]

because \(E(0)=1\). On \(|z|=1\),

\[
 \log|E(z)|=\log|\zeta(\tfrac12+it)|+log|s-1|.         \tag{11}
\]

The second term has zero mean. Indeed,
\(s-1=z/(1-z)\), so that

\[
 {1\over2\pi}\int_0^{2\pi}\log|s-1|\,d\theta
 =-{1\over2\pi}\int_0^{2\pi}\log|1-e^{i\theta}|\,d\theta
 =0.                                                     \tag{12}
\]

Equations (9)--(12) prove (3). Every summand on its right-hand side is
strictly positive. Using the functional symmetry
\(\rho\mapsto1-\overline\rho\), one obtains

\[
 \text{right-hand side of (3)}=0
 \quad\Longleftrightarrow\quad \mathrm{RH}.            \tag{13}
\]

The boundary modulus does not see the inner factor pointwise:
\(|B(e^{i\theta})|=1\) almost everywhere. Only the interior
normalization \(B(0)\), recovered via Jensen, registers the right-half
zeros.

## 3. What exactly the ordinary primes fix

The Euler half-plane \(\Re s>1\) corresponds to the horodisk

\[
 \left|z-{1\over2}\right|<{1\over2}.                   \tag{14}
\]

There,

\[
 E(z)={z\over1-z}
 \prod_p\left(1-p^{-1/(1-z)}\right)^{-1}.              \tag{15}
\]

The exact values of (15) on any open set, or even on a real
interval with an accumulation point, fix \(E\) on its whole domain by
the identity theorem. In particular they fix \(B\) and \(O\). This is a
uniqueness of the function, not a proof that \(B=1\): evaluating or
continuing the already-determined function does not supply the opposite
sign needed to cancel the positive sum in (3).

The functional equation only pairs the interior zero \(w_\rho\) with the
exterior one \(1/\overline{w_\rho}\). It does not force both to lie on
\(|z|=1\).

## 4. Local Euler rigidity lemma

Let \(\phi\) be analytic and non-vanishing near zero, with

\[
 \phi(0)=1,\qquad \log\phi(u)=cu+O(u^2).                \tag{16}
\]

For \(\Re s>1\), define

\[
 F_\phi(s)=\prod_p\phi(p^{-s}).                         \tag{17}
\]

Then, on that half-plane,

\[
 F_\phi(s)=\zeta(s)^cH_\phi(s),                        \tag{18}
\]

where

\[
 \log H_\phi(s)=
 \sum_p\left\{\log\phi(p^{-s})+c\log(1-p^{-s})\right\}.
                                                               \tag{19}
\]

Each summand of (19) is \(O(p^{-2\Re s})\), locally uniformly. The series
converges normally on \(\Re s>1/2\), so \(H_\phi\) is
holomorphic and non-vanishing there. In terms of logarithmic
derivatives,

\[
 -{F_\phi'\over F_\phi}
 =-c{\zeta'\over\zeta}-{H_\phi'\over H_\phi}.         \tag{20}
\]

If \(\rho\) is a right-hand zero of multiplicity \(m_\rho\), the first
term of (20) has residue \(-cm_\rho\) and the second is holomorphic.
Therefore:

* if \(c\ne0\), the transformation preserves the pole that generates
  Deep-\(\Lambda\), only scaled by \(c\);
* if \(c=0\), the product is non-vanishing on \(\Re s>1/2\), but it has
  also removed all information about the zeros of \(\zeta\).

This includes the coordinates

\[
 {\zeta(s)\over\zeta(2s)},\qquad {1\over\zeta(s)},
 \qquad {\zeta(s)^2\over\zeta(2s)},                    \tag{21}
\]

and the finite local Euler identities obtained from Möbius or from the
*squarefree* restriction. Since \(\Re(2\rho)>1\), a correction built
with \(\zeta(2s)\) is holomorphic and non-vanishing at \(\rho\); it cannot
selectively cancel the zero.

The functional equation does not alter the dichotomy either:

\[
 \zeta(1-s)=\chi(s)^{-1}\zeta(s).                       \tag{22}
\]

Thus, \(\zeta(s)^a\zeta(1-s)^b\) preserves the zero with multiplicity
\(a+b\) if \(a+b\ne0\); if \(a+b=0\), only the explicit Gamma factor
\(\chi^{-b}\) remains, which does not contain the arithmetic sought.

## 5. Falsifier of the qualitative properties

The exactness of (15) admits no distinct counter-model: preserving its
values on an open set forces coincidence with \(E\). But the qualitative
properties that usually substitute for that exactness do admit an
arbitrary inner factor.

For \(0<\delta<1/2\), \(\gamma>0\), set

\[
 X_{\delta,\gamma}(s)=C
 \left((s-\tfrac12-i\gamma)^2-\delta^2\right)
 \left((s-\tfrac12+i\gamma)^2-\delta^2\right),          \tag{23}
\]

with \(C>0\) chosen so that \(X_{\delta,\gamma}(1)=1\). Then

\[
 X_{\delta,\gamma}(s)=X_{\delta,\gamma}(1-s),          \tag{24}
\]

is real on the real axis, positive and non-vanishing for \(s>1\), and adds
the quartet

\[
 {1\over2}\pm\delta\pm i\gamma.                        \tag{25}
\]

Hence \(\xi(s)X_{\delta,\gamma}(s)\) preserves the functional equation,
reality, finite order, normalization, and positivity on the Euler ray, but
has \(B\ne1\). It does not preserve the exact ordinary Euler values; doing
so is impossible by analytic uniqueness.

## 6. Decision

```text
proved:
  Deep-Lambda = absence of the inner Blaschke factor;
  exact BSY/Jensen identity (3);
  the exact Euler product determines the function, but does not give B(0)=1;
  every local Euler identity preserves the pole or erases the observable;
  FE and the boundary modulus alone do not detect B.

ruled out:
  another local factorization Möbius/squarefree/zeta(2s)
  + functional equation or boundary modulus
  => Deep-Lambda.

only successor not ruled out by this gate:
  a non-local inequality, specific to the joint placement of the
  ordinary primes, that proves B(0)=1.

not proved:
  B(0)=1, Deep-Lambda, A1, or RH.
```
