# 104_85 — Global renormalization of primes, Hurwitz, and non-local Nyman form

**Result.** After the local gate of `104_84`, there are two constructions
that genuinely preserve the global interaction of the primes.

1. There is an explicit sequence of entire, zero-free functions,
   built with all weights \(\Lambda(m)\le X\) and the continuous
   comparator, that converges to \((s-1)\zeta(s)\) up to \(\Re s=1\).
   Its locally uniform convergence on \(\Re s>1/2\) is **equivalent to RH**.
2. The Möbius approximation of Nyman--Báez-Duarte produces a non-local,
   positive Gram form with kernel \(1/\max(m,n)\). A single zero
   \(\rho=\beta+i\gamma\), \(\beta>1/2\), imposes on every residual a norm
   at least \((2\beta-1)/|\rho|^2\). Proving that this norm tends to zero is
   exactly eliminating the Blaschke factor of `104_84`.

Hence neither the global renormalization nor the quadratic energy lose the
obstruction: they localize it exactly. This document does not prove
Deep-\(\Lambda\), A1, or RH.

---

## 1. Renormalized global product

Set

\[
 E(x)=\psi(x)-x,
 \qquad
 G_X(s)=\sum_{m\le X}{\Lambda(m)\over m^s}
         -\int_1^Xx^{-s}\,dx.                            \tag{1}
\]

The second function is entire: the apparent singularity of the integral at
\(s=1\) is removable. Define

\[
 F_X(s)=\zeta(2)\exp\left\{-\int_2^sG_X(w)\,dw\right\}. \tag{2}
\]

The integral does not depend on the path because \(G_X\) is entire. Each
\(F_X\) is entire and never vanishes. Integrating the two terms of (1),

\[
\begin{aligned}
 F_X(s)=\zeta(2)\exp\Bigg\{&
 \sum_{m\le X}{\Lambda(m)\over\log m}
       (m^{-s}-m^{-2})\\
 &+\int_1^X{x^{-2}-x^{-s}\over\log x}\,dx\Bigg\},      \tag{3}
\end{aligned}

where the quotient at \(x=1\) is understood by continuity. The formula uses
simultaneously all prime powers up to \(X\); it is not a fixed local
change of Euler factors.

Stieltjes integration gives the exact identity

\[
 \boxed{
 G_X(s)=1+E(X)X^{-s}
        +s\int_1^XE(x)x^{-s-1}\,dx.}                    \tag{4}
\]

Indeed,

\[
 \sum_{m\le X}\Lambda(m)m^{-s}
 =\psi(X)X^{-s}+s\int_1^X\psi(x)x^{-s-1}\,dx,          \tag{5}
\]

and the part with \(\psi(x)=x\) minus the comparator of (1) is exactly
one.

## 2. Unconditionally reached half-plane

The effective Vinogradov--Korobov bound has the form

\[
 |E(x)|\le x\exp\{-\eta(\log x)\},
 \qquad
 \eta(u)\asymp u^{3/5}(\log u)^{-1/5}.                  \tag{6}
\]

By (4), the boundary term and the tail converge uniformly on compacta of
\(\Re s\ge1\). For \(\Re s>1\),

\[
 G_X(s)\longrightarrow
 -{\zeta'\over\zeta}(s)-{1\over s-1}
 =-{d\over ds}\log\{(s-1)\zeta(s)\}.                  \tag{7}
\]

The normalization \(F_X(2)=\zeta(2)=(2-1)\zeta(2)\) proves

\[
 F_X(s)\longrightarrow (s-1)\zeta(s)                  \tag{8}
\]

locally uniformly on the certified half-plane.

VK does not deliver any \(\Re s>1-\delta\), \(\delta>0\) fixed. Indeed, the
majorant resulting from (4) contains

\[
 \int^\infty
 \exp\{\delta u-\eta(u)\}\,du=\infty,                 \tag{9}
\]

and the boundary term is
\(\exp\{\delta\log X-\eta(\log X)\}\), which also does not tend to zero.
Changing the constants of (6) does not alter this exponent barrier.

## 3. Hurwitz equivalence

We have

\[
 \boxed{
 F_X\longrightarrow(s-1)\zeta(s)
 \text{ locally uniformly on }\Re s>{1\over2}
 \quad\Longleftrightarrow\quad \mathrm{RH}.}           \tag{10}
\]

If the convergence holds, Hurwitz's theorem and the fact that each
\(F_X\) is zero-free imply that \((s-1)\zeta(s)\) is zero-free on that
half-plane. The functional symmetry gives RH.

Conversely, RH implies the von Koch bound

\[
 E(x)=O(x^{1/2}\log^2x),                                \tag{11}
\]

and (4) converges uniformly on every compact subset of \(\Re s>1/2\), which
proves (10).

The failure is quantitatively visible. If \(\rho\) is a right-hand zero and
the circle \(|s-\rho|=r\) contains no other zeros, then for all
\(X\)

\[
 \boxed{
 \sup_{|s-\rho|=r}|F_X(s)-(s-1)\zeta(s)|
 \ge \min_{|s-\rho|=r}|(s-1)\zeta(s)|>0.}              \tag{12}
\]

Otherwise, Rouché's theorem would force the zero-free function \(F_X\) to
have a zero inside the circle. A mode \(E_\rho(x)\asymp x^\rho\) produces
the same obstruction in (4) through a term
\(X^{\rho-s}/(s-\rho)\).

## 4. Non-local Nyman residual

Define

\[
 g_N=\sum_{k\le N}{\mu(k)\over k},
 \qquad
 A_N(s)=\sum_{k\le N}{\mu(k)\over k^s}
          -Ng_NN^{-s}.                                  \tag{13}
\]

Then \(A_N(1)=0\), which cancels the pole of \(\zeta\), and the residual

\[
 f_N(s)={1-\zeta(s)A_N(s)\over s}                       \tag{14}
\]

has Hardy norm

\[
 d_N^2={1\over2\pi}\int_{-\infty}^{\infty}
 { |1-\zeta(\tfrac12+it)A_N(\tfrac12+it)|^2
  \over t^2+1/4}\,dt.                                  \tag{15}
\]

In the Mellin coordinate, if a finite residual is written as
\(\sum_m r_mm^{-s}\), Plancherel gives the exact form

\[
 \boxed{
 \left\|\sum_mr_mm^{-s}/s\right\|_2^2
 =\sum_{m,n}{r_m\overline{r_n}\over\max(m,n)}.}        \tag{16}
\]

The kernel preserves all interactions and is PSD because

\[
 {1\over\max(m,n)}
 =\int_0^1
 \mathbf1_{\{x\le1/m\}}\mathbf1_{\{x\le1/n\}}\,dx.  \tag{17}
\]

## 5. A zero imposes a positive distance

If \(\rho=\beta+i\gamma\), \(\beta>1/2\), is a zero of \(\zeta\), then
for **every** multiplier \(A_N\)

\[
 f_N(\rho)={1\over\rho}.                                \tag{18}
\]

The evaluation inequality in
\(H^2(\Re s>1/2)\) gives

\[
 |f_N(\rho)|^2\le {d_N^2\over2\beta-1}.
\]

Hence

\[
 \boxed{d_N^2\ge{2\beta-1\over|\rho|^2}>0}            \tag{19}
\]

for any choice of weights, not only (13). On the disk,
\((2\beta-1)/|\rho|^2=1-|w_\rho|^2\), exactly the defect of an elementary
Blaschke factor.

Set, on the disk,

\[
 \mathcal G(z)=z\,\zeta\!\left({1\over1-z}\right),
 \qquad \mathcal G(0)=1.                                \tag{20}
\]

This function belongs to \(H^2(\mathbb D)\) and has the same inner
factor \(B\) as `104_84`; the factors that distinguish it from \(E\) are
outer. In the canonical Hardy normalization, the closure of all
outer multipliers satisfies

\[
 \inf_P\|1-\mathcal G P\|_2^2=1-|B(0)|^2.              \tag{21}
\]

where \(B\) is the inner factor of `104_84`. Thus

\[
 d_N\longrightarrow0
 \quad\Longleftrightarrow\quad B\equiv1
 \quad\Longleftrightarrow\quad\mathrm{RH}.             \tag{22}
\]

The positivity of (16) does not give an upper bound tending to zero. The
Möbius weights are the canonical arithmetic candidate, but proving (22) is
precisely the Nyman--Beurling/Báez-Duarte criterion.

## 6. Decision

```text
proved:
  all-primes zero-free renormalization (1)--(4);
  its convergence up to Re s=1 by VK;
  convergence up to Re s>1/2 iff RH;
  Nyman residual and exact non-local Gram form;
  every right-hand zero imposes the positive distance (19).

ruled out:
  PNT/VK + renormalized partial product + Hurwitz => RH;
  positivity of the Gram form, without a new upper bound => RH.

not proved:
  the convergence of (10), d_N->0, B(0)=1, Deep-Lambda, A1, or RH.
```
