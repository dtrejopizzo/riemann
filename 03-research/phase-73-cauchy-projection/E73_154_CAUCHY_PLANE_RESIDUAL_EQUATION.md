# E73.154 - Cauchy-plane residual equation

Date: 2026-07-12.

## 1. Purpose

E73.153 proves that the complete signed forced row is exactly the Cauchy
divisor row.  Thus the remaining target is

```text
H0-DIV_17:
|H_0(w)|+|H_0(-w)| <= C L^-17.
```

This note tests the next possible analytic mechanism: the action of the
finite operator `H_L` on the two-dimensional Cauchy plane

```text
Q_w:=span{q_w,q_-w},
q_w(n)=1/(w+i d_n),
q_-w(n)=1/(-w+i d_n).
```

## 2. Exact residual equation

Let

```text
q_j H_L = sum_{k=1}^2 a_{jk}(w) q_k + rho_j(w),
```

where `rho_j` is the least-squares residual against the row plane `Q_w`.

Pair this identity against the ground eigenvector:

```text
H_L xi_L=mu_L xi_L.
```

Writing

```text
h_1:=q_w xi_L=H_0(w),
h_2:=q_-w xi_L=H_0(-w),
r_j:=rho_j xi_L,
```

gives the exact finite system

```text
(mu_L I - A(w)) h = r,                         (1)
```

where `A(w)=(a_jk(w))`.

Therefore, if

```text
||(mu_L I-A(w))^-1|| <= C L^a
```

and

```text
||r|| <= C L^(-17-a),
```

then `H0-DIV_17` follows.

This avoids division by `mu_L`; the denominator is the Cauchy-plane action
matrix, not the tiny ground eigenvalue.

## 3. What the numerical probe says

The Cauchy plane is not almost invariant in row norm:

```text
||rho_j||/||q_j H_L|| ~= L^-1 to L^-2,
```

so a norm-small invariance theorem is false.

However, the residual evaluated on `xi_L`,

```text
rho_j xi_L,
```

is small in the same exponent range as `H_0(w)`.  Thus the plausible theorem
is not:

```text
rho_j is small as a row.
```

It is the evaluated residual estimate:

```text
|rho_1 xi_L|+|rho_2 xi_L| <= C L^(-17-a).       (RCE_17)
```

Together with invertibility of `mu I-A`, this proves `H0-DIV_17`.

## 4. Anti-circularity

Equation (1) is an identity.  It is circular if one proves `r` small by using
`h` small.

A non-circular proof must estimate `rho_j xi_L` directly from the explicit
finite Feshbach structure of `H_L` and the Cauchy rows.

This is close to the critical-cell route E73.138, but with one improvement:
the equation uses the two-dimensional Cauchy plane as the principal part, so
the tiny `mu_L` is not used as a divisor.

## 5. Updated frontier

The post-collapse chain is:

```text
RCE_17 + CPINV
=> H0-DIV_17
=> LDIV_17
=> CSV_17
=> Uniform GATE-73
=> scalar WRL
=> Omega_7.
```

where

```text
CPINV: ||(mu_L I-A(w))^-1|| <= C L^a,
RCE_17: ||(rho(w)xi_L)|| <= C L^(-17-a).
```

The next analytic question is whether `rho_j xi_L` has an explicit signed
Feshbach representation whose cancellation can be proved without appealing
to `H_0(w)` itself.
