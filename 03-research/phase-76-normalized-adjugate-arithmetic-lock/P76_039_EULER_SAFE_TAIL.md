# P76.039 - Euler-safe prime-power tail

Let `x=lambda^2=e^L`.  For every `delta>0`, uniformly on compact subsets of
`Re(s)>=1+delta`,

```text
sum_{n>x} Lambda(n)n^(-s)=O_delta(x^(-delta))
                         =O_delta(exp(-delta L)).   (ET-1)
```

## Proof

Write `psi(t)=sum_{n<=t}Lambda(n)`.  The Chebyshev bound `psi(t)=O(t)` is
sufficient; no prime number theorem or zero-free region is needed.  Partial
summation gives, with `sigma=Re(s)>=1+delta`,

```text
|sum_{n>x}Lambda(n)n^(-s)|
 <=x^(-sigma)psi(x)
   +|s| int_x^infinity psi(t)t^(-sigma-1)dt
 =O_K(x^(1-sigma))
 =O_K(x^(-delta)).
```

The estimate is locally uniform because `|s|` is bounded on each compact.

Consequently

```text
-sum_{n<=lambda^2}Lambda(n)n^(-s)
 -> zeta'(s)/zeta(s)                             (ET-2)
```

locally uniformly in `Re(s)>1`.

## Effect on the closure ledger

The prime-power tail estimate is theorem-grade and independent of RH.
However P76.040 falsifies the following proposed finite cell-to-Schur
transfer, so it is displayed only as an autopsied statement:

```text
CELL-TRACE:
core Schur logarithmic derivative
= arch_gamma(s)-2 sum_{n<=lambda^2}Lambda(n)n^(-s)
  + finite-section error,

finite-section error ->0 for N/L -> infinity.   (ET-3)
```

`(ET-3)` must not be used.  The exact cell-smoothed Schur symbol has to be
derived before any Euler-tail estimate is attached to it.
