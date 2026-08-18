# Theta hazard-convexity gate

## Question and verdict

For the positive theta kernel \(\Phi\), put
\[
 h(u)=-(\log\Phi)'(u).
\]
The proposed strengthening of `103_34` is
\[
 \boxed{\qquad h''(u)=-(\log\Phi)'''(u)>0\qquad(u>0).\qquad}     \tag{1}
\]

The property is proved below on the explicit outer interval
\(u\ge1/4\).  Near the modular fixed point, \(0<u<1/4\), dominance of the
first theta summand cannot prove it: at \(u=0\) that summand has the wrong
third-derivative sign, and the zero forced by evenness is produced by a
sharp cancellation with the \(m=2\) summand.  A uniform Taylor/interval
certificate for this compact modular interval has not been supplied.

Thus (1) is neither claimed nor falsified globally.  The note isolates the
exact compact verification still required and shows that, even if (1) is
completed, convexity of \(h\) does not by itself give the five-tilt
comparison of the covariances \(\Gamma_p\) needed by the cubic gate.

## 1. Exact third log-sum identity

Use the notation of `103_34`:
\[
 x=\pi e^{2u},\qquad
 f_m=\pi m^2e^{5u/2}(2m^2x-3)e^{-m^2x},
 \qquad \ell_m=\log f_m,                                      \tag{2}
\]
and \(w_m=f_m/\sum_jf_j\).  Direct differentiation gives
\[
 \ell_m'={5\over2}+{4y\over2y-3}-2y,                            \tag{3}
\]
\[
 \ell_m''=-4y-{24y\over(2y-3)^2},                              \tag{4}
\]
\[
 \ell_m'''=-8y+{48y(2y+3)\over(2y-3)^3},
 \qquad y=m^2x.                                                 \tag{5}
\]
Termwise differentiation is absolute and locally uniform because of
\(e^{-\pi m^2e^{2u}}\).  Differentiating the log-sum twice gives the exact
cumulant identity
\[
 \boxed{\quad
 (\log\Phi)'''=\mathbb E_w\ell'''
 +3\mathrm{Cov}_w(\ell',\ell'')
 +\mathbb E_w(\ell'-\mathbb E_w\ell')^3.\quad}                  \tag{6}
\]
Unlike the variance identity used for log-concavity, the last term in (6)
has no generic sign.

## 2. Explicit first-mode dominance for \(u\ge1/4\)

Write
\[
 \Phi=f_1(1+R),\qquad R=\sum_{m\ge2}r_m,qquad r_m={f_m\over f_1}.
\]
As in `103_34`, with \(a=m^2-1\),
\[
 0<r_m\le2m^4e^{-ax}.                                           \tag{7}
\]
For \(u\ge1/4\), the elementary bounds \(\pi>3\) and
\(e^{1/2}>3/2\) give
\[
 x>9/2.                                                         \tag{8}
\]

Put \(D=d/du=2x\,d/dx\).  From the explicit rational expression in (7),
or by differentiating \(\log r_m\), one obtains for \(ax\ge27/2\)
\[
 |D\log r_m|<3ax,qquad
 |D^2\log r_m|<5ax,qquad
 |D^3\log r_m|<10ax.                                           \tag{9}
\]
Consequently
\[
 |D r_m|<3axr_m,\qquad
 |D^2r_m|<10a^2x^2r_m,\qquad
 |D^3r_m|<35a^3x^3r_m.                                         \tag{10}
\]
The constants are deliberately rounded upward; substitution of
\(4t/(2t-3)=2+6/(2t-3)\) and its first two derivatives proves (9)
term by term.

Enlarging \(\{m^2-1:m\ge2\}\) to the integers \(a\ge3\), and using
\(m^4\le16a^2/9\), turns every sum in (10) into a geometric majorant
starting with \(e^{-3x}\).  At \(x\ge9/2\), the ratio of consecutive
majorant terms is less than \(1/5\).  More precisely, the finite Taylor
sum \(\sum_{k=0}^{14}(9/2)^k/k!>90\) proves
\(e^{9/2}>90\), hence \(e^{27/2}>729000\).  Separate the \(a=3\)
term; for the remaining tail the successive ratios are bounded by the
corresponding ratios at \(a=4\).  Rational summation then gives
\[
 |R'|<{19\over10000},\qquad
 |R''|<{83\over1000},\qquad
 |R'''|<{397\over100}.                                        \tag{11}
\]
For example, the first terms of the three majorants are bounded by
\(1296/729000\), \(58320/729000\), and
\(2755620/729000\).  Their first tail ratios are respectively
\((4/3)^3/90,(4/3)^4/90,(4/3)^5/90\); all later ratios are at most
\((5/4)^j/90\), with \(j=3,4,5\).  These rational bounds imply (11)
directly.  Substitution in
\[
 D^3\log(1+R)
 ={R'''\over1+R}-{3R'R''\over(1+R)^2}
 +{2(R')^3\over(1+R)^3}                                       \tag{12}
\]
gives the explicit uniform bound
\[
 \left|D^3\log(1+R)\right|
 <{397\over100}
   +3{19\over10000}{83\over1000}
   +2\left({19\over10000}\right)^3
 <4.                                                           \tag{13}
\]
All quantities in this estimate decrease after their value at \(x=9/2\):
each has the form a fixed polynomial in \(ax\) times \(e^{-ax}\), with
\(ax\ge27/2\).

For the first summand, (5) gives
\[
 \ell_1'''=-8x+{48x(2x+3)\over(2x-3)^3}.
\]
At \(x\ge9/2\), the positive rational term decreases relative to \(x\),
and direct rational arithmetic at \(x=9/2\) yields
\[
 \ell_1'''\le-36+12=-24.                                      \tag{14}
\]
(The positive rational term at \(9/2\) is exactly \(12\).)  Combining
(11)--(14),
\[
 (\log\Phi)'''=\ell_1'''+D^3\log(1+R)<-24+4<0.
\]
for every \(u\ge1/4\).  Hence
\[
 \boxed{\qquad h''(u)>0\qquad(u\ge1/4).\qquad}                 \tag{15}
\]

## 3. Why the modular interval is genuinely different

The theta transformation makes \(\Phi(|u|)\) a smooth even function.
Therefore
\[
 (\log\Phi)'''(0)=0.                                           \tag{16}
\]
But (5) at \(m=1,x=\pi\) has positive sign:
\[
 \ell_1'''(0)
 =-8\pi+{48\pi(2\pi+3)\over(2\pi-3)^3}>0.                     \tag{17}
\]
Thus first-mode dominance has the wrong sign at the endpoint.  The terms
\(m\ge2\), though small in mass, have derivatives containing powers of
\(m^2x\) and cancel (17) exactly to produce (16).

A rigorous completion on \((0,1/4)\) must retain that cancellation.  One
adequate certificate would be:

1. use evenness to write
   \((\log\Phi)'''(u)=u(\log\Phi)^{(4)}(0)+u^3R_6(u)/6\);
2. enclose \((\log\Phi)^{(4)}(0)\) strictly below zero by termwise theta
   differentiation;
3. give a rational uniform bound for \(|R_6(u)|\) on \([0,1/4]\) strong
   enough to preserve the sign, subdividing the interval if necessary;
4. bound the \(m\)-tail by a polynomial times \(e^{-\pi m^2}\).

The modular identity supplies the vanishing odd derivatives at zero, but it
does not by itself supply items 2--3.  Decimal evaluation of those
derivatives would be diagnostic, not a proof.  No such rational Taylor
model is presently checked into the phase, so (1) cannot yet be stated as a
global theorem.

## 4. Consequences for the tilted covariances \(\Gamma_p\)

Let
\[
 d\nu_p(u)={u^p\Phi(u)du\over M_p},\qquad
 \Gamma_p=\mathrm{Cov}_{\nu_p}(u,h),                     \tag{18}
\]
as in `103_39`.  The exact identities there are
\[
 \Gamma_p=(p+1)\left(1-{q_p\over q_{p-1}}\right),
 \qquad q_p={M_{p+1}/(p+1)!\over M_p/p!}.                        \tag{19}
\]
If the missing compact proof completed (1), then \(h\) would be increasing
and strictly convex.  Besides \(\Gamma_p>0\), convexity would give the
pointwise tangent inequality
\[
 h(u)\ge h(v)+h'(v)(u-v),                                      \tag{20}
\]
and hence the already useful one-tilt bound
\[
 \Gamma_p\ge h'(0)\mathrm{Var}_{\nu_p}(u).               \tag{21}
\]

It does not automatically order consecutive \(\Gamma_p\).  Size biasing
gives an exact formula for the change.  Put
\(\mu_p=\mathbb E_pu\), \(V_p=\mathrm{Var}_p(u)\), and
\[
 T_p=\mathbb E_p[(u-\mu_p)^2(h-\mathbb E_ph)].
\]
Since \(d\nu_{p+1}=u\,d\nu_p/\mu_p\), direct expansion yields
\[
 \boxed{\quad
 \Gamma_{p+1}
 =\left(1-{V_p\over\mu_p^2}\right)\Gamma_p+{T_p\over\mu_p}.
 \quad}                                                         \tag{22}
\]
Even when \(h''>0\), the centered mixed moment \(T_p\) is not determined
by (20) alone.  The cubic gate uses five successive \(\Gamma_p\)'s through
`103_39`, equations (5)--(8).  Therefore a global proof of (1) would be a
new structural input, but one would still need a quantitative estimate for
\(T_p\), or an equivalent comparison of consecutive \(\Gamma_p\), to close
PF\(_3\).

## Status

Hazard convexity is rigorously proved for \(u\ge1/4\).  The unresolved
piece is a finite modular interval with an explicitly stated rational
Taylor-certificate obligation.  No numerical sign check was promoted to a
global theorem.  Moreover, the exact update formula (22) shows why the sign
\(h''>0\), even if completed, is not alone the cubic Jensen inequality.
