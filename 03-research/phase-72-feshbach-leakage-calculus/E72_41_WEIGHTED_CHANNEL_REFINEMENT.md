# E72.41 -- Weighted channel refinement

**Date:** 2026-07-08.
**Role:** correct the too-strong uniform channel target from E72.40.

## 0. Numerical check

For the effective channel ratio

```text
|<v_s,T_nk>| / (n^(-1/2)tau_n),
tau_n=(log x-log n)/log x,
```

the maximum does not show `x^(-1/2)` decay:

```text
x=64:   max=3.44e-1, median=8.11e-2
x=100:  max=4.35e-1, median=5.02e-2
x=144:  max=4.65e-1, median=4.53e-2
x=196:  max=4.52e-1, median=3.34e-2
```

The median is compatible with half-power decay, but the maximum is not. Therefore a uniform channel
bound is too strong.

## 1. Correct norm

The scalar WRL transform does not need a uniform bound. It needs the weighted sum:

```text
N_x(s;z)=sum (n/x)^z <v_s,T_nk>.
```

Thus the correct dual norm is:

```text
||v_s||_{EWFT,K}
 := sup_{z in K}
    |sum (n/x)^z <v_s,T_nk>|.
```

Endpoint taper and Cauchy weighting may suppress a sparse set of large channel ratios.

## 2. Weighted channel theorem

### Theorem 72.41

Assume the post-main/model subtraction has been performed. If for every compact `K` in `Re z>1/2`,

```text
sup_{z in K}
|sum_{n<=x} (n/x)^z <v_{x,s},T_{x,n}k_x>| -> 0  (WCB)
```

on the two Cauchy heights, and the same holds after `partial_s`, then scalar WRL resonance
annihilation follows.

### Proof

This is exactly the normalized scalar resonance expression from E72.37/E72.31 after model-main
subtraction. The derivative statement supplies the current convergence required by E72.30. `QED`

## 3. Why this is better

`(WCB)` is not an absolute-value estimate. It preserves:

```text
oscillation of cells,
endpoint taper,
Cauchy compression,
Feshbach centering.
```

It matches the numerical signal: the normalized sum is small even though the maximum channel ratio is
not.

## 4. New target

### Weighted endpoint Weyl-Feshbach cancellation

Prove `(WCB)` directly from the finite CCM/prolate structure.

This is now the sharp scalar estimate:

```text
not sup_n channel small,
but endpoint-weighted coherent channel sum small.
```

## 5. Status

```text
falsified: uniform half-power channel bound;
survives:  weighted coherent endpoint channel bound;
open:      prove WCB.
```

The next step is to express `(WCB)` as a matrix element of an explicit endpoint-weighted cell operator.
