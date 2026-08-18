# D.208 — Flat-order-60 full-multiplier tail at `log(6)/2`

## Scope

This note certifies only the Legendre output tail after row 600 on the
source-defined safe space

\[
 S=\{(T^2-t^2)^{60}P(t):\deg P\le79\}\cap\ker J_+\cap\ker J_-.
\]

It does not replace the finite three-block Schur complement.

## Full-line reduction

Let `E_T` be zero extension and `P_T` restriction to `(-T,T)`.  For the
completed local action at `2T=log 6`,

\[
 A_T=P_TM_{W_T}E_T,
\]

where

\[
 W_T(\tau)=\Re\psi(1/4+i\tau/2)-\log\pi
 -2\sum_{n=2,3,4,5}{\Lambda(n)\over\sqrt n}
          \cos(\tau\log n).
\]

Translations by `log n >= 2T` have disjoint interiors and therefore do not
enter `W_T`.  Thus this single multiplier includes the complete Gamma term,
the constant mass, and exactly the four active contacts (including `4=2^2`).

Since every source in `S` has zero endpoint jets through order 59,

\[
 \widehat {E_TF}(\tau)=(i\tau)^{-60}\widehat {E_TF^{(60)}}(\tau).
\]

Consequently, with the Fourier convention used in D.161,

\[
 \int_{-T}^T(1-t^2/T^2)^{60}|(A_TF)^{(60)}|^2dt
 \le {1\over2\pi}\int_{\mathbb R}
 |\tau|^{120}|W_T(\tau)|^2|\widehat F(\tau)|^2d\tau.       \tag{1}
\]

This avoids the catastrophic cancellation produced by separately
differentiating the interior and endpoint pieces of the Hurwitz expansion.

## Explicit split

The shifted-digamma recurrence through 20, the elementary remainder bound
in the right half-plane, `log(pi)`, and the four finite contacts give the
deliberately rounded real-axis estimate

\[
 |W_T(\tau)|\le \log(|\tau|+21)+31.                       \tag{2}
\]

For `|tau| <= R`, Plancherel bounds (1) by

\[
 (\log(R+21)+31)^2\|F^{(60)}\|_2^2.                      \tag{3}
\]

One more integration by parts gives

\[
 |\widehat F(\tau)|\le {A(F)\over|\tau|^{61}},\qquad
 A(F)=|F^{(60)}(T)|+|F^{(60)}(-T)|
      +\sqrt{2T}\|F^{(61)}\|_2.                          \tag{4}
\]

For `tau >= R`, put `C_R=31+log(1+21/R)`.  Direct integration yields

\[
 \int_R^\infty{(\log\tau+C_R)^2\over\tau^2}d\tau
 ={(\log R+C_R)^2+2(\log R+C_R)+2\over R}.              \tag{5}
\]

Equations (3)--(5), including both half-lines, are exactly the bound
implemented by `114_d_208_t6_flat60_plancherel_tail_arb.py`.

## Directed linear algebra

All derivative norms and endpoint values are evaluated in the Legendre
basis with Arb balls.  D.207 supplies a frozen congruence `P` and proves

\[
 P^*B P\ge gI,
\]

by directed Gershgorin.  Therefore the largest normalized derivative Gram
is at most the sum of the 78 diagonal bounds divided by `g`.  Finally D.205
gives

\[
 \|R_{600}A_TSB^{-1/2}\|^2
 \le {540!\over660!}T^{120}J_{60}.
\]

The script requires the resulting upper endpoint to be below `0.05`; no
sampled derivative or floating-point singular value is used for that sign.
