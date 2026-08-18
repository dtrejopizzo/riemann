# D.123 — Sharp primitive Paley--Wiener evaluation and the dyadic deficit

## Verdict

The reproducing kernel of the Paley--Wiener space supported in \([-T,T]\),
after imposing the two Tate zeros \(\widehat F(\pm i/2)=0\), is explicit.
At real frequency zero its sharp squared evaluation norm is

\[
 C_0(T)=2T-{16\sinh^2(T/2)\over\sinh T+T}
       =2T-8+O(Te^{-T}).                                  \tag{0.1}
\]

Thus the two primitive conditions remove only an asymptotically constant
amount from the coherent zero-frequency channel; they do not yield a
factor decreasing with \(T\).

The Gamma multiplier is quadratic at zero.  On the natural band
\(|\tau|\lesssim1/T\), Gamma strength is \(O(T^{-2})\), while a dyadic
contact block has coherent strength \(W_Y\).  With
\(T\asymp\frac12\log Y\), direct Gamma domination misses by the factor

\[
 W_YT^2,                                                   \tag{0.2}
\]

which has the expected size \(\sqrt Y(\log Y)^2\) under Chebyshev-scale
contact mass.  Hence sharp Paley--Wiener uncertainty does not repair the
dyadic batching obstruction.  Earlier arithmetic blocks must enter the
Schur capacity essentially.

## 1. Exact primitive reproducing kernel

Let \(H_T=L^2([-T,T])\) and

\[
 h_-(t)=e^{-t/2},\qquad h_+(t)=e^{t/2}.                  \tag{1.1}
\]

The primitive space is

\[
 \mathcal P_T=\{F:\langle F,h_-\rangle
                    =\langle F,h_+\rangle=0\}.          \tag{1.2}
\]

Its moment Gram matrix is

\[
 G_T=\begin{pmatrix}2\sinh T&2T\\2T&2\sinh T\end{pmatrix}. \tag{1.3}
\]

For \(e_\tau(t)=e^{i\tau t}\), put

\[
 b_T(\tau)=
 \begin{pmatrix}\langle h_-,e_\tau\rangle\\
                 \langle h_+,e_\tau\rangle\end{pmatrix}. \tag{1.4}
\]

If \(P_T\) is orthogonal projection onto \(\mathcal P_T\), the exact RKHS
kernel is

\[
 \boxed{
 K_T(\tau,\sigma)
 =\langle e_\sigma,e_\tau\rangle
  -b_T(\tau)^*G_T^{-1}b_T(\sigma).}                     \tag{1.5}
\]

Indeed \(P_T=I-H_TG_T^{-1}H_T^*\), where
\(H_T(a,b)=ah_-+bh_+\).  Thus (1.5) is simply
\(\langle P_Te_\sigma,P_Te_\tau\rangle\), and

\[
 |\widehat F(\tau)|^2\le K_T(\tau,\tau)\|F\|^2         \tag{1.6}
\]

is sharp for every \(\tau\).

## 2. Exact zero-frequency constant

At \(\tau=0\),

\[
 b_T(0)=4\sinh(T/2)\binom11.                            \tag{2.1}
\]

The vector \((1,1)\) is an eigenvector of \(G_T\) with eigenvalue
\(2(\sinh T+T)\).  Substitution into (1.5) gives

\[
 \boxed{
 K_T(0,0)=C_0(T)
 =2T-{16\sinh^2(T/2)\over\sinh T+T}.}                  \tag{2.2}
\]

Using \(2\sinh^2(T/2)=\cosh T-1\),

\[
 {16\sinh^2(T/2)\over\sinh T+T}
 =8+O(Te^{-T}),                                         \tag{2.3}
\]

which proves (0.1).  In particular,

\[
 {C_0(T)\over2T}\longrightarrow1.                     \tag{2.4}
\]

The primitive projection becomes asymptotically ineffective at controlling
ordinary mean.

## 3. A source family showing the low-frequency scale

Choose \(u\in C_c^\infty((-1,1))\) with nonzero integral and set

\[
 u_T(t)=T^{-1/2}u(t/T),
 \qquad
 F_T=(\partial_t^2-\tfrac14)u_T.                        \tag{3.1}
\]

Integration by parts gives

\[
 \widehat F_T(\pm i/2)=0,                               \tag{3.2}
\]

so \(F_T\in\mathcal P_T\).  Moreover

\[
 \widehat F_T(\tau)=-(\tau^2+	frac14)
                     T^{1/2}\widehat u(T\tau).          \tag{3.3}
\]

Thus a fixed positive fraction of its Fourier mass lies in a band
\(|\tau|\le c/T\), while

\[
 |\widehat F_T(0)|^2
 ={T\over16}|\widehat u(0)|^2.                          \tag{3.4}
\]

This realizes the linear scale in (2.2) without violating either Tate
condition.

## 4. Gamma has only quadratic strength on this band

The Gamma symbol is

\[
 \ell_\infty(\tau)
 =\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4).        \tag{4.1}
\]

Taylor expansion gives

\[
 \ell_\infty(\tau)
 =c_\infty\tau^2+O(\tau^4),
 \qquad
 c_\infty=-{1\over8}\psi''(1/4)>0.                    \tag{4.2}
\]

Consequently, on \(|\tau|\le c/T\),

\[
 \ell_\infty(\tau)\le {C_c\over T^2}.                 \tag{4.3}
\]

The family (3.1) therefore has low-band Gamma energy smaller by a factor
\(T^{-2}\) than its low-band \(L^2\) mass.  Equivalently, the sharp Gamma
energy norm of zero evaluation grows at least on the order of \(T^3\): one
factor \(T\) from (3.4) and two from the inverse quadratic symbol.

## 5. Insertion into a dyadic contact block

For \(Y<n\le2Y\), the centered multiplier is

\[
 k_Y(\tau)=2\sum w_n\cos(\tau\log n),
 \qquad W_Y=\sum w_n.                                   \tag{5.1}
\]

For \(|\tau|\le c/T\) and \(T=\frac12\log(2Y)\), choosing a fixed small
\(c>0\) gives

\[
 \cos(\tau\log n)\ge\cos(2c)>0.                        \tag{5.2}
\]

Hence

\[
 k_Y(\tau)\ge2\cos(2c)W_Y                              \tag{5.3}
\]

throughout that band.  Comparing (5.3) with (4.3), any direct Loewner
constant must satisfy

\[
 C_Y\gg W_YT^2.                                         \tag{5.4}
\]

There is therefore no uniform Gamma absorption.  Elementary Chebyshev
bounds give the upper scale \(W_Y=O(\sqrt Y)\); whenever a block has the
corresponding lower scale, (5.4) is of order
\(\sqrt Y(\log Y)^2\).  The exact statement (5.4) does not require a lower
prime asymptotic: it quantifies the deficit in terms of the actual
source-derived block mass \(W_Y\).

## 6. Why prolate optimization cannot change the exponent

Replacing (3.1) by the top prolate vector optimizes the fraction of Fourier
mass in \([-c/T,c/T]\).  Under the scaling \(t=Tx\), the time--bandwidth
product is the fixed number \(c\), so the top concentration eigenvalue is a
positive constant independent of \(T\).  It can improve the constant in
(5.4), but not the factor \(T^2\).

Likewise the exact RKHS kernel (1.5) already gives the optimal pointwise
constant.  Its asymptotic (2.4) proves that no sharper Paley--Wiener
inequality based solely on the two Tate zeros can provide a decaying factor
at frequency zero.

## 7. Conclusion

The sharp uncertainty calculation closes the coherent-channel audit:

\[
 \boxed{
 \|\operatorname{ev}_0\|_{\mathcal P_T}^2
 =2T-8+o(1),
 \qquad
 \ell_\infty(\tau)\asymp\tau^2.}
\]

Thus the two jets do not suppress the dyadic zero-frequency contact, and
Gamma is weakest precisely there.  Direct dyadic absorption loses the
factor \(W_YT^2\).

The only remaining multiscale possibility is the joint Schur complement in
which earlier arithmetic contacts alter the low-frequency capacity.  Sharp
Paley--Wiener, prolate concentration and Gamma alone cannot prove its sign.

