# E72.23 -- Weyl log-current formula for two-height convergence

**Date:** 2026-07-08.
**Role:** express the finite divisor Cauchy transform `F_x'/F_x` directly from the finite CCM Weyl data
without constructing the numerator polynomial.

## 0. Finite Weyl data

Phase 71 identified the correct finite spectral carrier:

```text
m_x(s) = sum_k xi_{x,k}/(s-d_{x,k}),
d_{x,k}=2*pi*k/L_x.
```

Write

```text
Q_x(s)=prod_k (s-d_{x,k}),
m_x(s)=P_x(s)/Q_x(s).
```

The finite CCM divisor is the zero set of `P_x`. Thus the finite divisor current is controlled by

```text
P_x'(s)/P_x(s).
```

## 1. Exact log-current identity

### Lemma 72.23

On the complement of the pole mesh and the finite divisor,

```text
P_x'(s)/P_x(s)
  = m_x'(s)/m_x(s) + Q_x'(s)/Q_x(s).              (WLC)
```

Moreover,

```text
m_x'(s)/m_x(s)
 = - [sum_k xi_{x,k}(s-d_{x,k})^(-2)]
     /[sum_k xi_{x,k}(s-d_{x,k})^(-1)].
```

### Proof

Since `m_x=P_x/Q_x`,

```text
log P_x = log m_x + log Q_x
```

locally on every simply connected zero-free/pole-free region. Differentiating gives `(WLC)`.

The second formula follows by differentiating the finite sum defining `m_x`. `QED`

## 2. Pole mesh term

The pole mesh current is explicit:

```text
Q_x'(s)/Q_x(s)=sum_k 1/(s-d_{x,k}).
```

This is the finite sine-comb background. In the symmetric mesh limit it converges, after the standard
principal-value normalization, to the derivative of the sine background:

```text
sum_k 1/(s-2*pi*k/L_x)
  = (L_x/2) cot(L_x s/2)
```

for the infinite periodic mesh, with finite-window edge corrections.

E71.11 showed that this pole mesh alone is not the right full background, but `(WLC)` says it is still
one exact component of the current.

## 3. Two-height target in Weyl form

The THLC target from E72.22 becomes:

```text
int varphi(t)
[
  - S_{2,x}(t+i eta)/S_{1,x}(t+i eta)
  + sum_k 1/(t+i eta-d_{x,k})
  - Xi'(t+i eta)/Xi(t+i eta)
] dt -> 0,                                      (THLC-W)
```

where

```text
S_{1,x}(s)=sum_k xi_{x,k}/(s-d_{x,k}),
S_{2,x}(s)=sum_k xi_{x,k}/(s-d_{x,k})^2.
```

This formula uses only finite CCM data:

```text
D_x=(d_{x,k}),
xi_x.
```

No zero locations of `Xi` enter.

## 4. What must be proved

The finite current convergence splits into:

```text
mesh current + Weyl ratio current -> Xi log-current.
```

Thus the missing theorem is:

### Weyl two-height current convergence

For `eta != 0`, in distributions in `t`,

```text
- S_{2,x}(t+i eta)/S_{1,x}(t+i eta)
  + sum_k 1/(t+i eta-d_{x,k})
  -> Xi'(t+i eta)/Xi(t+i eta).                   (WTCC)
```

Together with local normal bounds for the left side in half-slabs, E72.22 and E72.19 imply RH.

## 5. Why this is better than root tracking

Root tracking asks where the zeros of `P_x` go. `(WTCC)` asks instead for convergence of the Cauchy
current of those zeros. This is lower resolution and may be accessible from the resolvent structure of
`xi_x`.

The finite vector `xi_x` is obtained as the lowest eigenvector of the explicit CCM matrix

```text
QW_x = arch_x - prime_x.
```

Therefore the next proof attempt must derive `(WTCC)` from the eigenvector equation

```text
QW_x xi_x = eps_x xi_x
```

without using the sign of `eps_x` or Weil positivity.

## 6. Status

```text
proved: exact finite formula for the divisor current in terms of Weyl data;
open:   prove WTCC and slab normal bounds from the finite CCM eigenvector equation.
```
