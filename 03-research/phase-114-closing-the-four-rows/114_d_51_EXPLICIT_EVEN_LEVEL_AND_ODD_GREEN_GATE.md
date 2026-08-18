# D.51 — Explicit even level and the complete odd Green-function gate

## 1. Purpose

D.50 reduces parity ordering to a source-defined scalar estimate.  This
note chooses a completely explicit even trial vector, evaluates its energy
using **all** prime powers and the full Gamma kernel, and writes the exact
odd resolvent inequality which would prove that this even level lies below
the whole odd spectrum.

No zero of zeta is used.  The outcome is an exact quantitative target, not
a proof of its sign.

## 2. The complete source operator

Work on `I_T=[-T,T]` with zero extension.  Put

\[
 \mathcal P_T=\{(p,k):p\text{ prime},\ k\geq1,\ k\log p\leq2T\},
 \qquad c_{p,k}={\log p\over p^{k/2}},                         \tag{2.1}
\]

and

\[
 w_\infty(r)={e^{-r/2}\over1-e^{-2r}},\qquad
 m_0=\log\pi-\psi(1/4),\qquad
 m_T=2\sum_{(p,k)\in\mathcal P_T}c_{p,k}+m_0.                \tag{2.2}
\]

The D.49 Levy form is

\[
 \begin{aligned}
 \mathcal E_T(F)={}&
 \sum_{(p,k)\in\mathcal P_T}c_{p,k}
       \|F-S_{k\log p}F\|_2^2\\
 &+\int_0^\infty w_\infty(r)\|F-S_rF\|_2^2\,dr,             \tag{2.3}
 \end{aligned}
\]

and `H_0=L_T-m_TI`.  In the parity normalization of D.50,

\[
 A_e=H_e+|u_e\rangle\langle u_e|,\qquad
 A_o=H_o-|u_o\rangle\langle u_o|,                            \tag{2.4}
\]

where `u_e=sqrt(2)cosh(t/2)` and `u_o=sqrt(2)sinh(t/2)`.

## 3. A closed formula for an explicit even level

Take

\[
 v_T(t)=(2T)^{-1/2}\mathbf1_{[-T,T]}(t).                     \tag{3.1}
\]

This is a unit even vector.  For `0<=a<=2T`, direct overlap of the two
intervals gives

\[
 \|v_T-S_av_T\|_2^2={a\over T}.                              \tag{3.2}
\]

Moreover

\[
 |\langle u_e,v_T\rangle|^2
 ={16\sinh^2(T/2)\over T},\qquad
 \|u_o\|_2^2=2\sinh T-2T.                                  \tag{3.3}
\]

Expand

\[
 w_\infty(r)=\sum_{j=0}^\infty e^{-b_jr},\qquad
 b_j=2j+\tfrac12.                                            \tag{3.4}
\]

Using (3.2) for `r<=2T` and the value `2` for `r>=2T`, one obtains

\[
 \begin{aligned}
 \mathcal E_{\infty,T}(v_T)
 &=\sum_{j=0}^\infty\left{
 {1-(1+2Tb_j)e^{-2Tb_j}\over Tb_j^2}
       +{2e^{-2Tb_j}\over b_j}\right}\\
 &=\sum_{j=0}^\infty{1-e^{-2Tb_j}\over Tb_j^2}.              \tag{3.5}
 \end{aligned}
\]

Therefore the fully explicit even Rayleigh level is

\[
 \boxed{
 \begin{aligned}
 E_T^{(0)}:=\langle v_T,A_ev_T\rangle
 ={}&\sum_{(p,k)\in\mathcal P_T}{\log p\over p^{k/2}}
       \left({k\log p\over T}-2\right)\\
 &+\sum_{j=0}^\infty{1-e^{-2T(2j+1/2)}
       \over T(2j+1/2)^2}
 -m_0+{16\sinh^2(T/2)\over T}.
 \end{aligned}}                                             \tag{3.6}
\]

Every prime power allowed by the support occurs exactly once.  In
particular, (3.6) is not a prime-only or first-power approximation.  By the
min--max principle,

\[
 \mu_e(T)\leq E_T^{(0)}.                                     \tag{3.7}
\]

The prolate vector of D.48 may give a sharper level, but (3.6) has the
advantage that no unproved approximation property enters its definition.

### Asymptotic audit of the polar jet

The last term of (3.6) is exponentially large:

\[
 {16\sinh^2(T/2)\over T}
 ={4e^T\over T}-{8\over T}+O(e^{-T}/T).                      \tag{3.8}
\]

It does not by itself make the trial level fail.  Partial summation with
the classical prime-number-theorem error gives for the complete prime-power
sum in (3.6)

\[
 \sum_{(p,k)\in\mathcal P_T}c_{p,k}
       \left({k\log p\over T}-2\right)
 =-{4e^T\over T}+O\!\left(e^Te^{-c\sqrt T}\right)+O(1)       \tag{3.9}
\]

for some `c>0`.  Thus the two `4e^T/T` terms cancel.  Also the Gamma series
in (3.6) is `O(1/T)`.  Unconditionally this yields only

\[
 E_T^{(0)}=O\!\left(e^Te^{-c\sqrt T}\right)+O(1),            \tag{3.10}
\]

which is far too weak to prove (4.1) or (4.3) and does not even force the
level to decay.  Numerical smallness of `E_T^(0)` on sampled windows is
therefore not an asymptotic theorem.  The leading polar growth is cancelled
arithmetically, but the remainder is exactly where finer prime information
enters.

## 4. The exact odd Green criterion at this level

Assume first that

\[
 E_T^{(0)}<\alpha_{o,0}(T):=\inf\mathrm{spec}\,H_o.       \tag{4.1}
\]

Define

\[
 m_{o,T}(E)=\langle u_o,(H_o-E)^{-1}u_o\rangle.              \tag{4.2}
\]

D.50 gives

\[
 \boxed{m_{o,T}(E_T^{(0)})<1
 \quad\Longrightarrow\quad
 \mu_e(T)\leq E_T^{(0)}<\mu_o(T).}                           \tag{4.3}
\]

This criterion sees persistent odd eigenvalues as well as secular roots.
It does not require cyclicity of `u_o`.

The variational identity

\[
 m_{o,T}(E)=sup_{0\ne F\in\mathcal H_o}
 { |\langle u_o,F\rangle|^2
  \over\langle F,(H_o-E)F\rangle}                            \tag{4.4}
\]

shows that (4.1)--(4.3) are equivalent to the following strict inequality
for every nonzero odd `F` in the form domain:

\[
 \boxed{
 \begin{aligned}
 &\sum_{(p,k)\in\mathcal P_T}{\log p\over p^{k/2}}
       \|F-S_{k\log p}F\|_2^2
 +\int_0^\infty w_\infty(r)\|F-S_rF\|_2^2\,dr\\
 &\quad>
 \left(2\sum_{(p,k)\in\mathcal P_T}{\log p\over p^{k/2}}
       +m_0+E_T^{(0)}\right)\|F\|_2^2
       +|\langle\sqrt2\sinh(t/2),F\rangle|^2.
 \end{aligned}}                                             \tag{4.5}
\]

Thus the missing estimate is a complete `p^k+Gamma` nonlocal Poincare
inequality with an explicit rank-one odd boundary term.

## 5. A norm-resolvent sufficient bound

Let

\[
 \delta_o(T,E)=\inf_{0\ne F\in\mathcal H_o}
 {\langle F,(H_o-E)F\rangle\over\|F\|_2^2}.                 \tag{5.1}
\]

Then

\[
 m_{o,T}(E)\leq{\|u_o\|_2^2\over\delta_o(T,E)}
 ={2\sinh T-2T\over\delta_o(T,E)}.                          \tag{5.2}
\]

Consequently the explicit coercive estimate

\[
 \boxed{
 \delta_o(T,E_T^{(0)})>2\sinh T-2T}                          \tag{5.3}
\]

is sufficient for (4.3).  It is stronger than necessary because it replaces
the spectral distribution of `u_o` by its full norm, but it is a clean
quantitative target.

The Markov estimate `L_T>=0` gives only

\[
 \delta_o(T,E_T^{(0)})\geq-m_T-E_T^{(0)},                    \tag{5.4}
\]

which is negative on the relevant windows and cannot imply (5.3).  Hence
positivity improving without a numerical spectral gap does no work here.

## 6. Why the complete prime kernel blocks a formal half-line proof

For an odd real function write `f=F|_(0,T)`.  If `0<a<=T`, its translation
correlation is

\[
 \langle F,S_aF\rangle
 =2\int_0^{T-a}f(x)f(x+a)\,dx
  -\int_0^a f(x)f(a-x)\,dx,                                 \tag{6.1}
\]

whereas for `T<a<=2T`,

\[
 \langle F,S_aF\rangle
 =-\int_{a-T}^{T}f(x)f(a-x)\,dx.                            \tag{6.2}
\]

The continuous Gamma density is positive and decreasing, so its odd
half-line kernel contains the favorable difference
`w_infty(|x-y|)-w_infty(x+y)`.  The complete finite-place kernel, however,
is the atomic measure

\[
 \nu_T=\sum_{(p,k)\in\mathcal P_T}c_{p,k}\,\delta_{k\log p}. \tag{6.3}
\]

It has no pointwise monotonicity under `|x-y| -> x+y`.  Equations
(6.1)--(6.2) therefore have no fixed sign for arbitrary odd `f`.  A
reflection-positivity or Sturm argument valid for the Gamma kernel alone
does not survive addition of all prime powers.

## 7. Fourier form of the same gate

On the real Fourier axis the Levy multiplier is

\[
 \ell_T(\tau)=2\sum_{(p,k)\in\mathcal P_T}c_{p,k}
       \bigl(1-\cos(\tau k\log p)\bigr)
 +\sum_{j=0}^\infty{1\over j+1/4}
 {\tau^2\over4(j+1/4)^2+\tau^2}.                            \tag{7.1}
\]

For odd `F`, `widehat F(0)=0`, but this single zero does not yield the
constant `m_T+E_T^(0)` in (4.5).  The required statement is a
Paley--Wiener uncertainty estimate for functions supported in `[-T,T]`,
with the two imaginary boundary evaluations encoded by the last term of
(4.5).  Dropping the oscillatory prime factor in (7.1), replacing it by its
average, or retaining only `p` instead of every `p^k` changes the required
constant and is not an admissible proof.

## 8. Circularity audit

Equation (4.5) is exactly positivity of the full CCM Weil form on the odd
sector above the explicit even trial level.  Therefore it cannot be proved
by citing positivity of the Weil form or by selecting a positive spectral
part; either move assumes the desired conclusion.

The logical status is more precise than simply “equivalent to RH”:

1. the primitive inequality of D.10/D.47 on every test is Weil's criterion
   and is equivalent to RH;
2. the odd ordering inequality (4.5) is a different, nonprimitive
   fixed-window spectral statement; no equivalence with RH alone is known;
3. (4.5) for all windows supplies the simple-even parity input only after
   a separate intra-even simplicity argument;
4. combined with the expanding-window determinant convergence of D.48, it
   would imply RH, because that convergence is itself RH-bearing.

Likewise, deriving decay of (3.6) by inserting a zero expansion for the
prime remainder would not prove anything unless every resulting off-line
term were controlled without assuming its absence.  The source formula
(3.6) is unconditional; a spectral sign estimate for its remainder is not.

Thus importing D.47 to prove (4.5) would be circular, while proving (4.5)
directly from the explicit kernel (2.3) would be a genuine new estimate.

## 9. Verdict and next estimate

The explicit choice (3.6) eliminates ambiguity about the comparison level.
The unresolved assertion is now the single Green bound

\[
 \boxed{
 \langle u_o,(H_o-E_T^{(0)})^{-1}u_o\rangle<1,}              \tag{9.1}
\]

together with `E_T^(0)<alpha_(o,0)`.  The complete-kernel form is (4.5).
Neither positivity improving, displacement rank, nor the Gamma
reflection inequality controls the atomic prime-power contribution tightly
enough to prove it.

A viable next attack is a certified lower bound for the smallest eigenvalue
of the odd Galerkin matrices using interval arithmetic, followed by a
uniform tail estimate from the Gamma multiplier.  Finite numerical checks
alone would not prove the all-window assertion, but this split would isolate
the finite arithmetic computation from the analytic tail.
