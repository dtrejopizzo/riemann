# E72.27 -- Relative bordered Fredholm theorem

**Date:** 2026-07-08.
**Role:** state and prove the determinant convergence theorem that would turn the bordered pencil
identity into Schur-free current convergence.

## 0. Bordered pencils

From E72.26:

```text
P_x(s) = -det B_x(s),
B_x(s)= [ 0        xi_x^T ]
        [ 1_x      sI-D_x ].
```

Let `B_x^0(s)` be the corresponding prolate/model bordered pencil, built from the model vector and the
same pole mesh/gauge.

Define the relative bordered perturbation

```text
K_x(s) := (B_x(s)-B_x^0(s))(B_x^0(s))^(-1).
```

Then formally

```text
det B_x(s) = det B_x^0(s) det(I+K_x(s)).
```

The point is to make this a stable Fredholm statement.

## 1. Relative determinant theorem

### Theorem 72.27

Let `Omega` be a compact subset of the centered strip avoiding the model divisor. Assume:

1. `B_x^0(s)` is invertible on `Omega`;
2. `K_x(s)` is trace class on the bordered Hilbert space and depends holomorphically on `s`;
3. there exists a trace-class holomorphic limit `K(s)` such that

```text
sup_{s in Omega} ||K_x(s)-K(s)||_1 -> 0;          (TC)
```

4. the model determinants converge locally uniformly:

```text
det B_x^0(s) -> G(s);
```

5. the limiting relative determinant satisfies

```text
G(s) det(I+K(s)) = c Xi(s),        c != 0.        (ID)
```

Then:

```text
P_x(s)/P_x(0) -> Xi(s)/Xi(0)
```

locally uniformly on `Omega`, after the corresponding normalization. Consequently the finite divisor
currents converge to the `Xi` divisor current on `Omega`.

If this holds on an exhaustion of the strip, RH follows by E72.19.

### Proof

Trace-norm convergence `(TC)` implies uniform convergence of Fredholm determinants on `Omega`:

```text
det(I+K_x(s)) -> det(I+K(s)).
```

Using the determinant factorization,

```text
det B_x(s)
 = det B_x^0(s) det(I+K_x(s)).
```

Assumption 4 gives

```text
det B_x(s) -> G(s)det(I+K(s)).
```

By `(ID)`, the limit is `c Xi(s)`. Since `P_x=-det B_x`, normalization at `0` gives

```text
P_x(s)/P_x(0) -> Xi(s)/Xi(0).
```

Locally uniform convergence of holomorphic functions implies convergence of Poincare-Lelong divisor
currents. E72.19 then gives RH when the convergence holds on a strip exhaustion. `QED`

## 2. Current version

Differentiating the determinant identity gives

```text
P_x'/P_x
 = (det B_x^0)'/det B_x^0
   + Tr((I+K_x)^(-1)K_x').
```

Under `(TC)` and local invertibility away from zeros,

```text
P_x'/P_x -> Xi'/Xi
```

on two interior heights. Thus E72.22 also applies.

## 3. What remains nontrivial

The theorem is purely functional analytic. The arithmetic content is exactly:

```text
(A) construct B_x^0 from the prolate model in the same gauge;
(B) prove trace-norm convergence K_x -> K;
(C) identify G det(I+K) with Xi without inserting Xi as a definition.
```

The dangerous step is `(C)`. It is admissible only if it follows from the finite CCM construction and
Connes's prolate limit, not by defining `K` through `Xi/G`.

## 4. How this relates to the leakage route

The old leakage target tried to prove vector convergence:

```text
theta_x -> k_lambda.
```

The relative bordered theorem asks for trace-class convergence of a rank/bordered current perturbation.
This is lower resolution:

```text
determinant/current convergence can hold even when vector convergence is too strong.
```

It is therefore the strongest surviving candidate after E72.25.

## 5. Status

```text
proved: trace-norm relative bordered convergence + determinant identification => RH;
open:   prove the trace-norm convergence and determinant identification from CCM data.
```

The next proof attempt must estimate `K_x(s)` explicitly.
