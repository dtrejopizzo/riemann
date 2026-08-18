# D.76 — Gamma-tail domination by one Robin channel

## The exact operator inequality

For (b>0), let

\[
 \mathcal E_b(F)=\int_0^\infty e^{-br}\|F-S_rF\|_2^2\,dr.
\]

After zero extension and Plancherel its multiplier is

\[
 e_b(\tau)={2\tau^2\over b(b^2+\tau^2)}.
\]

If (b\ge B>0), then

\[
 {e_b(\tau)\over e_B(\tau)}
 ={B(B^2+\tau^2)\over b(b^2+\tau^2)}
 \ge \left({B\over b}\right)^3.                 \tag{1}
\]

Indeed, after clearing positive denominators, the difference is
proportional to

\[
 B\tau^2(b^2-B^2)\ge0.
\]

Hence (1) is an operator inequality on every support window, with no
discretization:

\[
 \mathcal E_b\ge(B/b)^3\mathcal E_B.             \tag{2}
\]

For the Gamma parameters (b_j=2j+1/2), retain the channels (j<N) and
put (B=b_N).  Monotonicity gives

\[
 \sum_{j=N}^\infty b_j^{-3}
 \ge\int_N^\infty(2x+1/2)^{-3}\,dx={1\over4B^2}.
\]

Combining this with (2) proves the closed tail estimate

\[
 \boxed{\sum_{j=N}^\infty\mathcal E_{b_j}
 \ge {B\over4}\mathcal E_B.}                    \tag{3}
\]

All infinitely many omitted Gamma channels are therefore replaced by one
explicit exponential-resolvent channel.

## Parity and primitive use

On ([-T,T]), the eigenvalues of the kernel
(K_B(x,y)=e^{-B|x-y|}) are the Robin eigenvalues already derived in D.59.
Thus:

* on the odd channel, (3) contributes at least
  ((B/4)d_{B,o}\|F\|^2);
* on the even primitive channel
  (langle F,\cosh(t/2)\rangle=0), it contributes at least
  ((B/4)d_{B,e}\|F\|^2), with (d_{B,e}) given by the two-level angle
  formula D.59(5.8).

The second bound is deliberately asserted only on the exact primitive
subspace.  This is sufficient for nested-window propagation because zero
extension preserves both Tate moments.

At (T=\log3/2), the midpoint values for (N=80), (B=160.5), are

\[
 {B\over4}d_{B,e}\approx1.1587\,10^{-3},\qquad
 {B\over4}d_{B,o}\approx6.199\,10^{-4}.            \tag{4}
\]

These decimals are diagnostics, not the directed proof.  The proof of
(3) is exact; a final endpoint certificate must enclose the Robin roots in
(4) and combine them with an Arb enclosure of the first (N) channels.

## Scope

This theorem removes the infinite Gamma-tail truncation from the
(T=\log3/2) problem.  It does not by itself certify the finite first-80
block or row D globally.
