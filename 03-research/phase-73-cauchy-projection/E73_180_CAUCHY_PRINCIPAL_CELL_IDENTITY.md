# E73.180 - Cauchy-principal cell identity

Date: 2026-07-14.

## 1. Purpose

E73.179 isolates the two-dimensional divisor system

```text
(mu_L I-A(w))h(w)=r(w).
```

E73.155 had already shown that the smallness of `r(w)` is a signed
model-prime cancellation.  This note writes the precise finite identity that
has to be proved analytically, without hiding the Cauchy principal part.

## 2. Principal cell identity

Let

```text
q_1=q_w,       q_2=q_-w,
h_k=q_k xi_L,
q_jH_L=sum_k A_jk(w)q_k + rho_j(w).
```

Then, pairing against `xi_L`,

```text
rho_j(w)xi_L
= q_jH_Lxi_L - sum_k A_jk(w) q_kxi_L.          (1)
```

This is the Cauchy-principal cell identity.  The first term is a finite
explicit-formula cell:

```text
q_jH_Lxi_L = A_L[B_j] - P_L[B_j],

B_j(y)=q_j Q_L(y) xi_L,
```

where `Q_L(y)` has entries `q_mn(y)`.  The second term subtracts the
two-dimensional Cauchy principal part.  It must not be discarded: it is the
block whose inverse in `(mu I-A)^(-1)` converts residual control into
`H_0(w)` control.

Thus the exact proof-facing residual is:

```text
R_j(w)
:= A_L[B_j]-P_L[B_j]-sum_k A_jk(w)H_k(w),
H_k(w)=q_kxi_L.                                  (2)
```

Equation (1) says:

```text
R_j(w)=rho_j(w)xi_L.
```

## 3. Model-prime split with principal subtraction

Write

```text
H_L=H_model,L-Prime_L.
```

For each part, project its Cauchy-plane action separately:

```text
q_jH_model,L=sum_k A^model_jk q_k+rho^model_j,
q_jPrime_L=sum_k A^prime_jk q_k+rho^prime_j.
```

Then

```text
rho_jxi_L
= rho^model_jxi_L-rho^prime_jxi_L
```

and explicitly

```text
rho^model_jxi_L
= q_jH_model,Lxi_L - sum_k A^model_jk h_k,

rho^prime_jxi_L
= q_jPrime_Lxi_L - sum_k A^prime_jk h_k.
```

This is the sharpened `SCRCE` theorem:

```text
SCRCE-principal:
|rho^model_jxi_L-rho^prime_jxi_L| <= C L^(-R-a).
```

Together with `CPINV`, it gives `H0-DIV_R`.

## 4. Anti-tautology

This identity still contains `h_k=q_kxi_L`, but not as an assumed-small
quantity.  The term `sum A_jk h_k` is the principal part of the finite cell
action; it is retained on the left side of the linear system

```text
(mu I-A)h=r.
```

The proof obligation is therefore:

```text
prove the residual after subtracting the Cauchy principal action is small.
```

It is not:

```text
prove h is small and substitute it back.
```

That distinction is exactly what avoids the E73.126 rowspace tautology.

## 5. Current analytic theorem

The finite theorem left by Phase 73 can now be stated without auxiliary
operators:

```text
For every critical standard-box node w=-i gamma and j=1,2,

| q_j(H_model,L-Prime_L)xi_L
  - sum_k (A^model_jk(w)-A^prime_jk(w)) q_kxi_L |
<= C L^(-R-a).
```

Here each term is explicit from:

```text
q_j(n)=1/(±w+i d_n),
H_model,L(m,n)=A_L[q_mn],
Prime_L(m,n)=P_L[q_mn],
xi_L=ground vector of H_L.
```

This is the current minimal analytic identity behind `CHAR-node`.

## 6. Status

```text
proved:   principal cell identity (1);
proved:   model-prime principal split;
reduced:  RCE-cell to SCRCE-principal + CPINV;
open:     prove SCRCE-principal uniformly from the explicit prime/Gamma cells.
```
