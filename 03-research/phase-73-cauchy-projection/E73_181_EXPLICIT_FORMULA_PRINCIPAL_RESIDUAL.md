# E73.181 - Explicit-formula principal residual

Date: 2026-07-14.

## 1. Purpose

E73.180 states the surviving theorem as a Cauchy-principal cell identity.
This note removes the last matrix shorthand from the scalar cell term.

The object to prove is not merely

```text
q_jH_Lxi_L small.
```

It is the explicit-formula cell after subtracting its two-dimensional
Cauchy principal action:

```text
R_j(w)
= A_L[B_{j,w}] - P_L[B_{j,w}]
  - sum_k (A^model_jk(w)-A^prime_jk(w)) H_k(w).      (1)
```

Here

```text
B_{j,w}(y)=q_j Q_L(y)xi_L,
H_k(w)=q_kxi_L,
q_1=q_w, q_2=q_-w.
```

## 2. Exact explicit formula

The two functionals are:

```text
P_L[B] =
sum_{p^k<=exp(L)} (log p)p^(-k/2) B(k log p),
```

and

```text
A_L[B]
= int_0^L B(y)(e^(y/2)+e^(-y/2))dy
 - 1/2(log(4pi)+gamma)B(0)
 - int_0^L [e^(y/2)B(y)-B(0)]/[2sinh(y)]dy
 - 1/2 log(tanh(L/2))B(0).
```

At `y=0` the regularized integrand is the finite limit

```text
[B'(0)+B(0)/2]/2.
```

By the CCM entry definition,

```text
q_jH_model,Lxi_L = A_L[B_{j,w}],
q_jPrime_Lxi_L   = P_L[B_{j,w}].
```

Therefore (1) is exactly

```text
R_j(w)=rho_j(w)xi_L.
```

## 3. Minimal theorem

The current analytic theorem is:

```text
SCRCE-principal-explicit:
For every critical standard-box node w=-i gamma and j=1,2,

|A_L[B_{j,w}] - P_L[B_{j,w}]
 - sum_k (A^model_jk(w)-A^prime_jk(w))H_k(w)|
<= C L^(-R-a).
```

Together with

```text
||(mu_LI-A(w))^-1|| <= C L^a,
```

this gives

```text
H0-DIV_R => CHAR-node/CSV_R => scalar WRL.
```

## 4. What this buys

This is now a finite explicit-formula theorem:

```text
one smooth finite packet B_{j,w},
one prime-power sum P_L[B],
one Gamma/archimedean functional A_L[B],
one two-dimensional Cauchy principal correction.
```

No pseudoinverse, rowspace membership, root proximity, or global
characteristic convergence remains in the statement.

The theorem is still hard: the model and prime principal cells are not
separately small.  The proof must show the signed model-prime match after
the principal Cauchy subtraction.

## 5. Status

```text
proved:   matrix cell equals explicit A_L[B]-P_L[B];
proved:   SCRCE-principal can be stated as the scalar formula above;
open:     prove the scalar formula uniformly.
```
