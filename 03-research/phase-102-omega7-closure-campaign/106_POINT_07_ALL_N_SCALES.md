# Point 07 - All scales in n

## Required coverage

The proof of the infinite range must cover:

- the first indices after \(7\);
- the Laguerre transition region;
- the oscillatory region \(\log m\lesssim 4n\);
- the far tail;
- the limit \(n\to\infty\).

## What A0 covers

A0 covers the far tail for every fixed \(n\ge8\), with a cutoff \(T_n\)
chosen by the explicit inequality
\[
  C_0B_n
  \int_{T_n}^\infty(1+t)^{n-1}\exp(-\eta(t))\,dt
  \le {1\over4}\lambda_n^{\rm arch}.
\]
This includes the boundary regulator uniformly in
\(\varepsilon\in[0,1]\). Thus the far-tail part of point 07 is closed.

## What remains

The core interval \([1,e^{T_n}]\) still contains all delicate scales:
\[
  0\le \log y\le T_n .
\]
The current phase has not produced a theorem that proves
\[
  -n+\int_1^{e^{T_n}}E(y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{\rm arch}
  \qquad(n\ge8).
\]

Therefore point 07 is reduced but not closed. Its remaining content is
identical to A1: a single signed inequality valid for all \(n\ge8\).

## No-go constraint

A proof that handles only \(n\le N\), or only an asymptotic subsequence,
does not close point 07. It may be useful as a certificate block, but Li
requires every index.
