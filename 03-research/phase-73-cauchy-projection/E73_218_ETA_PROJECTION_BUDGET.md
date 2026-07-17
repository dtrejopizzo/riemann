# E73.218 - Cauchy projection radius budget

Date: 2026-07-14.

## 1. Purpose

E73.217 certifies the bordered eigenline ball `[xi,mu]`.  This note propagates
the eigenline radius through the Cauchy projection:

```text
eta_w=(I-P_w)xi.
```

## 2. Bound

If

```text
||xi-xi_0|| <= rho_xi,
```

then

```text
||eta_w-eta_{w,0}|| <= ||I-P_w|| rho_xi.
```

The projection is finite and explicit:

```text
P_w=Q_w^*(Q_wQ_w^*)^(-1)Q_w.
```

## 3. Status

```text
implemented: radius propagation from [xi] to [eta_w];
next: push [eta_w] through the final scalar A_L^digamma-P_L.
```

## 4. Result

For the tested windows and both Bernoulli-sector budgets `C_sec=1` and
`C_sec=10^6`, the computed operator norm satisfies

```text
||I-P_w||=1
```

to the displayed logarithmic precision.  Hence

```text
rho_eta <= rho_xi.
```

There is no hidden Cauchy-projection loss in the finite certificate chain.
