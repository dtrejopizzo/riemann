# E72.113 -- Operator final gate for scalar WRL annihilation

**Date:** 2026-07-09.
**Role:** package the current Phase 72 route into one finite operator criterion.

## 0. Finite objects

For each finite CCM window `x`, fixed physical band `H`, finite root `tau_j`, and compact Cauchy
window `K`, define:

```text
Y_x(tau_j)
 = (Ehat_x(tau_j-d_n),Ehat_x(tau_j+d_n),
    Ehat'_x(tau_j-d_n),Ehat'_x(tau_j+d_n))_{|d_n|<=H'},
```

with:

```text
Ehat_x(omega)=int_0^L exp(-i omega r)dE_x^leftarrow(r).
```

Let:

```text
R_{x,H,tau_j}
 := T_HP_H^0W_HB_xC_E^(-1)B_x^*P_H
    (2/(L sqrt(x)))L_{k_x,tau_j},
```

and:

```text
m_{x,H,tau_j}
 := 1_H^TW_HB_xC_E^(-1)B_x^*P_H
    (2/(L sqrt(x)))L_{k_x,tau_j}.
```

All these are finite matrix/vector expressions.  No limiting zeta zero is inserted.

## 1. Final finite gate

### Theorem 72.113

Assume the following three estimates.

```text
(CCGD)
lim_{H->infty} limsup_{x->infty} sup_{s in K}D1_x(H,s)=0.
```

For each fixed `H` and finite root-height window `T`:

```text
(MOP)
sup_{tau_j<=T}|m_{x,H,tau_j}Y_x(tau_j)| -> 0,
```

and:

```text
(ROP)
sup_{tau_j<=T}||R_{x,H,tau_j}||_{2->2} ||Y_x(tau_j)||_2 = O(1).
```

Assume the same two post-main estimates for the one `s`-derivative channel.  Then scalar WRL
resonance annihilation holds:

```text
x^rho L_x(s;x)-int_1^x u^rho partial_uL_x(s;u)du -> 0
```

on the two Cauchy heights.  Consequently the Phase 72 spectral-divisibility route to `Omega_7` closes
provided the standard finite CCM spectral convergence input holds.

### Proof

`(MOP)` is exactly the mass condition `(QMASS)` of E72.109.

By E72.112:

```text
Flux_x(H,tau_j)
 = ||R_{x,H,tau_j}Y_x(tau_j)||_2
 <= ||R_{x,H,tau_j}|| ||Y_x(tau_j)||_2.
```

Thus `(ROP)` is `(QFLUX)`.  E72.109 gives:

```text
D2_x^{pm}(H,s;tau_j)->0
```

uniformly on finite root-height windows.  E72.105 combines this post-main finite-band root transport
with `(CCGD)` to get post-main HPAC divisibility.  E72.68 then gives scalar WRL resonance
annihilation. `QED`

## 2. Equivalent direct quadratic form

The operator split can be replaced by the sharper finite identity:

```text
Y_x(tau_j)^*R_{x,H,tau_j}^*R_{x,H,tau_j}Y_x(tau_j)=O(1).      (DQF)
```

`(DQF)` is exactly the positive double discrepancy energy of E72.110 in frequency coordinates.

Thus the current endpoint has two equivalent finite forms:

```text
operator split:  ||R||||Y||=O(1),
direct energy:   Y^*R^*RY=O(1).
```

The direct energy is sharper; the operator split is easier to audit numerically.

## 3. What remains open

The remaining unproved content is now precisely:

```text
prove MOP and ROP/DQF,
prove or import CCGD for the Cauchy-channel physical tail.
```

Everything else in the Phase 72 route is an exact finite identity or a proved implication.

## 4. Status

```text
proved: CCGD + MOP + ROP imply scalar WRL resonance annihilation;
proved: MOP and ROP are finite matrix/vector estimates;
open:   prove those estimates uniformly, without zero input.
```
