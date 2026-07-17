# E73.234 - Adjoint principal residual equivalence

Date: 2026-07-14.

## 1. Purpose

E73.233 rewrote the TRANS-CELL center as the paired commutator defect:

```text
qH(I-P)xi = <[I-P,H]q^* + mu(I-P)q^*, xi>.
```

This note expands that identity completely.  The conclusion is important:
the E73.233 paired commutator is not a new independent mechanism.  Because
`q^*` lies in the Cauchy row plane, it collapses exactly to the adjoint form
of the E73.180 Cauchy-principal residual.

This is good bookkeeping: it prevents the route from splitting into two names
for the same obstruction.

## 2. Collapse of the commutator defect

Let

```text
Q=(q_1;q_2),          P=Q^*(QQ^*)^(-1)Q,          R=I-P.
```

For `q=q_a`, one of the rows of `Q`, we have

```text
Pq^*=q^*,             Rq^*=0.                         (1)
```

Therefore the E73.233 defect

```text
D_q=[R,H]q^* + mu Rq^*
```

reduces to

```text
D_q=RHq^*.                                             (2)
```

Indeed,

```text
[R,H]q^* = RHq^* - HRq^* = RHq^*,
mu Rq^*=0.
```

Pairing with the ground vector gives

```text
<D_q,xi>=<RHq^*,xi>=qHRxi.                             (3)
```

This is exactly the TRANS-CELL center.

## 3. Equivalence with the principal residual

Write the Cauchy-plane projection of the row action as

```text
qH = A_q Q + rho_q,
```

where `rho_q Q^*=0`.  In matrix form,

```text
rho_q=qHR.
```

Taking adjoints gives

```text
rho_q^*=RHq^*=D_q.                                     (4)
```

Thus

```text
qH(I-P)xi = rho_q xi = <rho_q^*,xi> = <D_q,xi>.          (5)
```

So the E73.233 target

```text
|<[I-P,H]q^*,xi> + mu <(I-P)q^*,xi>| <= A_M L^-M
```

is exactly the E73.180/E73.181 target:

```text
|A_L[B_q]-P_L[B_q]-sum_k A_qk H_k| <= A_M L^-M.
```

The explicit packet is

```text
B_q(y)=q Q_L(y)xi,
H_k=q_k xi.
```

## 4. Final finite identity for U4

The center cancellation U4 is therefore equivalent to the following finite
principal residual estimate:

```text
APR-U4:
For every admissible Cauchy plane Q_w and row q_a,

|A_L[B_{a,w}]-P_L[B_{a,w}]
 - sum_{k=1}^2 A_{ak}(w) q_k xi_L|
<= A_M L^(-M).                                      (6)
```

Here

```text
A(w)=Q_wH_LQ_w^*(Q_wQ_w^*)^(-1)
```

and every term in (6) is finite:

```text
A_L      Gamma/archimedean finite functional;
P_L      prime-power finite functional;
B_{a,w}  finite packet built from q_a, Q_L(y), xi_L;
A(w)     2x2 Cauchy principal action;
q_k xi_L finite Cauchy values.
```

## 5. Consequence

The proof route should not branch into:

```text
commutator theorem
versus
principal residual theorem.
```

They are the same theorem.  The correct next work is to prove (6) by expanding
`A_L[B]-P_L[B]` and the principal subtraction into the coefficient/weight
language of E73.222--E73.230, then isolating the exact finite divisibility
responsible for the rapid scalar cancellation.

The false norm route remains false:

```text
||rho_q|| = ||RHq^*||
```

is much larger than `|rho_q xi|` in E73.233.  The only possible closure is
therefore an evaluated principal residual estimate, not an operator-norm
estimate.

## 6. Status

```text
proved: E73.233 paired commutator = adjoint E73.180 principal residual;
reduced: U4 = APR-U4 finite explicit principal residual estimate;
next: expand APR-U4 in coefficient/weight form and seek the finite
      divisibility identity inside the scalar center.
```

