# E72.75 -- Even coborder certificate for EV-CERT

**Date:** 2026-07-08.
**Role:** rewrite the even-sector HPAC residual as a Weyl pairing with one shorted source vector.

## 0. Source vector

For a finite root `tau_j` of `P_x`, define:

```text
S_j := 2tau_j(tau_j^2I-D^2)^(-1),
r_j := (tau_jI-D)^(-1)1,
E_j := exp(i tau_j L),
h_x := k_x-xi_x.
```

E72.74 gives:

```text
F_x(s;tau_j)/alpha_j
 = i <v_even,S_j k_x>
   -(E_j-1)/L <v_even,S_j1><r_j,h_x>.
```

Define the even HPAC source:

```text
W_j := i S_j k_x - (E_j-1)/L S_j1 <r_j,h_x>.                    (W)
```

Then:

```text
F_x(s;tau_j)/alpha_j = <v_even,W_j>.                            (W-F)
```

Only the projection of `W_j` to the `k_x`-complement matters.

## 1. Shorted coborder form

Let:

```text
Q=I-k_xk_x^T,
C=Q(H_x-mu_x^0I)Q,
r_s^even=s(s^2I-D^2)^(-1)1.
```

Since:

```text
v_even=C_even^(-1)Q r_s^even,
```

we get the exact dual identity:

```text
F_x(s;tau_j)/alpha_j
 = <Q r_s^even, C_even^(-1)Q W_j>.                              (COB)
```

Thus EV-CERT is equivalent to Weyl invisibility of the shorted source:

```text
u_j:=C_even^(-1)QW_j.                                            (U)
```

## 2. Finite certificate

For compact height windows and the two Cauchy heights, define:

```text
R_x^{even}(K)
 := max_{tau_j in K, P_x(tau_j)=0}
    sup_s |<Q r_s^even, u_j>|.
```

Then:

```text
R_x^{even}(K)->0                                                 (EVC)
```

with one `s`-derivative implies `EV-CERT`, hence HPAC-DIV, hence scalar WRL resonance annihilation by
E72.68--E72.70.

## 3. Why this is the right norm

The raw source `QW_j` need not be small. The Phase 72 mechanism is the same as E72.3--E72.4:

```text
raw source  -> may be large,
shorted source C^(-1)QW_j -> relevant,
Weyl pairing of shorted source -> actual current certificate.
```

So the target is not:

```text
||QW_j|| -> 0.
```

It is:

```text
<Q r_s^even,C^(-1)QW_j> -> 0
```

on the two current-generating Cauchy heights.

## 4. Numerical signal

In the current finite harness, `||QW_j||` is not small, but the shorted Weyl pairing is much smaller.
Representative values at `s=10+0.2i`:

```text
lambda=8:
  tau=0.728  ||QW||=1.675e0  ||C^-1QW||=3.107e-1  |weyl|=1.905e-2
  tau=2.708  ||QW||=9.100e-1 ||C^-1QW||=1.681e-1  |weyl|=1.373e-2

lambda=12:
  tau=0.825  ||QW||=1.167e0  ||C^-1QW||=1.329e-1  |weyl|=3.091e-3
  tau=3.221  ||QW||=3.547e-1 ||C^-1QW||=4.039e-2  |weyl|=4.162e-4

lambda=20:
  tau=1.856  ||QW||=8.031e-1 ||C^-1QW||=5.042e-2  |weyl|=5.553e-4
  tau=4.351  ||QW||=7.553e-1 ||C^-1QW||=4.743e-2  |weyl|=2.346e-3
```

This supports the reduced-current nature of the certificate and warns against raw norm estimates.

## 5. Status

```text
proved: EV-CERT is exactly the Weyl pairing (COB) with u_j=C_even^(-1)QW_j;
reduced: HPAC divisibility to the Even Coborder Certificate (EVC);
open:   prove EVC from the finite even-sector Feshbach equation.
```
