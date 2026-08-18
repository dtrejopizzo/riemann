# Effective conditional threshold for the A1 transport

## Theorem and scope

Put \(a=\log 2\), \(N=n-1\), and
\[
 {\cal J}_n=\int_a^{T_n}(\psi(e^u)-e^u)e^{-u}L_N^{(2)}(u)\,du.    \tag{1}
\]
Define
\[
 B=25000,\quad P={B^2\over3},\quad K=4B^2e^P,                    \tag{2}
\]
\[
 C_2=(196+160P)K+2,\quad A=72C_2,                               \tag{3}
\]
and
\[
 n_{\rm eff}=\left\lceil\{A(8\log A)\}^{4}\right\rceil.          \tag{4}
\]

> **Theorem.** Assume RH. Then
> \[
> |{\cal J}_n|\le {3\over4}\lambda_n^{\rm arch}
>                 +1-L_n^{(1)}(\log2)
> \qquad(n\ge n_{\rm eff}).                                     \tag{5}
> \]

The constants are closed numerical expressions, and elementary rational
upper estimates give
\[
 \log n_{\rm eff}<833334000,\qquad
 n_{\rm eff}<10^{362320000}.                                    \tag{6}
\]
This is an effective theorem conditional on RH, not an unconditional
theorem. It does not prove the formerly advertised threshold 150.
The certificate in 103_51 stops at 149, so the finite interval
\(150\le n<n_{\rm eff}\) is not closed by combining the two results.

## 1. Reducing the Volterra constant

The ODE and Bessel transformations are those proved in 103_22 and audited
in 103_23. We replace only their deliberately enormous numerical
majorant.

For integer \(0\le m\le4\) and \(1\le t\le4\), the elementary integral
formula gives \(|J_m(t)|\le1\). In the integer-order series for \(Y_m\),
use
\[
 |\log(t/2)|+\gamma<2,\quad e^4<55,\quad\pi>3.
\]
The finite negative-power sum is less than \(384/\pi<128\). The infinite
sum is bounded by
\[
 {1\over\pi}\sum_{k\ge0}{(2k+6)2^{m+2k}\over k!(m+k)!}
 \le {16\over3}\sum_{k\ge0}{(2k+6)4^k\over(k!)^2}
 <{16\over3}\,14e^4<4107.                                      \tag{7}
\]
Thus \(|Y_m(t)|<4300\). The derivative recurrences imply, for
\(m=1,2,3\) and \(W=\sqrt tJ_m\) or \(\sqrt tY_m\),
\[
 |W|<8600,\qquad |W'|<10750.                                    \tag{8}
\]

For \(t\ge4\), set
\[
 q_m=1+{1-4m^2\over4t^2},\qquad E=W'^2+q_mW^2.
\]
Then \(q_m\ge29/64\), \(q_m'>0\), and
\[
 (E/q_m)'=-q_m'W'^2/q_m^2\le0.
\]
For the \(Y_m\) solutions, the exact integer inequality
\[
 {64\over29}(10750^2+8600^2)<21000^2                           \tag{9}
\]
propagates (8) to infinity.  The \(J_m\) solutions have the much smaller
initial bounds \(|W|\le2\), \(|W'|\le5/2\); the same energy calculation
gives
\[
 {64\over29}\left(2^2+(5/2)^2\right)<5^2.
\]
Thus the sum of the \(J_m\) and \(Y_m\) bounds is less than
\(21000+5<25000\), for both values and derivatives. Consequently,
\[
 |\sqrt tJ_m|+|\sqrt tY_m|\le B,\qquad
 |(\sqrt tJ_m)'|+|(\sqrt tY_m)'|\le B                           \tag{10}
\]
for \(t\ge1\), \(m=1,2,3\), with \(B=25000\).

At the joining point, the hypergeometric series gives
\[
 |w(1)|+|w'(1)|\le2A_{N,\alpha}.
\]
Cramer's rule, the Wronskian \(2/\pi\), and (10) bound the homogeneous
solution by \(4B^2A_{N,\alpha}\). The Green kernel and its derivative are
at most \(2B^2\), while
\[
 \int_1^{2\nu^{2/3}}{r^2\over16\nu^2}\,dr\le{1\over6}.
\]
Gronwall therefore gives
\[
 |w|\le KA_{N,\alpha},\qquad
 |w'|\le(1+P)KA_{N,\alpha},                                     \tag{11}
\]
with exactly (2).

Repeating the already audited conversion and short energy transport of
103_22 gives the full-half-line estimate
\[
 \boxed{\int_a^\infty e^{-u/2}|L_N^{(2)}(u)|\,du
 \le C_2N^{3/4}\quad(N\ge149).}                                 \tag{12}
\]
Indeed, the three pieces are at most
\[
 32Ka^{-1/4}N^{3/4},\quad
 160(1+P)KN^{3/4},\quad2N^{3/4}.
\]
Since \(a^{-1/4}<9/8\), their sum is (3).

For order three it is better to retain the small constant and sacrifice a
quarter power. Orthogonality and Cauchy--Schwarz give, for every \(N\ge1\),
\[
 \boxed{\int_a^\infty e^{-u/2}|L_N^{(3)}(u)|\,du
 <{21\over4}N^{3/2}.}                                          \tag{13}
\]
Here we used
\((N+1)(N+2)(N+3)\le24N^3\), \(a>2/3\), and \(\sqrt{12}<7/2\).

## 2. Effective zero counting without a hidden RvM constant

Let \({\cal N}(T)\) count all nontrivial zeros with
\(|\Im\rho|\le T\), including multiplicity and both signs. The positive
theta representation used in 103_31 is
\[
 \xi(s)=\int_{\mathbb R}e^{(s-1/2)u}\,d\mu(u),
 \qquad d\mu>0,\quad d\mu(-u)=d\mu(u).                           \tag{14}
\]
It implies the fully numerical bound
\[
 \boxed{{\cal N}(T)\le25T\log T\qquad(T\ge10).}                  \tag{15}
\]

To prove it, every counted zero lies in the disk centred at 2 with radius
\(R=(T^2+4)^{1/2}\). Jensen in the concentric disk of radius \(2R\)
gives
\[
 {\cal N}(T)\log2
 \le\max_{|s-2|=2R}\log|\xi(s)|-\log\xi(2).                     \tag{16}
\]
Positivity and symmetry in (14) give
\[
 |\xi(s)|\le\xi\bigl(\tfrac12+|\Re(s-\tfrac12)|\bigr)
 \le\xi(2+2R).                                                  \tag{17}
\]
For the real value \(r=2+2R>22\), the defining formula for \(\xi\), the
integral-test bound \(\zeta(r)<2\), and the elementary estimate
\(\Gamma(x)\le3(2x)^{x-1}\) give
\[
 \log\xi(r)\le2r\log r.                                        \tag{18}
\]
For the last Gamma estimate, split its defining integral at \(2x\).
The first piece is at most \((2x)^{x-1}\); on the second, extract
\(e^{-t/2}\), whose product with \(t^{x-1}\) is decreasing after
\(2x\), and integrate the remaining \(e^{-t/2}\). This gives the displayed
factor 3.
Also \(\xi(2)=\pi/6>1/2\). For \(T\ge10\),
\[
 R<(51/50)T,\quad2+2R<(9/4)T,\quad
 \log((9/4)T)<(3/2)\log T,\quad\log2>2/3.
\]
Substitution in (16)--(18) gives less than \(12T\log T\); (15)
retains more than a factor two of slack.

Under RH,
\[
 \sum_\rho{1\over|\rho|^2}
 =\sum_\rho{1\over\rho(1-\rho)}
 =2+\gamma-\log(4\pi)<1.                                      \tag{19}
\]
Partial summation with (15) and (19) gives, for \(Y\ge10\),
\[
 \sum_{|\gamma|\le Y}{1\over|\rho|}\le28\log^2Y,                \tag{20}
\]
\[
 \sigma(Y):=\sum_{|\gamma|>Y}{1\over|\rho|^2}
 \le {50(\log Y+1)\over Y}.                                    \tag{21}
\]
For (20), the block below 10 costs less than 11 by (19), while the
remaining Stieltjes integral costs at most
\(25\log Y+(25/2)\log^2Y\). For (21), discard the favourable boundary
term and calculate
\[
 2\int_Y^\infty {25t\log t\over t^3}\,dt
 ={50(\log Y+1)\over Y}.
\]

## 3. Effective RH transport

Split the explicit zero sum at
\[
 Y=N^{3/4}.                                                     \tag{22}
\]
The low zeros, (12), and (20) contribute at most
\[
 16C_2N^{3/4}\log^2N.                                          \tag{23}
\]

For the high zeros define, for \(u\ge c\),
\[
 V_c^Y(u)=\sum_{|\gamma|>Y}{e^{\rho u}-e^{\rho c}\over\rho^2}.
\]
Under RH, \(|V_c^Y(u)|\le2e^{u/2}\sigma(Y)\). Integrate by parts
separately on \([a,\infty)\) and \([T_n,\infty)\). This avoids an
unevaluated boundary value at \(T_n\). Since
\((e^{-u}L_N^{(2)})'=-e^{-u}L_N^{(3)}\), (13) and (21) give
\[
 \left|\int_a^{T_n}S^Y(u)e^{-u}L_N^{(2)}(u)\,du\right|
 \le4\sigma(Y){21\over4}N^{3/2}
 \le1050N^{3/4}\log N.                                        \tag{24}
\]

The elementary term
\[
 g(u)=\log(2\pi)+\tfrac12\log(1-e^{-2u})
\]
satisfies \(0<g(u)<2\) on \(u\ge a\), so its contribution is at most
\(2C_2N^{3/4}\). Since \(\log N>4\) and \(C_2>1050\), (23)--(24)
give
\[
 \boxed{|{\cal J}_n|
 \le18C_2N^{3/4}\log^2N
 \le18C_2n^{3/4}\log^2n.}                                     \tag{25}
\]

## 4. Reserve and the explicit threshold

No order-one Plancherel--Rotach constant is needed. The elementary identity
\[
 \int_0^\infty e^{-t}t^kJ_0(2\sqrt{xt})\,dt
 =k!e^{-x}L_k(x)
\]
and \(|J_0|\le1\) imply \(|L_k(x)|\le e^x\). Since
\(L_n^{(1)}=\sum_{k=0}^nL_k\),
\[
 |L_n^{(1)}(\log2)|\le2(n+1).                                  \tag{26}
\]
The archimedean lower bound from 103_02 therefore gives
\[
 q(n)\ge {3\over8}n(\log n-3)-2(n+1)+1.                        \tag{27}
\]
In particular,
\[
 q(n)\ge {1\over4}n\log n\qquad(\log n\ge27).                  \tag{28}
\]

Comparison of (25) with (28) reduces to
\[
 n^{1/4}\ge72C_2\log n=A\log n.                                \tag{29}
\]
Let \(L=\log A\).  The function \(L-\log(8L)\) is increasing for
\(L>1\), and it is positive at \(L=10\) because \(\log80<5\).
Thus \(L>10\) implies \(L>\log(8L)\). At
\[
 x=4\{L+\log(8L)\}
\]
one has \(e^{x/4}=8AL\ge Ax\). The ratio \(e^{x/4}/x\) increases for
\(x>4\). Formula (4) therefore implies (29) for all larger \(n\), and
also implies \(\log n\ge27\). This proves (5).

Finally,
\[
 P<208333334,\quad\log(4B^2)<22,\quad
 \log(196+160P)<25,\quad\log(8\log A)<22
\]
inserted into (2)--(4) prove (6) without floating-point input.

## Audit conclusion

The effectivity question now has a rigorous answer:

1. The measured threshold 150 remains unproved.
2. The transport estimates do imply the explicit conditional threshold
   (4), with no hidden asymptotic or zero-counting constant.
3. The huge finite interval between 150 and (4) is not certified.
4. RH is used only in (19)--(21) and in
   \(|e^{\rho u}|=e^{u/2}\). The Laguerre bounds are unconditional.

Thus this closes the constant-effectivity gap, but not the unconditional
A1/RH gate.
