# 106.28 — Hurwitz power sums and the co-Poisson floor-remainder gate

## Purpose

Document 106.26 isolates a sufficient two-orientation Mellin estimate for
the parity-corrected diagonal.  This note tests a direct route to that
estimate:

1. interchange the co-Poisson sum and the Mellin integral;
2. write the resulting partial power sum by Hurwitz zeta;
3. use \(\zeta(\rho)=\zeta(1-\rho)=0\) before estimating;
4. test whether the periodic Bernoulli remainder is controlled by the
   unconditional endpoint and exterior \(H^1\) estimates of 106.24.

The first three steps give exact new identities and an \(O(d_4)\) leading
moment.  The fourth step does not follow from the available estimates.  A
fixed-order Euler--Maclaurin bound grows polynomially in the zero ordinate,
while the first periodic Bernoulli term has no ordinate decay at all.  The
two pieces must be kept together.  Their joint cancellation is stated
exactly in (24) below.

This note therefore advances the diagonal reduction, but does not prove the
Fuchs--Mellin estimate or RH.

## 1. Semantic nonduplication audit

The repository contains many uses of Hurwitz's theorem and several
Euler--Maclaurin remainder certificates.  The closest named predecessor is
104.85.  It constructs zero-free all-prime approximants and applies
**Hurwitz's convergence theorem**; it does not use the Hurwitz zeta function
to expand a co-Poisson partial power sum.  Its obstruction is convergence to
the critical half-plane.

The periodic-Bernoulli lemmas E73.214 and E73.229 concern the digamma
expansion in a fixed right-half-plane sector.  Their arguments rely on a
uniform lower bound for the real part of the argument.  They do not address
the present regime, where the order of the Hurwitz zeta function is
\(1/2-w\) and \(|\Im w|\) is unbounded while its second argument starts at
one.

No previous document contains equations (5), (9), or (15) below.  The route
is therefore not a duplicate of 104.85.  Its failure under termwise bounds
is, however, consistent with the multiplicative-dilation obstruction proved
in 106.24(39)--(42).

## 2. Exact partial-power-sum identity

Keep the notation of 106.26:

\[
 \ell_\lambda=(1-P_\lambda)\widehat f_\lambda^{(0)},
 \qquad
 A_\lambda(w)=\int_\lambda^\infty
  \mathcal E(\ell_\lambda)(v)v^{-w}\,d^*v.
 \tag{1}
\]

For \(x\ge1\), put

\[
 S_w(x)=\sum_{1\le n\le x}n^{w-1/2}.
 \tag{2}
\]

### Theorem 1 — Exact co-Poisson/Hurwitz transform

On the strip \(|\Re w|<1/2\), with the same symmetric/improper convention
as the co-Poisson transform in 106.12,

\[
 \boxed{
 A_\lambda(w)=
 \int_\lambda^\infty
  \ell_\lambda(t)t^{-w-1/2}
  S_w(t/\lambda)\,dt.}
 \tag{3}
\]

Moreover,

\[
 \boxed{
 S_w(x)=
 \zeta\!\left(\frac12-w\right)
 -\zeta\!\left(\frac12-w,\lfloor x\rfloor+1\right).}
 \tag{4}
\]

Consequently, if \(w=\rho-1/2\), then

\[
 \boxed{
 S_w(x)=-\zeta(1-\rho,\lfloor x\rfloor+1),
 \qquad
 S_{-w}(x)=-\zeta(\rho,\lfloor x\rfloor+1).}
 \tag{5}
\]

Thus both constant Hurwitz terms vanish before any absolute value is taken.

#### Proof

First truncate the co-Poisson sum at \(n\le M\).  The substitution
\(t=nv\) gives

\[
\begin{aligned}
 A_{\lambda,M}(w)
 &=\sum_{n\le M}n^{w-1/2}
   \int_{n\lambda}^\infty
   \ell_\lambda(t)t^{-w-1/2}\,dt\\
 &=\int_\lambda^\infty
   \ell_\lambda(t)t^{-w-1/2}
   \sum_{n\le\min(M,t/\lambda)}n^{w-1/2}\,dt.
\end{aligned}
\tag{6}
\]

Pass to the same symmetric/improper limit which defines
\(\mathcal E(\ell_\lambda)\).  On the right of (3), this means the limit of
the kernels
\(\sum_{n\leq\min(M,t/\lambda)}n^{w-1/2}\) occurring in (6), not an
unjustified absolute interchange.  The Poisson identity and the BV bound of
106.12 give convergence on the left on compact substrips.  On the right,
the only non-absolutely-integrable asymptotic term is a constant multiple
of \(\ell_\lambda(t)\).  Its improper integral converges by Fourier
inversion and \(f_\lambda^{(0)}(0)=0\); all remaining terms are controlled
by Cauchy--Schwarz with a factor \(t^{-1}\).  Thus the limit of (6) is the
improper integral in (3).
Equation (4) is the defining finite-tail identity for Hurwitz zeta.  At
\(w=\rho-1/2\), its two constants are respectively
\(\zeta(1-\rho)\) and \(\zeta(\rho)\), which proves (5). \(\square\)

## 3. Exact first Bernoulli decomposition

Define the centered periodic Bernoulli function

\[
 P_1(x)=\frac12-\{x\},
 \qquad |P_1(x)|\le\frac12.
 \tag{7}
\]

Euler summation gives, for \(-1/2<\Re w<1/2\),

\[
\begin{aligned}
 S_w(x)={}&
 \frac{x^{w+1/2}}{w+1/2}
 +\zeta\!\left(\frac12-w\right)
 +P_1(x)x^{w-1/2}
 +\mathcal B_w(x),\\
 \mathcal B_w(x)={}&
 -\left(w-\frac12\right)
 \int_x^\infty P_1(y)y^{w-3/2}\,dy.
\end{aligned}
\tag{8}
\]

At \(w=\rho-1/2\), insert (8) into (3) and define

\[
 M_{0,\lambda}=\int_\lambda^\infty\ell_\lambda(t)\,dt,
 \qquad
 I_{1,\lambda}=\int_\lambda^\infty
  \ell_\lambda(t)P_1(t/\lambda)\frac{dt}{t},
 \tag{9}
\]

and

\[
 J_\lambda(w)=\int_\lambda^\infty
 \ell_\lambda(t)t^{-w-1/2}
 \mathcal B_w(t/\lambda)\,dt.
 \tag{10}
\]

Then the zero cancellation in (5) gives the exact formulas

\[
 \boxed{
 A_\lambda(w)=
 \frac{\lambda^{-w-1/2}}{w+1/2}M_{0,\lambda}
 +\lambda^{1/2-w}I_{1,\lambda}
 +J_\lambda(w),}
 \tag{11}
\]

and

\[
 \boxed{
 A_\lambda(-w)=
 \frac{\lambda^{w-1/2}}{1/2-w}M_{0,\lambda}
 +\lambda^{1/2+w}I_{1,\lambda}
 +J_\lambda(-w).}
 \tag{12}
\]

The identities are understood by continuation from compact substrips.  In
particular,

\[
\begin{aligned}
 A_\lambda(w)+A_\lambda(-w)
 ={}&M_{0,\lambda}
 \left(
  \frac{\lambda^{-w-1/2}}{w+1/2}
 +\frac{\lambda^{w-1/2}}{1/2-w}
 \right)\\
 &+2\lambda^{1/2}\cosh(w\log\lambda)I_{1,\lambda}
 +J_\lambda(w)+J_\lambda(-w).
\end{aligned}
\tag{13}
\]

Equation (13) is the exact output of the proposed Hurwitz route.

## 4. The parts which are controlled

For a normalized prolate mode \(\psi_j\), Fourier inversion and the
compressed-Fourier identity give

\[
\begin{aligned}
 \int_{|t|>\lambda}\widehat\psi_j(t)\,dt
 &=\psi_j(0)
   -\chi_j\int_{-\lambda}^{\lambda}\psi_j(t)\,dt\\
 &=\psi_j(0)(1-\chi_j^2)
 =a_jd_j.
\end{aligned}
\tag{14}
\]

The leakage is even.  The size of this moment can be computed more sharply
than an \(O(d_4)\) bound.  Put

\[
 q_j=1-\chi_j,
 \qquad d_j=1-\chi_j^2=q_j(2-q_j),
 \tag{15a}
\]

and use the coefficient coordinates \(x_j=a_jc_j\).  On the modes
\(0,4,8\), the two exact moment constraints are

\[
 \sum_jx_j=0,
 \qquad \sum_jq_jx_j=0.
 \tag{15b}
\]

Take the raw constrained vector

\[
 \widetilde x
 =(q_4-q_8,\ q_8-q_0,\ q_0-q_4)
 \tag{15c}
\]

and write

\[
 c_j=\mathcal N_\lambda\frac{\widetilde x_j}{a_j},
 \qquad
 \mathcal N_\lambda^{-2}
 =\sum_{j\in\{0,4,8\}}
   \frac{|\widetilde x_j|^2}{|a_j|^2}.
 \tag{15d}
\]

Thus \(\sum|c_j|^2=1\).  Since the fixed-mode values \(|a_j|\) are
bounded above and away from zero and
\(q_0\ll q_4\ll q_8\), one has
\(\mathcal N_\lambda\asymp q_8^{-1}\).  Equations (14)--(15b) now give
the exact Vandermonde identity

\[
 \boxed{
 M_{0,\lambda}
 =\frac{\mathcal N_\lambda}{2}
   (q_4-q_0)(q_8-q_4)(q_8-q_0)
 \asymp q_4q_8
 \asymp d_4d_8.}
 \tag{15}
\]

Indeed, \(\sum q_jx_j=0\) implies

\[
 \frac12\sum_jd_jx_j
 =-\frac12\sum_jq_j^2x_j,
 \qquad
 -\sum_jq_j^2\widetilde x_j
 =(q_4-q_0)(q_8-q_4)(q_8-q_0).
 \tag{15e}
\]

Thus the leading Hurwitz integral term is not merely first-order-small: it
is the product of the fourth- and eighth-mode angle-defect scales.

There is also an exact zero-moment refinement.  On the four modes
\(J=\{0,4,8,12\}\), set

\[
 \widetilde x_j^{[4]}
 =\frac1{\displaystyle\prod_{k\in J,\ k\ne j}(q_j-q_k)},
 \qquad
 c_j^{[4]}=\mathcal N_\lambda^{[4]}
              \frac{\widetilde x_j^{[4]}}{a_j},
 \tag{15f}
\]

where \(\mathcal N_\lambda^{[4]}\) normalizes the coefficient vector.
The barycentric/Vandermonde identities give

\[
 \sum_{j\in J}q_j^r\widetilde x_j^{[4]}=0,
 \qquad r=0,1,2.
 \tag{15g}
\]

The first two rows are exactly \(f(0)=0\) and \(\int f=0\).  Since
\(\chi_j^2=1-2q_j+q_j^2\), the third row is equivalently
\(\sum_j\chi_j^2x_j=0\).  Hence (14) gives

\[
 \boxed{M_{0,\lambda}^{[4]}=0\quad\hbox{exactly}.}
 \tag{15h}
\]

This extra constraint does not inflate the leakage scale.  The hierarchy
\(q_0\ll q_4\ll q_8\ll q_{12}\) gives

\[
 \left|\frac{\widetilde x_0^{[4]}}
                 {\widetilde x_4^{[4]}}\right|\asymp1,
 \quad
 \left|\frac{\widetilde x_8^{[4]}}
                 {\widetilde x_4^{[4]}}\right|
 \asymp\frac{q_4}{q_8},
 \quad
 \left|\frac{\widetilde x_{12}^{[4]}}
                 {\widetilde x_4^{[4]}}\right|
 \asymp\frac{q_4q_8}{q_{12}^2}.
 \tag{15i}
\]

After normalization, modes \(0\) and \(4\) therefore remain of constant
size, while the higher modes are suppressed, and

\[
 \boxed{
 \sum_{j\in J}d_j|c_j^{[4]}|^2\asymp d_4.}
 \tag{15j}
\]

Thus one may eliminate the complete leading moment in (13) without losing
the exponentially small prolate leakage.  This does **not** control the
periodic term or its joint remainder.  Document 106.29 independently
rederives (15)--(15j) directly from the exterior \(\chi_j^2\)-mass identity.

The first periodic moment is bounded by the angle identity alone:

\[
 \boxed{
 |I_{1,\lambda}|
 \le\frac12\|\ell_\lambda\|_2
       \left(\int_\lambda^\infty t^{-2}\,dt\right)^{1/2}
 \ll\lambda^{-1/2}\sqrt{d_4}.}
 \tag{16}
\]

The first line of (13) has ordinate decay \(O((1+|\Im w|)^{-1})\)
and an exponentially small coefficient.  It satisfies the qualitative
carrier condition of 106.26 for every \(q\le1\).

The second line does not admit such a termwise conclusion.  Uniformly for
\(|\Re w|<1/2\), (16) gives only

\[
 \left|2\lambda^{1/2}\cosh(w\log\lambda)I_{1,\lambda}\right|
 \ll\lambda^{1/2}\sqrt{d_4},
 \tag{17}
\]

with no decay as \(|\Im w|\to\infty\).  Therefore this term must cancel
against \(J_\lambda(w)+J_\lambda(-w)\).

## 5. Why the standard Bernoulli remainder estimate does not close the gate

From (8), if \(\sigma=\Re w<1/2\),

\[
 \boxed{
 |\mathcal B_w(x)|
 \le
 \frac{|w-1/2|}{2(1/2-\sigma)}x^{\sigma-1/2}.}
 \tag{18}
\]

Using \(\|\ell_\lambda\|_2^2\asymp d_4\), this yields only

\[
 \boxed{
 |J_\lambda(w)|
 \ll
 \frac{1+|w|}{1-2\sigma}
 \lambda^{-\sigma}\sqrt{d_4}.}
 \tag{19}
\]

The corresponding estimate for \(J_\lambda(-w)\) has
\(\lambda^\sigma\).  Hence the standard first-remainder bound grows like
\(1+|\Im w|\); it has the opposite ordinate behavior from the carrier
condition.

Taking more Euler--Maclaurin terms does not repair this uniformly.  The
order-(2K) periodic remainder contains the rising factorial

\[
 \left(\frac12-w\right)_{2K},
 \tag{20}
\]

and its absolute bound is of size

\[
 O_K\!\left((1+|\Im w|)^{2K}
 x^{\sigma-1/2-2K}\right).
 \tag{21}
\]

For \(x\gg|\Im w|\), (21) is useful.  But the integral in (3) begins at
\(x=t/\lambda=1\).  On that lower region the Euler--Maclaurin expansion is
not uniform in the order of the Hurwitz zeta function.  Increasing \(K\)
there makes the absolute estimate worse.

The same obstruction is visible directly from the floor.  Distributionally,

\[
 dS_w(x)=\sum_{n\ge1}n^{w-1/2}\delta_n(dx).
 \tag{22}
\]

At a jump, the Mellin factor cancels its entire ordinate phase:

\[
 n^{-w-1/2}\,n^{w-1/2}=\frac1n.
 \tag{23}
\]

Thus integration by parts does not produce an oscillatory Dirichlet factor
in \(n\); it produces the literal boundary lattice
\(\sum_n\ell_\lambda(n\lambda)/n\).  The additive (H^1) theorem gives a
polynomial-size sampling bound for this lattice, but 106.24(39)--(42)
proves that the global dilation derivative has infinite norm because of the
nonzero endpoint carrier.  The boundary term at infinity therefore cannot
be discarded in a global multiplicative integration by parts.

Equations (18)--(23) show that the floor remainder cannot be estimated
separately.  Doing so discards exactly the cancellation being sought.

## 6. The sharpened remaining theorem

Write \(w_\rho=\rho-1/2=\sigma_\rho+i\gamma_\rho\).  Choose any fixed
\(1/2<q\le1\) and \(m\ge0\).  By (13)--(17), the Hurwitz route closes the
qualitative diagonal gate of 106.26 if one proves the following estimate
on the actual divisor:

\[
\boxed{
\begin{aligned}
 &\sup_{\rho}
 (1+|\gamma_\rho|)^q(1-2|\sigma_\rho|)^m\\
 &\quad\times
 \left|
  2\lambda^{1/2}\cosh(w_\rho\log\lambda)
       I_{1,\lambda}
  +J_\lambda(w_\rho)
  +J_\lambda(-w_\rho)
 \right|
 \longrightarrow0.
\end{aligned}}
\tag{24}
\]

This divisor-only formulation is materially narrower than the full-strip
seminorm of 106.26.  It is also the logically correct endpoint of the
Hurwitz calculation: equations (11)--(13) use both
\(\zeta(\rho)=0\) and \(\zeta(1-\rho)=0\), so their reduced right-hand side
is not an identity at arbitrary points of the strip.  The proof of 106.26,
Theorem 2, applies verbatim to a supremum over the divisor, since its only
subsequent inputs are the bilateral Vinogradov--Korobov region and local
zero density.  The \(M_{0,\lambda}\) line in (13) already obeys this
divisor carrier bound for every \(q\leq1\).

This is a strict sharpening of the unspecified transfer in 106.24: the
constant zeta terms are gone, the three-mode leading exterior moment is
\(\asymp d_4d_8\), and the optional four-mode vector makes that moment
exactly zero.  Only the joint periodic-floor cancellation remains.

The available PSWF input is sufficient for every scale appearing outside
the absolute value in (24): endpoint values, endpoint slopes, additive
exterior \(H^1\), and \(L^2\) angle leakage are all unconditional.  It does
not control the signed cancellation inside (24).  A proof needs a uniform
oscillatory estimate for the exterior prolate solution paired with the
complete periodic Bernoulli remainder.  Neither fixed-order
Euler--Maclaurin nor a multiplicative Sobolev norm supplies it.

## 7. Verdict

\[
\begin{array}{c|c}
\text{statement}&\text{status}\\ \hline
\text{co-Poisson partial-power-sum identity (3)}
 &\text{proved exactly}\\
\text{two Hurwitz constants vanish at every zero (5)}
 &\text{proved exactly}\\
M_{0,\lambda}\asymp d_4d_8\text{ on three modes}
 &\text{proved exactly}\\
M_{0,\lambda}^{[4]}=0,\quad
 \|(1-P_\lambda)\widehat f_\lambda^{[4]}\|_2^2\asymp d_4
 &\text{proved exactly}\\
\text{fixed-order Bernoulli remainder}\Rightarrow\text{FM}
 &\text{false as a termwise estimate}\\
\text{joint floor cancellation (24)}
 &\text{open}.
\end{array}
\tag{25}
\]

The Hurwitz expansion does not close the diagonal theorem, but it reduces
its uncontrolled part to the divisor-only estimate (24).  No statement
here proves the diagonal Rayleigh limit, the cross residual, the
complementary inertia estimate, or RH.
