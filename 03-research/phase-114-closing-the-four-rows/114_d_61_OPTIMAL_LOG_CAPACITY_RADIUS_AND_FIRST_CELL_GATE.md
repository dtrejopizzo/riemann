# D.61 — Optimal logarithmic-capacity radius and the first-cell gate

## 1. Result

D.60 used the intentionally excessive choices `R=10^300` and
`h=10^-610`.  This note optimizes that argument.  It proves the larger
rational interval

\[
 \boxed{T_2\leq T\leq T_2+10^{-61}}                     \tag{1.1}
\]

with the explicit primitive bound

\[
 \boxed{QW_T(F,F)>6.7\,10^{-4}\|F\|_2^2.}               \tag{1.2}
\]

It also determines the exact limit of this particular capacity estimate:
its optimized posterior length is between `9.37*10^-61` and
`9.38*10^-61`.  Thus logarithmic capacity alone cannot cover a
macroscopic portion of the cell `(log2/2,log3/2)`; a parity--Feshbach
certificate is genuinely necessary.

## 2. Sharp elementary lower bound for the Gamma multiplier

For

\[
 \ell(R)=\sum_{j=0}^\infty {R^2\over
 (j+1/4)(4(j+1/4)^2+R^2)},                               \tag{2.1}
\]

the summand is decreasing as a function of `x=j+1/4`.  Therefore

\[
 \begin{aligned}
 \ell(R)&\geq\int_{1/4}^{\infty}
 {R^2\over x(4x^2+R^2)}\,dx\\
 &=\log2+{1\over2}\log(R^2+1/4)
 >\log(2R).                                               \tag{2.2}
 \end{aligned}
\]

This removes the factor-two loss in the coarse partial-sum estimate of
D.60.

## 3. The optimized two-parameter inequality

Let

\[
 D_0=5.41312,\quad c={\log2\over\sqrt2},\quad
 m_0<5.372184,\quad h=T-T_2.                             \tag{3.1}
\]

D.60 gives `L_(infty,T)>=D_0||F||^2` throughout every interval considered
here.  Its boundary-concentration argument, now using (2.2), gives

\[
 QW_T(F,F)>\Phi(h,R)\|F\|^2,                            \tag{3.2}
\]

where

\[
 \Phi(h,R)=D_0-m_0-{2cD_0\over\log(2R)}
                    -{8chR\over\pi}.                    \tag{3.3}
\]

All constants and the `p=2` contribution are present in (3.3).  No
operator-norm continuity of the entering shift is assumed.

For `h=10^-61`, choose the integer

\[
 R=2\,10^{57}.                                           \tag{3.4}
\]

The atanh series with rational remainder gives

\[
 \log(2R)=\log(4\,10^{57})>132.63364,
\]

and the standard rational enclosures

\[
 {693147\over10^6}<\log2<{693148\over10^6},\quad
 {1414213\over10^6}<\sqrt2,quad
 \pi>{3141592\over10^6}                                \tag{3.5}
\]

inserted with the adverse endpoint in every occurrence give

\[
 \Phi(10^{-61},2\,10^{57})>0.00067.                     \tag{3.6}
\]

This proves (1.1)--(1.2).

## 4. Exact optimum of the capacity method

Put

\[
 G=D_0-m_0,qquad A=2cD_0,qquad B={8c\over\pi},qquad
 L=\log(2R).                                              \tag{4.1}
\]

For fixed `h`, the loss in (3.3) is

\[
 {A\over L}+{Bh\over2}e^L.                              \tag{4.2}
\]

It is strictly convex at its critical point.  The critical equation and
the zero-margin equation are

\[
 {Bh\over2}e^L={A\over L^2},qquad
 G=A\left({1\over L}+{1\over L^2}\right).               \tag{4.3}
\]

The second equation has a unique positive solution `L_*`, and then

\[
 h_{cap}={\pi D_0\over2L_*^2}e^{-L_*}.                   \tag{4.4}
\]

Directed evaluation of (4.3), using (3.5) and the rational exponential
series, gives

\[
 130.6155<L_*<130.6157,                                  \tag{4.5}
\]

\[
 \boxed{9.37\,10^{-61}<h_{cap}<9.38\,10^{-61}.}          \tag{4.6}
\]

Thus (1.1) is within a factor ten of the largest clean decimal interval,
and (4.6) is the actual limit of the D.60 capacity inequality with the
fixed finite archimedean seed `D_0`.

## 5. Why a new interior certificate is unavoidable

The first cell has length

\[
 {\log3-\log2\over2}>0.20,                               \tag{5.1}
\]

whereas (4.6) is less than `10^-60`.  The discrepancy is structural.  A
function in the logarithmic Gamma form domain can concentrate in a boundary
interval of length `delta` at cost only of order `log(1/delta)`.  Therefore
the elementary absorption loses order `1/log(1/delta)`, forcing an
exponentially short startup interval when the endpoint gap is about `0.04`.

The next certificate must retain the exact `p=2` shift in the finite core,
not estimate it by absolute value.  A suitable interior point is

\[
 T_c={2\over5}.                                          \tag{5.2}
\]

At this point the exact parity matrices use only:

* the Gamma--Lerch entries of D.57;
* the single value of the explicit convolution table at `y=log2`;
* the even moment `cosh(t/2)` and odd moment `sinh(t/2)`;
* the D.55 high-sector residual.

Ordinary 100-mode floating diagnostics give positive full-form minima of
about `1.8*10^-4` (even) and `1.5*10^-2` (odd); after imposing the Tate
moments the margins are substantially larger.  These numbers are only
diagnostics and are not used as a proof.  The required next step is a
directed parity--Feshbach `LDL*` certificate at (5.2), followed by the D.57
interval engine both leftward and rightward.

## 6. Status

Closed:

* the optimally tuned logarithmic-capacity startup bound;
* an explicit improvement of D.60 by 549 decimal orders;
* the rigorous maximum reach of this method;
* proof that a macroscopic first-cell closure requires exact finite-core
  cancellation with `p=2`.

Not claimed here: closure of the entire first cell.  The precise remaining
finite datum is the directed interior Feshbach certificate at `T=2/5`.
