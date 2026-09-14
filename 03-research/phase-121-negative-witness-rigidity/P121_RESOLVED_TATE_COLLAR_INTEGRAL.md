# P121 -- exact evaluation of the Tate-collar current

## Status

This note evaluates the continuous Gamma collar integral and the finite
prime-power collar sum in closed form.  No positivity, spectral inverse or
asymptotic estimate is used.

The outcome is useful but sharply delimited.  The scalar collar current is
an ordinary pairing of the source with an explicit prime--Gamma potential.
That potential has nonzero jumps at the active prime-power seams and is not
in the two-dimensional Tate span.  Consequently the two Tate moment
conditions alone do not annihilate the current.  Any cancellation at first
contact must use the uncompressed equality equation, not merely evaluate
the collar integral.

## 1. Setup

Put `I_T=(-T,T)` and, for `sigma in {+1,-1}`, define

\[
 R_{\sigma,u}(F)=\int_{T-u}^{T}e^{\sigma t/2}F(t)\,dt,
 \qquad
 L_{\sigma,u}(F)=\int_{-T}^{-T+u}e^{\sigma t/2}F(t)\,dt.       \tag{1.1}
\]

The current obtained in
`P121_EXACT_TATE_COLLAR_LOCALIZATION.md` is

\[
\begin{aligned}
 J_\sigma(F)={}&\int_0^{2T}{e^{-u/2}\over1-e^{-2u}}
 \left(e^{\sigma u/2}R_{\sigma,u}(F)
      +e^{-\sigma u/2}L_{\sigma,u}(F)\right)du\\
 &+\sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
 \left(e^{\sigma\log(n)/2}R_{\sigma,\log n}(F)
      +e^{-\sigma\log(n)/2}L_{\sigma,\log n}(F)\right).
                                                               \tag{1.2}
\end{aligned}
\]

Introduce the two elementary tails

\[
 \begin{aligned}
 A_T(v)&:=\int_v^{2T}{du\over1-e^{-2u}}
 ={1\over2}\log {e^{4T}-1\over e^{2v}-1},\\
 B_T(v)&:=\int_v^{2T}{du\over2\sinh u}
 ={1\over2}\log {\tanh T\over\tanh(v/2)}.
 \end{aligned}                                                \tag{1.3}
\]

They are finite for `v>0` and have only logarithmic singularities at
`v=0`.  Those singularities are locally integrable against every
`L^2(I_T)` source.

For `x in R` write the finite right tails

\[
 \Theta_T(x):=\sum_{\substack{2\le n<e^{2T}\\ \log n\ge x}}\Lambda(n),
 \qquad
 H_T(x):=\sum_{\substack{2\le n<e^{2T}\\ \log n\ge x}}{\Lambda(n)\over n}.
                                                               \tag{1.4}
\]

Changing `>=` to `>` changes values only at finitely many points and hence
does not change any formula below.

## 2. Closed formula

### Theorem 2.1 -- resolved collar current

For every `F in L^2(I_T)`,

\[
 \boxed{J_+(F)=\int_{-T}^{T}e^{t/2}F(t)\,\Phi_{+,T}(t)\,dt}    \tag{2.1}
\]

where

\[
 \boxed{
 \Phi_{+,T}(t)=A_T(T-t)+B_T(T+t)
              +\Theta_T(T-t)+H_T(T+t).}                       \tag{2.2}
\]

Likewise,

\[
 \boxed{J_-(F)=\int_{-T}^{T}e^{-t/2}F(t)\,\Phi_{-,T}(t)\,dt}  \tag{2.3}
\]

with

\[
 \boxed{
 \Phi_{-,T}(t)=B_T(T-t)+A_T(T+t)
              +H_T(T-t)+\Theta_T(T+t)
              =\Phi_{+,T}(-t).}                               \tag{2.4}
\]

#### Proof

For the right Gamma collar in `J_+`, Fubini gives

\[
\begin{aligned}
 \int_0^{2T}{R_{+,u}(F)\over1-e^{-2u}}du
 &=\int_{-T}^{T}e^{t/2}F(t)
   \int_{T-t}^{2T}{du\over1-e^{-2u}}dt\\
 &=\int_{-T}^{T}e^{t/2}F(t)A_T(T-t)dt.             \tag{2.5}
\end{aligned}
\]

For the left Gamma collar,

\[
 \int_0^{2T}{L_{+,u}(F)\over2\sinh u}du
 =\int_{-T}^{T}e^{t/2}F(t)B_T(T+t)dt.              \tag{2.6}
\]

The prime coefficients at the two edges are exactly

\[
 {\Lambda(n)\over\sqrt n}e^{\log n/2}=\Lambda(n),
 \qquad
 {\Lambda(n)\over\sqrt n}e^{-\log n/2}={\Lambda(n)\over n}.  \tag{2.7}
\]

A point `t` belongs to the right collar of width `log n` precisely when
`log n >= T-t`, and to the left collar precisely when
`log n >= T+t`.  Interchanging the finite sum and the integral therefore
produces `Theta_T(T-t)` and `H_T(T+t)`.  This proves (2.1)--(2.2).
Replacing `+` by `-` exchanges the two elementary kernels and the two
arithmetic tails, proving (2.3)--(2.4).  QED.

Absolute Fubini is legitimate: the prime sum is finite, while the Gamma
potential has only endpoint logarithms, which belong to `L^2(I_T)`.

### Corollary 2.2 -- parity reduction

If `F(-t)=epsilon F(t)`, then

\[
 J_-(F)=\epsilon J_+(F),                             \tag{2.8}
\]

and the unique scalar current is

\[
 J_\epsilon(F)
 ={1\over2}\int_{-T}^{T}F(t)
 \left[e^{t/2}\Phi_{+,T}(t)
 +\epsilon e^{-t/2}\Phi_{+,T}(-t)\right]dt.         \tag{2.9}
\]

## 3. The integral does not collapse to the Tate moments

The continuous part of `Phi_(+,T)` is smooth in the open interval away
from the endpoint logarithms.  Its arithmetic part has the distributional
jumps

\[
 \Delta_{t=T-\log n}\Phi_{+,T}=\Lambda(n),
 \qquad
 \Delta_{t=\log n-T}\Phi_{+,T}=-{\Lambda(n)\over n},          \tag{3.1}
\]

with the obvious addition when two seam locations coincide.  In
particular, whenever an active prime power is present, `Phi_(+,T)` is not a
linear combination of `1` and `e^{-t}`.  Equivalently,

\[
 e^{t/2}\Phi_{+,T}(t)
 \notin \operatorname{span}\{e^{t/2},e^{-t/2}\}.              \tag{3.2}
\]

Therefore

\[
 M_+(F)=M_-(F)=0
 \quad\not\Longrightarrow\quad J_+(F)=J_-(F)=0.               \tag{3.3}
\]

This is not merely a dimension count.  Work in the real Hilbert space, let
`P_T` be the orthogonal projection off the Tate span, and put

\[
 F=P_T\bigl(e^{t/2}\Phi_{+,T}(t)\bigr).                        \tag{3.4}
\]

Then `F` is primitive, nonzero by (3.2), and

\[
 J_+(F)=\|F\|_2^2>0.                                           \tag{3.5}
\]

Thus resolving the integral proves exactly where the remaining information
must enter: a first-contact source is not an arbitrary primitive source.
One must use its full equality equation to force the pairing (2.1) to
vanish.  The evaluated integral itself supplies no such vanishing.

## 4. Exact substitution at first contact

If

\[
 \mathscr A_TF=\alpha e^{-t/2}+\beta e^{t/2},                  \tag{4.1}
\]

then the multiplier system becomes the completely explicit formula

\[
 \boxed{
 \begin{pmatrix}2T&2\sinh T\\2\sinh T&2T\end{pmatrix}
 \binom{\alpha}{\beta}
 =
 \binom{
 \langle e^{t/2}\Phi_{+,T},F\rangle
 }{
 \langle e^{-t/2}\Phi_{-,T},F\rangle
 }.}                                                           \tag{4.2}
\]

Consequently the collar integral has now been eliminated completely from
the first-contact problem.  The remaining exact statement is not an
integral evaluation but the special-source orthogonality

\[
 F\in\ker(P_T\mathscr A_TP_T)
 \quad\Longrightarrow\quad
 \langle e^{t/2}\Phi_{+,T},F\rangle=0.                         \tag{4.3}
\]

Equation (4.3) is equivalent to removal of the Tate forcing on the
first-contact branch.  It is not asserted by the calculation above.

## 5. Ledger

```text
continuous Gamma collar integral                  EVALUATED EXACTLY
finite prime-power collar sum                     EVALUATED EXACTLY
parity reduction                                  PROVED
Tate moments alone kill the current               FALSE (explicit witness)
first-contact equation kills the resolved current OPEN: equation (4.3)
global square / row (d)                           OPEN
```
