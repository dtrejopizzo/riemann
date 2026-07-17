# E72.47 -- Fourier overlap bound for the continuous endpoint operator

**Date:** 2026-07-08.
**Role:** remove the dimension-loss obstruction in E72.46 by using the Fourier-overlap structure of
the CCM cells.

## 0. Overlap representation

Let `E_N` be the finite Fourier subspace on `[0,L]` used by the Phase 71 CCM matrix. The cell matrix

```text
Q_x(y)=(q_{mn}(y))_{|m|,|n|<=N}
```

is the matrix of the even overlap/translation form:

```text
q_{mn}(y)=<e_m, A_y e_n>_{[0,L]},
```

where `A_y` is the symmetrized shift-overlap operator supported on the overlap interval of length
`L-y`.

Equivalently:

```text
A_y = R_y^*R_y + R_yR_y^*
```

up to the harmless even normalization used in `make_q`, with `R_y` the restriction/translation between
the two overlapping subintervals.

This representation gives the exact formulas used in Phase 71:

```text
q_nn(y)=2(1-y/L)cos(2*pi*n*y/L),
q_mn(y)= [sin(2*pi*m*y/L)-sin(2*pi*n*y/L)]/[pi(n-m)].
```

## 1. Operator norm bound

### Lemma 72.47

For every `0<=y<=L`,

```text
||Q_x(y)||_{E_N->E_N} <= 2(1-y/L).               (FOB)
```

### Proof

The operator `R_y` is restriction to an interval of length `L-y`, followed by translation. On normalized
Fourier modes, its Hilbert-space norm is bounded by the square root of the relative overlap length:

```text
||R_y|| <= ((L-y)/L)^(1/2).
```

Therefore:

```text
||R_y^*R_y|| <= (L-y)/L,
||R_yR_y^*|| <= (L-y)/L.
```

Since `Q_x(y)` is the symmetrized overlap matrix,

```text
||Q_x(y)|| <= ||R_y^*R_y||+||R_yR_y^*||
            <= 2(1-y/L).
```

`QED`

This is the operator version of the endpoint taper from E72.38. Crucially, it has no dimension factor.

## 2. Continuous endpoint operator norm

Recall:

```text
S_x^{cont}(z)
 = int_0^L exp(z(y-L))e^(-y/2)Q_x(y)dy.
```

For `sigma=Re z>1/2`, using `(FOB)` and `r=L-y`,

```text
||S_x^{cont}(z)||
 <= 2x^(-1/2) int_0^L exp(-(sigma-1/2)r) r/L dr
 <= 2x^(-1/2)/(L(sigma-1/2)^2).                 (CEO)
```

Thus:

```text
||S_x^{cont}(z)|| -> 0
```

uniformly on compact subsets of `Re z>1/2`.

## 3. Consequence

For bounded compressed Cauchy channel vectors `v_{x,s}` and normalized `k_x`,

```text
|<v_{x,s},S_x^{cont}(z)k_x>|
 <= ||v_{x,s}|| ||S_x^{cont}(z)|| ||k_x||
 -> 0
```

provided:

```text
||v_{x,s}|| = o(x^(1/2)L)
```

uniformly on the two Cauchy heights. This is far weaker than the earlier pointwise channel target.

## 4. What remains

The continuous model endpoint contribution is controlled. The only remaining endpoint scalar WRL
problem is the discrepancy operator:

```text
S_x^{disc-err}(z)
 = int_1^x (u/x)^z u^(-1/2)Q_x(log u)dE(u).
```

The same overlap bound reduces it to a scalar Chebyshev-discrepancy estimate with the endpoint taper.

## 5. Status

```text
proved: Fourier overlap bound ||Q_x(y)|| <= 2(1-y/L);
proved: continuous endpoint operator norm is O(x^-1/2/L);
open:   prove the endpoint-tapered discrepancy operator is small in the scalar compressed channel.
```

This closes the geometric/model half of endpoint scalar WRL.
