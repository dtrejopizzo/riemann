# P76.038 - Unconditional high-zero tail bound

Let

```text
X(z)=Xi(1/2+iz).
```

Pair the zeros of `X` using the functional equation and conjugation.  For
`sigma` in a compact subset of `(1/2,infinity)`, the contribution to

```text
d/dsigma log X(-i sigma)^2
```

from zero quartets whose ordinates have magnitude greater than `R` is

```text
O_K(log R/R).                                   (HT-1)
```

This estimate is unconditional; it does not assume that the zeros are real
in the `z` coordinate.

## Proof

Every nontrivial zeta zero has `0<Re(rho)<1`.  After pairing the Hadamard
terms under `rho`, `1-rho`, `conj(rho)`, and `1-conj(rho)`, the constant and
linear pieces cancel and a quartet with ordinate `gamma` contributes

```text
O_K((1+gamma^2)^(-1)).
```

The unconditional Riemann--von Mangoldt estimate gives

```text
N(T)=O(T log T).
```

Partial summation therefore yields

```text
sum_{|gamma|>R} O_K(gamma^(-2))
 =O_K(int_R^infinity (log t)/t^2 dt)
 =O_K(log R/R).
```

This proves `(HT-1)`.

## Consequence for the core trace

Put `R_{L,N}=2*pi*N/L`.  Under `N/L -> infinity`, the high target tail is
`o_K(1)`.  Hence `CORE-SR-LOG` reduces to the finite-window statement

```text
CELL-TRACE-WINDOW:
core Schur quotient trace below R_{L,N}
 - completed-zeta trace below R_{L,N}
 ->0                                             (HT-2)
```

locally uniformly for `s>1`.

The high tail is therefore closed independently of RH.  The sole remaining
load-bearing step is `(HT-2)`, to be proved without inserting a zero list by
the finite Gamma-prime cell identity.
