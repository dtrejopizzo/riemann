# Phase 86 - Signed spectral Abel reduction

## 1. Objective

Prove or sharply reduce the two signed parity sums left by Phase 85 while
preserving cancellation across the complementary spectrum.

## 2. Binding target

For each parity channel, order the complementary eigenvalues and prove that

```text
coefficient times
sum_q safe_weight_q Delta_P(lambda_q) -> 0             (2.1)
```

locally uniformly on safe sets, with one derivative.

## 3. Restrictions

```text
- no termwise bound on Delta_P(lambda_q);
- no maximum-partial-sum estimate is accepted without scale verification;
- endpoints in Abel summation are retained;
- the parity channels remain separate on the imaginary axis;
- any identification with historical scalar WRL is made explicitly.
```

## 4. Work order

```text
E86.001  exact finite Abel identity.
E86.002  crude ceiling autopsy.
E86.003  variation-weighted return criterion.
E86.004  first complementary mode and lower-variation tail.
```
