# E72.112 -- Shorted pushforward bound

**Date:** 2026-07-09.
**Role:** isolate the operator estimate that would prove the finite-frequency energy bound.

## 0. From frequency data to centered flux

E72.111 writes:

```text
Y_x(tau) -> Z_x^{pm}(tau) -> c_{x,H}^{pm}(tau)
          -> phi_{x,H,tau}^{pm} -> centered flux.
```

Package this as one finite operator:

```text
R_{x,H,tau}
 := T_HP_H^0W_HB_xC_E^(-1)B_x^*P_H
    (2/(L sqrt(x)))L_{k_x,tau},                              (R)
```

where `L_{k_x,tau}` maps the frequency packet `Y_x(tau)` to `K_x^E(tau)k_x`.

Then:

```text
Flux_x(H,tau)=||R_{x,H,tau}Y_x(tau)||_2.
```

Similarly, define the mass functional:

```text
m_{x,H,tau}
 := 1_H^TW_HB_xC_E^(-1)B_x^*P_H(2/(L sqrt(x)))L_{k_x,tau}.
```

Then:

```text
Mass_x(H,tau)=m_{x,H,tau}Y_x(tau).
```

## 1. Finite operator criterion

### Theorem 72.112

Fix `H` and a finite root-height window `T`.  Suppose:

```text
sup_{tau_j<=T} ||R_{x,H,tau_j}||_{2->2}
        * sup_{tau_j<=T} ||Y_x(tau_j)||_2 = O(1),             (ROP)

sup_{tau_j<=T} |m_{x,H,tau_j}Y_x(tau_j)| -> 0.                (MOP)
```

Then `(QMASS)` and `(QFLUX)` of E72.109 hold, hence post-main finite-band root transport follows.

### Proof

Immediate:

```text
Flux_x(H,tau_j)
 = ||R_{x,H,tau_j}Y_x(tau_j)||_2
 <= ||R_{x,H,tau_j}|| ||Y_x(tau_j)||_2.
```

The mass statement is `(MOP)`.  Apply E72.109. `QED`

## 2. Stronger but structural sufficient bound

The operator norm condition `(ROP)` can be split as:

```text
||Y_x(tau_j)||_2 = O(sqrt(x) A_x),

||T_HP_H^0W_HB_xC_E^(-1)B_x^*P_HL_{k_x,tau_j}||_{2->2}
   = O(L/A_x),
```

because of the prefactor `2/(L sqrt(x))` in `R`.

This is not meant as a final estimate; it identifies where the proof must use geometry:

```text
raw Chebyshev packet size          -> arithmetic;
shorted Loewner pushforward norm   -> CCM/Feshbach geometry.
```

The gain diagnostic of E72.111 indicates that the raw post-main source is not small, but the shorted
pushforward is.

## 3. Exact matrix form

Let `M_{x,H,tau}=R_{x,H,tau}^*R_{x,H,tau}`.  Then:

```text
FENERGY:
Y_x(tau_j)^*M_{x,H,tau_j}Y_x(tau_j)=O(1).
```

The remaining proof can now be attacked in either of two equivalent ways:

```text
direct quadratic form: prove Y^*MY=O(1);
operator split: prove ||M||^{1/2}||Y||=O(1).
```

The direct form is sharper.  The operator split is easier to falsify numerically.

## 4. Status

```text
proved: FENERGY is equivalent to bounded shorted pushforward energy;
proved: an operator-norm split is a sufficient finite criterion;
open:   prove the shorted pushforward bound or the sharper direct quadratic form.
```

## 5. Operator split diagnostic

The companion script:

```text
E72_112_operator_split_probe.py
```

constructs the matrix `R_{x,H,tau}` explicitly and verifies that its action reproduces the centered
flux.  Representative output:

```text
E72.112 operator split probe
 lam   N roots  max||Y||   max||R||   max prod   maxFlux2  relCheck
   6  18     3 3.830e+01 2.578e-02  9.873e-01 5.504e-02   4.1e-16
   8  24     4 5.914e+01 1.877e-02  1.110e+00 6.287e-02   3.8e-16
  10  28     3 8.708e+01 9.900e-03  8.620e-01 3.929e-02   3.9e-16
  12  32     4 1.227e+02 8.450e-03  1.037e+00 2.291e-02   7.8e-16
  14  36     4 1.378e+02 4.607e-03  6.349e-01 2.312e-02   1.7e-16
```

The raw frequency packet grows, but the shorted pushforward norm decreases enough that the product
stays `O(1)` in the tested windows.  The `relCheck` column verifies the matrix factorization to
roundoff.
