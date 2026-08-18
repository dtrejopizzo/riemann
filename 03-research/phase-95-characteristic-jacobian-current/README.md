# Phase 95 - Characteristic Jacobian current

## 1. Objective

Eliminate the moving finite level from the bordered deformation by treating it
as an algebraic branch of the full characteristic determinant.

## 2. Main construction

Let

```text
chi(t,mu)=det(H_t-mu I)                               (2.1)
```

and let `P(t,mu,z)` be the global cofactor numerator of Phase 94 before
substitution of the selected level.  Along a simple branch
`chi(t,mu_t)=0`, the total derivative of `log P` is a determinant Jacobian
divided by `P partial_mu chi`.

## 3. Work order

```text
E95.001  two-parameter algebraic lift;
E95.002  characteristic Jacobian theorem;
E95.003  bilateral projective current;
E95.004  branch and chart audit;
E95.005  exact remaining determinant identity.
```

