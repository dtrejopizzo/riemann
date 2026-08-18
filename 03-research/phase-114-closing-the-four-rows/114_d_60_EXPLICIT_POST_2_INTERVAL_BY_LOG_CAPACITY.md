# D.60 — An explicit interval after the first prime threshold

## 1. Purpose and result

D.59 proves a coercive primitive gap at

\[
 T_2={\log2\over2}.
\]

The entering `p=2` translation is not small in operator norm, even when the
overlap of the two translated windows is arbitrarily short.  This note
controls it instead by the logarithmic Gamma energy.  The resulting interval
is deliberately tiny, but completely explicit:

\[
 \boxed{
 QW_T(F,F)>0.02524\,\|F\|_2^2
 \quad (F\in\ker M_+(T)\cap\ker M_-(T))
 }
 \tag{1.1}
\]

for

\[
 \boxed{
 T_2\leq T\leq T_2+10^{-610}.}
 \tag{1.2}
\]

Thus the first prime-power hinge is crossed on a nonempty right-hand
interval.  No RH, zero location, screw positivity or floating eigenvalue is
used.

## 2. Audit of the D.59 endpoint seed

The identities used in D.59 have the following independent checks.

1. From
   \[
   {e^{-r/2}\over1-e^{-2r}}=\sum_{j\geq0}e^{-(2j+1/2)r}
   \]
   and Tonelli,
   \[
   L_{\infty,T}=\sum_{j\geq0}\mathcal E_{2j+1/2}.
   \]
2. The identity
   \[
   \mathcal E_b(F)={2\over b}\|F\|^2-
   \iint_{[-T,T]^2}e^{-b|x-y|}F(y)\overline{F(x)}\,dy\,dx
   \]
   has the factor two required by the two half-lines `r>0` and `r<0`.
3. Differentiating the exponential kernel gives the Robin conditions
   `f'(-T)=bf(-T)` and `f'(T)=-bf(T)`.  Hence the odd equation is
   `x cot x=-bT`, while the even equation is `x tan x=bT`, on exactly the
   branches stated in D.59.
4. Directed bisection of these branches reproduces
   \[
   \sum_{j=0}^{19}d_{j,o}>5.41313,
   \qquad
   \sum_{j=0}^{4}d_{j,e}>5.45749,
   \]
   and
   \[
   m_0<5.372184.
   \]

In particular, the weaker common endpoint margin `0.0409` used below is
valid.  No correction to D.59 is needed.

## 3. A uniform archimedean lower bound

For variable `T`, retain the finite lower bounds from D.59 and write

\[
 D_o(T)=\sum_{j=0}^{19}d_{j,o}(T),\qquad
 D_e(T)=\sum_{j=0}^{4}d_{j,e}(T).                         \tag{3.1}
\]

The same max--min argument, now at `T`, gives

\[
 L_{\infty,T}(F,F)\geq D_o(T)\|F\|^2                    \tag{3.2}
\]

in the odd channel and

\[
 L_{\infty,T}(F,F)\geq D_e(T)\|F\|^2                    \tag{3.3}
\]

in the even channel satisfying the current Tate condition
`<F,cosh(t/2)>=0`.

All roots in (3.1) remain on the branches of D.59 for
`0.34<=T<=0.35`.  Implicit differentiation of

\[
 x\cot x=-bT,\qquad x\tan x=bT                           \tag{3.4}
\]

gives completely elementary (deliberately coarse) bounds

\[
 |D_o'(T)|<10^5,\qquad |D_e'(T)|<10^8
 \quad(0.34\leq T\leq0.35).                              \tag{3.5}
\]

Here are sufficient details for (3.5).  On the odd branch,

\[
 \left|{d\over dx}(x\cot x)\right|
 ={x-\sin x\cos x\over\sin^2x}>1,
\]

so `|x'|<b`.  On the first even branch the equation itself gives
`x>1/10` (for `x<=1/10`, the Taylor bound for `tan x` gives
`x tan x<1/50<bT`), and hence

\[
 {d\over dx}(x\tan x)=\tan x+x\sec^2x>x>1/10.
\]

On the second even branch the same derivative is larger than `x>3`.
Thus `|x'|<10b` on the first even branch and `|x'|<b/3` on the second.
Using `1/T<3`, `1/T^2<9`, `pi<22/7`, and `b<=77/2` in the odd sum and
`b<=17/2` in the even sum bounds all derivatives of `mu=x/T` by `400`.
Differentiating

\[
 {2b\over b^2+\mu^2},\quad
 T+{\sin(2\mu T)\over2\mu},\quad
 T+\sinh T,
\]

and D.59(5.5), and using `|sin|,|cos|<=1`, `cosh(.35)<2`,
`sinh(.35)<1`, `mu^2+1/4>=1/4`, gives respectively the safe totals
`10^5` and `10^8` in (3.5).  Every denominator in the normalized overlap
is bounded away from zero because both squared norms are at least `T>0.34`.
These inequalities use only rational bounds (the displayed decimal
endpoints may be replaced by `17/50` and `7/20`).  The accompanying
verifier evaluates the sharper endpoint values as an independent check.

Since `10^8*10^-610<10^-6`, D.59 and (3.5) imply, throughout (1.2),

\[
 \boxed{D_o(T)>5.41312,\qquad D_e(T)>5.41312.}            \tag{3.6}
\]

Consequently, on either primitive parity channel,

\[
 L_{\infty,T}(F,F)>5.41312\|F\|^2.                       \tag{3.7}
\]

## 4. Logarithmic capacity of the entering overlap

Put

\[
 a=\log2,\qquad c={\log2\over\sqrt2},\qquad
 \delta=2T-a.
\]

For `T` in (1.2), `0<=delta<=2*10^-610`.  The correlation
`<F,S_aF>` uses two boundary intervals, each of length `delta`.  If `E` is
their union, Cauchy--Schwarz gives

\[
 |\langle F,S_aF\rangle|\leq{1\over2}\|1_EF\|_2^2.       \tag{4.1}
\]

Let `Pi_R` be the full-line Fourier projection to `[-R,R]`.  With the
Plancherel convention of D.55,

\[
 |\Pi_RF(x)|^2\leq{R\over\pi}\|F\|_2^2.
\]

Splitting `F=Pi_RF+(1-Pi_R)F`, using `|E|=2delta`, and then (4.1), yields

\[
 |\langle F,S_aF\rangle|
 \leq {2\delta R\over\pi}\|F\|_2^2
      +\|(1-\Pi_R)F\|_2^2.                              \tag{4.2}
\]

The Gamma energy has multiplier

\[
 \ell(\tau)=\sum_{j=0}^\infty {1\over j+1/4}
 {\tau^2\over4(j+1/4)^2+\tau^2},                         \tag{4.3}
\]

which is increasing for positive `tau`.  Therefore

\[
 \|(1-\Pi_R)F\|_2^2
 \leq {L_{\infty,T}(F,F)\over\ell(R)}.                  \tag{4.4}
\]

Choose the integer

\[
 R=10^{300}.
\]

For `0<=j<=R/2-1`, the fraction in (4.3) is at least `1/2`.  Integral
comparison gives

\[
 \ell(R)\geq {1\over2}\log(2R+1)
 >{1\over2}\log R=150\log10>345.                        \tag{4.5}
\]

The last strict inequality follows, for example, from the atanh series of
D.57, which gives `log 10>23/10` by rational arithmetic.

## 5. Absorption of the `p=2` hinge

There is no other prime-power term before `T=log(3)/2`.  On the primitive
space the polar block vanishes, so

\[
 QW_T(F,F)=L_{\infty,T}(F,F)-m_0\|F\|^2
 -2c\,\operatorname{Re}\langle F,S_aF\rangle.           \tag{5.1}
\]

Combining (4.2)--(4.5), and using `c<1/2`, gives

\[
 QW_T(F,F)
 >\left(1-{1\over345}\right)L_{\infty,T}(F,F)
 -\left(m_0+{4\delta R\over\pi}\right)\|F\|^2.         \tag{5.2}
\]

Here

\[
 {4\delta R\over\pi}
 <{8\over3}10^{-310}.                                   \tag{5.3}
\]

Using (3.7), `m_0<5.372184`, and exact rational arithmetic,

\[
 {344\over345}(5.41312)-5.372184
 ={43549\over1725000}>0.025245.                          \tag{5.4}
\]

Equations (5.2)--(5.4) prove (1.1), with room to replace the final constant
by `0.02524`.

## 6. What has been closed

The endpoint seed of D.59 has now been propagated across the first hinge:

* the `p=2` term is included with its correct sign;
* its lack of operator-norm continuity is not hidden;
* the boundary concentration is absorbed by the logarithmic Gamma energy;
* a rational, nonzero posterior length is stated explicitly.

The size `10^-610` is not intended to be efficient.  Optimizing `R`, using
the parity Feshbach core, or replacing the elementary Fourier split by a
sharp logarithmic-capacity estimate would enlarge it substantially.  The
next global task is propagation across the rest of the cell
`(log2/2,log3/2)` and then through successive prime-power thresholds.
