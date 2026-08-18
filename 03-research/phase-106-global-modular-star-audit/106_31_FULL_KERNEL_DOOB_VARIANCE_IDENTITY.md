# 106.31 — The full-kernel Doob--variance identity

## Purpose

The smooth truncation of Riemann's kernel in 106.27 proves an operator
quasimode, but the complementary floor remains open.  This note removes the
cutoff from the algebra before estimating anything.  It uses the full positive
Riemann kernel $K$, whose transform is $\Xi$, as an exact ground function.

For every even compactly supported multiplier $r$, the completed Weil form has
the exact representation

\[
 \boxed{
 QW(Kr,Kr)=\mathscr E_K(r)-2c_K^2\operatorname {Var}_{\mu_K}(r).}
 \tag{1}
\]

Here $\mathscr E_K$ is a positive jump energy containing jointly every
ordinary von Mangoldt atom and the full Gamma jump measure, while
$\mu_K$ is an explicit probability measure coming from the two polar
evaluations.  Thus Weil positivity becomes one fixed Poincare inequality on
the full line.  The identity is unconditional.  The Poincare inequality is
not proved here.

## 1. Setup

Use the additive Fourier convention of 106.17.  Normalize Riemann's even
kernel by

\[
 \widehat K(z)=\Xi(z).
 \tag{2}
\]

The theta-series representation shows that $K$ is smooth, even, strictly
positive, and double-exponentially decreasing.  Indeed, up to the positive
normalizing constant forced by (2), for $x\geq0$,

\[
 K(x)=C_\Xi\sum_{m\geq1}
 \left(2\pi^2m^4e^{9x/2}-3\pi m^2e^{5x/2}\right)
 e^{-\pi m^2e^{2x}},
 \qquad C_\Xi>0,
 \tag{3}
\]

and every summand is positive because
$2\pi m^2e^{2x}-3>0$.  Evenness supplies the negative half-line.

Put

\[
 h(x)=\cosh(x/2),\qquad
 c_K=\int_{\mathbb R}h(x)K(x)\,dx>0,
 \tag{4}
\]

Evenness of $K$ and the Fourier convention give

\[
 c_K=\widehat K(i/2)=\Xi(i/2)=\xi(0)=\frac12.
 \tag{4a}
\]

Define the probability measure

\[
 d\mu_K(x)=\frac{h(x)K(x)}{c_K}\,dx.
 \tag{5}
\]

The complete positive jump measure is

\[
 \nu_\zeta(du)
 =\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
   \delta_{\log n}(du)
 +\frac{e^{-u/2}}{1-e^{-2u}}\,du,
 \qquad u>0.
 \tag{6}
\]

For even $r\in C_c^\infty(\mathbb R)$, set

\[
 \boxed{
 \mathscr E_K(r)
 :=\int_{(0,\infty)}\!\int_{\mathbb R}
 K(x)K(x-u)|r(x)-r(x-u)|^2\,dx\,\nu_\zeta(du).}
 \tag{7}
\]

This is finite.  Near $u=0$, the Gamma density is $1/(2u)+O(1)$
and the squared difference is $O(u^2)$.  For large $u$, one of
$x,x-u$ lies outside the fixed support of $r$; the double-exponential
decay of the corresponding $K$-factor dominates both the Gamma tail and
the aggregate von Mangoldt mass $e^{u/2+o(u)}$.

## 2. Exact identity

### Theorem 1 — Full-kernel Doob--variance formula

For every even complex $r\in C_c^\infty(\mathbb R)$,

\[
 \boxed{
 QW(Kr,Kr)
 =\mathscr E_K(r)
 -2c_K^2
 \left(
  \int |r|^2\,d\mu_K
  -\left|\int r\,d\mu_K\right|^2
 \right).}
 \tag{8}
\]

#### Proof

Use the convention of 106.17: the inner product and $QW$ are
conjugate-linear in the first entry and linear in the second.  The polarized
zero-side domain statement of 106.27(19), together with (2), gives

\[
 QW(K,g)=0
 \tag{9}
\]

for every Weil-admissible $g$: at each nontrivial zero the transform of
$K$ vanishes.  In particular, with $g=K|r|^2$,

\[
 QW(K,K|r|^2)=0.
 \tag{10}
\]

First multiply $K$ by a common smooth spatial cutoff and use the same prime
cutoff $n\leq N$ in both physical-side expressions.  Write $QW_N$ for the
completed physical form with this prime cutoff but with the full Gamma and
polar terms, and write $\mathscr E_{K,N}$ for (7) with the same prime cutoff
and the full Gamma measure.  Subtract the two regulated forms before removing
either cutoff.  Neither separately regulated expression is asserted to equal
the full zero-side form.  At each retained jump
$u>0$, with $K_x=K(x)$, $K_y=K(x-u)$, $r_x=r(x)$, and
$r_y=r(x-u)$, the Picone identity is

\[
 \begin{aligned}
 |K_xr_x-K_yr_y|^2
 &-(K_x-K_y)
   \bigl(K_x|r_x|^2-K_y|r_y|^2\bigr)\\
 &=K_xK_y|r_x-r_y|^2.
 \end{aligned}
 \tag{11}
\]

Integrating (11) against the regulated positive prime--Gamma jump measure
gives the corresponding regulated difference.  At a finite spatial cutoff,
$K$, $c_K$, and $\mu_K$ in this calculation are replaced by their cutoff
versions; (11)--(14) record the limits after that cutoff is removed.  The
scalar centering term
cancels exactly, cutoff by cutoff, when
$QW_N(Kr,Kr)$ and $QW_N(K,K|r|^2)$ are subtracted, since

\[
 \|Kr\|_2^2=\langle K,K|r|^2\rangle.
 \tag{12}
\]

In the even sector the two polar evaluations have the rank-one form

\[
 2\overline{\langle h,f\rangle}\langle h,g\rangle.
 \tag{13}
\]

Their contribution to the same subtraction is

\[
 \begin{aligned}
 2\left|\int hKr\right|^2
 -2\left(\int hK\right)\left(\int hK|r|^2\right)
 &=-2c_K^2\operatorname {Var}_{\mu_K}(r).
 \end{aligned}
 \tag{14}
\]

Equations (11)--(14) identify the regulated difference.  Remove the spatial
cutoff by dominated convergence.  For clarity, after this first limit and
before removing the prime cutoff, the identity is

\[
 \begin{aligned}
 &QW_N(Kr,Kr)-QW_N(K,K|r|^2)\\
 &\qquad=\mathscr E_{K,N}(r)
 -2c_K^2\operatorname {Var}_{\mu_K}(r),
 \end{aligned}
 \tag{14a}
\]

where $\mathscr E_{K,N}$ contains all Gamma jumps and only the prime-power
atoms with $n\leq N$.  In particular, (14a) does not set its second term on
the left to zero.

Now let $N\to\infty$.  For $QW_N(Kr,Kr)$ the Euler sum eventually
stabilizes because $Kr$ is compactly supported.  For
$QW_N(K,K|r|^2)$ the Euler series converges absolutely: one factor is
supported in a fixed compact set and the translated $K$ factor has
double-exponential decay, which dominates the aggregate von Mangoldt
weight.  Thus the left side tends to

\[
 QW(Kr,Kr)-QW(K,K|r|^2)=QW(Kr,Kr)
\]

by (10).  On the right, monotone convergence of the nonnegative prime part
gives $\mathscr E_{K,N}(r)\to\mathscr E_K(r)$; the Gamma part was already
retained in full and is finite by the small-$u$ estimate following (7).
This proves (8).  \(\square\)

The proof is stated in the even normalization because that is the branch
used in 106.11 and 106.25.  The corresponding two-channel statement before
parity projection follows by retaining the separate $e^{x/2}$ and
$e^{-x/2}$ polar functionals.

## 3. Exact remaining inequality

Since $K(x)>0$, every even compactly supported smooth test $f$ can be written
uniquely as $f=Kr$ with even compactly supported smooth $r=f/K$.  By the
bilateral parity-detection theorem of 106.11, failure of RH already produces
a negative even test.  Hence positivity on the even sector is equivalent to
the full Weil criterion.  Therefore Theorem 1 gives the exact equivalence

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \mathscr E_K(r)\geq
 \frac12\operatorname {Var}_{\mu_K}(r)
 \quad\text{for every even }r\in C_c^\infty(\mathbb R).}
 \tag{15}
\]

Constants do not affect either side.  Hence (15) is a spectral-gap
inequality for one explicit reversible jump energy, rather than a family of
cutoff-dependent inequalities.  All prime powers, Gamma, the pole and the
functional equation are still present: the functional equation enters
through the exact radical $\widehat K=\Xi$, and the pole becomes the
variance measure (5).

The one-atom falsifier of 106.19 does not satisfy (9) with Riemann's $K$,
so it cannot falsify the identity or supply the missing inequality.  This is
precisely the zeta-specific input absent from generic positive-jump
arguments.

## 4. Nonduplication audit and status

The semantic audit found the following nearest predecessors.

1. 106.19 proves a zero-extension Picone formula using an unspecified
   positive comparison function and shows that using the true ground state
   merely reproduces the unknown spectral gap.
2. Phases 60 and 72 study Doob transforms of finite semilocal ground states;
   the ground state is not explicit there and the polar term is not converted
   into the probability variance (14).
3. 106.27 proves that smooth truncations of $K$ are operator quasimodes,
   but it does not subtract the exact full-kernel radical identity.
4. The audited CCM and Suzuki papers formulate finite semilocal operators,
   determinant or screw-function limits, and Weil positivity.  They do not
   state (8), the measure (5), or the fixed full-line Poincare problem (15).

Thus (8) is the explicit full-radical specialization of the Picone algebra
already present in 106.19.  The specialization to $K$ and the exact variance
normalization were not previously written in the audited project or sources.
It is a new coordinate, not a new positivity mechanism.  It does not prove
(15).  The next and only mathematical task in this coordinate is to prove
the sharp $K$-weighted all-prime Poincare
constant $2c_K^2=1/2$, or to produce an actual Riemann-weight countervector.
