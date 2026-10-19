# R170_823 — Multiscale averaging of Poisson--Chebyshev

Continuation of R170_819--822. This note replaces
the pointwise comparison of two scales with an oriented average of the
fully conjugated PC identity. The average produces a real analytic
piece: the nontrivial arithmetic translations become smoothing and, after
compression to a finite window, Hilbert--Schmidt. It does not by itself
produce a sign. It is also shown that averaging and then subtracting scale
one does not remove the norm obstruction of R170_821.

## 1. Fixed weight and averaged operators

We fix, before choosing a contact, a vector, or a sign,

\[
 0<\rho _0<1,\qquad
 w\in C_c^k((\rho _0,1);\mathbb R),\qquad
 \int_{\rho _0}^1w(\rho)\,d\rho=1.                 \tag{1}
\]

The weight may be positive. Signed weights are also allowed; in that case
\(w\) is replaced by \(|w|\) in the bounds below. A recipe with variable
width can be obtained from a universal profile fixed in advance,

\[
 w_h(\rho)=h^{-1}W((1-\rho)/h),\qquad
 W\in C_c^k((0,1)),\quad \int_0^1W=1.               \tag{2}
\]

The profile does not depend on \(F\) nor on \(T\); the smoothing constants of
(2), however, worsen as \(h\downarrow0\). For a weakly measurable and
uniformly bounded field \(B_\rho\), we write

\[
 \langle B\rangle_w=\int_{\rho _0}^1w(\rho)B_\rho\,d\rho              \tag{3}
\]

as a weak integral of operators. All PC operators are finite sums or
products of bounded operators over the regular kernel, so that (3) is
legitimate there. The form identities are then extended by joint
continuity, as in R170_819--820.

With the notation of R170_820, for each \(\rho\)

\[
\begin{aligned}
 S_\rho&=S_N^{(\rho)},&L_\rho&=L_M^{(\rho)},
 &K_\rho&=K_N^{(\rho)},\\
 U_\rho&=D_\rho^*\mathscr F D_\rho,&
 E_\rho&=S_\rho U_\rho-JS_\rho,
 &H_\rho&=L_\rho S_\rho-K_\rho,\\
 A_\rho&=m(D/\rho)-(L_\rho+L_\rho^*).
\end{aligned}                                                        \tag{4}
\]

Here \(E_\rho\) is the Poisson defect; the interior energy will be denoted
\(\mathcal E_\rho^{\rm int}\) to avoid a symbol collision.

## 2. Averaged PC preserves all the arithmetic

The conjugated identity of R170_820 holds pointwise in \(\rho\):

\[
 S_\rho A_\rho U_\rho
 =\{\rho X,E_\rho\}-L_\rho^*E_\rho
   -JH_\rho-H_\rho U_\rho.                           \tag{5}
\]

Weak integration gives the exact identity

\[
\boxed{
 \big\langle S_\rho A_\rho U_\rho\big\rangle_w
 =\big\langle\{\rho X,E_\rho\}-L_\rho^*E_\rho
   -JH_\rho-H_\rho U_\rho\big\rangle_w .}            \tag{APC}
\]

Averages of products have not been factored: in general
\(\langle L_\rho^*E_\rho\rangle_w\ne
\langle L_\rho^*\rangle_w\langle E_\rho\rangle_w\).
The divisor identity remains exact before and after integrating:

\[
 H_\rho=\sum_{N<j\le MN}\frac{h_{M,N}(j)}{\sqrt j}
                   \tau_{\log j/\rho},
 \qquad
 \langle H_\rho\rangle_w
 =\sum_{N<j\le MN}\frac{h_{M,N}(j)}{\sqrt j}
                   \langle\tau_{\log j/\rho}\rangle_w.              \tag{6}
\]

In particular, \(\Lambda*1=\log\) still eliminates every coefficient with
\(j\le N\). The average does not create a new interior tail.

If the data in each integrand are also conjugated, each scalar of (5) is
the same scalar written in other coordinates. Its average is then a
tautology. The nontrivial situation keeps the contact data fixed.
For fixed \(F,r,g\), define

\[
 z_\rho=S_\rho U_\rho g,
 \qquad
 e_v^{(\rho)}(z)=\langle v,A_\rho z\rangle-\langle r,z\rangle,
 \qquad
 \chi_v^{(\rho)}(g)=
 \langle v,S_\rho A_\rho U_\rho g\rangle
 -\langle r,S_\rho U_\rho g\rangle .                               \tag{7}
\]

The second functional, and not \(e_v^{(\rho)}(z_\rho)\) without a
corrector, is the one that controls PC. Indeed,

\[
 e_v^{(\rho)}(z_\rho)
 =\chi_v^{(\rho)}(g)
  +\langle v,[A_\rho,S_\rho]U_\rho g\rangle .                       \tag{7a}
\]

This commutator is not declared zero. Pairing (5) with \(v\), keeping
\(g\) fixed and integrating gives

\[
\boxed{
\begin{aligned}
 \int w(\rho)\Re \chi_v^{(\rho)}(g)\,d\rho
  ={}&\Re\int w(\rho)
 \langle v,(\{\rho X,E_\rho\}-L_\rho^*E_\rho
              -JH_\rho-H_\rho U_\rho)g\rangle\,d\rho\\
 &-\Re\int w(\rho)
       \langle S_\rho^*r,U_\rho g\rangle\,d\rho .
\end{aligned}}                                                       \tag{8}
\]

Thus \(X,U,E,H\), both collars, and the correct Tate port appear together.
The formula does not use \(S_\rho r\) in place of \(S_\rho^*r\).

## 3. The gain that the average does contribute

For \(a\ne0\), let

\[
 T_{a,w}=\int_{\rho _0}^1w(\rho)\tau_{a/\rho}\,d\rho .               \tag{9}
\]

Setting \(s=1/\rho\), its Fourier multiplier is

\[
 q_{a,w}(\xi)=\int_1^{1/\rho _0}\eta(s)e^{-ia\xi s}\,ds,
 \qquad \eta(s)=w(1/s)s^{-2}.                                      \tag{10}
\]

Since \(w\) has compact support in the open interval, integration
by parts \(j\le k\) times leaves no boundary terms and proves

\[
 |q_{a,w}(\xi)|\le
 \min\left(\|w\|_1,
       \frac{\|\eta^{(j)}\|_1}{|a\xi|^j}\right),
 \qquad 0\le j\le k.                                               \tag{11}
\]

Hence

\[
 \boxed{\ T_{a,w}:L^2(\mathbb R)\longrightarrow H^k(\mathbb R)
       \quad\hbox{is bounded for all }a\ne0.\ }                  \tag{12}
\]

This does not require that the vector it is applied to belong to the
domain of \(D=-i\partial_t\): the derivatives were transferred to the
weight. For the rescaled profile (2), \(\|\eta_h^{(j)}\|_1=O(h^{-j})\); the
gain exists for each \(h>0\), but does not have a uniform constant as
\(h\to0\).

The operator (9) is not compact on \(L^2(\mathbb R)\): a nonzero
multiplier on a nonatomic space is not compact. There is, however, a
compact consequence precisely in the geometry of the contact. If \(P_T\)
is the compression to \((-T,T)\), then

\[
 \boxed{\ P_TT_{a,w}P_T\ \hbox{is Hilbert--Schmidt}.\ }             \tag{13}
\]

Indeed, (9) is convolution with a \(C_c^{k-1}\) density supported in the
interval swept out by \(-a/\rho\); restricting both arguments to a finite
window, its kernel \(K(t,s)=\kappa(t-s)\) belongs to
\(L^2((-T,T)^2)\). Consequently, by (6),

\[
 P_T\langle H_\rho\rangle_wP_T
 \quad\hbox{is a finite sum of Hilbert--Schmidt operators}.      \tag{14}
\]

The same holds for the parts with nonzero shift of
\(\langle L_\rho\rangle_w,\langle K_\rho\rangle_w\) and
\(\langle S_\rho\rangle_w\). The \(n=1\) summand of \(S_\rho\) is the
identity and must be separated out: its compression is not compact. This
separation avoids attributing false compactness to the whole of
\(S_\rho\).

The claim admits an explicit bound. With the convention
\((\tau_bf)(t)=f(t+b)\) and
\((\kappa*f)(t)=\int\kappa(u)f(t-u)du\), (9) has the convolution kernel

\[
 \kappa_{a,w}(u)=\frac{|a|}{u^2}
 w\!\left(-\frac a u\right)
 \mathbf 1_{\{-a/u\in[\rho _0,1]\}},                              \tag{15}
\]

with the corresponding orientation if \(a<0\). A change of variables gives

\[
 \|\kappa_{a,w}\|_2^2
 =\frac1{|a|}\int_{\rho _0}^1\rho^2|w(\rho)|^2d\rho,
 \qquad
 \|P_TT_{a,w}P_T\|_{\rm HS}^2
 \le2T\|\kappa_{a,w}\|_2^2.                                      \tag{16}
\]

For \(\overline H_{M,N,w}:=\langle H_\rho\rangle_w\), the triangle
inequality in the Hilbert--Schmidt class proves the quantitative theorem

\[
\boxed{
 \|P_T\overline H_{M,N,w}P_T\|_{\rm HS}
 \le \left(2T\int_{\rho _0}^1\rho^2|w(\rho)|^2d\rho\right)^{1/2}
 \sum_{N<j\le MN}\frac{h_{M,N}(j)}{\sqrt{j\log j}} .}              \tag{17}
\]

For (2), the \(L^2\) factor of the weight grows like \(h^{-1/2}\), while
the derivative bounds of (11) grow like \(h^{-k}\). Even though in the tail
\(a=\log j\ge\log N\), (17) does not give a constant uniform in \(T,N,M\):
the coefficient sum and the width also change.

(17) must be distinguished from the surviving collar in PC, which is
\(H_\rho U_\rho\) inside the same integral. In general

\[
 \langle H_\rho U_\rho\rangle_w
 \ne\langle H_\rho\rangle_w\langle U_\rho\rangle_w,                \tag{18}
\]

and \(P_T\) cannot be inserted for free between the two factors, since
\(U_\rho P_Tf\) is not supported in the window. Compactness of
\(P_T\overline H_{M,N,w}P_T\) does not prove compactness of the average of
the product. Obtaining it would require analyzing the joint phase of
\(H_\rho U_\rho\); it is not claimed here that this product has a bounded
kernel or that its compression is Hilbert--Schmidt.

Claims (11)--(17) are the new piece: they replace a family of
translations with no norm continuity by an averaged arithmetic block with
spectral decay and compactness after the relevant compression. They do not
yet orient its quadratic form.

## 4. Why subtracting against scale one still fails

The normalization in (1) and Riemann--Lebesgue give

\[
 q_{a,w}(\xi)\longrightarrow0\quad(|\xi|\to\infty),
\]

while \(\tau_a\) has multiplier \(e^{-ia\xi}\). Hence

\[
 \boxed{
 \|T_{a,w}-\tau_a\|_{L^2\to L^2}
 =\operatorname*{ess\,sup}_\xi|q_{a,w}(\xi)-e^{-ia\xi}|
 \ge1.}                                                            \tag{19}
\]

The same conclusion holds in \(Q_{\log}\). In particular, not even the
profile (2) concentrated on \([1-h,1]\) produces norm convergence toward
\(\tau_a\): frequencies of order \((|a|h)^{-1}\) always resolve the width
of the average. Smooth signed weights do not fix (19) either, since their
transform still tends to zero. If their mass is not one, the comparison
with \(\tau_a\) still has a limit of modulus one at high frequency.

That is why the useful piece is the average \(T_{a,w}\) itself, not
declaring \(T_{a,w}-\tau_a\) small. An averaged subtraction of PC against
PC at scale one still contains a block that is not small in norm.

## 5. Exact interface with the flux and the interior reserve

Let \(T\) now be a hypothetical first contact, \(F\in\ker H_T\), and let us
keep fixed the Tate vector \(r=r_F\) and a test \(g=S_LF\). For each
\(\rho\) in the support of \(w\), construct the primitive contraction of
R170_814,

\[
 G_\rho F=D_\rho F-C(D_\rho F)p-S(D_\rho F)q,
 \qquad \delta_\rho=G_\rho F-F.                                   \tag{20}
\]

It is assumed here that the same pair of correctors is valid over the
whole chosen scale interval; for the narrow recipe (2) it suffices to take
its support inside the contraction interval of R170_814. Set

\[
 \mathcal E_\rho^{\rm int}
  =(1-\rho)^{-1}a_M(\delta_\rho,\delta_\rho)\ge0,
 \qquad
 \mathcal R_\rho=\delta_\rho-(1-\rho)z_\rho .                      \tag{21}
\]

Since \(e_F^{(1)}(\delta_\rho)=0\), the same polarization of R170_819, now
at each scale, gives

\[
 \Phi_\rho(F)+\mathcal E_\rho^{\rm int}
 =\Re e_{G_\rho F}^{(1)}(z_\rho)
  +(1-\rho)^{-1}\Re a_M(\delta_\rho,\mathcal R_\rho),              \tag{22}
\]

where \(\Phi_\rho(F)=\Re e_F^{(1)}(z_\rho)\). Averaged PC controls the
scaled form (8), not the fixed form (22). The exact difference is

\[
 e_{G_\rho F}^{(1)}(z_\rho)
 =e_{G_\rho F}^{(\rho)}(z_\rho)
  +\langle G_\rho F,(A_1-A_\rho)z_\rho\rangle .                    \tag{23}
\]

Integrating (22) and using (23) gives the complete port between the
averaged piece and the interior reserve:

\[
\boxed{
\begin{aligned}
 \int w(\rho)(\Phi_\rho+\mathcal E_\rho^{\rm int})\,d\rho
 ={}&\int w(\rho)\Re \chi_{G_\rho F}^{(\rho)}(g)\,d\rho\\
 &+\int w(\rho)\Re
   \langle G_\rho F,[A_\rho,S_\rho]U_\rho g\rangle\,d\rho\\
 &+\int w(\rho)\Re
   \langle G_\rho F,(A_1-A_\rho)z_\rho\rangle\,d\rho\\
 &+\int \frac{w(\rho)}{1-\rho}
    \Re a_M(\delta_\rho,\mathcal R_\rho)\,d\rho .
\end{aligned}}                                                     \tag{24}
\]

The first line expands exactly via the pointwise identity behind (8),
taking \(v=G_\rho F\) before integrating, and includes

\[
 \{\rho X,E_\rho\},\quad -L_\rho^*E_\rho,\quad
 -JH_\rho,\quad-H_\rho U_\rho,\quad
 -\langle S_\rho^*r,U_\rho g\rangle .                              \tag{25}
\]

The second line of (24) is the operator-order corrector that would be
missing if \(A_\rho S_\rho U_\rho\) and \(S_\rho A_\rho U_\rho\) were
confused. The third line contains the joint Gamma--primes corrector

\[
 A_1-A_\rho=m(D)-m(D/\rho)
 -(L_1+L_1^*)+(L_\rho+L_\rho^*),                                  \tag{26}
\]

and cannot be omitted nor separated by signs. The fourth line is the
alignment error with the interior flux. Thus (24) explicitly contains
\(X,U,E,H\), Tate, the order commutator, Gamma, primes, and primitivity
correctors. It is an interface, not the definition of a remainder as the
quantity one wishes to prove.

The potential advantage of (24) is that the isolated block
\(\langle H_\rho\rangle_w\) possesses (11)--(17). But the real collar in
(25) is \(\langle H_\rho U_\rho\rangle_w\), and moreover \(G_\rho F\),
\(U_\rho\) and \(E_\rho\) vary inside the integral. Hence (17) does not
establish compactness or a sign for the complete PC line. The interface
remains exact, but the compact gain has only been demonstrated for the
decoupled averaged tail.

## 6. Dilation generator and domain

For a function in the domain of the generator

\[
 \mathcal A=-\tfrac12-t\partial_t,
 \qquad \partial_\rho D_\rho F=\rho^{-1}D_\rho\mathcal AF,          \tag{27}
\]

integration by parts in \(\rho\) can transfer a derivative from
\(D_\rho F\) to the weight. But R170_819--821 does not prove
\(F\in\operatorname{Dom}\mathcal A\) for a general first-contact vector.
Hence (27) cannot be used to claim
\(D_\rho F-F=O(1-\rho)\) in the form norm.

For translations the situation is different:

\[
 \partial_\rho\tau_{a/\rho}
 =-a\rho^{-2}\partial_t\tau_{a/\rho},                              \tag{28}
\]

and the integration by parts leading to (11) transfers the derivative to
the weight at the level of the multiplier. That is why (12) holds for
every \(L^2\) datum, without a domain hypothesis on that datum. Averaging
the dilation orbit may also smooth with respect to its generator in a
separate spectral theory, but that does not imply physical regularity nor
remove the commutators with \(U\); it is not used here.

## 7. Result and next obligation

The construction contributes two facts that were previously absent:

1. every nontrivial arithmetic translation and the decoupled tail
   \(\overline H_{M,N,w}\) gain regularity under the average; their
   compression to the window is Hilbert--Schmidt. This is not extended
   here to the coupled product \(\langle H_\rho U_\rho\rangle_w\);
2. identity (24) connects that average, with Tate and all the
   correctors, to the reserve
   \(\int w(\rho)\mathcal E_\rho^{\rm int}d\rho\), which is nonnegative
   when \(w\ge0\). For a signed weight (24) remains exact, but that
   orientation is lost.

It also rules out a false exit: the average minus the base scale has norm
at least one and is not a uniformly small remainder. It has not been
proved that the right-hand side of (24) is nonpositive, nor that the
compressed compactness produces such a sign. The next piece must decide
whether the joint phase of the coupled collar admits an estimate on
\(F\in\ker H_T\), preserving the commutator of (24), (26), and the
alignment error; estimating each line of (24) by its absolute value would
again lose the cancellation that motivated PC.
