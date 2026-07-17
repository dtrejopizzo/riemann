# E72.109 -- Quadratic centered flux certificate

**Date:** 2026-07-09.
**Role:** convert the centered spectral divergence gate into explicit finite quadratic forms.

## 0. Key observation

E72.108 requires:

```text
|mass(phi)| -> 0,
h||Psi(phi)||_1 -> 0.
```

The second condition is stronger than necessary to prove directly.  In a fixed physical band
`0<=d<=H`, the number of mesh points is:

```text
M_H(x) = H/h+O(1) = HL/(2*pi)+O(1),
h=2*pi/L.
```

Therefore:

```text
h||Psi||_1 <= h sqrt(M_H)||Psi||_2
            <= sqrt(2*pi H/L)(1+o(1))||Psi||_2.              (L2GAIN)
```

Thus a uniform `l2` bound on the centered flux already gives the `l1` flux condition.

## 1. Finite operators

Let `W_H` be the map from the two-sided even band vector to the nonnegative weighted vector:

```text
(W_H phi)_0=phi_0,
(W_H phi)_n=2phi_n,       n>0, d_n<=H.
```

Let:

```text
1_H=(1,...,1)^T,
e_H=(0,...,0,1)^T.
```

Define the mass functional and endpoint-centering projection:

```text
m(phi)=1_H^T W_H phi,
P_H^0 y = y-(1_H^T y)e_H.
```

Let `T_H` be the lower cumulative matrix:

```text
(T_H y)_n=sum_{j=0}^n y_j,       0<=n<M_H.
```

For the post-main cofactor:

```text
phi_{x,H,tau}^{pm}
 = B_xC_E^(-1)c_{x,H}^{pm}(tau),
```

define:

```text
Mass_x(H,tau)
 := 1_H^T W_H B_xC_E^(-1)c_{x,H}^{pm}(tau),                  (QM)

Flux_x(H,tau)^2
 := ||T_HP_H^0W_HB_xC_E^(-1)c_{x,H}^{pm}(tau)||_2^2.          (QF)
```

Both are finite expressions in the same matrices as E72.106.

Equivalently:

```text
Mass_x(H,tau)=b_H^*C_E^(-1)c_{x,H}^{pm}(tau),
b_H=B_x^*W_H^T1_H,
```

and:

```text
Flux_x(H,tau)^2
 = c_{x,H}^{pm}(tau)^*
   C_E^(-1)B_x^*W_H^*(P_H^0)^*T_H^*T_HP_H^0W_HB_xC_E^(-1)
   c_{x,H}^{pm}(tau).
```

So the new target is a bordered determinant plus one positive quadratic form.

## 2. Quadratic centered flux theorem

### Theorem 72.109

Fix a physical band `H` and a finite root-height window `T`.  Suppose:

```text
sup_{tau_j<=T}|Mass_x(H,tau_j)| -> 0,                         (QMASS)
sup_{tau_j<=T}Flux_x(H,tau_j) = O(1),                         (QFLUX)
```

with the same estimates for the one `s`-derivative channel.  Then:

```text
sup_{s in K,tau_j<=T}|D2_x^{pm}(H,s;tau_j)| -> 0
```

for every compact Cauchy window `K`.

### Proof

By E72.108:

```text
|D2_x^{pm}|
 <= C_{K,H}|Mass_x(H,tau_j)|
    + C_{K,H}h||Psi_{x,H,tau_j}||_1.
```

The centered flux is:

```text
Psi_{x,H,tau_j}=T_HP_H^0W_Hphi_{x,H,tau_j}^{pm}.
```

Use `(L2GAIN)`:

```text
h||Psi||_1
 <= sqrt(2*pi H/L)(1+o(1))Flux_x(H,tau_j).
```

`(QMASS)` kills the mass term and `(QFLUX)` kills the flux term because `L->infty`.
The differentiated statement is identical. `QED`

## 3. New finite target

The hard theorem is now:

```text
Quadratic centered flux bound:
Mass_x(H,tau_j)->0,
Flux_x(H,tau_j)=O(1)
```

uniformly on finite root-height windows.

This is much sharper than E72.98 absolute `D2->0` and more realistic than E72.107 `l1` flux
smallness.  It asks for bounded cumulative energy after:

```text
post-main subtraction,
Feshbach shorting,
endpoint mass centering.
```

## 4. Why this is the right finite shape

The incoherent Chebyshev bound grows because it estimates every `sigma_n^E` separately.  The quadratic
certificate estimates the cumulative flux **after** the Loewner-Feshbach pairing has converted those
oscillatory coefficients into the actual cofactor seen by Cauchy tests.

The gain is geometric, not arithmetical:

```text
fixed physical band => h sqrt(M_H) ~ L^(-1/2).
```

The arithmetic content is isolated in:

```text
Mass_x(H,tau_j)->0,
Flux_x(H,tau_j)=O(1).
```

## 5. Status

```text
proved: MASS + uniform quadratic centered flux imply post-main D2->0;
proved: the certificate is finite and positive;
open:   prove QMASS and QFLUX from the Loewner-Feshbach equations.
```

## 6. First diagnostic

The companion script:

```text
E72_109_quadratic_flux_probe.py
```

computes the post-main cofactor, its mass, its centered flux `l2` norm, and the scaled quantity
`h sqrt(M_H)Flux`.

Representative output:

```text
E72.109 quadratic centered flux probe
 lam   N roots  max|D2pm|  max|mass|   max Flux2   max hsqrtMFlux2
   6  18     3  1.607e-02  9.332e-02   5.504e-02        1.930e-01
   8  24     4  8.291e-03  4.973e-02   6.287e-02        2.124e-01
  10  28     3  5.647e-03  4.051e-02   3.929e-02        1.199e-01
  12  32     4  4.960e-03  2.100e-02   2.291e-02        7.094e-02
```

This does not prove `(QMASS)` or `(QFLUX)`, but it supports the scaling: the quadratic flux is bounded
in the tested windows and the scaled Cauchy contribution decreases.  The centering is performed at
the physical-band endpoint, not at the last global mode.
