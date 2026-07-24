# Single Laguerre bulk \(L^1\) obstruction

## Purpose

`219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md` reduces the absolute
diagonal load to one high-degree Laguerre polynomial:
\[
  \int_{T_8}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du
\]
plus two fixed low-cutoff correction intervals.

This note audits that sharper absolute route for canonical
Vinogradov--Korobov type envelopes.  The conclusion is negative: the
collapsed single-Laguerre absolute load is exponentially large in the bulk
\(u\asymp n\), while the VK relative envelope has only subexponential decay
there.  Hence the absolute \(L^1\) route with a VK envelope cannot dominate
the collapsed load by the quadratic budget \(\mathcal B_n\).

This does not disprove A1.  It shows that the proof must use arithmetic
sign, a one-sided tail theorem, a strong-margin theorem, or a much stronger
non-VK envelope.

## Bulk Laguerre lower scale

Use the standard Plancherel--Rotach bulk asymptotic for fixed
\(\alpha=2\).  For any compact interval
\[
  0<a<b<4,
\]
there are constants \(c_{a,b}>0\) and \(N_{a,b}\) such that, for
\(N\ge N_{a,b}\),
\[
\boxed{
  \int_{aN}^{bN}|L_N^{(2)}(u)|\,du
  \ge
  c_{a,b}\,N^{-K_{a,b}}e^{aN/2}
}
\tag{1}
\]

Here \(K_{a,b}\) is fixed.  The exact power of \(N\) is irrelevant here.
What matters is the
exponential factor \(e^{u/2}\) in the Laguerre bulk.  The absolute value
prevents cancellation between oscillatory lobes.

Taking \(N=n-1\), and for instance \(a=2\), \(b=3\), gives
\[
\boxed{
  \int_{2(n-1)}^{3(n-1)}|L_{n-1}^{(2)}(u)|\,du
  \ge c\,n^{-K}e^{n+O(1)}.
}
\tag{2}
\]

## The bulk interval lies inside the collapsed range

For the canonical VK cutoffs of `208`,
\[
  T_n\asymp n^{5/3}(\log n)^2.
\tag{3}
\]

Therefore, for all sufficiently large \(n\),
\[
\boxed{
  T_8<2(n-1)<3(n-1)<T_n.
}
\tag{4}
\]

Thus the bulk interval in (2) is contained in the collapsed single-Laguerre
range \((T_8,T_n)\) from `219`.

## VK relative decay is subexponential in the bulk

A VK-type relative envelope has the form
\[
  \varepsilon(u)=A\exp(-\eta(u)),
\]
with
\[
  \eta(u)=O(u^\theta(\log u)^q)
  \qquad(0<\theta<1)
\tag{5}
\]
on dyadic \(u\)-ranges.  In the classical VK scale, \(\theta=3/5\), with a
logarithmic correction.

On
\[
  2(n-1)\le u\le3(n-1),
\]
this gives
\[
\boxed{
  \varepsilon(u)
  \ge
  A\exp(-C n^\theta(\log n)^q)
}
\tag{6}
\]
for some fixed \(C\).

Combining (2) and (6),
\[
\boxed{
\begin{aligned}
  \int_{T_8}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du
  &\ge
  A c\,n^{-K}
  \exp\!\left(n-C n^\theta(\log n)^q+O(1)\right).
\end{aligned}
}
\tag{7}
\]

Since \(\theta<1\), the right side is exponential in \(n\).

## Budget comparison

The base budget has only quadratic scale:
\[
  \mathcal B_n=\Gamma_{\mathcal B}n^2+O(n\log n),
\tag{8}
\]
from `210`.  After `217` and `215`,
\[
  \Gamma_{\mathcal B}>25/64,
\]
but this positive sign does not change the order:
\[
\boxed{
  \mathcal B_n=O(n^2).
}
\tag{9}
\]

Equations (7)--(9) imply
\[
\boxed{
  \int_{T_8}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du
  >
  \mathcal B_n
}
\tag{10}
\]
for all sufficiently large \(n\), for every fixed VK-type envelope of the
form (5).

Therefore the absolute theorem
\[
  \mathcal B_n\ge W_n(\varepsilon)
\]
cannot hold with a VK relative envelope.

## Interpretation

The failure comes from taking absolute values.  In the signed compact
pairing, the oscillatory bulk of \(L_{n-1}^{(2)}\) can cancel against the
arithmetic sign structure of \(E(e^u)\).  In the absolute route, that
cancellation is discarded, and the Laguerre bulk \(e^{u/2}\) overwhelms
subexponential PNT decay.

Thus `219` simplifies the kernel, but it also reveals that a VK-based
absolute \(L^1\) proof is too expensive.

## Remaining viable routes

After this obstruction, the viable A1 routes are:

1. a direct signed compact proof, for example the finite certificate of
   `190`;
2. a one-sided tail theorem stronger than A0, preserving sign;
3. the strong-margin theorem
   \[
     \lambda_n\ge {1\over2}\lambda_n^{\rm arch};
   \]
4. a comparative Loewner--Schur theorem that proves the required positivity
   before reading off the diagonal;
5. a global half-plane theorem equivalent to RH.

The absolute route could still be resurrected only with an envelope having
bulk decay at least \(e^{-u/2}\) on \(u\asymp n\).  Such an envelope is far
stronger than VK and is essentially of RH-strength in this context.

## Status

Closed as a scale obstruction for the collapsed absolute \(L^1\) route
with canonical VK-type PNT envelopes.

A1 remains open.  The absolute VK route is no longer viable; the phase must
return to a signed proof, one-sided tail, strong margin, comparative
Loewner--Schur, or global half-plane theorem.
