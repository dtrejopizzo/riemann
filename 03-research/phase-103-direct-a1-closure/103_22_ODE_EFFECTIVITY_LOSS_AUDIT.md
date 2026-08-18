# Laguerre ODE effectivity audit for \(\alpha=2,3\)

## Purpose

This note starts directly from the Laguerre differential equation and proves
the target interior budgets with fully explicit (deliberately enormous)
constants, without importing a uniform hard-edge/bulk/turning-point theorem.
The first four sections identify the quarter-power lost by global
orthogonality; Section 5 recovers it by a Bessel--Volterra connection to a
mesoscopic point, short energy transport for \(\alpha=2\), and weighted
Cauchy--Schwarz on the remaining tail.

Put
\[
 v(x)=x^{\alpha/2+1/2}e^{-x/2}L_N^{(\alpha)}(x),
 \qquad \nu=N+{\alpha+1\over2}.
\]
Then
\[
 v''+Q_{\alpha,N}(x)v=0,
 \qquad
 Q_{\alpha,N}(x)={\nu\over x}-{1\over4}+{1-\alpha^2\over4x^2}.
 \tag{1}
\]

## 1. Exact global energy bound

Laguerre orthogonality is exactly
\[
 \int_0^\infty {v(x)^2\over x}\,dx
 =\int_0^\infty x^\alpha e^{-x}\bigl(L_N^{(\alpha)}(x)\bigr)^2dx
 ={\Gamma(N+\alpha+1)\over N!}.                                    \tag{2}
\]
For \(a=\log2\) and \(\alpha>1\), Cauchy--Schwarz therefore gives the
completely explicit bound
\[
\begin{aligned}
 I_\alpha(a;N)
 &=\int_a^{4N}x^{-\alpha/2-1/2}|v(x)|\,dx\\
 &\le\left({\Gamma(N+\alpha+1)\over N!}
 {a^{1-\alpha}\over\alpha-1}\right)^{1/2}.                         \tag{3}
\end{aligned}
\]
In particular,
\[
 I_2(a;N)\le {\sqrt{(N+1)(N+2)}\over\sqrt a},
 \qquad
 I_3(a;N)\le {\sqrt{(N+1)(N+2)(N+3)}\over\sqrt{2}\,a}.             \tag{4}
\]
These are rigorous for every \(N\), but have orders \(N\) and
\(N^{3/2}\), respectively.

## 2. The loss is exactly a quarter-power

The target bounds are
\[
 I_2(a;N)=O(N^{3/4}),\qquad I_3(a;N)=O(N^{5/4}).                      \tag{5}
\]
Comparing (4) with (5), the sole deficit is \(N^{1/4}\) in both cases.
It enters at the one and only inequality in (3): orthogonality controls
the squared mass of \(v\), while Cauchy--Schwarz discards its oscillation.
No endpoint convention, outer tail, or hidden constant is responsible for
this loss.

## 3. What the ODE energy does prove, and what it does not

On the interval \([a,4N]\), for \(\alpha=2,3\) and all sufficiently
large \(N\), \(Q_{\alpha,N}>0\).  The energy
\[
 \mathcal E(x)=v'(x)^2+Q_{\alpha,N}(x)v(x)^2
\]
satisfies the exact identity
\[
 \mathcal E'(x)=Q_{\alpha,N}'(x)v(x)^2,
 \qquad
 Q_{\alpha,N}'(x)=-{\nu\over x^2}+{\alpha^2-1\over2x^3}.           \tag{6}
\]
Away from the hard edge this derivative is negative.  Thus Prüfer/energy
methods correctly identify the local wavelength
\[
 Q_{\alpha,N}(x)^{-1/2}\asymp\sqrt{x/N}                             \tag{7}
\]
in the bulk and the turning scale \(N^{1/3}\) near \(4N\).

However, (2) plus the monotonicity in (6) does not by itself bound the
energy entering from the hard edge with the factor \(N^{-1/2}\) needed to
turn the global \(L^2\) mass into the pointwise WKB amplitude.  The missing
quantitative statement is an explicit connection/Volterra estimate of the
form
\[
 |v(x)|\le C_\alpha N^{\alpha/2}
 x^{1/4}\bigl(N^{1/3}+|4N-x|\bigr)^{-1/4},                           \tag{8}
\]
with a numerical \(C_\alpha\), uniformly from the fixed lower endpoint
through the turning window.  Dividing (8) by \(x^{\alpha/2+1/2}\)
reproduces exactly the pointwise majorant (3) of `103_10` on \(x\ge a\):
\[
 e^{-x/2}|L_N^{(\alpha)}(x)|
 \le C_\alpha N^{\alpha/2}x^{-\alpha/2-1/4}
 (N^{1/3}+|4N-x|)^{-1/4}.
\]
Away from the soft edge the final factor is \(O(N^{-1/4})\), which is
where the required quarter-power is gained.  A uniform *pointwise* proof of
(8) would require Bessel, bulk, and Airy connections.  The integral budgets
need less: Section 5 reaches \(x=\nu^{1/3}\) by Volterra, closes
\(\alpha=3\) directly by weighted Cauchy--Schwarz, and closes \(\alpha=2\)
after energy transport only to \(x=\nu^{1/2}\).  Thus no Airy estimate is
needed for the two stated integral bounds.

## 4. Consequence for the conditional threshold

The outer-tail estimate of `103_09` is fully explicit and sufficient beyond
\(4N\).  Section 5 gives effective (but extremely large) constants
\(C_2,C_3\), without a bulk or Airy connection theorem.  These establish
the eventual conditional estimates.  They do not establish the advertised
threshold \(150\): the constants are much too coarse, and the finite-range
certificate has not been redone with them.

## 5. Bessel--Volterra connection through the mesoscopic scale

The hard edge itself can be disposed of with deliberately crude, but fully
numerical, constants.  Put \(t=2\sqrt{\nu x}\), view \(v\) as a function
of \(t\), and set
\[
 w(t)={v(x)\over\sqrt t},\qquad q_\alpha(t)=1+{1-4\alpha^2\over4t^2}.
\]
Equation (1) becomes exactly
\[
 w''+q_\alpha(t)w={t^2\over16\nu^2}w.                              \tag{9}
\]
The regular homogeneous solution is \(\phi_\alpha(t)=\sqrt tJ_\alpha(t)\),
and matching at zero gives
\[
 w(t)\sim A_{N,\alpha}\phi_\alpha(t),\qquad
 A_{N,\alpha}={\Gamma(N+\alpha+1)\over
 2\Gamma(N+1)\nu^{(\alpha+1)/2}}.                                  \tag{10}
\]
Equivalently \(v(x)\sim A_{N,\alpha}tJ_\alpha(t)\).  The factor
\(2\sqrt\nu\) here is essential.

### 5.1 An explicit Bessel constant

For \(m=1,\ldots,4\) and \(1\le t\le8\), the Frobenius series give
\[
 |J_m(t)|\le {4^m\over m!}e^{16}<3\cdot10^9.                       \tag{11}
\]
The integer-order Frobenius expansion for \(Y_m\), after absolute values,
gives
\[
\begin{aligned}
 |Y_m(t)|
 &\le {2\over\pi}(\log4+\gamma)|J_m(t)|
 +{1\over\pi}\sum_{k=0}^{m-1}{(m-k-1)!\over k!}
       \left({t\over2}\right)^{2k-m}\\
 &\quad+{1\over\pi}\sum_{k\ge0}{(2k+6)4^{m+2k}\over k!(m+k)!}
 <5\cdot10^{10}.                                                    \tag{12}
\end{aligned}
\]
Only \(e^{16}<10^7\), \(\log4+\gamma<2\), \(H_j\le j\), \(\pi>3\),
and \((m+k)!\ge k!\) are used.  In particular, the last series before
division by \(\pi\) is at most
\[
 4^m\sum_{k\ge0}(2k+6){16^k\over(k!)^2}
 \le4^m(32+6)e^{16}<10^{11},
\]
so no numerical special-function evaluation is hidden here.  The finite
sum in (12) is at most \(4\cdot6\cdot16=384\): it has at most four
terms, \((m-k-1)!/k!\le6\), and every power of \(t/2\) occurring there
is at most \(16\).  Thus the three terms in (12) are below
\(4\cdot10^9\), \(128\), and \(10^{11}/\pi\), respectively.

The derivative recurrence \(F_m'=(F_{m-1}-F_{m+1})/2\), for
\(F=J,Y\), gives \(|J_m'|\le3\cdot10^9\) and
\(|Y_m'|\le5\cdot10^{10}\) on \([1,8]\), for \(m=2,3\).  Therefore,
for \(W=\sqrt tF\),
\[
 |W'|\le {|F|\over2\sqrt t}+\sqrt t|F'|<1.6\cdot10^{11},
 \qquad |W|<1.5\cdot10^{11}.                                     \tag{12a}
\]

For \(F=J_m,Y_m\), write \(W=\sqrt tF\).  Then
\(W''+q_mW=0\).  On \(t\ge8\), \(q_m\ge4/5\) for \(m=2,3\), and
\((E/q_m)'=-q_m'W'^2/q_m^2\le0\) for \(E=W'^2+q_mW^2\).  At
\(t=8\), (12a) gives \(E(8)/q_m(8)<5.5\cdot10^{22}\).  Thus the
bounds at \(8\) yield, with ample slack,
\[
 |\sqrt tJ_m(t)|,\ |\sqrt tY_m(t)|<4\cdot10^{11}\quad(t\ge8).
\]
Together with (11)--(12) on \([1,8]\), this proves
\[
 |\phi_m(t)|+|\chi_m(t)|\le B:=10^{12}
 \quad(t\ge1,\ m=2,3),                                             \tag{13}
\]
where \(\chi_m=\sqrt tY_m\).  The same series recurrence on \([1,8]\)
and the energy estimate on \([8,\infty)\) also give
\[
 |\phi_m'(t)|+|\chi_m'(t)|\le B
 \quad(t\ge1,\ m=2,3).                                             \tag{13a}
\]

### 5.2 Joining at \(t=1\) and Volterra bootstrap

For \(0\le t\le1\), the exact hypergeometric series is
\[
 {L_N^{(\alpha)}(t^2/(4\nu))\over L_N^{(\alpha)}(0)}
 ={}_1F_1\left(-N;\alpha+1;{t^2\over4\nu}\right).
\]
Its absolute value is at most \(e^{1/4}<4/3\); differentiating the same
series gives, safely,
\[
 |w(1)|+|w'(1)|\le2A_{N,\alpha}.                                   \tag{14}
\]
The preceding series and recurrence bounds at \(1\), together with
\(W(\phi_m,\chi_m)=2/\pi\), show that the homogeneous solution having
the data in (14) has coefficients \(c_\phi,c_\chi\) with
\[
 |c_\phi|+|c_\chi|\le10^{13}A_{N,\alpha}.                        \tag{15}
\]

Let \(N\ge149\), and put \(T=2\nu^{2/3}>8\).  Variation of constants on
\([1,T]\), (13), and Gronwall give
\[
 |w(t)|\le 10^{13}BA_{N,\alpha}
 \exp\!\left({\pi B^2\over6}\right),
 \qquad1\le t\le2\nu^{2/3},                                     \tag{16}
\]
because
\[
 {\pi\over2}|\phi(r)\chi(t)-\chi(r)\phi(t)|\le\pi B^2,qquad
 \int_1^{2\nu^{2/3}}{r^2\over16\nu^2}\,dr\le{1\over6}.          \tag{17}
\]
This constant is enormous but numerical and uniform.  Differentiating the
variation-of-constants formula (its upper-limit term is zero) and using
(13a) gives, on the same interval,
\[
 |w'(t)|\le K_1A_{N,\alpha},\qquad
 K_1=(1+P)K,\quad P={\pi B^2\over6},
 \quad K=10^{13}Be^P.                                              \tag{16a}
\]
Finally,
\(A_{N,2}\le4\sqrt N\) and \(A_{N,3}\le2N\).  Since
\(v=\sqrt t\,w\) and \(t=2\sqrt{\nu x}\), (16) proves
\[
 |v(x)|\le C_\alpha N^{\alpha/2-1/4}x^{1/4}
 \qquad(a\le x\le\nu^{1/3},\ N\ge149),                          \tag{18}
\]
with explicit \(C_\alpha\).

### 5.3 An explicit \(\alpha=3\) integral budget

Write
\[
 K=10^{13}B\exp\!\left({\pi B^2\over6}\right).
\]
The deliberately loose inequalities used above give from (16)
\[
 |v(x)|\le HN^{5/4}x^{1/4},\qquad
 H=4K,\qquad a\le x\le M:=\nu^{1/3}.                              \tag{19}
\]
For \(\alpha=3\), \(e^{-x/2}|L_N^{(3)}(x)|=x^{-2}|v(x)|\).  Hence
\[
 \int_a^M e^{-x/2}|L_N^{(3)}(x)|\,dx
 \le {4H\over3}a^{-3/4}N^{5/4}.                                  \tag{20}
\]
The exact Cauchy--orthogonality bound (3), now used only beyond \(M\), is
\[
 \int_M^\infty e^{-x/2}|L_N^{(3)}(x)|\,dx
 \le\left({(N+1)(N+2)(N+3)\over2M^2}\right)^{1/2}
 \le2N^{7/6}\le2N^{5/4}.                                         \tag{21}
\]
Combining (20)--(21) proves the first fully explicit target budget in this
note:
\[
 \boxed{\quad I_3(a;N)\le C_3N^{5/4},\qquad
 C_3={4H\over3}a^{-3/4}+2,\quad N\ge149.\quad}                   \tag{22}
\]
No bulk or Airy connection estimate is needed for this conclusion.

### 5.4 Elementary transport closes the \(\alpha=2\) budget

Set \(x_0=\nu^{1/3}\) and \(M=\nu^{1/2}\).  At the point corresponding
to \(t_0=2\nu^{2/3}\), (16) and (16a), followed by the elementary change
of variables back to \(x\), give
\[
 |v(x_0)|\le2KA_{N,2}\nu^{1/3},\qquad
 |v'(x_0)|\le2K_1A_{N,2}\nu^{2/3}.                                \tag{23}
\]
For \(\alpha=2\), put
\[
 S(x)=v(x)^2+{v'(x)^2\over Q_{2,N}(x)}.
\]
On \([x_0,M]\), \(Q_{2,N}>0\), \(Q_{2,N}'<0\), and direct
differentiation using \(v''+Q_{2,N}v=0\) gives the exact identity
\[
 S'(x)=-{Q_{2,N}'(x)v'(x)^2\over Q_{2,N}(x)^2}
 \le-{Q_{2,N}'(x)\over Q_{2,N}(x)}S(x).                           \tag{24}
\]
Here the elementary inequalities
\[
 Q_{2,N}(x_0)\ge\tfrac12\nu^{2/3},\qquad
 Q_{2,N}(x)\ge{\nu\over2x}\quad(x_0\le x\le M)                  \tag{25}
\]
hold for \(N\ge149\).  Thus (23) gives
\[
 S(x_0)\le12K_1^2A_{N,2}^2\nu^{2/3},                              \tag{26}
\]
and integrating (24) yields
\[
 S(x)\le S(x_0){Q_{2,N}(x_0)\over Q_{2,N}(x)}
 \le2S(x_0){x\over x_0}.
\]
Consequently, since \(A_{N,2}\le4\sqrt N\),
\[
 |v(x)|\le G N^{2/3}x^{1/2},qquad
 G=40K_1,qquad x_0\le x\le M.                                   \tag{27}
\]
This uses no oscillatory cancellation: it is a positive energy transport
estimate over just the short mesoscopic interval.

The contribution before \(x_0\) follows from (18), with
\(H_2=8K\):
\[
 \int_a^{x_0}e^{-x/2}|L_N^{(2)}(x)|\,dx
 \le4H_2a^{-1/4}N^{3/4}.                                          \tag{28}
\]
On \([x_0,M]\), (27) gives
\[
 \int_{x_0}^M e^{-x/2}|L_N^{(2)}(x)|\,dx
 \le G N^{2/3}\log{M\over x_0}
 \le4G N^{3/4}.                                                    \tag{29}
\]
For the last inequality use \(\log\nu\le12\nu^{1/12}\) and
\(\nu\le2N\).  Finally, (3) gives
\[
 \int_M^\infty e^{-x/2}|L_N^{(2)}(x)|\,dx
 \le\left({(N+1)(N+2)\over M}\right)^{1/2}
 \le2N^{3/4}.                                                      \tag{30}
\]
We have therefore obtained the second target budget:
\[
 \boxed{\quad I_2(a;N)\le C_2N^{3/4},\qquad
 C_2=4H_2a^{-1/4}+4G+2,\quad N\ge149.\quad}                      \tag{31}
\]

There is no residual finite-range assumption in the Laguerre theorem.
For \(1\le N<149\), the elementary bounds (4), together with
\((N+1)(N+2)\le6N^2\) and
\((N+1)(N+2)(N+3)\le24N^3\), give
\[
 I_2(a;N)\le {\sqrt6\,148^{1/4}\over\sqrt a}N^{3/4},\qquad
 I_3(a;N)\le {\sqrt{12}\,148^{1/4}\over a}N^{5/4}.                \tag{32}
\]
Replacing \(C_2,C_3\) by the maxima of their values in (31), (22), and
(32) proves both budgets for every \(N\ge1\) with completely explicit
constants.  These constants are far too large to recover the conditional
threshold \(150\), but they remove the previously unproved uniform
Laguerre input from the eventual conditional argument.
