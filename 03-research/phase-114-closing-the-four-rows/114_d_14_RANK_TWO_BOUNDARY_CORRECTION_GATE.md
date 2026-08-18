# Row (d): rank-two boundary correction gate

## Setup

On a finite logarithmic window let `H_T=L^2(-T,T)`, let

\[
 R_TF=\left(\int e^{-t/2}F(t)dt,
             \int e^{t/2}F(t)dt\right),
 \qquad P_T=\ker R_T,
\]

and let `a_T` be the closed form

\[
 a_T(F)=\mathcal D_{T,X}(F)-(2A_X+m_0)\|F\|^2
       =-B_{\rm nuc}(f,f).
\]

The desired Hodge assertion is `a_T >= 0` on `P_T` for every `T`.

## Proposition 1 (boundary forms vanish exactly where needed)

Every Hermitian correction depending only on the two ruling degrees has the
form

\[
 b_C(F,G)=\langle C R_TF,R_TG\rangle_{\mathbb C^2}
\]

for a Hermitian `2 by 2` matrix `C`.  It vanishes identically on
`P_T x P_T`.  Therefore

\[
 (a_T+b_C)|_{P_T}=a_T|_{P_T}.                       \tag{1}
\]

In particular, if `a_T+b_C` is proved nonnegative on its full form domain,
then row (d) on that window follows immediately.  But choosing `C` cannot
change a negative primitive vector.

### Proof

A sesquilinear form that factors through the two ruling functionals factors
through `R_T`, and hence is represented by a Hermitian matrix on
`C^2`.  Equation (1) follows from `R_TF=0` on `P_T`.

## Proposition 2 (Schur-complement content)

Assume for clarity that the form operator has compact resolvent and that
zero is not in the spectrum of its compression to `P_T`.  Decompose

\[
 H_T=P_T\oplus E_T,
 \qquad E_T=(P_T)^\perp=\mathrm{span}\,\{e^{-t/2},e^{t/2}\}.
\]

Relative to this decomposition, write the form operator as

\[
 A_T=\begin{pmatrix}A_{PP}&A_{PE}\\A_{EP}&A_{EE}\end{pmatrix}.
\]

There exists a ruling correction `C` for which `A_T+R_T^*CR_T` is
nonnegative if and only if `A_PP` is positive.  When this holds, the least
correction is governed by the Schur complement

\[
 A_{EE}+R_T^*CR_T-A_{EP}A_{PP}^{-1}A_{PE}\ge0.      \tag{2}
\]

### Proof

Necessity is restriction to `P_T`.  If `A_PP>0`, completing the square in
the `P_T` variable shows that the full block form is nonnegative precisely
when (2) holds.  Since `R_T:E_T\to\mathbb C^2` is an isomorphism, an
arbitrarily large positive Hermitian `C` makes (2) hold.  This proves
sufficiency.

If `A_PP` is merely semidefinite, the same statement requires the equality
condition

\[
 \ker A_{PP}\subseteq\ker A_{EP};                  \tag{3}
\]

otherwise a null primitive vector with nonzero mixed block makes every
completion indefinite.  Condition (3) is exactly the additional equality
theorem expected in a complete Hodge package.

## Consequence

A freely chosen rank-two boundary term is not a new proof mechanism.  Its
ability to make the full operator positive is equivalent to primitive
positivity, together with the equality condition at zero.  The correction
becomes useful only if geometry independently supplies a specific `C` and
a positivity theorem for the completed form.

Thus the two rulings correctly identify the codimension-two primitive
space, but they cannot repair the arithmetic jump form algebraically.  A
non-circular closure still needs either:

1. a geometric current/line bundle whose already-positive curvature gives
   `a_T+b_C`; or
2. a direct boundary theorem proving the constrained eigenvalue bound.

Defining `C` by the Schur complement (2) is circular, because computing that
the complement is bounded below presupposes the sign of `A_PP`.

## The continuous model explains what a genuine boundary correction is

Let

\[
 Q_0(F)=\iint_{[-T,T]^2}e^{|t-s|/2}F(t)\overline{F(s)}\,dt\,ds,
 \qquad
 u(t)=\int_{-T}^{T}e^{|t-s|/2}F(s)\,ds.
\]

Since \((d^2/dt^2-1/4)u=F\), integration by parts now gives, without
assuming the two moments vanish,

\[
 Q_0(F)=-\int_{-T}^{T}
 \left(|u'|^2+\frac14|u|^2\right)dt
 +\frac{e^T}{2}\left(|R_TF|_1^2+|R_TF|_2^2\right).  \tag{4}
\]

Indeed, outside the interval

\[
 u(t)=e^{t/2}(R_TF)_1\quad(t>T),
 \qquad
 u(t)=e^{-t/2}(R_TF)_2\quad(t<-T),
\]

so the last term of (4) is exactly
\([u'\bar u]_{-T}^{T}\).  Hence the rank-two correction

\[
 -Q_0(F)+\frac{e^T}{2}\|R_TF\|^2
 =\int_{-T}^{T}\left(|u'|^2+\frac14|u|^2\right)dt   \tag{5}
\]

is positive for a reason independent of the primitive sign: it is the
boundary term in a differential Green identity.  This is the model the
arithmetic construction would have to reproduce.  Merely selecting a
matrix `C` after inspecting the spectrum is not analogous to (5).

For the arithmetic jump operator no corresponding rank-two flux identity
has been obtained.  Its nonlocal exterior flux depends on the whole
boundary profile of `F`, not only on the two numbers `R_TF`; the finite-prime
translations and the continuous gamma jump measure both contribute such
profile-dependent terms.

This failure can be made exact.  Write the positive jump measure as

\[
 \nu_X=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}
 +\frac{e^{-r/2}}{1-e^{-2r}}\,dr.
\]

Splitting the jump energy of the zero extension into pairs lying inside
the interval and pairs crossing its boundary gives

\[
 \mathcal D_{T,X}(F)=\mathcal D_{T,X}^{\rm int}(F)
 +\int_{-T}^{T}V_{T,X}(t)|F(t)|^2dt,                 \tag{6}
\]

where

\[
 V_{T,X}(t)=\nu_X((T-t,\infty))+\nu_X((T+t,\infty)). \tag{7}
\]

The gamma part makes `V_{T,X}` a nonconstant positive function on every
open subinterval; it diverges logarithmically at the endpoints in the form
sense.  Therefore the boundary-flux form in (6) has infinite algebraic
rank.  Indeed, restricting multiplication by `V_{T,X}` to arbitrarily many
disjoint compact subintervals produces arbitrarily many independent
positive directions.  A form factoring through `R_T` has rank at most two.

Hence the actual nonlocal boundary flux cannot equal a ruling correction
`R_T^* C R_T`.  Any successful rank-two identity would have to cancel the
infinite-rank flux against the internal contact and Green pieces before
taking the boundary, which is exactly the missing global comparison.

## Why min--max and oscillation do not add a sign

Let \(L_{T,X}\) be the positive jump operator and write its unconstrained
eigenvalues as

\[
 \mu_1\le\mu_2\le\mu_3\le\cdots.
\]

The codimension-two min--max principle only yields

\[
 \mu_1\le\lambda_1(T;X)\le\mu_3.                    \tag{8}
\]

Positivity improvement of the jump semigroup can prove that \(\mu_1\) is
simple and has a positive eigenfunction.  It neither places \(\mu_3\) nor
the constrained eigenvalue relative to the required threshold
\(2A_X+m_0\).  An oscillation theorem similarly orders nodal counts but
does not supply that numerical location.

A totally-positive kernel strong enough to imply
\(\lambda_1(T;X)\ge2A_X+m_0\) would solve the problem, but verifying that
property for the arithmetic kernel includes all minors of its primitive
compression.  In particular its first nontrivial quadratic minor is the
primitive form itself.  Thus total positivity cannot be inferred from the
positive jump weights alone; it is another formulation of the missing
boundary inequality unless a separate geometric factorization is supplied.

Finally, `a_T` already defines a self-adjoint compact-resolvent operator by
the closed-form construction.  A bounded rank-two perturbation preserves
self-adjointness and compact resolvent.  It therefore cannot create the
missing sign through a choice of extension: only the Schur-complement
positivity, which is equivalent to the primitive assertion, remains.
